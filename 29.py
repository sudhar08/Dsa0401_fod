from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

def get_user_input():
    feature_names = input("Enter the names of the features separated by commas: ").split(',')
    target_name = input("Enter the name of the target variable: ")
    return feature_names, target_name

def main():
    # Load the dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Get user input for features and target variable
    feature_names, target_name = get_user_input()

    # Find the indices of the features and target variable in the dataset
    feature_indices = [list(iris.feature_names).index(feature.strip()) for feature in feature_names]
    target_index = iris.target_names.tolist().index(target_name.strip())

    # Use only the selected features and target variable
    X_selected = X[:, feature_indices]
    y_selected = (y == target_index).astype(int)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y_selected, test_size=0.2, random_state=42)

    # Create and train a logistic regression classifier
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = clf.predict(X_test)

    # Calculate and display evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")

if __name__ == "__main__":
    main()
