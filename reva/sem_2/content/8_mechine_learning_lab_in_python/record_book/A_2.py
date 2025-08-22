#!/usr/bin/env python

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold, RFE, SelectFromModel
from sklearn.linear_model import LogisticRegression, Lasso
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print(" Dataset Head ")
print(X.head())

print("\n Filter Method: Variance Threshold ")
selector = VarianceThreshold(threshold=0.6)  # remove low variance features
X_var = selector.fit_transform(X)
selected_features = X.columns[selector.get_support()]
print("Selected features based on variance:", list(selected_features))

print("\n Filter Method: Correlation ")
corr_matrix = X.corr()
print("Correlation Matrix:\n", corr_matrix)

# Drop features with high correlation (>0.9)
upper = corr_matrix.where(~np.tril(np.ones(corr_matrix.shape)).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column].abs() > 0.9)]
X_corr = X.drop(columns=to_drop)
print("Features after removing highly correlated:", list(X_corr.columns))

print("\n Wrapper Method: RFE ")
model = LogisticRegression(max_iter=200)
rfe = RFE(model, n_features_to_select=2)
rfe.fit(X, y)
selected_rfe = X.columns[rfe.support_]
print("Selected features by RFE:", list(selected_rfe))

print("\n Embedded Method: Lasso ")
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)
model = SelectFromModel(lasso, prefit=True)
selected_lasso = X.columns[model.get_support()]
print("Selected features by Lasso:", list(selected_lasso))

plt.figure(figsize=(8,6))
sns.heatmap(X.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("photos/A_2_correlation_heatmap.png", dpi=300, bbox_inches='tight')
