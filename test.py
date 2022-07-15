from unittest import TestCase, main

from main import move_zeroes

class MoveZeroesTestCase(TestCase):
	def test_1_base(self):
		self.assertEquals(move_zeroes([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0], "Lists don't match!")
	
	def test_2_no_zero(self):
		self.assertEquals(move_zeroes([1, 7, 8, 10, 12, 4]), [1, 7, 8, 10, 12, 4], "Lists don't match!")
	
	def test_1_all_zero(self):
		self.assertEquals(move_zeroes([0, 0, 0 ,0]), [0, 0, 0 ,0], "Lists don't match!")
	
	def test_1_empty(self):
		self.assertEquals(move_zeroes([]), [], "Lists don't match!")