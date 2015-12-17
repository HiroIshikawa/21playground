from flask import render_template, flash, redirect
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
	if form.validate_on_submit():
		flash('Login requested for OponID="%s", remember_me=%s' % 
			(form.openid.data,str(form.remember_me.data)))
		return redirecr('/index')
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])