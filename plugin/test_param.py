import unittest

from data_driver.param import data, file_data


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


class FileDataTest(unittest.TestCase):

    @file_data("file_data_dict.json")
    def test_file_data_json(self, start, end, value):
        """
        json数据文件
        """
        print("json file->", start, end, value)

    @file_data("file_data_dict.yaml")
    def test_file_data_yaml(self, start, end, value):
        """
        yaml数据文件
        """
        print("yaml file->", start, end, value)

    @file_data("file_data_csv.csv", line=2)
    def test_file_data_csv(self, firstname, lastname):
        """
        csv数据文件
        """
        print("csv file->", firstname, lastname)

    @file_data(file="file_data_excel.xlsx", sheet="Sheet1", line=2)
    def test_file_data_excel(self, firstname, lastname):
        """
        excel数据文件
        """
        print("excel file->", firstname, lastname)


if __name__ == '__main__':
    unittest.main()
