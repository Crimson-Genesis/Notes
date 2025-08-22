#!/usr/bin/env python

# Decision Tree using ID3 Algorithm (Entropy Criterion)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Load dataset (Iris dataset - predefined, has categorical-like classes)
iris = load_iris()
X, y = iris.data, iris.target

# Split into training & testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Build Decision Tree using ID3 (criterion="entropy")
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Show decision rules
tree_rules = export_text(clf, feature_names=iris.feature_names)

print("Decision Tree Rules (ID3 style):\n")
print(tree_rules)

print("\nModel Accuracy on Test Set:", accuracy)

# Classify a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]  # Example: sepal length, sepal width, petal length, petal width
prediction = clf.predict(new_sample)

print("\nNew Sample:", new_sample)
print("Predicted Class:", iris.target_names[prediction][0])

