# 09.pdf
def list_unpack():
    """
    >>> lst = [32, 64]
    >>> x, y = lst
    >>> x
    32
    >>> y
    64
    >>>
    >>> pairs = [[3, 4], [2, 5], [1, 6]]
    >>> for a, b in pairs:
    ...     print(a * b)
    12
    10
    6
    >>> # reduce 归纳
    >>> from functools import reduce
    >>> from operator import add
    >>> reduce(add, [1, 2, 3, 4])
    10
    >>> # add(add(add(1, 2), 3), 4)
    """
    pass


# Dictionaries and for loops
def dictionary():
    """
    >>> d = {'a': 2, 'b': 5}
    >>> for k in d:
    ...     print(k)
    a
    b
    >>> # d.values(): only the values
    >>> for v in d.values():
    ...     print(v)
    2
    5
    >>> # d.items(): key-value pairs
    >>> for k, v in d.items():
    ...     print(k, v)
    a 2
    b 5
    """
    pass


def most_frequent(lst):
    "*** YOUR CODE HERE ***"
    counts = {}

    for elem in lst:
        if elem not in counts:
            counts[elem] = 1
        else:
            counts[elem] += 1

    return max(counts, key=lambda elem: counts[elem])


# exam
# Q1
def stem_and_leaf(lst, leaf_max):
    """Returns a dictionary representing a stem-and-leaf plot.
    >>> stem_and_leaf([7, 31, 365, 365, 3650], 100)
    {0: [7, 31], 3: [65, 65], 36: [50]}
    """
    "*** YOUR CODE HERE ***"
    plot = {}
    for i in lst:
        key = i // leaf_max

        if key in plot:
            plot[key] += [i % leaf_max]
        else:
            plot[key] = [i % leaf_max]
    print(plot)


# Q2
def one_to_one(d):
    """Returns True if D represents a one-to-one mapping of keys
    to values.

    >>> d = {'a': 4, 'b': 5, 'c': 3}
    >>> one_to_one(d)
    True
    >>> fail = {'a': 2, 'b': 4, 'c': 2}
    >>> one_to_one(fail)
    False
    """
    "*** YOUR CODE HERE ***"
    values = []
    for v in d.values():
        if v in values:
            return False
        else:
            values += [v]

    return True


# Q3
def degrees(users, start, end, visited):
    """Finds the degree of separation between START and END. If
    START and END are not connected, return infinity: float('inf').

    PARAMETERS:
    users   -- dictionary; keys are users, values are friends lists
    start   -- starting user
    end     -- ending user
    visited -- a Python set of users we've already checked
    """
    if start == end:
        return 0
    smallest = float('inf')  # infinity
    visited.add(start)
    for friend in users[start]:
        if friend not in visited:
            friend_degree = degrees(users, friend, end, visited)
            smallest = min(friend_degree + 1, smallest)
    return smallest
