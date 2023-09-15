# -*- coding: utf-8 -*-
"""Problem 4 -- Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Source: https://projecteuler.net/problem=4
"""


def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def solution_naive() -> int:
    largest_palindrome = 0

    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            palindrome = x*y

            if is_palindrome(palindrome):
                largest_palindrome = max(palindrome, largest_palindrome)

    return largest_palindrome


def solution_optimized() -> int:
    largest_palindrome = 0

    x = y = 999
    z = 0

    while x >= 100:
        # Any 6-digits palindromes can be written:
        #
        #   p = x*y = 100000a + 10000b + 1000c + 100c + 10b + 1a
        #           = 11*(9091a + 910b + 100c)
        #
        # So either 'x' or 'y' must have a factor of 11: it determines what
        # values of 'y' to check depending on 'x'.
        if x % 11 == 0:
            y, z = 999, 1
        else:
            y, z = 990, 11

        # Do not process any doublet twice, e.g. '{x=345,y=567}' and
        # '{x=567,y=345}'.
        while y >= x:
            palindrome = x*y

            # If 'n' is less or equal to the largest palindrome found so far,
            # the next ones will necessarily be smaller: break the loop.
            if palindrome <= largest_palindrome:
                break

            if is_palindrome(palindrome):
                largest_palindrome = palindrome

            y -= z

        x -= 1

    return largest_palindrome


if __name__ == "__main__":
    solution = 906609

    assert(solution_naive() == solution)
    assert(solution_optimized() == solution)
