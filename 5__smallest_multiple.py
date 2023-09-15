# -*- coding: utf-8 -*-
"""Problem 5 -- Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Source: https://projecteuler.net/problem=5
"""
from math import lcm


def solution_optimized(n: int) -> int:
    # Finding the smallest number divisible by all integers from 1 to n is
    # equivalent to finding the range's least common multiple.
    return lcm(*range(1, n+1))


if __name__ == "__main__":
    n = 20
    solution = 232792560

    assert(solution_optimized(n) == solution)
