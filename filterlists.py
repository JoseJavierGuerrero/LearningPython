#!/usr/bin/env python
# encoding: utf-8


def map(function, list, condition=lambda x: True):
    """
    Applies function to each element of list if they satisfy the condition.
    
    Returns a filtered list with function aplied to all elements.
    """
    return [function(element) for element in list if condition(element)]


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
	print 'Let\'s take those wich are greater than 3'
	greaterThan3List = map(lambda x:x, numberList, lambda x : x > 3)
	print greaterThan3List
	print 'Factorials multiples of four?'
	multiplesOf4 = map(lambda x:x, factorialList, lambda x : x % 4 == 0)
