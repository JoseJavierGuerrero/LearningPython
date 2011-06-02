#!/usr/bin/env python
# encoding: utf-8


def fib():
    a = b = 1
    while True:
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    gen = fib()
    for i in range(1000):
        print gen.next()

    for i in fib():
        if i > 10 ** 100:
            break
        else:
            print i

    
