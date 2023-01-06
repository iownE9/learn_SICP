# 14.pdf


# basic review
# Q5
def foo():
    lst = []

    def bar(m):
        nonlocal lst
        lst = lst + [m]
        return lst

    return bar


# Q6
def foo():
    lst = []

    def bar(m):
        lst.append(m)
        return lst

    return bar


# exam review
# Q1
def make_sassy_function(f, msg):
    """Returns a version of f that only works every other function
    call.

    >>> f = lambda x: x**2
    >>> sassy_f = make_sassy_function(f, 'Um, excuse me?')
    >>> sassy_f(4)
    16
    >>> sassy_f(5)
    'Um, excuse me?'
    >>> sassy_f(6)
    36
    >>> g = lambda x, y: x*y
    >>> sassy_g = make_sassy_function(g, "Ain't nobody got time for that!")
    >>> sassy_g(1, 2)
    2
    >>> sassy_g(5, 4)
    "Ain't nobody got time for that!"
    """
    sassy = True

    # 可变参数
    def fn(*args):
        nonlocal sassy
        sassy = not sassy

        if sassy:
            return msg
        return f(*args)

    return fn


# Q2
def sentence_buffer():
    """Returns a function that will return entire sentences when it
    receives a string that ends in a period.

    >>> buffer = sentence_buffer()
    >>> buffer("This")
    >>> buffer("is")
    >>> buffer("Spot.")
    'This is Spot.'
    >>> buffer("See")
    >>> buffer("Spot")
    >>> buffer("run.")
    'See Spot run.'
    """
    "*** YOUR CODE HERE ***"
    sentence = ""

    def buffer(word):
        nonlocal sentence
        sentence += word

        if '.' in word:
            res, sentence = sentence, ''
            return res

        sentence += ' '

    return buffer