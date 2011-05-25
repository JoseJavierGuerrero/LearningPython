#!/usr/bin/env python
# encoding: utf-8


	
def splitString(param):
	""" Split a string using " " as a separator
	
	
	Returns strings list.
	 """
	tokenList = param.split(' ')
	return tokenList
	
def joinString(param):
	""" Join a list of strings using " " as a separator
	
	
	Returns strings list.
	 """
	print param
	return ' '.join(param)


if __name__ == '__main__':
	print 'Splitting and joining a String'
	splittedString = splitString('Hello world, Python knows how to split and join strings like me')
	joinedString = joinString(splittedString)
	print joinedString

