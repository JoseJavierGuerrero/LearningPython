#!/usr/bin/env python
# encoding: utf-8

	
def mapLists(param):
	""" Maps a list into other list using list comprehensions
	
	Returns None.
	"""
	print param
	print 'arithmetical operation *2 to all elements on the list'
	print [elem*2 for elem in param]
	
	
if __name__ == "__main__":
	myNumberList = [1, 1, 2, 3, 5, 8, 13]
	mapLists(myNumberList)