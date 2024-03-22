#!/usr/bin/python3
""" 0-minoperations"""


def minOperations(n):
    """
    minOperations
    calculates the fewest number of operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0

    ops = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            ops += divisor
            n //= divisor
        else:
            divisor += 1

    return ops
