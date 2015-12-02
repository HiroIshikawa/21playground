import requests

from flask import Flask, request

from two1.lib.wallet import Wallet
from two1.commands.config import Config
from two1.lib.bitserv.flask import Payment
from two1.lib.bitrequests import BitTransferRequests

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)
bit_requests = BitTransferRequests(wallet, Config().username)

in_msg_url = "https://hooks.slack.com/services/---/---/---"

result == ""

@app.route('/from')
@payment.required(1000)
def send_translation_request():

	text = request.args.get('text')

	payload = {"channel":"#translation", "username": "request", "text": text}

	r = requests.post(in_msg_url, json=payload)

	print('Request sent...!')
	print('Translating...')


@app.route('/to', methods=['GET','POST'])
def receive_translation_result():
	
	if request.methods == 'GET':
		return result

	if request.method == 'POST':
		data = request.data
		dataDict = json.loads(data)

		result = dataDict.get('text', default='Not found')

		print "Received"


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)