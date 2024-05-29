"""
assert 基本使用
"""
import unittest


def pprint(msg) -> str:
    print(msg)
    return msg


class MyNumber:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyNumber({self.value})"


class TestBaseAssert(unittest.TestCase):
    # ...

    def test_base_assert(self):
        """
        基础断言方法
        :return:
        """
        num = 100
        num2 = 80

        self.assertEqual(1 + 2, 2)
        self.assertNotEqual(1 + 2, 1)

        ret = True
        self.assertTrue(ret)
        self.assertFalse(ret)

        self.assertIs(num < num2, ret)
        self.assertIsNot(num < num2, ret)

        r = pprint("hello")
        self.assertIsNone(r)
        self.assertIsNotNone(r)

        result = "欢迎, lisi"
        username = "zhangsan"
        self.assertIn(username, result)
        self.assertNotIn(username, result)

        usernames = ["zhangsan", "lisi"]
        self.assertIsInstance(usernames, list)
        self.assertNotIsInstance(usernames, str)

        self.assertDictEqual({"key": 11}, {"key": 22})
        self.assertEqual({"key": 11}, {"key": 22})

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
