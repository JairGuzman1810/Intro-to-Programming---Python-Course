# Loops are a way to repeatedly execute some code.
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')  # print all on same line
# The for loop specifies
# the variable name to use (in this case, planet)
# the set of values to loop over (in this case, planets)
print("\n")
# In addition to lists, we can iterate over the elements of a tuple:
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

# even loop through each character in a string:
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

# range() is a function that returns a sequence of numbers.
for i in range(5):
    print("Doing important work. i =", i)

# ------ while loops ------
# The other type of loop in Python is a while
# loop, which iterates until some condition is met:
i = 0
while i < 10:
    print(i, end=' ')
    i += 1  # increase the value of i by 1
