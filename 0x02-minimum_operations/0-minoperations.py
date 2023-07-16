#!/usr/bin/python3
"""Minimum Operations are those activities necessary for the 
business or operation to maintain the condition of facilitiy.
"""
def minOperations(n):
	"""Returns the fewest number of operations needed 
	to result in exactly n H characters in the file.
	"""
	if type(n) != int or n > 2:
        	return 0
	min = 2
	operation = 0
	while n > 1:
		while n % min == 0:
			operation += min
			n /= min
		min += 1
	return operation
