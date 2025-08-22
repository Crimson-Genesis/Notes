#!/usr/bin/env python

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load a predefined dataset (Wine dataset)
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target

# Step 2: Save dataset into a CSV file
csv_file = "wine_dataset.csv"
df.to_csv(csv_file, index=False)
print(f"Dataset saved to {csv_file}")

# Step 3: Read dataset from CSV
data = pd.read_csv(csv_file)
print("\nFirst 5 rows of dataset:")
print(data.head())

# Step 4: Split into features (X) and labels (y)
X = data.drop('target', axis=1)
y = data['target']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 6: Train Naive Bayes Classifier
nb = GaussianNB()
nb.fit(X_train, y_train)

# Step 7: Predict
y_pred = nb.predict(X_test)

# Step 8: Evaluate model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

