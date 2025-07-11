# Unit - 3 -> Unsupervised learning
Introduction, tupes and challenges, preprocessing and scaling of dataset, Dimensinality reduction, feature extraction, Principal Compinet Analysis (PCA), k-means, Agglomerative and DBSCAN clustering algorithms.

## Content ->
### **Unsupervised Learning – Introduction**

---

#### 1. **Definition**

* **Unsupervised Learning** is a type of machine learning where:

  * **No labeled data** is provided.
  * The algorithm tries to **discover patterns**, **structures**, or **relationships** in the data on its own.
  * Output variables (i.e., target values) are **not known**.

---

#### 2. **Goal**

* To **group, cluster, compress, or describe** data without pre-defined labels.
* Find **hidden structures**, **density patterns**, or **data distributions** in unlabeled datasets.

---

#### 3. **Key Differences from Supervised Learning**

| Aspect          | Supervised Learning               | Unsupervised Learning            |
| --------------- | --------------------------------- | -------------------------------- |
| Labeled data    | Required                          | Not required                     |
| Output variable | Known (classification/regression) | Not known (clustering, patterns) |
| Example task    | Spam detection                    | Customer segmentation            |
| Objective       | Predict outcome                   | Discover structure               |

---

#### 4. **Typical Applications**

* **Clustering**:

  * Grouping similar items together
* **Dimensionality Reduction**:

  * Compressing data while retaining meaningful variation
* **Anomaly Detection**:

  * Finding rare or unusual patterns
* **Association Rule Mining**:

  * Market basket analysis (e.g., “people who bought X also bought Y”)
* **Feature Learning / Extraction**:

  * Discovering new informative representations of data

---

#### 5. **Examples of Unsupervised Learning Tasks**

| Task                     | Example                                 |
| ------------------------ | --------------------------------------- |
| Customer segmentation    | Grouping users based on buying behavior |
| Document clustering      | Grouping similar news articles          |
| Image compression        | Reducing image size without labels      |
| Gene expression analysis | Finding co-expressed gene clusters      |

---

#### 6. **Common Unsupervised Learning Techniques**

| Technique                                   | Purpose                                |
| ------------------------------------------- | -------------------------------------- |
| **K-Means**                                 | Partition data into clusters           |
| **Hierarchical Clustering (Agglomerative)** | Build nested clusters                  |
| **DBSCAN**                                  | Density-based clustering               |
| **PCA**                                     | Dimensionality reduction               |
| **t-SNE / UMAP**                            | Visualization of high-dimensional data |

---

#### 7. **Nature of Output**

* Outputs are not labels but **group assignments**, **embeddings**, or **clusters**.
* Often require **human interpretation** to label or understand the discovered groups.

---
### **Types of Unsupervised Learning**

---

Unsupervised learning algorithms can be broadly classified based on **what they aim to do** with the data. The main types include:

---

### **1. Clustering**

* **Definition**: Grouping similar data points into clusters based on similarity or distance.
* **Goal**: Points in the same cluster are more similar to each other than to those in other clusters.

#### Examples:

* **K-Means Clustering**
* **Hierarchical Clustering (Agglomerative/Divisive)**
* **DBSCAN (Density-Based Spatial Clustering)**

#### Applications:

* Customer segmentation
* Document categorization
* Social network analysis

---

### **2. Dimensionality Reduction**

* **Definition**: Reducing the number of variables/features in a dataset while preserving the structure or important information.
* **Goal**: Simplify data, remove noise, improve visualization and speed up training.

#### Examples:

* **PCA (Principal Component Analysis)**
* **t-SNE (t-distributed Stochastic Neighbor Embedding)**
* **UMAP (Uniform Manifold Approximation and Projection)**

#### Applications:

* Visualization of high-dimensional data
* Feature compression
* Noise reduction

---

### **3. Association Rule Learning**

* **Definition**: Discovering **interesting relationships** or **co-occurrences** among variables in large datasets.
* **Goal**: Identify rules like "If A happens, B is likely to happen."

#### Examples:

* **Apriori Algorithm**
* **ECLAT Algorithm**

#### Applications:

* Market basket analysis (e.g., Amazon or supermarket recommendation systems)
* Medical diagnosis rules
* Web usage mining

---

### **4. Anomaly Detection (Outlier Detection)**

* **Definition**: Identifying **rare**, **unusual**, or **abnormal data points** that deviate from the majority.
* **Goal**: Detect frauds, faults, or any kind of irregular behavior.

#### Examples:

* Statistical methods (e.g., Z-score, IQR)
* Clustering-based outlier detection
* Autoencoders (unsupervised deep learning)

#### Applications:

* Fraud detection in finance
* Network intrusion detection
* Medical diagnosis (e.g., tumor detection)

---

### **5. Generative Models**

* **Definition**: Learn the **underlying distribution** of the data and can generate **new, similar data**.
* **Goal**: Generate realistic synthetic data.

#### Examples:

* **Autoencoders**
* **GANs (Generative Adversarial Networks)**
* **Restricted Boltzmann Machines**

#### Applications:

* Image synthesis
* Text generation
* Data augmentation

---

### **Challenges in Unsupervised Learning**

---

#### 1. **Lack of Ground Truth**

* **No labeled data** makes it hard to **evaluate performance**.
* Unlike supervised learning, we can’t directly compare predictions to known outputs.

---

#### 2. **Choosing the Right Algorithm**

* Many unsupervised algorithms exist (e.g., k-means, DBSCAN, PCA), but:

  * **No universal best** algorithm
  * The effectiveness of an algorithm depends heavily on **data structure**, **scale**, and **distribution**

---

#### 3. **Determining the Number of Clusters or Components**

* Most clustering algorithms (e.g., k-means) require the number of clusters as input.
* **No prior knowledge** of how many groups/classes exist.
* Techniques like **Elbow Method**, **Silhouette Score** help but are not always definitive.

---

#### 4. **High Dimensionality**

* Real-world data often has **many features** (dimensions), making it:

  * Hard to visualize
  * Prone to **noise** and **irrelevant features**
* Known as the **curse of dimensionality**.

---

#### 5. **Interpretability of Results**

* Clusters or components may not correspond to meaningful categories.
* It’s hard to **explain** what a discovered cluster actually represents without labels.

---

#### 6. **Scalability and Computational Cost**

* Some methods (e.g., hierarchical clustering) are **computationally expensive**.
* Difficult to scale to **very large datasets** without optimization.

---

#### 7. **Sensitivity to Parameters and Initialization**

* Results can vary based on:

  * **Initial centroid positions** (in k-means)
  * **Epsilon and MinPts** in DBSCAN
* **Random initialization** can lead to inconsistent clustering.

---

#### 8. **Handling Noise and Outliers**

* Algorithms like k-means are sensitive to **outliers**, which can distort the cluster centroids.
* Need robust methods like **DBSCAN** or **median-based** clustering.

---

#### 9. **Cluster Shape Assumptions**

* Some algorithms assume specific cluster shapes (e.g., spherical in k-means).
* Fails when data has **arbitrary or non-convex** shapes.

---

#### 10. **Data Preprocessing Dependency**

* Unsupervised methods heavily rely on:

  * **Feature scaling**
  * **Normalization**
  * **Missing value handling**
* Poor preprocessing leads to **poor quality results**.

---

#### 11. **Validation Difficulty**

* Cannot directly compute accuracy, precision, recall.
* Need to use **internal validation metrics** like:

  * **Silhouette Score**
  * **Calinski-Harabasz Index**
  * **Davies–Bouldin Index**

---
### **Preprocessing in Unsupervised Learning**

---

#### 1. **Definition**

* **Preprocessing** is the process of **cleaning and transforming raw data** into a suitable format for unsupervised learning algorithms.
* Essential because most unsupervised algorithms are **sensitive to the scale, distribution, and structure** of the input data.

---

#### 2. **Goals of Preprocessing**

* Improve **algorithm performance** and **convergence**
* Reduce **noise**, **bias**, and **inconsistencies**
* Make data **comparable**, especially when using distance-based methods (e.g., k-means)

---

#### 3. **Key Preprocessing Steps**

---

### **A. Handling Missing Data**

* Missing values must be dealt with before applying any unsupervised algorithm.

| Technique          | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Remove Rows**    | Drop rows with missing entries                                            |
| **Imputation**     | Fill missing values with mean, median, mode, or using model-based methods |
| **KNN Imputation** | Use neighbors to estimate missing data                                    |

---

### **B. Handling Categorical Data**

* Algorithms like k-means or PCA require numerical input.

| Method                 | Description                               |
| ---------------------- | ----------------------------------------- |
| **One-Hot Encoding**   | Convert each category into binary vectors |
| **Label Encoding**     | Assign integer values to categories       |
| **Frequency Encoding** | Replace category with its frequency       |

---

### **C. Feature Scaling**

* Ensures all features contribute **equally** to distance metrics.

| Method              | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| **Standardization** | Convert features to have **mean = 0** and **std = 1** (Z-score) |
| **Normalization**   | Scale features to a **fixed range** (e.g., \[0, 1])             |
| **Max Abs Scaling** | Scale using maximum absolute value (for sparse data)            |

---

### **D. Removing Outliers**

* Outliers can distort results of distance-based clustering.

| Method                | Description                        |   |     |
| --------------------- | ---------------------------------- | - | --- |
| **Z-Score**           | Remove points with                 | z | > 3 |
| **IQR Method**        | Use interquartile range thresholds |   |     |
| **Isolation Forests** | Learn-based anomaly filtering      |   |     |

---

### **E. Feature Selection / Extraction**

* Reduce irrelevant or redundant features.

| Method                    | Description                         |
| ------------------------- | ----------------------------------- |
| **Variance Threshold**    | Remove low-variance features        |
| **Correlation Filtering** | Remove highly correlated features   |
| **Autoencoders**          | Learn compact, informative features |

---

### **F. Dimensionality Reduction (Optional Pre-step)**

* Helps visualize and speed up training.

| Method    | Description                             |
| --------- | --------------------------------------- |
| **PCA**   | Projects data to fewer dimensions       |
| **t-SNE** | Non-linear projection for visualization |
| **UMAP**  | Preserves global and local structures   |

---

### **G. Noise Reduction**

* Removes random variation in the dataset.

| Method                | Description                              |
| --------------------- | ---------------------------------------- |
| **Smoothing filters** | Apply for image/temporal data            |
| **Autoencoders**      | Use denoising versions to clean features |

---

#### 4. **Why Preprocessing is Critical in Unsupervised Learning**

* No labels to guide the learning, so **data quality directly impacts results**.
* Many unsupervised algorithms use **Euclidean distance** or **cosine similarity**, which are highly sensitive to:

  * Feature scale
  * Outliers
  * Noise

---

#### 5. **Order of Preprocessing (Typical Flow)**

1. Handle missing data
2. Convert categorical data
3. Normalize or standardize features
4. Remove outliers
5. Feature selection or dimensionality reduction (if needed)

---

### **Scaling of Dataset in Unsupervised Learning**

---

#### 1. **Definition**

* **Scaling** is the process of transforming feature values so that they are on the **same scale or range**.
* It ensures that **no single feature dominates** others due to larger numeric values.

---

#### 2. **Why Scaling is Important**

* Many unsupervised algorithms (especially clustering) rely on **distance metrics** (e.g., Euclidean distance).
* Features with larger values can **bias** the results and lead to incorrect clustering or projection.
* Without scaling:

  * **K-means** may group based on dominant features only.
  * **PCA** might be skewed by high-magnitude features.

---

#### 3. **When to Use Scaling**

* **Always required** for:

  * K-means clustering
  * DBSCAN
  * PCA
  * Hierarchical clustering (with distance metrics)
* **Not always required** for:

  * Tree-based models (not distance-based)

---

#### 4. **Common Scaling Techniques**

---

### **A. Min-Max Normalization (Rescaling)**

* Scales values to a fixed range, usually **\[0, 1]**.

$$
X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
$$

* **Preserves shape**, but not outlier resistant.

#### Used in:

* Image data
* Algorithms requiring **bounded input**

---

### **B. Standardization (Z-score Normalization)**

* Transforms data to have:

  * **Mean = 0**
  * **Standard Deviation = 1**

$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
$$

* **Removes mean** and scales by variance.
* Better when data follows a **Gaussian distribution**.

#### Used in:

* PCA
* K-means
* DBSCAN

---

### **C. Max-Abs Scaling**

* Scales each feature by its **maximum absolute value**.

$$
X_{\text{scaled}} = \frac{X}{|X_{\max}|}
$$

* Keeps **zero-centered** sparse data unchanged.

#### Used in:

* Sparse data (e.g., text, frequency vectors)

---

### **D. Robust Scaling**

* Uses **median** and **interquartile range (IQR)**:

$$
X_{\text{scaled}} = \frac{X - \text{median}}{\text{IQR}}
$$

* **Robust to outliers**

#### Used in:

* Datasets with **extreme values**

---

#### 5. **Comparison Table**

| Technique       | Sensitive to Outliers | Output Range      | Common Uses             |
| --------------- | --------------------- | ----------------- | ----------------------- |
| Min-Max Scaling | Yes                   | \[0, 1]           | Image data, neural nets |
| Z-score         | No (moderate)         | Mean = 0, Std = 1 | PCA, K-means            |
| Max-Abs Scaling | Yes                   | \[-1, 1]          | Sparse data             |
| Robust Scaling  | No (very robust)      | Depends on IQR    | Skewed data             |

---

#### 6. **Practical Considerations**

* Always **fit the scaler on training data**, then transform both train and test/validation data.
* Scaling should be part of **preprocessing pipelines** (e.g., using `Pipeline` in Scikit-learn).
* Never apply **scaling after** applying algorithms — it must be done **before** model fitting.

---
### **Dimensionality Reduction**

---

#### 1. **Definition**

* The process of **reducing the number of input variables (features)** in a dataset while retaining as much important information as possible.
* Helps simplify data, reduce noise, improve computational efficiency, and aid visualization.

---

#### 2. **Why Dimensionality Reduction is Important**

* High-dimensional data often suffers from the **curse of dimensionality**, where:

  * Data becomes sparse.
  * Distances become less meaningful.
  * Models tend to overfit.
* Reducing dimensions helps to:

  * Improve **model performance**.
  * Make data **easier to visualize**.
  * Speed up **training and inference**.

---

#### 3. **Types of Dimensionality Reduction**

---

### **A. Feature Selection**

* Select a **subset of original features** based on criteria like variance or importance.
* Examples:

  * Removing low-variance features.
  * Selecting features based on correlation or importance scores.

---

### **B. Feature Extraction**

* Create **new features** by transforming the original features.
* New features are usually a combination or projection of the original features.

---

#### 4. **Popular Dimensionality Reduction Techniques**

| Technique                              | Type              | Description                                                 |
| -------------------------------------- | ----------------- | ----------------------------------------------------------- |
| **Principal Component Analysis (PCA)** | Linear Projection | Projects data to directions maximizing variance             |
| **Linear Discriminant Analysis (LDA)** | Supervised Linear | Maximizes class separability (supervised)                   |
| **t-SNE**                              | Non-linear        | Visualizes high-dimensional data preserving local structure |
| **UMAP**                               | Non-linear        | Faster and preserves global structure better than t-SNE     |
| **Autoencoders**                       | Neural Network    | Learn compressed representations in an unsupervised manner  |

---

#### 5. **Principal Component Analysis (PCA) (Most Common)**

* Finds **orthogonal directions (principal components)** that capture maximum variance.
* Projects data onto fewer principal components with minimal loss of information.
* Reduces dimensions while **maximizing variance retained**.
* Commonly used as a **preprocessing step** before clustering or visualization.

---

#### 6. **Benefits**

* Removes **noise** and **redundant features**.
* Facilitates **data visualization** in 2D or 3D.
* Improves **computational efficiency**.
* Helps in overcoming the **curse of dimensionality**.

---

#### 7. **Challenges**

* Sometimes difficult to interpret transformed features.
* Linear methods (like PCA) cannot capture complex nonlinear structures.
* Need to choose how many components to keep (trade-off between compression and information loss).

---
### **Feature Extraction**

---

#### 1. **Definition**

* The process of **transforming raw data** into a set of **informative, non-redundant features** that can be effectively used for machine learning tasks.
* Unlike feature selection (which chooses existing features), feature extraction **creates new features** from the original data.

---

#### 2. **Purpose**

* Simplify the data by **capturing the essential information**.
* Reduce **dimensionality** while retaining key characteristics.
* Improve model performance and reduce computational cost.
* Make complex data more **interpretable** and structured.

---

#### 3. **Feature Extraction vs Feature Selection**

| Aspect                  | Feature Extraction                     | Feature Selection             |
| ----------------------- | -------------------------------------- | ----------------------------- |
| Creates new features    | Yes                                    | No                            |
| Combines input features | Often combines features                | Selects a subset of features  |
| Goal                    | Transform data into new representation | Choose most relevant features |
| Example                 | PCA, Autoencoders                      | Filter, Wrapper methods       |

---

#### 4. **Common Feature Extraction Techniques**

---

### **A. Principal Component Analysis (PCA)**

* Projects data onto new axes (principal components) that maximize variance.
* Transforms original correlated features into uncorrelated features.

---

### **B. Linear Discriminant Analysis (LDA)**

* Finds linear combinations that best separate classes (supervised).
* Useful when class labels are available.

---

### **C. Autoencoders**

* Neural networks trained to **reconstruct input** at output.
* Middle layer (bottleneck) acts as compressed feature representation.
* Can capture **nonlinear relationships** in data.

---

### **D. Wavelet Transform and Fourier Transform**

* Used especially for **signal processing** and **image data**.
* Extract frequency or time-frequency domain features.

---

### **E. Bag-of-Words (BoW) and TF-IDF (for text data)**

* Convert text documents into numerical feature vectors.
* Capture word occurrence and importance.

---

#### 5. **Steps in Feature Extraction**

1. **Input raw data** (images, text, signals, tabular data)
2. **Apply transformation or projection** to extract features
3. **Obtain new feature vectors** with reduced dimension or enhanced representation
4. **Use extracted features** as inputs for learning algorithms

---

#### 6. **Advantages**

* Can capture **complex, nonlinear structures** (with methods like autoencoders).
* Reduces data dimensionality efficiently.
* Often improves downstream **model accuracy** and **generalization**.

---

#### 7. **Limitations**

* Extracted features may be **hard to interpret**.
* Feature extraction process might be **computationally intensive**.
* Requires **careful tuning** of parameters (e.g., number of components).

---
### **Principal Component Analysis (PCA)**

---

#### 1. **Definition**

* PCA is a **linear dimensionality reduction technique** that transforms the original data into a new coordinate system.
* The new axes (called **principal components**) are orthogonal and capture the **maximum variance** in the data.
* PCA reduces the number of features while preserving the most important information.

---

#### 2. **Objectives**

* Find a set of uncorrelated variables (principal components) from correlated variables.
* Capture the **largest variance** in the data in the fewest components.
* Reduce noise and redundancy.

---

#### 3. **How PCA Works (Step-by-step)**

1. **Standardize the data**

   * Center the data by subtracting the mean and scale (usually) to unit variance.

2. **Compute the covariance matrix**

   * Measures how features vary together.

3. **Calculate eigenvalues and eigenvectors of covariance matrix**

   * Eigenvectors represent directions of principal components.
   * Eigenvalues represent the magnitude of variance along those directions.

4. **Sort eigenvectors by eigenvalues in descending order**

   * The top eigenvectors correspond to principal components with highest variance.

5. **Select top-k eigenvectors** to form a projection matrix.

6. **Project the original data onto this lower-dimensional subspace**

   * Resulting data has fewer dimensions but retains most variance.

---

#### 4. **Mathematical Formulation**

* Given data matrix $X$ of size $n \times d$ (n samples, d features):

$$
\text{Covariance matrix} \quad C = \frac{1}{n-1} X^T X
$$

* Solve:

$$
C \mathbf{v} = \lambda \mathbf{v}
$$

where $\mathbf{v}$ is an eigenvector and $\lambda$ its eigenvalue.

---

#### 5. **Principal Components**

* First PC: direction with maximum variance.
* Second PC: direction orthogonal to the first with next highest variance.
* Continues similarly for all PCs.

---

#### 6. **Choosing Number of Components**

* Based on **explained variance ratio** — cumulative sum of eigenvalues normalized.
* Choose minimum components capturing, e.g., **95%** of total variance.

---

#### 7. **Advantages**

* Reduces dimensionality with minimal information loss.
* Removes correlated features, leading to uncorrelated principal components.
* Helps visualize high-dimensional data (2D or 3D plots).
* Enhances efficiency of learning algorithms.

---

#### 8. **Limitations**

* PCA assumes **linear relationships** between variables.
* Sensitive to **scaling** — features must be normalized.
* Principal components may lack intuitive interpretation.
* Does not work well if data lies on a **nonlinear manifold**.

---

#### 9. **Applications**

* Preprocessing for clustering or classification.
* Image compression.
* Data visualization.
* Noise reduction.

---
### **k-Means Clustering**

---

#### 1. **Definition**

* A popular **unsupervised clustering algorithm** that partitions data into **k distinct, non-overlapping clusters**.
* Each data point belongs to the cluster with the nearest mean (centroid).

---

#### 2. **Goal**

* Minimize the **within-cluster sum of squares (WCSS)** or variance:

$$
\sum_{i=1}^k \sum_{x \in C_i} \|x - \mu_i\|^2
$$

where $C_i$ is the cluster $i$, and $\mu_i$ is its centroid.

---

#### 3. **Algorithm Steps**

1. **Initialize**: Choose k initial centroids randomly or using methods like k-means++.

2. **Assign Points**: Assign each data point to the nearest centroid based on distance (usually Euclidean).

3. **Update Centroids**: Calculate the new centroid of each cluster as the mean of all points assigned to it.

4. **Repeat** steps 2 and 3 until convergence:

   * No change in assignments or centroids
   * Or max iterations reached

---

#### 4. **Features**

* Partitions data into **Voronoi cells**.
* Assumes clusters are **spherical and equally sized**.
* Sensitive to **initial centroid selection**.

---

#### 5. **Initialization Techniques**

* **Random Initialization**: Pick k points randomly.
* **k-means++**: Improves initialization by spreading initial centroids.

---

#### 6. **Advantages**

* Simple and easy to implement.
* Efficient and scales well to large datasets.
* Works well when clusters are well-separated.

---

#### 7. **Limitations**

| Limitation                  | Explanation                                   |
| --------------------------- | --------------------------------------------- |
| Must specify **k**          | Number of clusters must be known a priori     |
| Sensitive to outliers       | Outliers can skew centroids                   |
| Assumes spherical clusters  | Fails for non-convex or varying size clusters |
| Sensitive to initialization | Different runs can yield different clusters   |

---

#### 8. **Applications**

* Market segmentation
* Document clustering
* Image segmentation
* Customer profiling

---

#### 9. **Extensions**

* **k-medoids**: Uses actual data points as centers, more robust to outliers.
* **Fuzzy c-means**: Assigns probabilities of belonging to clusters.
* **Mini-batch k-means**: Uses small batches for faster computation.

---
### **Agglomerative Clustering**

---

#### 1. **Definition**

* A type of **hierarchical clustering** method that builds clusters **bottom-up**.
* Starts with each data point as its own cluster and **iteratively merges** the closest pairs until one cluster or desired number of clusters remains.

---

#### 2. **Process**

1. **Initialization**: Each data point is a separate cluster.

2. **Calculate Distances**: Compute the pairwise distances between all clusters.

3. **Merge Clusters**: Merge the two clusters with the smallest distance.

4. **Update Distances**: Recalculate distances between the new cluster and all remaining clusters.

5. **Repeat** steps 3 and 4 until stopping criteria is met:

   * Only one cluster remains, or
   * Desired number of clusters is reached.

---

#### 3. **Distance Metrics**

* Common distance measures between clusters:

  * **Single linkage**: Minimum distance between points of clusters (nearest neighbor).
  * **Complete linkage**: Maximum distance between points (farthest neighbor).
  * **Average linkage**: Average distance between points.
  * **Ward’s method**: Minimize variance increase after merging.

---

#### 4. **Output**

* Results in a **dendrogram** (tree diagram showing cluster merges at different distances).
* Cut the dendrogram at a chosen height to get the desired number of clusters.

---

#### 5. **Advantages**

* Does not require pre-specifying the number of clusters.
* Captures **nested cluster structure**.
* Works with **arbitrary cluster shapes**.
* Easy to visualize with dendrograms.

---

#### 6. **Limitations**

| Limitation                        | Description                                                    |
| --------------------------------- | -------------------------------------------------------------- |
| Computationally expensive         | $O(n^3)$ in naive implementations; less for optimized versions |
| Sensitive to noise/outliers       | Outliers can cause incorrect merges                            |
| Choice of linkage affects results | Different linkage methods yield different clusters             |
| No objective function to optimize | May lead to unstable clusters                                  |

---

#### 7. **Applications**

* Gene expression analysis
* Document clustering
* Image segmentation
* Social network analysis

---

### **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

---

#### 1. **Definition**

* DBSCAN is a **density-based clustering algorithm** that forms clusters based on the **density of data points**.
* It can find clusters of **arbitrary shapes** and is **robust to noise and outliers**.

---

#### 2. **Key Concepts**

| Term             | Meaning                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| **ε (epsilon)**  | Radius that defines the neighborhood around a point                          |
| **MinPts**       | Minimum number of points required in ε-neighborhood to form a cluster        |
| **Core Point**   | A point with at least MinPts points (including itself) in its ε-neighborhood |
| **Border Point** | A point that is within ε of a core point but has fewer than MinPts points    |
| **Noise Point**  | A point that is neither a core nor a border point (i.e., an outlier)         |

---

#### 3. **Algorithm Steps**

1. For each point in the dataset:

   * Count how many points are within distance **ε**.
   * If the count ≥ **MinPts**, mark it as a **core point**.

2. Group each core point with all **density-reachable points** (connected via other core points).

3. Expand clusters by recursively adding all directly density-reachable points.

4. Points not assigned to any cluster are marked as **noise**.

---

#### 4. **Important Properties**

* **Density-Reachable**: A point A is density-reachable from B if there is a path of core points from B to A.
* **Cluster shape**: Can identify **non-convex and irregular-shaped clusters**.
* **Noise handling**: Naturally identifies and excludes outliers.

---

#### 5. **Advantages**

| Advantage                             | Explanation                         |
| ------------------------------------- | ----------------------------------- |
| No need to specify number of clusters | Unlike k-means                      |
| Detects arbitrary shapes              | Works with non-convex clusters      |
| Robust to outliers                    | Automatically excludes noise points |
| Works well for uneven density         | With tuning of ε and MinPts         |

---

#### 6. **Limitations**

| Limitation                                    | Explanation                         |
| --------------------------------------------- | ----------------------------------- |
| Sensitive to **ε and MinPts**                 | Poor choice leads to bad clustering |
| Not good with **varying densities**           | One ε may not fit all clusters      |
| Performance degrades on high-dimensional data | Due to curse of dimensionality      |

---

#### 7. **Parameter Selection Guidelines**

* **ε**:

  * Use **k-distance graph** (plot distance to k-th nearest neighbor) to find elbow point.

* **MinPts**:

  * General rule: MinPts ≥ **D+1**, where **D** is the number of dimensions.
  * Typical values: **4–10**

---

#### 8. **Time Complexity**

* With spatial indexing (like KD-Tree or Ball Tree):

  $$
  O(n \log n)
  $$
* Without indexing:

  $$
  O(n^2)
  $$

---

#### 9. **Applications**

* Geospatial clustering (e.g., identifying urban areas)
* Anomaly detection (e.g., fraud, network intrusion)
* Image segmentation
* Clustering gene expression data

---

