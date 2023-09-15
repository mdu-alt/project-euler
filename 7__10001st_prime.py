# -*- coding: utf-8 -*-
"""Problem 7 -- 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

Source: https://projecteuler.net/problem=7
"""


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    a = 5

    while a**2 <= n:
        if n % a == 0 or n % (a+2) == 0:
            return False
        a += 6
    return True


def solution_optimized(ith: int) -> int:
    count = 1
    x = 2

    while count != ith:
        x += 1

        if is_prime(x):
            count += 1

    return x


if __name__ == "__main__":
    n = 10001
    solution = 104743

    assert(solution_optimized(n) == solution)
