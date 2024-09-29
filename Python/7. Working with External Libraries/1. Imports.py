import math

# We'll start our example by importing math from the standard library.

print("It's math! It has type {}".format(type(math)))

# math is a module. A module is just a collection of variables
# (a namespace, if you like) defined by someone else.
print(dir(math))

# We can access these variables using dot syntax. Some
# of them refer to simple values, like math.pi:
print("pi to 4 significant digits = {:.4}".format(math.pi))

# But most of what we'll find in the module are functions, like math.log:
print(math.log(32, 2))

help(math.log)

# Other import syntax
import math as mt

# If we know we'll be using functions in math frequently we can import it
# under a shorter alias to save some typing (though in this case "math"
# is already pretty short).
print(mt.pi)

# The as simply renames the imported module. It's equivalent to doing something like:
# import math
# mt = math

# Wouldn't it be great if we could refer to all the variables in the math module by themselves?
from math import *

print(pi, log(32, 2))

# A good compromise is to import only the specific things we'll need from each module:
# from math import log, pi
# from numpy import asarray

# Submodules
import numpy

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
      )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# ------ Three tools for understanding strange objects ------
print(type(rolls))

print(dir(rolls))

# If I want the average roll, the "mean" method looks promising...
print(rolls.mean())

# Or maybe I just want to turn the array into a list, in which case I can use "tolist"

print(type(rolls.tolist()))

# That "ravel" attribute sounds interesting. I'm a big classical music fan.
help(rolls.ravel)

# Operator overloading
# What's the value of the below expression?
# print([3, 4, 1, 2, 2, 1] + 10) What a silly question. Of course it's an error.


print(rolls + 10)

# At which indices are the dice less than or equal to 3?
print(rolls <= 3)

xlist = [[1, 2, 3], [2, 4, 6], ]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# Get the last element of the second row of our numpy array
print(x[1, -1])
