import pandas as pd



melb_data = pd.read_csv('./melb_data.csv/melb_data.csv')

# number of columns and row in the dataframe
melb_data.shape

# display all colunms name as list
melb_data.columns

# loc [Label based selection] operator 

melb_data.loc[0, 'Address']


#  Conditional Selection   #

# This operation produced a Series of True/False booleans based on the `Address` of each record
melb_data.Address == '85 Turner St'


# you can use loc also with
# it will only display the rows `records` that match this condition
melb_data.loc[melb_data.Address == '85 Turner St']


# display records that match these two conditions (using and)
melb_data.loc[(melb_data.Rooms >= 5) & (melb_data.Bathroom >= 1.0)] 


# display records that match these two conditions (using or)
melb_data.loc[(melb_data.Rooms >= 5) | (melb_data.Bathroom > 1.0)] 


# Conditional Selector #

# `isin` is lets you select data whose value "is in" a list of values.
melb_data.loc[melb_data.Address.isin(['5 Charles St', '40 Federation La'])]