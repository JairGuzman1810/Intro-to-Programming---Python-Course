# ------ String syntax ------
# strings in Python can be defined using either single or
# double quotations. They are functionally equivalent.
x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

# Double quotes are convenient if your string contains a single
# quote character (e.g. representing an apostrophe).
# Similarly, it's easy to create a string that contains
# double-quotes if you wrap it in single quotes:
print("Pluto's a planet!")
print('My dog is named "Pluto"')

# If we try to put a single quote character
# inside a single-quoted string, Python gets confused:
# print('Pluto's a planet!') ---> SyntaxError: unterminated string literal (detected at line 17)

# We can fix this by "escaping" the single quote with a backslash.
print('Pluto\'s a planet!')

# Escaping single quotes
example_1 = 'What\'s up?'
print(example_1)  # Output: What's up?

# Escaping double quotes
example_2 = "That's \"cool\""
print(example_2)  # Output: That's "cool"

# Escaping a backslash
example_3 = "Look, a mountain: /\\"
print(example_3)  # Output: Look, a mountain: /\

# New line with \n
example_4 = "1\n2 3"
print(example_4)  # Output:
# 1
# 2 3


# newline character. It causes Python to start a new line.
hello = "hello\nworld"
print(hello)

# Python's triple quote syntax for strings lets us include newlines literally (i.e. by just
# hitting 'Enter' on our keyboard, rather than using the special '\n' sequence).
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

# The print() function automatically adds a newline character unless we
# specify a value for the keyword argument end other than the default value of '\n':
print("hello")
print("world")
print("hello", end='')
print("pluto")

# ------ Strings are sequences ------
# Strings can be thought of as sequences of characters.
# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# How long is this string?
print(len(planet))

# we can even loop over them
print([char + '! ' for char in planet])

# We can't modify them.
# planet[0] = 'B'
# planet.append doesn't work either

# ------ String methods ------
# the type str has lots of very useful methods.

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())

# all lowercase
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))

print(claim.startswith(planet))

# false because of missing exclamation mark
print(claim.endswith('planet'))

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

print(year, month, day)

print('/'.join([month, day, year]))

# we can put Unicode characters right in our string literals
print(' 👏 '.join([word.upper() for word in words]))

# Building strings with .format()
print(planet + ', we miss you.')

# If we want to throw in any non-string objects,
# we have to be careful to call str() on them first
position = 9
# print(planet + ", you'll always be the " + position + "th planet to me.")
# TypeError: can only concatenate str (not "int") to str
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

# This is getting hard to read and annoying to type. str.format() to the rescue.
print("{}, you'll always be the {}th planet to me.".format(planet, position))
# we didn't even have to call str() to convert position from an
# int. format() takes care of that for us.

pluto_mass = 1.303 * 10 ** 22
earth_mass = 5.9722 * 10 ** 24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas

print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population, ))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

help(str)
