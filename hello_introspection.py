#!/usr/bin/env python
# encoding: utf-8

import os

def info(object):
    """Prints methods, atributes and doc strings."""
    
    # Extract methods and atributes.
    members = dir(object)
    methods = [e for e in members if callable(getattr(object, e))]
    atributes = [e for e in members if not callable(getattr(object, e))]
    
    # Extract __name__ and __doc__ if available.
    try:
        getattr(object, "__name__")
        infostring = object.__name__ + "\n"
    except AttributeError:
        infostring = ""
    
    try:
        getattr(object, "__doc__")
        docstring = object.__doc__ + "\n"
    except AttributeError:
        docstring = ""
        
    if docstring != "":
        infostring = "\n\n".join([infostring, docstring])
    
    # Extract atribute and method information.
    atribute_info = "\n".join([atribute for atribute in atributes])
    infostring = "\n\n".join([infostring, "ATRIBUTES", atribute_info])
    
    method_info = "\n\n".join([name_and_doc(object, method) for method in methods])
    infostring = "\n\n".join([infostring, "METHODS", method_info])
    
    # Show the info.
    os.system('clear')
    print infostring
    
def name_and_doc(object, method):
    return name(object, method) + doc(object, method)
    
def name(object, method):
    return str(getattr(object, method).__name__)
    
def doc(object, method):
    return str(getattr(object, method).__doc__)
    
if __name__ == '__main__':
    info(os)
    #info(1)
    #info((1,))
    #info([])
    #info({})