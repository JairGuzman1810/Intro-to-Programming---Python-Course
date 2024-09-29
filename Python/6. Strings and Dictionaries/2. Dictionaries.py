# Dictionaries are a built-in Python data structure for mapping keys to values.
numbers = {'one': 1, 'two': 2, 'three': 3}
print(numbers['one'])

# We can use the same syntax to add another key, value pair
numbers['eleven'] = 11
print(numbers)

# Or to change the value associated with an existing key
numbers['one'] = 'Pluto'
print(numbers)

# Python has dictionary comprehensions with a syntax similar to
# the list comprehensions we saw in the previous tutorial.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# The in operator tells us whether something is a key in the dictionary
print('Saturn' in planet_to_initial)

print('Betelgeuse' in planet_to_initial)

# A for loop over a dictionary will loop over its keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# We can access a collection of all the keys or all the
# values with dict.keys() and dict.values(), respectively.
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))

# The very useful dict.items() method lets us iterate
# over the keys and values of a dictionary simultaneously.
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
