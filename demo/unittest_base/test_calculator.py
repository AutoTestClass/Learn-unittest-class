import time
import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    # 用例前置动作
    def setUp(self):
        print("test start")

    # 用例后置动作
    def tearDown(self):
        print("test end")

    def test_aa_fail(self):
        self.assertAlmostEqual(2+2, 3)

    def test_add_one(self):
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
        c = Calculator(3, 5)
        result = c.add()
        time.sleep(3)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add_one"))
    suit.addTest(TestCalculator("test_add_two"))
    suit.addTest(TestCalculator("test_add_three"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
