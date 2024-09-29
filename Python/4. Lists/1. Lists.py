# Lists in Python represent ordered sequences of values.
primes = [2, 3, 5, 7]

print(primes)

# We can put other types of things in lists:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# We can even make a list of lists:
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

print(hands)

# A list can contain a mix of different types of variables:
my_favourite_things = [32, 'raindrops on roses', help]

# ------ Indexing ------
# You can access individual list elements with square brackets.
print(planets[0])

# Elements at the end of the list can be accessed with negative numbers, starting from -1:

print(planets[-1])

# ------ Slicing ------
print(planets[0:3])

# planets[0:3] is our way of asking for the elements of planets
# starting from index 0 and continuing up to but not including index 3.

# The starting and ending indices are both optional.
# If I leave out the start index, it's assumed to be 0.
print(planets[:3])

# If I leave out the end index, it's assumed to be the length of the list.
print(planets[3:])

# We can also use negative indices when slicing:
# All the planets except the first and last
print(planets[1:-1])

# The last 3 planets
print(planets[-3:])

# ------ Changing lists ------
# Lists are "mutable", meaning they can be modified "in place".
# For example, let's say we want to rename Mars:
planets[3] = 'Malacandra'
print(planets)

# Shortening the names of the first 3 planets.
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars', ]

# ------ List functions ------
# Python has several useful functions for working with lists.

# len gives the length of a list:
# How many planets are there?
print(len(planets))

# sorted returns a sorted version of a list:
# The planets sorted in alphabetical order
print(sorted(planets))

# Min and max
print(max(primes))

# ------ Interlude: objects ------
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

# For example, numbers have a method called bit_length. Again, we access it using dot syntax:
print(x.bit_length())

# ------ List methods ------
# list.append modifies a list by adding an item to the end:
# Pluto is a planet darn it!
planets.append('Pluto')
print(planets)

# list.pop removes and returns the last element of a list:
planets.pop()
print(planets)

# Searching lists
print(planets.index('Earth'))

# we can use the in operator to determine whether a list contains a particular value:
print("Earth" in planets)

# Is Calbefraques a planet?
print("Calbefraques" in planets)

# ------ Tuples ------
# Tuples are almost exactly the same as lists. They differ in just two ways.
# 1: The syntax for creating them uses parentheses instead of square brackets
t = (1, 2, 3)  # t = 1, 2, 3  equivalent

print(t)

# 2: They cannot be modified (they are immutable).
# t[0] = 100
# Tuples are often used for functions that have multiple return values.

# For example, the as_integer_ratio() method of float objects
# returns a numerator and a denominator in the form of a tuple:
x = 0.125
print(x.as_integer_ratio())

# These multiple return values can be individually assigned as follows:
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

# swapping two variables
a = 1
b = 0
a, b = b, a
print(a, b)
