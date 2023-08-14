import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X = np.array([[symptom1_value, symptom2_value, symptom3_value],   
              [symptom1_value, symptom2_value, symptom3_value],
              ...
              [symptom1_value, symptom2_value, symptom3_value]])
y = np.array([label1, label2, ..., labelN])  
def predict_condition(new_patient_features, k):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn_classifier.fit(X_train, y_train)
    prediction = knn_classifier.predict([new_patient_features])
    return prediction[0]
def main():
    new_patient_features = []
    num_features = len(X[0])  
    for i in range(num_features):
        feature_value = float(input(f"Enter feature {i+1}: "))
        new_patient_features.append(feature_value)
    k = int(input("Enter the value of k (number of neighbors): "))
    prediction = predict_condition(new_patient_features, k)
    if prediction == 0:
        print("The patient does not have the medical condition.")
    else:
        print("The patient has the medical condition.")
if _name_ == "_main_":
    main()
