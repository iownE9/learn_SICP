# 14-Mutable Objects and Functions.pdf 30~33
def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    return withdraw


def make_withdraw_list(balance):
    b = [balance]

    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]

    return withdraw


def f(x):
    x = 4

    def g(y):

        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z

        return h

    return g


# Referential Transparency, Lost
a = f(1)
b = a(2)
b(3) + b(4)


# Review  Resource/61a-sp18-mt2.pdf
def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    
    >>> combo(531, 432)      # 45312 contains both _531_ and 4_3_2.
    45312
    >>> combo(531, 4321)     # 45321 contains both _53_1 and 4_321.
    45321
    >>> combo(1234, 9123)    # 91234 contains both _1234 and 9123_
    91234
    >>> combo(0, 321)        # The number 0 has no digits,so 0 is not in the result.
    321
    """
    if a == 0 or b == 0:
        return a + b

    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10

    return min(
        combo(a // 10, b) * 10 + a % 10,
        combo(a, b // 10) * 10 + b % 10)


# Q&A
from tree import *


def profit(t):
    """Return the max profit.
    
    >>> t = tree(2, [tree(3), tree(4, [tree(5)])])
    >>> profit(t)
    8
    """
    return helper(t, False)


def helper(t, used_parent):
    f = lambda cond: sum([helper(b, cond) for b in branches(t)])
    if used_parent:
        return f(False)
    else:
        use_label_total = label(t) + f(True)
        skip_label_total = 0 + f(False)

        return max(use_label_total, skip_label_total)
