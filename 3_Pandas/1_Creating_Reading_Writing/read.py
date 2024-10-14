import pandas as pd

# a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.

# you have to convert data into object to able interact with data

melb_data = pd.read_csv('./melb_data.csv/melb_data.csv', index_col=1)

# return tuple represent data dimensionality of the DataFrame (rows number, columns number)
melb_data.shape


# head => return first five enteries in your dataframe

melb_data.head()