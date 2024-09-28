# Booleans are most useful when combined with conditional
# statements, using the keywords if, elif, and else.

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")


inspect(0)
inspect(-15)


# The if and else keywords are often used
# in other languages; its more unique keyword is elif, a
# contraction of "else if". In these conditional clauses,
# elif and else blocks are optional;

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)


f(1)
f(0)

# ------ Combining Boolean Values ------
# We've seen int(), which turns things into ints, and float(), which turns
# things into floats, so you might not be surprised to hear that Python has a
# bool() function which turns things into bools.
print(bool(1))  # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf"))  # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

# We can use non-boolean objects in if conditions and other
# places where a boolean would be expected.
if 0:
    print(0)
elif "spam":
    print("spam")
