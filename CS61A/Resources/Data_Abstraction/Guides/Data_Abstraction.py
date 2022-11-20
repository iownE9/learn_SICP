# Functions
def is_odd(x):
    if x % 2 == 1:
        return True
    return False


# What We Can Do
def numbers():
    print("one")
    print("two")
    print("two")
    print("three")
    print("three")
    print("three")
    print("four")
    print("four")
    print("four")
    print("four")


def numbers():
    for _ in range(0, 1):  #repeats once
        print("one")
    for _ in range(0, 2):  #repeats twice
        print("two")
    for _ in range(0, 3):  #repeats three times
        print("three")
    for _ in range(0, 4):  #repeats four times
        print("four")


# the only things that are different between each of the for loops are:
# 1. The number of iterations
# 2. The word that’s printed
def repeat_print(w, n):
    for _ in range(n):  #repeats n
        print(w)


def numbers():
    repeat_print("one", 1)
    repeat_print("two", 2)
    repeat_print("three", 3)
    repeat_print("four", 4)


def numbers():
    words = ["one", "two", "three", "four"]
    for i in range(0, 4):
        repeat_print(words[i], i + 1)


# Modularity


def numbers(words, start):
    for i in range(0, len(words)):
        repeat_print(words[i], start + i + 1)


# Deconstructing the Problem
# We’re assuming we have:
#     ● A function that takes in 4 coordinate points and returns a square
#     ● A function that takes in an x and a y value and returns a coordinate point


def make_square(p1, p2, p3, p4):
    return [p1, p2, p3, p4]


def make_point(x, y):
    return [x, y]


square = make_square(make_point(0, 0), make_point(1, 0), make_point(1, 1),
                     make_point(0, 1))


# generalize
def make_polygon(*args):
    return args


square = make_polygon(make_point(0, 0), make_point(1, 0), make_point(1, 1),
                      make_point(0, 1))
