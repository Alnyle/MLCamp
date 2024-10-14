import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = './melb_data.csv/melb_data.csv'


melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melborune data
melbourne_data.describe()