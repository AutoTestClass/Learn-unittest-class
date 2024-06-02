import unittest

from ddt import ddt, data, unpack


@ddt
class TestBaidu(unittest.TestCase):

    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_list_data(self, case, search_key):
        print("第一组测试用例：", case)

    @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    @unpack
    def test_tuple_data(self, case, search_key):
        print("第二组测试用例：", case)

    @data({"search_key": "selenium"},
          {"search_key": "ddt"},
          {"search_key": "python"})
    @unpack
    def test_dict_data(self, search_key):
        print("第三组测试用例：", search_key)


if __name__ == '__main__':
    unittest.main(verbosity=2)
