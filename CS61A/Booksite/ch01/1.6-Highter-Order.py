# 1.6.1

# >>> def sum_naturals(n):
#         total, k = 0, 1
#         while k <= n:
#             total, k = total + k, k + 1
#         return total
# >>> sum_naturals(100)
# 5050

# >>> def sum_cubes(n):
#         total, k = 0, 1
#         while k <= n:
#             total, k = total + k*k*k, k + 1
#         return total
# >>> sum_cubes(100)
# 25502500

# >>> def pi_sum(n):
#         total, k = 0, 1
#         while k <= n:
#             total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
#         return total
# >>> pi_sum(100)
# 3.1365926848388144

# ======================= #

# def <name>(n):
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + <term>(k), k + 1
#     return total

# >>> def summation(n, term):
#         total, k = 0, 1
#         while k <= n:
#             total, k = total + term(k), k + 1
#         return total
#
# >>> def identity(x):
#         return x
#
# >>> def sum_naturals(n):
#         return summation(n, identity)
#
# >>> sum_naturals(10)
# 55
#
# >>> summation(10, square)
# 385

# >>> def pi_term(x):
#         return 8 / ((4*x-3) * (4*x-1))
#
# >>> def pi_sum(n):
#         return summation(n, pi_term)
#
# >>> pi_sum(1e6)
# 3.141592153589902
#

# =================================
# 1.6.2

# def square_root(a):
#     x = 1
#     while x * x != a:
#         x = square_root_update(x, a)
#     return x

# def cube_root(a):
#     x = 1
#     while x*x*x != a:
#         x = cube_root_update(x, a)
#     return x


def square_root_update(x, a):
    return (x + a / x) / 2


def cube_root_update(x, a):
    return (2 * x + a / (x * x)) / 3


def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k += 1
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def square_root(a):

    def update(x):
        return square_root_update(x, a)

    def close(x):
        return approx_eq(x * x, a)

    return improve(update, close)


def cube_root(a):
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(x * x * x, a))


# 1.6.5
def newton_update(f, df):

    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):

    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):

    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


# >>> square_root_newton(64)
# 8.0


def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):

    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


# >>> nth_root_of_a(2, 64)
# 8.0
# >>> nth_root_of_a(3, 64)
# 4.0
# >>> nth_root_of_a(6, 64)
# 2.0

# ===============
# 1.6.6
