# 银行卡校验码


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if (n < 10):
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


# Inverse Cascade


def inverse_cascsde(n):
    """
    >>> inverse_cascsde(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow = lambda n: f_then_g(grow, print, n // 10)
    shrink = lambda n: f_then_g(print, shrink, n // 10)
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


#
from ucb import trace


@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Partitions
def count_partitions(n, max):
    """
    The number of ways to partition n using integers up to m equals:
    1. the number of ways to partition n-m using integers up to m, and
    2. the number of ways to partition n using integers up to m-1.
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif max == 0:
        return 0
    else:
        with_m = count_partitions(n - max, max)
        without_m = count_partitions(n, max - 1)
        return with_m + without_m
