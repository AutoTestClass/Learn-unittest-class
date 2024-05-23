import unittest

import test_example
from test_example import ExampleTest

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    # 加载测试类
    suite = test_loader.loadTestsFromTestCase(ExampleTest)

    # 加载测试用例
    suite = test_loader.loadTestsFromName("test_example.ExampleTest.test_case_1")

    # 加载多个测试
    suite = test_loader.loadTestsFromNames([
        "test_example.ExampleTest.test_case_1",
        "test_example.ExampleTest.test_case_2"
    ])

    # 加载测试模块
    suite = test_loader.loadTestsFromModule(test_example)

    # 测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suite)
