from flask import Flask, render_template, request, redirect, url_for, jsonify
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
@app.route('/items/new', methods=['GET', 'POST'])
def categoryItemNew():
	categories = session.query(Category).all()
	if request.method == 'POST':
		newCategoryItem = CategoryItem(name=request.form['name'], description=request.form['description'],
			category_id = request.form['category_id'])
		session.add(newCategoryItem)
		session.commit()
		return redirect(url_for('categoryItemShow', category_id=newCategoryItem.category_id, item_id = newCategoryItem.id))
	else:
		return render_template('categoryItems/new.html', categories=categories)

# Item Show
@app.route('/categories/<int:category_id>/<int:item_id>')
def categoryItemShow(category_id, item_id):
	categoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
	return render_template('categoryItems/show.html', category_id = category_id, item_id = item_id, categoryItem = categoryItem)

# Item Edit
@app.route('/categories/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def categoryItemEdit(category_id, item_id):
	editCategoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
	categories = session.query(Category).all()

	if request.method == 'POST':
		if requst.form['name']:
			editCategoryItem.name = request.form['name']
		if requst.form['description']:
			editCategoryItem.description = request.form['description']
		if requst.form['category_id']:
			editCategoryItem.category_id = request.form['category_id']
		session.add(editCategoryItem)
		session.commit()
		return redirect(url_for('categoryItemShow', category_id=editCategoryItem.category_id, item_id = editCategoryItem.id))
	else:
		return render_template('categoryItems/edit.html', category_id=category_id, item_id = item_id, editCategoryItem = editCategoryItem, categories=categories)

# Item Delete
@app.route('/items/<int:item_id>/delete')
def categoryItemDelete():
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)