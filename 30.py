from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np

def get_user_input(feature_names):
    features = []
    for feature_name in feature_names:
        feature_value = float(input(f"Enter the {feature_name}: "))
        features.append(feature_value)
    return np.array([features])

def main():
    # Load the car dataset (replace this with your own dataset)
    # Replace 'X' with the features and 'y' with the target variable (price) of your dataset
    X = np.array([[10000, 5, 1, 0], [20000, 3, 2, 1], [15000, 4, 0, 0]])  # Sample feature data
    y = np.array([25000, 30000, 20000])  # Sample target data (car prices)

    # Get the feature names (replace this with your actual feature names)
    feature_names = ["mileage", "age", "brand", "engine_type"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Decision Tree Regressor
    regressor = DecisionTreeRegressor()

    # Train the regressor on the training data
    regressor.fit(X_train, y_train)

    # Get user input for the new car
    new_car_features = get_user_input(feature_names)

    # Make a prediction for the price of the new car
    predicted_price = regressor.predict(new_car_features)

    # Display the predicted price
    print(f"The predicted price of the new car is: {predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()
