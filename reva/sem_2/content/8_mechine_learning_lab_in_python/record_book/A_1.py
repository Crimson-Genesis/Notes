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

