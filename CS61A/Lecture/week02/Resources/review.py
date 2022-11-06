# Question 8
def summation(n, term):
    """Computes the summation of the first n numbers in the
    sequence defined by the function term.

    >>> square = lambda x: x * x
    >>> summation(5, square)
    55
    """
    "*** YOUR CODE HERE ***"
    i, sum = 1, 0
    while i <= n:
        sum += term(i)
        i += 1

    return sum


# Question 9
def is_fib(n):
    """Returns True if n is a fibonacci number,
    else False

    >>> is_fib(8)
    True
    >>> is_fib(9)
    False
    """
    "*** YOUR CODE HERE ***"
    first, second = 0, 1
    if n == first or n == second:
        return True
    i = first + second
    while i < n:
        first, second = second, i
        i = first + second

    if i == n:
        return True
    return False

    # solution
    #
    # def is_fib(n):
    # cur, next = 0, 1
    # while cur < n:
    #     cur, next = next, cur + next
    # return cur == n


# http://albertwu.org/cs61a/review/control/exam.html
# Question 2
def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    "*** YOUR CODE HERE ***"
    end = 0
    while n:
        if end > n % 10:
            return False
        n, end = n // 10, n % 10
    return True


# Question 3
def count_one(n):
    """Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n:
        if n % 10 == 1:
            count += 1
        n = n // 10
    return count


# Question 4
def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while n:
        total += count_one(n)
        n -= 1
    return total
