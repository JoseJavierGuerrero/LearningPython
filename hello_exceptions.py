#!/usr/bin/env python
# encoding: utf-8

def open_file(file_):
	"""Opens a file with the name specified on file_"""
	
	try:
		f = open(file_)
	except IOError:
		print 'Error opening the following file: ' + file_
	else:
		print file_ + ' opened succesfully.'


if __name__ == '__main__':
	open_file('/idontexist')