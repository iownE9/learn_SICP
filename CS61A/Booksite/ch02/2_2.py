def rational(n, d):
    return [n, d]  # list


def numer(x):
    return x[0]


def denom(x):
    return x[1]


# =============== #


def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
    print(numer(x), '/', denom(x))


def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


# from fractions import gcd

# def rational(n, d):
#     g = gcd(n, d)
#     return (n // g, d // g)  # tupe

# >>> from operator import getitem
# >>> getitem(pair, 0)
# 10
# >>> getitem(pair, 1)
# 20


def pair(x, y):
    """Return a function that represents a pair."""

    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y

    return get


def select(p, i):
    """Return the element at index i of pair p.
    >>> p = pair(20, 14)
    >>> select(p, 0)
    20
    >>> select(p, 1)
    14
    """
    return p(i)
