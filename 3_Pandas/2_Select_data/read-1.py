import pandas as pd

#  index-based selection: select row and columns based on index

# a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.

# you have to convert data into object to able interact with data

melb_data = pd.read_csv('./melb_data.csv/melb_data.csv', index_col=1)

# return tuple represent data dimensionality of the DataFrame (rows number, columns number)
melb_data.shape


# head => return first five enteries (records) in your dataframe
melb_data.head()

# select column
# melb_data['Suburb']

# select specific value in that column
melb_data['Suburb'][0]


# returns all the columns of the first row as a pandas Series.
melb_data.iloc[0, : ]

# returns first columns of first and second rows as pandas Series
melb_data.iloc[1:3, :]


# you can aslo pass a list 
# selecting 1,2,3 columns of 1,2,3 rows
melb_data.iloc[[1, 2, 3], [1, 2, 3]]


# you can aslo usin negative values
melb_data.iloc[-5: , 0] # select first row of last 5 rows


