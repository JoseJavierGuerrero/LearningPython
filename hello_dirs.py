#!/usr/bin/env python
# encoding: utf-8

import os
import glob

def dirs_and_files(path_):
    """Prints separately the subdirectories and files of given directory. """
    
    if os.path.isdir(path_):
        print 'DIRECTORIES'
        print '-----------'
        print "\n".join(get_dirs(path_))
        print
        print 'FILES'
        print '-----'
        print "\n".join(get_files(path_))
    else:
        print 'Usage: dirs_and_files(path_)'

def get_dirs(path_):
    """Returns the subdirectory list of given directory"""
    
    return [f for f in os.listdir(path_) 
                if os.path.isdir(os.path.join(path_, f))]
    
def get_files(path_):
    """Returns the subdirectory list of given directory"""
    
    return [f for f in os.listdir(path_) 
                if os.path.isfile(os.path.join(path_, f))]

def find(path_, regex):
    """Finds matches with regex in the given path."""
   
    if os.path.isdir(path_):
        path_and_regex = os.path.join(path_, regex)
        matches = glob.glob(path_and_regex)
        if matches != []:
            print "\n".join(matches)
        for d in get_dirs(path_):
            find(os.path.join(path_, d), regex)
    else:
        print 'Usage: find(path_, regex)'


if __name__ == '__main__':
    print '>>> dirs_and_files(\'.\')'
    dirs_and_files('.')
    print
    print '>>> find(\'.\', \'*.py\')'
    find ('.', '*.py')