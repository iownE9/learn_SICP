# Implementing Function


def remove(n, digit):
    """Return all digits of non-negative N
        that are not DIGIT,for some
        non-negative DIGIT less than 10.
    >>> remove (231,3)
    21
    >>> remove(243132,2)
    4313
    """
    kept, digits = 0, 0
    while n:
        n, last = n // 10, n % 10
        if last != digit:
            # kept = last * pow(10, digits) + kept
            kept = last * 10**digits + kept
            digits = digits + 1

    return kept


# Read the description

# Verify the examples & pick a simple one

# Read the template

# Implement without the template, then change
# your implementation to match the template.
# OR
# If the template is helpful, use it.
