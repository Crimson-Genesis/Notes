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

