#!/usr/bin/python3
import requests
import csv

api_key = "KCCEK7NQHS377BWD"
url = "https://www.alphavantage.co/query?"

querystring = {
				"outputsize":"full",
				"datatype":"csv",
				"symbol":"BTC-USD",
				"function":"TIME_SERIES_INTRADAY",
				"interval":"1min",
				"apikey":api_key
				}

response = requests.request("GET", url, params=querystring)
res = response.text

with open('dataset.csv', 'a') as csvfile:
	file = csvfile.write(res)
