# It can also use conditional statements to perform different calculations.
def get_taxes(earnings):
    # If earnings are less than 12,000, calculate tax at 25%
    if earnings < 12000:
        tax_owed = 0.25 * earnings
    # Otherwise, calculate tax at 30% for earnings of 12,000 or more
    else:
        tax_owed = 0.30 * earnings
    # Return the calculated tax
    return tax_owed


ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)


#  It accepts a number as input and adds three if the input is less than 10, and otherwise adds eight.
def add_three_or_eight(number):
    if number < 10:
        result = number + 3
    else:
        result = number + 8

    return result
