import unittest

from ddt import ddt, file_data


@ddt
class TestFile(unittest.TestCase):

    @file_data('data/test_data_dict_dict.json')
    def test_file_data_json_dict_dict(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)

    @file_data('data/test_data_dict_dict.yaml')
    def test_file_data_yaml_dict_dict(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)


if __name__ == '__main__':
    unittest.main(verbosity=2)
