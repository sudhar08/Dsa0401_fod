from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
iris = load_iris()
X, y = iris.data, iris.target
def get_user_input():
    features = input("Enter the names of the features separated by commas: ").strip().split(',')
    target = input("Enter the name of the target variable: ").strip()
    return features, target
selected_features, target_variable = get_user_input()
feature_indices = [iris.feature_names.index(feature.strip()) for feature in selected_features]
target_index = iris.target_names.tolist().index(target_variable.strip())
X_selected = X[:, feature_indices]
y_selected = (y == target_index).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X_selected, y_selected, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
