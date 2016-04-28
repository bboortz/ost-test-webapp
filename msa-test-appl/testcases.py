#!/usr/bin/env python

import sys
import os
import time
import json
import unittest
from pprint import pprint


def store_result(f):

	"""
	Store the results of a test
	On success, store the return value.
	On failure, store the local variables where the exception was thrown.
	"""
	def wrapped(self):
		start_time = time.time()
		if 'results' not in self.__dict__:
			self.results = {}
		# If a test throws an exception, store local variables in results:
		try:
			result = f(self)
		except Exception as e:
			runtime = time.time() - start_time
			if not hasattr(e, 'value'):
				self.results[f.__name__] = {'testcase': f.__name__, 'success':False, 'message': 'UNKNOWN ERROR', 'runtime': runtime}
			else:
				self.results[f.__name__] = {'testcase': f.__name__, 'success':False, 'message': e.value, 'runtime': runtime}
			return
		runtime = time.time() - start_time
		self.results[f.__name__] = {'testcase': f.__name__, 'success':True, 'result':result, 'runtime': runtime}
		return result
	return wrapped



def test_assert(condition, message=None):
	if not condition:
		raise TestError(message)


# Exception Type
class TestError(Exception):
        def __init__(self):
                self.value = "UNKNOWN ERROR"

        def __init__(self, value):
		if value == None:
			value = "UNKNOWN ERROR"
                self.value = value

        def __str__(self):
		return repr(self.value)
		

# Test Cases
class TestSequence(unittest.TestCase):

	def setUp(self):
		pass

	@store_result
	def test1_success(self):
		test_assert(1 == 1, "cannot calculate")
		return "SUCCESS"

	@store_result
	def test2_fail(self):
		self.assertEqual(1, 2)
		test_assert(1 == 2, "cannot calculate")
		return "SUCCESS"

	@store_result
	def test3_fail(self):
		test_assert(1 == 2)
		return "SUCCESS"

	@store_result
	def test4_success(self):
		test_assert(1 == 1, "cannot calculate")
		return "SUCCESS"




class TestCases():

	def __init__(self, show_errors_only=False):
		self.suite = None
		self.devnull = sys.stderr = open(os.devnull, 'w')
		self.show_errors_only = show_errors_only

	def run(self):
		self.suite = unittest.TestLoader().loadTestsFromTestCase(TestSequence)
		unittest.TextTestRunner(stream=self.devnull, verbosity=0).run(self.suite)

	def get_results(self):
		"""
		Get all the results from a test suite
		"""

		test_count = 0
		fail_count = 0
		ans = {}

		for test in self.suite:
			if 'results' in test.__dict__:
				test_count += 1
				if not test.results.itervalues().next()['success']:
					fail_count += 1
				else:
					if self.show_errors_only:
						continue
				ans.update(test.results)

		result = {'summary': { 'tests': test_count, 'failed': fail_count  }, 'results': ans }
		return result


	def print_results(self):
		pprint(self.get_results())





