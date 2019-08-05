# -*- coding:utf-8 -*-
"""
Little program for printing multiplication table
"""
import multiplication

def main():
	number = input('Give an integer number: ')
	number = int(number)

	multiplication.table(number)

if __name__ == '__main__':
	main()