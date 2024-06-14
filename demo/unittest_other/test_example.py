# test_example.py
import unittest


# 目录>文件>类>方法：名称的字符，按照 0~9  a~z顺序。
# ** 用例之间不要有依赖。避免
# 通过命令控制执行：test_01_login.py   test_02_create.py  ... test_09_logout.py
# 需求：就是按照从上到下的顺序？ 需要自己去修改。

class ExampleTest3(unittest.TestCase):
    def test_case_2(self):
        print("this is test_case_2")
        self.assertEqual(2 + 2, 4)

    def test_case_1(self):
        print("this is test_case_1")
        self.assertEqual(1 + 1, 2)


class ExampleTest2(unittest.TestCase):
    def test_case_3(self):
        print("this is test_case_3")
        self.assertEqual(1 + 1, 2)

    def test_case_4(self):
        print("this is test_case_4")
        self.assertEqual(2 + 2, 5)
