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
            collections.Counter.__init__(self, tokens)
        elif list_ is not None:
            d={}
            for (k, v) in list_:
                d[k]=v
            collections.Counter.__init__(self, d)
        else: raise IOError
        self.longest_word = reduce(lambda x, y: len(x) > len(y) and x or y, self.keys())
        self.word_count = reduce(lambda n, (k,v): v+n, self.items(), 0)
        [(k,v)] = self.most_common(1)
        self.most_frequent = k
        
    def __str__(self):
        string_list = [k.ljust(len(self.longest_word)+5) + ": " + '*'*v 
                            for (k, v) in self.items() ]
        twords = "Total words: %d" % self.word_count
        lword = "Longest word: %s, %d characters" % (self.longest_word,len(self.longest_word))
        mfword = "Most frequent word: %s, %d times " % (self.most_frequent, self[self.most_frequent])
        string_list.extend([twords,lword,mfword])
        return '\n'.join(string_list)
        
   
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
        
    def starts_with(self,c):
        """Returns a new instance with the words starting with prefix c"""
        return self.filter(lambda x: x.startswith(c))


if __name__=="__main__":
    try:
        filepath = "./bible.txt"
        book = Histogram(filepath_=filepath)
        print book
        print "\nThe ten most common words\n"
        print book.top(10)
        print "\nWords longer than 10"
        print book.longer_than(10)
        print "\nWords starting with \'lo\'"
        print book.starts_with("lo")
    except IOError: 
        print "Error opening the file %s" % filepath


#TODO number of words, more filters, compare between two files: 
#longest word, most frequent word, number of words