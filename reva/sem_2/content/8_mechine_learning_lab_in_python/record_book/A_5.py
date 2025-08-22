#!/usr/bin/env python

# ML Lab: SVM with Different Kernels
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ========= 1. Load dataset =========
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

print(" Dataset Head ")
print(X.head())

# ========= 2. Train-Test Split =========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ========= 3. Feature Scaling =========
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ========= 4. SVM with Different Kernels =========
kernels = ['linear', 'poly', 'rbf']
results = {}

for kernel in kernels:
    svm = SVC(kernel=kernel, random_state=42)
    svm.fit(X_train_scaled, y_train)
    y_pred = svm.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    
    results[kernel] = {'Accuracy': acc, 'Precision': prec, 'Recall': rec}

# ========= 5. Display Results =========
print("\n SVM Evaluation with Different Kernels ")
for k, v in results.items():
    print(f"Kernel: {k}")
    print(f"  Accuracy: {v['Accuracy']:.4f}")
    print(f"  Precision: {v['Precision']:.4f}")
    print(f"  Recall: {v['Recall']:.4f}\n")

