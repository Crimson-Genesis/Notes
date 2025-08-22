#!/usr/bin/env python

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# ------------------------------
# 1. Load dataset
# ------------------------------
data = load_breast_cancer()
X, y = data.data, data.target

# Normalize data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# 2. Define ANN structure
# ------------------------------
input_neurons = X_train.shape[1]   # number of features
hidden_neurons = 10
output_neurons = 1   # binary classification

# Initialize weights & biases
np.random.seed(42)
W1 = np.random.randn(input_neurons, hidden_neurons)
b1 = np.zeros((1, hidden_neurons))
W2 = np.random.randn(hidden_neurons, output_neurons)
b2 = np.zeros((1, output_neurons))

# ------------------------------
# 3. Define activation functions
# ------------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# ------------------------------
# 4. Training with Backpropagation
# ------------------------------
lr = 0.01
epochs = 1000

for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X_train, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # Loss (binary cross-entropy simplified as MSE)
    loss = np.mean((y_train.reshape(-1,1) - a2)**2)

    # Backpropagation
    error_output = y_train.reshape(-1,1) - a2
    d_output = error_output * sigmoid_derivative(a2)

    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(a1)

    # Update weights & biases
    W2 += a1.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += X_train.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

    # Print progress occasionally
    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# ------------------------------
# 5. Testing the Model
# ------------------------------
# Forward pass on test data
z1 = np.dot(X_test, W1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)

y_pred = (a2 > 0.5).astype(int)
acc = accuracy_score(y_test, y_pred)

print("\nFinal Accuracy on Test Data:", acc)

