# Builtin functions are great, but we can only get so far
# with them before we need to start defining our own functions.

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    # Calculate the absolute difference between 'a' and 'b'
    diff1 = abs(a - b)

    # Calculate the absolute difference between 'b' and 'c'
    diff2 = abs(b - c)

    # Calculate the absolute difference between 'a' and 'c'
    diff3 = abs(a - c)

    # Return the smallest of the three differences
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),  # Python allows trailing commas in argument lists. How nice is that?
)

help(least_difference)
