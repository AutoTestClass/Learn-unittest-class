import unittest


def setUpModule():
    print("all module case before")


def tearDownModule():
    print("all module case after")


class Test(unittest.TestCase):

    def test_case(self):
        print("this is  Test  class case")


class Test2(unittest.TestCase):

    def test_case(self):
        print("this is Test2 class  case")


if __name__ == '__main__':
    unittest.main()
