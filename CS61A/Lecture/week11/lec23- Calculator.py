def demo():
    """"
    >>> def square(x):
    ...     return x * x
    ...
    >>> square(3)
    9
    >>> from dis import dis
    >>> dis(square)
    2           0 LOAD_FAST                0 (x)
                2 LOAD_FAST                0 (x)
                4 BINARY_MULTIPLY
                6 RETURN_VALUE
    >>>   
    """
    pass
