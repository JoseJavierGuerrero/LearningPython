#!/usr/bin/env python
# encoding: utf-8


import collections

if __name__=='__main__':
    
    #print "\n".join([k.ljust(80)+": "+'*'*v for k, v in collections.Counter(open("./gpl-3.0.dos.ascii").read().split()).items() if k.isalnum()])
    
    print "\n".join([k.ljust(reduce(lambda x, y: max(x,len(y)),open("./gpl-3.0.dos.ascii").read().split(), 0)+2)+": "+'*'*v 
                        for k, v in collections.Counter(open("./gpl-3.0.dos.ascii").read().split()).items() if k.isalnum()])