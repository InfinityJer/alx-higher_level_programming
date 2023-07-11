#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        file_data = load_from_json_file(filename)
    except FileNotFoundError:
        file_data = []

    for arg in argv[1:]:
        file_data.append(arg)

    save_to_json_file(file_data, filename)
