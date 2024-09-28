# When we called help(print), we saw that the print
# function has several optional arguments.

# For example, we can specify a value for sep
print(1, 2, 3, sep=' < ')

# But if we don't specify a value, sep is treated as
# having a default value of ' ' (a single space).
print(1, 2, 3)


# Adding optional arguments with default values to the functions
def greet(who="Colin"):
    print("Hello,", who)


greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
