#!/usr/bin/env python
# encoding: utf-8

def person(name='Edgar', age=18):
    """ 
    Prints a string using "name" and "age".    
    
    Returns None.
    """
    print name + ' is ' + str(age)


if __name__ == '__main__':
    person()
    person('Miles')
    person(age=21)
    person('Damian', 23)
    person(age=30, name='Herman')
    

