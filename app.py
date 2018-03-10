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
	categories = session.query(Category).all()
	categoryItems = session.query(CategoryItem).limit(8).all()
	return render_template('home.html', categories=categories, categoryItems=categoryItems)

# Category Index
@app.route('/categories')
def categoryIndex():
	categories = session.query(Category).all()
	return render_template('categories/index.html', categories=categories)

# Item Index
@app.route('/items')
def categoryItemIndex():
	categoryItems = session.query(CategoryItem).all()
	return render_template('categoryItems/index.html', categoryItems=categoryItems)

# Item New
@app.route('/items/new')
def categoryItemNew():
	pass

# Item Show
@app.route('/items/<int:item_id>')
def categoryItemShow():
	pass

# Item Edit
@app.route('/items/<int:item_id>/edit')
def categoryItemEdit():
	pass

# Item Delete
@app.route('/items/<int:item_id>/delete')
def categoryItemDelete():
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)