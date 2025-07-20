# Unit - 3 -> Unsupervised learning
Introduction, tupes and challenges, preprocessing and scaling of dataset, Dimensinality reduction, feature extraction, Principal Compinet Analysis (PCA), k-means, Agglomerative and DBSCAN clustering algorithms.

## Content ->
### **Unit 3 – Unsupervised Learning: Introduction**

---

#### **1. Definition of Unsupervised Learning**

* A type of machine learning where:

  * The model is trained on **unlabeled data** (no output variable).
  * The goal is to **discover hidden patterns, groupings, or structures** in the data.
  * No supervision is provided during training (i.e., no “correct answers”).

---

#### **2. Key Objectives**

* **Cluster** similar data points together (e.g., customer segmentation).
* **Reduce dimensionality** while preserving key features (e.g., PCA).
* **Discover latent variables** (hidden causes or patterns).
* **Detect anomalies** (e.g., fraud detection).
* **Find associations** (e.g., market basket analysis).

---

#### **3. Main Characteristics**

* **No ground truth (no labels)** is used during training.
* Learning is **data-driven and exploratory**.
* Often used for **preprocessing or exploratory data analysis (EDA)**.
* Models try to learn the **underlying structure** of the data.

---

#### **4. Example Problem**

* Given the following data (without labels):

  ```python
  import numpy as np
  X = np.array([[1.0, 2.0],
                [1.2, 1.8],
                [5.0, 8.0],
                [6.0, 9.0]])
  ```

  A clustering algorithm like K-means can group the first two points and the last two into separate clusters based on distance.

---

#### **5. Common Unsupervised Learning Algorithms**

* **Clustering**

  * K-Means
  * DBSCAN
  * Agglomerative Hierarchical Clustering
* **Dimensionality Reduction**

  * PCA (Principal Component Analysis)
  * t-SNE
  * Autoencoders
* **Association Rule Mining**

  * Apriori algorithm
  * FP-growth

---

#### **6. Applications**

* Customer segmentation
* Anomaly detection
* Data compression
* Document clustering
* Image segmentation
* Pattern recognition

---

#### **7. Comparison with Supervised Learning**

| Feature           | Supervised Learning  | Unsupervised Learning |
| ----------------- | -------------------- | --------------------- |
| Input Data        | Labeled              | Unlabeled             |
| Output            | Prediction           | Pattern discovery     |
| Common Algorithms | SVM, Decision Tree   | K-means, PCA, DBSCAN  |
| Example           | Email spam detection | Customer segmentation |

---

#### **8. Visualization Example with PCA + KMeans**

```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = load_iris()
X = data.data

# Dimensionality Reduction using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Clustering using KMeans
kmeans = KMeans(n_clusters=3)
y_kmeans = kmeans.fit_predict(X_pca)

# Plotting clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='viridis')
plt.title("K-Means Clustering after PCA")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.show()
```

---

#### **9. Limitations**

* Hard to evaluate model accuracy due to no labels.
* May discover meaningless patterns if data is noisy.
* Sensitive to data scaling and initial parameters.

---

#### **10. Summary**

* Unsupervised learning explores **unknown structure** in unlabeled data.
* Often used for **clustering**, **compression**, and **pattern discovery**.
* **Essential for exploratory data analysis and representation learning**.

---

## **1. Types of Unsupervised Learning**

---

### **1.1. Clustering**

* **Objective**: Group data points into clusters where points in the same cluster are similar.
* **Algorithms**:

  * **K-Means**
  * **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
  * **Agglomerative Hierarchical Clustering**
* **Use cases**:

  * Customer segmentation
  * Document grouping
  * Image segmentation

---

### **1.2. Dimensionality Reduction**

* **Objective**: Reduce the number of input variables or features while preserving the information.
* **Algorithms**:

  * **PCA (Principal Component Analysis)**
  * **t-SNE (t-distributed Stochastic Neighbor Embedding)**
  * **Autoencoders (Neural Networks)**
* **Use cases**:

  * Data visualization
  * Noise reduction
  * Feature extraction for supervised models

---

### **1.3. Anomaly Detection**

* **Objective**: Detect rare or unusual data points (outliers).
* **Algorithms**:

  * One-class SVM
  * Isolation Forest
  * DBSCAN (can identify noise)
* **Use cases**:

  * Fraud detection
  * Fault detection in manufacturing
  * Network intrusion detection

---

### **1.4. Association Rule Mining**

* **Objective**: Discover interesting relationships or associations between variables in large datasets.
* **Algorithms**:

  * Apriori algorithm
  * FP-Growth
* **Use cases**:

  * Market basket analysis
  * Recommender systems

---

### **1.5. Generative Models**

* **Objective**: Learn to model the underlying distribution of data and generate new samples.
* **Examples**:

  * GANs (Generative Adversarial Networks)
  * Variational Autoencoders (VAE)
* **Use cases**:

  * Image generation
  * Data augmentation
  * Style transfer

---

## **2. Challenges in Unsupervised Learning**

---

### **2.1. Lack of Ground Truth**

* **Problem**: No labeled output means no way to directly evaluate model performance.
* **Impact**: Difficult to validate clustering or structure learned by the model.

---

### **2.2. Interpretability**

* **Problem**: Unsupervised models often find latent features that may not have intuitive meaning.
* **Impact**: Makes explaining results to humans or stakeholders harder.

---

### **2.3. Choosing the Number of Clusters or Components**

* **Problem**: Algorithms like K-Means or PCA require specification of number of clusters/components.
* **Impact**: Improper selection may lead to poor results.
* **Solution**: Use metrics like Silhouette Score, Elbow Method, or Variance Explained.

---

### **2.4. Sensitivity to Scaling**

* **Problem**: Many algorithms (e.g., K-Means, PCA) are sensitive to the scale of input features.
* **Impact**: Features with larger scales dominate distance-based metrics.
* **Solution**: Apply preprocessing like **StandardScaler** or **MinMaxScaler**.

---

### **2.5. High Dimensionality (Curse of Dimensionality)**

* **Problem**: As the number of dimensions increases, data becomes sparse, and distances lose meaning.
* **Impact**: Clustering and nearest neighbor methods become ineffective.
* **Solution**: Use dimensionality reduction (PCA, t-SNE).

---

### **2.6. Initialization Sensitivity**

* **Problem**: Algorithms like K-Means can converge to local minima based on initial centroids.
* **Impact**: May produce different results on different runs.
* **Solution**: Run multiple times with different seeds or use smarter initialization (e.g., KMeans++).

---

### **2.7. Noisy Data and Outliers**

* **Problem**: Outliers can distort clustering and dimensionality reduction.
* **Impact**: Poor model performance.
* **Solution**: Preprocess to remove or handle outliers.

---

### **2.8. Scalability to Large Datasets**

* **Problem**: Algorithms like Agglomerative clustering have high computational complexity.
* **Impact**: Long training times on big data.
* **Solution**: Use scalable algorithms (e.g., MiniBatch K-Means).

---

### **2.9. Overfitting in Generative Models**

* **Problem**: Models like Autoencoders can memorize training data.
* **Impact**: Poor generalization to new samples.
* **Solution**: Use regularization, dropout, or increase dataset size.

---

### **2.10. Evaluation Metrics**

* **Problem**: No labels make it difficult to assess model quality.
* **Solutions**:

  * Internal metrics (Silhouette score, Davies-Bouldin index)
  * Visualizations
  * External metrics (if some ground truth is available): Adjusted Rand Index, Mutual Information

---

## **3. Summary Table**

| Type                     | Goal                       | Common Algorithms        | Challenge Example                    |
| ------------------------ | -------------------------- | ------------------------ | ------------------------------------ |
| Clustering               | Group similar data points  | K-Means, DBSCAN          | Choosing number of clusters          |
| Dimensionality Reduction | Reduce features, keep info | PCA, t-SNE, Autoencoders | Interpreting new dimensions          |
| Anomaly Detection        | Detect unusual patterns    | Isolation Forest, DBSCAN | High false positives                 |
| Association Mining       | Find co-occurring items    | Apriori, FP-Growth       | Too many uninteresting rules         |
| Generative Modeling      | Generate new similar data  | GANs, VAEs               | Overfitting and training instability |

---

## **Conclusion**

* Unsupervised learning has **diverse types** and is critical for **hidden pattern discovery**.
* Challenges mainly arise due to **lack of labels**, **high dimensionality**, **sensitivity to parameters**, and **interpretability**.
* **Proper preprocessing**, **metric evaluation**, and **algorithm choice** are essential.

### **Unit 3 – Unsupervised Learning: Preprocessing and Scaling of Dataset**

---

## **1. Introduction to Preprocessing**

Data preprocessing is the critical first step in any machine learning task. In unsupervised learning, preprocessing is especially important due to the absence of labeled data. Poorly preprocessed data can lead to misleading clusters, distorted feature spaces, or meaningless patterns.

---

## **2. Objectives of Preprocessing**

* Remove noise and inconsistencies
* Handle missing or redundant values
* Standardize or normalize feature values
* Prepare data for clustering or dimensionality reduction algorithms
* Improve performance and reliability of algorithms

---

## **3. Common Preprocessing Steps**

---

### **3.1. Handling Missing Values**

* **Techniques**:

  * **Removal**: Delete rows/columns with missing values (if proportion is low)
  * **Imputation**:

    * **Mean/Median/Mode Imputation** for numeric data
    * **Most Frequent** or **Constant** for categorical data
    * **KNN Imputation**: Use similarity to estimate missing value
* **Impact**: Prevents loss of data and ensures mathematical operations are defined

---

### **3.2. Removing Duplicates**

* **Method**: Identify and remove duplicate rows to avoid overemphasis on repeated data
* **Tool**: `pandas.DataFrame.drop_duplicates()`

---

### **3.3. Removing Noise and Outliers**

* **Techniques**:

  * **Z-Score method** (values with Z > 3 considered outliers)
  * **IQR Method** (Q1 - 1.5×IQR and Q3 + 1.5×IQR)
  * **Visual tools**: Box plots, scatter plots
* **Impact**: Reduces skewed distances in clustering algorithms

---

### **3.4. Encoding Categorical Data**

* **One-Hot Encoding**: Converts categories into binary columns
* **Label Encoding**: Converts categories into integers (can mislead distance-based methods)
* **Impact**: Allows inclusion of categorical data in numerical algorithms

---

### **3.5. Feature Selection**

* Remove irrelevant or highly correlated features
* Methods:

  * **Variance Threshold** (drop low-variance features)
  * **Correlation Matrix**
* Improves clustering and PCA effectiveness

---

## **4. Feature Scaling**

Feature scaling ensures that no single feature dominates others due to scale. Many unsupervised algorithms rely on distance measures (e.g., Euclidean distance), so inconsistent feature ranges can distort outcomes.

---

### **4.1. Why Scaling is Important**

* Prevents **biased distance calculations**
* Required for **K-Means**, **PCA**, **DBSCAN**, etc.
* Ensures **fair contribution** of all features

---

## **5. Common Scaling Techniques**

---

### **5.1. Min-Max Scaling (Normalization)**

* **Formula**:

  $$
  X_{\text{scaled}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}
  $$
* **Range**: Scales features to \[0, 1]
* **Best for**: When data does not contain outliers
* **Tool**: `sklearn.preprocessing.MinMaxScaler`

---

### **5.2. Standardization (Z-score Scaling)**

* **Formula**:

  $$
  X_{\text{scaled}} = \frac{X - \mu}{\sigma}
  $$
* **Range**: Mean = 0, Std. Dev. = 1
* **Best for**: When data contains outliers and is normally distributed
* **Tool**: `sklearn.preprocessing.StandardScaler`

---

### **5.3. MaxAbs Scaling**

* **Formula**:

  $$
  X_{\text{scaled}} = \frac{X}{|X_{\text{max}}|}
  $$
* Scales features to \[-1, 1]
* Preserves sparsity (non-zero structure)
* Useful for sparse data (e.g., text features)
* **Tool**: `sklearn.preprocessing.MaxAbsScaler`

---

### **5.4. Robust Scaling**

* Uses **median** and **IQR** instead of mean and std. dev.
* **Formula**:

  $$
  X_{\text{scaled}} = \frac{X - \text{median}}{\text{IQR}}
  $$
* Best for **datasets with outliers**
* **Tool**: `sklearn.preprocessing.RobustScaler`

---

## **6. Dimensionality Reduction Preprocessing**

Before applying algorithms like PCA or t-SNE:

* **Centering the data** (mean = 0) is necessary
* **Feature scaling** is essential for **PCA**
* Remove multicollinearity among features
* Apply **log or square-root transforms** for skewed data

---

## **7. Summary Table**

| Preprocessing Step     | Purpose                          | Key Tools                        |
| ---------------------- | -------------------------------- | -------------------------------- |
| Missing Value Handling | Avoid loss or corruption of data | `SimpleImputer`, `KNNImputer`    |
| Outlier Removal        | Eliminate distortion in patterns | Z-score, IQR, Box plots          |
| Feature Scaling        | Uniform contribution to distance | `MinMaxScaler`, `StandardScaler` |
| Categorical Encoding   | Convert to numerical form        | `OneHotEncoder`, `LabelEncoder`  |
| Noise Reduction        | Improve quality of data          | Filters, visual checks           |
| Feature Selection      | Reduce redundancy                | Variance threshold, correlation  |

---

## **8. Conclusion**

* Preprocessing and scaling are **essential** for effective unsupervised learning.
* Proper preprocessing ensures **robust clustering**, **accurate dimensionality reduction**, and **meaningful structure detection**.
* Always apply **scaling before** algorithms that depend on distances or magnitudes.

### **Unit 3 – Unsupervised Learning: Dimensionality Reduction**

---

## **1. Definition**

Dimensionality reduction refers to the process of reducing the number of input variables or features in a dataset while preserving the essential structure and information. It simplifies datasets, removes noise, and makes patterns more interpretable.

---

## **2. Objectives**

* Reduce computational cost and memory
* Remove multicollinearity and noise
* Visualize high-dimensional data (2D/3D)
* Improve clustering or classification performance
* Prevent overfitting and enhance generalization

---

## **3. Types of Dimensionality Reduction Techniques**

Dimensionality reduction is generally categorized into:

---

### **3.1. Feature Selection (Filter-based)**

* Selects a subset of the original features
* Keeps the most informative variables
* Examples:

  * Variance Thresholding
  * Mutual Information
  * Correlation-based Selection

---

### **3.2. Feature Extraction (Projection-based)**

* Transforms data to a lower-dimensional space
* Combines or compresses original features into new ones
* Techniques:

  * **Principal Component Analysis (PCA)**
  * **Linear Discriminant Analysis (LDA)** (supervised)
  * **t-Distributed Stochastic Neighbor Embedding (t-SNE)**
  * **Autoencoders** (Neural networks-based)

---

## **4. Why Dimensionality Reduction is Needed**

* High-dimensional datasets (curse of dimensionality) make clustering inefficient and less accurate.
* Many features may be redundant or irrelevant.
* Visual interpretation becomes impossible beyond 3D.

---

## **5. Curse of Dimensionality**

* As dimensions increase:

  * Distance metrics lose meaning
  * Data becomes sparse
  * Overfitting increases
  * Computation becomes expensive

---

## **6. Principal Component Analysis (PCA)**

### **Definition**:

PCA is a statistical technique that transforms original correlated features into a set of linearly uncorrelated features called **principal components**.

### **Key Concepts**:

* First component captures the maximum variance
* Each subsequent component captures remaining variance orthogonal to the previous one
* Components are eigenvectors of the covariance matrix

### **Steps**:

1. Standardize the data
2. Compute covariance matrix
3. Compute eigenvectors and eigenvalues
4. Sort eigenvalues and select top-k components
5. Project data onto new axes

### **Advantages**:

* Fast and interpretable
* Preserves variance
* Used before clustering (e.g., K-means)

---

## **7. t-SNE (t-distributed Stochastic Neighbor Embedding)**

### **Definition**:

Non-linear dimensionality reduction technique for visualizing high-dimensional data in 2D or 3D.

### **Key Features**:

* Captures local structure and patterns
* Preserves neighborhood relationships
* Common in image and text data visualization

### **Limitations**:

* Computationally expensive
* Not suitable for scaling or clustering directly

---

## **8. Autoencoders**

### **Definition**:

Neural network-based unsupervised technique that learns to compress and then reconstruct the input data.

### **Structure**:

* Encoder: compresses data to lower dimensions
* Decoder: reconstructs data from compressed representation
* Bottleneck layer holds compressed data

### **Use Case**:

* Effective for large-scale, complex, nonlinear datasets

---

## **9. UMAP (Uniform Manifold Approximation and Projection)**

* Similar to t-SNE but faster and scalable
* Preserves both global and local structure
* Suitable for real-time visualization

---

## **10. Comparison Table**

| Technique    | Linear/Non-linear | Use Case                      | Suitable for Visualization |
| ------------ | ----------------- | ----------------------------- | -------------------------- |
| PCA          | Linear            | Fast, large datasets          | Limited (2D/3D)            |
| t-SNE        | Non-linear        | Small/medium, visualization   | Yes                        |
| Autoencoders | Non-linear        | Deep learning, large datasets | No (used for compression)  |
| UMAP         | Non-linear        | Fast visualization            | Yes                        |

---

## **11. Evaluation Metrics**

* **Explained Variance Ratio**: In PCA, percentage of data variance captured by each principal component
* **Reconstruction Error**: Used in autoencoders, measures difference between input and output
* **Clustering Accuracy (Post-reduction)**: How well clusters are formed after reduction

---

## **12. Conclusion**

* Dimensionality reduction is crucial for efficient and interpretable unsupervised learning.
* PCA is the most commonly used linear method.
* For complex datasets, nonlinear methods like t-SNE, UMAP, and autoencoders are preferred.
* Reduction must be preceded by preprocessing and scaling.

### **Unit 3 – Unsupervised Learning: Feature Extraction**

---

## **1. Definition**

Feature extraction is the process of transforming raw data into a set of informative and non-redundant features that can be effectively used in machine learning tasks. It reduces the dimensionality by generating new features that capture the essential characteristics of the original data.

---

## **2. Objectives of Feature Extraction**

* Reduce the number of input variables
* Increase learning accuracy
* Improve computational efficiency
* Extract hidden structures and patterns
* Enable better visualization and clustering

---

## **3. Feature Extraction vs Feature Selection**

| Feature Selection                      | Feature Extraction                          |
| -------------------------------------- | ------------------------------------------- |
| Selects a subset of existing features  | Creates new features from original features |
| No transformation of original features | Transforms data into a new feature space    |
| Simpler, interpretable                 | May be complex but more powerful            |

---

## **4. Types of Feature Extraction Techniques**

---

### **4.1. Linear Techniques**

#### a. **Principal Component Analysis (PCA)**

* Projects data onto a new coordinate system with reduced dimensions.
* Captures maximum variance in fewer features (principal components).
* Features are uncorrelated and ordered by importance.

#### b. **Independent Component Analysis (ICA)**

* Similar to PCA but finds statistically independent components instead of uncorrelated ones.
* Suitable for blind source separation (e.g., audio signal decomposition).

#### c. **Linear Discriminant Analysis (LDA)**

* Supervised method for maximizing class separability.
* Projects data onto a lower-dimensional space with maximum class distinction.

---

### **4.2. Non-Linear Techniques**

#### a. **t-SNE (t-distributed Stochastic Neighbor Embedding)**

* Preserves local relationships between points.
* Mainly used for data visualization in 2D/3D.
* Not suitable for general-purpose feature extraction.

#### b. **Isomap**

* Maintains geodesic distances on a data manifold.
* Useful for nonlinear dimensionality reduction.

#### c. **UMAP (Uniform Manifold Approximation and Projection)**

* Preserves both local and global structure.
* Faster and more scalable than t-SNE.

---

### **4.3. Neural Network-Based Techniques**

#### a. **Autoencoders**

* Use deep learning to compress and reconstruct data.
* Bottleneck layer acts as the feature extractor.
* Handles nonlinear relationships.

#### b. **Convolutional Neural Networks (CNNs)**

* Extract spatial features from images.
* Lower layers extract edges/textures; higher layers extract abstract patterns.
* Used in computer vision, object recognition, etc.

#### c. **Recurrent Neural Networks (RNNs)**

* Extract sequential features from time-series data.
* Suitable for language modeling, audio signals, etc.

---

## **5. Feature Extraction in Text Data**

* **Bag-of-Words (BoW)**: Represents text by word frequency vectors.
* **TF-IDF**: Weighs words based on importance (term frequency × inverse document frequency).
* **Word Embeddings**: Captures semantic meaning using vectors (e.g., Word2Vec, GloVe).
* **Transformers (BERT)**: Extract contextual embeddings of words.

---

## **6. Feature Extraction in Image Data**

* **Edge detection**: Using Sobel, Canny, etc.
* **Histogram of Oriented Gradients (HOG)**: Extracts edge orientation patterns.
* **Scale-Invariant Feature Transform (SIFT)**: Detects local features invariant to scale/rotation.
* **CNN features**: Automatically learned features through convolutional layers.

---

## **7. Applications of Feature Extraction**

* **Computer Vision**: Object recognition, facial recognition
* **Natural Language Processing**: Sentiment analysis, document classification
* **Speech Processing**: Speaker identification, emotion detection
* **Bioinformatics**: Gene expression analysis, disease classification

---

## **8. Evaluation of Extracted Features**

* **Variance Explained** (PCA)
* **Reconstruction Error** (Autoencoders)
* **Clustering Accuracy** (Post-extraction performance)
* **Silhouette Score** (Clustering compactness)

---

## **9. Advantages**

* Captures complex structures in data
* Reduces redundancy and noise
* Enables effective clustering and classification
* Improves model generalization

---

## **10. Conclusion**

* Feature extraction is essential for simplifying complex data and enabling efficient unsupervised learning.
* Linear techniques (e.g., PCA) are fast and interpretable.
* Nonlinear and neural-based methods are powerful for capturing deeper patterns.
* Proper preprocessing (e.g., normalization, scaling) is necessary before applying extraction techniques.

### **Unit 3 – Unsupervised Learning: Principal Component Analysis (PCA)**

---

## **1. Definition**

Principal Component Analysis (PCA) is a statistical technique used for **dimensionality reduction** by transforming a large set of correlated variables into a smaller set of **uncorrelated variables** called **principal components**. These components capture the maximum variance in the data.

---

## **2. Objectives**

* Reduce dimensionality while preserving variance
* Remove redundancy and multicollinearity
* Improve performance of machine learning models
* Visualize high-dimensional data in 2D or 3D
* Extract meaningful features from noisy data

---

## **3. Key Concepts**

| Concept                  | Description                                       |
| ------------------------ | ------------------------------------------------- |
| **Variance**             | Amount of information spread in data              |
| **Covariance Matrix**    | Measures how two variables vary together          |
| **Eigenvectors**         | Directions of the new feature space               |
| **Eigenvalues**          | Amount of variance carried by each eigenvector    |
| **Principal Components** | Ordered set of orthogonal axes capturing variance |

---

## **4. PCA Process (Step-by-Step)**

1. **Standardize the Data**

   * Subtract the mean and divide by standard deviation for each feature.
   * Required to treat all features equally.

2. **Compute Covariance Matrix**

   * Calculate covariance between all pairs of features.
   * Matrix is of size $n \times n$ for $n$ features.

3. **Compute Eigenvectors and Eigenvalues**

   * Eigenvectors define the direction of new axes (principal components).
   * Eigenvalues define the magnitude (variance) along those axes.

4. **Sort and Select Top-k Components**

   * Sort eigenvalues in descending order.
   * Select top $k$ eigenvectors (principal components) with highest eigenvalues.

5. **Project Data**

   * Multiply original data matrix by selected eigenvectors.
   * New data has reduced dimensions but preserves maximum variance.

---

## **5. Mathematical Representation**

Let:

* $X$: mean-centered data matrix of size $m \times n$
* $C = \frac{1}{m-1} X^T X$: covariance matrix
* $\mathbf{v}_i$: eigenvectors (principal components)
* $\lambda_i$: eigenvalues (variances)

PCA projection:

$$
X_{\text{new}} = X \cdot W_k
$$

where $W_k$ is a matrix of top $k$ eigenvectors.

---

## **6. Explained Variance Ratio**

* Measures how much variance each principal component captures.
* Useful for selecting the number of components:

  $$
  \text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^{n} \lambda_j}
  $$
* **Scree Plot** is used to visualize this and decide the optimal number of components.

---

## **7. Advantages of PCA**

* Reduces computation time
* Removes noise and multicollinearity
* Improves visualization
* Helps in compressing data
* Useful before clustering and classification

---

## **8. Disadvantages of PCA**

* Assumes linearity
* Components are difficult to interpret
* Loses some information (though minimal)
* Affected by outliers
* Doesn’t work well with categorical variables

---

## **9. Applications**

* **Image Compression**: Reduces dimensions of pixel data
* **Genomics**: Visualizes gene expression data
* **Finance**: Analyzes financial time series
* **Natural Language Processing**: Reduces word embedding dimensions
* **Recommender Systems**: Compresses user-item matrices

---

## **10. Comparison with Other Methods**

| Technique   | Linearity  | Interpretability | Use Case                      |
| ----------- | ---------- | ---------------- | ----------------------------- |
| PCA         | Linear     | Moderate         | General-purpose               |
| t-SNE       | Non-linear | Low              | Visualization                 |
| LDA         | Linear     | High             | Classification                |
| Autoencoder | Non-linear | Low              | Deep learning-based reduction |

---

## **11. Example**

Given a dataset with 3 correlated features:

1. PCA transforms it into 3 uncorrelated principal components.
2. You can keep top 2 components that explain, say, 95% variance.
3. You reduce the data from 3D to 2D while preserving the structure.

---

## **12. Conclusion**

PCA is a powerful and commonly used unsupervised technique for simplifying high-dimensional data while retaining the most important information. It is essential for exploratory data analysis, visualization, and preprocessing in machine learning pipelines.

### **Unit 3 – Unsupervised Learning: K-Means Clustering (with Python Example)**

---

## **1. Definition**

K-Means is an **unsupervised clustering algorithm** used to **partition data into `k` clusters**, where each data point belongs to the cluster with the **nearest mean** (centroid).

---

## **2. Objectives**

* Group data into meaningful clusters
* Minimize **intra-cluster variance**
* Maximize **inter-cluster separation**

---

## **3. Key Concepts**

| Concept          | Description                                      |
| ---------------- | ------------------------------------------------ |
| **Centroid**     | Center of a cluster (mean of points)             |
| **Inertia**      | Sum of squared distances to the closest centroid |
| **Elbow Method** | Used to determine optimal value of `k`           |
| **Convergence**  | When centroids stop moving or change is minimal  |

---

## **4. Algorithm Steps**

1. Choose number of clusters `k`
2. Initialize `k` random centroids
3. Assign each data point to the nearest centroid
4. Compute new centroids by averaging points in each cluster
5. Repeat steps 3–4 until centroids stabilize (convergence)

---

## **5. Advantages**

* Simple and fast
* Scales to large datasets
* Often gives good results

---

## **6. Disadvantages**

* Must specify `k` in advance
* Sensitive to initialization
* Struggles with non-spherical clusters and noise
* Assumes equal cluster sizes

---

## **7. Applications**

* Customer segmentation
* Market basket analysis
* Document clustering
* Image compression
* Anomaly detection

---

## **8. Python Example**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

# Fit KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("K-Means Clustering Example")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
```

---

## **9. Explanation of Code**

* `make_blobs`: generates synthetic data for clustering
* `KMeans(n_clusters=3)`: model with 3 clusters
* `fit(X)`: trains the model
* `predict(X)`: assigns each point to a cluster
* `cluster_centers_`: gives coordinates of cluster centers
* `plt.scatter`: visualizes clusters and centroids

---

## **10. Elbow Method for Optimal `k`**

```python
inertias = []
for k in range(1, 10):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertias.append(model.inertia_)

plt.plot(range(1, 10), inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
plt.show()
```

* Plot `k` vs inertia
* Look for the **"elbow"** point where inertia stops decreasing significantly

---

## **11. Mathematical Formulation**

Given:

* Dataset $X = \{x_1, x_2, \ldots, x_n\}$
* Cluster centroids $\mu_1, \mu_2, \ldots, \mu_k$

Objective:

$$
\min \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2
$$

---

## **12. Conclusion**

K-Means is a foundational and effective clustering method for exploratory data analysis. It is computationally efficient but needs careful preprocessing and parameter selection (like `k`) for optimal results.

### **Agglomerative and DBSCAN Clustering Algorithms (Unit 3 – Unsupervised Learning)**

---

## **A. Agglomerative Clustering**

---

### **1. Definition**

Agglomerative clustering is a **hierarchical bottom-up clustering** algorithm where:

* Each data point starts in its **own cluster**
* Pairs of clusters are **merged** iteratively based on their **distance**

---

### **2. Algorithm Steps**

1. Start with `n` clusters (each data point is its own cluster)
2. Compute the **distance matrix** between all clusters
3. Merge the **closest pair** of clusters
4. Recalculate the distance matrix
5. Repeat steps 3–4 until only **one cluster** remains or a **stopping condition** is met

---

### **3. Linkage Criteria (Distance between clusters)**

| Type                 | Definition                                                    |
| -------------------- | ------------------------------------------------------------- |
| **Single linkage**   | Minimum distance between any 2 points from different clusters |
| **Complete linkage** | Maximum distance between any 2 points from different clusters |
| **Average linkage**  | Average of all pairwise distances between clusters            |
| **Ward’s method**    | Minimize increase in total intra-cluster variance             |

---

### **4. Advantages**

* Produces **dendrograms** (tree structures)
* No need to pre-define number of clusters (optional)
* Works with various distance metrics

---

### **5. Disadvantages**

* **Computationally expensive**: $O(n^3)$
* Sensitive to **noisy data and outliers**
* Not suitable for **very large** datasets

---

### **6. Python Example**

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate sample data
X, _ = make_blobs(n_samples=100, centers=3, random_state=42)

# Agglomerative clustering
model = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = model.fit_predict(X)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.title("Agglomerative Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()

# Optional dendrogram
linked = linkage(X, 'ward')
plt.figure(figsize=(10, 5))
dendrogram(linked, truncate_mode='lastp', p=10)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Cluster Index")
plt.ylabel("Distance")
plt.show()
```

---

## **B. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

---

### **1. Definition**

DBSCAN is a **density-based clustering** algorithm:

* Groups together **points with many nearby neighbors**
* Marks points in **low-density** regions as **outliers**

---

### **2. Core Concepts**

| Concept          | Definition                                      |
| ---------------- | ----------------------------------------------- |
| **ε (epsilon)**  | Neighborhood radius                             |
| **MinPts**       | Minimum number of points to form a dense region |
| **Core Point**   | Has at least MinPts in its ε-neighborhood       |
| **Border Point** | Not a core, but within ε of a core point        |
| **Noise Point**  | Neither core nor border                         |

---

### **3. Algorithm Steps**

1. For each point, check ε-neighborhood
2. If ≥ MinPts → mark as **core point**
3. Group all reachable core and border points into a cluster
4. Mark all unclustered points as **noise**

---

### **4. Advantages**

* Can find **arbitrarily shaped** clusters
* Automatically detects **outliers**
* No need to specify number of clusters

---

### **5. Disadvantages**

* Struggles when **densities vary**
* Choosing appropriate `ε` and `MinPts` is critical

---

### **6. Python Example**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Create sample data
X, _ = make_moons(n_samples=300, noise=0.05, random_state=0)

# DBSCAN
model = DBSCAN(eps=0.2, min_samples=5)
labels = model.fit_predict(X)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
```

---

### **7. Key Differences (Agglomerative vs. DBSCAN)**

| Feature            | Agglomerative              | DBSCAN             |
| ------------------ | -------------------------- | ------------------ |
| Type               | Hierarchical               | Density-based      |
| Cluster Shape      | Spherical or chain-like    | Arbitrary          |
| Outlier Detection  | No                         | Yes                |
| Predefine Clusters | Optional                   | No need            |
| Runtime Complexity | High (slow for large data) | Fast with indexing |

---

### **8. Applications**

* **Agglomerative**: Gene analysis, taxonomy, social network hierarchy
* **DBSCAN**: Geospatial data, anomaly detection, image segmentation, crime pattern analysis

---

### **9. Conclusion**

Agglomerative is useful for **hierarchical clustering**, while DBSCAN excels in **discovering non-linear shapes** and **ignoring noise**. Choice depends on **data structure** and **desired output**.


