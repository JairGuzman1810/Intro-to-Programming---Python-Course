# Collection of characters (like alphabet letters, punctuation,
# numerical digits, or symbols) contained in quotation marks.
w = "Hello, Python!"
print(w)
# Print the data type of the variable w, which in this case is <class 'str'> (string)
print(type(w))

# Get the length of a string with len().
print(len(w))

# Special type of string, empty string
shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

# Number in quotation marks === string data
my_number = "1.12321"
print(my_number)
print(type(my_number))

# We can convert the string to a float, if its valid
also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

# Concatenating strings
new_string = "abc" + "def"
print(new_string)
print(type(new_string))

# It's not possible to do subtraction or division with 2 strings,
# but we can multiply by an integer.
newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))
