# 1.1
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 1)


# 1.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

    if n == 0:
        return 1
    elif n < 0 or k == 0:
        return 0
    else:
        return sum([count_k(n - i - 1, k) for i in range(k)])


# Lists
def test():
    """
    >>> fantasy_team = ['aaron rodgers', 'desean jackson']
    >>> print(fantasy_team)
    ['aaron rodgers', 'desean jackson']
    >>> fantasy_team[0]
    'aaron rodgers'
    >>> fantasy_team[len(fantasy_team) - 1]
    'desean jackson'
    >>> fantasy_team[-1]
    'desean jackson'
    
    """
    return 0


# List Slicing
def test2():
    """
    >>> directors = ['jenkins', 'spielberg', 'bigelow', 'kubrick']
    >>> directors[:2]
    ['jenkins', 'spielberg']
    >>> directors[1:3]
    ['spielberg', 'bigelow']
    >>> directors[1:]
    ['spielberg', 'bigelow', 'kubrick']
    >>> directors[0:4:2]
    ['jenkins', 'bigelow']
    >>> directors[::-1]
    ['kubrick', 'bigelow', 'spielberg', 'jenkins']
    """
    return 0


# List Comprehensions
# 2.1
def test3():
    """
    >>> a = [1, 5, 4, [2, 3], 3]
    >>> print(a[0], a[-1])
    1 3
    >>> len(a)
    5
    >>> 2 in a
    False
    >>> 4 in a
    True
    >>> a[3][0]
    2
    """


# 2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]


# 2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1

    return max(s[0] * max_product(s[2:]), 1 * max_product(s[1:]))
