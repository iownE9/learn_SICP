# base


# Question 5
def geo_sum(a, r, n):
    """Returns the first n elements of a geometric series.

    >>> geo_sum(1, 1/2, 4)  # 1 + 1/2 + 1/4 + 1/8
    1.875
    >>> geo_sum(2, 2, 3)  # 2 + 4 + 8
    14
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return a
    return a + geo_sum(a * r, r, n - 1)


# Question 6
def num_primes(n):
    """Returns the number of primes less than or equal to n.

    >>> num_primes(6)   # 2, 3, 5
    3
    >>> num_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return 0

    return 1 + num_primes(n - 1) if is_prime(n) else num_primes(n - 1)


def is_prime(i):
    m = 2
    while m * m <= i:
        if i % m == 0:
            return False
        m += 1
    return True


# Question 7
def any(a, b, pred):
    """Returns True if any numbers from a to b inclusive satisfy
    pred.

    >>> any(1, 4, lambda x: x % 2 == 0)
    True
    >>> any(-5, 2, lambda x: x * x == -3 * x)   # -3 satisfies pred
    True
    >>> any(1, 6, lambda x: x % 7 == 0)
    False
    >>> any(0, 6, lambda x: x % 7 == 0)
    True
    """
    "*** YOUR CODE HERE ***"
    if a > b:
        return False
    return pred(a) or any(a + 1, b, pred)


# exam http://albertwu.org/cs61a/review/recursion/exam.html
# Question 1
def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    "*** YOUR CODE HERE ***"
    if number < 1:
        return False
    if 0 < number < 4:
        return True

    return not (can_win(number - 1) and can_win(number - 2)
                and can_win(number - 3))


def can_win2(number):
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win2(new_state):
            return True
        action += 1
    return False