#!/usr/bin/env python
# encoding: utf-8

def map(function, list, condition=True):
	""" Maps function to each element in list if condition is True
	
	
	Returns list.
	"""
	return [function(element) for element in list if condition]
	
def filter(filter,list):  
	""" Filters list to another list with all elements from list wich 
	filter(element) is True
	
	Returns list. 
	"""
	return [elem for elem in list if filter(elem)]


if __name__ == '__main__':
	print 'We have a list of numbers:'	
	numberList = [1, 2, 3, 4, 5,]
	print numberList
	print 'Let\'s map str function to it:'
	stringListOdd = map(str, numberList)
	print stringList
	print 'Now, what about factorials?:'
	from math import factorial
	factorialList = map(factorial, numberList)
	print factorialList
	print 'Multiples of four?'
	multiplesOfFour = filter(lambda x: x%4 == 0, factorialList)
	print multiplesOfFour
	
