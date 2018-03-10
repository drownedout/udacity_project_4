from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_assets import Bundle, Environment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

# Importing routes
from views.static import static
from views.category import category
from views.category_item import categoryItem

# Intializing app, blueprints
app = Flask(__name__)
app.register_blueprint(static)
app.register_blueprint(category)
app.register_blueprint(categoryItem)

# Assets
assets = Environment(app)
css = Bundle('css/style.css', 'css/normalize.css', output='gen/main.css')
assets.register('main', css)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)