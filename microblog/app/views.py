from flask import render_template, flask, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
							title='Sign In',
							form=form)