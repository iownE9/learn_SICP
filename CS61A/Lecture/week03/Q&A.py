# lecture07
"""
Definitions. A repeatable integer function takes an integer argument and returns a repeatable integer function.

(a) (6 pt) Implement repeat, which is a repeatable integer function that detects repeated arguments. As a side
effect of repeated calls, it prints each argument that has been used before in a sequence of repeated calls.
Therefore, if an argument appears n times, it is printed n- 1 times in total, each time other than the first.

The detector function is part of the implementation of repeat; you must determine how it is used.

Important: You may not use a list, set, or any other data type not covered yet in the course.

"""

# def repeat(k):
#     """When called repeatedly, print each repeated argument.

#     >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
#     7
#     1
#     5
#     1
#     """
#     return detector(lambda i: i == k)(k)

# def detector(f):

#     def g(i):
#         if f(i):
#             print(i)
#         return detector

#     return g

# 依靠栈帧保存值
# 相互返回彼此，实现chain调用


def repeat(k):
    """When called repeatedly, print each repeated argument.
    
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)


def detector(f):

    def g(i):
        if f(i):
            print(i)
        return detector(lambda j: j == i or f(j))
        #  or f(j)   点睛之笔

    return g
