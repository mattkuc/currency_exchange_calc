from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


currency = input("Provide currency code: ")
url = "https://api.nbp.pl/api/exchangerates/rates/c/{}/today/".format(currency)

response = requests.get(url)
data = response.json()
exchange_rate = data['rates']['rate']['Bid']


