import unittest


class TestAssert(unittest.TestCase):

    def test_eq(self):
        str1 = """hello
        world"""
        str2 = """hello world"""
        self.assertMultiLineEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
