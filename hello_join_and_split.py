#!/usr/bin/env python
# encoding: utf-8

	
def split_string(param):
	""" 
	Split a string using " " as a separator	
	
	Returns strings list.
	 """
	
	tokenList = param.split(' ')
	return tokenList
	
def join_string(param):
	""" 
	Join a list of strings using " " as a separator
	
	Returns strings list.
    """

	print param
	return ' '.join(param)


if __name__ == '__main__':
	print 'Splitting and joining a String'
	splitted_string = split_string('Hello world, Python knows how to split and join strings like me')
	joined_string = join_string(splitted_string)
	print joined_string

