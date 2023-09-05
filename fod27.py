import matplotlib.pyplot as plt
from sklearn import linear_model,datasets
from sklearn.model_selection import train_test_split
data1=datasets.load_iris()
X = data1.data
y = data1.target
X_train, X_test, y_train, y_test = train_test_split(
			X, y, test_size = 0.2, random_state=12)
lin=linear_model.LogisticRegression()
lin.fit(X_train[:20],y_train[:20])
print(lin.predict(X_test))
plt.plot(X_train,y_train,marker="o")
plt.show()
