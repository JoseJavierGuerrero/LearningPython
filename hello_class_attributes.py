#!/usr/bin/env python
# encoding: utf-8


class OneMore:
	count = 0
	
	def __init__(self):
		self.__class__.count += 1
	
	
if __name__ == '__main__':
	print '>>>from hello_class_attributes import OneMore'
	print '>>>one = OneMore()'
	one = OneMore()
	print '>>>two = OneMore()'
	two = OneMore()
	print '>>>print one.count'
	print one.count
	print '>>>print OneMore.count'
	print OneMore.count
	print '>>>print two.__class__.count'
	print two.__class__.count