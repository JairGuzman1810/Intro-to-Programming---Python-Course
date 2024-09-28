# Conditional statements use conditions to modify how your function runs. T
# ------ "if" statements ------
def evaluate_temp(temp):
    # Initialize the message to a default value for normal temperature
    message = "Normal temperature."

    # Check if the temperature is greater than 38
    # If it is, update the message to indicate a fever
    if temp > 38:
        message = "Fever!"

    # Return the final message based on the temperature
    return message


print(evaluate_temp(37))

print(evaluate_temp(39))


# ------ "if ... else" statements ------

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message


print(evaluate_temp_with_else(37))


# ------ "if ... elif ... else" statements ------
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message


evaluate_temp_with_elif(36)

evaluate_temp_with_elif(34)
