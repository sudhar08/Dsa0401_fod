import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Load the customer data from CSV
data = pd.read_csv("C:/Users/mailm/Downloads/customer_data1.csv")

# Select the features for clustering
X = data[['Spending on Groceries', 'Spending on Electronics', 'Spending on Clothing']]

# Create a KMeans object and set n_init explicitly
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)

# Fit the model to the data
kmeans.fit(X)

# Get the cluster assignments
cluster_labels = kmeans.labels_

# Add the cluster labels to the original data
data['Cluster'] = cluster_labels

# 3D Scatter Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Assign colors for each cluster
colors = ['red', 'blue', 'green']
for i in range(3):
    ax.scatter(X[data['Cluster'] == i]['Spending on Groceries'],
               X[data['Cluster'] == i]['Spending on Electronics'],
               X[data['Cluster'] == i]['Spending on Clothing'],
               c=colors[i], label=f'Cluster {i}')

# Set labels and title
ax.set_xlabel('Spending on Groceries')
ax.set_ylabel('Spending on Electronics')
ax.set_zlabel('Spending on Clothing')
ax.set_title('KMeans Clustering of Customer Spending Patterns')

# Add legend
ax.legend()

# Show the plot
plt.show()

print(data)
