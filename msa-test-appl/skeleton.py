#!/usr/bin/env python

import unittest
from testcases import TestCases


def main():
	testcases = TestCases()
	testcases.run()
	testcases.print_results()


if __name__ == '__main__':
	main()


