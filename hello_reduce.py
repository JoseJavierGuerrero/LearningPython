#!/usr/bin/env python
# encoding: utf-8


def suma(a,b):
	return a + b

if __name__ == '__main__':
	number_list = [1, 2, 3, 4, 5]
	char_list = ['h', 'e', 'l', 'l', 'o']
	suma_todos = reduce(suma, number_list)
	print suma_todos
	hello = reduce(suma, char_list)
	print hello