from flask import Flask, render_template
from flask_assets import Bundle, Environment
app = Flask(__name__)

# Assets
assets = Environment(app)
css = Bundle('css/style.css', output='gen/main.css')

assets.register('main', css)

# Root
@app.route('/')
def index():
	return render_template('index.html')

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