#!/usr/bin/python3

def minOperations(n: int) -> int:
    if type(n) != int or n < 2:
        return 0
    repr = 1
    ops = 0
    status = False
    while repr < n:
        if n % repr == 0 and not status:
            copy = repr
            ops += 1
            status = True
        else:
            repr += copy
            ops += 1
            status = False
    return ops
