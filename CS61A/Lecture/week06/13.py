# Q&A
""""
>>> min([3, 2, 5, 6], key=lambda x: abs(x * x - 24))
5
>>> f = lambda x: abs(x * x - 24)
>>> [f(x) for x in [3, 2, 5, 6]]
[15, 20, 1, 12]

>>> [15, 3] < [20, 2]
True
>>> f = lambda x: abs(x * x - 24)
>>> [[f(x), x] for x in [3, 2, 5, 6]]
[[15, 3], [20, 2], [1, 5], [12, 6]]
>>> min([[f(x), x] for x in [3, 2, 5, 6]])
[1, 5]

>>> min([[f(x), x] for x in [3, 2, 5, 6]])[1]
5
>>> min([3, 2, 5, 6], key=abs)
2
>>> def f(x, y):
...     return abs(x * x - y)
>>> min([3, 2, 5, 6], key=lambda x: f(x, 24))
5

"""
min([3, 2, 5, 6], key=lambda x: abs(x * x - 24))

f = lambda x: abs(x * x - 24)

[f(x) for x in [3, 2, 5, 6]]

min([[f(x), x] for x in [3, 2, 5, 6]])

min([[f(x), x] for x in [3, 2, 5, 6]])[1]

min([3, 2, 5, 6], key=abs)


def f(x, y):
    return abs(x * x - y)


min([3, 2, 5, 6], key=lambda x: f(x, 24))

[15, 3] < [20, 2]
