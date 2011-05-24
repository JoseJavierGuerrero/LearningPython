#!/usr/bin/env python
# encoding: utf-8

def helloTuples():
	"""Basic operations with a dictionary
	
	Returns None.
	"""
	print 'tuple:'
	tuple = ('one', 'two', 'three', 'four', )
	print tuple
	print 'tuple to list:'
	listT = list(tuple)
	print listT
	print 'asign multiple values at once:'
	(a, b, c, d, ) = tuple
	print '%s = %s' % ('a', a)
	print '%s = %s' % ('b', b)
	print '%s = %s' % ('c', c)
	print '%s = %s' % ('d', d)
	

if __name__ == "__main__":
	helloTuples()