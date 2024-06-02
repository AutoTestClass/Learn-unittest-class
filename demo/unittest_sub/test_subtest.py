import unittest


def calculate_discounted_price(original_price, discount_rate):
    """
    计算打折后的价格。
    :param original_price: 原价
    :param discount_rate: 折扣率（0-1之间的浮点数）
    :return: 折后价格
    """
    return original_price * (1 - discount_rate)


class TestDiscountCalculator(unittest.TestCase):

    def test_calculate_discounted_price(self):
        # 定义一系列测试用例
        test_cases = [
            (100, 0.1, 90.0),  # 10% 的折扣
            (200, 0.2, 160.0),  # 20% 的折扣
            (300, 0.3, 220.0),  # 30% 的折扣 210.0 error
            (400, 0.4, 240.0),  # 40% 的折扣
            (500, 0.5, 250.0),  # 50% 的折扣
        ]

        # 使用 subTest 对每个测试用例进行迭代
        for original_price, discount_rate, expected_price in test_cases:
            print(f"原价：{original_price}, 折扣率：{discount_rate}, 现价：{expected_price}")
            with self.subTest(
                    op=original_price,
                    dr=discount_rate,
                    ep=expected_price
            ):
                calculated_price = calculate_discounted_price(original_price, discount_rate)
                self.assertAlmostEqual(calculated_price, expected_price,
                                       msg=f"对于原价{original_price}和折扣率{discount_rate}，计算结果有误。")


if __name__ == '__main__':
    unittest.main()
