# basic


# Q7
def link_to_list(lst):
    """Returns a list that contains the same elements as the
    linked list.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(r)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return []

    return [first(lst)] + link_to_list(rest(lst))


# Q8
def map_link(lst, f):
    """Maps f onto each element in the linked list.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(map_link(r, lambda x: x**2))
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return lst

    return link(f(first(lst)), map_link(rest(lst), f))


# ADT
empty = None


def link(first, rest=empty):
    return [first, rest]


def first(s):
    return s[0]


def rest(s):
    return s[1]


# exam
# Q3
def alternate(lst):
    """Returns a new linked list that contains every other element
    of the original.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(alternate(r))
    [1, 3]
    >>> r = link(1, link(2, link(3, link(4, empty))))
    >>> link_to_list(alternate(r))
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return lst

    if rest(lst) == empty:
        return lst

    return link(first(lst), alternate(rest(rest(lst))))


# Q4
def filter_link(pred, lst):
    """Returns a new link that contains elements of lst that
    satisfy the predicate.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(filter_link(lambda x: x % 2 == 1, r))
    [1, 3]
    >>> r = link(1, link(2, link(3, link(4, empty))))
    >>> link_to_list(filter_link(lambda x: x % 3 == 1, r))
    [1, 4]
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return lst

    if pred(first(lst)):
        return link(first(lst), filter_link(pred, rest(lst)))

    return filter_link(pred, rest(lst))