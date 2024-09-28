def mult_by_five(x):
    # Multiplies the input 'x' by 5 and returns the result
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    # Takes a function 'fn' and an argument 'arg',
    # and calls 'fn' with 'arg' as its argument
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    # Takes a function 'fn' and an argument 'arg',
    # calls 'fn' on 'arg', then calls 'fn' again on the result
    return fn(fn(arg))


# Test the functions and print the results
# First, calls mult_by_five with argument 1
# Second, calls squared_call which applies mult_by_five twice
print(
    call(mult_by_five, 1),  # Outputs 5 (mult_by_five(1))
    squared_call(mult_by_five, 1),  # Outputs 25 (mult_by_five(mult_by_five(1)) = 5 * 5)
    sep='\n',  # '\n' is the newline character, used to print each result on a new line
)


# Functions that operate on other functions are called "higher-order functions."
# Here's an interesting example using the max function.

def mod_5(x):
    # Returns the remainder when 'x' is divided by 5 (this is the modulo operation)
    return x % 5


# Print statements
print(
    'Which number is biggest?',
    # This compares 100, 51, and 14, and returns the largest number (100)
    max(100, 51, 14),

    'Which number is the biggest modulo 5?',
    # This compares the numbers 100, 51, and 14 based on the result of mod_5
    # max will apply mod_5 to each number:
    # 100 % 5 = 0, 51 % 5 = 1, and 14 % 5 = 4
    # Since 14 gives the largest remainder (4), max returns 14
    max(100, 51, 14, key=mod_5),

    sep='\n',  # '\n' is the newline character, meaning each result will be printed on a new line
)
