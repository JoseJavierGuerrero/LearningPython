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
from pygments import console

_URL_RAE = 'http://buscon.rae.es/draeI/SrvltGUIBusUsual?'

class MeaningLister(SGMLParser):
	
	"""Stores the meanings (spans with class="eAcep") of the specified SGML"""
	
	def reset(self):
		SGMLParser.reset(self) 
		self.store = False
		self.ref = False
		self.processMoreMeanings = True
		self.meanings = []
		
	def start_a(self, attrs):
		"""Process a tags in order to stop when meanings end"""
		vease = [v for k, v in attrs if k == 'title' and v == 'Véase']
		if vease:
			self.processMoreMeanings = False
			
	def start_span(self, attrs): 
		"""Procces span tags to find meanings of the word"""
		meaning = [v for k, v in attrs if k == 'class' and v == 'eAcep']
		ref = [v for k, v in attrs if k == 'class' and v == 'eRefLema' or v == 'eReferencia']
		complexMeaning = [v for k, v in attrs if k == 'class' and v == 'eFCompleja']
		if complexMeaning:
			self.processMoreMeanings = False
		elif ref:
			self.ref = True
		elif meaning:
			self.store = True
		else:
			self.store = False			
			
	def handle_data(self, data):
		"""Take the raw text of a meaning and store it"""
		if self.processMoreMeanings:
			if self.ref:
				meaning = ''
				try:
					meaning = self.meanings.pop()
				except IndexError:
					meaning = data
				else:
					meaning += data
				self.meanings.append(meaning)
			elif self.store:
				self.meanings.append(data)
			
	def end_span(self):
		self.store = False
		self.ref = False

def printMeanings(meanings):
	i = 1
	for meaning in meanings:
		print console.colorize('blue', str(i) + '. ') + formatMeaning(meaning)
		i += 1
		
# TODO
def formatMeaning(meaning):
	"""Takes the raw text of the meaning and formats it"""
	return meaning.strip(' ').capitalize()

if __name__ == '__main__':
	argc = len(sys.argv)
	if argc == 2:
		word = sys.argv[1]
		try:
			params = urllib.urlencode(	{
										'TIPO_HTML':2, 
										'TIPO_BUS':3, 
										'LEMA': word
										})
			sock = urllib.urlopen(_URL_RAE + '%s' % params)
			htmlSource = sock.read()
			parser = MeaningLister()
			parser.feed(htmlSource)
			if parser.meanings:
				print console.colorize('darkgray', word.capitalize())
				printMeanings(parser.meanings)
			else:
				print 'Cant find any meaning for %s' % word
			sock.close()
		except IOError:
			print 'Cannot get the requested URL'
		except UnicodeDecodeError:
			print 'Decode error'
	else:
		print 'Usage: %s word' % sys.argv[0]