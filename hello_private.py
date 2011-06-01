#!/usr/bin/env python
# encoding: utf-8

class Private:
	__secret = 42
	
	def tell_secret(self):
		print self.__class__.__secret
		
	def __change_secret(self, number=42):
		self.__class__.__secret = number
		
		
if __name__ == '__main__':
	secret = Private()
	try:
		Private.__secret
	except AttributeError:
		print 'AttributeError: class Private has no attribute \'__secret\''
	try:
		secret.__change_secret(23)
	except AttributeError:
		print 'AttributeError: class Private has no attribute \'__change_secret\''
	secret.tell_secret()
	secret._Private__change_secret(number=23)
	secret.tell_secret()
	
	
	
	