from flask import Blueprint, render_template, redirect, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categoryItem = Blueprint('categoryItem', __name__)

# Item Index
@categoryItem.route('/items')
def categoryItemIndex():
	categoryItems = session.query(CategoryItem).all()
	return render_template('categoryItems/index.html', categoryItems=categoryItems)

# Item New
@categoryItem.route('/items/new', methods=['GET', 'POST'])
def categoryItemNew():
	categories = session.query(Category).all()
	if request.method == 'POST':
		newCategoryItem = CategoryItem(name=request.form['name'], description=request.form['description'],
			category_id = request.form['category_id'])
		session.add(newCategoryItem)
		session.commit()
		return redirect(url_for('categoryItem.categoryItemShow', category_id=newCategoryItem.category_id, item_id = newCategoryItem.id))
	else:
		return render_template('categoryItems/new.html', categories=categories)

# Item Show
@categoryItem.route('/categories/<int:category_id>/<int:item_id>')
def categoryItemShow(category_id, item_id):
	categoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
	return render_template('categoryItems/show.html', category_id = category_id, item_id = item_id, categoryItem = categoryItem)

# Item Edit
@categoryItem.route('/categories/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def categoryItemEdit(category_id, item_id):
	editCategoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
	categories = session.query(Category).all()

	if request.method == 'POST':
		if request.form['name']:
			editCategoryItem.name = request.form['name']
		if request.form['description']:
			editCategoryItem.description = request.form['description']
		if request.form['category_id']:
			editCategoryItem.category_id = request.form['category_id']
		session.add(editCategoryItem)
		session.commit()
		return redirect(url_for('categoryItem.categoryItemShow', category_id=editCategoryItem.category_id, item_id = editCategoryItem.id))
	else:
		return render_template('categoryItems/edit.html', category_id=category_id, item_id = item_id, editCategoryItem = editCategoryItem, categories=categories)

# Item Delete
@categoryItem.route('/categories/<int:category_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def categoryItemDelete(category_id, item_id):
	deletedCategoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
	if request.method == 'POST':
		session.delete(deletedCategoryItem)
		session.commit()
		return redirect(url_for('categoryItem.categoryItemIndex'))
	else:
		return render_template('categoryItems/show.html', category_id=category_id, item_id = item_id, CategoryItem = deletedCategoryItem)