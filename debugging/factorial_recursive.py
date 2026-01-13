#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Function Description:
		Computes the factorial of a non-negative integer n using recursion.

	Parameters:
		n (int): A non-negative integer whose factorial is to be calculated.

	Returns:
		int: The factorial of the given integer n. If n is 0, returns 1.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

if len(sys.argv) > 1:
	f = factorial(int(sys.argv[1]))
	print(f)
