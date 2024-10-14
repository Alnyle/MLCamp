import pandas as pd

# Data Loading Code Hidden Here
import pandas as pd

# Load data
melbourne_file_path = './melb_data.csv/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)


from sklearn.metrics import mean_absolute_error


predicted_home_prices = melbourne_model.predict(X)

mean_absolute_error(y, predicted_home_prices)


# ------------------------

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Define model
melbourne_model = DecisionTreeRegressor()

# train_X (X1): Features for training the model.
# val_X (X2):   Features for validating (testing) the model.
# train_y (Y1): Target values for training.
# val_y (Y2):   Target values for validation.

# Fit model => train the model
melbourne_model.fit(train_X, train_y)



# get predicted prices on `validation data`
val_prediction = melbourne_model.predict(val_X)

# mean_absolute_errro = validation actuall data values - validation predicted values
print(mean_absolute_error(val_y, val_prediction))