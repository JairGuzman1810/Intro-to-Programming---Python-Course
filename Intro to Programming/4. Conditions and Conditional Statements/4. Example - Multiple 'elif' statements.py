# there's no limit to the number of "elif" statements
# in this block of cocde calculates the dose of medication
# (in milliliters) to give to a child, based on weight (in kilograms).

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose


print(get_dose(12))


def get_phone_bill(gb):
    plan_cost = 100  # Base cost of the plan for 15 GB
    gb_limit = 15  # Included GB in the plan
    additional_cost_per_gb = 100  # Cost for additional GB

    if gb <= gb_limit:
        bill = plan_cost  # If within the limit, charge only the base cost
    else:
        gb_difference = gb - gb_limit  # Additional GB used
        additional_cost = gb_difference * additional_cost_per_gb  # Calculate additional cost
        bill = plan_cost + additional_cost  # Total bill

    return bill


# Example usage to check your answer
print(get_phone_bill(10))  # Should output: 100
print(get_phone_bill(15.1))  # Should output: 110
print(get_phone_bill(20))  # Should output: 200
