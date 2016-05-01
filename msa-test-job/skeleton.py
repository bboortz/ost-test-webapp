#!/usr/bin/env python

import sys
import os
from datetime import datetime
from pprint import pprint
import requests
import json



class RestError(Exception):
        def __init__(self):
                self.value = "UNKNOWN ERROR"

        def __init__(self, value):
                if value == None:
                        value = "UNKNOWN ERROR"
                self.value = value

        def __str__(self):
                return repr(self.value)


class RestClient():
	
	def __init__(self, format="json", good_status_codes=[200,201], ssl_verify=True):
		self.format = format
		self.good_status_codes = good_status_codes
		self.ssl_verify = ssl_verify

	def get(self, url):
		result = None
		try:
			response = requests.get(url, verify=self.ssl_verify)
		except requests.exceptions.ConnectionError as e:
			raise RestError("cannot connect to: %s" % url), None, sys.exc_info()[2]
		except Exception as e:
			raise RestError(), None, sys.exc_info()[2]

		if response.status_code not in self.good_status_codes:
			raise RestError("bad status code: %s" % response.status_code)

		if self.is_format_json():
			result = response.json()
		else:
			result = response.text()

		return result

	def post(self, url):
		pass

	def is_format_json(self):
		if (self.format == "json"):
			return True
		return False



def main():
	# This allows us to use a plain HTTP callback
	os.environ['DEBUG'] = "1"
	rc = RestClient(ssl_verify=False)

	try:
		result = rc.get("https://localhost:9090/api/test")
		pprint(result)
	except Exception as e:
		print e.value



if __name__ == '__main__':
	main()

