#!/usr/bin/python3

def minOperations(n):
	min = 2
	operation = 0
	while n > 1:
		while n % min == 0:
			operation += min
			n /= min
		min += 1
	return operation
