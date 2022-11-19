from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i, k = 0, 0
    while k < 10:
        if has_digit(n, k):
            i += 1
        k += 1
    return i

    # BearSir's better
    # count = 0
    # while n > 0:
    #     if not has_digit(n // 10, n % 10):
    #         count += 1
    #     n //= 10
    # return count


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    # in a positive integer (1..n) 无需考虑 n = 0
    # if n == k:
    #     return True
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    r = 9
    while x > 0:
        l = x % 10
        if l > r:
            return False
        x, r = x // 10, l
    return True


def get_k_run_starter(n, k):
    """
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while (n > 9) and (n % 10) > ((n % 100) // 10):
            n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"

    def repeater(x):
        num = n
        while num > 1:
            x = composer(func, func)(x)
            num -= 2
        return func(x) if num == 1 else x

    return repeater

    # BearSir's perfect
    # f = lambda x: x
    # while n > 0:
    #     f = composer(func, f)
    #     n -= 1
    # return f


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""

    def f(x):
        return func1(func2(x))

    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func, 2)


# # Q6: Doge
# wow = 6
# def much(wow):
#     if much == wow:
#         such = lambda wow: 5
#         def wow():
#             return such
#         return wow
#     such = lambda wow: 4
#     return wow()
# wow = much(much(much))(wow)
# 5

# challenge 1
# def funny(joke):
#     hoax = joke + 1
#     return funny(hoax)
# def sad(joke):
#     hoax = joke - 1
#     return hoax + hoax
# funny, sad = sad, funny
# result = funny(sad(1))
# # 2

# challenge 2
# def double(x):
#     return double(x + x)
# first = double
# def double(y):
#     return  y + y
# result = first(10)
# 40


def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love UCB", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love UCB
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """

    def get_secret(password_attempt):
        "*** YOUR CODE HERE ***"

        if num_attempts == 0:
            print('SECRET LOCKED')
            return protected_secret(password, secret, 0)
        elif password_attempt == password:
            print(secret)
            return protected_secret(password, secret, num_attempts)
        else:
            print('INCORRECT PASSWORD')
            return protected_secret(password, secret, num_attempts - 1)

    return get_secret
