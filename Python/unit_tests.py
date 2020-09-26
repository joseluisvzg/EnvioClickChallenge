#!/usr/bin/env python
import unittest
from Exercise1 import vowels_counter
from Exercise2 import vowels_changer

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

if __name__ == '__main__':
    unittest.main()