import pandas as pd



melb_data = pd.read_csv('./melb_data.csv/melb_data.csv')

# display all colunms name as list
melb_data.columns


## Selecting null and not null records  ##

# return all the records where the `YearBuilt` column is not empty or null
melb_data.loc[melb_data['YearBuilt'].notnull()]

# return all the records where the `YearBuilt` column is not empty or null
melb_data.loc[melb_data['YearBuilt'].notnull()]




## Assigning data ##