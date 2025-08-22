#!/usr/bin/env python

# Clustering Comparison Example
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, adjusted_rand_score

# Load dataset
iris = load_iris()
X = iris.data
y_true = iris.target

# --- Model 1: KMeans Clustering ---
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)

# --- Model 2: Agglomerative Clustering ---
agglo = AgglomerativeClustering(n_clusters=3, linkage='ward')
agglo_labels = agglo.fit_predict(X)

# --- Evaluation ---
# Silhouette Score (higher = better cluster separation)
kmeans_sil = silhouette_score(X, kmeans_labels)
agglo_sil = silhouette_score(X, agglo_labels)

# Adjusted Rand Index (ARI) - compares clustering with true labels
kmeans_ari = adjusted_rand_score(y_true, kmeans_labels)
agglo_ari = adjusted_rand_score(y_true, agglo_labels)

# Results Table
results = pd.DataFrame({
    "Algorithm": ["KMeans", "Agglomerative"],
    "Silhouette Score": [kmeans_sil, agglo_sil],
    "Adjusted Rand Index": [kmeans_ari, agglo_ari]
})

print(" Clustering Results ")
print(results)

# --- Comment on results ---
if kmeans_sil > agglo_sil:
    print("\nKMeans forms better separated clusters based on silhouette score.")
else:
    print("\nAgglomerative Clustering forms better separated clusters.")

if kmeans_ari > agglo_ari:
    print("KMeans clustering is closer to the true Iris classes.")
else:
    print("Agglomerative clustering is closer to the true Iris classes.")

