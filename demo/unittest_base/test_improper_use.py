"""
unittest 错误用法
"""
import unittest


class TestImproperUse(unittest.TestCase):
    """
    用例错误的设计
    """

    def test_login(self, username, password):
        """
        1. 给用例加参数
        """
        print("this is login case")

    def test_case_1(self):
        print("this is test case 1")

    def test_case_2(self):
        """
        2. 在一条用例里面调用另一条用例。
        """
        self.test_case_1()
        print("this is test case 2")


class CorrectUsage(unittest.TestCase):

    def login(self, username, password):
        """封装的登录"""
        print("this is login method")

    def test_case_1(self):
        self.login("admin", "admin123")
        print("this is test case 1")

    def test_case_2(self):
        self.login("guest", "guest123")
        print("this is test case 2")


if __name__ == '__main__':
    unittest.main()
