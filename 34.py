import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Step 1: Load the dataset
data = pd.read_csv("C:/Users/mailm/Downloads/treatment_data.csv")  # Replace 'treatment_data.csv' with your dataset filename

# Step 2: Perform one-hot encoding for 'gender' and 'treatment'
data = pd.get_dummies(data, columns=['gender', 'treatment'], drop_first=True)

# Step 3: Separate features and target variable
X = data.drop('outcome', axis=1)
y = data['outcome']

# Step 4: Convert the data to NumPy arrays with compatible data types
X = X.values
y = y.values

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Build and train the KNN classification model
knn_model = KNeighborsClassifier(n_neighbors=5)  # You can adjust the number of neighbors (k) as needed
knn_model.fit(X_train, y_train)

# Step 7: Make predictions on the test set
y_pred = knn_model.predict(X_test)

# Step 8: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1-score:', f1)
