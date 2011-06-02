#!/usr/bin/env python
# encoding: utf-8

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

if __name__ == '__main__':
    print '>>> file_length(\'./gpl-3.0.dos.ascii\')'
    myFile = './gpl-3.0.dos.ascii'
    l = file_length(myFile)
    print myFile + ' is ' + str(l) + ' bytes long.'
    print
    print '>>> hello_write(\'test.txt\')'
    hello_write('test.txt')