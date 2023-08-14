from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    def get_new_flower_input():
        sepal_length = float(input("Enter sepal length (cm): "))
        sepal_width = float(input("Enter sepal width (cm): "))
        petal_length = float(input("Enter petal length (cm): "))
        petal_width = float(input("Enter petal width (cm): "))
        return [sepal_length, sepal_width, petal_length, petal_width]
    new_flower = get_new_flower_input()
    predicted_species = clf.predict([new_flower])
    species_names = iris.target_names
    predicted_species_name = species_names[predicted_species[0]]
    print(f"The predicted species of the new flower is: {predicted_species_name}")
