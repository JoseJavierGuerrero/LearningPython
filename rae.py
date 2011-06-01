#!/usr/bin/env python
# encoding: utf-8

"""
A script that retrieves definitions of a spanish word from www.rae.es

Uses sys, urllib and sgmllib from standard libraries.
Uses pygments open source library.

Usage: rae.py word
"""

import sys
import urllib
from sgmllib import SGMLParser

from pygments import console


_URL_RAE = 'http://buscon.rae.es/draeI/SrvltGUIBusUsual?'

class MeaningLister(SGMLParser):
    
    """Stores the meanings (spans with class="eAcep") of the specified SGML"""
    
    def reset(self):
        SGMLParser.reset(self) 
        self.addText = False
        self.currentMeaning = ''
        self.meanings = []
        self.processingMeaning = False
        self.processMoreMeanings = True
        
    def start_a(self, attrs):
        """Process <a> tags in order to stop when meanings end"""
        vease = attrs.count(('title', 'Véase'))
        if vease:
            self.processMoreMeanings = False
            
    def start_span(self, attrs): 
        """Procces span tags to find meanings of the word"""
        newMeaning = attrs.count(('class', 'eOrdenAcepLema'))
        
        meaningText = attrs.count(('class', 'eAcep'))
        
        abrv = attrs.count(('class', 'eAbrv'))
        abrv += attrs.count(('class', 'eAbrvNoEdit'))
        example = attrs.count(('class', 'eEjemplo'))
        ref = attrs.count(('class', 'eRef'))
        ref += attrs.count(('class', 'eReferencia'))
        
        complexMeaning = attrs.count(('class', 'eFCompleja'))
        
        if newMeaning:
            if self.processingMeaning and self.currentMeaning is not '':
                self.meanings.append(self.currentMeaning)
            self.processingMeaning = True
            self.currentMeaning = ''
            self.addText = True

        if meaningText or abrv or example or ref:
            self.addText = True
        elif complexMeaning:
            self.processMoreMeanings = False
        else:
            if self.processingMeaning and self.currentMeaning is not '':
                self.meanings.append(self.currentMeaning)
                self.processingMeaning = False
            
    def handle_data(self, data):
        """Take the raw text of a meaning and store it"""
        if self.processMoreMeanings:
            if self.processingMeaning:
                self.currentMeaning += data
            elif self.currentMeaning is not '' and self.processingMeaning:
                self.processingMeaning = False
                self.meanings.append(self.currentMeaning)
        elif self.processingMeaning and self.currentMeaning is not '':
            self.meanings.append(self.currentMeaning)
            self.processingMeaning = False

def print_meanings(meanings):
    print '\n'.join([format_meaning(meaning) for meaning in meanings])

def format_meaning(meaning):
    """Takes the raw text of the meaning and formats it"""
    return meaning.strip(' \t').capitalize()

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 2:
        word = sys.argv[1]
        try:
            params = urllib.urlencode(  {
                                        'TIPO_HTML':2, 
                                        'TIPO_BUS':3, 
                                        'LEMA': word
                                        })
            sock = urllib.urlopen(_URL_RAE + '%s' % params)
            html_source = sock.read()
            parser = MeaningLister()
            parser.feed(html_source)
            parser.meanings = filter(lambda m: m is not '', parser.meanings)
            if parser.meanings:
                print console.colorize('darkgray', word.capitalize())
                print_meanings(parser.meanings)
            else:
                print 'The word "%s" is not in the dictionary' % word
            sock.close()
        except IOError:
            print 'Cannot get the requested URL'
        except UnicodeDecodeError:
            print 'Decode error'
    else:
        print 'Usage: %s word' % sys.argv[0]