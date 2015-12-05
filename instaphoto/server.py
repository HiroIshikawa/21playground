
import json
import requests
from pprint import pprint
from flask import Flask,render_template

app = Flask(__name__)

ACCESS_TOKEN = 'YOUR ACCESS TOKEN HERE'

@app.route('/')
def index():
	resp = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=' + ACCESS_TOKEN)

	data = json.loads(resp.text)['data']

	for el in data:
		pprint(el['images']['standard_resolution']['url'])
	
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
