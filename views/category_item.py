from flask import Blueprint, render_template, redirect, request, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()

categoryItem = Blueprint('categoryItem', __name__)

# Item Index
@categoryItem.route('/items')
def categoryItemIndex():
	categoryItems = database_session.query(CategoryItem).all()
	return render_template('categoryItems/index.html', categoryItems=categoryItems)

# Item New
@categoryItem.route('/items/new', methods=['GET', 'POST'])
def categoryItemNew():
	try:
		if session['username']:
			categories = database_session.query(Category).all()
			user = database_session.query(User).filter_by(id=session['user_id']).one()

			if request.method == 'POST':
				newCategoryItem = CategoryItem(name=request.form['name'], description=request.form['description'],
					category_id = request.form['category_id'], user_id = user.id)
				database_session.add(newCategoryItem)
				database_session.commit()
				return redirect(url_for('categoryItem.categoryItemShow', category_id=newCategoryItem.category_id, item_id = newCategoryItem.id))
			else:
				return render_template('categoryItems/new.html', categories=categories)
	except:
		return redirect(url_for('auth.login'))

# Item Show
@categoryItem.route('/categories/<int:category_id>/<int:item_id>')
def categoryItemShow(category_id, item_id):
	categoryItem = database_session.query(CategoryItem).filter_by(id=item_id).one()
	return render_template('categoryItems/show.html', category_id = category_id, item_id = item_id, categoryItem = categoryItem)

# Item Edit
@categoryItem.route('/categories/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def categoryItemEdit(category_id, item_id):
	try:
		if session['username']:
			editCategoryItem = database_session.query(CategoryItem).filter_by(id=item_id).one()
			categories = database_session.query(Category).all()
			if session['user_id'] != editCategoryItem.user_id:
				return redirect(url_for('categoryItem.categoryItemShow', category_id=editCategoryItem.category_id, item_id = editCategoryItem.id))
			if request.method == 'POST':
				if request.form['name']:
					editCategoryItem.name = request.form['name']
				if request.form['description']:
					editCategoryItem.description = request.form['description']
				if request.form['category_id']:
					editCategoryItem.category_id = request.form['category_id']
				database_session.add(editCategoryItem)
				database_session.commit()
				return redirect(url_for('categoryItem.categoryItemShow', category_id=editCategoryItem.category_id, item_id = editCategoryItem.id))
			else:
				return render_template('categoryItems/edit.html', category_id=category_id, item_id = item_id, editCategoryItem = editCategoryItem, categories=categories)
	except:
		return redirect(url_for('auth.login'))

# Item Delete
@categoryItem.route('/categories/<int:category_id>/<int:item_id>/delete', methods=['POST'])
def categoryItemDelete(category_id, item_id):
	if not session['username']:
		redirect(url_for('auth.login'))
	deletedCategoryItem = database_session.query(CategoryItem).filter_by(id=item_id).one()
	if request.method == 'POST':
		database_session.delete(deletedCategoryItem)
		database_session.commit()
		return redirect(url_for('categoryItem.categoryItemIndex'))
	else:
		return render_template('categoryItems/show.html', category_id=category_id, item_id = item_id, CategoryItem = deletedCategoryItem)