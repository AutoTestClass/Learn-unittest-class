import unittest


class SomeWork():

    def init_env(self):
        print("初始化环境")

    def clear_env(self):
        print("清理环境配置")


class Test(unittest.TestCase):
    some_work = None

    @classmethod
    def setUpClass(cls):
        cls.some_work = SomeWork()
        cls.some_work.init_env()

    def test_case(self):
        print("this is case")

    @classmethod
    def tearDownClass(cls):
        cls.some_work.clear_env()


if __name__ == '__main__':
    unittest.main()
