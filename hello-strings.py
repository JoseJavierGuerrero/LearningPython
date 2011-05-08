#!/usr/bin/env python
# encoding: utf-8

def helloStrings(param):
	"""Concatenate all strings from a dictionary
	
	Returns string.
	"""
	
	return "".join([elem for elem in param.values()])

if __name__ == "__main__":
	myParams = {1:"one", \
				2:"two", \
				3:"three"
				}
	print helloStrings(myParams)