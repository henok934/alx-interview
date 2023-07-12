#!/usr/bin/python3
def minOperations(n):
	operations = 0
	min_operation = 2
	while n > 1:
		while n % min_operation == 0:
			operations += min_operation
			n /= min_operation
		min_operation += 1

	return operations
