import math
import unittest

from parameterized import parameterized


def calculate_discounted_price(original_price, discount_rate):
    """
    计算打折后的价格。
    :param original_price: 原价
    :param discount_rate: 折扣率（0-1之间的浮点数）
    :return: 折后价格
    """
    return original_price * (1 - discount_rate)


from parameterized import parameterized_class


@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
    (1, 2, 3, 2),
    (5, 5, 10, 25)
])
class TestMathClass(unittest.TestCase):

    def test_add(self):
        print("param-->", self.a, self.b, self.expected_sum)
        self.assertEqual(self.a + self.b, self.expected_sum)

    def test_multiply(self):
        print("param-->", self.a, self.b, self.expected_sum)
        self.assertEqual(self.a * self.b, self.expected_product)


@unittest.skip("跳过")
class TestMathUnitTest(unittest.TestCase):

    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(math.floor(input), expected)

    @parameterized.expand([
        (100, 0.1, 90.0),  # 10% 的折扣
        (200, 0.2, 160.0),  # 20% 的折扣
        (300, 0.3, 220.0),  # 30% 的折扣 210.0 error
        (400, 0.4, 240.0),  # 40% 的折扣
        (500, 0.5, 250.0),  # 50% 的折扣
        (600, 0.6, 240.0),  # 60% 的折扣
    ])
    def test_calculate_discounted_price(self, original_price, discount_rate, expected_price):
        """测试折扣率"""
        calculated_price = calculate_discounted_price(original_price, discount_rate)
        # 断言失败了不会影响后续的数据的遍历。
        self.assertAlmostEqual(calculated_price, expected_price,
                               msg=f"对于原价{original_price}和折扣率{discount_rate}，计算结果有误。")


if __name__ == '__main__':
    unittest.main(verbosity=2)
