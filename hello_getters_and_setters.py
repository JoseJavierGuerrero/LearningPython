#!/usr/bin/env python
# encoding: utf-8


class MyDict(dict):
	""" 
	MyDict is a class that acts as a wrapper modifying the behaviour of 
	the built-in dict. 
	
	Adds an access counter and an items counter
	"""
	
	def __init__(self,dict_=None):
		if dict_ is not None:
			self.update(dict_)
			self.items_counter = len(self.items())
		else : 
			self.items_counter = 0
		self.access_counter = 0
		 
	def __setitem__(self, key, value):
		self.items_counter += 1
		dict.__setitem__(self,key,value)
		
	def __getitem__(self, key):
		self.access_counter += 1
		return dict.__getitem__(self, key) 
	
	def __delitem__(self, key):
		try:
			dict.__delitem__(self, key)
			self.items_counter -= 1
		except KeyError:
			pass
		finally:
			self.access_counter += 1
		
	def __str__(self):
		items_ = 'Size: %d items' % self.items_counter 
		access_ = 'Accesed %d times' % self.access_counter
		dict_ = dict.__str__(self)
		return '\n'.join([dict_, items_, access_])
	
	#def get(self,key): return self.__getitem__(key)

if __name__ == '__main__':
	dict_sample = MyDict({'Ran':'Akira Kurosawa', 'The Shining':'Stanley Kubrick',
	 					'Pulp Fiction':'Quentin Tarantino', 'Spirited Away':'Hayao Miyazaki'}) 
	print dict_sample
	print
	print "Who directed Ran? "
	print ">>>print dict_sample['Ran']"
	print dict_sample['Ran']
	print 
	print dict_sample
	print
	print """What about 'The Shining'?"""
	print """>>>print dict_sample.get('The Shining')"""
	print dict_sample.get('The Shining')
	print
	print dict_sample
	print
	print """Watch how dict_sample.get('The Shining') didn't add one access in our access_counter"""
	print """You could figure out why if you 'uncomment' get definition"""
	print 
	print ">>>del dict_sample['Ran']"
	del dict_sample['Ran']
	print
	print dict_sample
	print 
	