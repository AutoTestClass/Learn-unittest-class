import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


#
# json_path = os.path.join(DATA_DIR, "test_data_dict_dict.json")
# yaml_path = os.path.join(DATA_DIR, "test_data_dict_dict.yaml")
#

def data_file(file_name: str) -> str:
    file_path = os.path.join(DATA_DIR, file_name)
    return file_path
