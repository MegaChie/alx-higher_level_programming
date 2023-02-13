#!/usr/bin/python3
""" Unittest for class Rectangle """


import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testRetangle(unittest.TestCase):
	def tearDown(self):
		""" test case """
		Base._Base__nb_objects = 0
		self.assertEqual(Base._Base__nb_objects, 0)

	def test_instance(self):
		""" test case """
		value1 = Rectangle(3, 2)
		value2 = Rectangle(8, 7, 0, 0, 12)
		with self.assertRaises(TypeError):
			value3 = Rectangle("string")
			value4 = Rectangle(None)
			value5 = Rectangle(float('inf'))
			value6 = Rectangle(9.5, 9.3)
			value7 = Rectangle(-8, 9)
			value8 = Rectangle()
		self.assertEqual(value1.id, 1)
		self.assertEqual(value1._Base__nb_objects, 1)
		self.assertEqual(value2.id, 12)
		self.assertEqual(value2._Base__nb_objects, 1)

	def test_area(self):
		""" test case """
		value1 = Rectangle(3, 2)
		value2 = Rectangle(8, 7, 0, 0, 12)
		value3 = Rectangle(999, 999)
		self.assertEqual(value1.area(), 6)
		self.assertEqual(value2.area(), 56)
		self.assertEqual(value3.area(),998001)

	def test_display(self):
		""" test case """
		value1 = Rectangle(3, 2)
		value2 = Rectangle(4, 5, 0, 1, 12)
		with patch('sys.stdout', new=StringIO()) as fakeOutput:
			value1.display()
			self.assertEqual(fakeOutput.getvalue(), '###\n###\n')
		with patch('sys.stdout', new=StringIO()) as fakeOutput:
			value2.display()
			self.assertEqual(fakeOutput.getvalue(),
							 '\n####\n####\n####\n####\n####\n')

	def test_str(self):
		""" test case """
		value1 = Rectangle(3, 2)
		value2 = Rectangle(8, 7, 0, 0, 12)
		value3 = Rectangle(3, 2, 1)
		value4 = Rectangle(3, 2, id="fuckYeah")
		self.assertEqual(value1.__str__(), '[Rectangle] (1) 0/0 - 3/2')
		self.assertEqual(value2.__str__(), '[Rectangle] (12) 0/0 - 8/7')
		self.assertEqual(value3.__str__(), '[Rectangle] (2) 1/0 - 3/2')
		self.assertEqual(value4.__str__(), '[Rectangle] (fuckYeah) 0/0 - 3/2')

	def test_update(self):
		""" test case """
		value1 = Rectangle(3, 2)
		value2 = Rectangle(8, 7, 0, 0, 12)
		value3 = Rectangle(3, 2, 1)
		value4 = Rectangle(3, 2, id="fuckYeah")
		value5 = Rectangle(3, 2, id="fuckYeah")

		o1.update(5, 7)
		self.assertEqual(value1.__str__(), '[Rectangle] (5) 0/0 - 7/2')
		with self.assertRaises(ValueError):
			value2.update(**{'id': 1337, 'x': -1})
			value3.update("stringid", None, None)
		o4.update(None)
		self.assertEqual(value4.__str__(), '[Rectangle] (None) 0/0 - 3/2')
		o5.update(-5)
		self.assertEqual(value5.__str__(), '[Rectangle] (-5) 0/0 - 3/2')

	def test_to_dictionary(self):
		""" test case """
		value1 = Rectangle(3, 2)
		outPut1 = {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
		value2 = Rectangle(8, 7, 0, 0, 12)
		outPut2 = {'id': 12, 'width': 8, 'height': 7, 'x': 0, 'y': 0}
		value3 = Rectangle(3, 2, 1)
		utPut3 = {'id': 2, 'width': 3, 'height': 2, 'x': 1, 'y': 0}
		value4 = Rectangle(3, 2, id="fuckYeah")
		outPut4 = {'id': 'fuckYeah', 'width': 3, 'height': 2, 'x': 0, 'y': 0}
		self.assertEqual(value1.to_dictionary(), outPut1)
		self.assertEqual(value2.to_dictionary(), outPut2)
		self.assertEqual(value3.to_dictionary(), outPut3)
		self.assertEqual(value4.to_dictionary(), outPut4)

if __name__ == "__main__":
	unittest.main
