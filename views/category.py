from flask import Blueprint, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category = Blueprint('category', __name__)

# Category Index
@category.route('/categories')
def categoryIndex():
	categories = session.query(Category).all()
	return render_template('categories/index.html', categories=categories)

# Category Show
@category.route('/categories/<int:category_id>')
def categoryShow(category_id):
	category = session.query(Category).filter_by(id=category_id).one()
	categoryItems = session.query(CategoryItem).filter_by(category_id=category.id).all()
	return render_template('categories/show.html', category_id = category_id, category=category, categoryItems=categoryItems)