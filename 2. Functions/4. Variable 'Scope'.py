#  Variables defined inside the
#  function body cannot be accessed outside the function.
def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax


pay_fulltime = get_pay(40)
print(pay_fulltime)

# NameError: name 'pay_aftertax' is not defined
print(pay_aftertax)
