import math
import unittest

from parameterized import parameterized
from parameterized import parameterized_class


@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
    (1, 2, 3, 2),
    (5, 5, 10, 25)
])
class TestMathClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(self.a + self.b, self.expected_sum)

    def test_multiply(self):
        self.assertEqual(self.a * self.b, self.expected_product)


class TestMathUnitTest(unittest.TestCase):
    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(math.floor(input), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
