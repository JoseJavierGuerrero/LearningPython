#!/usr/bin/env python
# encoding: utf-8

def hello_dictionaries(param):
	"""
	Basic operations with a dictionary
	
	Returns None.
	"""
	
	print 'dictionary:'
	print param
	print 'add a key-value pair to a dictionary:'
	print 'param["one"] = 1'
	param['one'] = 1
	print param
	print 'add another key-value to a dictionary:'
	dic = {'one':1, 2:'two', }
	param['another_dictionary'] = dic
	print param
	print 'deleting a key-value pair in a dictionary:'
	del param['another_dictionary']
	print param
	print 'clear a dictionary:'
	param.clear()
	print param
	
	
if __name__ == "__main__":
	my_params = {1:"one", \
				2:"two", \
				3:"three",
				}
	print hello_dictionaries(my_params)