import os
import yaml


def read_test_data(file_name):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(current_dir + "/../../data/" + file_name)
    with open(path, 'r') as stream:
        data = yaml.load(stream)

    return data
