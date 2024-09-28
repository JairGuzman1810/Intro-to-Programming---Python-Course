# Booleans represent one of two values: True or False
z_one = True
print(z_one)
# which in this case is <class 'bool'>
print(type(z_one))

z_two = False
print(z_two)
print(type(z_two))

# Booleans are used to represent the truth value of an expression.
z_three = (1 < 2)
print(z_three)
print(type(z_three))

# Similarly, since 5 < 3 is a false statement, return False
z_four = (5 < 3)
print(z_four)
print(type(z_four))

# We can switch the value of a boolean by using not.
# So, not True is equivalent to False, and not False becomes True.
z_five = not z_four
print(z_five)
print(type(z_five))
