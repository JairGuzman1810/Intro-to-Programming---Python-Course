# Python has a type of variable called bool. It has two possible values: True and False.
x = True
print(x)
print(type(x))


# ------ Comparison Operations ------
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

# Comparisons frequently work like you'd hope
print(3.0 == 3)

# But sometimes they can be tricky
print('3' == 3)


# we can check if a number is odd by checking that the modulus with 2 returns 1:
def is_odd(n):
    return (n % 2) == 1


print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))


# ------ Combining Boolean Values ------
# We can combine boolean values using the standard concepts
# of "and", "or", and "not". In fact, the words to do this are: and, or, and not.

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))
