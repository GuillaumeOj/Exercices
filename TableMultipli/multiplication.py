# -*- codding:utf-8 -*-
"""
Multiplication module with 'table' function
"""

def table(number, max = 10):
	"""
	Print multiplication table for 'number' from 1 to 'max'
	"""

	i = 0

	while i < max:
		i += 1
		print(i, "*", number, "=", i * number)

if __name__ == '__main__':
	print('Error !')