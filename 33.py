import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Load and explore the dataset
data = pd.read_csv("C:/Users/mailm/Downloads/car_data.csv")  # Replace 'car_data.csv' with your dataset filename

# Explore the dataset
print(data.head())
print(data.info())
print(data.describe())

# Step 3: Prepare the data for linear regression
selected_features = ['mileage','engine_power']  # Replace with the selected features

X = data[selected_features]
y = data['car_price']

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate the model's performance
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Absolute Error (MAE):', mae)
print('R-squared (R2):', r2)

# Step 7: Identify feature importance
feature_importance = pd.Series(model.coef_, index=selected_features).sort_values(ascending=False)

# Step 8: Provide insights to the marketing team
print("Feature Importance:")
print(feature_importance)

# Visualization of feature importance (optional)
plt.figure(figsize=(10, 6))
sns.lineplot(x=feature_importance.values, y=feature_importance.index)
plt.title('Feature Importance - Influential Factors Affecting Car Prices')
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.show()
