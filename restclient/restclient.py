#!/usr/bin/env python

import sys
import os
import requests



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
	
	def __init__(self, format="json", good_status_codes=[200,201], ssl_verify=True, timeout=0.03):
		self.format = format
		self.good_status_codes = good_status_codes
		self.ssl_verify = ssl_verify
		self.timeout = timeout

	def get(self, url):
		result = None
		try:
			response = requests.get(url, verify=self.ssl_verify, timeout=self.timeout)
		except requests.exceptions.ConnectionError as e:
			raise RestError("cannot connect to: %s" % url), None, sys.exc_info()[2]
		except requests.exceptions.Timeout as e:
			raise RestError("connection timed out to: %s after %s seconds" % (url, self.timeout) ), None, sys.exc_info()[2]
		except Exception as e:
			raise RestError(e.message), None, sys.exc_info()[2]

		if response.status_code not in self.good_status_codes:
			raise RestError("bad status code: %s - %s" % (response.status_code, response.reason) )

		if self.is_format_json():
			result = response.json()
		else:
			result = response.text()

		return result

	def post(self, url, payload):
		result = None
		try:
			if self.is_format_json():
				response = requests.post(url, verify=self.ssl_verify, timeout=self.timeout, json=payload)
			else:
				response = requests.post(url, verify=self.ssl_verify, timeout=self.timeout, data=payload)
		except requests.exceptions.ConnectionError as e:
			raise RestError("cannot connect to: %s" % url), None, sys.exc_info()[2]
		except requests.exceptions.Timeout as e:
			raise RestError("connection timed out to: %s after %s seconds" % (url, self.timeout) ), None, sys.exc_info()[2]
		except Exception as e:
			raise RestError(e.message), None, sys.exc_info()[2]

		if response.status_code not in self.good_status_codes:
			raise RestError("bad status code: %s - %s" % (response.status_code, response.reason) )

		if self.is_format_json():
			result = response.json()
		else:
			result = response.text()

		return result

	def is_format_json(self):
		if (self.format == "json"):
			return True
		return False

