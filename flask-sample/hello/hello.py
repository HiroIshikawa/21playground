from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

# simple routing example
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




if __name__ == '__main__':
	app.run()