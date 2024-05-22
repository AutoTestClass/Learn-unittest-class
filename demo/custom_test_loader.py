import os

import unittest


def custom_test_loader(start_dir: str, sub_dir_list: dict):
    """
    自定义测试加载器
    :param start_dir: 开始查找用例的目录，
    :param sub_dir_list: 包含的子目录
    :return:
    """
    test_suite = unittest.TestSuite()

    for subdir, pattern in sub_dir_list.items():
        sub_dir_path = os.path.join(start_dir, subdir)
        if os.path.isdir(sub_dir_path) is True:
            # 使用unittest.defaultTestLoader来发现并加载指定子目录下的测试
            sub_suite = unittest.defaultTestLoader.discover(
                start_dir=sub_dir_path,
                pattern=pattern,
                top_level_dir=start_dir)
            test_suite.addTest(sub_suite)

    return test_suite


if __name__ == '__main__':
    # 假设你的测试目录结构从当前目录开始
    start_dir = os.path.dirname(os.path.abspath(__file__))
    # 定义你想要包含的子目录列表
    run_sub_dir = {
        "unittest_assert": "*_equal.py",
        "unittest_base": "test_*.py"
    }
    suite = custom_test_loader(start_dir, run_sub_dir)
    runner = unittest.TextTestRunner()
    runner.run(suite)
