import unittest

from ddt import ddt, data, unpack


@ddt
class TestData(unittest.TestCase):

    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_list_data(self, case, search_key):
        print("第一组测试用例：", case)

    @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    @unpack
    def test_tuple_data(self, case, search_key):
        print("第二组测试用例：", case)

    @data({"search_key": "selenium", "case_name": "case1"},
          {"search_key": "ddt", "case_name": "case2"},
          {"search_key": "python", "case_name": "case3"})
    @unpack
    def test_dict_data(self, case_name, search_key):
        print("第三组测试用例：", case_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
