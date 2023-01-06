# exam review
# Q5
class CircularBuffer:
    """Doctests:

    >>> buffer = CircularBuffer(3)
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('a')
    >>> buffer.remove()
    'a'
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('b')
    >>> buffer.append('c')
    >>> buffer.append('d')
    >>> buffer.append('e')
    Buffer capacity exceeded
    >>> buffer.remove()
    'b'
    >>> buffer.remove()
    'c'
    >>> buffer.remove()
    'd'
    >>> buffer.remove()
    Buffer is empty
    """

    def __init__(self, n):
        self.array = [None] * n  # list of length n
        self.n = n
        self.start = 0
        self.end = 0

    def append(self, elem):
        "*** YOUR CODE HERE ***"
        if self.start - self.end >= self.n:
            print("Buffer capacity exceeded")
        else:
            self.array[self.start % self.n] = elem
            self.start += 1

    def remove(self):
        "*** YOUR CODE HERE ***"
        if self.start == self.end:
            print("Buffer is empty")
        else:
            elem = self.array[self.end % self.n]
            self.end += 1
            return elem


# Q6
class Chef:
    """Doctests:

    >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
    >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
    >>> ramsay.cook()
    'Not enough ingredients!'
    >>> ramsay.serve()
    'No food to serve!'
    >>> ramsay.fetch_ingredients()     # 1 salt remaining
    "Fetched: ['meat', 'bbq sauce', 'salt']"
    >>> ramsay.cook()
    'Cooked steak!'
    >>> ramsay.serve()
    >>> Chef.finished
    ['steak']
    >>> albert.fetch_ingredients()     # 0 salt remaining
    "Fetched: ['egg', 'cheese', 'cream', 'salt']"
    >>> albert.cook()
    'Cooked quiche!'
    >>> albert.serve()
    >>> Chef.finished
    ['steak', 'quiche']
    >>> ramsay.fetch_ingredients()
    'No more salt!'
    """
    "*** YOUR CODE HERE ***"
    storage = {}
    finished = []

    def __init__(self, food, ingredients):
        self.food, self.ingredients = food, ingredients
        self.fetched, self.cooked = False, False
        for elem in self.ingredients:
            Chef.storage[elem] = 2

    def fetch_ingredients(self):
        for elem in self.ingredients:
            if Chef.storage[elem] == 0:
                return 'No more ' + elem + '!'
            Chef.storage[elem] -= 1
        self.fetched = True
        return 'Fetched: ' + str(self.ingredients)

    def cook(self):
        if self.fetched:
            self.cooked, self.fetched = True, False
            return 'Cooked ' + self.food + '!'
        return 'Not enough ingredients!'

    def serve(self):
        if not self.cooked:
            return 'No food to serve!'
        Chef.finished.append(self.food)
        self.cooked = False