import json
import requests
import urllib.request
import os
import random

from pprint import pprint

from flask import Flask, render_template, request, send_from_directory

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment


app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# directory of the digital content we'd like to sell
dir_path = '/home/twenty-server/instagram-server/images'

# get a list of the files in the dir
file_list = os.listdir(dir_path)

# simple content model: dictionary of filew w/ prices
files = {}
for file_id in range(len(file_list)):
	files[file_id+1] = file_list[file_id], random.randrange(1, 20)


<<<<<<< HEAD
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
=======
ACCESS_TOKEN = 'YOUR ACCESS TOKEN HERE'
>>>>>>> dfdea4a79f885a1735f36e8ae4bf8e5516891322


# end point to initiate photo garelley
@app.route('/update')
def update_images():
	os.chdir('/home/twenty-server/instagram-server/images')
	resp = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=' + ACCESS_TOKEN)

	data = json.loads(resp.text)['data']

	i = 0
	for el in data:
<<<<<<< HEAD
		i = i+1
		photo_url = el['images']['standard_resolution']['url']
		pprint(photo_url)
		urllib.request.urlretrieve(photo_url, '%d.jpg' % (i))
	return render_template('updated.html')

# endpoint to show current abailable photos
@app.route('/show')
def show_images():
	filename = './images/1.jpg'
	return render_template('show.html', filename=filename)

# endpoint to look up images to buy
@app.route('/files')
def file_lookup():
	return json.dumps(files)

# return the price of the selected file
def get_price_from_request(request):
	id = int(request.args.get('selection'))
	return files[id][1]

# machine-payable endpoint that returns selected file if payment succeed
@app.route('/buy')
@payment.required(get_price_from_request)
def buy_file():

	# extract selection from client request
	sel = int(request.args.get('selection'))

	# check if selection is valid
	if(sel < 1 or sel > len(file_list)):
		return 'Invalid selection.'
	else:
		return send_from_directory(dir_path, file_list[int(sel)-1])


if __name__ == '__main__':
	app.run(debug='true')
=======
		pprint(el['images']['standard_resolution']['url'])
	
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
>>>>>>> dfdea4a79f885a1735f36e8ae4bf8e5516891322
