"""
Beginner-level Machine Learning Practice.
The goal is to create a model that predicts a test score from number of hours studied.
"""

# Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Creating sample data
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [12, 25, 32, 40, 50, 55, 65, 72, 80, 90]
    }

df = pd.DataFrame(data)


# Features and target
x = df[['Hours_Studied']] # creates a new Pandas Dataframe with Hours_Studied as column | 2D Dataframe | ML Input
y = df['Score'] # creates a new series (one column vector) with 'Score' as column | 1D Vector | ML Output

# Splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Training the data
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
y_pred = model.predict(X_test)
print("Predictions:", y_pred)

# Evaluate the model
mse = mean_squared_error(Y_test, y_pred)
print("Mean Squared Error:", mse)

# Visualize results
X_1d = x['Hours_Studied'].values
y_pred_full = model.predict(x).flatten()


# Plotting
plt.scatter(X_1d, y, color = 'Blue', label = 'Actual Scores')
plt.plot(X_1d, y_pred_full, color = 'red', label = 'Predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours Studied vs Score Prediction')
plt.show()