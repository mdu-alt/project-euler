# -*- coding: utf-8 -*-
"""Problem 1 -- Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Source: https://projecteuler.net/problem=1
"""


def solution_naive(n: int) -> int:
    sum = 0

    for x in range(3, n):
        if x % 3 == 0 or x % 5 == 0:
            sum += x

    return sum


def solution_optimized(n: int) -> int:
    def sum_1_to_n(n: int) -> int:
        return n*(n+1) // 2

    # The sum of multiples of a given 'n' can be expressed as a regular sum:
    #
    #   sum_of_multiples(3, 1000) = 3 + 6 + 9 + ... + 999
    #                             = 3 * (1 + 2 + 3 + ... + 333)
    #                             = 3 * sum_1_to_n(999 // 3)
    #
    def sum_of_multiples(multiple: int, n: int) -> int:
        return multiple * sum_1_to_n((n-1) // multiple)

    return sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)


if __name__ == '__main__':
    n = 1000
    solution = 233168

    assert(solution_naive(n) == solution)
    assert(solution_optimized(n) == solution)
