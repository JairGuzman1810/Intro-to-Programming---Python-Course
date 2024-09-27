# ------ Creating variable ------
test_var = 4 + 5
# Print the value of test_var
print(test_var)

# ------ Manipulating variables ------
my_var = 3

print(my_var)

my_var = 100

print(my_var)

# Increasing the value by 3
my_var = my_var + 3

print(my_var)

# ------ Multiple variables ------

# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

# Update to include leap years
days_per_year = 365.25

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

# ------ Debugging ------
# Typo mistake
print(hours_per_dy)
