#!/usr/bin/env python
# encoding: utf-8

def main():
	map = lambda f, list: [f(elem) for elem in list]
	numberList = [1, 2, 3, 4, 5,]
	print map (lambda x: pow(x, 2), numberList)

if __name__ == '__main__':
	main()

