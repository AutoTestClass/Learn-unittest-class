"""
认识unittest测试用例:
    * test fixture
    * test case
    * test suite
    * test runner
"""
import time
import unittest

from .calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    # 测试类：**. 创建测试类 必须 继承 unittest.TestCase
    """

    def setUp(self) -> None:
        """
        text fixture
        用例前置动作：启动浏览器、连接数据库，准备的数据，
        """
        print("test start")

    def tearDown(self) -> None:
        """
        text fixture
        用例后置动作：关闭浏览器，关闭数据库，删除/还原数据
        """
        print("test end")

    def login(self, username, password):
        """封装用户登录模块"""
        print("this is method")

    def test_case(self):
        """
         1. 必须以 test 开头.
         2.每个用例都是独立的个体，不能有入参，不能被调用。
        """
        print("this is test case")

    def test_user_login(self):
        """测试用户登录"""
        self.login("admin", "admin123")

    def test_aa_fail(self):
        self.assertAlmostEqual(2 + 2, 3)

    def test_add_one(self):
        self.login("aaa", "bbb")
        c = Calculator(2)
        result = c.add()
        time.sleep(1)
        self.assertEqual(result, 2)

    def test_add_two(self):
        c = Calculator(3, 5)
        result = c.add()
        time.sleep(2)
        self.assertEqual(result, 8)

    def test_add_three(self):
        c = Calculator(3, 5, 2)
        result = c.add()
        time.sleep(3)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    # 创建测试套件 test suite
    suit = unittest.TestSuite()
    # suit.addTest(TestCalculator("test_add_one"))
    # suit.addTest(TestCalculator("test_add_two"))
    # suit.addTest(TestCalculator("test_add_three"))
    suit.addTests([
        TestCalculator("test_add_one"),
        TestCalculator("test_add_two"),
        TestCalculator("test_add_three")
    ])
    # 创建测试运行器  test runner
    runner = unittest.TextTestRunner()
    runner.run(suit)
