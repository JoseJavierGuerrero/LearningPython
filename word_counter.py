#!/usr/bin/env python
# encoding: utf-8


import collections

if __name__=='__main__':
    
    #print "\n".join([k.ljust(80)+": "+'*'*v for k, v in collections.Counter(open("/users/JotaJota/Downloads/about_turtle.txt").read().split()).items()])
    print "\n".join([k.ljust(reduce(lambda x, y: max(x,len(y)),open("/users/JotaJota/Downloads/about_turtle.txt").read().split(), 0)+2)+": "+'*'*v for k, v \
                                                            in collections.Counter(open("/users/JotaJota/Downloads/about_turtle.txt").read().split()).items()])