#!/usr/bin/env python

# ML Lab: Clustering with K-Means
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ========= 1. Load Dataset =========
data = load_iris(as_frame=True)
X = data.data
y = data.target  # for optional evaluation

print(" Dataset Head ")
print(X.head())

# ========= 2. Feature Scaling =========
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ========= 3. Apply K-Means Clustering =========
# Choose number of clusters = 3 (known from dataset)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# ========= 4. Evaluation =========
# Silhouette score measures how well the clusters are separated (range -1 to 1)
sil_score = silhouette_score(X_scaled, labels)

print("\n Clustering Results ")
print(f"Cluster Labels for first 10 samples: {labels[:10]}")
print(f"Centroids of clusters:\n{kmeans.cluster_centers_}")
print(f"Silhouette Score: {sil_score:.4f}")

# Optional: Compare with original labels
comparison = pd.DataFrame({'Original': y, 'Cluster': labels})
print("\nOriginal vs Cluster (first 10 rows):")
print(comparison.head(10))

