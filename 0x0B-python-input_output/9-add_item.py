#!/usr/bin/python3
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
filename = 'add_item.json'
from sys import argv
import os

if not os.path.exists(filename):
    save([], filename)

obj = load(filename)
for i in range(1, len(argv)):
    obj.append(argv[i])
save(obj, filename)
