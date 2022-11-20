# Trees


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


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


def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


# Depth:  the number of edges between the root of the tree to the node


# 1.1
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])


# 1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(branch) for branch in branches(t)])


# 1.3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                     [tree(3),
    ...                     tree(4)]),
    ...                 tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t)**2)

    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])


# 1.4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    >>> sum([[1], [2, 3]], [4])
    [4, 1, 2, 3]
    """
    if is_leaf(tree):
        return [label(tree)]

    for branch in branches(tree):
        # path = sum([[label(tree)], find_path(branch, x)], [])
        # TypeError: can only concatenate list (not "NoneType") to list
        path = find_path(branch, x) if find_path(branch, x) != None else []
        if x in path:
            return [label(tree)] + path


# 2.2
def prune_binary(t, nums):
    """
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> prune_binary(t, ['01', '110', '100'])
    >>> ['1', ['0', ['0']], ['1', ['0']]]
    """

    if is_leaf(t):
        if any(str(label(t)) == num[0] for num in nums):
            return t
        return None
    else:
        next_valid_nums = sum([[num[1:]]
                               for num in nums if num[0] == str(label(t))], [])
        new_branches = []
        for branch in branches(t):
            pruned_branch = prune_binary(branch, next_valid_nums)

            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)
