#!/usr/bin/env python
# encoding: utf-8

# Formato de las definiciones en RAE.es
# la definición con una sola acepción está en:
# <span class="eAbrv"> :: Abreviación
# <span class="eAcep"> :: Acepción
# y con varias:
# <span class="eEtimo"> :: Etimología
# <span class="eOrdenAcepLema"> :: Número
# <span class="eAbrv"> :: Abreviación
# <span class="eAcep"> :: Acepción
# en caso de no existir la palabra no aparece ningún <span class="eAbrev">

import sys

import urllib
from sgmllib import SGMLParser

_URL_RAE = 'http://buscon.rae.es/draeI/SrvltGUIBusUsual?'

class MeaningLister(SGMLParser): 
	def reset(self):
		SGMLParser.reset(self) 
		self.spans = []
		self.isMeaning = False
		self.meanings = []
			
	def start_span(self, attrs): 
		"""Procces span tags to find meanings of the word"""
		meaning = [v for k, v in attrs if k == 'class' and v == 'eAcep'] 
		if meaning:
			self.spans.extend(meaning)
			self.isMeaning = True
		abbr = [v for k, v in attrs if k == 'class' and v == 'eAbrv']
		if abbr:
			self.isMeaning = False
		etim = [v for k, v in attrs if k == 'class' and v == 'eEtimo']
		if etim:
			self.isMeaning = False
			
	def end_span(self):
		self.isMeaning = False
		
	def handle_data(self, data):
		"""Take the raw text of a meaning and store it"""
		if self.isMeaning:
			self.meanings.append(data)

# TODO
def formatMeaning(meaning):
	"""Takes the raw text of the meaning and formats it."""
	return meaning

if __name__ == '__main__':
	argc = len(sys.argv)
	if argc == 2:
		word = sys.argv[1]
		try:
			params = urllib.urlencode(	{
										'TIPO_HTML':2, 
										'TIPO_BUS':3, 
										'LEMA': word})
			sock = urllib.urlopen(_URL_RAE + '%s' % params)
			htmlSource = sock.read()
			parser = MeaningLister()
			parser.feed(htmlSource)
			
			meanings = [formatMeaning(meaning) for meaning in parser.meanings]
			if meanings:
				print word.capitalize() + ':'
				print '\n\n'.join(meanings)
			else:
				print 'Cant find any meaning for %s' % word
			sock.close()
		except IOError:
			print 'Cannot get the requested URL'
		except UnicodeDecodeError:
			print 'Decode error'
	else:
		print 'Usage: %s word' % sys.argv[0]