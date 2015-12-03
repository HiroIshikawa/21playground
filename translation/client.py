import json
import urllib.parse
import os

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)


def translate():

    print("--Generate bitcoin-powered digital artwork--")

    message = input("Please enter the sentence you want to translate: ")

    # call the machine-payable endpoint
    response = requests.get(url='http://localhost:8080/from?text='+message)

    response = requests.get(url='http://localhost:8080/to')

    print("Response: ")
    print(response)
    print('Translation completed')

if __name__ == '__main__':
    translate()
