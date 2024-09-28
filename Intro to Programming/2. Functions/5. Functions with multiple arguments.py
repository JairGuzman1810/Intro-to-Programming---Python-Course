"""
calculates a weekly paycheck based on three arguments:

num_hours - number of hours worked in one week
hourly_wage - the hourly wage (in $/hour)
tax_bracket - percentage of your salary that is removed for taxes
"""


def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax


# calculate the pay after taxes for someone who works 40 hours, makes $24/hour, and is in a 22% tax bracket.
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)
