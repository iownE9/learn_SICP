# 13-Trees.pdf


# review Linked list
def insert(lst, item, index):
    if lst == empty:
        return link(item)
    elif index == 0:
        return link(item, lst)

    new = insert(rest(lst), item, index - 1)
    return link(first(lst), new)


def sum_tree(t):
    if is_leaf(t):
        return entry(t)

    total = entry(t)
    for s in subtrees(t):
        total += sum_tree(s)
    return total


def sum_tree(t):
    lst = [sum_tree(s) for s in subtrees(t)]
    return entry(t) + sum(lst)


def map_tree(t, fn):
    if is_leaf(t):
        return tree(fn(entry(t)))

    subs = []
    for s in subtrees(t):
        subs += [map_tree(s, fn)]
    return tree(fn(entry(t)), subs)


def map_tree(t, fn):

    subs = [map_tree(s, fn) for s in subtrees(t)]
    return tree(fn(entry(t)), subs)


# exam review
# Q1
def contains(t, e):
    if root(t) == e:
        return True
    elif is_leaf(t):
        return False

    return any([contains(s, e) for s in subtrees(t)])


# Q2
def all_paths(t):
    if is_leaf(t):
        return [[root(t)]]

    return [[root(t)] + i
            for i in sum([all_paths(s) for s in subtrees(t)], [])]


# Q3
def max_tree(t):
    if is_leaf(t):
        return tree(root(t))

    new_subtrees = [max_tree(s) for s in subtrees(t)]
    new_root = max([root(t)] + [root(s) for s in new_subtrees])
    return tree(new_root, new_subtrees)


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


# Linked list ADT
empty = None


def link(first, rest=empty):
    return [first, rest]


def first(s):
    return s[0]


def rest(s):
    return s[1]
