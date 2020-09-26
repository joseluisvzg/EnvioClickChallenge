#!/usr/bin/env python

"""
	Client class (with helper functions) for Exercise 3 test using data from standard input (JSON formated data)
"""

from Data import Data
from DataSet import DataSet
import json
from json.decoder import JSONDecodeError
import sys
import os

def make_unique(key, dct):
	"""
		Helper function: Generate a new key name 
	"""
	counter = 0
	unique_key = key
	while unique_key in dct:
	    counter += 1
	unique_key = '{}_{}'.format(key, counter)
	return unique_key

def parse_object_pairs(pairs):
	"""
		Helper function: Detect an already existing key and generates a new one
	"""
	dct = {}
	for key, value in pairs:
	    if key in dct:
	        key = make_unique(key, dct)
	    dct[key.lower()] = value
	return dct

def get_json():
	"""
		Helper function for getting raw text and parsing to json data
	"""
	json_data = None
	while json_data == None:
		print("Type and use Use ctrl + d to stop the input:")
		try:
			raw_data = sys.stdin.read()
			raw_data = raw_data.strip(os.linesep)
			if raw_data.startswith('{') and raw_data.endswith('}'):
				raw_data = raw_data.strip("{}")
			json_data = json.loads(f"{{ {raw_data} }}", object_pairs_hook=parse_object_pairs)
		except JSONDecodeError as e:
			print("Error ocurring during input parsing. Try again please.")
	return json_data

def menu():
	print("""
	Options:
		1) Enter new data.
		2) Show ordered data.
		0) Exit.
	""")

def select_menu_opt():
	return int(input("Select an option:"))

def parse_dict(json_data):
	"""
		From an dictionary, it returns a Data list
	"""
	parsed_dataset = []
	for kr_data, r_data in json_data.items():
		if isinstance(r_data, dict):
			parsed_dataset.append(Data(kr_data, r_data['name'], r_data['level'].lower(), r_data['priority'].lower()))
	return parsed_dataset

def get_raw_childs(json_data):
	"""
		Extract inner dictionaries (parent's childs)
	"""
	childs = {}
	for k, v in json_data.items():
		if isinstance(v, dict):
			childs[k] = v
	return childs

def json2data(json_data):
	"""
		Helper function for json to data parsing
	"""
	dataset = parse_dict(json_data)
	data = dataset
	items = [(child, raw_child) for child, raw_child in zip(dataset, json_data.values())]
	while len(items) > 0:
		parent, raw_childs = items.pop()
		childs = parse_dict(raw_childs)
		for child, raw_child in zip(childs, get_raw_childs(raw_childs).values()):
			parent.childs.append(child)
			items.append((child, raw_child))
	return data

if __name__ == "__main__":
	dataset = DataSet()
	option = 1
	while option > 0:
		menu()
		option = select_menu_opt()
		if option == 1:
			json_data = get_json()
			parsed_data = json2data(json_data)
			dataset.addData(parsed_data)
		elif option == 2:
			dataset.show()