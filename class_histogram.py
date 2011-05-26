#!/usr/bin/env python
# encoding: utf-8

import os
import collections
import math

class Histogram(collections.Counter):
    """Stores an histogram with the word frequency of a txt document"""
    
    def __init__(self, filepath_=None, list_=None):
        """
        Takes filepath and returns an histogram instance
        wich represents the frequency of the words in the file at 
        filepath or a list of pairs (word, freq)
        
        If both given dict will be ignored
        
        If no dict is given neither filepath (or it doesn't exists) it raises 
        an exception
        """
        
        if filepath_ is not None:
            f = open(filepath_).read()
            tokens = [elem for elem in f.split() if elem.isalnum()]
            self.longest_word = reduce(lambda x, y: max(x,len(y)), tokens, 0)
            collections.Counter.__init__(self, tokens)
        elif list_ is not None:
            d={}
            for (k, v) in list_:
                d[k]=v
            self.longest_word = reduce(lambda x, y: max(x,len(y)), d.keys(), 0)
            collections.Counter.__init__(self, d)
        else: raise IOError
            
        
    def __str__(self):
        return '\n'.join([k.ljust(self.longest_word+5) + ": " + '*'*v 
                            for (k, v) in self.items() ])

   
    def filter(self,filter_):
        """filter an histogram with filter_
        
        Returns a new instance with the elements wich key accomplish filter_"""
        l = [(k, v) for k, v in self.items() if filter_(k)]
        
        return Histogram(list_=l)
        
    def longer_than(self,n):
        """Returns a new instance with the words longer than n"""
        return self.filter(lambda x: len(x) > n)

    def top(self,n):
        """Returns a new instance with the top n words ordered by frequency"""
        topn = self.most_common(n)
        return Histogram(list_=topn)    
        
        
        
    

if __name__=="__main__":
    try:
        filepath = "./bible.txt"
        book = Histogram(filepath_=filepath)
        #print book
        print "\nThe ten most common words\n"
        #print book.top(10)
        print "\nWords longer than 10"
        #print book.longer_than(10)
    except IOError: 
        print "Error opening the file %s" % filepath


#TODO number of words, more filters, compare between two files: 
#longest word, most frequent word, number of words