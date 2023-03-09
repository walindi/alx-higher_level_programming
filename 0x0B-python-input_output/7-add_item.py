#!/usr/bin/python3
# file 7-add_item.py
"""
Adds all arguments to a list and then saves them to a file
"""

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import json
import sys

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
