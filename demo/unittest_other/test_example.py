# test_example.py
import unittest


class ExampleTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertEqual(2 + 2, 4)
