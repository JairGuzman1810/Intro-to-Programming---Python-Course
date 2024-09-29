squares = [n ** 2 for n in range(10)]
print(squares)

# Here's how we would do the same thing without a list comprehension:
squares = []
for n in range(10):
    squares.append(n ** 2)
print(squares)

# We can also add an if condition:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
# (If you're familiar with SQL, you might think of this as being like a "WHERE" clause)


# Here's an example of filtering with an if condition
# and applying some transformation to the loop variable:
# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

"""
People usually write these on a single line, 
but you might find the structure clearer when it's split up over 3 lines:

[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

List comprehensions combined with functions like min, 
max, and sum can lead to impressive one-line solutions for 
problems that would otherwise require several lines of code.

For example, compare the following two cells of code that do the same thing.

"""


def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative


# Here's a solution using a list comprehension:
def count_negatives_one_line(nums):
    return len([num for num in nums if num < 0])


def count_negatives_more_simple(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
