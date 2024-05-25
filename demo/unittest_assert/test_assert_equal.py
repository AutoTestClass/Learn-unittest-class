import unittest


class MyNumber:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyNumber({self.value})"


class TestBaseAssert(unittest.TestCase):
    # ...

    def test_isinstance_my_number(self):
        # 创建一个MyNumber的实例
        my_num = MyNumber(42)
        you_num = 43
        # 使用assertIsInstance()进行断言
        self.assertIsInstance(my_num, MyNumber)
        self.assertNotIsInstance(you_num, MyNumber)

    def test_eq(self):
        str1 = """hello
        world"""
        str2 = """hello world"""
        self.assertMultiLineEqual(str1, str2)
        self.assertEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
