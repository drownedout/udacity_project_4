from flask import Flask, render_template
app = Flask(__name__)

from flask_assets import Bundle, Environment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Assets
assets = Environment(app)
css = Bundle('css/style.css', 'css/normalize.css', output='gen/main.css')
assets.register('main', css)

# Root
@app.route('/')
def home():
	category = session.query(Category).first()
	return render_template('home.html', category=category)

# Category Index
@app.route('/categories')
def categoryIndex():
	pass

# Item Index
@app.route('/items')
def itemIndex():
	pass

# Item New
@app.route('/items/new')
def itemNew():
	pass

# Item Show
@app.route('/items/<int:item_id>')
def itemShow():
	pass

# Item Edit
@app.route('/items/<int:item_id>/edit')
def itemEdit():
	pass

# Item Delete
@app.route('/items/<int:item_id>/delete')
def itemDelete():
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)