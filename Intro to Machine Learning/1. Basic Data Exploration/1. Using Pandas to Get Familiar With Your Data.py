# Pandas is the primary tool data scientists use for exploring and manipulating data.
# Most people abbreviate pandas in their code as pd. We do this with the command
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
print(melbourne_data.describe())
