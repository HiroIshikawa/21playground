from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

# simple routing example
# the trailing slash is matter
#  if you accee ~/hello/ here, it will produce 404 error
@app.route('/hello')
def hello():
	return 'Hello!'

# routing with argument
@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

# routing with type defined argument
@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %s' % post_id 

# by default, a route only accept GET request
# methods are polymorphism tools
# it enables a noun (resource / URL) to behave in multiple way
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else
		show_the_login_form()




if __name__ == '__main__':
	app.run()