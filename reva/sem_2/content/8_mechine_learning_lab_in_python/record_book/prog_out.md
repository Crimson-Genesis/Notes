# A_1.py\n===================
# Q - Write a program to implement how to read and display a dataset in Python.
 
## Code:- 
```python
#!/usr/bin/env python

import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import json
import requests
from io import StringIO

print(" 1. Read CSV file ")
try:
    df_csv = pd.read_csv("data.csv")
    print(df_csv)
except FileNotFoundError:
    print("CSV file not found, skipping...")

print("\n 2. Read Excel file ")
try:
    df_excel = pd.read_excel("data.xlsx")
    print(df_excel)
except FileNotFoundError:
    print("Excel file not found, skipping...")

print("\n 3. Read JSON file ")
try:
    df_json = pd.read_json("data.json")
    print(df_json)
except FileNotFoundError:
    print("JSON file not found, skipping...")

print("\n 4. Read CSV from URL ")
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
try:
    response = requests.get(url)
    data = StringIO(response.text)
    df_url = pd.read_csv(data)
    print(df_url.head())
except Exception as e:
    print("Error reading from URL:", e)

print("\n 5. Built-in dataset from sklearn ")
iris = load_iris()
df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target
print(df_iris.head())

print("\n 6. Built-in dataset from seaborn ")
df_tips = sns.load_dataset('tips')
print(df_tips.head())

print("\n 7. Display dataset info and description ")
print("\n--- Iris Dataset Info ---")
print(df_iris.info())
print("\n--- Iris Dataset Description ---")
print(df_iris.describe())

```
 
## Output:- 
```python
 1. Read CSV file 
CSV file not found, skipping...

 2. Read Excel file 
Excel file not found, skipping...

 3. Read JSON file 
JSON file not found, skipping...

 4. Read CSV from URL 
  Month   "1958"   "1959"   "1960"
0   JAN      340      360      417
1   FEB      318      342      391
2   MAR      362      406      419
3   APR      348      396      461
4   MAY      363      420      472

 5. Built-in dataset from sklearn 
   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target
0                5.1               3.5  ...               0.2       0
1                4.9               3.0  ...               0.2       0
2                4.7               3.2  ...               0.2       0
3                4.6               3.1  ...               0.2       0
4                5.0               3.6  ...               0.2       0

[5 rows x 5 columns]

 6. Built-in dataset from seaborn 
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

 7. Display dataset info and description 

--- Iris Dataset Info ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
 4   target             150 non-null    int64  
dtypes: float64(4), int64(1)
memory usage: 6.0 KB
None

--- Iris Dataset Description ---
       sepal length (cm)  sepal width (cm)  ...  petal width (cm)      target
count         150.000000        150.000000  ...        150.000000  150.000000
mean            5.843333          3.057333  ...          1.199333    1.000000
std             0.828066          0.435866  ...          0.762238    0.819232
min             4.300000          2.000000  ...          0.100000    0.000000
25%             5.100000          2.800000  ...          0.300000    0.000000
50%             5.800000          3.000000  ...          1.300000    1.000000
75%             6.400000          3.300000  ...          1.800000    2.000000
max             7.900000          4.400000  ...          2.500000    2.000000

[8 rows x 5 columns]
```
# A_2.py\n===================
# Q - Write a program to learn how to select features for machine learning.
 
## Code:- 
```python
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
```
 
## Output:- 
```python
 Dataset Head 
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2

 Filter Method: Variance Threshold 
Selected features based on variance: ['sepal length (cm)', 'petal length (cm)']

 Filter Method: Correlation 
Correlation Matrix:
                    sepal length (cm)  ...  petal width (cm)
sepal length (cm)           1.000000  ...          0.817941
sepal width (cm)           -0.117570  ...         -0.366126
petal length (cm)           0.871754  ...          0.962865
petal width (cm)            0.817941  ...          1.000000

[4 rows x 4 columns]
Features after removing highly correlated: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']

 Wrapper Method: RFE 
Selected features by RFE: ['petal length (cm)', 'petal width (cm)']

 Embedded Method: Lasso 
Selected features by Lasso: ['petal length (cm)']
```
# A_3.py\n===================
# Q - Write the program to implement Data Pre-processing for machine learning.

 
## Code:- 
```python
#!/usr/bin/env python

# ML Lab: Data Preprocessing for Machine Learning
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# ML Lab: Data Preprocessing using sklearn predefined dataset
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

# ========= 1. Load dataset =========
housing = fetch_california_housing(as_frame=True)
df = housing.frame
print(" Original Dataset ")
print(df.head())

# ========= 2. Introduce some missing values for demo =========
df.loc[0, 'AveRooms'] = np.nan
df.loc[5, 'HouseAge'] = np.nan
print("\n Dataset with Missing Values ")
print(df.head(6))

# ========= 3. Handle missing values =========
# Numeric columns: fill with mean
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("\n After Handling Missing Values ")
print(df_imputed.head(6))

# ========= 4. Feature Scaling =========
X = df_imputed.drop('MedHouseVal', axis=1)
y = df_imputed['MedHouseVal']

# Standardization
scaler_std = StandardScaler()
X_std = scaler_std.fit_transform(X)
print("\n Standardized Features (first 5 rows) ")
print(np.round(X_std[:5], 2))

# Min-Max Scaling
scaler_mm = MinMaxScaler()
X_mm = scaler_mm.fit_transform(X)
print("\n Min-Max Scaled Features (first 5 rows) ")
print(np.round(X_mm[:5], 2))

# ========= 5. Train-Test Split =========
X_train, X_test, y_train, y_test = train_test_split(X_mm, y, test_size=0.3, random_state=42)
print("\n Train and Test Split ")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

```
 
## Output:- 
```python
 Original Dataset 
   MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
0  8.3252      41.0  6.984127  ...     37.88    -122.23        4.526
1  8.3014      21.0  6.238137  ...     37.86    -122.22        3.585
2  7.2574      52.0  8.288136  ...     37.85    -122.24        3.521
3  5.6431      52.0  5.817352  ...     37.85    -122.25        3.413
4  3.8462      52.0  6.281853  ...     37.85    -122.25        3.422

[5 rows x 9 columns]

 Dataset with Missing Values 
   MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
0  8.3252      41.0       NaN  ...     37.88    -122.23        4.526
1  8.3014      21.0  6.238137  ...     37.86    -122.22        3.585
2  7.2574      52.0  8.288136  ...     37.85    -122.24        3.521
3  5.6431      52.0  5.817352  ...     37.85    -122.25        3.413
4  3.8462      52.0  6.281853  ...     37.85    -122.25        3.422
5  4.0368       NaN  4.761658  ...     37.85    -122.25        2.697

[6 rows x 9 columns]

 After Handling Missing Values 
   MedInc   HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
0  8.3252  41.000000  5.428924  ...     37.88    -122.23        4.526
1  8.3014  21.000000  6.238137  ...     37.86    -122.22        3.585
2  7.2574  52.000000  8.288136  ...     37.85    -122.24        3.521
3  5.6431  52.000000  5.817352  ...     37.85    -122.25        3.413
4  3.8462  52.000000  6.281853  ...     37.85    -122.25        3.422
5  4.0368  28.638355  4.761658  ...     37.85    -122.25        2.697

[6 rows x 9 columns]

 Standardized Features (first 5 rows) 
[[ 2.34  0.98  0.   -0.15 -0.97 -0.05  1.05 -1.33]
 [ 2.33 -0.61  0.33 -0.26  0.86 -0.09  1.04 -1.32]
 [ 1.78  1.86  1.16 -0.05 -0.82 -0.03  1.04 -1.33]
 [ 0.93  1.86  0.16 -0.05 -0.77 -0.05  1.04 -1.34]
 [-0.01  1.86  0.34 -0.03 -0.76 -0.09  1.04 -1.34]]

 Min-Max Scaled Features (first 5 rows) 
[[0.54 0.78 0.03 0.02 0.01 0.   0.57 0.21]
 [0.54 0.39 0.04 0.02 0.07 0.   0.57 0.21]
 [0.47 1.   0.05 0.02 0.01 0.   0.56 0.21]
 [0.35 1.   0.04 0.02 0.02 0.   0.56 0.21]
 [0.23 1.   0.04 0.02 0.02 0.   0.56 0.21]]

 Train and Test Split 
X_train shape: (14448, 8)
X_test shape: (6192, 8)
y_train shape: (14448,)
y_test shape: (6192,)
```
# A_4.py\n===================
# Q - Write a program to implement Classification Algorithm. Calculate the accuracy, presicion, recall.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
 Dataset Head 
   mean radius  mean texture  ...  worst fractal dimension  target
0        17.99         10.38  ...                  0.11890       0
1        20.57         17.77  ...                  0.08902       0
2        19.69         21.25  ...                  0.08758       0
3        11.42         20.38  ...                  0.17300       0
4        20.29         14.34  ...                  0.07678       0

[5 rows x 31 columns]

 Train-Test Split 
X_train shape: (398, 30)
X_test shape: (171, 30)

 Evaluation Metrics 
Accuracy: 0.9825
Precision: 0.9907
Recall: 0.9815

Classification Report:
              precision    recall  f1-score   support

           0       0.97      0.98      0.98        63
           1       0.99      0.98      0.99       108

    accuracy                           0.98       171
   macro avg       0.98      0.98      0.98       171
weighted avg       0.98      0.98      0.98       171

```
# A_5.py\n===================
# Q - Write a program to demonstrate SVM with different kernel methods.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
 Dataset Head 
   mean radius  mean texture  ...  worst symmetry  worst fractal dimension
0        17.99         10.38  ...          0.4601                  0.11890
1        20.57         17.77  ...          0.2750                  0.08902
2        19.69         21.25  ...          0.3613                  0.08758
3        11.42         20.38  ...          0.6638                  0.17300
4        20.29         14.34  ...          0.2364                  0.07678

[5 rows x 30 columns]

 SVM Evaluation with Different Kernels 
Kernel: linear
  Accuracy: 0.9766
  Precision: 0.9815
  Recall: 0.9815

Kernel: poly
  Accuracy: 0.8947
  Precision: 0.8571
  Recall: 1.0000

Kernel: rbf
  Accuracy: 0.9766
  Precision: 0.9815
  Recall: 0.9815

```
# A_6.py\n===================
# Q - Comparison of Machine Learning techniques.
 
## Code:- 
```python
#!/usr/bin/env python

# ML Lab: Comparison of ML Techniques
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ========= 1. Load Dataset =========
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

# ========= 2. Train-Test Split =========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ========= 3. Feature Scaling =========
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ========= 4. Define ML Models =========
models = {
    'Logistic Regression': LogisticRegression(max_iter=500),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# ========= 5. Train, Predict and Evaluate =========
results = {}

for name, model in models.items():
    # SVM and KNN require scaled data
    if name in ['SVM', 'Logistic Regression', 'KNN']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    
    results[name] = {'Accuracy': acc, 'Precision': prec, 'Recall': rec}

# ========= 6. Display Results =========
print("\n Comparison of ML Techniques ")
for name, metrics in results.items():
    print(f"{name}:")
    print(f"  Accuracy: {metrics['Accuracy']:.4f}")
    print(f"  Precision: {metrics['Precision']:.4f}")
    print(f"  Recall: {metrics['Recall']:.4f}\n")

```
 
## Output:- 
```python

 Comparison of ML Techniques 
Logistic Regression:
  Accuracy: 0.9825
  Precision: 0.9907
  Recall: 0.9815

Decision Tree:
  Accuracy: 0.9415
  Precision: 0.9712
  Recall: 0.9352

Random Forest:
  Accuracy: 0.9708
  Precision: 0.9640
  Recall: 0.9907

SVM:
  Accuracy: 0.9766
  Precision: 0.9815
  Recall: 0.9815

KNN:
  Accuracy: 0.9591
  Precision: 0.9633
  Recall: 0.9722

```
# A_7.py\n===================
# Q - Write a program to create the clustering model.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
 Dataset Head 
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2

 Clustering Results 
Cluster Labels for first 10 samples: [1 2 2 2 1 1 1 1 2 2]
Centroids of clusters:
[[ 0.57100359 -0.37176778  0.69111943  0.66315198]
 [-0.81623084  1.31895771 -1.28683379 -1.2197118 ]
 [-1.32765367 -0.373138   -1.13723572 -1.11486192]]
Silhouette Score: 0.4799

Original vs Cluster (first 10 rows):
   Original  Cluster
0         0        1
1         0        2
2         0        2
3         0        2
4         0        1
5         0        1
6         0        1
7         0        1
8         0        2
9         0        2
```
# A_8.py\n===================
# Q - Write a program to create two clustering models on the same datase. Compare the results of these two algorithns and comments on the quality of clustering.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
 Clustering Results 
       Algorithm  Silhouette Score  Adjusted Rand Index
0         KMeans          0.552819             0.730238
1  Agglomerative          0.554324             0.731199

Agglomerative Clustering forms better separated clusters.
Agglomerative clustering is closer to the true Iris classes.
```
# B_1.py\n===================
# Q - Write a program to demonstrate the working of the decision tree based ID3 algorithm. Use an appropriate data set for building the decision tree a dn apply this knowledge to classify n new sample.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
Decision Tree Rules (ID3 style):

|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal length (cm) <= 4.75
|   |   |--- petal width (cm) <= 1.60
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.60
|   |   |   |--- class: 2
|   |--- petal length (cm) >  4.75
|   |   |--- petal length (cm) <= 5.15
|   |   |   |--- class: 2
|   |   |--- petal length (cm) >  5.15
|   |   |   |--- class: 2


Model Accuracy on Test Set: 0.9777777777777777

New Sample: [[5.1, 3.5, 1.4, 0.2]]
Predicted Class: setosa
```
# B_2.py\n===================
# Q - Build an Artificial Neural Network by implementing the Backpropagatino algorithm and test the same using appropriate data sets.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
Epoch 0, Loss: 0.2616
Epoch 200, Loss: 0.0164
Epoch 400, Loss: 0.0117
Epoch 600, Loss: 0.0093
Epoch 800, Loss: 0.0073

Final Accuracy on Test Data: 0.9824561403508771
```
# B_3.py\n===================
# Q - Write a program to implement the naive Bayesian classifier for a sample training data set stored as a .CSV file. Compute the accuracy of the classifier, considering few test data sets.
 
## Code:- 
```python
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

```
 
## Output:- 
```python
Dataset saved to wine_dataset.csv

First 5 rows of dataset:
   alcohol  malic_acid   ash  ...  od280/od315_of_diluted_wines  proline  target
0    14.23        1.71  2.43  ...                          3.92   1065.0       0
1    13.20        1.78  2.14  ...                          3.40   1050.0       0
2    13.16        2.36  2.67  ...                          3.17   1185.0       0
3    14.37        1.95  2.50  ...                          3.45   1480.0       0
4    13.24        2.59  2.87  ...                          2.93    735.0       0

[5 rows x 14 columns]

Accuracy: 1.0

Classification Report:
              precision    recall  f1-score   support

     class_0       1.00      1.00      1.00        19
     class_1       1.00      1.00      1.00        21
     class_2       1.00      1.00      1.00        14

    accuracy                           1.00        54
   macro avg       1.00      1.00      1.00        54
weighted avg       1.00      1.00      1.00        54

```
# B_4.py\n===================
# Write a program to demonstrate Reinforcement learning.
 
## Code:- 
```python
#!/usr/bin/env python

import numpy as np
import gymnasium as gym

# Create the FrozenLake environment (4x4 grid, slippery by default)
env = gym.make("FrozenLake-v1", is_slippery=True)

# Initialize Q-table with zeros
state_size = env.observation_space.n   # Number of states
action_size = env.action_space.n       # Number of actions
Q = np.zeros((state_size, action_size))

# Hyperparameters
learning_rate = 0.8
discount_factor = 0.95
epsilon = 1.0        # Exploration rate
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000
max_steps = 100

# Training
rewards = []

for episode in range(episodes):
    state, _ = env.reset()
    total_rewards = 0
    done = False

    for _ in range(max_steps):
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state, :])     # Exploit

        # Take action and observe outcome
        new_state, reward, done, truncated, info = env.step(action)

        # Update Q-value using Q-Learning formula
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + discount_factor * np.max(Q[new_state, :]) - Q[state, action]
        )

        state = new_state
        total_rewards += reward

        if done:
            break

    # Decay epsilon (exploration probability)
    epsilon = max(min_epsilon, epsilon * epsilon_decay)
    rewards.append(total_rewards)

print("Training finished!\n")

# Evaluate performance
print(f"Average reward over {episodes} episodes: {np.mean(rewards):.2f}")

# Test the trained agent
state, _ = env.reset()
env.render()
done = False

print("\nTesting trained agent:")
while not done:
    action = np.argmax(Q[state, :])  # Always exploit
    new_state, reward, done, truncated, info = env.step(action)
    env.render()
    state = new_state

print("Test finished with reward:", reward)

```
 
## Output:- 
```python
Training finished!

Average reward over 2000 episodes: 0.36

Testing trained agent:
Test finished with reward: 1.0
```
# B_5.py\n===================
# Q - Write a program to Implement CNN models for classification of images.
 
## Code:- 
```python
#!/usr/bin/env python

# CNN for Image Classification using MNIST dataset
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# 1. Load dataset (predefined in Keras)
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

# 2. Preprocess data
# Normalize pixel values (0-255 -> 0-1)
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32') / 255

# One-hot encode labels
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 3. Build CNN Model
model = models.Sequential()

# Convolution + Pooling Layers
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Flatten + Dense Layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 4. Compile model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train model
history = model.fit(X_train, y_train, epochs=5, batch_size=64,
                    validation_data=(X_test, y_test))

# 6. Evaluate model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print("\nTest Accuracy:", test_acc)

# 7. Plot training history
plt.figure(figsize=(12, 5))

# Accuracy graph
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.legend()
plt.title('CNN Accuracy')

# Loss graph
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Test Loss')
plt.legend()
plt.title('CNN Loss')

plt.savefig("photos/B_5_CNN_accuracy_and_Loss.png", dpi=300, bbox_inches='tight')
```
 
## Output:- 
```python
Epoch 1/5
938/938 ━━━━━━━━━━━━━━━━━━━━ 24s 24ms/step - accuracy: 0.9443 - loss:
0.1830 - val_accuracy: 0.9824 - val_loss: 0.0542
Epoch 2/5
938/938 ━━━━━━━━━━━━━━━━━━━━ 23s 24ms/step - accuracy: 0.9844 - loss:
0.0504 - val_accuracy: 0.9896 - val_loss: 0.0342
Epoch 3/5
938/938 ━━━━━━━━━━━━━━━━━━━━ 22s 24ms/step - accuracy: 0.9887 - loss:
0.0352 - val_accuracy: 0.9866 - val_loss: 0.0393
Epoch 4/5
938/938 ━━━━━━━━━━━━━━━━━━━━ 22s 24ms/step - accuracy: 0.9918 - loss:
0.0263 - val_accuracy: 0.9907 - val_loss: 0.0289
Epoch 5/5
938/938 ━━━━━━━━━━━━━━━━━━━━ 22s 24ms/step - accuracy: 0.9932 - loss:
0.0223 - val_accuracy: 0.9892 - val_loss: 0.0342
313/313 - 2s - 5ms/step - accuracy: 0.9892 - loss: 0.0342
```
