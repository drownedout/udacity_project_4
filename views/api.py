from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

api = Blueprint('api', __name__)

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()


# Categories JSON endpoint

@api.route('/api/categories')
def categoryJSON():
	# Query DB
    categories = database_session.query(Category).all()
    # Return JSON
    return jsonify(categories=[category.serialize for category in categories])


# Category Items (Items) JSON endpoint

@api.route('/api/items')
def categoryItemJSON():
    categoryItems = database_session.query(CategoryItem).all()
    return jsonify(categoryItems=[item.serialize for item in categoryItems])
