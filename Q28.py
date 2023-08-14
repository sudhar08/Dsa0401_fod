from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
dataset = [
    [50, 20],   
    [35, 45],    
    [20, 10],    
    [15, 5],     
]
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(dataset)
def get_new_customer_input(num_features):
    new_customer_features = []
    for i in range(num_features):
        feature_value = float(input(f"Enter feature {i+1}: "))
        new_customer_features.append(feature_value)
    return new_customer_features
new_customer = get_new_customer_input(num_features=len(dataset[0]))
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(dataset)
new_customer_scaled = scaler.transform([new_customer])
predicted_cluster = kmeans.predict(new_customer_scaled)
print(f"The new customer belongs to cluster {predicted_cluster[0]}")
