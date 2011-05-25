#!/usr/bin/env python
# encoding: utf-8

def helloList(param):
	"""Basic operations to a list
	
	Returns None.
	"""
	print 'list:'
	print param
	print 'first value:'
	print param[0]
	print 'last value:'
	print param[-1]
	print 'first 3 values:'
	print param[:3]
	print 'even values:'
	print param[0:5:2]
	print 'odd values:'
	print param[1:5:2]
	print 'extend the list:'
	param.extend(['f', 'g', 'h'])
	print param
	print 'pop one element of the list:'
	elem = param.pop()
	print param
	print ' popped value:' + elem
	print 'append popped element to the list:'
	param.append(elem)
	print param
	print 'search the first occurrence of an element:'
	print 'searching for "c"... position:'
	i = param.index('c')
	print i
	print 'remove an element:'
	print 'removing "a"...'
	param.remove('a')
	print param
	
if __name__ == '__main__':
	param = ['a', 'b', 'c', 'd', 'e']
	helloList(param)
	