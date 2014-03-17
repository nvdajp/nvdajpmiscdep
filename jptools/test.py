# -*- coding: UTF-8 -*-

import unittest
import jpBrailleRunner

class JpBrailleTests(unittest.TestCase):

	def test_pass1(self):
		count, outfile = jpBrailleRunner.pass1()
		self.assertEqual(count, 0)

	def test_pass2(self):
		count, outfile = jpBrailleRunner.pass2()
		self.assertEqual(count, 0)

if __name__ == '__main__':
	unittest.main()
