# tree


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def test():
    """
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> t
    [3, [1], [2, [1], [1]]]
    >>> label(t)
    3
    >>> branches(t)
    [[1], [2, [1], [1]]]
    >>> label(branches(t)[1])
    2
    >>> is_leaf(t)
    False
    >>> is_leaf(branches(t)[0])
    True
    """
    return 0


def fib_tree(n):
    """
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    >>> fib_tree(6)
    [8, [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]], [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    """
    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


# Partition trees.
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m.
    >>> partition_tree(2, 2)
    [2, [True], [1, [1, [True], [False]], [False]]]
    """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    """
    >>> print_parts(partition_tree(6, 4))
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
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


def right_binarize(tree):
    """Construct a right-branching binary tree.
    
    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


# 2.3.7   Linked Lists

empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def test_list():
    """
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> first(four)
    1
    >>> rest(four)
    [2, [3, [4, 'empty']]]
    >>> len_link(four)
    4
    >>> getitem_link(four, 1)
    2
    """
    return 0


def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s.
    >>> len_link_recursive(four)
    4
    >>> getitem_link_recursive(four, 1)
    2
    """
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t.
    >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    """
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    """Apply f to each element of s.
    
    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true.
    
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]    
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


def join_link(s, separator):
    """Return a string of all elements in s separated by separator.
    
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    
    
    """
    if n == 0:
        return link(empty, empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n - m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return extend_link(with_m, without_m)


def print_partitions(n, m):
    """
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
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
