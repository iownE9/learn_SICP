# 2.9   Recursive Objects

class Link:
    """A linked list with a first element and the rest.
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[1]
    4
    """
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    """Return a string that would evaluate to s.
    >>> s = Link(3, Link(4, Link(5)))
    >>> link_expression(s)
    'Link(3, Link(4, Link(5)))'
    """
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

Link.__repr__ = link_expression

def test_1():
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> s_first = Link(s, Link(6))
    >>> s_first
    Link(Link(3, Link(4, Link(5))), Link(6))
    >>> len(s_first)
    2
    >>> len(s_first[0])
    3
    >>> s_first[0][2]
    5
    """

def extend_link(s, t):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> extend_link(s, s)
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    >>> Link.__add__ = extend_link
    >>> s + s
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    """
    if t is Link.empty:
        return s

    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

Link.__add__ = extend_link


def square(n):
    return n*n

def map_link(f, s):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> map_link(square, s)
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))



def filter_link(f, s):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> odd = lambda x: x % 2 == 1
    >>> map_link(square, filter_link(odd, s))
    Link(9, Link(25))
    >>> [square(x) for x in [3, 4, 5] if odd(x)]
    [9, 25]
    """
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered
def join_link(s, separator):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> join_link(s, ", ")
    '3, 4, 5'
    """

    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)



def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)

        # return with_m + without_m
        return with_m + without_m if with_m is not Link.empty else without_m + with_m

# PS C:\Users\iown_home\Desktop> Python3.8 -i 2_9.py
# >>> print_partitions(6, 4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "2_9.py", line 158, in print_partitions
#     lists = partitions(n, m)
#   File "2_9.py", line 132, in partitions
#     using_m = partitions(n-m, m)
#   File "2_9.py", line 134, in partitions
#     without_m = partitions(n, m-1)
#   File "2_9.py", line 138, in partitions
#     return with_m + without_m
# TypeError: can only concatenate tuple (not "Link") to tuple
# >>> t = Link.empty
# >>> s = Link(3, Link(4, Link(5)))
# >>> s + t
# Link(3, Link(4, Link(5)))
# >>> t + t
# ()
# >>> t + s
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "Link") to tuple
# >>>



def print_partitions(n, m):
    """"
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1

    """
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


# 2.9.2   Tree Class

class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    """
    >>> fib_tree(5)
    Tree(3, (Tree(1, (Tree(0), Tree(1))), Tree(2, (Tree(1), Tree(1, (Tree(0), Tree(1)))))))
    """
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, (left, right))

def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None.
    >>> sum_labels(fib_tree(5))
    10
    """
    return t.label + sum([sum_labels(b) for b in t.branches])


def test_1():
    """
    >>> # 2_8.py
    >>> fib_tree = memo(fib_tree)
    >>> big_fib_tree = fib_tree(35)
    >>> big_fib_tree.label
    5702887
    >>> big_fib_tree.branches[0] is big_fib_tree.branches[1].branches[1]
    True
    >>> sum_labels = memo(sum_labels)
    >>> sum_labels(big_fib_tree)
    142587180    
    """
    pass

# 2.9.3   Sets

def test_sets():
    """
    >>> s = {3, 2, 1, 4, 4}
    >>> s
    {1, 2, 3, 4}
    >>> 3 in s
    True
    >>> len(s)
    4
    >>> s.union({1, 5}) # 并集
    {1, 2, 3, 4, 5}
    >>> s.intersection({6, 5, 4, 3}) # 交集
    {3, 4}
    """
    pass


def empty(s):
    return s is Link.empty

def set_contains(s, v):
    """Return True if and only if set s contains v.

    >>> s = Link(4, Link(1, Link(5)))
    >>> set_contains(s, 2)
    False
    >>> set_contains(s, 5)
    True    
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def adjoin_set(s, v):
    """Return a set containing all elements of s and element v.
    
    >>> s = Link(4, Link(1, Link(5)))
    >>> t = adjoin_set(s, 2)
    >>> t
    Link(2, Link(4, Link(1, Link(5))))
    """
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> t = Link(2, Link(4, Link(1, Link(5))))
    >>> s = Link(4, Link(1, Link(5)))
    >>> intersect_set(t, apply_to_all_link(s, square))
    Link(4, Link(1))
    """
    return keep_if_link(set1, lambda v: set_contains(set2, v))

def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2.
    
    >>> t = Link(2, Link(4, Link(1, Link(5))))
    >>> s = Link(4, Link(1, Link(5)))
    >>> union_set(t, s)
    Link(2, Link(4, Link(1, Link(5))))
    """
    set1_not_set2 = keep_if_link(set1, lambda v: not set_contains(set2, v))
    return extend_link(set1_not_set2, set2)




# 从小到大
def set_contains(s, v):
    """
    >>> u = Link(1, Link(4, Link(5)))
    >>> set_contains(u, 0)
    False
    >>> set_contains(u, 4)
    True
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def intersect_set(set1, set2):
    """
    >>> intersect_set(s, s.rest)
    Link(4, Link(5))
    """
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set(set1.rest, set2)
        elif e2 < e1:
            return intersect_set(set1, set2.rest)



# 平衡树
def set_contains(s, v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains(s.right, v)
    elif s.entry > v:
        return set_contains(s.left, v)

def adjoin_set(s, v):
    """
    >>> adjoin_set(adjoin_set(adjoin_set(None, 2), 3), 1)
    Tree(2, Tree(1), Tree(3))
    """
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry, s.left, adjoin_set(s.right, v))
    elif s.entry > v:
        return Tree(s.entry, adjoin_set(s.left, v), s.right)

