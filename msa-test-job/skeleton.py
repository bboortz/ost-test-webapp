#!/usr/bin/env python

import sys
import os
from restclient import RestClient
from pprint import pprint




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

