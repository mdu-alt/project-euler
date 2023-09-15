# -*- coding: utf-8 -*-
"""Problem 3 -- Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Source: https://projecteuler.net/problem=3
"""


def solution_naive(n: int) -> int:
    divisor = 1

    while n > 1:
        divisor += 1

        while n % divisor == 0:
            n //= divisor

    return divisor


def solution_optimized(n: int) -> int:
    divisor = 1

    while n > 1:
        divisor += 1

        while n % divisor == 0:
            n //= divisor

        # The smallest prime factor of a composite number 'n' is less than or
        # equal to 'sqrt(n)': otherwise, 'n' itself is prime.
        if divisor**2 > n:
            divisor = n
            break

    return divisor


if __name__ == "__main__":
    n = 600851475143
    solution = 6857

    assert(solution_naive(n) == solution)
    assert(solution_optimized(n) == solution)
