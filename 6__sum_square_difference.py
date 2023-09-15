# -*- coding: utf-8 -*-
"""Problem 6 -- Sum square difference

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is,

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Source: https://projecteuler.net/problem=6
"""


def solution_naive(n: int) -> int:
    def sum_1_to_n(n: int) -> int:
        return n*(n+1) // 2

    square_of_sum = (sum_1_to_n(n))**2
    sum_of_squares = sum(i**2 for i in range(n+1))

    return square_of_sum - sum_of_squares


def solution_optimized(n: int) -> int:
    # Knowing that:
    #
    #   1^2 + 2^2 + ... + n^2 = 1/6 * n * (n+1) * (2n+1)
    #   (1 + 2 + ... + n)^2 = 1/4 * (n^2 * (n+1)^2)
    #
    # The difference simplifies to:
    #
    #   d = (n^4 - n^2)/4 + (n^3 - n)/6
    #
    a = n**4 - n**2
    b = n**3 - n

    return int(a/4 + b/6)


if __name__ == "__main__":
    n = 100
    solution = 25164150

    assert(solution_naive(n) == solution)
    assert(solution_optimized(n) == solution)
