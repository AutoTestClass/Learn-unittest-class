import unittest

# from unittest_base.test_calculator import TestCalculator
#
# suit = unittest.TestSuite()
# suit.addTests([
#     TestCalculator("test_add_one"),
#     TestCalculator("test_add_two"),
#     TestCalculator("test_add_three")
# ])


if __name__ == '__main__':
    # 指定测试开始的目录为 `top_level_dir/tests`
    start_dir = 'top_level_dir/tests'
    # 指定顶层目录为 `top_level_dir`
    top_level_dir = 'top_level_dir'

    suite = unittest.defaultTestLoader.discover(
        start_dir="unittest_base",
        pattern='test_cal*.py',
        top_level_dir="??"
    )

    runner = unittest.TextTestRunner()
    runner.run(suite)
