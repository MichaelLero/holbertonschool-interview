#!/usr/bin/python3

"""Module for computing the minimum number of operations to reach a
target number"""


def minOperations(n):
    """Compute the minimum number of operations to reach n starting from 1.

    Args:
        n (int): The target number to reach.

    Returns:
        int: The minimum number of operations required to reach n.
    """
    if n < 2:
        return 0

    operations = 0
    current = n

    while current > 1:
        for i in range(2, current + 1):
            if current % i == 0:
                operations += i
                current //= i
                break

    return operations
