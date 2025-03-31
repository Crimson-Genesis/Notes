# Data Structer
---

## **Unit 3: Searching, Sorting, and Graphs**  

### **1. Searching Algorithms**  
Searching is the process of finding an element in a data structure. The two main searching techniques are:  

#### **(a) Linear Search**  
- Works by checking each element in the list sequentially.  
- **Best Case:** O(1) (if the element is found at the first position)  
- **Worst Case:** O(n) (if the element is at the last position or not present)  
- **Implementation:**  

```c
// C program for Linear Search
#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;  // Return index if element found
        }
    }
    return -1;  // Return -1 if not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int key = 30;
    int n = sizeof(arr) / sizeof(arr[0]);

    int result = linearSearch(arr, n, key);
    if (result == -1)
        printf("Element not found\n");
    else
        printf("Element found at index %d\n", result);
    return 0;
}
```

---

#### **(b) Binary Search (Only for Sorted Arrays)**  
- Uses **Divide & Conquer** to find the element.  
- **Time Complexity:** O(log n)  
- **Steps:**  
  1. Find the middle element.  
  2. If it matches the key, return index.  
  3. If the key is smaller, search in the left half.  
  4. If the key is larger, search in the right half.  
  5. Repeat until the element is found or the array is exhausted.  

- **Implementation (Iterative Binary Search):**  

```c
// C program for Binary Search
#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;

        if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int key = 30;
    int n = sizeof(arr) / sizeof(arr[0]);

    int result = binarySearch(arr, 0, n - 1, key);
    if (result == -1)
        printf("Element not found\n");
    else
        printf("Element found at index %d\n", result);
    return 0;
}
```

✅ **Key Differences Between Linear Search and Binary Search:**  

| **Criteria**      | **Linear Search**  | **Binary Search**  |
|------------------|------------------|------------------|
| **Works on**     | Any array        | Sorted array only |
| **Time Complexity** | O(n) | O(log n) |
| **Best Case** | O(1) | O(1) (when middle element is the key) |
| **Worst Case** | O(n) | O(log n) |

---
## **Sorting Algorithms**  

Sorting is the process of arranging data in ascending or descending order. Various sorting techniques are used based on time complexity, stability, and memory usage.  

---

### **1. Bubble Sort**  
- **Concept:** Repeatedly swaps adjacent elements if they are in the wrong order.  
- **Time Complexity:**  
  - Best Case (Already Sorted): O(n)  
  - Worst Case (Reversed Order): O(n²)  
- **Stable?** ✅ Yes (Does not change the relative order of equal elements)  

**Implementation:**  
```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {  // Swap if elements are in wrong order
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    bubbleSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
```
✅ **Key Takeaways:**  
- Simple but inefficient for large datasets.  
- Optimized versions check if swaps were made in an iteration.  

---

### **2. Selection Sort**  
- **Concept:** Finds the smallest element and places it in the correct position.  
- **Time Complexity:** O(n²) for all cases.  
- **Stable?** ❌ No (Swaps can change the relative order of equal elements).  

**Implementation:**  
```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    selectionSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
```
✅ **Key Takeaways:**  
- Fewer swaps than Bubble Sort but still O(n²).  
- Works well for small arrays.  

---

### **3. Insertion Sort**  
- **Concept:** Picks elements one by one and places them in the correct position.  
- **Time Complexity:**  
  - Best Case: O(n) (Already Sorted)  
  - Worst Case: O(n²) (Reversed Order)  
- **Stable?** ✅ Yes  

**Implementation:**  
```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
```
✅ **Key Takeaways:**  
- Efficient for small datasets or nearly sorted arrays.  
- Works well in situations where new elements are inserted frequently.  

---

### **4. Quick Sort (Efficient Sorting Algorithm)**  
- **Concept:** Uses Divide & Conquer to sort elements around a pivot.  
- **Time Complexity:**  
  - Best & Average Case: O(n log n)  
  - Worst Case: O(n²) (When pivot is always the smallest/largest element)  
- **Stable?** ❌ No  

**Implementation:**  
```c
#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Pivot element
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    quickSort(arr, 0, n - 1);
    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
```
✅ **Key Takeaways:**  
- Works well for large datasets.  
- **Use randomized pivot selection** to avoid worst-case O(n²).  

---

### **5. Merge Sort (Stable & Efficient Sorting Algorithm)**  
- **Concept:** Uses Divide & Conquer to divide the array into halves, sorts them, and merges them.  
- **Time Complexity:** O(n log n) in all cases.  
- **Stable?** ✅ Yes  

**Implementation:**  
```c
#include <stdio.h>

void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    i = 0; j = 0; k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);
    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}
```
✅ **Key Takeaways:**  
- **More memory usage (O(n))** than Quick Sort but stable.  
- Used in **external sorting (e.g., sorting large files on disk).**  

---

## **Graphs and Graph Algorithms**  

Graphs are non-linear data structures consisting of **nodes (vertices)** and **edges (connections between vertices)**. They can be **directed or undirected**, **weighted or unweighted**, and **cyclic or acyclic**.  

---

### **1. Graph Representation**  
Graphs can be represented in two ways:  

#### **(a) Adjacency Matrix (2D Array Representation)**  
- Uses a **2D array** where `graph[i][j] = 1` if there is an edge between `i` and `j`, otherwise `0`.  
- **Space Complexity:** O(V²) (not efficient for sparse graphs).  
- **Example:**  

```
0 -- 1 -- 2
|    |
3    4
```
**Adjacency Matrix:**  
```
  0 1 2 3 4
0 0 1 0 1 0
1 1 0 1 0 1
2 0 1 0 0 0
3 1 0 0 0 0
4 0 1 0 0 0
```

**Implementation in C:**  
```c
#include <stdio.h>
#define V 5  // Number of vertices

void printGraph(int graph[V][V]) {
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++)
            printf("%d ", graph[i][j]);
        printf("\n");
    }
}

int main() {
    int graph[V][V] = { {0, 1, 0, 1, 0},
                        {1, 0, 1, 0, 1},
                        {0, 1, 0, 0, 0},
                        {1, 0, 0, 0, 0},
                        {0, 1, 0, 0, 0} };
    
    printGraph(graph);
    return 0;
}
```
✅ **Pros:** Easy to implement, fast lookup.  
❌ **Cons:** Uses more space for sparse graphs.  

---

#### **(b) Adjacency List (Linked List Representation)**  
- Uses an **array of linked lists**, where each index stores a list of neighbors.  
- **Space Complexity:** O(V + E) (efficient for sparse graphs).  

**Example:**  

```
Adjacency List Representation:
0 → 1 → 3  
1 → 0 → 2 → 4  
2 → 1  
3 → 0  
4 → 1
```

**Implementation in C:**  
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int dest;
    struct Node* next;
} Node;

typedef struct Graph {
    int V;
    Node** adjList;
} Graph;

Graph* createGraph(int V) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->V = V;
    graph->adjList = (Node**)malloc(V * sizeof(Node*));
    for (int i = 0; i < V; i++)
        graph->adjList[i] = NULL;
    return graph;
}

void addEdge(Graph* graph, int src, int dest) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->dest = dest;
    newNode->next = graph->adjList[src];
    graph->adjList[src] = newNode;
}

void printGraph(Graph* graph) {
    for (int i = 0; i < graph->V; i++) {
        Node* temp = graph->adjList[i];
        printf("%d -> ", i);
        while (temp) {
            printf("%d ", temp->dest);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    Graph* graph = createGraph(5);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 3);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 4);

    printGraph(graph);
    return 0;
}
```
✅ **Pros:** Uses less space for sparse graphs.  
❌ **Cons:** Takes longer to find a specific edge.  

---

### **2. Graph Traversal Algorithms**  

Graph traversal is visiting all nodes in a graph systematically.

#### **(a) Depth First Search (DFS)**
- **Uses recursion (or stack)**
- Explores a branch fully before backtracking.
- **Time Complexity:** O(V + E)  

**Example:**  
```
Graph:
    0
   / \
  1   2
 / \
3   4
```
DFS Order: **0 → 1 → 3 → 4 → 2**  

**Implementation in C:**  
```c
#include <stdio.h>
#include <stdlib.h>

void DFS(int graph[][5], int v, int visited[], int V) {
    visited[v] = 1;
    printf("%d ", v);

    for (int i = 0; i < V; i++)
        if (graph[v][i] && !visited[i])
            DFS(graph, i, visited, V);
}

int main() {
    int graph[5][5] = { {0, 1, 1, 0, 0},
                         {1, 0, 0, 1, 1},
                         {1, 0, 0, 0, 0},
                         {0, 1, 0, 0, 0},
                         {0, 1, 0, 0, 0} };

    int visited[5] = {0};

    printf("DFS Traversal: ");
    DFS(graph, 0, visited, 5);
    return 0;
}
```
✅ **Key Takeaways:**  
- DFS is useful for **detecting cycles, topological sorting, and connected components**.  
- Can be implemented using recursion or a stack.  

---

#### **(b) Breadth First Search (BFS)**
- **Uses a queue**  
- Explores all neighbors first before moving to the next level.  
- **Time Complexity:** O(V + E)  

**Example:**  
```
Graph:
    0
   / \
  1   2
 / \
3   4
```
BFS Order: **0 → 1 → 2 → 3 → 4**  

**Implementation in C:**  
```c
#include <stdio.h>
#include <stdlib.h>

void BFS(int graph[][5], int start, int V) {
    int visited[V];
    for (int i = 0; i < V; i++)
        visited[i] = 0;

    int queue[10], front = 0, rear = 0;

    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int v = queue[front++];
        printf("%d ", v);

        for (int i = 0; i < V; i++)
            if (graph[v][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
    }
}

int main() {
    int graph[5][5] = { {0, 1, 1, 0, 0},
                         {1, 0, 0, 1, 1},
                         {1, 0, 0, 0, 0},
                         {0, 1, 0, 0, 0},
                         {0, 1, 0, 0, 0} };

    printf("BFS Traversal: ");
    BFS(graph, 0, 5);
    return 0;
}
```
✅ **Key Takeaways:**  
- BFS is useful for **shortest path (unweighted graphs), level-order traversal, and finding connected components**.  

---

## **Unit 4: Tree and Heap
### **1. Trees** 🌳  

A **tree** is a **non-linear data structure** that organizes data hierarchically. It consists of **nodes** connected by **edges**.  

#### **Basic Terminology:**
- **Root:** The topmost node of a tree.  
- **Parent & Child:** A node **above** is a parent, and a node **below** is a child.  
- **Siblings:** Nodes that share the same parent.  
- **Leaf Node:** A node with **no children**.  
- **Degree:** The number of children a node has.  
- **Depth:** The number of edges from the root to a node.  
- **Height:** The number of edges from a node to the deepest leaf.  

#### **Types of Trees:**
1. **General Tree:** Each node can have **any number of children**.  
2. **Binary Tree:** Each node can have **at most two children** (left & right).  
3. **Binary Search Tree (BST):** A **sorted binary tree**, where:  
   - Left child < Root < Right child.  
4. **AVL Tree:** A **self-balancing BST**, where the **height difference** (balance factor) between left and right subtrees is **at most 1**.  
5. **B-Trees:** Used in **databases & file systems** for efficient storage and retrieval.  
6. **Heap:** A **specialized tree** used for **priority queues**.  

---
### **2. Binary Trees** 🌳  

A **binary tree** is a **hierarchical data structure** where each node has at most **two children**:  
- **Left Child**  
- **Right Child**  

---

### **2.1 Types of Binary Trees**
1. **Full Binary Tree:** Every node has **either 0 or 2 children** (no node has only one child).  
2. **Complete Binary Tree:**  
   - All levels except possibly the last are **completely filled**.  
   - The last level is filled **from left to right**.  
3. **Perfect Binary Tree:**  
   - All internal nodes have **two children**.  
   - All leaf nodes are at the **same level**.  
4. **Skewed Binary Tree:**  
   - Nodes are **only on one side** (either left or right).  
   - **Left Skewed Tree:** All nodes have only **left children**.  
   - **Right Skewed Tree:** All nodes have only **right children**.  
5. **Degenerate Tree:** A skewed tree where every node has only **one child**, making it behave like a **linked list**.  

---
### **3. Binary Tree Traversals** 🌳  

**Tree traversal** is the process of visiting all nodes in a tree **systematically**. There are two main types:  
1. **Depth-First Search (DFS) Traversals**  
2. **Breadth-First Search (BFS) Traversal**  

---

### **3.1 Depth-First Search (DFS) Traversals**  
DFS explores as far as possible **along each branch** before backtracking.  

✅ **Types of DFS Traversals:**  
1. **Inorder (Left → Root → Right)**  
   - Used in **Binary Search Trees (BSTs)** to retrieve elements in **sorted order**.  
   - Example: If a BST has `{5, 3, 7, 2, 4, 6, 8}`, its **Inorder Traversal** will be:  
     ```
     2 → 3 → 4 → 5 → 6 → 7 → 8
     ```
   - **Algorithm:**  
     1. Traverse the **left subtree** recursively.  
     2. Visit the **root node**.  
     3. Traverse the **right subtree** recursively.  

2. **Preorder (Root → Left → Right)**  
   - Used to **copy a tree** or **generate prefix expressions**.  
   - Example: `{5, 3, 7, 2, 4, 6, 8}` → **Preorder Traversal:**  
     ```
     5 → 3 → 2 → 4 → 7 → 6 → 8
     ```
   - **Algorithm:**  
     1. Visit the **root node**.  
     2. Traverse the **left subtree** recursively.  
     3. Traverse the **right subtree** recursively.  

3. **Postorder (Left → Right → Root)**  
   - Used in **deleting a tree** (since it deletes children before the parent).  
   - Example: `{5, 3, 7, 2, 4, 6, 8}` → **Postorder Traversal:**  
     ```
     2 → 4 → 3 → 6 → 8 → 7 → 5
     ```
   - **Algorithm:**  
     1. Traverse the **left subtree** recursively.  
     2. Traverse the **right subtree** recursively.  
     3. Visit the **root node**.  

---

### **3.2 Breadth-First Search (BFS) / Level Order Traversal**
- Visits nodes **level by level**, starting from the root.  
- Uses a **queue** to store nodes temporarily.  
- **Example:** `{5, 3, 7, 2, 4, 6, 8}` → **Level Order Traversal:**  
  ```
  5 → 3 → 7 → 2 → 4 → 6 → 8
  ```
- **Algorithm:**  
  1. Enqueue the **root node**.  
  2. While the queue is not empty:  
     - Dequeue a node, visit it, and enqueue its **left** and **right children**.  

---

Here are C programs for each **Binary Tree Traversal** method:  

---

### **1️⃣ Inorder Traversal (Left → Root → Right)**
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Inorder Traversal
void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Main function
int main() {
    struct Node* root = createNode(5);
    root->left = createNode(3);
    root->right = createNode(7);
    root->left->left = createNode(2);
    root->left->right = createNode(4);
    root->right->left = createNode(6);
    root->right->right = createNode(8);

    printf("Inorder Traversal: ");
    inorder(root);
    return 0;
}
```
**Output:**  
```
Inorder Traversal: 2 3 4 5 6 7 8
```

---

### **2️⃣ Preorder Traversal (Root → Left → Right)**
```c
// Preorder Traversal (Root → Left → Right)
void preorder(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Main function remains the same
```
**Expected Output:**  
```
Preorder Traversal: 5 3 2 4 7 6 8
```

---

### **3️⃣ Postorder Traversal (Left → Right → Root)**
```c
// Postorder Traversal (Left → Right → Root)
void postorder(struct Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

// Main function remains the same
```
**Expected Output:**  
```
Postorder Traversal: 2 4 3 6 8 7 5
```

---

### **4️⃣ Level Order (BFS) Traversal using Queue**
```c
#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

// Queue structure for level order traversal
struct Queue {
    struct Node* arr[SIZE];
    int front, rear;
};

// Function to initialize the queue
void initQueue(struct Queue* q) {
    q->front = q->rear = -1;
}

// Function to check if queue is empty
int isEmpty(struct Queue* q) {
    return q->front == -1;
}

// Function to enqueue an element
void enqueue(struct Queue* *q, struct Node* node) {
    if (q->rear == SIZE - 1) return;
    if (isEmpty(q)) q->front = 0;
    q->arr[++q->rear] = node;
}

// Function to dequeue an element
struct Node* dequeue(struct Queue* *q) {
    if (isEmpty(q)) return NULL;
    struct Node* temp = q->arr[q->front];
    if (q->front == q->rear) q->front = q->rear = -1; // Reset queue
    else q->front++;
    return temp;
}

// Level Order Traversal
void levelOrder(struct Node* root) {
    struct Queue q;
    initQueue(&q);

    enqueue(&q, root);

    while (!isEmpty(&q)) {
        struct Node* temp = dequeue(&q);
        printf("%d ", temp->data);
        if (temp->left) enqueue(&q, temp->left);
        if (temp->right) enqueue(&q, temp->right);
    }
}

// Main function remains the same
```
**Expected Output:**  
```
Level Order Traversal: 5 3 7 2 4 6 8
```

---
### **Binary Search Tree (BST)**
A **Binary Search Tree (BST)** is a binary tree in which:  
1. The left subtree of a node contains only nodes with values **less than** the node’s value.  
2. The right subtree of a node contains only nodes with values **greater than** the node’s value.  
3. The left and right subtrees must also be binary search trees.  

---
## **Operations in BST**
1. **Insertion**  
2. **Searching**  
3. **Deletion**  
4. **Traversal (Inorder, Preorder, Postorder, Level Order)**  

---

## **1️⃣ Insertion in a BST**
To insert a node in a BST:
- If the tree is empty, create a new node.
- Compare the value to be inserted with the root:
  - If it's smaller, insert it in the left subtree.
  - If it's larger, insert it in the right subtree.
- Recursively call the insert function.

### **C Program for BST Insertion**
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to insert a node in BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) return createNode(data);

    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);

    return root;
}

// Inorder traversal (For checking correctness)
void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Main function
int main() {
    struct Node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);

    printf("Inorder traversal of BST: ");
    inorder(root);

    return 0;
}
```
**Output:**  
```
Inorder traversal of BST: 20 30 40 50 60 70 80
```
---

## **2️⃣ Searching in a BST**
- If the value matches the root, return the node.
- If the value is smaller, search in the left subtree.
- If the value is larger, search in the right subtree.

### **C Program for Searching in BST**
```c
// Function to search for a value in BST
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key)
        return root;

    if (key < root->data)
        return search(root->left, key);

    return search(root->right, key);
}

// In main function:
int key = 40;
if (search(root, key) != NULL)
    printf("\n%d found in BST", key);
else
    printf("\n%d not found in BST", key);
```
**Output:**  
```
40 found in BST
```
---

## **3️⃣ Deletion in a BST**
There are three cases:
1. **Node has no children** → Simply delete it.  
2. **Node has one child** → Replace it with the child.  
3. **Node has two children** → Replace it with its **inorder successor** (smallest node in the right subtree).  

### **C Program for Deletion in BST**
```c
// Function to find the minimum node in a subtree
struct Node* minValueNode(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

// Function to delete a node in BST
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) return root;

    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Case 1: Node with only one child or no child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }

        // Case 2: Node with two children, get inorder successor
        struct Node* temp = minValueNode(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

// In main function:
root = deleteNode(root, 30);
printf("\nInorder traversal after deletion: ");
inorder(root);
```
**Output (after deleting 30):**  
```
Inorder traversal after deletion: 20 40 50 60 70 80
```
---

## **4️⃣ Traversals in BST**
BST follows **same traversals** as binary trees:  
- **Inorder (L → Root → R)**
- **Preorder (Root → L → R)**
- **Postorder (L → R → Root)**
- **Level Order (BFS)**

Already covered in the previous **Binary Tree Traversals** section! ✅  

---

## **Applications of BST**
✅ **Efficient Searching (O(log n))**  
✅ **Symbol Tables & Dictionaries**  
✅ **Auto-completion & Spell Checking**  
✅ **Routing Tables in Networks**  
✅ **Database Indexing**  

---
### **AVL Trees (Self-Balancing BSTs)**
An **AVL Tree** is a **self-balancing Binary Search Tree (BST)** where:  
1. The difference between the heights of left and right subtrees **(Balance Factor)** is at most **1** for every node.  
2. If an imbalance occurs after insertion or deletion, **rotations** are performed to restore balance.  

---
## **1️⃣ Balance Factor in AVL Trees**
The **Balance Factor (BF)** of a node is:  
\[
BF = \text{Height of Left Subtree} - \text{Height of Right Subtree}
\]
- **BF = -1, 0, 1** → Tree is balanced ✅  
- **BF < -1 or BF > 1** → Tree is unbalanced ❌  

---
## **2️⃣ Rotations in AVL Tree**
To fix imbalances, **four types of rotations** are used:

### **(i) Right Rotation (Single Rotation) – LL Case**  
Occurs when a node is inserted into the **left subtree of the left child**.  
🔹 **Fix:** Perform a **Right Rotation (RR)**.

### **(ii) Left Rotation (Single Rotation) – RR Case**  
Occurs when a node is inserted into the **right subtree of the right child**.  
🔹 **Fix:** Perform a **Left Rotation (LL)**.

### **(iii) Left-Right Rotation (Double Rotation) – LR Case**  
Occurs when a node is inserted into the **right subtree of the left child**.  
🔹 **Fix:** Perform **Left Rotation on child → Right Rotation on parent**.

### **(iv) Right-Left Rotation (Double Rotation) – RL Case**  
Occurs when a node is inserted into the **left subtree of the right child**.  
🔹 **Fix:** Perform **Right Rotation on child → Left Rotation on parent**.

---
## **3️⃣ Insertion in an AVL Tree**
Insertion follows the normal **BST insertion** rules.  
After insertion, check the **balance factor** and perform the required **rotations**.

### **C Program for AVL Tree Insertion**
```c
#include <stdio.h>
#include <stdlib.h>

// Structure of AVL Tree Node
struct Node {
    int key;
    struct Node *left, *right;
    int height;
};

// Function to get the height of a node
int height(struct Node *N) {
    if (N == NULL)
        return 0;
    return N->height;
}

// Function to get balance factor of a node
int getBalance(struct Node *N) {
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}

// Function to create a new node
struct Node* createNode(int key) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->key = key;
    node->left = node->right = NULL;
    node->height = 1; // New node is initially a leaf
    return node;
}

// Right Rotate
struct Node* rightRotate(struct Node* y) {
    struct Node* x = y->left;
    struct Node* T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));
    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));

    return x;
}

// Left Rotate
struct Node* leftRotate(struct Node* x) {
    struct Node* y = x->right;
    struct Node* T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights
    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));
    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));

    return y;
}

// Insert function for AVL Tree
struct Node* insert(struct Node* node, int key) {
    if (node == NULL)
        return createNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else
        return node; // Duplicates not allowed

    // Update height
    node->height = 1 + (height(node->left) > height(node->right) ? height(node->left) : height(node->right));

    // Get balance factor
    int balance = getBalance(node);

    // LL Case
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    // RR Case
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    // LR Case
    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // RL Case
    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

// Inorder Traversal
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

// Main function
int main() {
    struct Node* root = NULL;

    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 10);
    root = insert(root, 25);
    root = insert(root, 35);
    root = insert(root, 50);

    printf("Inorder Traversal of AVL Tree: ");
    inorder(root);

    return 0;
}
```
**Output:**
```
Inorder Traversal of AVL Tree: 10 20 25 30 35 40 50
```

---
## **4️⃣ Deletion in an AVL Tree**
- **Delete node as in BST.**  
- **After deletion, check balance factor and perform rotations** if needed.  

---
## **5️⃣ Applications of AVL Trees**
✅ **Database Indexing (Balanced Search Trees)**  
✅ **File System Organization (NTFS in Windows)**  
✅ **Memory Management (Heap & Priority Queues)**  
✅ **Network Routing Algorithms**  

---
### **B-Trees (Balanced Search Trees for Disk-Based Storage)**  

A **B-Tree** is a **self-balancing search tree** designed for **disk storage and databases** where large amounts of data need efficient searching, insertion, and deletion.

---

## **1️⃣ Properties of B-Trees**
1. **Balanced Structure**: All leaf nodes are at the same level.  
2. **M-Way Tree**: A B-Tree of order **m** has:
   - **Each node can have at most `m` children**.
   - **Each node can store at most `m-1` keys**.
   - **Minimum children per node (except root) = ceil(m/2)**.  
3. **Efficient Disk Access**: Unlike Binary Search Trees (BST), B-Trees minimize disk reads/writes.  

### **Example: B-Tree of Order 3 (B-Tree of degree 2)**
```
         [10]    
        /    \  
   [2, 5]    [15, 20]  
```
- Each node **can have at most 3 children** (order `m=3`).
- Each node **stores at most 2 keys** (`m-1 = 3-1 = 2`).

---

## **2️⃣ Operations on B-Trees**
### **Insertion in B-Trees**
Insertion follows these steps:
1. Insert the key into the correct position in a **leaf node**.
2. If the node overflows (**more than `m-1` keys**), split it into two nodes:
   - **Median key moves up** to the parent.
   - **Left half and right half remain as new child nodes**.
3. If the parent also overflows, **repeat the process recursively** until the tree is balanced.

#### **Example: Inserting into a B-Tree of Order 3**
**Insert Keys:** `10, 20, 5, 6, 12, 30, 7, 17`
```
Step 1: Insert 10, 20
[10 20]

Step 2: Insert 5, 6 → No split needed
[5 6 10 20]

Step 3: Insert 12 → Node Overflows (Split it)
      [10]
     /    \
[5 6]   [12 20]

Step 4: Insert 30, 7, 17 → Split again
        [10 17]
      /    |     \
[5 6 7] [12] [20 30]
```

### **Deletion in B-Trees**
Deletion works as follows:
1. **If the key is in a leaf node**, remove it.
2. **If the key is in an internal node**:
   - Replace it with the **largest key from the left subtree** OR the **smallest key from the right subtree**.
   - Delete that key from the corresponding leaf.
3. **If a node has fewer than `ceil(m/2)` keys**, merge or borrow keys from siblings.

#### **Example: Deleting from B-Tree**
Given:
```
      [10 17]
     /   |   \
[5 6] [12] [20 30]
```
Delete `12`:
```
      [10 17]
     /       \
[5 6]       [20 30]
```

---
## **3️⃣ Complexity of B-Trees**
| Operation  | Time Complexity |
|------------|----------------|
| Search     | **O(log n)**   |
| Insert     | **O(log n)**   |
| Delete     | **O(log n)**   |

Unlike BSTs, **B-Trees remain balanced**, ensuring worst-case performance is **logarithmic**.

---
## **4️⃣ Applications of B-Trees**
✅ **Database Systems (Indexing & Storage)**  
✅ **File Systems (NTFS, Ext4, HFS+ use B-Trees)**  
✅ **Search Engines (Google uses B-Trees for indexing data)**  
✅ **Operating Systems (Virtual Memory Page Tables)**  

---
### **Red-Black Trees (Self-Balancing Binary Search Trees)**  

A **Red-Black Tree (RBT)** is a **self-balancing binary search tree** where each node is colored **red** or **black** to maintain balance. This ensures that search, insert, and delete operations run in **O(log n)** time.

---

## **1️⃣ Properties of Red-Black Trees**
1. **Every node is either RED or BLACK.**  
2. **The root is always BLACK.**  
3. **No two consecutive RED nodes can appear (no RED-RED violation).**  
4. **Every path from the root to a leaf has the same number of BLACK nodes (called the Black-Height Property).**  
5. **Newly inserted nodes are always RED (to maintain balance easily).**

---

## **2️⃣ Structure of a Red-Black Tree**
Example of a **balanced Red-Black Tree**:
```
         (20, BLACK)
        /          \
  (15, RED)     (30, BLACK)
    /     \        /      \
(10, BLACK) (17, BLACK) (25, RED) (40, RED)
```

- **Black Height**: Every root-to-leaf path has the **same number of black nodes**.
- **Red-Red Violation Avoided**: No two consecutive red nodes exist.

---

## **3️⃣ Operations on Red-Black Trees**
### **Insertion**
1. Insert the node as in a **Binary Search Tree (BST)**.
2. If the inserted node causes a **Red-Red violation**, perform **fixing using rotations and recoloring**.
3. Fixing is done using **Rotations (Left/Right) and Recoloring**.

#### **Example: Inserting into a Red-Black Tree**
**Inserting 20, 15, 30, 10, 17**
```
Step 1: Insert 20 (Root must be BLACK)
         (20, BLACK)

Step 2: Insert 15 (RED, no violation)
         (20, BLACK)
        /
   (15, RED)

Step 3: Insert 30 (RED, no violation)
         (20, BLACK)
        /          \
  (15, RED)    (30, RED)

Step 4: Insert 10 → Red-Red Violation (Fix needed)
        (20, BLACK)
       /          \
 (15, BLACK)    (30, RED)
   /
(10, RED)  ✅ FIXED by recoloring
```

### **Rotations Used for Fixing**
- **Left Rotation (LL Case)**  
- **Right Rotation (RR Case)**  
- **Left-Right Rotation (LR Case)**  
- **Right-Left Rotation (RL Case)**  

---

### **Deletion**
1. **Delete as in BST.**  
2. **Fix any violations using rotations and recoloring.**  
3. **If a black node is deleted, it reduces the black height → Must be balanced using fixes.**  

#### **Example: Deleting from a Red-Black Tree**
Given:
```
         (20, BLACK)
        /          \
  (15, BLACK)    (30, BLACK)
    /
(10, RED)
```
**Delete 10** → No fix needed.

If deleting **a black node**:
- **Case 1: If it has a red child → Replace it with the red child.**  
- **Case 2: If it has only black children → Fix using rotations & recoloring.**  

---

## **4️⃣ Complexity of Red-Black Trees**
| Operation  | Time Complexity |
|------------|----------------|
| Search     | **O(log n)**   |
| Insert     | **O(log n)**   |
| Delete     | **O(log n)**   |

Red-Black Trees guarantee **balanced height**, unlike normal BSTs.

---

## **5️⃣ Applications of Red-Black Trees**
✅ **Linux Process Scheduler (Completely Fair Scheduler - CFS)**  
✅ **Memory Allocation (Used in malloc/free implementations)**  
✅ **Java TreeMap & C++ STL (std::map, std::set use Red-Black Trees)**  
✅ **File Systems (NTFS, Ext3, Ext4 use Red-Black Trees for indexing)**  

---
### **Threaded Binary Trees**  

A **Threaded Binary Tree (TBT)** is a special type of binary tree where **null pointers are replaced with threads**. These threads help in efficient **inorder, preorder, and postorder traversals** without using recursion or stacks.  

---

## **1️⃣ Why Use Threaded Binary Trees?**
🔹 In a normal Binary Tree, traversal requires a **stack or recursion** (extra memory).  
🔹 A **Threaded Binary Tree** avoids recursion by using **extra pointers (threads)** for traversal.  
🔹 This reduces **time and space complexity**.

---

## **2️⃣ Types of Threaded Binary Trees**
1. **Single Threaded:** Threads are used only for the **inorder successor** (Right threads).  
2. **Double Threaded:** Threads are used for **both inorder predecessor & successor** (Left and Right threads).  

---

## **3️⃣ Structure of a Threaded Binary Tree**
Example of a **Double Threaded Binary Tree:**
```
       20
      /  \
    10    30
       \  /
       15 25
```
Here, if **10 has no right child, its right pointer (thread) points to 15 (inorder successor).**  
Similarly, if **30 has no left child, its left pointer (thread) points to 25 (inorder predecessor).**  

---

## **4️⃣ Threaded Binary Tree Node Structure**
Each node in a **Threaded Binary Tree** has:
- `left`: Left child OR Inorder Predecessor (Thread)
- `right`: Right child OR Inorder Successor (Thread)
- `lTag`: `0` if the left pointer is a child, `1` if it’s a thread  
- `rTag`: `0` if the right pointer is a child, `1` if it’s a thread  

```c
struct Node {
    int data;
    struct Node *left, *right;
    int lTag, rTag;
};
```

---

## **5️⃣ Insertion in a Threaded Binary Tree**
### **Steps to Insert a Node**
1. Insert a new node as in **Binary Search Tree (BST)**.  
2. Modify **left and right pointers** to maintain threading.  
3. **Update lTag & rTag** to mark threads.  

Example:  
```
       20
      /  \
    10    30
       \  /
       15 25
```
If we insert `12`, it will be threaded as:
```
       20
      /  \
    10    30
   /  \  /
  5    15 25
      /
    12
```

---

## **6️⃣ Traversals in a Threaded Binary Tree**
### **1️⃣ Inorder Traversal (Left → Root → Right)**
1. **Find the leftmost node.**  
2. **Follow the threads for traversal.**  

```c
void inorder(Node *root) {
    Node *curr = root;
    while (curr->lTag == 0) 
        curr = curr->left;  // Go to leftmost node

    while (curr != NULL) {
        printf("%d ", curr->data);
        if (curr->rTag == 1)  
            curr = curr->right;  // Follow thread
        else {
            curr = curr->right;
            while (curr->lTag == 0)
                curr = curr->left;  // Find leftmost node again
        }
    }
}
```

### **2️⃣ Preorder Traversal (Root → Left → Right)**
1. **Print the node.**  
2. **Follow left child if available. If not, follow the right thread.**  

```c
void preorder(Node *root) {
    Node *curr = root;
    while (curr != NULL) {
        printf("%d ", curr->data);
        if (curr->lTag == 0) 
            curr = curr->left;  // Move to left child
        else 
            curr = curr->right;  // Follow thread
    }
}
```

---

## **7️⃣ Advantages of Threaded Binary Trees**
✅ **Faster Traversal** (No stack/recursion needed)  
✅ **Reduces Space Complexity** (Uses O(1) extra space)  
✅ **Easier Inorder Successor Access**  

---

## **8️⃣ Applications of Threaded Binary Trees**
🔹 **Expression Trees (for parsing expressions)**  
🔹 **Database Indexing (for fast search operations)**  
🔹 **Compiler Design (Abstract Syntax Trees)**  

---
### **Heaps**  

A **Heap** is a specialized tree-based data structure that satisfies the **heap property**. It is primarily used to implement **priority queues** and is an essential data structure for **sorting algorithms** like Heap Sort.  

---

## **1️⃣ Why Use Heaps?**
✅ **Efficient Priority Queue Implementation** (Insertion & Deletion in O(log n))  
✅ **Efficient Sorting (Heap Sort - O(n log n))**  
✅ **Used in Graph Algorithms (Dijkstra's, Prim's Algorithm)**  
✅ **Memory-efficient (Implemented as an array)**  

---

## **2️⃣ Types of Heaps**
1. **Max Heap:**  
   - The **largest element** is always at the root.  
   - Each parent node is **greater than or equal to** its children.  
2. **Min Heap:**  
   - The **smallest element** is always at the root.  
   - Each parent node is **less than or equal to** its children.  

### **Example of a Max Heap**
```
        50
       /  \
     30    40
    /  \   /  \
   10   20 15  35
```
- The **largest element (50) is at the root**.  
- Every parent is **greater than or equal to its children**.  

---

## **3️⃣ Heap Representation in an Array**
A **binary heap** is typically represented as an **array**, where:
- **Root is at index 0**
- **Left child of node at index i:** `2*i + 1`
- **Right child of node at index i:** `2*i + 2`
- **Parent of node at index i:** `(i-1)/2`

**Example Heap in Array Form**
```
Heap: [50, 30, 40, 10, 20, 15, 35]
Indexes:  0   1   2   3   4   5   6
```
For node at index `1` (30):
- Left Child = `arr[3] = 10`
- Right Child = `arr[4] = 20`
- Parent = `arr[0] = 50`

---

## **4️⃣ Operations on Heaps**
### **1️⃣ Insertion in a Heap (O(log n))**
1. **Insert the new element** at the end of the array (last level).  
2. **Heapify Up**: Compare with parent and swap if necessary.  
3. **Repeat until the heap property is restored.**  

**Example:** Insert `45` into the max heap  
```
Before:   [50, 30, 40, 10, 20, 15, 35]
Insert 45: [50, 30, 40, 10, 20, 15, 35, 45]
Heapify Up: Swap(45, 10) → Swap(45, 30)
Final Heap: [50, 45, 40, 30, 20, 15, 35, 10]
```

**Code for Insertion in Max Heap**
```c
void insertHeap(int arr[], int *size, int value) {
    int i = (*size)++;
    arr[i] = value;
    while (i > 0 && arr[(i-1)/2] < arr[i]) {
        int temp = arr[(i-1)/2];
        arr[(i-1)/2] = arr[i];
        arr[i] = temp;
        i = (i-1)/2;  // Move up to parent
    }
}
```

---

### **2️⃣ Deletion in a Heap (O(log n))**
1. **Delete the root (largest/smallest element)**.  
2. **Replace it with the last element** in the heap.  
3. **Heapify Down**: Compare with children and swap if necessary.  
4. **Repeat until the heap property is restored.**  

**Example:** Delete `50` from the max heap  
```
Before: [50, 45, 40, 30, 20, 15, 35, 10]
Replace root with last element: [10, 45, 40, 30, 20, 15, 35]
Heapify Down: Swap(10, 45) → Swap(10, 30)
Final Heap: [45, 30, 40, 10, 20, 15, 35]
```

**Code for Deletion in Max Heap**
```c
void deleteRoot(int arr[], int *size) {
    arr[0] = arr[--(*size)]; // Replace root with last element
    int i = 0;
    while (2*i+1 < *size) {
        int child = 2*i+1;
        if (child+1 < *size && arr[child] < arr[child+1])
            child++;  // Choose the larger child
        if (arr[i] >= arr[child]) break; // Heap property satisfied
        int temp = arr[i]; arr[i] = arr[child]; arr[child] = temp;
        i = child;
    }
}
```

---

### **3️⃣ Heap Sort (O(n log n))**
Heap Sort works by:
1. **Building a Max Heap** from an array.
2. **Extracting the largest element** (root) and placing it at the end.
3. **Reheapifying** the remaining elements.
4. **Repeating until the array is sorted**.

**Example:** Sort `[50, 30, 40, 10, 20, 15, 35]`  
```
Step 1: Build Max Heap → [50, 30, 40, 10, 20, 15, 35]
Step 2: Swap 50 ↔ last element → [35, 30, 40, 10, 20, 15, 50]
Step 3: Reheapify → [40, 30, 35, 10, 20, 15, 50]
Repeat until sorted → [10, 15, 20, 30, 35, 40, 50]
```

**Code for Heap Sort**
```c
void heapify(int arr[], int n, int i) {
    int largest = i, left = 2*i + 1, right = 2*i + 2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        int temp = arr[i]; arr[i] = arr[largest]; arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n-1; i > 0; i--) {
        int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
        heapify(arr, i, 0);
    }
}
```

---

## **5️⃣ Applications of Heaps**
🔹 **Priority Queues (Job Scheduling, CPU Scheduling)**  
🔹 **Graph Algorithms (Dijkstra’s Shortest Path, Prim’s MST)**  
🔹 **Heap Sort (Efficient Sorting Algorithm)**  
🔹 **Memory Management (Garbage Collection in Java & Python)**  
🔹 **Database Query Optimization**  

---

### **Final Summary**
✅ **Max Heap:** Largest element at root  
✅ **Min Heap:** Smallest element at root  
✅ **Heapify:** Used to maintain heap property  
✅ **Insertion & Deletion:** O(log n)  
✅ **Heap Sort:** O(n log n)  

---

