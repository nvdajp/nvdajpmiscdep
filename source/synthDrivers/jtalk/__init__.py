from __future__ import absolute_import

from synthDriverHandler import SynthDriver
class SynthDriver(SynthDriver):
	@classmethod
	def check(cls):
		return False
