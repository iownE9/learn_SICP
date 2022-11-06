def mapper(fn, num):
    """
    >>> mapper(lambda x: (n+1)//2 if n%2==0 else -(n+1)//2, 5)
    0
    -1
    1
    -2
    2
    """
    i = 0
    while i < num:
        print(fn(i))
        i = i + 1


# mapper(lambda x: (x + 1) * (-1) ** x // 2, 5)