from flask import Flask, request, make_response

app = Flask(__name__)

# reading cookies
@app.route('/read')
def index():
	username = request.cookies.get('username')


# storing cookies
@app.route('/store')
def index():
	resp = make_response(render_template(...))
	resp.set_cookie('username', 'the username')
	return resp