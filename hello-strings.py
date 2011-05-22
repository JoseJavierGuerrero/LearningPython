#!/usr/bin/env python
# encoding: utf-8

def helloStrings(param):
	"""Concatenate all strings from a dictionary
	
	Returns string.
	"""
	
	string = "".join([elem for elem in param.values()])
	print string
	print string.split("two", 1)

if __name__ == "__main__":
	myParams = {1:"one", \
				2:"two", \
				3:"three"
				}
	helloStrings(myParams)