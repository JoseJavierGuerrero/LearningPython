#!/usr/bin/env python
# encoding: utf-8

"""A script that retrieves definitions of a spanish word from www.rae.es"""

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
        # Check for the starting of a meaning
        newMeaning = attrs.count(('class', 'eOrdenAcepLema'))
        # Check for the text of a meaning
        meaningText = attrs.count(('class', 'eAcep'))
        # Check for various elements that appear in a meaning
        abrv = attrs.count(('class', 'eAbrv'))
        abrv += attrs.count(('class', 'eAbrvNoEdit'))
        example = attrs.count(('class', 'eEjemplo'))
        ref = attrs.count(('class', 'eRef'))
        ref += attrs.count(('class', 'eReferencia'))
        # TODO : store complex meanings
        # I'm ignoring complex meaning right now
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
            elif self.processingMeaning and self.currentMeaning is not '':
                self.processingMeaning = False
                self.meanings.append(self.currentMeaning)
        elif self.processingMeaning and self.currentMeaning is not '':
            self.meanings.append(self.currentMeaning)
            self.processingMeaning = False

def printMeanings(meanings):
    print '\n'.join([formatMeaning(meaning) for meaning in meanings])

def formatMeaning(meaning):
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
        except IOError:
            print 'Cannot get the requested URL'
        except UnicodeDecodeError:
            print 'Decode error'
        else:
            htmlSource = sock.read()
            parser = MeaningLister()
            parser.feed(htmlSource)
            if parser.meanings:
                print console.colorize('darkgray', word.capitalize())
                printMeanings(parser.meanings)
            else:
                print 'The word "%s" is not in the dictionary' % word
        finally:
            sock.close()
    else:
        print 'Usage: %s word' % sys.argv[0]