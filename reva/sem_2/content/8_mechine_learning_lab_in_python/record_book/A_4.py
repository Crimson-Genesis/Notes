#!/usr/bin/env python

# ML Lab: Classification with Evaluation Metrics
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# ========= 1. Load dataset =========
data = load_breast_cancer(as_frame=True)
df = data.frame
X = df.drop('target', axis=1)
y = df['target']
print(" Dataset Head ")
print(df.head())

# ========= 2. Train-Test Split =========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\n Train-Test Split ")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# ========= 3. Feature Scaling =========
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ========= 4. Train Classification Model =========
model = LogisticRegression(max_iter=500)
model.fit(X_train_scaled, y_train)

# ========= 5. Predictions =========
y_pred = model.predict(X_test_scaled)

# ========= 6. Evaluation Metrics =========
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\n Evaluation Metrics ")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")

# Optional: detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

