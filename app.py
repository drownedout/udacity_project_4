from flask import Flask
from flask_assets import Bundle, Environment

# Importing routes
from views.static import static
from views.auth import auth
from views.category import category
from views.category_item import categoryItem
from views.api import api

# Intializing app
app = Flask(__name__)
app.config.from_object('config')

# Blueprints
app.register_blueprint(static)
app.register_blueprint(auth)
app.register_blueprint(category)
app.register_blueprint(categoryItem)
app.register_blueprint(api)

# Assets
assets = Environment(app)
css = Bundle(
    'css/style.css',
    'css/normalize.css',
    'css/fontawesome-all.min.css',
    output='gen/main.css')
assets.register('main', css)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
