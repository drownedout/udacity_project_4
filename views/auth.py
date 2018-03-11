from flask import Blueprint, render_template, session, request, make_response
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from util.keys import google_client_id
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User
import random, string, httplib2, json, requests

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()

CLIENT_ID = json.loads(open('secrets.json', 'r').read())['web']['client_id']

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	# Create a state token to prevent forgery
	# Stored in session for later validation
	# State is set to a randomly generate string of 32 characters, ints 
	state = ''.join(random.choice(string.ascii_uppercase + string.digits)
					for x in range(32))
	session['state'] = state
	return render_template('/auth/login.html', google_client_id=google_client_id, state=state)


@auth.route('/gconnect', methods=['POST'])
def gconnect():
	if request.args.get('state') != session['state']:
		response = make_request(json.dumps('Invalid State'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Obtain auth code
	code = request.data

	try:
		oauth_flow = flow_from_clientsecrets('secrets.json', scope="")
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(json.dumps('Failed to update auth code'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])

	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'
		return response

	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(
		json.dumps("Token's user ID doesn't match given user ID."), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	if result['issued_to'] != google_client_id:
		response = make_response(
		json.dumps("Token's client ID does not match app's."), 401)
		print("Token's client ID does not match app's.")
		response.headers['Content-Type'] = 'application/json'
		return response
	stored_access_token = session.get('access_token')
	stored_gplus_id = session.get('gplus_id')

	if stored_access_token is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps('Current user is already connected.'),
			                     200)
		response.headers['Content-Type'] = 'application/json'
		print('You are already signed in')
		return response

	# Store the access token in the session for later use.
	print(credentials.access_token)
	
	session['access_token'] = credentials.access_token
	session['gplus_id'] = gplus_id
	

	# Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt': 'json'}
	answer = requests.get(userinfo_url, params=params)
	data = answer.json()

	session['username'] = data['name']
	session['picture'] = data['picture']
	session['email'] = data['email']

	user_id = getUserID(data['email'])
	if not user_id or user_id == None:
		user_id = userNew(session)
	session['user_id'] = user_id

	return 'OK'

@auth.route('/gdisconnect')
def gdisconnect():
	# Only disconnect a connected user
	access_token = session.get('access_token')
	if access_token is None:
		response = make_response(json.dumps('Current user not connected'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	print(session['username'])
	print(session)
	# Execute an HTTP 'GET' request to revoke current token
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	print(url)
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]
	print(result)

	if result['status'] == '200':
		# Reset the user's session
		del session['access_token']
		del session['gplus_id']
		del session['username']
		del session['email']
		del session['picture']

		# Reponse indicating to user that session has been disconnected
		response = make_response(json.dumps('Successfully disconnected'), 200)
		response.headers['Content-Type'] = 'application/json'
		return render_template('/auth/logout.html')
	else:
		# In case something went wrong with disconnecting
		response = make_response(json.dumps('Failed to disconnect'), 400)
		response.headers['Content-Type'] = 'application/json'
		return response

# Helper functions
def userNew(session):
	newUser = User(name=session['username'], email=session['email'], picture=session['picture'])

	database_session.add(newUser)
	database_session.commit()
	user = database_session.query(User).filter_by(id=newUser.id).one()
	return user.id


def getUserInfo(user_id):
	user = database_session.query(User).filter_by(id=user_id).one()
	return user

def getUserID(email):
	try:
		user = session.query(User).filter_by(email=email).one()
		return user.id
	except:
		return None