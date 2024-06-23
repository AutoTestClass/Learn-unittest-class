import unittest

from jsonrunner.runner import JSONTestRunner


class TestDemo(unittest.TestCase):
    """Test Demo class"""

    def test_pass(self):
        """pass case"""
        self.assertEqual(5, 5)

    def test_fail(self):
        """fail case"""
        self.assertEqual(5, 6)

    def test_error(self):
        """error case"""
        self.assertEqual(a, 6)

    @unittest.skip("skip case")
    def test_skip(self):
        """skip case"""
        ...


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        TestDemo("test_pass"),
        TestDemo("test_skip"),
        TestDemo("test_fail"),
        TestDemo("test_error")
    ])

    runner = JSONTestRunner(output="./reports/result.json", verbosity=2)
    runner.run(suit)
