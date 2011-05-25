#!/usr/bin/env python
# encoding: utf-8

import os
import glob

def file_length(file_):
    """Return the file length in bytes"""
    try:
        f = open(file_)
        f.seek(0, 2)
        f_length = f.tell()
        f.close()
    except IOError:
        print 'Couldn\'t open the specified file'
        raise ValueError
    else:
        return f_length
        
def hello_write(file_):
    """Demonstration of writing a file."""
    # Create file if doesn't exist, overwrite it otherwise.
    f = open(file_, 'w')
    
    # Write some content into the file and close it.
    f.write('bye bye, previous content!')
    f.close()
    
    # Open file for appending data, create if doesn't exist.
    f = open(file_, 'a')
    
    # Append content at the end of the file and close it.
    f.write('\nappended text')
    f.close()
    
    print file(file_).read()
    
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
    print '>>> file_length(\'/Users/alejandrogomez/Desktop/git.rtf\')'
    myFile = '/Users/alejandrogomez/Desktop/git.rtf'
    l = file_length(myFile)
    print myFile + ' is ' + str(l) + ' bytes long.'
    print
    print '>>> hello_write(\'test.txt\')'
    hello_write('test.txt')
    print
    print '>>> dirs_and_files(\'/Users/alejandrogomez/Desktop/code/\')'
    dirs_and_files('/Users/alejandrogomez/Desktop/code/')
    print
    print '>>> find(\'/Users/alejandrogomez/Desktop/code/reuse/\', \'*.c\')'
    find ('/Users/alejandrogomez/Desktop/code/reuse/', '*.c')