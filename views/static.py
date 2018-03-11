from flask import Blueprint, render_template, redirect, request, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()

static = Blueprint('static', __name__)

# Root, Home
@static.route('/')
def home():
	categories = database_session.query(Category).all()
	categoryItems = database_session.query(CategoryItem).limit(8).all()
	return render_template('home.html', categories=categories, categoryItems=categoryItems)