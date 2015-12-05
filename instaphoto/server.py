
import json
import requests
from pprint import pprint
from flask import Flask,render_template

app = Flask(__name__)

# USER_ID = '485679741'
ACCESS_TOKEN = '485679741.1d8a980.7bacc3e0264640d59c63171106b23725'

@app.route('/')
def index():
	resp = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=' + ACCESS_TOKEN)

	data = json.loads(resp.text)['data']
	#pprint(data)

	for el in data:
		pprint(el['images']['standard_resolution']['url'])
	
	#pics = data[""]
	#pprint(pics)
	return render_template('index.html')

if __name__ == '__main__':
	app.run()