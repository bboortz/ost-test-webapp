#!/usr/bin/env python

import sys
import os
from restclient import RestClient, RestError
from pprint import pprint




def main():
	# This allows us to use a plain HTTP callback
	os.environ['DEBUG'] = "1"
	rc = RestClient(ssl_verify=False)

	try:
		for i in range(1,1000):
			result = rc.get("https://localhost:9090/api/test")
			pprint(result)
			result = rc.post("https://localhost:9091/api/info", payload=result)
			pprint(result)
	except RestError as e:
		print e.value
	except Exception as e:
		print e



if __name__ == '__main__':
	main()

