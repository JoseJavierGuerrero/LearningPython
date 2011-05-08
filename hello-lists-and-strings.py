#!/usr/bin/env python
# encoding: utf-8

def main():
	print 'Mapping list into other list using list comprehensions'
	mapLists()
	print 'Splitting and joining a String'
	splittedString = splitString('Hello world, Python knows how to split and join strings like me')
	joinedString = joinString(splittedString)
	print joinedString

def mapLists():
	numberList = [1, 1, 2, 3, 5, 8, 13]
	print numberList
	print 'aritmetical operation *2 to all elements on the list'
	print [elem*2 for elem in numberList]
	
def splitString(param):
	tokenList = param.split(' ')
	return tokenList
	
def joinString(param):
	print param
	return ' '.join(param)


if __name__ == '__main__':
	main()

