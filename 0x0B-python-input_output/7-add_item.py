#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    loaded = load_from_json_file("add_item.json")
except FileNotFoundError:
    fileList = []
arrgumentCount = len(sys.argv)
for place in range(1, arrgumentCount):
    fileList.append(sys.argv[place])
save_to_json_file(fileList, "add_item.json")
