#!/usr/bin/python3
""" Unittest for class Square """


import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
	def tearDown(self):
		""" test case """
		Base._Base__nb_objects = 0
		self.assertEqual(Base._Base__nb_objects, 0)

	def test_instance(self):
		""" test case """
		value1 = Square(5)
		value2 = Square(id="hello", size=3)
		with self.assertRaises(ValueError):
			value3 = Square(-5, 3, 4)
			value4 = Square(9.5, 9.3)
			value5 = Square(float('inf'))
			value6 = Square("string")
			value9 = Square(None)
		with self.assertRaises(TypeError):
			value7 = Square(5, "hi")
			value8 = Square(5, None)
			value10 = Square(5, float('inf'))
			value11 = Square(5, 9.5)
			value12 = Square()
		self.assertEqual(value1.id, 1)
		self.assertEqual(value1._Base__nb_objects, 3)
		self.assertEqual(value2.id, 'hello')
		self.assertEqual(value2._Base__nb_objects, 3)

	def test_area(self):
		""" test case """
		value1 = Square(5)
		value2 = Square(999, 0, 0, "helloo")
		value3 = Square(id="hello", size=3, x=1, y=0)
		self.assertEqual(value1.area(), 25)
		self.assertEqual(value2.area(), 998001)
		self.assertEqual(value3.area(), 9)

	def test_display(self):
		""" test case """
		value1 = Square(4)
		value2 = Square(id="hello", size=3, x=1, y=0)
		with patch('sys.stdout', new=StringIO()) as fakeOutput:
			value1.display()
			self.assertEqual(fakeOutput.getvalue(), '####\n####\n####\n####\n')
		with patch('sys.stdout', new=StringIO()) as fakeOutput:
			value2.display()
			self.assertEqual(fakeOutput.getvalue(), ' ###\n ###\n ###\n')

	def test_str(self):
		""" test case """
		value1 = Square(5)
		value2 = Square(3, 2)
		value3 = Square(1, 2, 3, 4)
		value4 = Square(id="hello", size=3, x=1, y=0)
		self.assertEqual(value1.__str__(), '[Square] (1) 0/0 - 5')
		self.assertEqual(value2.__str__(), '[Square] (2) 2/0 - 3')
		self.assertEqual(value3.__str__(), '[Square] (4) 2/3 - 1')
		self.assertEqual(value4.__str__(), '[Square] (hello) 1/0 - 3')

	def test_update(self):
		""" test case """
		value1 = Square(5)
		value2 = Square(3, 2)
		value3 = Square(1, 2, 3, 4)
		value4 = Square(id="hello", size=3, x=1, y=0)
		value1.update(6, 1, 2, 8)
		self.assertEqual(value1.__str__(), '[Square] (6) 2/8 - 1')
		value2.update(1, 2, 3, id="hello")
		self.assertEqual(value2.__str__(), '[Square] (hello) 2/0 - 3')
		with self.assertRaises(ValueError):
			value3.update("hello", -5)
			value4.update(x=9.5)

	def test_to_dictionary(self):
		""" test case """
		value1 = Square(5)
		value2 = Square(5, 6)
		value3 = Square(1, 2, 3, 5)
		value4 = Square(3, 2, id="holberton")
		d1 = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
		d2 = {'id': 2, 'size': 5, 'x': 6, 'y': 0}
		d3 = {'id': 5, 'size': 1, 'x': 2, 'y': 3}
		d4 = {'id': 'holberton', 'size': 3, 'x': 2, 'y': 0}
		self.assertDictEqual(value1.to_dictionary(), d1)
		self.assertDictEqual(value2.to_dictionary(), d2)
		self.assertDictEqual(value3.to_dictionary(), d3)
		self.assertDictEqual(value4.to_dictionary(), d4)

if __name__ == '__main__':
	unittest.main()
