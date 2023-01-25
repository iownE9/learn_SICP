# Object Abstraction

# We will consider three different techniques for implementing generic functions:
# shared interfaces, type dispatching, and type coercion


# Callable objects
def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """

    def adder(k):
        return n + k

    return adder


class Adder(object):
    """
    >>> add_three_obj = Adder(3)
    >>> add_three_obj(4)
    7
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, k):
        return self.n + k


# 2.7.3   Multiple Representations
class Number:

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


class Complex(Number):

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


# ComplexRI constructs a complex number from real and imaginary parts.
# ComplexMA constructs a complex number from a magnitude and angle.

from math import atan2


class ComplexRI(Complex):
    """
    >>> ri = ComplexRI(5, 12)
    >>> ri.real
    5
    >>> ri.magnitude
    13.0
    >>> ri.real = 9
    >>> ri.real
    9
    >>> ri.magnitude
    15.0
    """

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real**2 + self.imag**2)**0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)


from math import sin, cos, pi


class ComplexMA(Complex):
    """
    >>> ma = ComplexMA(2, pi/2)
    >>> ma.imag
    2.0
    >>> ma.angle = pi
    >>> ma.real
    -2.0
    """

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude,
                                                     self.angle / pi)


def test_complex():
    """
    shared interfaces 借此实现了 + 的泛型化
    >>> from math import pi
    >>> ComplexRI(1, 2) + ComplexMA(2, pi/2)
    ComplexRI(1, 4)
    >>> ComplexRI(0, 1) * ComplexRI(0, 1)
    ComplexMA(1, 1 * pi)
    """
    pass


# 2.7.4   Generic Functions
from fractions import gcd


class Rational(Number):
    """
    >>> Rational(2, 5) + Rational(1, 10)
    Rational(1, 2)
    >>> Rational(1, 4) * Rational(2, 3)
    Rational(1, 6)
    """

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)

    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)


# Type dispatching
def test_():
    """
    >>> c = ComplexRI(1, 1)
    >>> isinstance(c, ComplexRI)
    True
    >>> isinstance(c, Complex)
    True
    >>> isinstance(c, ComplexMA)
    False
    """
    pass


def is_real(c):
    """
    >>> is_real(ComplexRI(1, 1))
    False
    >>> is_real(ComplexMA(2, pi))
    True
    """
    """Return whether c is a real number with no imaginary part."""
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0


def test_2():
    """
    give a type_tag attribute 

    >>> Rational.type_tag = 'rat'
    >>> Complex.type_tag = 'com'
    >>> Rational(2, 5).type_tag == Rational(1, 2).type_tag
    True
    >>> ComplexRI(1, 1).type_tag == ComplexMA(2, pi/2).type_tag
    True
    >>> Rational(2, 5).type_tag == ComplexRI(1, 1).type_tag
    False
    """
    pass


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer / r.denom, c.imag)


def mul_complex_and_rational(c, r):
    # The angle 0 indicates a positive number. The angle pi indicates a negative number.
    r_magnitude, r_angle = r.numer / r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)


# commutative 交换律
def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)


def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


# 重写 Number 基类
class Number:

    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)  # 同类型
        elif (self.type_tag, other.type_tag) in self.adders:  # 是否可以跨类型 +
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    adders = {
        ("com", "rat"): add_complex_and_rational,
        ("rat", "com"): add_rational_and_complex
    }
    multipliers = {
        ("com", "rat"): mul_complex_and_rational,
        ("rat", "com"): mul_rational_and_complex
    }


def test_3():
    """
    >>> ComplexRI(1.5, 0) + Rational(3, 2)
    ComplexRI(3, 0)
    >>> Rational(-1, 2) * ComplexMA(4, pi/2)
    ComplexMA(2, 1.5 * pi)
    """
    pass


# Coercion 强制类型转换
def rational_to_complex(r):
    return ComplexRI(r.numer / r.denom, 0)


class Number:

    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))

    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)

    coercions = {('rat', 'com'): rational_to_complex}
