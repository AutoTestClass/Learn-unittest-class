import unittest

import test_example

# from test_example import ExampleTest

if __name__ == '__main__':
    # 1.用于测试所有的用例， 更适合测试项目里面
    # suit = unittest.defaultTestLoader.discover()

    # 2. 用于用例级别，更适合单个用例的执行
    # suite = unittest.TestSuite()
    # suite.addTests([
    #     ExampleTest("test_case_2"),
    #     ExampleTest("test_case_1"),
    # ])

    # 3. 当前文件下面所有用例的执行 main()

    test_loader = unittest.TestLoader()
    # 加载测试类
    # suite = test_loader.loadTestsFromTestCase(ExampleTest)

    # 加载测试用例  **不能指定目录
    # suite = test_loader.loadTestsFromName("test_example.ExampleTest.test_case_1")

    # 加载多个测试
    # suite = test_loader.loadTestsFromNames([
    #     "test_example.ExampleTest.test_case_1",
    #     "test_example.ExampleTest2.test_case_4"
    # ])

    # 加载测试模块  模块(module) = 文件
    suite = test_loader.loadTestsFromModule(test_example)

    # 测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suite)
