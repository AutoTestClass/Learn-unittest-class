import unittest

from data_driver.param import data


class DataTest(unittest.TestCase):

    @data([
        ("case1", "hello"),
        ("case2", "hi"),
        ("case3", "你好"),
    ])
    def test_data_tuple(self, name, keyword):
        """
        tuple数据
        """
        print("tuple->", name, keyword)

    @data([
        ["case1", "hello"],
        ["case2", "hi"],
        ["case3", "你好"],
    ])
    def test_data_list(self, name, keyword):
        """
        list数据
        """
        print("list->", name, keyword)

    @data([
        {"scene": "case1", "keyword": "hello"},
        {"scene": "case2", "keyword": "hi"},
        {"scene": "case3", "keyword": "你好"},
    ])
    def test_data_dict(self, name, keyword):
        """
        dict数据
        """
        print("dict->", name, keyword)


if __name__ == '__main__':
    unittest.main()
