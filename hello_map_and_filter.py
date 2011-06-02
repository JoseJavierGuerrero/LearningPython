#!/usr/bin/env python
# encoding: utf-8


if __name__ == '__main__':
	print 'We have a list of numbers:'	
	number_list = [1, 2, 3, 4, 5]
	print number_list
	print 'Let\'s map str function to it:'
	string_list = [str(item) for item in number_list]
	print string_list
	print 'Now, what about factorials?:'
	from math import factorial
	factorial_list = map(factorial, number_list)
	print factorial_list
	print 'Let\'s take those wich are greater than 3'
	greater_than_3 = filter(lambda x : x > 3, number_list)
	print greater_than_3
	print 'Factorials multiples of four? squared?'
	multiples_of_4 = [elem ** 2 for elem in factorial_list if elem % 4 == 0]
	print multiples_of_4
	print 'Let\'s play a little more with map and filter'
	char_list = ['a', 'b', 'c', 'd', 'e']
	print map(lambda x,y: (x*2)*y, number_list, char_list)
	print map(None, number_list, char_list)
	print filter(None, [[],'a',(), 0, 12 ,{}])