# Unit - 1 -> Introduction to machine learning
Overview of ML, broad categories of Machine learning - Supervised, Uncupervised, Semi-Supervised, and Reinforcement Learing, Applications areas of Machine Learning.
Data Pre-processing, Training and Choosing Predictive Models, Model Evaluation and Validation of unseen data intances.

## Content ->
**Overview of Machine Learning (ML)**

---

### 1. **Definition of Machine Learning**

* Machine Learning is a subfield of Artificial Intelligence (AI) that focuses on enabling systems to learn from data and improve their performance over time without being explicitly programmed.
* Introduced by Arthur Samuel in 1959: *“Field of study that gives computers the ability to learn without being explicitly programmed.”*

---

### 2. **Main Goal of ML**

* To create algorithms that can receive input data and use statistical analysis to predict an output while updating outputs as new data becomes available.

---

### 3. **Key Characteristics of ML**

* **Data-driven:** Learns from historical data.
* **Self-improving:** Improves its performance with more data.
* **Pattern Recognition:** Detects hidden patterns in data.
* **Automation:** Enables decision-making processes to be automated.

---

### 4. **Categories of Machine Learning**

#### a. **Supervised Learning**

* **Definition:** Model is trained on labeled data (input-output pairs).
* **Goal:** Learn a mapping function from input to output.
* **Example Algorithms:** Linear Regression, Decision Trees, SVM, KNN.
* **Use Case Example:** Email spam detection (emails labeled as spam or not spam).

#### b. **Unsupervised Learning**

* **Definition:** Model is trained on data with no labels.
* **Goal:** Find hidden patterns or intrinsic structures.
* **Example Algorithms:** K-Means, PCA, DBSCAN, Hierarchical Clustering.
* **Use Case Example:** Customer segmentation.

#### c. **Semi-Supervised Learning**

* **Definition:** Combination of labeled and unlabeled data for training.
* **Goal:** Improve learning accuracy using a small amount of labeled data.
* **Use Case Example:** Classifying a large set of documents when only a few are labeled.

#### d. **Reinforcement Learning**

* **Definition:** An agent learns by interacting with the environment and receiving rewards or penalties.
* **Goal:** Maximize cumulative reward over time.
* **Example Algorithms:** Q-Learning, Deep Q Networks, Policy Gradients.
* **Use Case Example:** Game playing (e.g., Pacman, Chess AI).

---

### 5. **Common Steps in Machine Learning Process**

1. **Problem Definition**

   * Define the problem to solve (e.g., classification, regression).
2. **Data Collection**

   * Gather relevant data from different sources.
3. **Data Preprocessing**

   * Clean, transform, and prepare data.
4. **Feature Engineering**

   * Select or create features that contribute to model accuracy.
5. **Model Selection**

   * Choose appropriate ML algorithm.
6. **Training**

   * Feed data to the model and allow it to learn patterns.
7. **Evaluation**

   * Assess model performance using test data and evaluation metrics.
8. **Hyperparameter Tuning**

   * Adjust parameters to improve performance.
9. **Deployment**

   * Use the trained model in a production environment.
10. **Monitoring**

    * Continuously monitor and update the model as necessary.

---

### 6. **Key Concepts in ML**

* **Features:** Independent variables or attributes used for learning.
* **Labels:** Dependent variables or target outputs.
* **Training Set:** Data used to train the model.
* **Test Set:** Data used to evaluate the model.
* **Model:** The mathematical representation learned from data.

---

### 7. **Types of Problems in ML**

* **Classification:** Predict categorical output (e.g., spam or not spam).
* **Regression:** Predict continuous output (e.g., house price prediction).
* **Clustering:** Group similar items (e.g., customer segmentation).
* **Dimensionality Reduction:** Reduce the number of features (e.g., PCA).
* **Anomaly Detection:** Identify rare items or events (e.g., fraud detection).

---

### 8. **Real-World Examples of Machine Learning**

| Domain          | Application Example                        |
| --------------- | ------------------------------------------ |
| Healthcare      | Disease prediction, medical image analysis |
| Finance         | Fraud detection, credit scoring            |
| E-commerce      | Product recommendation engines             |
| Social Media    | Sentiment analysis, fake news detection    |
| Autonomous Cars | Lane detection, obstacle avoidance         |

---

### 9. **Python Code Example: Simple ML using `sklearn`**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### 10. **Conclusion**

* Machine Learning provides systems the ability to automatically learn and improve from experience.
* It powers numerous applications and is a critical component in modern artificial intelligence systems.

**Broad Categories of Machine Learning**

---

### 1. **Supervised Learning**

#### a. **Definition**

* Learning from a labeled dataset, where each input is paired with a correct output (target).
* Goal: Learn a mapping function from inputs $X$ to outputs $Y$:

  $$
  f: X \rightarrow Y
  $$

#### b. **Types**

* **Classification**: Output is a discrete label.
  Example: Email spam detection (spam / not spam)
* **Regression**: Output is a continuous value.
  Example: Predicting house prices

#### c. **Workflow**

1. Collect labeled dataset
2. Train model on (X, Y) pairs
3. Predict for new $X$, get predicted $Y$
4. Evaluate using metrics (Accuracy, RMSE, etc.)

#### d. **Example in Python: Classification using KNN**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

#### e. **Algorithms**

* Linear Regression
* Logistic Regression
* k-Nearest Neighbors (KNN)
* Support Vector Machines (SVM)
* Decision Trees
* Naive Bayes
* Neural Networks

---

### 2. **Unsupervised Learning**

#### a. **Definition**

* Learning from data with **no labels**.
* Goal: Discover hidden structure, patterns, or groupings.

#### b. **Tasks**

* **Clustering**: Group data into clusters
  Example: Customer segmentation
* **Dimensionality Reduction**: Reduce number of input variables
  Example: PCA for visualization or noise removal
* **Association Rule Learning**: Find rules among features
  Example: Market basket analysis

#### c. **Example in Python: Clustering using K-Means**

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(iris.data)

print("Cluster centers:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
```

#### d. **Algorithms**

* K-Means
* DBSCAN
* Hierarchical Clustering (Agglomerative)
* Principal Component Analysis (PCA)
* t-SNE

---

### 3. **Semi-Supervised Learning**

#### a. **Definition**

* Learning from a **small amount of labeled data** and a **large amount of unlabeled data**.
* Goal: Use the structure in unlabeled data to improve learning accuracy.

#### b. **Why Use It?**

* Labeling is expensive or time-consuming.
* Unlabeled data is abundant and cheap.

#### c. **Approaches**

* Self-training: Train model on labeled data, label some unlabeled examples, re-train.
* Graph-based models: Represent data as graph, spread labels via nodes.
* Generative models: Use mixture models or EM algorithm.

#### d. **Use Cases**

* Document classification with few labeled examples
* Image recognition with few labeled images

#### e. **No direct sklearn example**, but conceptually:

```python
# Pseudo code structure:
1. Train model on small labeled set
2. Predict labels for high-confidence unlabeled examples
3. Add confident predictions to labeled set
4. Retrain model
```

---

### 4. **Reinforcement Learning (RL)**

#### a. **Definition**

* Learning by interacting with an **environment**.
* Agent learns to take actions to **maximize cumulative reward** over time.

#### b. **Key Concepts**

* **Agent**: Learner/decision maker
* **Environment**: World the agent interacts with
* **State (S)**: Current situation of the agent
* **Action (A)**: Possible moves the agent can make
* **Reward (R)**: Feedback from the environment
* **Policy ($\pi$)**: Strategy used by the agent to decide actions

#### c. **Formalized as a Markov Decision Process (MDP)**

* Tuple: $(S, A, P, R, \gamma)$

#### d. **Learning Types**

* **Model-Free**

  * Q-Learning
  * Policy Gradient
* **Model-Based**

  * Agent builds a model of environment to plan

#### e. **Example in Python: Q-learning (simplified)**

```python
import numpy as np

q_table = np.zeros((5, 2))  # 5 states, 2 actions
learning_rate = 0.1
discount = 0.95

state = 0
action = 1
reward = 1
next_state = 1

# Q-learning update rule
q_table[state, action] = q_table[state, action] + learning_rate * (
    reward + discount * np.max(q_table[next_state]) - q_table[state, action]
)
print(q_table)
```

#### f. **Use Cases**

* Game AI (e.g., AlphaGo, Dota 2 bots)
* Robotics
* Dynamic pricing
* Self-driving cars

---

### Summary Table

| Category               | Data Type                 | Output           | Goal                        | Example Algorithms                          |
| ---------------------- | ------------------------- | ---------------- | --------------------------- | ------------------------------------------- |
| Supervised Learning    | Labeled                   | Known target     | Predict labels or values    | SVM, Decision Trees, KNN, Linear Regression |
| Unsupervised Learning  | Unlabeled                 | Hidden structure | Discover groups or patterns | K-Means, PCA, DBSCAN                        |
| Semi-Supervised        | Few labeled               | Partial labels   | Improve prediction accuracy | Self-training, Label propagation            |
| Reinforcement Learning | Feedback from environment | Rewards          | Learn action policy         | Q-Learning, Deep Q-Network, Policy Gradient |

**Application Areas of Machine Learning**

---

### 1. **Healthcare**

#### a. **Disease Diagnosis**

* ML models trained on medical records/images to predict disease.
* Example: Detection of cancer from MRI or X-ray images.

#### b. **Drug Discovery**

* Predict molecular interactions, bioactivity, and toxicity using ML.
* Speeds up drug design using supervised and reinforcement learning.

#### c. **Personalized Medicine**

* Recommending treatment plans based on patient genetic data.

#### d. **Python Example: Breast Cancer Prediction**

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### 2. **Finance**

#### a. **Fraud Detection**

* Identify fraudulent transactions using anomaly detection or classification.

#### b. **Credit Scoring**

* Predict loan repayment ability of users based on financial history.

#### c. **Algorithmic Trading**

* Use regression and reinforcement learning to make buy/sell decisions.

#### d. **Portfolio Management**

* Use ML to optimize asset allocation and risk balancing.

---

### 3. **Retail and E-commerce**

#### a. **Recommendation Systems**

* Suggest products using collaborative filtering and content-based filtering.
* Example: Amazon or Flipkart product suggestions.

#### b. **Customer Segmentation**

* Cluster customers by behavior and preferences (unsupervised learning).

#### c. **Price Optimization**

* Predict optimal product prices using demand forecasting.

---

### 4. **Manufacturing**

#### a. **Predictive Maintenance**

* Predict machine failures before they occur using time-series models.

#### b. **Quality Control**

* Image-based classification of defective products.

#### c. **Supply Chain Optimization**

* Demand forecasting, stock management using regression models.

---

### 5. **Marketing**

#### a. **Customer Lifetime Value Prediction**

* Regression models to estimate how long a customer will continue buying.

#### b. **Sentiment Analysis**

* Classify public opinions on products or brands using NLP.

#### c. **Targeted Advertising**

* Personalized ads based on user activity and demographics.

---

### 6. **Transportation and Logistics**

#### a. **Self-Driving Cars**

* Object detection, lane following, path planning using deep learning.

#### b. **Route Optimization**

* Dynamic route planning based on traffic data.

#### c. **Autonomous Delivery Drones**

* Reinforcement learning-based control systems for obstacle avoidance.

---

### 7. **Cybersecurity**

#### a. **Intrusion Detection**

* Anomaly detection in network traffic to identify threats.

#### b. **Malware Classification**

* Detect malicious files using supervised learning.

---

### 8. **Natural Language Processing (NLP)**

#### a. **Speech Recognition**

* Convert spoken language to text (e.g., Google Assistant).

#### b. **Machine Translation**

* Translate languages (e.g., Google Translate using sequence-to-sequence models).

#### c. **Chatbots and Virtual Assistants**

* Understand and respond to human queries using intent classification.

---

### 9. **Education**

#### a. **Automated Grading**

* ML algorithms assess student assignments and exams.

#### b. **Personalized Learning**

* Recommend study material and quizzes based on student's performance.

---

### 10. **Agriculture**

#### a. **Crop Disease Prediction**

* Image-based detection of plant diseases.

#### b. **Yield Prediction**

* Predict output using environmental and soil data.

---

### 11. **Energy**

#### a. **Load Forecasting**

* Predict future electricity consumption using time series models.

#### b. **Smart Grid Management**

* Optimize energy distribution using predictive analytics.

---

### 12. **Gaming and Simulation**

#### a. **AI Opponents**

* Reinforcement learning used to develop game-playing agents.

#### b. **Game Content Generation**

* Generative models to create levels or stories.

---

### 13. **Robotics**

#### a. **Navigation**

* Use CNNs and SLAM algorithms for robot localization and mapping.

#### b. **Grasping and Manipulation**

* Train robotic arms using reinforcement learning for tasks like pick and place.

---

### 14. **Astronomy**

#### a. **Star Classification**

* Cluster celestial bodies using unsupervised learning.

#### b. **Gravitational Wave Detection**

* Time-series analysis using ML for signal extraction.

---

### 15. **Real Estate**

#### a. **Price Prediction**

* Estimate property value based on location, area, features.

#### b. **Property Recommendation**

* Personalized listing suggestions using user browsing history.

---

### Summary Table

| Domain         | Applications                               | ML Techniques Used                  |
| -------------- | ------------------------------------------ | ----------------------------------- |
| Healthcare     | Diagnosis, Drug discovery, Personalization | Classification, Neural Networks     |
| Finance        | Fraud detection, Trading, Credit scoring   | Anomaly Detection, Regression       |
| Retail         | Recommendations, Price prediction          | Collaborative Filtering, Clustering |
| Manufacturing  | Maintenance, Quality control               | Time Series, Classification         |
| NLP            | Chatbots, Translation, Sentiment analysis  | RNNs, Transformers, Naive Bayes     |
| Transportation | Self-driving, Routing                      | CNNs, Reinforcement Learning        |
| Education      | Grading, Adaptive learning                 | Classification, Clustering          |
| Robotics       | Navigation, Control                        | CNNs, RL                            |
| Agriculture    | Disease detection, Yield prediction        | CNNs, Regression                    |
| Real Estate    | Price prediction, Recommendations          | Regression, KNN                     |

**Data Pre-processing in Machine Learning**

---

### 1. **Definition**

* Data Pre-processing is a data mining technique that transforms raw data into an understandable and efficient format.
* Essential for improving model accuracy and reducing noise or irrelevant data.

---

### 2. **Why Data Pre-processing is Needed**

* Raw data is often:

  * Incomplete (missing values)
  * Inconsistent (conflicting values)
  * Noisy (errors or outliers)
  * Not normalized or scaled
  * Categorical instead of numeric

---

### 3. **Steps in Data Pre-processing**

---

#### **Step 1: Data Cleaning**

##### a. **Handling Missing Data**

* Remove rows or columns with missing values.
* Impute missing values using:

  * Mean/Median/Mode (for numerical)
  * Most frequent value (for categorical)

**Python Example:**

```python
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'Age': [25, 30, None, 45],
    'Salary': [50000, 60000, 52000, None]
})

imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])

print(df)
```

##### b. **Handling Duplicates**

* Drop duplicate rows if they provide no extra value.

```python
df = df.drop_duplicates()
```

##### c. **Handling Outliers**

* Detect using IQR or Z-score and remove or cap.

```python
import numpy as np
z_scores = np.abs((df['Age'] - df['Age'].mean()) / df['Age'].std())
df = df[z_scores < 3]  # Remove outliers with Z-score > 3
```

---

#### **Step 2: Data Integration**

* Combine data from multiple sources (databases, APIs, files).
* Resolve conflicts (e.g., naming, units).

---

#### **Step 3: Data Transformation**

##### a. **Normalization / Feature Scaling**

* Ensures features contribute equally during training.

**Techniques:**

* **Min-Max Scaling**:

  $$
  x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
  $$

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[['Age', 'Salary']])
```

* **Standardization (Z-score Normalization)**:

  $$
  x' = \frac{x - \mu}{\sigma}
  $$

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
standardized = scaler.fit_transform(df[['Age', 'Salary']])
```

---

##### b. **Encoding Categorical Variables**

* **Label Encoding**: Converts categories to integers.

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Gender'] = le.fit_transform(['Male', 'Female', 'Female', 'Male'])
```

* **One-Hot Encoding**: Creates binary columns for each category.

```python
df = pd.get_dummies(df, columns=['Gender'])
```

---

#### **Step 4: Feature Extraction and Selection**

##### a. **Feature Extraction**

* Derive new features from raw data.
* Example: Extract year/month from date column.

##### b. **Feature Selection**

* Choose most relevant features for model input.
* Techniques: Chi-square test, ANOVA, Recursive Feature Elimination.

---

#### **Step 5: Data Discretization**

* Convert continuous data into discrete bins.

```python
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 50, 100], labels=['Young', 'Middle', 'Old'])
```

---

### 4. **Preprocessing Pipeline Using `sklearn`**

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['Age', 'Salary']], [1, 0, 1, 0], test_size=0.2)

pipeline = Pipeline([
    ('impute', SimpleImputer(strategy='mean')),
    ('scale', StandardScaler()),
    ('model', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
print("Score:", pipeline.score(X_test, y_test))
```

---

### 5. **Final Notes**

* Pre-processing should be performed before splitting the dataset into train and test.
* Always apply the same transformations to test data as the training data using fitted scalers/imputers.

---

### Summary Table

| Task                  | Technique                      | Library / Function                     |
| --------------------- | ------------------------------ | -------------------------------------- |
| Handle Missing Values | Imputation (mean/median)       | `SimpleImputer`                        |
| Remove Duplicates     | `drop_duplicates()`            | Pandas                                 |
| Normalize Data        | MinMaxScaler, StandardScaler   | `sklearn.preprocessing`                |
| Encode Categorical    | LabelEncoder, OneHotEncoder    | `sklearn.preprocessing`, `get_dummies` |
| Feature Engineering   | Manual or automated extraction | Pandas, `FeatureTools`                 |
| Feature Selection     | SelectKBest, RFE               | `sklearn.feature_selection`            |
| Build Pipeline        | Chain multiple steps           | `Pipeline()` from `sklearn.pipeline`   |

**Training and Choosing Predictive Models**

---

### 1. **Definition**

* **Training**: The process of teaching an ML model to make predictions or decisions by feeding it input data and corresponding outputs.
* **Choosing Predictive Models**: Selecting an appropriate algorithm and architecture that best fits the structure, size, and type of dataset for a given task (classification, regression, etc.).

---

### 2. **Steps in Training a Model**

---

#### **Step 1: Prepare the Dataset**

* **Split the dataset** into:

  * **Training set**: Used to train the model (usually 70–80%).
  * **Testing set**: Used to evaluate performance (20–30%).

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

#### **Step 2: Choose a Suitable Algorithm**

* Based on:

  * **Type of problem**: Classification, regression, clustering, etc.
  * **Size of dataset**
  * **Feature type**: Categorical, numerical, text
  * **Accuracy and interpretability requirements**
  * **Computational resources**

| Task           | Algorithms                                                                 |
| -------------- | -------------------------------------------------------------------------- |
| Classification | Logistic Regression, Decision Tree, SVM, KNN, Naive Bayes, Neural Networks |
| Regression     | Linear Regression, SVR, Decision Tree Regressor, Ridge, Lasso              |
| Clustering     | K-Means, DBSCAN, Agglomerative, GMM                                        |
| Time Series    | ARIMA, LSTM, Prophet                                                       |

---

#### **Step 3: Initialize and Train the Model**

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

---

#### **Step 4: Predict Using the Model**

```python
y_pred = model.predict(X_test)
```

---

#### **Step 5: Evaluate the Model**

* Based on the problem type:

**Classification Metrics:**

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC

**Regression Metrics:**

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* R² Score

```python
from sklearn.metrics import accuracy_score, confusion_matrix
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

---

### 3. **Choosing the Right Predictive Model**

---

#### **A. Consider the Nature of the Target Variable**

* **Categorical Output → Classification**

  * Example: Email spam (Yes/No)
* **Continuous Output → Regression**

  * Example: House price prediction

---

#### **B. Size of Data**

* **Small Dataset**:

  * Logistic Regression
  * Decision Trees
  * Naive Bayes
* **Large Dataset**:

  * Neural Networks
  * Gradient Boosting Machines (XGBoost, LightGBM)

---

#### **C. Linearity of Data**

* **Linear Relationships**:

  * Linear Regression, Logistic Regression
* **Non-Linear Relationships**:

  * Decision Trees, Random Forest, SVM (RBF), Neural Networks

---

#### **D. Feature Type**

* **Numerical Features**: Linear/Logistic Regression
* **Categorical Features**: Decision Trees, Naive Bayes

---

#### **E. Model Interpretability**

* If interpretability is needed (e.g., for healthcare):

  * Prefer Logistic Regression, Decision Trees

---

### 4. **Model Comparison Example (Classification)**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

models = {
    'LogisticRegression': LogisticRegression(),
    'DecisionTree': DecisionTreeClassifier(),
    'SVM': SVC()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{name} Accuracy:", accuracy_score(y_test, y_pred))
```

---

### 5. **Overfitting and Underfitting**

#### a. **Overfitting**

* Model learns noise and performs well on training but poorly on test data.
* **Solution**: Cross-validation, regularization, pruning, dropout (NNs)

#### b. **Underfitting**

* Model is too simple and fails to capture the pattern.
* **Solution**: Use complex models, feature engineering

---

### 6. **Cross-Validation (for better training)**

* Evaluate model on different train/test splits to avoid overfitting.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(LogisticRegression(), X, y, cv=5)
print("Cross-validation scores:", scores)
```

---

### 7. **Hyperparameter Tuning (Model Optimization)**

* Use GridSearchCV or RandomizedSearchCV to find best parameters.

```python
from sklearn.model_selection import GridSearchCV

params = {'C': [0.1, 1, 10]}
grid = GridSearchCV(LogisticRegression(), param_grid=params, cv=5)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
```

---

### 8. **Final Model Deployment**

* Save and export trained model for production use.

```python
import joblib
joblib.dump(model, 'model.pkl')

# Load later
model = joblib.load('model.pkl')
```

---

### Summary Table

| Step            | Description               | Python Tool                          |
| --------------- | ------------------------- | ------------------------------------ |
| Split data      | Training vs Test          | `train_test_split()`                 |
| Select model    | Based on problem and data | LogisticRegression, SVM, etc.        |
| Train model     | Fit model on training set | `model.fit()`                        |
| Predict results | Generate predictions      | `model.predict()`                    |
| Evaluate model  | Measure accuracy, F1, MSE | `accuracy_score`, `confusion_matrix` |
| Tune model      | Improve with parameters   | `GridSearchCV`, `RandomSearchCV`     |
| Save model      | Persist model for reuse   | `joblib.dump()`, `pickle.dump()`     |

**Model Evaluation and Validation of Unseen Data Instances**

---

### 1. **Definition**

* **Model Evaluation**: Process of assessing how well a trained machine learning model performs on test or validation data.
* **Validation of Unseen Data Instances**: Measuring model performance on new data not used during training to check generalization.

---

### 2. **Why Evaluation and Validation Are Important**

* To ensure the model:

  * Generalizes well to unseen data
  * Doesn’t overfit or underfit
  * Is reliable and accurate in real-world usage

---

### 3. **Evaluation Techniques**

---

#### **A. Hold-Out Validation**

* Split dataset into:

  * Training set (e.g. 80%)
  * Testing set (e.g. 20%)

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

* Train model on `X_train`, evaluate on `X_test`

---

#### **B. K-Fold Cross Validation**

* Split data into `k` equal parts.
* Train the model on `k-1` folds, test on the remaining fold.
* Repeat `k` times and take average accuracy.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

scores = cross_val_score(LogisticRegression(), X, y, cv=5)
print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
```

---

#### **C. Stratified K-Fold Cross Validation**

* Ensures each fold has the same proportion of class labels (for classification problems).

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5)
```

---

#### **D. Leave-One-Out Cross Validation (LOOCV)**

* Train on all data except one instance, test on the left-out one.
* Repeat for all instances.

```python
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()
```

---

### 4. **Common Evaluation Metrics**

---

#### **A. For Classification Problems**

| Metric               | Formula or Description                                        |
| -------------------- | ------------------------------------------------------------- |
| **Accuracy**         | $\frac{TP + TN}{TP + TN + FP + FN}$                           |
| **Precision**        | $\frac{TP}{TP + FP}$                                          |
| **Recall**           | $\frac{TP}{TP + FN}$                                          |
| **F1 Score**         | $2 \times \frac{Precision \times Recall}{Precision + Recall}$ |
| **Confusion Matrix** | Matrix of TP, TN, FP, FN                                      |
| **ROC-AUC**          | Area under Receiver Operating Characteristic curve            |

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1 Score:", f1_score(y_test, y_pred, average='macro'))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

---

#### **B. For Regression Problems**

| Metric                                      | Formula / Description                  |                   |   |
| ------------------------------------------- | -------------------------------------- | ----------------- | - |
| **Mean Absolute Error (MAE)**               | ( \frac{1}{n} \sum                     | y\_i - \hat{y}\_i | ) |
| **Mean Squared Error (MSE)**                | $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ |                   |   |
| **Root Mean Squared Error (RMSE)**          | $\sqrt{MSE}$                           |                   |   |
| **R² Score (Coefficient of Determination)** | $1 - \frac{SS_{res}}{SS_{tot}}$        |                   |   |

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))
```

---

### 5. **Validation Using Unseen Data Instances**

* After selecting the best model using cross-validation:

  * Final performance must be tested on a **completely new test set** (unseen during training and validation).
  * This simulates real-world data prediction.

```python
# Assume unseen_data is the actual real-world data
unseen_pred = model.predict(unseen_data)
```

---

### 6. **Overfitting vs. Underfitting**

| Type             | Description                                     | Symptoms                           |
| ---------------- | ----------------------------------------------- | ---------------------------------- |
| **Overfitting**  | High accuracy on training but poor on test      | Model memorizes training data      |
| **Underfitting** | Poor performance on both training and test data | Model too simple to learn the data |

---

### 7. **Confusion Matrix Example**

Assume prediction on binary classification (1 = spam, 0 = not spam):

```python
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
```

Example Output:

```
               Predicted
               0     1
Actual   0    88    12
         1    10    90
```

* **True Positives (TP)**: 90
* **True Negatives (TN)**: 88
* **False Positives (FP)**: 12
* **False Negatives (FN)**: 10

---

### 8. **Receiver Operating Characteristic (ROC) Curve**

* Plot of True Positive Rate vs False Positive Rate at various threshold settings.
* Used to evaluate binary classifiers.

```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

y_scores = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
```

---

### Summary Table

| Type           | Metric                       | Suitable For       | `sklearn` Function                            |
| -------------- | ---------------------------- | ------------------ | --------------------------------------------- |
| Classification | Accuracy, F1, ROC-AUC        | Discrete Outputs   | `accuracy_score`, `f1_score`, `roc_auc_score` |
| Regression     | MAE, MSE, R²                 | Continuous Outputs | `mean_squared_error`, `r2_score`              |
| Evaluation     | Confusion Matrix             | Binary/Multiclass  | `confusion_matrix`                            |
| Validation     | K-Fold, LOOCV                | All tasks          | `cross_val_score`                             |
| Visual Tools   | ROC, Precision-Recall Curves | Binary tasks       | `roc_curve`, `ConfusionMatrixDisplay`         |

