import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read the data from the CSV file
df = pd.read_csv("C:/Users/mailm/Downloads/customer_data2.csv")

# Convert 'PurchaseBehavior' to numeric values using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['PurchaseBehavior'], drop_first=True)

# Extract the features (SpendingScore) for clustering
X = df_encoded[['SpendingScore']].values

# Initialize and fit the K-Means model with n_init explicitly set to 10
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# Add the cluster labels to the original DataFrame
df['Cluster'] = kmeans.labels_

# Visualize the clusters using a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['SpendingScore'], np.zeros(len(df)), c=df['Cluster'], cmap='viridis', s=100)
plt.xlabel('Spending Score')
plt.title('Customer Clusters')
plt.show()

# Print the cluster centers (mean spending score for each cluster)
print("Cluster Centers (Mean Spending Score):")
print(kmeans.cluster_centers_)
