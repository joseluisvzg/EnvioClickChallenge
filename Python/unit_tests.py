#!/usr/bin/env python
import unittest
from Exercise1 import vowels_counter
from Exercise2 import vowels_changer
from Exercise3.DataSet import DataSet
from Exercise3.Data import Data

class TestExercise1(unittest.TestCase):
    def test_vowel_counter(self):
        self.assertEqual(vowels_counter("hello"), 2, "Should be 2")

    def test_no_vowel(self):
        self.assertEqual(vowels_counter("hll"), 0, "Should be 0")

    def test_no_chars(self):
        self.assertEqual(vowels_counter(""), 0, "Should be 0")

class TestExercise2(unittest.TestCase):
    def test_vowel_changer(self):
        self.assertEqual(vowels_changer("hello"), "hillu", "Should be 'hillu'")

    def test_no_vowel(self):
        self.assertEqual(vowels_changer("hll"), 'hll', "Should be 'hll'")

    def test_no_chars(self):
        self.assertEqual(vowels_changer(""), '', "Should be ''")

class TestExercise3(unittest.TestCase):
	def test_order_siblings(self):
		dataset = DataSet()

		data1 = Data("DataA", "One name", "one", "highest")
		data2 = Data("DataB", "One nameB", "two", "highest")
		data3 = Data("DataC", "One nameC", "one", "high")
		dataset.data = [data1, data2, data3]
		dataset.order_siblings(dataset.data)

		self.assertEqual(dataset.data[0].key, 'DataA', "Should be 'DataA'")
		self.assertEqual(dataset.data[1].key, 'DataC', "Should be 'DataC'")
		self.assertEqual(dataset.data[2].key, 'DataB', "Should be 'DataB'")

	def test_order(self):
		dataset = DataSet()

		data1 = Data("DataA", "One name", "one", "highest")
		data11 = Data("SubdataA", "One nameSubdataA", "one", "highest")
		data12 = Data("SubdataA", "One nameSubdataA2", "two", "high")
		data1.childs.append(data11)
		data1.childs.append(data12)
		data121 = Data("SubdataAA", "One nameSubdataAA", "one", "highest")
		data12.childs.append(data121)
		data2 = Data("DataB", "One nameB", "two", "highest")
		data21 = Data("SubdataB", "One nameSubdataB", "one", "highest")
		data2.childs.append(data21)	    
		data3 = Data("DataC", "One nameC", "one", "high")
		dataset.addData([data1, data2, data3])
		dataset.show()

		self.assertEqual(dataset.data[0].key, "DataA", "Should be 'DataA'")
		self.assertEqual(dataset.data[0].childs[0].key, "SubdataA", "Should be 'SubdataA'")
		self.assertEqual(dataset.data[0].childs[1].key, "SubdataA", "Should be 'SubdataA'")
		self.assertEqual(dataset.data[0].childs[1].childs[0].key, "SubdataAA", "Should be 'SubdataAA'")
		self.assertEqual(dataset.data[1].key, "DataC", "Should be 'DataC'")
		self.assertEqual(dataset.data[2].key, "DataB", "Should be 'DataB'")
		self.assertEqual(dataset.data[2].childs[0].key, "SubdataB", "Should be 'SubdataB'")

if __name__ == '__main__':
    unittest.main()