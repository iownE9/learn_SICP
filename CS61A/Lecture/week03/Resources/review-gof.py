# http://albertwu.org/cs61a/review/hof/basic.html
# Question 11
def make_mod(n):
    """Returns a function that takes an argument x.
    That function will return x modulo n.

    >>> mod_7 = make_mod(7)
    >>> mod_7(3)
    3
    >>> mod_7(41)
    6
    """
    "*** YOUR CODE HERE ***"

    def mod(m):
        return m % n

    return mod