import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA

# Step 1: Load the data
data = pd.read_csv("C:/Users/mailm/Downloads/customer_data.csv")

# Step 2: Preprocess the data
X = data.drop(columns=['CustomerID'])  # Drop the CustomerID column if not needed

# Step 3: Apply one-hot encoding to the 'Gender' column
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), ['Gender'])], remainder='passthrough')
X = ct.fit_transform(X)

# Step 4: Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

# Step 5: Determine the optimal number of clusters using the Elbow Method
wcss = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

# Step 6: Apply K-means clustering with the optimal number of clusters
num_clusters = 4  # Choose the optimal number of clusters from the Elbow Method
kmeans = KMeans(n_clusters=num_clusters, n_init=9, random_state=42)
kmeans.fit(scaled_data)

# Step 7: Visualize the clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# Create a DataFrame with cluster assignments and the PCA-reduced data
clusters_df = pd.DataFrame({'Cluster': kmeans.labels_, 'PCA1': pca_data[:, 0], 'PCA2': pca_data[:, 1]})

# Visualize the clusters
plt.figure(figsize=(10, 6))
for cluster in range(num_clusters):
    plt.scatter(clusters_df[clusters_df['Cluster'] == cluster]['PCA1'],
                clusters_df[clusters_df['Cluster'] == cluster]['PCA2'],
                label=f'Cluster {cluster}')
plt.title('Customer Segmentation using K-means Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()
