import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Load and explore the dataset
data = pd.read_csv("C:/Users/mailm/Downloads/house.csv")  # Replace 'house_data.csv' with your dataset filename
print(data.head())  # Check the first few rows of the dataset

# Step 3: Perform bivariate analysis (scatter plot)
plt.scatter(data['house_size'], data['house_price'])
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Bivariate Analysis - House Size vs. House Price')
plt.show()

# Step 4: Prepare the data for the linear regression model
X = data[['house_size']]  # Feature (independent variable)
y = data['house_price']  # Target (dependent variable)

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate the model's performance
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Absolute Error (MAE):', mae)
print('R-squared (R2):', r2)

# Step 8: Make predictions and visualize the results
plt.scatter(X_test, y_test, label='Actual Prices')
plt.plot(X_test, y_pred, color='red', label='Predicted Prices')
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Linear Regression - House Size vs. House Price')
plt.legend()
plt.show()
