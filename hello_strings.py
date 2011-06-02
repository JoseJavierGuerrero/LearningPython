#!/usr/bin/env python
# encoding: utf-8


def hello_strings(param):
    """
    Concatenate all strings from a dictionary
    
    Returns string.
    """
    
    string = " ".join([elem for elem in param.values()])
    print string
    print string.split("two", 1)


if __name__ == "__main__":
    my_params = {1:"one", \
                2:"two", \
                3:"three"
                }
    hello_strings(my_params)