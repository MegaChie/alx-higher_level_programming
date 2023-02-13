#!/usr/bin/python3
""" Unittest for class Base """


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase(unittest.TestCase)
	def tearDown(self):
		""" test case """
		Base._base__nb_objects = 0
		self.assertEqual(Base._Base__nb_objects, 0)

	def test_instance(self):
		""" test case """
		value1 = Base()
		value2 = Base(9)
		value3 = Base(9.5)
		value4 = Base(float('inf'))
		value5 = Base("string")
		value6 = Base(["list", 4, 2.5])
		value7 = Base(None)
		self.assertEqual(value1.id, 1)
		self.assertEqual(value2.id, 9)
		self.assertEqual(value3.id, 9.5)
		self.assertEqual(value4.id, float('inf'))
		self.assertEqual(value5.id, "string")
		self.assertEqual(value6.id, ["list", 4, 2.5])
		self.assertEqual(value7.id, 2)
		self.assertEqual(Base._Base__nb_objects, 2)

	def test_to_json_string(self):
		""" test case """
		value1 = [{"hi": 1, "yo": "hol"}]
		value2 = [{"hello": 3}]
		value3 = None
		value4 = "a string"
		value5 = 123
		value6 = [[1, 2, 3]]
		value7 = []
		self.assertCountEqual(Base.to_json_string(value1),
							'[{"hi": 1, "yo": "hol"}]')
		self.assertCountEqual(Base.to_json_string(value2), '[{"hello": 3}]')
		self.assertCountEqual(Base.to_json_string(value3), '[]')
		self.assertCountEqual(Base.to_json_string(value4), '"a string"')
		with self.assertRaises(TypeError):
			Base.to_json_string(value5)
		self.assertCountEqual(Base.to_json_string(value6), '[[1, 2, 3]]')
		self.assertCountEqual(Base.to_json_string(value7), '[]')

	def test_from_json_string(self):
		""" test case """
		value1 = [{"hi": 1, "yo": "hol"}]
		outPut1 = Base.from_json_string(value1)
		value2 = [{"hello": 3}]
		outPut2 = Base.from_json_string(value2)
		value3 = None
		outPut3 = Base.from_json_string(value3)
		value4 = "a string"
		outPut4 = Base.from_json_string(value4)
		value5 = 123
		outPut5 = Base.from_json_string(value5)
		value6 = [[1, 2, 3]]
		outPut6 = Base.from_json_string(value6)
		value7 = []
		outPut7 = Base.from_json_string(value7)
		self.assertEqual(Base.from_json_string(value1), outPut1)
		self.assertEqual(Base.from_json_string(value2), outPut2)
		self.assertEqual(Base.from_json_string(value3), outPut3)
		self.assertEqual(Base.from_json_string(value4), outPut4)
		self.assertEqual(Base.from_json_string(value5), outPut5)
		self.assertEqual(Base.from_json_string(value6), outPut6)
		self.assertEqual(Base.from_json_string(value7), outPut7)

	def test_create(self):
		""" test case """
		value1 = {'id': 1, 'width': 1, 'height': 2, 'x': 2, 'y':2}
		outPut1 = Rectangle.create(value1)
		value2 = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
		outPut2 = Square.create(value2)
		value3 = {'id': 1, 'width': "string", 'height': 2, 'x': 2, 'y':2}
		outPut3 = {'id': 2, 'size': "string", 'x': 4, 'y': 5}
		self.assertEqual(value1.__str__(), '[Rectangle] (1) 2/2 - 1/2')
		self.assertEqual(value2.__str__(), '[Square] (2) 4/5 - 3')
		with self.assertRaises(TypeError):
			outPut4 = Rectangle.create(value2)
			outPut5 = Square.create(value3)

	def test_save_to_file(self):
		""" test case """
		value1 = Rectangle(10, 7, 2, 8)
		value2 = Rectangle(2, 4)
		value3 = Square(10, 7, 2)
		value4 = Square(8)
		save1 = Rectangle.save_to_file([value1, value2])
		save2 = Square.save_to_file([value3, value4])
		self.assertTrue(os.path.isfile('Rectangle.json'))
		self.assertTrue(os.path.isfile('Square.json'))

	def test_load_from_file(self):
		""" test case """
		value1 = Rectangle(10, 7, 2, 8)
		value2 = Rectangle(2, 4)
		value3 = Square(10, 7, 2)
		value4 = Square(8)
		save1 = Rectangle.save_to_file([value1, value2])
		save2 = Square.save_to_file([value3, value4])
		list1 = Rectangle.load_from_file()
		list2 = Square.load_from_file()
		self.assertIsInstance(list1[0], Rectangle)
		self.assertIsInstance(list1[1], Rectangle)
		self.assertIsInstance(list2[0], Square)
		self.assertIsInstance(list2[1], Square)
		self.assertEqual(list1[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
		self.assertEqual(list1[1].__str__(), '[Rectangle] (2) 0/0 - 2/4')
		self.assertEqual(list2[0].__str__(), '[Square] (3) 7/2 - 10')
		self.assertEqual(list2[1].__str__(), '[Square] (4) 0/0 - 8')

if __name__ == "__main__":
	unittest.main()
