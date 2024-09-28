# Floats are numbers with fractional parts. They can have many numbers after decimal.
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
# Print the data type of the variable nearly_pi,
# which in this case is <class 'float'>
print(type(nearly_pi))

# Float with a fraction
almost_pi = 22 / 7
print(almost_pi)
print(type(almost_pi))

# One function that is particularly useful for fractions is
# the round() function. It lets you round a number to a specified
# number of decimal places.

# Round to 5 decimal places
rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

# Whenever you write an number with a decimal point,
# Python recognizes it as a float data type.
y_float = 1.
print(y_float)
print(type(y_float))
