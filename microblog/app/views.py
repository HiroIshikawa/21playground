from flask import 
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Tak'} # fake user
	posts = [
	{
		'author': {'nickname': 'Tak'},
		'body': 'Beautiful day in Tokyo!'
	},
	{
		'author': {'nickname': 'Susan'},
		'body': 'This is it!'
	}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)