# 14.pdf 相关 week07 16.py


def tree_size(t):
    # if is_leaf(t):
    #     return 1
    sub_sizes = [tree_size(s) for s in subtrees(t)]
    return 1 + sum(sub_sizes)


def review_list():
    """
    >>> nums = [1, 2, 3]
    >>> nums[0:2] = [0,1]
    >>> nums
    [0, 1, 3]
    """
    pass


def group_by_key(pairs):
    """
    >>> example = [[1, 2], [3, 2], [1, 3], [3, 1], [1, 2]]
    >>> group_by_key(example)
    {1: [2, 3, 2], 3: [2, 1]}
    """
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)
    return d


# Function that return multiple values return tuples


def string_demo():
    """
    >>> 'banana'[2:]
    'nana'
    >>> x, y = 1, 2
    >>> '{} + {} = {}'.format(x, y, x + y)
    '1 + 2 = 3'
    >>> words = 'This is a sentence.'.split()
    >>> words
    ['This', 'is', 'a', 'sentence.']
    >>> ' '.join(words)
    'This is a sentence.'
    """
    pass


# basic review
# slicing always creates new objects in memnry


def Q4_Q5():
    """
    >>> s = [1, 2, 3, 4]
    >>> a = s
    >>> a[1:] is s[1:]
    False  
    >>> # slicing always creates new objects in memory
    >>> s = (1, 2, 3, 4)
    >>> s is (1, 2, 3, 4)
    False  
    >>> # Immutability has nothing to do with identity
    >>> s == [1, 2, 3, 4]
    False  
    >>> # a tuple cannot be equivalent to a list
    >>> 'hello' == 'hello'
    True
    >>> 'hello' is 'hello'
    True   
    >>> # strings are special -- Python only creates one copy of a string literal in memory
    """
    pass


# exam review
def Q1_Q2():
    """
    >>> def outer():
    ...     def inner():
    ...         return 42
    ...     return inner
    >>> outer is outer
    True   
    >>> # referring to the function outer
    >>> outer() is outer()
    False  
    >>> # referring to the return value of outer; draw an environment diagram to see why it is False
    >>> outer() == outer()
    False  
    >>> # == for functions behaves like is
    >>> [1, 2, (3, 4)] == [1, 2, (3, 4)]
    True
    >>> [1, 2, outer()] == [1, 2, outer()]
    False  
    >>> # == for list checks if each pair of elements satisfies ==    
    >>> # Q2
    >>> a = [1, 2, 3, 4]
    >>> a[0] = a
    >>> a is a[0]
    True
    """
    pass


# Tree ADT
def tree(root, subtrees=[]):
    return [root] + list(subtrees)


def root(t):
    return t[0]


def entry(s):
    return s[0]


def subtrees(s):
    return s[1:]


def is_leaf(t):
    return not subtrees(t)
