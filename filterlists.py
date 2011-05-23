#!/usr/bin/env python
# encoding: utf-8

def map(function, list, condition=True):
	return [function(element) for element in list if condition]

if __name__ == '__main__':
	print 'We have a list of numbers:'	
	numberList = [1, 2, 3, 4, 5,]
	print numberList
	print 'Let\'s map str function to it:'
	stringList = map(str, numberList)
	print stringList
	print 'Now, what about factorials?:'
	from math import factorial
	factorialList = map(factorial, numberList)
	print factorialList
