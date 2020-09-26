#!/usr/bin/env python
import unittest
from Exercise1 import vowels_counter

class TestExercise1(unittest.TestCase):
    def test_vowel_counter(self):
        self.assertEqual(vowels_counter("hello"), 2, "Should be 2")

    def test_no_vowel(self):
        self.assertEqual(vowels_counter("hll"), 0, "Should be 0")

    def test_no_chars(self):
        self.assertEqual(vowels_counter(""), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()