#!/usr/bin/env python

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import sys
import os
import time
from restclient.restclient import RestClient, RestError
from pprint import pprint




def main():
	# This allows us to use a plain HTTP callback
	os.environ['DEBUG'] = "1"
	rc = RestClient(ssl_verify=False)

	try:
		result = {
			"date": time.time(),
			"results": {
			},
			"summary": {
				"failed": 1,
				"runtime": 0.0004849433898925781,
				"tests": 4
			}
		}
		result = rc.post("https://localhost:9091/api/info", payload=result)
		pprint(result)
	except RestError as e:
		print e.value
	except Exception as e:
		print e



if __name__ == '__main__':
	main()

