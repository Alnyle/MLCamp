import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# save filepath to variable for easier access
melbourne_file_path = './melb_data.csv/melb_data.csv'


melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melborune data as (table)
melbourne_data.describe()


# choose our columns names
melbourne_data.columns


# romove the rows that contains missing data
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)


# prediction target we always called `y` (what we want to predict)

y = melbourne_data.Price

# select columns (features) those columns would be the columns used to determine
# the home price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']


# By convention, this data is called X.

X = melbourne_data[melbourne_features]


X.describe()

#  is a method in pandas that allows you to view the first few rows of a DataFrame (or Series).
X.head()


# define model
melbourne_model = DecisionTreeRegressor(random_state=1)

# fit model : fit(X, y) trains the model using features (X) and target values (y), 
#             allowing the model to learn patterns in the data.
melbourne_model.fit(X,y)


print("Making predictions ofr the following 5 houses: ")
print(X.head())

# is used to generate predictions from your decision tree model (melbourne_model)
# using the first few rows of your feature dataset X.
print("The predictions are")
print(melbourne_model.predict(X.head()))