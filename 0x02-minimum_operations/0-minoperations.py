#!/usr/bin/python3
"""
MINIMUM OPERATIONS
"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    ops, root = 0, 2

    if (n <= 1):
        return ops

    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1

    return ops
