import unittest


def add_floats(a: float, b: float):
    return a + b


class MyTestClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyTestClass({self.value})"

    # 测试数据


data1 = MyTestClass(10)
data2 = MyTestClass(5)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5, 6]  # 注意这里有一个字符串'4'


class TestAssertions(unittest.TestCase):

    def test_add_floats(self):
        # 两个浮点数相加
        result = add_floats(0.1, 0.2)

        # 由于浮点数的精度问题，直接比较可能不等
        # 使用assertAlmostEqual来允许微小的差异
        self.assertAlmostEqual(result, 0.4, delta=0.0001)

        # 另一个例子，这次我们故意制造一个较大的误差
        bad_result = 0.3001
        with self.assertRaises(AssertionError):
            # 这个断言会失败，因为bad_result和0.3的差值大于delta
            self.assertAlmostEqual(bad_result, 0.3, delta=0.0001)

    def test_assertGreater(self):
        # 检查 data1.value 是否大于 data2.value
        self.assertGreater(data1.value, data2.value)

    def test_assertLess(self):
        # 检查 data2.value 是否小于 data1.value
        self.assertLess(data2.value, data1.value)

    def test_assertRegex(self):
        # 假设我们有一个字符串，并想检查它是否匹配某个正则表达式
        test_string = "This is a test string 123"
        # 使用正则表达式匹配包含数字的模式
        self.assertRegex(test_string, r'\d+')

    def test_assertCountEqual(self):
        # 检查两个列表是否包含相同的元素（不考虑顺序）
        # 注意 list2 中有一个字符串'4'，但整数值4仍然被认为是相等的（因为它们是相等的值）
        self.assertCountEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
