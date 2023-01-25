# 2.8   Efficiency
def fib(n):
    """
    >>> fib(5)
    5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def count(f):
    """
    >>> fib = count(fib)
    >>> fib(5)
    5
    >>> fib.call_count
    15
    >>> fib(5)
    5
    >>> fib.call_count
    30
    """

    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0
    return counted


def count_frames(f):
    """
    >>> fib = count_frames(fib)
    >>> fib(19)
    4181
    >>> fib.open_count
    0
    >>> fib.max_count
    19
    >>> fib(24)
    46368
    >>> fib.max_count
    24
    """

    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


# 2.8.2   Memoization


def memo(f):
    """
    >>> counted_fib = count(fib)
    >>> fib = memo(counted_fib)
    >>> fib(19)
    4181
    >>> counted_fib.call_count
    20
    >>> fib(34)
    5702887
    >>> counted_fib.call_count
    35
    """
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized
    # Bear lec19-demo.py make_memo_fib()


def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def exp_iter(b, n):
    result = 1
    for _ in range(n):
        result = result * b
    return result


def square(x):
    return x * x


def fast_exp(b, n):
    """
    >>> fast_exp(2, 100)
    1267650600228229401496703205376
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n // 2))
    else:
        return b * fast_exp(b, n - 1)
