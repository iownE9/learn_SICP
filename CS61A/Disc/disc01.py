# 1.1
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


# 1.2
def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# square(so_slow(5))


# 1.3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = n - 1

    while n % i != 0:
        i -= 1
        if i == 1:
            return True

    return False


#


def f(x):
    return x


def g(x, y):
    if x(y):
        return not y
    return y
