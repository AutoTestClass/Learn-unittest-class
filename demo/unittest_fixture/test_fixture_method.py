import unittest


class Test(unittest.TestCase):

    def setUp(self) -> None:
        print("before")

    def test_case(self):
        print("this is case")

    def tearDown(self) -> None:
        print("after")


if __name__ == '__main__':
    unittest.main()
