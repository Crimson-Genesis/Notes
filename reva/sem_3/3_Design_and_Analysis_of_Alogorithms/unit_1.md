# Unit - 1

## Introfuction, Fundamentals of the Analysis of Algorithm Effiviency
- Notation of Algorithm
- Fundamentals of Algorithmic Problem Solving
- Important Problem Types
- Fundamentals data Stucutres
- Analysis Framework
- Asymptotic Notations and Basic Effiviency classes
- Mathematical analysis of Recursive and Non-recursive algorithams

- Introduction: Algorithm
- Pseudo code for Expressing Algorithms
- Mathematics for Algorithmic Sets
- Functions and Relations
- Vectors and matrices
- Linear Inequalities and Linear Equations

- Analysis Framework
- Measuring and Input's Size
- Units for Measuring Running Time
- Order of Growth
- Worst-Case Effiviency
- Best-Case Effiviency
- Average-Case Effiviency

- Performance Analysis
- Space Complexity
- Time Complexity
- Asymptotic Notation- Big(O) Notation, Omega Notation, Theta Notation and Little (o) Notation
- Recurrences

---
---

# 🧠 **Notation of Algorithm**

---

## 🔹 1. What is an Algorithm?

An **algorithm** is a **finite sequence of well-defined instructions** designed to perform a specific task or solve a specific problem.

It takes **input**, performs **processing**, and produces **output**.

### General Structure:

```
Algorithm  <AlgorithmName>
Input: <Description of input>
Output: <Description of output>
Steps:
    Step 1: ...
    Step 2: ...
    Step 3: ...
    ...
    Step n: ...
```

---

## 🔹 2. Purpose of Algorithm Notation

The **notation of algorithm** is the **way we express** or **represent** an algorithm clearly so that:

* It is **independent of programming language** (not C, Python, etc.)
* It is **easy to understand**, **analyze**, and **implement**
* It expresses **logic**, not syntax

Common representations:

1. **Natural Language Description**
2. **Flowchart**
3. **Pseudo Code**
4. **Mathematical Notation**

---

## 🔹 3. Example of Algorithm Representation

Let’s take a simple example — **finding the maximum of two numbers.**

---

### (a) **Natural Language Form**

> Step 1: Read two numbers, A and B
> Step 2: If A > B, print A is greater
> Step 3: Else, print B is greater

---

### (b) **Flowchart Representation**

```
   ┌───────────┐
   │ Start     │
   └───┬───────┘
       │
       ▼
 ┌──────────────┐
 │ Read A, B    │
 └─────┬────────┘
       │
       ▼
 ┌──────────────┐
 │ A > B ?      │
 └─────┬────────┘
   Yes │ No
       ▼
 ┌──────────┐    ┌──────────┐
 │ Print A  │    │ Print B  │
 └────┬─────┘    └────┬─────┘
       │               │
       └───────┬───────┘
               ▼
          ┌────────┐
          │ Stop   │
          └────────┘
```

---

### (c) **Pseudo Code Notation**

```
Algorithm Max_of_Two(A, B)
Input: Two numbers A and B
Output: Maximum of A and B

Begin
    if A > B then
        print "A is greater"
    else
        print "B is greater"
    end if
End
```

---

### (d) **Mathematical Form (Functional)**

[
\text{max}(A, B) =
\begin{cases}
A, & \text{if } A > B \
B, & \text{otherwise}
\end{cases}
]

---

## 🔹 4. Characteristics of a Good Algorithm Notation

| Property                       | Description                                    |
| ------------------------------ | ---------------------------------------------- |
| **Clarity**                    | Must be unambiguous and easy to follow         |
| **Language Independence**      | Not tied to any specific programming syntax    |
| **Stepwise Refinement**        | Complex steps can be broken into sub-steps     |
| **Ease of Analysis**           | Should help estimate time and space complexity |
| **Implementation Feasibility** | Should be easily translatable into real code   |

---

## 🔹 5. Why Not Use Real Code?

Using programming languages directly (like C or Python) makes the **logic less clear** because:

* Syntax varies between languages
* Efficiency analysis becomes harder
* The focus shifts from logic to implementation

Hence, **notation like pseudocode or flowcharts** are preferred during **algorithm design**.

---

## 🔹 6. Levels of Notation

| Level                   | Description                                        | Example                                  |
| ----------------------- | -------------------------------------------------- | ---------------------------------------- |
| **High-Level Notation** | English-like description                           | “Find the largest element in the array.” |
| **Mid-Level Notation**  | Pseudocode with structured constructs              | `for i ← 1 to n do`                      |
| **Low-Level Notation**  | Machine-level details, like steps of CPU execution | Register and memory operations           |

---

## 🔹 7. Example: Sum of First n Natural Numbers

Let’s write it in **different notations**.

### (a) Natural Language

> Read n
> Initialize sum = 0
> Repeat from i = 1 to n
> Add i to sum
> Print sum

### (b) Pseudocode

```
Algorithm Sum_Natural(n)
Input: A positive integer n
Output: Sum of first n natural numbers

Begin
    sum ← 0
    for i ← 1 to n do
        sum ← sum + i
    end for
    print sum
End
```

### (c) Mathematical Representation

[
S = \sum_{i=1}^{n} i = \frac{n(n+1)}{2}
]

---

## 🔹 8. Summary Table

| Representation       | Advantages                        | Disadvantages                 |
| -------------------- | --------------------------------- | ----------------------------- |
| **Natural Language** | Easy to understand                | Ambiguous                     |
| **Flowchart**        | Visual & clear logic              | Hard for large algorithms     |
| **Pseudo Code**      | Structured & language-independent | Needs familiarity with syntax |
| **Mathematical**     | Compact & formal                  | Hard for beginners            |

---

## ✅ **Key Takeaways**

* **Algorithm notation** provides a **clear and standard way** to represent an algorithm.
* It separates **logic** from **implementation**.
* **Pseudocode** is the most common and preferred form in algorithm analysis.
* Helps in **analyzing efficiency** (time & space complexity).

---

# 🧠 Fundamentals of Algorithmic Problem Solving

---

## 🔹 1. What is Problem Solving?

**Problem Solving** is the process of **identifying**, **analyzing**, and **developing a procedure (algorithm)** to find a solution for a given problem.

> **Goal:** To design an algorithm that is **correct**, **efficient**, and **easy to implement**.

---

## 🔹 2. Steps in Algorithmic Problem Solving

The process of solving a problem algorithmically can be divided into **seven standard steps**:

| Step                              | Description                                                            |
| --------------------------------- | ---------------------------------------------------------------------- |
| **1. Understanding the Problem**  | Identify what the problem asks and what the desired output should be.  |
| **2. Analyzing the Problem**      | Determine constraints, available data, and relationships among data.   |
| **3. Designing the Algorithm**    | Develop the step-by-step logic to solve the problem.                   |
| **4. Representing the Algorithm** | Express it in pseudocode or flowchart form.                            |
| **5. Implementing the Algorithm** | Translate the pseudocode into a programming language (like C, Python). |
| **6. Testing and Debugging**      | Verify correctness using test cases and fix errors.                    |
| **7. Analyzing Efficiency**       | Measure time and space requirements and optimize if needed.            |

---

## 🔹 3. Step-by-Step Example

Let’s take an example problem to understand the process:

### 🧩 **Problem:** Find the largest number in a list of n numbers.

---

### **Step 1 – Understanding the Problem**

We need to find the **maximum** number among given numbers.
Input: A list of `n` numbers → `[a1, a2, ..., an]`
Output: The **maximum** number.

---

### **Step 2 – Analyzing the Problem**

* Operation: Compare each element with the current maximum.
* Constraints: At least one number must be given.
* Data Type: Can be integers or floats.

---

### **Step 3 – Designing the Algorithm**

Idea:

* Start with the first number as the maximum.
* Compare it with every other number.
* If any number is larger, update the maximum.

---

### **Step 4 – Representing the Algorithm (Pseudocode)**

```
Algorithm Find_Max(A, n)
Input: A list A of n numbers
Output: The maximum number in A

Begin
    max ← A[1]
    for i ← 2 to n do
        if A[i] > max then
            max ← A[i]
        end if
    end for
    print "Maximum =", max
End
```

---

### **Step 5 – Implementation (C code)**

```c
#include <stdio.h>

int main() {
    int n, i;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int A[n];
    printf("Enter elements: ");
    for (i = 0; i < n; i++)
        scanf("%d", &A[i]);

    int max = A[0];
    for (i = 1; i < n; i++)
        if (A[i] > max)
            max = A[i];

    printf("Maximum = %d\n", max);
    return 0;
}
```

---

### **Step 6 – Testing and Debugging**

Test Case 1:
Input: `[3, 7, 2, 9, 5]` → Output: `9`

Test Case 2:
Input: `[-1, -5, -3]` → Output: `-1`

---

### **Step 7 – Efficiency Analysis**

* **Time Complexity:** $O(n)$ (as each element is checked once)
* **Space Complexity:** $O(1)$ (no extra space used)

---

## 🔹 4. Key Elements in Algorithmic Problem Solving

| Element           | Description                                 | Example                         |
| ----------------- | ------------------------------------------- | ------------------------------- |
| **Input**         | Data given to the algorithm                 | Array of numbers                |
| **Output**        | Result produced by algorithm                | Maximum number                  |
| **Definiteness**  | Each step must be clear and unambiguous     | Step 2: “Compare A[i] with max” |
| **Finiteness**    | Algorithm must terminate after finite steps | Loop ends when i = n            |
| **Effectiveness** | Steps must be basic enough to be executed   | Comparison operation            |
| **Correctness**   | Algorithm should give correct results       | Verified by test cases          |

---

## 🔹 5. Types of Problems in Algorithmic Solving

| Type                     | Description                       | Example                 |
| ------------------------ | --------------------------------- | ----------------------- |
| **Computation Problem**  | Calculate a result based on input | Sorting, Searching      |
| **Decision Problem**     | Output is “Yes” or “No”           | Is the number prime?    |
| **Optimization Problem** | Find best (minimum/maximum) value | Shortest path, Knapsack |
| **Enumeration Problem**  | List all possible configurations  | All subsets of a set    |

---

## 🔹 6. Problem-Solving Strategies

| Strategy                 | Idea                                             | Example               |
| ------------------------ | ------------------------------------------------ | --------------------- |
| **Brute Force**          | Try all possible solutions                       | Linear Search         |
| **Divide and Conquer**   | Break into subproblems and combine results       | Merge Sort            |
| **Decrease and Conquer** | Reduce size of problem step-by-step              | Insertion Sort        |
| **Greedy Approach**      | Take best choice at each step                    | Kruskal’s, Dijkstra’s |
| **Dynamic Programming**  | Solve subproblems and reuse results              | Fibonacci, Knapsack   |
| **Backtracking**         | Explore all solutions but backtrack when invalid | N-Queens Problem      |
| **Branch and Bound**     | Use bounds to cut off unpromising solutions      | Travelling Salesman   |

---

## 🔹 7. Diagram – The Algorithmic Problem Solving Process

```
 ┌────────────────────────────┐
 │ 1. Understand the Problem  │
 └──────────────┬─────────────┘
                │
                ▼
 ┌────────────────────────────┐
 │ 2. Analyze the Problem     │
 └──────────────┬─────────────┘
                │
                ▼
 ┌────────────────────────────┐
 │ 3. Design the Algorithm    │
 └──────────────┬─────────────┘
                │
                ▼
 ┌────────────────────────────┐
 │ 4. Represent in Pseudocode │
 └──────────────┬─────────────┘
                │
                ▼
 ┌────────────────────────────┐
 │ 5. Implement & Test        │
 └──────────────┬─────────────┘
                │
                ▼
 ┌────────────────────────────┐
 │ 6. Analyze Efficiency      │
 └────────────────────────────┘
```

---

## ✅ **Key Takeaways**

* Problem-solving in algorithms involves **understanding, designing, implementing, and analyzing**.
* A good algorithm should be **correct, efficient, and finite**.
* **Pseudocode** is the preferred form to represent algorithm logic.
* Common strategies include **Brute Force**, **Divide & Conquer**, **Greedy**, **Dynamic Programming**, and **Backtracking**.

---

# 🧠 Important Problem Types

---

## 🔹 1. Introduction

In algorithm design, problems can be classified into **different types** based on the **nature of the task** they perform and the **type of output** expected.

Understanding these types helps us choose the **right algorithmic strategy** (Brute Force, Divide & Conquer, Greedy, etc.) for solving them efficiently.

---

## 🔹 2. Major Types of Problems in Algorithm Design

Let’s go through each major type with **definition**, **examples**, **pseudocode**, and **remarks** 👇

---

## 🧩 **1. Sorting Problems**

### 🔸 Definition

Sorting means **arranging elements in a particular order**, typically ascending or descending.

### 🔸 Examples

* Sorting student marks from lowest to highest
* Sorting names alphabetically
* Sorting numbers for efficient searching later

### 🔸 Common Algorithms

| Algorithm      | Approach         | Time Complexity     |
| -------------- | ---------------- | ------------------- |
| Bubble Sort    | Brute Force      | $O(n^2)$            |
| Selection Sort | Brute Force      | $O(n^2)$            |
| Merge Sort     | Divide & Conquer | $O(n \log n)$       |
| Quick Sort     | Divide & Conquer | $O(n \log n)$ (avg) |

### 🔸 Example Pseudocode (Bubble Sort)

```
Algorithm Bubble_Sort(A, n)
Input: Array A with n elements
Output: Sorted array in ascending order

Begin
    for i ← 1 to n-1 do
        for j ← 1 to n-i do
            if A[j] > A[j+1] then
                swap A[j] and A[j+1]
            end if
        end for
    end for
End
```

---

## 🧩 **2. Searching Problems**

### 🔸 Definition

Finding whether an element exists in a collection, or finding its position.

### 🔸 Examples

* Searching a student roll number in a list
* Looking up a word in a dictionary

### 🔸 Common Algorithms

| Algorithm     | Approach         | Time Complexity |
| ------------- | ---------------- | --------------- |
| Linear Search | Brute Force      | $O(n)$          |
| Binary Search | Divide & Conquer | $O(\log n)$     |

### 🔸 Example Pseudocode (Binary Search)

```
Algorithm Binary_Search(A, n, key)
Input: Sorted array A with n elements, element key
Output: Index of key if found, else -1

Begin
    low ← 1
    high ← n
    while low ≤ high do
        mid ← (low + high) / 2
        if A[mid] = key then
            return mid
        else if A[mid] < key then
            low ← mid + 1
        else
            high ← mid - 1
        end if
    end while
    return -1
End
```

---

## 🧩 **3. Graph Problems**

### 🔸 Definition

Graph problems involve **nodes (vertices)** connected by **edges**, used to model networks or relationships.

### 🔸 Examples

* Finding the **shortest path** between two cities
* **Minimum spanning tree** for road networks
* **Topological sorting** of project tasks

### 🔸 Common Algorithms

| Problem                 | Algorithm            | Technique               |
| ----------------------- | -------------------- | ----------------------- |
| Shortest Path           | Dijkstra’s Algorithm | Greedy                  |
| All-Pairs Shortest Path | Floyd-Warshall       | Dynamic Programming     |
| Minimum Spanning Tree   | Prim’s / Kruskal’s   | Greedy                  |
| Traversal               | BFS, DFS             | Brute Force / Recursive |

### 🔸 Diagram Example

```
A──5──B──2──C
│     │
4     3
│     │
D─────E
```

**Goal:** Find shortest paths, MST, etc.

---

## 🧩 **4. Combinatorial Problems**

### 🔸 Definition

These problems deal with **arranging or selecting objects** from a set according to certain rules.

### 🔸 Examples

* Generating all possible passwords of a certain length
* Solving the **N-Queens problem**
* The **Travelling Salesman Problem (TSP)**

### 🔸 Common Techniques

| Approach           | Examples                  |
| ------------------ | ------------------------- |
| **Brute Force**    | Generate all combinations |
| **Backtracking**   | N-Queens, Subset Sum      |
| **Branch & Bound** | TSP, Knapsack             |

---

## 🧩 **5. Numerical Problems**

### 🔸 Definition

Problems based on **mathematical or arithmetic computations**.

### 🔸 Examples

* Finding the **GCD** (Greatest Common Divisor)
* Solving linear equations
* Computing factorials, Fibonacci numbers

### 🔸 Common Algorithms

| Problem               | Algorithm            | Technique             |
| --------------------- | -------------------- | --------------------- |
| GCD                   | Euclid’s Algorithm   | Recursive / Iterative |
| Fibonacci             | Dynamic Programming  | DP                    |
| Matrix Multiplication | Strassen’s Algorithm | Divide & Conquer      |

### 🔸 Example (Euclid’s Algorithm)

```
Algorithm GCD(a, b)
Input: Two positive integers a, b
Output: Greatest common divisor of a and b

Begin
    while b ≠ 0 do
        temp ← b
        b ← a mod b
        a ← temp
    end while
    return a
End
```

---

## 🧩 **6. Optimization Problems**

### 🔸 Definition

Find the **best solution** among many possible solutions (max or min value).

### 🔸 Examples

* **Knapsack Problem:** maximize profit with limited weight
* **Shortest Path Problem:** minimize total distance
* **Job Scheduling:** minimize total completion time

### 🔸 Common Techniques

| Technique               | Examples                 |
| ----------------------- | ------------------------ |
| **Greedy**              | Dijkstra’s, Kruskal’s    |
| **Dynamic Programming** | Knapsack, Floyd-Warshall |
| **Branch and Bound**    | TSP, Assignment Problem  |

---

## 🧩 **7. String Processing Problems**

### 🔸 Definition

Problems involving manipulation or matching of **character strings**.

### 🔸 Examples

* Searching for a **substring** in a text (e.g., “cat” in “concatenate”)
* Counting pattern occurrences

### 🔸 Common Algorithms

| Algorithm          | Technique         | Time Complexity |
| ------------------ | ----------------- | --------------- |
| Naïve String Match | Brute Force       | $O(nm)$         |
| Horspool’s         | Input Enhancement | $O(n)$ (avg)    |
| Boyer-Moore        | Input Enhancement | $O(n)$ (avg)    |

---

## 🧩 **8. Geometric Problems**

### 🔸 Definition

Problems dealing with **geometrical shapes** like points, lines, and polygons.

### 🔸 Examples

* Finding the **closest pair of points**
* Computing **convex hull**
* Detecting **line intersections**

### 🔸 Common Algorithms

| Problem      | Algorithm        | Technique     |
| ------------ | ---------------- | ------------- |
| Closest Pair | Divide & Conquer | $O(n \log n)$ |
| Convex Hull  | Graham’s Scan    | $O(n \log n)$ |

---

## 🧩 **9. Graphical Representation (Summary)**

| Problem Type  | Example           | Common Approach   | Example Algorithm |
| ------------- | ----------------- | ----------------- | ----------------- |
| Sorting       | Arrange numbers   | Brute Force / D&C | Merge Sort        |
| Searching     | Find key in array | Brute Force       | Binary Search     |
| Graph         | Shortest path     | Greedy / DP       | Dijkstra, Floyd   |
| Combinatorial | N-Queens          | Backtracking      | Recursive         |
| Numerical     | Fibonacci         | DP / Recursive    | Fibonacci DP      |
| Optimization  | Knapsack          | Greedy / DP       | 0/1 Knapsack      |
| String        | Pattern matching  | Input Enhancement | Boyer-Moore       |
| Geometric     | Convex Hull       | Divide & Conquer  | Graham’s Scan     |

---

## ✅ **Key Takeaways**

* Problem types guide us in choosing the **right design technique**.
* **Sorting & Searching** are the foundation for most others.
* **Optimization**, **Graph**, and **Combinatorial** problems form the **core of advanced algorithm design**.
* The **same problem** can sometimes be solved by **multiple techniques**, each with different efficiency.

---

# 🧠 Fundamentals of Data Structures

---

## 🔹 1. Introduction

Before writing or analyzing algorithms, we must decide **how to store and organize data** so that the algorithm can process it efficiently.

> A **Data Structure** is a **way of organizing data** in memory so that it can be used effectively.

### Example:

To find a student’s record quickly:

* A **list** may work (slow search).
* A **hash table** may be better (fast search).

So, choosing the **right data structure** directly affects **algorithm efficiency**.

---

## 🔹 2. Need for Data Structures

| Need                         | Explanation                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **Efficient Data Access**    | Store data so that insertion, deletion, and searching are fast.                     |
| **Memory Management**        | Use minimum space to represent data.                                                |
| **Reusability & Modularity** | Standard data structures can be reused in many programs.                            |
| **Improved Performance**     | Proper structures reduce algorithm complexity (e.g., from $O(n^2)$ to $O(\log n)$). |

---

## 🔹 3. Classification of Data Structures

Data structures are mainly divided into two broad categories:

```
                Data Structures
                      │
     ┌────────────────┴────────────────┐
     │                                 │
Primitive Data Structures      Non-Primitive Data Structures
     │                                 │
  (Built-in Types)                ┌───────────────┬───────────────┐
     │                            │               │               │
 Integer, Float, Char, Bool     Linear         Non-Linear     File Structures
                                (List, Stack,  (Tree, Graph)  (for data storage)
                                 Queue)
```

---

## 🔹 4. Primitive Data Structures

These are **basic data types** directly provided by programming languages.

| Type               | Description              | Example             |
| ------------------ | ------------------------ | ------------------- |
| **Integer**        | Stores whole numbers     | `int a = 5;`        |
| **Float / Double** | Stores real numbers      | `float x = 3.14;`   |
| **Character**      | Stores single characters | `char c = 'A';`     |
| **Boolean**        | Stores true/false values | `bool flag = true;` |

---

## 🔹 5. Non-Primitive Data Structures

These are **derived** from primitive types and used to handle **large and complex data**.

---

### 🧩 (A) **Linear Data Structures**

Data elements are **arranged sequentially**, and each element has a **unique predecessor and successor** (except first and last).

#### Examples:

1. **Arrays**
2. **Linked Lists**
3. **Stacks**
4. **Queues**

Let’s go through each 👇

---

### 1️⃣ **Array**

* Fixed-size, homogeneous collection (all same data type).
* Elements stored in **contiguous memory locations**.

#### Representation:

```
Index →   0   1   2   3   4
Value →  [10, 20, 30, 40, 50]
```

#### Example (C Code)

```c
int A[5] = {10, 20, 30, 40, 50};
printf("%d", A[2]);  // prints 30
```

#### Characteristics:

* Random access → $O(1)$
* Insertion/Deletion → $O(n)$ (slow)

---

### 2️⃣ **Linked List**

* Collection of **nodes**, each containing **data** and **pointer** to the next node.
* Memory need **not be contiguous**.

#### Singly Linked List Diagram:

```
[10|*] → [20|*] → [30|NULL]
```

#### Node Structure:

```c
struct Node {
    int data;
    struct Node *next;
};
```

#### Characteristics:

* Dynamic size
* Easy insertion/deletion → $O(1)$ (if position known)
* Sequential access only → $O(n)$

---

### 3️⃣ **Stack**

* Linear structure following **LIFO (Last In, First Out)** order.

#### Diagram:

```
Top → [50]
       [40]
       [30]
       [20]
       [10]
```

#### Operations:

| Operation | Description             |
| --------- | ----------------------- |
| `push(x)` | Insert element on top   |
| `pop()`   | Remove element from top |
| `peek()`  | View top element        |

#### Example:

```c
push(10)
push(20)
push(30)
pop() → removes 30
```

#### Applications:

* Expression evaluation
* Function call stack
* Undo operations

---

### 4️⃣ **Queue**

* Linear structure following **FIFO (First In, First Out)** order.

#### Diagram:

```
Front → [10] [20] [30] ← Rear
```

#### Operations:

| Operation    | Description               |
| ------------ | ------------------------- |
| `enqueue(x)` | Add element at rear       |
| `dequeue()`  | Remove element from front |

#### Example:

```c
enqueue(10)
enqueue(20)
dequeue() → removes 10
```

#### Applications:

* Scheduling tasks
* Print queue
* CPU process management

---

### 🧩 (B) **Non-Linear Data Structures**

Data elements are **not sequentially connected** — each element can have multiple relationships.

#### Examples:

1. **Trees**
2. **Graphs**

---

### 1️⃣ **Tree**

* Hierarchical structure with **root** and **children nodes**.
* Each node can have **0 or more child nodes**.

#### Diagram:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

#### Terminology:

| Term   | Meaning                        |
| ------ | ------------------------------ |
| Root   | Topmost node                   |
| Parent | Node having children           |
| Leaf   | Node with no children          |
| Height | Longest path from root to leaf |

#### Applications:

* Binary Search Trees (BST)
* Syntax trees (compiler)
* File system hierarchy

---

### 2️⃣ **Graph**

* A set of **vertices (nodes)** and **edges (connections)**.

#### Types:

* **Directed Graph (Digraph)**
* **Undirected Graph**

#### Diagram:

```
A —— B —— C
 \    |
  \   |
    D
```

#### Representation:

* **Adjacency Matrix**
* **Adjacency List**

#### Applications:

* Social networks
* Shortest path algorithms
* Web page ranking

---

## 🧩 (C) **File Structures**

* Used to **store and retrieve data permanently** from external storage (like hard disks).
* Examples:

  * Sequential file
  * Indexed file
  * Direct (hash) file

---

## 🔹 6. Abstract Data Types (ADT)

> An **ADT** defines *what operations* can be performed, not *how* they are implemented.

### Example: Stack ADT

| Operation   | Description             |
| ----------- | ----------------------- |
| `push(x)`   | Insert element          |
| `pop()`     | Remove top element      |
| `isEmpty()` | Check if stack is empty |
| `top()`     | Get top element         |

Implementation may differ (Array or Linked List), but interface remains same.

---

## 🔹 7. Comparison of Linear & Non-Linear Structures

| Feature           | Linear                           | Non-Linear                     |
| ----------------- | -------------------------------- | ------------------------------ |
| Data Organization | Sequential                       | Hierarchical / Network         |
| Traversal         | Single path                      | Multiple paths                 |
| Examples          | Array, Stack, Queue, Linked List | Tree, Graph                    |
| Implementation    | Simple                           | Complex                        |
| Applications      | Sorting, Searching               | Hierarchical storage, Networks |

---

## 🔹 8. Diagram – Classification Summary

```
                  Data Structures
                        │
        ┌───────────────┴────────────────┐
        │                                │
   Primitive                        Non-Primitive
(Integer, Float, Char)                 │
                                       ├───────────────┐
                                       │               │
                                   Linear          Non-Linear
                                   (Array,         (Tree,
                                   Stack, Queue)   Graph)
```

---

## ✅ **Key Takeaways**

* **Data Structure** = way of organizing data for efficient access & modification.
* Divided into **Primitive** and **Non-Primitive**.
* Non-primitive further divided into **Linear** and **Non-linear**.
* Choosing the right data structure = better **time & space efficiency**.
* **ADT (Abstract Data Type)** defines *operations*, not *implementation*.

---

# 🧩 **Analysis Framework**

---

## 🔹 1. Introduction

When we design an algorithm, we often have multiple ways to solve the same problem.
For example:

* Searching an element: **Linear Search** vs **Binary Search**
* Sorting data: **Bubble Sort**, **Merge Sort**, **Quick Sort**, etc.

So, **how do we decide which algorithm is better?**

👉 We need a **framework** — a *structured method* to measure and compare the performance of algorithms in terms of:

* **Efficiency** (Time & Space)
* **Scalability**
* **Simplicity**
* **Correctness**

That’s what we call the **Analysis Framework**.

---

## 🔹 2. Objectives of Analysis Framework

The goal is to:

1. **Measure the efficiency** of algorithms.
2. **Compare** multiple algorithms solving the same problem.
3. **Predict performance** before actual implementation.
4. **Understand scalability** when input size grows.

---

## 🔹 3. Key Components of the Framework

| Component               | Description                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Input Size (n)**      | The number of elements or data items the algorithm processes.                       |
| **Operation Count**     | The number of basic operations executed (comparisons, additions, assignments, etc.) |
| **Time Complexity**     | How the running time grows with input size.                                         |
| **Space Complexity**    | How much memory the algorithm needs during execution.                               |
| **Type of Analysis**    | Best case, Average case, Worst case.                                                |
| **Asymptotic Notation** | Mathematical notation for comparing growth rates (O, Ω, Θ).                         |

---

## 🔹 4. Steps in Algorithm Analysis Framework

Let’s go through the process step-by-step:

### Step 1️⃣ — Define the Algorithm

You start with a **clear algorithm** (usually written in pseudocode).

### Step 2️⃣ — Identify Input Parameters

Determine what influences the algorithm’s running time.
Example:

* For searching → size of array `n`
* For matrix operations → dimensions `m × n`

### Step 3️⃣ — Identify the Basic Operation

Find the operation that **dominates the running time**.
Examples:

* Searching → comparison
* Sorting → swapping or comparison
* Matrix multiplication → multiplication or addition

### Step 4️⃣ — Count the Basic Operations

Express how many times the basic operation executes as a function of `n`.
👉 This gives **T(n)** = number of basic operations as a function of input size.

Example:
For linear search,
$$T(n) = n$$ (in the worst case)

### Step 5️⃣ — Express Growth Rate

We then use **asymptotic notations** (like Big O) to express this growth rate.
Example:
If $T(n) = 3n + 2$,
we simplify it to **O(n)**.

### Step 6️⃣ — Classify Efficiency

Group algorithms into efficiency classes such as:

* Constant time → O(1)
* Logarithmic → O(log n)
* Linear → O(n)
* Quadratic → O(n²)
* Exponential → O(2ⁿ)

---

## 🔹 5. Visual Representation

### ⚙️ Flow Diagram of Algorithm Analysis Framework

```
          ┌───────────────────────┐
          │   Design Algorithm    │
          └────────────┬──────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Identify Input Size (n) │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Choose Basic Operation │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Count Operation Steps  │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Express T(n) Function  │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Use Asymptotic Notation│
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Compare Algorithm Class│
          └────────────────────────┘
```

---

## 🔹 6. Example: Linear Search

### Pseudocode

```text
Algorithm LinearSearch(A, key)
1. for i ← 0 to n-1 do
2.     if A[i] = key then
3.         return i
4. return -1
```

### Step-by-step analysis

* **Input size (n):** number of elements in A
* **Basic operation:** comparison `A[i] = key`
* **Count:**

  * Best case → 1 comparison (if first element matches)
  * Worst case → n comparisons (if last or absent)
* **T(n):**

  * Best case → O(1)
  * Worst case → O(n)
  * Average case → O(n)

---

## 🔹 7. Example Table for Comparison

| Algorithm     | Best Case | Worst Case | Average Case | Efficiency Class |
| ------------- | --------- | ---------- | ------------ | ---------------- |
| Linear Search | O(1)      | O(n)       | O(n)         | Linear           |
| Binary Search | O(1)      | O(log n)   | O(log n)     | Logarithmic      |
| Bubble Sort   | O(n)      | O(n²)      | O(n²)        | Quadratic        |

---

## 🔹 8. Why the Framework Matters

Because without it:

* We can’t objectively say which algorithm is better.
* Code efficiency depends on system, compiler, and language — but asymptotic analysis gives **machine-independent comparison**.
* It helps us **predict performance** before coding.

---

## 🧠 Summary

| Aspect            | Description                                      |
| ----------------- | ------------------------------------------------ |
| **Purpose**       | To systematically analyze and compare algorithms |
| **Core Metrics**  | Time complexity & Space complexity               |
| **Approach**      | Mathematical estimation of growth rates          |
| **Notation Used** | O, Ω, Θ, o                                       |
| **Outcome**       | Classification into efficiency classes           |

---

# 🧩 **Asymptotic Notations and Basic Efficiency Classes**

---

## 🔹 1. What is Asymptotic Analysis?

When we analyze an algorithm, we often care about **how it behaves as the input size grows very large (n → ∞)**.

Instead of measuring **exact running time**, we study the **rate of growth** —
i.e., how quickly the running time increases with respect to input size.

👉 This is called **Asymptotic Analysis**.
It focuses on the **trend** of performance, not the actual number of milliseconds.

---

### 🔸 Example

If one algorithm takes
$$T_1(n) = 3n^2 + 10n + 20$$
and another takes
$$T_2(n) = 5n + 100$$

For small `n`, the second one might be slower (because of the +100 overhead).
But as `n` grows large, the **n² term dominates**, making `T₁(n)` grow much faster.

Thus, **T₂(n)** is more efficient for large inputs.

---

## 🔹 2. Asymptotic Notations — Overview

There are **four main asymptotic notations**:

| Notation          | Meaning            | Describes                   | Example              |
| ----------------- | ------------------ | --------------------------- | -------------------- |
| **Big O (O)**     | Upper Bound        | Worst-case growth rate      | $T(n) = O(n^2)$      |
| **Big Omega (Ω)** | Lower Bound        | Best-case growth rate       | $T(n) = Ω(n)$        |
| **Big Theta (Θ)** | Tight Bound        | Average / exact growth rate | $T(n) = Θ(n \log n)$ |
| **Little o (o)**  | Strict Upper Bound | Grows slower than           | $T(n) = o(n^2)$      |

---

## 🔹 3. Mathematical Definitions

Let’s go one by one 👇

---

### ⚙️ **1. Big O Notation (O)** — *Upper Bound*

**Definition:**
An algorithm’s time complexity is said to be `O(f(n))` if there exist positive constants `c` and `n₀` such that:

[
T(n) \leq c \cdot f(n) \quad \text{for all } n \ge n_0
]

It represents the **worst-case** growth rate — how fast time *can* grow.

#### Example:

If
[
T(n) = 3n^2 + 10n + 5
]
then we can say
[
T(n) = O(n^2)
]
because for large `n`, `n²` term dominates all others.

#### Graphically:

```
     |
 T(n)|            O(n^2)
     |          /
     |        /
     |      /
     |____/__________________ n
           n₀
```

---

### ⚙️ **2. Big Omega Notation (Ω)** — *Lower Bound*

**Definition:**
An algorithm’s time complexity is `Ω(f(n))` if there exist positive constants `c` and `n₀` such that:

[
T(n) \ge c \cdot f(n) \quad \text{for all } n \ge n_0
]

It represents the **best-case** growth rate — the least possible time.

#### Example:

If
[
T(n) = 5n^2 + 3n
]
then
[
T(n) = Ω(n^2)
]

---

### ⚙️ **3. Big Theta Notation (Θ)** — *Tight Bound*

**Definition:**
An algorithm is said to be `Θ(f(n))` if it is **both** O(f(n)) and Ω(f(n)).

[
c_1 \cdot f(n) \le T(n) \le c_2 \cdot f(n) \quad \text{for all } n \ge n_0
]

This gives a **precise growth rate**.

#### Example:

If
[
T(n) = 2n^2 + 10n + 20
]
then
[
T(n) = Θ(n^2)
]
(because it grows at the same rate as n²)

#### Graphically:

```
     |
 T(n)|   Θ(n^2)
     |  /
     | /
     |/
     |_________________________ n
```

---

### ⚙️ **4. Little o Notation (o)** — *Strictly Lower Order*

**Definition:**
`T(n) = o(f(n))` means that **T(n)** grows *slower* than **f(n)**.
Formally:
[
\lim_{n \to \infty} \frac{T(n)}{f(n)} = 0
]

#### Example:

If
[
T(n) = n
]
then
[
T(n) = o(n^2)
]
because n grows slower than n².

---

## 🔹 4. Visual Comparison

| Function    | Growth Rate | Notation Example |
| ----------- | ----------- | ---------------- |
| Constant    | Slowest     | O(1)             |
| Logarithmic |             | O(log n)         |
| Linear      |             | O(n)             |
| n log n     |             | O(n log n)       |
| Quadratic   |             | O(n²)            |
| Cubic       |             | O(n³)            |
| Exponential |             | O(2ⁿ)            |
| Factorial   | Fastest     | O(n!)            |

### 📈 Graph:

```
Time ↑
     |
     |                             O(n!)
     |                          /
     |                       /
     |                    /  O(2^n)
     |                 /
     |              /
     |           /   O(n^3)
     |        /   O(n^2)
     |     /
     |  /  O(n log n)
     |/ O(n)
     | O(log n)
     | O(1)
     +--------------------------------→ Input size (n)
```

---

## 🔹 5. Example Analysis

### Example 1: Linear Search

* Best case → Key found at first position → 1 comparison → **Ω(1)**
* Worst case → Key not found → n comparisons → **O(n)**
* Average case → (n+1)/2 comparisons → **Θ(n)**

### Example 2: Binary Search

* Best case → Key at middle → **Ω(1)**
* Worst case → Repeated halving → **O(log n)**
* Average case → **Θ(log n)**

### Example 3: Bubble Sort

* Best case (already sorted) → **Ω(n)**
* Worst case → **O(n²)**
* Average case → **Θ(n²)**

---

## 🔹 6. Basic Efficiency Classes

Algorithms are grouped into **efficiency classes** according to their asymptotic growth:

| Efficiency Class | Time Complexity | Example Algorithms               |
| ---------------- | --------------- | -------------------------------- |
| Constant Time    | O(1)            | Accessing array element          |
| Logarithmic      | O(log n)        | Binary Search                    |
| Linear           | O(n)            | Linear Search                    |
| Linearithmic     | O(n log n)      | Merge Sort, Quick Sort           |
| Quadratic        | O(n²)           | Bubble Sort, Insertion Sort      |
| Cubic            | O(n³)           | Matrix Multiplication            |
| Exponential      | O(2ⁿ)           | Subset Generation                |
| Factorial        | O(n!)           | Traveling Salesman (Brute Force) |

---

## 🔹 7. Importance of Asymptotic Notation

| Advantage                    | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| **Machine Independent**      | Does not depend on CPU speed or compiler.      |
| **Simplifies Comparison**    | Easy to compare algorithms mathematically.     |
| **Predicts Scalability**     | Shows how performance changes as input grows.  |
| **Focus on Core Efficiency** | Ignores unimportant constants and small terms. |

---

## 🧠 Summary

| Notation | Meaning              | Used For           | Symbolic Form |
| -------- | -------------------- | ------------------ | ------------- |
| O(f(n))  | Upper Bound          | Worst Case         | ≤             |
| Ω(f(n))  | Lower Bound          | Best Case          | ≥             |
| Θ(f(n))  | Tight Bound          | Average/Exact Case | =             |
| o(f(n))  | Strictly Lower Order | Slower growth      | <             |

---

# 🧩 **Mathematical Analysis of Recursive and Non-Recursive Algorithms**

---

## 🔹 1. Introduction

Every algorithm performs a **series of operations** depending on input size `n`.
To analyze how fast an algorithm runs, we define a **function T(n)** — representing the **number of basic operations** (or total time) executed for an input of size `n`.

There are **two categories** of algorithms:

| Type              | Description                              | Example                              |
| ----------------- | ---------------------------------------- | ------------------------------------ |
| **Non-Recursive** | Executes sequentially — no self-calls.   | Linear Search, Bubble Sort           |
| **Recursive**     | Calls itself on smaller input instances. | Binary Search, Merge Sort, Factorial |

We analyze them differently because recursion introduces **repeated sub-problems**.

---

## 🔹 2. Mathematical Analysis of **Non-Recursive Algorithms**

### 🧠 Idea:

We simply **count** the number of times the basic operation executes.

---

### ⚙️ Example 1 — Linear Search

**Algorithm:**

```text
Algorithm LinearSearch(A, n, key)
1. for i ← 0 to n−1 do
2.     if A[i] == key then
3.         return i
4. return −1
```

**Basic operation:** Comparison `A[i] == key`

**Counting:**

* Best case → 1 comparison
* Worst case → `n` comparisons
* Average case → `(n+1)/2` comparisons

So,
[
T_{best}(n) = 1,\quad T_{worst}(n) = n,\quad T_{avg}(n) = \frac{n+1}{2}
]

**Asymptotic form:**
[
T(n) = O(n)
]

---

### ⚙️ Example 2 — Nested Loops (Non-Recursive)

```text
Algorithm Example(A, n)
1. for i ← 1 to n do
2.     for j ← 1 to n do
3.         x ← x + A[i][j]
```

Here, **inner loop** runs `n` times for every `i` of outer loop.
Total iterations = `n × n = n²`.

So,
[
T(n) = c \cdot n^2 \quad \Rightarrow \quad O(n^2)
]

---

### ⚙️ Example 3 — Arithmetic Progression

```text
for i = 1 to n
   for j = 1 to i
      statement;
```

The inner loop runs `i` times for each `i`.

Total operations = 1 + 2 + 3 + … + n
[
T(n) = \frac{n(n+1)}{2} = O(n^2)
]

---

## 🔹 3. Mathematical Analysis of **Recursive Algorithms**

### 🧠 Idea:

For recursive algorithms, we form a **recurrence relation** for `T(n)` — the total time to solve input size `n`.

Then, we **solve** that recurrence using:

* Substitution Method
* Iteration / Expansion Method
* Master Theorem

---

### ⚙️ Example 1 — Factorial Function

**Algorithm:**

```text
Algorithm Factorial(n)
1. if n == 0 then return 1
2. else return n * Factorial(n - 1)
```

**Recurrence Relation:**
Each call makes **1 recursive call** of size (n−1) and performs 1 multiplication.

[
T(n) = T(n-1) + c
]
Base case: (T(0) = d)

**Solve:**
[
T(n) = c + T(n-1)
= c + [c + T(n-2)]
= n \cdot c + T(0)
\Rightarrow T(n) = O(n)
]

So factorial runs in **linear time**.

---

### ⚙️ Example 2 — Binary Search

**Algorithm:**

```text
Algorithm BinarySearch(A, low, high, key)
1. if low > high then return -1
2. mid = (low + high) / 2
3. if A[mid] == key then return mid
4. else if A[mid] < key
5.     return BinarySearch(A, mid+1, high, key)
6. else
7.     return BinarySearch(A, low, mid-1, key)
```

**Recurrence:**
Each call halves the array → `n/2`, and does constant work `c`.

[
T(n) = T(n/2) + c
]
Base case: (T(1) = d)

**By Iteration Method:**
[
\begin{align*}
T(n) &= c + T(n/2) \
&= c + [c + T(n/4)] \
&= c + c + [c + T(n/8)] \
&= k \cdot c + T(n/2^k)
\end{align*}
]
When (n/2^k = 1 \Rightarrow k = \log_2 n)

[
T(n) = c \log_2 n + d = O(\log n)
]

✅ **Binary Search is logarithmic**.

---

### ⚙️ Example 3 — Merge Sort

**Algorithm:**

```text
Algorithm MergeSort(A, n)
1. if n > 1 then
2.     mid = n/2
3.     MergeSort(left half)
4.     MergeSort(right half)
5.     Merge(left, right)
```

**Recurrence:**
Each call splits into 2 subproblems of size `n/2`, plus merging cost `cn`.

[
T(n) = 2T(n/2) + c n
]

**Using Master Theorem:**

Form:
[
T(n) = aT(n/b) + f(n)
]
Here `a = 2`, `b = 2`, `f(n) = cn`

Compute:
[
n^{\log_b a} = n^{\log_2 2} = n^1 = n
]

Since (f(n) = Θ(n)),
→ **Case 2 of Master Theorem**

[
T(n) = Θ(n \log n)
]

✅ Merge Sort runs in **O(n log n)**.

---

### ⚙️ Example 4 — Tower of Hanoi

**Algorithm:**

```text
Algorithm TowerOfHanoi(n)
1. if n == 1 then move disk
2. else
3.     TowerOfHanoi(n−1)
4.     move disk
5.     TowerOfHanoi(n−1)
```

**Recurrence:**
[
T(n) = 2T(n-1) + 1
]
Base case: (T(1) = 1)

**Solve:**
[
T(n) = 2T(n-1) + 1
= 2[2T(n-2) + 1] + 1
= 2^2 T(n-2) + 2 + 1
= \dots = 2^{n-1} T(1) + (2^{n-1} - 1)
]

[
T(n) = 2^n - 1 = O(2^n)
]

✅ Exponential growth.

---

## 🔹 4. Summary Table

| Algorithm             | Recurrence Relation  | Solution   | Time Complexity |
| --------------------- | -------------------- | ---------- | --------------- |
| Factorial             | T(n)=T(n−1)+c        | O(n)       | Linear          |
| Binary Search         | T(n)=T(n/2)+c        | O(log n)   | Logarithmic     |
| Merge Sort            | T(n)=2T(n/2)+cn      | O(n log n) | Linearithmic    |
| Tower of Hanoi        | T(n)=2T(n−1)+1       | O(2ⁿ)      | Exponential     |
| Fibonacci (recursive) | T(n)=T(n−1)+T(n−2)+c | O(2ⁿ)      | Exponential     |

---

## 🔹 5. Graphical Comparison (Growth of T(n))

```
T(n) ↑
     |
     |                Exponential
     |             /
     |          /
     |       /      MergeSort (n log n)
     |    /  BinarySearch (log n)
     |  /
     | / Linear (n)
     |/ Constant
     +--------------------------→ n
```

---

## 🔹 6. Key Differences Between Recursive & Non-Recursive Analysis

| Aspect         | Non-Recursive        | Recursive                       |
| -------------- | -------------------- | ------------------------------- |
| Definition     | Executes in sequence | Calls itself with smaller input |
| Representation | Simple summation     | Recurrence relation             |
| Solving Method | Direct counting      | Recurrence solving              |
| Example        | Linear Search        | Merge Sort                      |
| Complexity     | Easy to derive       | Requires mathematical expansion |

---

## 🧠 Summary

| Concept                | Formula                         | Example                        |
| ---------------------- | ------------------------------- | ------------------------------ |
| Non-Recursive Analysis | Count basic operations directly | Linear Search, Loops           |
| Recursive Analysis     | Form recurrence relation        | Merge Sort, Binary Search      |
| Tools Used             | Summation formulas              | Recurrence, Master Theorem     |
| Goal                   | Express `T(n)` in Big-O form    | Compare algorithm growth rates |

---

# 🧠 **Introduction to Algorithm**

---

## 🔹 1. What is an Algorithm?

An **algorithm** is a **finite sequence of well-defined instructions** designed to perform a specific task or solve a particular problem.
It acts as a **step-by-step procedure** that transforms **input data** into **output results**.

### ✴ Formal Definition:

> “An algorithm is a finite set of instructions that, if followed, accomplish a particular task in a finite amount of time.”

---

## 🔹 2. Characteristics of an Algorithm

An algorithm must satisfy the following **five key properties** (often remembered as **FDEIT**):

| Property          | Description                                                                                           | Example                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Finiteness**    | The algorithm must terminate after a finite number of steps.                                          | A loop with a fixed number of iterations.                  |
| **Definiteness**  | Each step must be precisely and unambiguously defined.                                                | “Add A to B” is clear; “Do something with A and B” is not. |
| **Input**         | It must have zero or more well-defined inputs.                                                        | A sorting algorithm takes an array as input.               |
| **Output**        | It must produce one or more outputs.                                                                  | A sorted list or computed value.                           |
| **Effectiveness** | Every operation must be basic enough to be carried out by a computer or human using pencil and paper. | Basic arithmetic or comparison operations.                 |

---

## 🔹 3. Example of an Algorithm

Let’s consider a **simple example**:

### 🔸 Problem:

Find the largest number among three given numbers.

### 🔸 Algorithm (in English):

1. Start
2. Read three numbers: `A`, `B`, `C`
3. If `A > B` and `A > C`, then **A is largest**
4. Else if `B > A` and `B > C`, then **B is largest**
5. Else **C is largest**
6. Stop

### 🔸 Flowchart Representation:

```
          ┌────────────┐
          │   Start    │
          └────┬───────┘
               │
     ┌─────────▼─────────┐
     │ Read A, B, and C  │
     └─────────┬─────────┘
               │
       ┌───────▼──────────┐
       │ Is A > B & A > C │
       └───────┬──────────┘
           Yes  │   No
               ▼
         ┌─────────────┐
         │ A is largest│
         └─────────────┘
```

(Similarly, conditions for `B` and `C` follow.)

---

## 🔹 4. Representation of an Algorithm

Algorithms can be represented in multiple forms depending on clarity and purpose:

| Representation           | Description                                                      | Example                   |
| ------------------------ | ---------------------------------------------------------------- | ------------------------- |
| **Natural Language**     | Described in plain English.                                      | “Add A and B.”            |
| **Pseudocode**           | Structured description similar to code but language-independent. | `if A > B then print A`   |
| **Flowchart**            | Diagrammatic representation using symbols.                       | Used in algorithm design. |
| **Programming Language** | Actual implementation in C, Python, etc.                         | `if (A > B) printf("A");` |

---

## 🔹 5. Importance of Algorithms

| Reason              | Explanation                                                 |
| ------------------- | ----------------------------------------------------------- |
| **Efficiency**      | Optimized algorithms reduce time and memory usage.          |
| **Scalability**     | Efficient algorithms perform well even for large data.      |
| **Reusability**     | Algorithms can be used as building blocks for new problems. |
| **Maintainability** | Well-defined algorithms make debugging easier.              |

---

## 🔹 6. Classification of Algorithms (Basic Overview)

| Type                    | Description                                      | Example                |
| ----------------------- | ------------------------------------------------ | ---------------------- |
| **Brute Force**         | Try all possible solutions.                      | Linear Search          |
| **Divide and Conquer**  | Break into subproblems, solve recursively.       | Merge Sort, Quick Sort |
| **Greedy**              | Choose locally optimal solution.                 | Kruskal’s Algorithm    |
| **Dynamic Programming** | Store subproblem results to avoid recomputation. | Fibonacci using DP     |
| **Backtracking**        | Try and undo if the choice fails.                | N-Queens Problem       |
| **Randomized**          | Use random choices during computation.           | Randomized Quick Sort  |

---

## 🔹 7. Real-Life Example: Algorithm in Daily Life

**Example:** Making a cup of tea ☕
Algorithm:

1. Start
2. Boil water
3. Add tea leaves
4. Add sugar and milk
5. Stir and boil for 2 minutes
6. Strain into a cup
7. Stop

✅ Input: Water, tea leaves, sugar, milk
✅ Output: Cup of tea

---

## 🔹 8. Difference Between Algorithm and Program

| **Aspect**     | **Algorithm**           | **Program**                            |
| -------------- | ----------------------- | -------------------------------------- |
| Definition     | Step-by-step solution   | Implementation of an algorithm         |
| Representation | Pseudocode / Flowchart  | Code written in a programming language |
| Dependence     | Language independent    | Language dependent                     |
| Example        | Steps to find factorial | C/Python code using loops or recursion |

---

## 🔹 9. Conclusion

An **algorithm** is the **foundation of problem solving** in computer science.
It defines *how efficiently* a problem is solved, directly affecting:

* Performance of software,
* Use of system resources, and
* Scalability for large datasets.

Thus, learning algorithms is the first and most crucial step in becoming a **good programmer or computer scientist**.

---

# 🧠 **Pseudo Code for Expressing Algorithms**

---

## 🔹 1. What is Pseudocode?

**Pseudocode** is a **high-level, language-independent** description of an algorithm that uses a **structured format** similar to programming languages — but **without strict syntax**.

It is used to represent an algorithm **clearly and concisely**, making it easier to convert into any programming language (like C, Python, or Java).

---

### ⚙️ Definition:
> **Pseudocode** is an informal, human-readable way of describing the logic and steps of an algorithm, without worrying about syntax rules of a specific programming language.

---

## 🔹 2. Why Use Pseudocode?

| **Reason** | **Explanation** |
|-------------|----------------|
| **Language independence** | Works across all programming languages. |
| **Focus on logic** | Lets you think about *how* to solve the problem, not *how to write code*. |
| **Easy to read and understand** | Clear structure without complex syntax. |
| **Bridge between algorithm and program** | It helps in translating a design into code easily. |
| **Simplifies debugging and optimization** | Errors in logic can be found early before coding. |

---

## 🔹 3. Rules for Writing Good Pseudocode

Here are the **standard conventions** followed when writing pseudocode:

| **Aspect** | **Rule / Convention** | **Example** |
|-------------|----------------------|--------------|
| **Structure** | Write steps line by line, top to bottom. | Step 1 → Step 2 → Step 3 |
| **Keywords** | Use capitalized words for control structures. | `IF`, `THEN`, `ELSE`, `FOR`, `WHILE`, `END` |
| **Indentation** | Indent blocks to show hierarchy. | For loops, conditions, functions |
| **Comments** | Use comments to explain logic. | `// This line adds two numbers` |
| **Input/Output** | Use `READ`, `WRITE`, or `PRINT`. | `READ X`, `PRINT Result` |
| **Assignments** | Use `←` or `=` for assignment. | `Sum ← A + B` |
| **Conditionals** | Use `IF`, `ELSE IF`, `ELSE`. | `IF X > Y THEN ...` |
| **Loops** | Use `FOR`, `WHILE`, or `REPEAT`. | `FOR i ← 1 TO n DO ...` |

---

## 🔹 4. Basic Structure of a Pseudocode

```text
BEGIN
    Step 1: Initialize or input data
    Step 2: Perform computations or logic
    Step 3: Use loops or conditions if necessary
    Step 4: Display or return output
END
```

✅ **Note:**  
The pseudocode must start with a **BEGIN** and end with **END** (or `STOP`), ensuring **finiteness**.

---

## 🔹 5. Example 1 — Sum of Two Numbers

### 🔸 Problem:
Write pseudocode to find the sum of two numbers.

### 🔸 Pseudocode:

```
BEGIN
    READ A, B
    SUM ← A + B
    PRINT "Sum = ", SUM
END
```

✅ **Explanation:**  
- Inputs: A and B  
- Process: Add A and B  
- Output: Display the result  

---

## 🔹 6. Example 2 — Find the Largest of Three Numbers

```
BEGIN
    READ A, B, C
    IF A ≥ B AND A ≥ C THEN
        PRINT "A is the largest"
    ELSE IF B ≥ A AND B ≥ C THEN
        PRINT "B is the largest"
    ELSE
        PRINT "C is the largest"
    ENDIF
END
```

✅ **Control structures:**  
- Uses **IF–ELSE IF–ELSE** structure.  
- Logical operators like `AND`, `≥` are used.  

---

## 🔹 7. Example 3 — Sum of First N Natural Numbers (Using Loop)

```
BEGIN
    READ N
    SUM ← 0
    FOR i ← 1 TO N DO
        SUM ← SUM + i
    ENDFOR
    PRINT "Sum = ", SUM
END
```

✅ **Loop type:** `FOR` loop  
✅ **Variables:** `N`, `SUM`, and `i`  

---

## 🔹 8. Example 4 — Check Whether a Number is Even or Odd

```
BEGIN
    READ N
    IF N MOD 2 = 0 THEN
        PRINT "Even"
    ELSE
        PRINT "Odd"
    ENDIF
END
```

✅ **Operator Used:**  
- `MOD` → Gives remainder.  
- If remainder = 0, the number is even.  

---

## 🔹 9. Example 5 — Find Factorial of a Number (Using Loop)

```
BEGIN
    READ N
    FACT ← 1
    FOR i ← 1 TO N DO
        FACT ← FACT * i
    ENDFOR
    PRINT "Factorial = ", FACT
END
```

✅ **Logic:** Multiply all integers from 1 to N.  
✅ **Loop Type:** `FOR` loop  

---

## 🔹 10. Example 6 — Factorial Using Recursion

```
FUNCTION FACTORIAL(N)
    IF N = 0 OR N = 1 THEN
        RETURN 1
    ELSE
        RETURN N * FACTORIAL(N - 1)
    ENDIF
END FUNCTION
```

✅ **Demonstrates:**  
- **Recursive structure**  
- **Base case** (`N=0` or `N=1`)  
- **Recursive call** (`FACTORIAL(N-1)`)  

---

## 🔹 11. Example 7 — Linear Search (Array Example)

```
BEGIN
    READ N
    READ ARRAY A[1..N]
    READ ITEM
    FOUND ← FALSE
    FOR i ← 1 TO N DO
        IF A[i] = ITEM THEN
            PRINT "Item found at position ", i
            FOUND ← TRUE
            BREAK
        ENDIF
    ENDFOR
    IF FOUND = FALSE THEN
        PRINT "Item not found"
    ENDIF
END
```

✅ **Demonstrates:**  
- Array traversal  
- Looping and conditional checks  
- Flag variable for control  

---

## 🔹 12. Advantages of Pseudocode

| **Advantage** | **Explanation** |
|----------------|----------------|
| Easy to write and modify | Simple language and structure |
| Focuses on logic | Ignores syntax and technical details |
| Easier collaboration | Non-programmers can understand it |
| Step toward implementation | Can be easily converted into actual code |
| Useful for documentation | Describes what a program does without showing code |

---

## 🔹 13. Limitations of Pseudocode

| **Limitation** | **Explanation** |
|----------------|----------------|
| No standard syntax | Different people may write differently |
| Cannot be executed | Needs translation to real code |
| Ambiguity possible | Without strict format, misinterpretation may occur |
| Not suitable for complex systems | Hard to manage very large algorithms |

---

## 🔹 14. Conclusion

✅ **Pseudocode** serves as a bridge between **algorithmic thinking** and **actual programming**.  
It allows you to **design logic clearly**, debug early, and communicate algorithms effectively.

It’s one of the **most important tools** in algorithm design — used by developers, researchers, and students alike.

---

# 🧮 **Mathematics for Algorithmic Sets**

---

## 🔹 1. Introduction

Mathematics is the **foundation** of algorithm design and analysis.
Before we can analyze efficiency or correctness, we must understand the **mathematical tools** used to describe relationships, data groupings, and operations — particularly **Sets**, **Functions**, **Relations**, and **Matrices**.

Here we focus on the **Set theory** part, as this topic — *Mathematics for Algorithmic Sets* — deals with the **use of sets** in algorithmic design and problem-solving.

---

## 🔹 2. What is a Set?

> A **Set** is a well-defined collection of distinct objects.

These objects are called **elements** or **members** of the set.

**Example:**

* $A = {1, 2, 3, 4, 5}$ → A set of numbers.
* $B = {\text{red}, \text{green}, \text{blue}}$ → A set of colors.

---

## 🔹 3. Representation of Sets

| **Representation**   | **Example**                            | **Meaning**                                       |
| -------------------- | -------------------------------------- | ------------------------------------------------- |
| **Roster Form**      | $A = {2, 4, 6, 8, 10}$                 | Elements are explicitly listed.                   |
| **Set Builder Form** | $A = {x \mid x = 2n, 1 \leq n \leq 5}$ | Describes a rule that defines the set.            |
| **Venn Diagram**     | (Graphical)                            | Represents sets and their relationships visually. |

---

### 🧩 Example Diagram – Venn Representation

```
      _________
     |         |
     |   A     | = {1, 2, 3}
     |_________|
```

When we compare two sets (A and B), the Venn diagram helps to show **union, intersection, and difference**.

---

## 🔹 4. Important Set Terminology

| **Term**              | **Symbol** | **Meaning**                | **Example**     |
| --------------------- | ---------- | -------------------------- | --------------- |
| **Element of**        | ∈          | x belongs to A             | 2 ∈ {1,2,3}     |
| **Not an element of** | ∉          | x not in A                 | 5 ∉ {1,2,3}     |
| **Subset**            | ⊆          | All elements of A are in B | {1,2} ⊆ {1,2,3} |
| **Proper subset**     | ⊂          | A ⊆ B and A ≠ B            | {1,2} ⊂ {1,2,3} |
| **Superset**          | ⊇          | Opposite of subset         | {1,2,3} ⊇ {1,2} |
| **Universal set**     | U          | Contains all elements      | U = {1,2,3,4,5} |
| **Empty set**         | ∅          | Set with no elements       | ∅ = {}          |

---

## 🔹 5. Set Operations

Sets can be **combined or compared** using specific operations — important in algorithmic logic, searching, and data grouping.

| **Operation**            | **Symbol** | **Definition**                          | **Example**                            |
| ------------------------ | ---------- | --------------------------------------- | -------------------------------------- |
| **Union**                | A ∪ B      | Elements in A or B or both              | A={1,2,3}, B={3,4,5} → A∪B={1,2,3,4,5} |
| **Intersection**         | A ∩ B      | Elements common to both A and B         | {1,2,3} ∩ {2,3,4} = {2,3}              |
| **Difference**           | A − B      | Elements in A but not in B              | {1,2,3} − {2,3} = {1}                  |
| **Complement**           | A′         | Elements not in A (w.r.t universal set) | U={1,2,3,4}, A={1,2} → A′={3,4}        |
| **Symmetric Difference** | A ⊕ B      | Elements in either A or B, but not both | {1,2,3} ⊕ {3,4} = {1,2,4}              |

---

## 🔹 6. Laws of Set Operations (Important in Algorithm Design)

| **Law Name**         | **Formula**                     |
| -------------------- | ------------------------------- |
| **Commutative Law**  | A ∪ B = B ∪ A ; A ∩ B = B ∩ A   |
| **Associative Law**  | (A ∪ B) ∪ C = A ∪ (B ∪ C)       |
| **Distributive Law** | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| **Identity Law**     | A ∪ ∅ = A ; A ∩ U = A           |
| **Complement Law**   | A ∪ A′ = U ; A ∩ A′ = ∅         |
| **Idempotent Law**   | A ∪ A = A ; A ∩ A = A           |
| **Domination Law**   | A ∪ U = U ; A ∩ ∅ = ∅           |

These are used when simplifying logical expressions or algorithmic set operations.

---

## 🔹 7. Cardinality of a Set

> **Cardinality** means the **number of elements** in a set.

**Notation:** |A| = number of elements in set A.

**Example:**
If A = {2, 4, 6, 8}, then |A| = 4.

**Useful Relation:**
If A and B are finite sets:
$$
|A ∪ B| = |A| + |B| - |A ∩ B|
$$

---

## 🔹 8. Cartesian Product

> The **Cartesian Product** of two sets A and B is the set of all **ordered pairs (a, b)** where **a ∈ A** and **b ∈ B**.

**Notation:**
$A × B = {(a,b) \mid a ∈ A, b ∈ B}$

**Example:**
A = {1, 2}, B = {x, y}
Then,
A × B = {(1,x), (1,y), (2,x), (2,y)}

Used in algorithms to:

* Represent **relations**, **graphs**, and **matrices**.
* Define **edges** in directed graphs (vertex pairs).

---

## 🔹 9. Application of Sets in Algorithms

| **Area**                | **Use of Sets**                                  |
| ----------------------- | ------------------------------------------------ |
| **Searching**           | Represent data items as a set, check membership. |
| **Sorting**             | Maintain sets of sorted/unsorted elements.       |
| **Graph Theory**        | Vertices and edges represented as sets.          |
| **Database Systems**    | Relational model is based on sets.               |
| **Optimization**        | Used in constraint sets and feasible regions.    |
| **Dynamic Programming** | Subproblems represented as subsets.              |

---

## 🔹 10. Example — Using Sets in Algorithm

### Problem: Find the union and intersection of two arrays.

**Algorithm (in Pseudocode):**

```
BEGIN
    READ n, m
    READ Array A[n], B[m]
    UNION ← A
    FOR each element x in B DO
        IF x ∉ UNION THEN
            ADD x to UNION
        ENDIF
    ENDFOR

    INTERSECTION ← ∅
    FOR each element x in A DO
        IF x ∈ B THEN
            ADD x to INTERSECTION
        ENDIF
    ENDFOR

    PRINT UNION
    PRINT INTERSECTION
END
```

**Example Input:**
A = {1,2,3}, B = {3,4,5}

**Output:**
Union = {1,2,3,4,5}
Intersection = {3}

---

## 🔹 11. Real-Life Analogy

Think of:

* **Set A** = students who like coding.
* **Set B** = students who like gaming.
  Then:
* **A ∩ B** → students who like both.
* **A ∪ B** → students who like either coding or gaming or both.
* **A − B** → students who like only coding.

This same logic is used in **database queries**, **recommendation systems**, and **search algorithms**.

---

## 🔹 12. Summary Table

| **Concept**       | **Symbol** | **Example / Use**                     |
| ----------------- | ---------- | ------------------------------------- |
| Membership        | ∈          | 2 ∈ {1,2,3}                           |
| Subset            | ⊆          | {1,2} ⊆ {1,2,3}                       |
| Union             | ∪          | {1,2} ∪ {2,3} = {1,2,3}               |
| Intersection      | ∩          | {1,2,3} ∩ {2,3,4} = {2,3}             |
| Difference        | −          | {1,2,3} − {2} = {1,3}                 |
| Complement        | A′         | U={1,2,3,4}, A={1,2} → A′={3,4}       |
| Cartesian Product | ×          | {1,2}×{a,b}={(1,a),(1,b),(2,a),(2,b)} |

---

## ✅ **Conclusion**

Set theory is one of the most **fundamental mathematical tools** in algorithms.
It provides the **language and logic** for grouping data, comparing relationships, and defining **problems** in terms of **inputs, outputs, and constraints**.

Almost every algorithm — from **searching**, **sorting**, to **graph theory** — internally uses **set operations**.

---

# 🧮 **Functions and Relations**

---

## 🔹 1. Introduction

In the study of algorithms, **functions and relations** are mathematical tools used to **describe how inputs are mapped to outputs**, and how **data elements are related** to each other.

They are essential for:

* Understanding **algorithm behavior**
* Expressing **recurrence relations**
* Analyzing **time and space complexity**
* Defining **dependencies** between data elements (e.g., in graphs, sorting, searching)

---

## 🔹 2. What is a Relation?

> A **Relation (R)** is a **subset** of the **Cartesian product** of two sets.

If $A$ and $B$ are two sets,
then a **relation R from A to B** is:
$$
R ⊆ A × B
$$

That is, **R** consists of ordered pairs **(a, b)** where **a ∈ A** and **b ∈ B**, and **a is related to b** by R.

---

### 🧩 Example 1 — Relation Definition

Let
$A = {1, 2, 3}$,
$B = {4, 5, 6}$,

Define relation $R$ as:
“a is less than b”

So,
$$
R = {(1,4), (1,5), (1,6), (2,5), (2,6), (3,6)}
$$

✅ **Here**,

* $R ⊆ A×B$
* Each ordered pair shows a relationship “a < b”.

---

## 🔹 3. Types of Relations

Relations can have specific **properties** that describe their behavior.

| **Property**      | **Definition**                          | **Example**               |
| ----------------- | --------------------------------------- | ------------------------- |
| **Reflexive**     | Every element is related to itself.     | (a,a) ∈ R for all a ∈ A   |
| **Symmetric**     | If (a,b) ∈ R, then (b,a) ∈ R.           | Equality relation (=)     |
| **Antisymmetric** | If (a,b) ∈ R and (b,a) ∈ R ⇒ a = b.     | “≤” relation              |
| **Transitive**    | If (a,b) ∈ R and (b,c) ∈ R ⇒ (a,c) ∈ R. | “≤” or “divides” relation |

---

### 🧩 Example 2 — Check Relation Properties

Let $A = {1, 2, 3}$, and
$R = {(1,1), (2,2), (3,3), (1,2), (2,3), (1,3)}$

* Reflexive? ✅ yes (each element related to itself)
* Symmetric? ❌ no (1,2) ∈ R but (2,1) ∉ R
* Transitive? ✅ yes ((1,2),(2,3)) ⇒ (1,3) ∈ R

So R is **Reflexive and Transitive**, but not Symmetric.

---

## 🔹 4. Representation of Relations

Relations can be represented in **three ways**:

| **Type**                     | **Representation** | **Example**                  |
| ---------------------------- | ------------------ | ---------------------------- |
| **Set of Ordered Pairs**     | R = {(1,2), (2,3)} | Direct listing               |
| **Matrix Representation**    | Binary matrix      | R represented as 0’s and 1’s |
| **Directed Graph (Digraph)** | Nodes and arrows   | Shows connections visually   |

---

### 🧩 Example — Relation Matrix and Graph

Let $A = {1, 2, 3}$ and
$R = {(1,2), (2,3), (3,1)}$

**Matrix Representation:**

|   | 1 | 2 | 3 |
| - | - | - | - |
| 1 | 0 | 1 | 0 |
| 2 | 0 | 0 | 1 |
| 3 | 1 | 0 | 0 |

**Graphical Representation:**

```
(1) → (2)
 ↑     ↓
 (3) ←
```

Each arrow represents a pair in R.

---

## 🔹 5. Equivalence Relation

> A **relation R** on set A is called an **Equivalence Relation** if it is **Reflexive**, **Symmetric**, and **Transitive**.

**Example:**
Equality ( = ) relation on any set is an equivalence relation.

* a = a → Reflexive
* if a = b, then b = a → Symmetric
* if a = b and b = c, then a = c → Transitive

Equivalence relations partition the set into **equivalence classes**.

---

## 🔹 6. Partial and Total Order Relations

| **Type**          | **Condition**                                                  | **Example**         |
| ----------------- | -------------------------------------------------------------- | ------------------- |
| **Partial Order** | Reflexive, Antisymmetric, Transitive                           | “≤”, “divides”      |
| **Total Order**   | Partial order + Comparability (for all a,b, either aRb or bRa) | “≤” on real numbers |

Used in **sorting algorithms** — elements compared using total order relations.

---

## 🔹 7. What is a Function?

> A **Function (f)** is a **special kind of relation** between two sets **A** and **B**, where **every element of A** is related to **exactly one element of B**.

**Notation:**
$$
f : A → B
$$

**Meaning:** f maps each element from set A (domain) to one element in set B (codomain).

---

### 🧩 Example 1 — Function Definition

Let
A = {1, 2, 3},
B = {a, b, c},
and f = {(1,a), (2,b), (3,c)}

✅ Each element of A has **exactly one** image in B.
→ Hence f is a valid function.

❌ Example of invalid function:
f = {(1,a), (1,b)} → not valid, as 1 maps to more than one value.

---

## 🔹 8. Function Terminology

| **Term**      | **Meaning**                  | **Example**         |
| ------------- | ---------------------------- | ------------------- |
| **Domain**    | Set of all input values (A)  | {1,2,3}             |
| **Codomain**  | Set of possible outputs (B)  | {a,b,c,d}           |
| **Range**     | Actual outputs produced      | {a,b,c}             |
| **Image**     | Value f(x) for input x       | f(1) = a            |
| **Pre-image** | The input x for which f(x)=y | x is pre-image of y |

---

## 🔹 9. Types of Functions

| **Type**                   | **Condition**                                      | **Example**                      | **Diagram**                 |
| -------------------------- | -------------------------------------------------- | -------------------------------- | --------------------------- |
| **One-to-One (Injective)** | Each element of A maps to a unique element of B    | f(x)=x+1                         | A→B (no overlap in outputs) |
| **Onto (Surjective)**      | Every element of B has at least one pre-image in A | f(x)=x² on {-2,-1,0,1,2}→{0,1,4} | Covers full codomain        |
| **Bijective**              | Both one-to-one and onto                           | f(x)=x                           | Perfect pairing             |

---

### 🧩 Example:

Let A={1,2,3}, B={a,b,c}

* f₁ = {(1,a),(2,b),(3,c)} → **Bijective**
* f₂ = {(1,a),(2,a),(3,b)} → **Not injective**
* f₃ = {(1,a),(2,b)} → **Not surjective** (c has no preimage)

---

## 🔹 10. Composition of Functions

If
$f: A → B$ and $g: B → C$,
then **composition** $(g ∘ f): A → C$ is defined as:
$$
(g ∘ f)(x) = g(f(x))
$$

**Example:**

* f(x) = x + 1
* g(x) = 2x
  Then,
  (g ∘ f)(x) = g(f(x)) = 2(x + 1) = 2x + 2

---

## 🔹 11. Inverse of a Function

> The **inverse function** of f, denoted as $f^{-1}$, reverses the mapping — if $f(a)=b$, then $f^{-1}(b)=a$.

Exists **only for bijective functions**.

**Example:**
If f(x) = 2x + 3, then
$f^{-1}(x) = (x − 3)/2$

---

## 🔹 12. Functions in Algorithm Analysis

Functions are used to:

* Represent **running time**, e.g. $T(n) = n^2 + 3n + 5$
* Represent **memory use**, **growth**, or **recurrence relations**
* Define **asymptotic complexity**, e.g.
  $T(n) = O(f(n))$

### Example:

If $T(n) = 3n^2 + 2n + 1$,
we express it asymptotically as:
$$
T(n) = O(n^2)
$$

Thus, functions describe how **algorithm efficiency changes** with input size.

---

## 🔹 13. Real-World Analogy

Think of a **function** as a **machine**:

* You give it an input (from the domain)
* It performs an operation
* It gives one output (in the codomain)

```
   +-----------+
   |  f(x)=2x  |
   +-----------+
   Input: 3 → Output: 6
```

A **relation** could be a more general connection — e.g., “students and subjects they take” — one student can take many subjects.

---

## 🔹 14. Summary Table

| **Concept** | **Symbol/Condition**                 | **Example**                  |
| ----------- | ------------------------------------ | ---------------------------- |
| Relation    | R ⊆ A×B                              | {(1,2),(2,3)}                |
| Reflexive   | (a,a) ∈ R                            | ≤, ≥                         |
| Symmetric   | (a,b) ⇒ (b,a)                        | “=”                          |
| Transitive  | (a,b),(b,c) ⇒ (a,c)                  | “divides”                    |
| Function    | Each a∈A → one b∈B                   | f(x)=x+1                     |
| Injective   | Different inputs → different outputs | f(x)=2x                      |
| Surjective  | Every B value has preimage           | f(x)=x² (on suitable domain) |
| Bijective   | Injective + Surjective               | f(x)=x                       |
| Composition | (g∘f)(x)=g(f(x))                     | f(x)=x+1, g(x)=2x            |
| Inverse     | f⁻¹(f(x))=x                          | f(x)=2x → f⁻¹(x)=x/2         |

---

## ✅ **Conclusion**

* **Relations** describe **connections** between elements of sets.
* **Functions** are **special types of relations** with a one-to-one mapping from inputs to outputs.
* Both are **crucial mathematical tools** used in algorithms for:

  * Modeling relationships (graphs, dependencies)
  * Expressing computation rules
  * Analyzing algorithm efficiency (time functions, recurrences)

---

# 🧮 **Vectors and Matrices (in Algorithm Analysis)**

---

## 🔹 1. Introduction

In algorithm analysis, **vectors and matrices** are used to:

* Represent **data**,
* Express **relationships** between data elements, and
* Perform **mathematical operations** like transformation, optimization, and graph representation.

They play a critical role in fields like:

* Dynamic programming,
* Graph algorithms,
* Machine learning,
* Linear algebra–based computation (matrix multiplication, determinant, etc.).

---

## 🔹 2. What is a Vector?

A **vector** is an **ordered collection of numbers (scalars)** that can represent data, direction, or states.

### ✴ Representation:

A vector of size `n` can be written as:

$$
\vec{v} = [v_1, v_2, v_3, \ldots, v_n]
$$

### Example:

$$
\vec{v} = [3, 5, 7]
$$

Here:

* $v_1 = 3$, $v_2 = 5$, $v_3 = 7$
* It’s a **3-dimensional vector**

---

## 🔹 3. Types of Vectors

| Type              | Description                                       | Example                                   |
| ----------------- | ------------------------------------------------- | ----------------------------------------- |
| **Row Vector**    | Single row of elements                            | $[1, 2, 3]$                               |
| **Column Vector** | Single column of elements                         | $\begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}$ |
| **Zero Vector**   | All elements are zero                             | $\begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$ |
| **Unit Vector**   | Magnitude = 1                                     | $\hat{i} = [1, 0, 0]$                     |
| **Equal Vectors** | Two vectors are equal if all components are equal | $[2, 3] = [2, 3]$                         |

---

## 🔹 4. Vector Operations

| Operation                 | Description                         | Formula                                  | Example                                  |   |       |      |
| ------------------------- | ----------------------------------- | ---------------------------------------- | ---------------------------------------- | - | ----- | ---- |
| **Addition**              | Add corresponding elements          | $\vec{a} + \vec{b} = [a_1+b_1, a_2+b_2]$ | $[2,3]+[4,5]=[6,8]$                      |   |       |      |
| **Subtraction**           | Subtract corresponding elements     | $\vec{a} - \vec{b}$                      | $[4,5]-[2,1]=[2,4]$                      |   |       |      |
| **Scalar Multiplication** | Multiply each element by scalar $k$ | $k\vec{a} = [ka_1, ka_2]$                | $2[3,4]=[6,8]$                           |   |       |      |
| **Dot Product**           | $a \cdot b = \sum a_i b_i$          | $[1,2]\cdot[3,4]=11$                     |                                          |   |       |      |
| **Magnitude**             | $                                   | \vec{a}                                  | = \sqrt{a_1^2 + a_2^2 + \ldots + a_n^2}$ | $ | [3,4] | = 5$ |

---

## 🔹 5. Applications of Vectors in Algorithms

1. **Graph Representation:**

   * A graph with `n` nodes can be represented using an **adjacency vector**.
   * Example: neighbors of node `A = [1, 0, 1, 0]` (connected to 1st and 3rd nodes)

2. **Dynamic Programming:**

   * State values or subproblem solutions are often stored in **vectors**.

3. **Machine Learning Algorithms:**

   * Feature sets or input data are represented as vectors in *n-dimensional space*.

4. **Computational Geometry:**

   * Used for representing **points**, **directions**, or **positions** in 2D/3D.

---

## 🔹 6. What is a Matrix?

A **matrix** is a **rectangular array** of numbers arranged in **rows and columns**.

### ✴ Representation:

An $m \times n$ matrix:
$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & \ldots & a_{1n} \
a_{21} & a_{22} & a_{23} & \ldots & a_{2n} \
\vdots & \vdots & \vdots & \ddots & \vdots \
a_{m1} & a_{m2} & a_{m3} & \ldots & a_{mn}
\end{bmatrix}
$$

---

## 🔹 7. Types of Matrices

| Type                    | Description                     | Example                                      |
| ----------------------- | ------------------------------- | -------------------------------------------- |
| **Row Matrix**          | Single row                      | $[1\ 2\ 3]$                                  |
| **Column Matrix**       | Single column                   | $\begin{bmatrix}1 \ 2 \ 3\end{bmatrix}$      |
| **Square Matrix**       | Rows = Columns                  | $\begin{bmatrix}1 & 2 \ 3 & 4\end{bmatrix}$  |
| **Diagonal Matrix**     | Only diagonal elements non-zero | $\begin{bmatrix}5 & 0 \ 0 & 3\end{bmatrix}$  |
| **Identity Matrix (I)** | Diagonal = 1, rest = 0          | $\begin{bmatrix}1 & 0 \ 0 & 1\end{bmatrix}$  |
| **Zero Matrix**         | All zeros                       | $\begin{bmatrix}0 & 0 \ 0 & 0\end{bmatrix}$  |
| **Symmetric Matrix**    | $A = A^T$                       | $\begin{bmatrix}1 & 2 \ 2 & 3\end{bmatrix}$  |
| **Skew-Symmetric**      | $A = -A^T$                      | $\begin{bmatrix}0 & 2 \ -2 & 0\end{bmatrix}$ |

---

## 🔹 8. Matrix Operations

| Operation                 | Formula / Rule                    | Example                                                                                                             |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Addition**              | $(A + B)*{ij} = a*{ij} + b_{ij}$  | $\begin{bmatrix}1&2\3&4\end{bmatrix} + \begin{bmatrix}5&6\7&8\end{bmatrix} = \begin{bmatrix}6&8\10&12\end{bmatrix}$ |
| **Scalar Multiplication** | $(kA)*{ij} = k \times a*{ij}$     | $2\begin{bmatrix}1&2\3&4\end{bmatrix} = \begin{bmatrix}2&4\6&8\end{bmatrix}$                                        |
| **Matrix Multiplication** | $(AB)*{ij} = \sum_k a*{ik}b_{kj}$ | Shown below ↓                                                                                                       |

### Example of Matrix Multiplication

Let
$$
A =
\begin{bmatrix}
1 & 2 \
3 & 4
\end{bmatrix},
B =
\begin{bmatrix}
2 & 0 \
1 & 2
\end{bmatrix}
$$

Then:

$$
AB =
\begin{bmatrix}
(1×2 + 2×1) & (1×0 + 2×2) \
(3×2 + 4×1) & (3×0 + 4×2)
\end{bmatrix}
=============

\begin{bmatrix}
4 & 4 \
10 & 8
\end{bmatrix}
$$

---

## 🔹 9. Matrix Transpose and Determinant

* **Transpose ($A^T$):**
  Interchange rows and columns
  $A = \begin{bmatrix}1 & 2 \ 3 & 4\end{bmatrix} \Rightarrow A^T = \begin{bmatrix}1 & 3 \ 2 & 4\end{bmatrix}$

* **Determinant ($|A|$):**
  For 2×2 matrix
  $$
  \begin{vmatrix}a & b \ c & d\end{vmatrix} = ad - bc
  $$

---

## 🔹 10. Applications of Matrices in Algorithms

| Area                       | Use                                          |
| -------------------------- | -------------------------------------------- |
| **Graph Theory**           | Adjacency Matrix, Incidence Matrix           |
| **Dynamic Programming**    | Tabular storage of subproblems               |
| **Image Processing**       | Pixel representation as matrices             |
| **Machine Learning**       | Feature transformation & data representation |
| **Cryptography**           | Encryption using matrix transformations      |
| **Pathfinding Algorithms** | Floyd–Warshall uses matrix of distances      |

---

## 🔹 11. Example: Adjacency Matrix Representation (Graph)

For a graph with vertices A, B, C:

```
   A -- B
   |    |
   C---- 
```

|   | A | B | C |
| - | - | - | - |
| A | 0 | 1 | 1 |
| B | 1 | 0 | 1 |
| C | 1 | 1 | 0 |

This **matrix form** is used in algorithms like **Floyd-Warshall**, **Dijkstra**, and **Warshall’s Algorithm**.

---

## 🔹 12. Summary

| Concept                | Key Idea                                                  |
| ---------------------- | --------------------------------------------------------- |
| **Vector**             | 1D ordered list of values                                 |
| **Matrix**             | 2D array of numbers                                       |
| **Operations**         | Addition, scalar multiplication, matrix multiplication    |
| **Applications**       | Graphs, DP, ML, Image processing, Cryptography            |
| **Role in Algorithms** | Represent data relationships and computations efficiently |

---

# 🧮 **Linear Equations and Linear Inequalities**

These are fundamental mathematical tools for **analyzing algorithm performance**, **formulating optimization problems**, and **expressing constraints** in computational problems like shortest path, knapsack, or scheduling.

---

## 🔹 1. What is a Linear Equation?

A **linear equation** is an algebraic equation in which **each term is either a constant or the product of a constant and a single variable**.

The equation forms a **straight line** when plotted in 2D.

### ✴ General Form:

For one variable:
$$
ax + b = 0
$$

For two variables:
$$
ax + by = c
$$

For multiple variables:
$$
a_1x_1 + a_2x_2 + a_3x_3 + \ldots + a_nx_n = b
$$
where:

* $a_1, a_2, \ldots, a_n$ → coefficients
* $x_1, x_2, \ldots, x_n$ → variables
* $b$ → constant term

---

## 🔹 2. Example of Linear Equations

| Type            | Equation        | Description                            |
| --------------- | --------------- | -------------------------------------- |
| One Variable    | $3x + 9 = 0$    | Solving gives $x = -3$                 |
| Two Variables   | $2x + 3y = 8$   | Represents a straight line in XY-plane |
| Three Variables | $x + y + z = 6$ | Represents a plane in 3D space         |

---

## 🔹 3. System of Linear Equations

A **system of linear equations** is a collection of two or more linear equations involving the same set of variables.

### ✴ Example:

[
\begin{cases}
2x + y = 5 \
x - y = 1
\end{cases}
]

### 🔹 Solving Methods:

| Method                  | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| **Substitution Method** | Substitute value of one variable into another equation |
| **Elimination Method**  | Add/subtract equations to eliminate a variable         |
| **Matrix Method**       | Represent as $AX = B$ and compute $X = A^{-1}B$        |

---

### ✅ Matrix Representation Example

System:
[
\begin{cases}
2x + y = 5 \
x - y = 1
\end{cases}
]

Matrix form:

[
\underbrace{
\begin{bmatrix}
2 & 1 \
1 & -1
\end{bmatrix}
}*{A}
\underbrace{
\begin{bmatrix}
x \
y
\end{bmatrix}
}*{X}
=====

\underbrace{
\begin{bmatrix}
5 \
1
\end{bmatrix}
}_{B}
]

Then solution is:

[
X = A^{-1}B
]

---

## 🔹 4. What is a Linear Inequality?

A **linear inequality** is similar to a linear equation but uses **inequality symbols** (`<`, `>`, `≤`, `≥`) instead of `=`.

### ✴ General Form:

For one variable:
$$
ax + b < 0
$$
or
$$
ax + b \le 0
$$

For two variables:
$$
ax + by \le c
$$

---

## 🔹 5. Graphical Representation of Linear Inequality

Example:
[
x + y \le 4
]

1. First, draw the **boundary line** for $x + y = 4$.
2. The region **below** the line (since ≤) represents all valid points.

### ✴ Diagram:

```
y
↑
│      • (x + y = 4)
│     /
│    /
│   /
│__/_ _ _ _ _ _ _ _ _ _> x
   Feasible Region (≤)
```

The **shaded region** (below the line) represents the **solution set** of the inequality.

---

## 🔹 6. System of Linear Inequalities

When several inequalities are combined, the **common shaded region** that satisfies all conditions is called the **feasible region**.

### ✴ Example:

[
\begin{cases}
x + y \le 4 \
x \ge 0 \
y \ge 0
\end{cases}
]

The feasible region lies in the **first quadrant**, bounded by $x+y=4$.

---

## 🔹 7. Role in Algorithms and Optimization

Linear equations and inequalities are heavily used in **algorithm design** and **analysis**, especially in:

| Algorithm / Field       | Use                                          |
| ----------------------- | -------------------------------------------- |
| **Linear Programming**  | Objective and constraint formulation         |
| **Graph Algorithms**    | Representing network flow and shortest paths |
| **Machine Learning**    | Decision boundaries in SVM, regression       |
| **Scheduling Problems** | Representing task constraints                |
| **Dynamic Programming** | State relations often linear                 |
| **Complexity Analysis** | Recurrence relations (linear forms)          |

---

## 🔹 8. Example in Algorithmic Context

### Problem:

A company produces two products, P1 and P2.

* Profit for P1 = ₹30/unit, P2 = ₹20/unit
* Each unit requires:

  * 2 hours of labor
  * 3 units of material
* Available: 12 hours of labor, 18 units of material

### Formulate as Linear Equations/Inequalities:

Let:

* $x$ = units of P1
* $y$ = units of P2

Then:

| Constraint                  | Type       | Equation/Inequality      |
| --------------------------- | ---------- | ------------------------ |
| Labor constraint            | Inequality | $2x + 2y \le 12$         |
| Material constraint         | Inequality | $3x + 3y \le 18$         |
| Non-negativity              | Inequality | $x, y \ge 0$             |
| Profit (Objective Function) | Equation   | Maximize $Z = 30x + 20y$ |

✅ These are **linear inequalities** forming the **feasible region** in Linear Programming.

---

## 🔹 9. Solving Linear Inequalities in Algorithmic Context

### Steps:

1. Convert each condition into equation form (for boundary).
2. Plot all lines on graph.
3. Identify intersection points (vertices).
4. Evaluate objective function at each vertex.
5. Choose the one that gives **maximum or minimum value**.

This process is fundamental to **optimization algorithms** like:

* **Simplex Method**
* **Branch and Bound**
* **Dynamic Programming optimization**

---

## 🔹 10. Summary Table

| Concept             | Equation Type                   | Symbol Used  | Example                        | Used In                            |
| ------------------- | ------------------------------- | ------------ | ------------------------------ | ---------------------------------- |
| Linear Equation     | Equality                        | `=`          | $3x + 2y = 10$                 | Matrix algebra, recurrence solving |
| Linear Inequality   | Inequality                      | `<, >, ≤, ≥` | $2x + y ≤ 8$                   | Linear programming, constraints    |
| System of Equations | Multiple equations              | `=`          | $x + y = 2$, $2x - y = 3$      | Simultaneous solving               |
| Feasible Region     | Common solution of inequalities | -            | Intersection of shaded regions | Optimization problems              |

---

## 🔹 11. Key Takeaways

* **Linear equations** model exact relationships (equalities).
* **Linear inequalities** model constraints or limits.
* Both are crucial in **algorithm analysis**, **optimization**, and **problem formulation**.
* They form the **mathematical foundation** for topics like:

  * **Greedy algorithms**
  * **Dynamic programming**
  * **Linear programming**
  * **Branch & Bound**
  * **NP-completeness theory**

---

# **Analysis Framework in R (Big Data Context)**

An **analysis framework** in R defines the **structured process** or **workflow** used to analyze data — from collection to visualization and interpretation. It ensures consistency, reproducibility, and efficiency when working with datasets, especially large ones.

---

### **1. Purpose of an Analysis Framework**

* To **standardize** the process of data analysis.
* To make code **reusable** and **scalable**.
* To help in **debugging and reproducibility**.
* To make it easier to **document and share** the analysis process.

---

### **2. Typical Steps in an Analysis Framework**

#### **a. Data Acquisition**

* Collect or load data from sources like:

  * CSV, Excel, JSON
  * Databases (MySQL, PostgreSQL, etc.)
  * APIs or Web scraping
  * Big data systems (HDFS, Spark, etc.)

```R
data <- read.csv("sales.csv")
```

---

#### **b. Data Cleaning and Preprocessing**

* Handle **missing values**, **outliers**, and **inconsistent data**.
* Convert data types if needed.
* Normalize or standardize numerical values.
* Encode categorical data.

```R
data <- na.omit(data)        # Remove missing rows
data$category <- as.factor(data$category)
```

---

#### **c. Exploratory Data Analysis (EDA)**

* Understand data distribution using:

  * Summary statistics
  * Correlation and covariance
  * Visualization (histograms, boxplots, scatter plots)

```R
summary(data)
plot(data$sales, data$profit)
```

---

#### **d. Model Building**

* Apply **statistical** or **machine learning models**:

  * Linear Regression, Logistic Regression
  * ANOVA, T-tests, Clustering, etc.

```R
model <- lm(profit ~ sales + cost, data = data)
summary(model)
```

---

#### **e. Model Evaluation**

* Check model accuracy using metrics like:

  * $R^2$, MSE, RMSE for regression
  * Accuracy, Precision, Recall for classification

```R
pred <- predict(model, data)
mean((data$profit - pred)^2)
```

---

#### **f. Visualization and Reporting**

* Create statistical graphics using `ggplot2`, `plotly`, etc.
* Prepare dashboards or reports for insights.

```R
library(ggplot2)
ggplot(data, aes(x=sales, y=profit)) + geom_point() + geom_smooth(method="lm")
```

---

### **3. Tools Supporting Analysis Framework in R**

| Stage           | Common Packages                                |
| --------------- | ---------------------------------------------- |
| Data Collection | `readr`, `readxl`, `DBI`, `RMySQL`, `jsonlite` |
| Cleaning        | `dplyr`, `tidyr`, `stringr`                    |
| EDA             | `summarytools`, `ggplot2`, `corrplot`          |
| Modeling        | `stats`, `caret`, `glm`, `lm`                  |
| Reporting       | `knitr`, `rmarkdown`, `shiny`                  |

---

### **4. Advantages**

* Makes analysis **systematic** and **replicable**.
* Reduces errors due to inconsistency.
* Helps handle **large datasets** efficiently.
* Encourages **modular** and **scalable** R scripts.

---

### **Example Mini Framework in R**

```R
# Step 1: Load data
data <- read.csv("data.csv")

# Step 2: Clean data
data <- na.omit(data)

# Step 3: EDA
summary(data)

# Step 4: Model
model <- lm(Y ~ X1 + X2, data=data)
summary(model)

# Step 5: Visualization
plot(data$X1, data$Y)
abline(model)
```

---

### **In Summary**

> An **Analysis Framework** in R is a **structured workflow** for processing, analyzing, and interpreting data — ensuring the results are **accurate, reproducible, and scalable**.

---

# **Measuring and Input’s Size in R**

In data analysis, it’s essential to **understand the size and structure** of your data — how many rows, columns, and memory it uses.
This helps in optimizing performance, especially when dealing with **big data** in R.

---

## 🧩 **1. Measuring Input Size**

When you load a dataset into R (like a CSV or DataFrame), you can measure its **dimensions**, **structure**, and **memory usage**.

---

### **a. Checking the Dimensions of Data**

The number of **rows (observations)** and **columns (variables)**.

```R
# Example data
data <- read.csv("data.csv")

# Number of rows
nrow(data)

# Number of columns
ncol(data)

# Both rows and columns
dim(data)
```

**Example Output:**

```
[1] 1000 10
```

👉 means the dataset has 1000 rows and 10 columns.

---

### **b. Checking the Structure**

Displays the type of each column, number of entries, and a data preview.

```R
str(data)
```

**Output Example:**

```
'data.frame':  1000 obs. of  4 variables:
 $ Name  : chr  "John" "Mary" "Ali" ...
 $ Age   : int  25 30 22 ...
 $ Salary: num  50000 60000 45000 ...
 $ Dept  : Factor w/ 3 levels "HR","IT","Sales": 1 3 2 ...
```

---

### **c. Viewing Column Names and Data Types**

```R
colnames(data)      # Column names
sapply(data, class) # Type of each variable
```

---

## ⚖️ **2. Measuring Memory Size**

R stores all data in memory (RAM), so knowing how much space your data takes is crucial for performance.

---

### **a. Object Size**

```R
object.size(data)
```

Output (in bytes):

```
[1] 345678
```

You can make it more readable:

```R
print(object.size(data), units = "auto")
```

**Output:**

```
338.1 Kb
```

---

### **b. Memory Usage Summary**

Shows how much memory is used overall:

```R
memory.size()      # On Windows
memory.limit()     # Memory limit
```

For Linux/macOS:

```R
gc()               # Garbage collection info
```

---

## 🧮 **3. Measuring Input Size Before Loading**

When working with large files, it’s better to know their size before reading them into R.

### **a. Check File Size**

```R
file.info("data.csv")$size
```

**Readable format:**

```R
round(file.info("data.csv")$size / (1024*1024), 2)
```

→ gives size in **MB**

---

## 📏 **4. Example Workflow**

```R
# Load data
data <- read.csv("employees.csv")

# Measure size
cat("Rows:", nrow(data), "\n")
cat("Columns:", ncol(data), "\n")
cat("Memory:", format(object.size(data), units="auto"), "\n")

# Structure check
str(data)
```

**Output:**

```
Rows: 5000 
Columns: 8 
Memory: 2.1 Mb 
'data.frame': 5000 obs. of 8 variables
```

---

## ⚙️ **5. For Large Datasets**

When data is huge, use efficient packages:

| Task              | Package               | Description                    |
| ----------------- | --------------------- | ------------------------------ |
| Reading large CSV | `data.table::fread()` | Faster and memory efficient    |
| Memory inspection | `pryr::object_size()` | Better measurement than base R |
| Handling big data | `bigmemory`, `ff`     | Work with data larger than RAM |

Example:

```R
library(data.table)
data <- fread("bigdata.csv")
object.size(data)
```

---

## 🧠 **Summary**

| Task          | Function        | Purpose                |
| ------------- | --------------- | ---------------------- |
| Count rows    | `nrow()`        | Number of observations |
| Count columns | `ncol()`        | Number of variables    |
| Dimensions    | `dim()`         | Rows × Columns         |
| Structure     | `str()`         | Data type and preview  |
| Memory usage  | `object.size()` | Memory used by object  |
| File size     | `file.info()`   | Size before loading    |

---

**In short:**

> Measuring input size helps you understand how much data you’re working with, how it’s structured, and how efficiently R can handle it — a key step in any data analysis or big data workflow.

---

# 🕒 **Units for Measuring Running Time (Algorithm Analysis)**

When analyzing an algorithm, one of the most important factors is **how long it takes to run** — i.e., its **running time**.
However, instead of measuring the exact **physical time** (in seconds), we usually measure **abstract time units** that represent **how many basic operations** the algorithm performs.

Let’s go step-by-step 👇

---

## ⚙️ **1. What is Running Time?**

The **running time** of an algorithm is the **amount of time an algorithm takes to complete** its execution for a given input size.

For example:

* A sorting algorithm might take **1 second** to sort 1,000 elements.
* But **8 seconds** to sort 2,000 elements.

So, we analyze **how the running time grows with input size**.

---

## 🧮 **2. Two Ways to Measure Running Time**

| Type                            | Description                                                        | Example                                         |
| ------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------- |
| **Empirical (Actual Time)**     | Run the algorithm on a computer and measure time in seconds        | `time()` function in R or Python                |
| **Theoretical (Abstract Time)** | Count the number of fundamental operations independent of hardware | Counting statements, comparisons, or iterations |

---

### **a. Empirical Measurement (Real Time)**

Measured in **seconds**, **milliseconds (ms)**, or **microseconds (µs)** using built-in timers.

#### Example (in R):

```R
start <- Sys.time()

# Algorithm - Example: sum of numbers
sum <- 0
for (i in 1:1000000) {
  sum <- sum + i
}

end <- Sys.time()
runtime <- end - start
print(runtime)
```

**Output:**

```
Time difference of 0.14 secs
```

🕐 Here, R measured the **actual running time**.

---

### **b. Theoretical Measurement (Abstract Units)**

Instead of seconds, we use **abstract units** to measure **how many basic steps** (like additions, comparisons, assignments) are performed.

Example:

```c
sum = 0;              // 1 step
for (i = 1; i <= n; i++)  // n steps
    sum = sum + i;        // n steps
```

**Total steps = 1 + n + n = 2n + 1**

So, time complexity is proportional to **2n + 1 ≈ O(n)**.
→ This is the **unit-independent measurement** of algorithm time.

---

## 🧭 **3. Common Units for Measuring Running Time**

| Unit                 | Meaning                                | Example                     |
| -------------------- | -------------------------------------- | --------------------------- |
| **Second (s)**       | Standard base unit                     | 1 s = 1000 ms               |
| **Millisecond (ms)** | 1/1000 of a second                     | 0.001 s                     |
| **Microsecond (µs)** | 1/1,000,000 of a second                | 0.000001 s                  |
| **Nanosecond (ns)**  | 1/1,000,000,000 of a second            | 0.000000001 s               |
| **CPU Cycle**        | One tick of the processor clock        | Hardware-dependent          |
| **Operation Count**  | Theoretical unit — one basic operation | Used in asymptotic analysis |

---

## ⚖️ **4. Why Abstract Units Are Preferred**

| Physical Time (seconds)                | Abstract Time (operations)    |
| -------------------------------------- | ----------------------------- |
| Depends on CPU speed, compiler, and OS | Independent of hardware       |
| Difficult to compare between systems   | Same across all systems       |
| Not scalable                           | Scales easily with input size |

🧠 Therefore, in **algorithm analysis**, we usually measure **running time in terms of number of operations**, not seconds.

---

## 📊 **5. Measuring Running Time in R**

### Example 1: Simple operation

```R
system.time({
  x <- 0
  for (i in 1:1000000) {
    x <- x + i
  }
})
```

**Output:**

```
   user  system elapsed 
  0.121   0.003   0.125 
```

| Field       | Meaning                        |
| ----------- | ------------------------------ |
| **user**    | Time spent by CPU in user mode |
| **system**  | Time spent by OS kernel        |
| **elapsed** | Total real-world time          |

---

### Example 2: Compare two algorithms

```R
n <- 10000
x <- runif(n)

system.time(sort(x))     # Built-in sort
system.time(for (i in 1:(n-1)) for (j in 1:(n-i)) if (x[j] > x[j+1]) tmp <- x[j])  # Manual bubble sort
```

You’ll see built-in `sort()` is **much faster** — it has **O(n log n)** complexity versus **O(n²)** for bubble sort.

---

## 🧠 **6. Summary**

| Concept                     | Description                                | Example                       |
| --------------------------- | ------------------------------------------ | ----------------------------- |
| **Empirical measurement**   | Time in seconds/milliseconds               | `system.time()` in R          |
| **Theoretical measurement** | Number of basic operations                 | Count comparisons/assignments |
| **Preferred for analysis**  | Theoretical (independent of hardware)      | Big O, Ω, Θ notation          |
| **Common units**            | s, ms, µs, ns, CPU cycles, operation count | 1 ms = 0.001 s                |

---

✅ **In short:**

> * The *running time* of an algorithm can be measured either **empirically** (seconds) or **theoretically** (operation counts).
> * In algorithm analysis, we usually use **abstract units** like the number of basic operations — because they are **hardware-independent** and give a true measure of algorithmic efficiency.

---

# 📈 **Order of Growth (in Algorithm Analysis)**

When analyzing algorithms, we are interested in **how the running time increases** as the **input size (n)** grows.
This relationship is called the **Order of Growth** — it helps us understand how efficiently an algorithm scales.

---

## 🧠 **1. Definition**

> **Order of Growth** describes how the **running time** (or **space**) of an algorithm **changes with the size of input**.

It focuses on the **rate of growth** — not the exact time.

---

### 🔹 Example

Suppose two algorithms take the following number of steps:

| Input size (n) | Algorithm A steps | Algorithm B steps |
| -------------- | ----------------- | ----------------- |
| 10             | 100               | 5                 |
| 100            | 10,000            | 500               |
| 1000           | 1,000,000         | 50,000            |

✅ Both grow with $n^2$ → so both have **O(n²)** order of growth.
Even if one runs faster in practice, both scale the same way.

---

## ⚙️ **2. Why It Matters**

* Helps compare algorithms **independent of hardware**.
* Predicts **performance for large inputs**.
* Simplifies analysis using **asymptotic notations** (Big O, Ω, Θ).
* Focuses on **dominant terms** that matter as $n \to \infty$.

---

## 📏 **3. How to Determine the Order of Growth**

We analyze the **dominant term** in the time complexity expression —
the one that grows fastest as `n` increases.

---

### 🔹 Example 1: Linear Growth

```c
for (i = 0; i < n; i++)
    sum = sum + i;
```

* Executes `n` times → **O(n)**
* **Order of Growth:** Linear

---

### 🔹 Example 2: Quadratic Growth

```c
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        sum = sum + i + j;
```

* Executes `n × n = n²` times → **O(n²)**
* **Order of Growth:** Quadratic

---

### 🔹 Example 3: Logarithmic Growth

```c
i = 1;
while (i < n) {
    i = i * 2;
}
```

* Number of iterations = log₂(n) → **O(log n)**
* **Order of Growth:** Logarithmic

---

### 🔹 Example 4: Exponential Growth

```c
function fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```

* Calls grow roughly as $2^n$ → **O(2ⁿ)**
* **Order of Growth:** Exponential

---

## 📊 **4. Common Orders of Growth**

| Growth Rate  | Time Complexity | Example Algorithm                | Growth Behavior      |
| ------------ | --------------- | -------------------------------- | -------------------- |
| Constant     | **O(1)**        | Accessing array element          | 🔹 Fastest           |
| Logarithmic  | **O(log n)**    | Binary Search                    | ⚙️ Very efficient    |
| Linear       | **O(n)**        | Linear Search                    | 📈 Moderate          |
| Linearithmic | **O(n log n)**  | Merge Sort, Quick Sort           | 🔄 Efficient sorting |
| Quadratic    | **O(n²)**       | Bubble Sort, Insertion Sort      | 🐢 Slower            |
| Cubic        | **O(n³)**       | Matrix multiplication            | 🐌 Very slow         |
| Exponential  | **O(2ⁿ)**       | Recursive Fibonacci              | 🚫 Extremely slow    |
| Factorial    | **O(n!)**       | Traveling Salesman (Brute force) | ❌ Impractical        |

---

### 📈 **Graphical View**

```
Growth Rate vs Input Size (n)
|
|                  O(2ⁿ)
|              O(n²)
|         O(n log n)
|     O(n)
|  O(log n)
| O(1)
+---------------------------------> n
```

As input grows, algorithms with higher orders (like $O(2^n)$) **explode** in runtime.

---

## 🧮 **5. Practical Example**

Let’s analyze this code:

```c
for (i = 0; i < n; i++)        // runs n times
    for (j = 0; j < 1000; j++) // runs 1000 times
        sum = sum + i + j;
```

Total steps = `n × 1000 = 1000n` → Dominant term is `n`.

✅ **Order of Growth = O(n)** (constant multipliers like 1000 are ignored).

---

## 🧠 **6. Focus on Dominant Term**

If $T(n) = 5n^3 + 2n^2 + 8n + 10$

Then:

* As $n$ increases, $5n^3$ dominates.
* So, **Order of Growth = O(n³)**

---

## ⚖️ **7. Example Comparison Table**

| Algorithm             | Time Complexity | Order of Growth | Comments                |
| --------------------- | --------------- | --------------- | ----------------------- |
| Linear Search         | O(n)            | Linear          | Scans each element      |
| Binary Search         | O(log n)        | Logarithmic     | Divides input each time |
| Bubble Sort           | O(n²)           | Quadratic       | Nested loops            |
| Merge Sort            | O(n log n)      | Linearithmic    | Divide and conquer      |
| Fibonacci (Recursive) | O(2ⁿ)           | Exponential     | Very slow               |

---

## 🔍 **8. Summary**

| Concept               | Meaning                                      |
| --------------------- | -------------------------------------------- |
| **Order of Growth**   | How runtime increases with input size        |
| **Dominant Term**     | Highest-degree term decides growth           |
| **Ignored constants** | 5n and n are both O(n)                       |
| **Goal**              | Choose algorithms with smaller growth orders |

---

✅ **In short:**

> The **Order of Growth** gives a mathematical model of how an algorithm’s running time increases with input size `n`.
> It helps classify algorithms into efficiency classes such as **O(1)**, **O(log n)**, **O(n)**, **O(n log n)**, **O(n²)**, etc.

---

# ⚠️ **Worst-Case Efficiency (Algorithm Analysis)**

When analyzing an algorithm, we often want to know **how bad things can get** —
that is, how much **time or space** the algorithm will need **in the worst possible situation**.
This is called **Worst-Case Efficiency**.

---

## 🧠 **1. Definition**

> **Worst-case efficiency** refers to the **maximum amount of time or space** an algorithm will take **for any input of size n**.

In other words,
it measures the **upper bound** on how long the algorithm could take to finish.

---

### 🔹 Example (Conceptual)

If an algorithm takes:

* 1 ms for best input,
* 10 ms for average input,
* 50 ms for worst input,
  then the **worst-case running time = 50 ms**.

---

## 🧮 **2. Why We Need Worst-Case Analysis**

| Reason             | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Reliability**    | Guarantees that the algorithm will never exceed this time.                                  |
| **Predictability** | Helps in designing systems that must respond within strict limits (like real-time systems). |
| **Comparison**     | Provides a standard baseline to compare algorithms fairly.                                  |

---

## ⚙️ **3. Formal Definition**

Let $T(n)$ = running time of an algorithm for input size $n$.

Then:
[
T_{worst}(n) = \max_{all\ inputs\ of\ size\ n} \ T(n)
]

That is — it’s the **maximum** running time among all inputs of size `n`.

---

## 🔍 **4. Example 1: Linear Search**

### **Algorithm:**

```c
int linear_search(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}
```

### **Analysis:**

| Case             | Description                   | Comparisons |
| ---------------- | ----------------------------- | ----------- |
| **Best Case**    | Key found at first position   | 1           |
| **Average Case** | Key somewhere in the middle   | n/2         |
| **Worst Case**   | Key not found or last element | n           |

✅ So, **Worst-Case Efficiency:**
[
T_{worst}(n) = O(n)
]

---

## 🔍 **5. Example 2: Binary Search**

```c
int binary_search(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

| Case           | Description          | Comparisons           |
| -------------- | -------------------- | --------------------- |
| **Best Case**  | Key is at the middle | 1                     |
| **Worst Case** | Key not in array     | log₂n (approximately) |

✅ **Worst-Case Efficiency:**
[
T_{worst}(n) = O(\log n)
]

---

## 📊 **6. Graphical Representation**

```
Running Time ↑
|
|                Worst-case (max)
|                *
|              *   
|            *
|          *
|       *
|    *
|__*______________________________→ Input size (n)
```

The **worst-case curve** always lies **above** average and best cases.

---

## 🧩 **7. Example: Sorting Algorithms**

| Algorithm      | Best Case  | Average Case | **Worst Case** | Notes                              |
| -------------- | ---------- | ------------ | -------------- | ---------------------------------- |
| Bubble Sort    | O(n)       | O(n²)        | **O(n²)**      | Worst when array is reverse sorted |
| Merge Sort     | O(n log n) | O(n log n)   | **O(n log n)** | Always consistent                  |
| Quick Sort     | O(n log n) | O(n log n)   | **O(n²)**      | Worst when pivot is poorly chosen  |
| Insertion Sort | O(n)       | O(n²)        | **O(n²)**      | Worst when array is reverse sorted |
| Binary Search  | O(1)       | O(log n)     | **O(log n)**   | Sorted data required               |
| Linear Search  | O(1)       | O(n/2)       | **O(n)**       | Works on unsorted data             |

---

## 🧮 **8. Mathematical Representation**

If $T(n)$ represents total steps of an algorithm,
and $C_i$ represents cost of each operation,
then:

[
T(n) = C_1 \cdot f_1(n) + C_2 \cdot f_2(n) + \dots + C_k \cdot f_k(n)
]

For worst-case analysis,
we only consider the **largest possible $T(n)$** for all valid inputs of size `n`.

---

## ⚖️ **9. Relation to Other Efficiencies**

| Type                        | Description                        | Example                                         |
| --------------------------- | ---------------------------------- | ----------------------------------------------- |
| **Best-Case Efficiency**    | Minimum running time for any input | Binary Search finds element at first mid → O(1) |
| **Average-Case Efficiency** | Expected time for random input     | O(log n) for Binary Search                      |
| **Worst-Case Efficiency**   | Maximum time over all inputs       | O(log n) for Binary Search                      |

---

## 🧠 **10. Summary**

| Feature        | Explanation                                                               |
| -------------- | ------------------------------------------------------------------------- |
| **Definition** | Maximum running time for any input of size n                              |
| **Purpose**    | Provides guaranteed performance limit                                     |
| **Notation**   | Represented using Big-O notation                                          |
| **Examples**   | O(n) for Linear Search, O(log n) for Binary Search                        |
| **Used in**    | Real-time, critical, and secure systems (where predictability is crucial) |

---

✅ **In short:**

> **Worst-case efficiency** measures the **maximum possible time** an algorithm can take for input size `n`.
> It provides a **guaranteed upper bound** on running time and is expressed using **Big O notation**.

---

# ⚡ **Best-Case Efficiency (Algorithm Analysis)**

When analyzing algorithms, we often want to know how **fast** they can possibly run —
that is, the **minimum amount of time or space** an algorithm will take under the **most favorable input conditions**.
This is called **Best-Case Efficiency**.

---

## 🧠 **1. Definition**

> **Best-case efficiency** measures the **minimum running time** (or space) an algorithm takes for **any input of size n**.

Formally, if $T(n)$ is the running time of an algorithm, then:

[
T_{\text{best}}(n) = \min_{\text{all inputs of size } n} \ T(n)
]

It represents the **lower bound** of the algorithm’s performance.

---

## 💡 **2. Why It Matters**

| Reason                  | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **Optimistic analysis** | Shows how efficient the algorithm can be under perfect conditions        |
| **Useful for**          | Understanding algorithm’s behavior on *sorted, trivial, or small inputs* |
| **Not always reliable** | Real inputs are rarely best-case, so it’s used mainly for reference      |

---

## 🧩 **3. Example 1: Linear Search**

```c
int linear_search(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}
```

### **Analysis:**

* If `key` is found at **first position**, only **1 comparison** is made.

✅ **Best-case time:** $T_{best}(n) = O(1)$
⏱️ Only one operation — immediate success.

---

## 🧩 **4. Example 2: Bubble Sort**

```c
for (i = 0; i < n-1; i++)
    for (j = 0; j < n-i-1; j++)
        if (a[j] > a[j+1])
            swap(a[j], a[j+1]);
```

### **Analysis:**

* **Best case:** When array is already sorted.
* If algorithm includes an **optimization check** (flag to stop early), it will make only one pass and stop.

✅ **Best-case time:**
[
T_{best}(n) = O(n)
]

Without optimization, even a sorted array would take **O(n²)** (since all passes run).

---

## 🧩 **5. Example 3: Insertion Sort**

```c
for (i = 1; i < n; i++) {
    key = a[i];
    j = i - 1;
    while (j >= 0 && a[j] > key) {
        a[j + 1] = a[j];
        j--;
    }
    a[j + 1] = key;
}
```

### **Analysis:**

* If array is already sorted → no shifting happens.
* Inner loop executes **zero times** per element.

✅ **Best-case time:**
[
T_{best}(n) = O(n)
]

---

## 🧮 **6. Mathematical Definition**

Let $T(n)$ be the number of basic operations for input size `n`.
Then:
[
T_{best}(n) = \min_{\text{inputs of size } n} T(n)
]
and it represents the **lower bound** of runtime.

---

## 📊 **7. Graphical Comparison**

```
Running Time ↑
|
|      Worst Case
|           *
|         *
|       *
|     *
|   *
| *     ← Best Case
+--------------------------→ Input size (n)
```

The **best-case curve** is always **below** the average and worst-case curves.

---

## ⚙️ **8. Example: Sorting Algorithms Comparison**

| Algorithm          | Best Case  | Average Case | Worst Case | Remarks                     |
| ------------------ | ---------- | ------------ | ---------- | --------------------------- |
| **Bubble Sort**    | O(n)       | O(n²)        | O(n²)      | If optimized                |
| **Insertion Sort** | O(n)       | O(n²)        | O(n²)      | Already sorted input        |
| **Merge Sort**     | O(n log n) | O(n log n)   | O(n log n) | Same in all cases           |
| **Quick Sort**     | O(n log n) | O(n log n)   | O(n²)      | Best pivot choice           |
| **Selection Sort** | O(n²)      | O(n²)        | O(n²)      | No improvement in best case |

---

## ⚖️ **9. Relation to Other Efficiencies**

| Case             | Meaning               | Formula        | Example                                 |
| ---------------- | --------------------- | -------------- | --------------------------------------- |
| **Best Case**    | Minimum running time  | $T_{best}(n)$  | Already sorted array for Insertion Sort |
| **Average Case** | Expected running time | $T_{avg}(n)$   | Random array                            |
| **Worst Case**   | Maximum running time  | $T_{worst}(n)$ | Reverse sorted array for Insertion Sort |

---

## 🧠 **10. Key Points to Remember**

✅ **Best-case efficiency** gives the *fastest possible* performance.
⚙️ Often used to show the *theoretical lower limit*.
📊 Usually expressed in **Big Ω notation (Omega)** — meaning *lower bound*.
💡 But, **real-world performance** is better represented by **average case**.

---

### 💬 **Example Summary Table**

| Algorithm      | Best-Case Condition  | Best-Case Complexity |
| -------------- | -------------------- | -------------------- |
| Linear Search  | Key at first index   | O(1)                 |
| Binary Search  | Key at middle        | O(1)                 |
| Bubble Sort    | Already sorted array | O(n)                 |
| Quick Sort     | Ideal pivot          | O(n log n)           |
| Merge Sort     | Any input            | O(n log n)           |
| Insertion Sort | Already sorted       | O(n)                 |

---

✅ **In short:**

> **Best-case efficiency** measures the **minimum time** an algorithm will take under **ideal input conditions**.
> It represents the **lower bound** of performance and is typically expressed using **Ω (Omega) notation**.

---

# **Average-Case Efficiency**

---

## 🧩 **1. Introduction**

While **worst-case efficiency** measures the maximum time an algorithm can take and **best-case efficiency** measures the minimum time, **average-case efficiency** gives a more realistic view of how an algorithm performs **on average**, across all possible inputs.

It helps us understand the algorithm’s **expected performance in practical use**, rather than in extreme cases.

---

## ⚙️ **2. Definition**

**Average-case efficiency** measures the **expected running time (or space)** of an algorithm over **all possible inputs** of a given size, assuming each input occurs with some probability.

Formally, if there are ( n ) possible inputs of size ( N ), and

* ( T(I_i) ) = time for input ( I_i )
* ( P(I_i) ) = probability of input ( I_i )

then the **average-case time** is:

[
T_{avg}(N) = \sum_{i=1}^{n} T(I_i) \times P(I_i)
]

If all inputs are equally likely, ( P(I_i) = \frac{1}{n} ), then:

[
T_{avg}(N) = \frac{1}{n} \sum_{i=1}^{n} T(I_i)
]

---

## 📘 **3. Why Average-Case Analysis is Important**

| Type             | Description                     | Usage                             |
| ---------------- | ------------------------------- | --------------------------------- |
| **Best Case**    | Minimum time algorithm can take | Rare in practice                  |
| **Worst Case**   | Maximum time algorithm can take | Good for guarantees               |
| **Average Case** | Expected time over all inputs   | Realistic performance expectation |

Most real-world users care about **average performance**, since worst-case inputs rarely occur.

---

## 🧮 **4. Example 1: Linear Search**

**Problem:** Search for element `x` in array `A[1..n]`.

### **Algorithm**

```pseudo
LinearSearch(A, x)
  for i ← 1 to n do
      if A[i] = x then
          return i
  return -1
```

### **Case 1: Element found**

If the element `x` is equally likely to be in any position:

Average number of comparisons:

[
C_{avg} = \frac{1 + 2 + 3 + ... + n}{n} = \frac{n + 1}{2}
]

### **Case 2: Element not found**

Requires `n` comparisons.

If probability that `x` is in the array = `p`, and not in array = `1 - p`,
then:

[
C_{avg} = p \times \frac{n + 1}{2} + (1 - p) \times n
]

If `p = 1` (always found), average = ( \frac{n+1}{2} )
If `p = 0` (never found), average = ( n )

---

## 🧮 **5. Example 2: Binary Search**

For binary search on a sorted array:

At each step, the array size is halved.

Average number of comparisons ≈ **O(log n)**

> So, even in average case, binary search is logarithmic — making it very efficient.

---

## 📊 **6. Graphical Representation**

```
| Time
|        .
|       . \
|      .   \   Average Case
|     .     \
|----.-------\--------------------> Input size (n)
|    |        \
| Best Case    Worst Case
```

* **Best case:** smallest time (element found at start).
* **Average case:** mid behavior.
* **Worst case:** largest time (element found at end or not found).

---

## 🧠 **7. Key Insights**

* Average-case gives **expected performance**.
* Requires knowledge of **input distribution** (probabilities).
* Often hard to compute precisely.
* Useful for **probabilistic or randomized algorithms** (like QuickSort).

---

## ⚖️ **8. Comparison Summary**

| Criterion                    | Best Case            | Worst Case               | Average Case       |
| ---------------------------- | -------------------- | ------------------------ | ------------------ |
| **Meaning**                  | Fastest execution    | Slowest execution        | Expected execution |
| **Example in Linear Search** | Found at 1st element | Not found / last element | Found in middle    |
| **Notation**                 | Ω (Omega)            | O (Big O)                | Θ (Theta)          |
| **Practical Relevance**      | Low                  | Medium                   | High               |

---

## 🧩 **9. Example: QuickSort**

| Case    | Partitioning Quality                 | Time Complexity |
| ------- | ------------------------------------ | --------------- |
| Best    | Equal halves                         | O(n log n)      |
| Average | Random partitions                    | O(n log n)      |
| Worst   | One side empty (already sorted data) | O(n²)           |

Even though the worst case is bad, the **average case is excellent**, which is why QuickSort is often used in practice.

---

## 🏁 **10. Conclusion**

* **Average-case efficiency** provides a **realistic estimate** of algorithm performance.
* It depends on **input distribution** and **expected behavior**.
* For many algorithms (e.g., QuickSort, Hashing), average case is the **most meaningful measure** of efficiency.

---

# **Performance Analysis**

---

## 🧩 **1. Introduction**

**Performance Analysis** is the process of determining how efficient an algorithm is in terms of the **resources** it uses.

There are two main resources to measure:

1. **Time** – How long the algorithm takes to execute.
2. **Space** – How much memory the algorithm uses.

So, **Performance Analysis = Time Complexity + Space Complexity**

---

## ⚙️ **2. What Is Performance Analysis?**

When we analyze an algorithm, we want to know **how it behaves** as the input size grows.
This helps us choose the best algorithm for a given problem.

> 📘 **Definition:**
> Performance analysis is the process of evaluating an algorithm by **estimating the computational and memory resources** required for its execution.

---

## 📏 **3. Categories of Performance**

| Type                         | Description                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| **Compile-Time Performance** | Time taken by the compiler to translate the program into executable code. |
| **Run-Time Performance**     | Time taken by the program to execute the algorithm with actual input.     |
| **Space Performance**        | Memory consumed during the execution of the program.                      |

Usually, we focus on **run-time** and **space** performance.

---

## 🧮 **4. Factors Affecting Performance**

1. **Algorithm Design** – The logic and approach (e.g., sorting by comparing vs. counting).
2. **Input Size (n)** – The number of elements or data points.
3. **Hardware/Software** – CPU speed, memory size, compiler optimizations.
4. **Programming Language & Compiler** – Affect constant factors but not growth order.
5. **Implementation Details** – Data structures and coding style.

---

## 🔍 **5. Performance Metrics**

Two main metrics:

### 🕒 **A. Time Complexity**

Measures the total time an algorithm takes to complete, as a function of input size ( n ).

We usually measure **number of primitive operations** rather than actual seconds, since seconds depend on hardware.

Formally:

[
T(n) = \text{Number of operations as a function of input size } n
]

### 💾 **B. Space Complexity**

Measures how much memory is required by the algorithm during execution.

Includes:

* Memory for variables
* Memory for constants
* Input/output storage
* Recursion stack or dynamic memory

Formally:

[
S(n) = \text{Memory units used as a function of input size } n
]

---

## 📊 **6. Example: Linear Search**

### **Algorithm**

```pseudo
LinearSearch(A, n, x)
  for i ← 1 to n do
      if A[i] = x then
          return i
  return -1
```

### **Time Analysis**

| Operation              | Count |
| ---------------------- | ----- |
| Initialization (i=1)   | 1     |
| Comparison `i <= n`    | n + 1 |
| Comparison `A[i] == x` | n     |
| Increment `i++`        | n     |
| Return                 | 1     |

[
T(n) = 1 + (n + 1) + n + n + 1 = 3n + 3
]

So, **time complexity = O(n)**.

### **Space Analysis**

Memory used:

* Array `A[n]` → O(n)
* Variables `i`, `x`, `n` → O(1)

Total space = O(n + 1) = **O(n)**

---

## 🧠 **7. Components of Performance Analysis**

| Component                    | Description                                                    |
| ---------------------------- | -------------------------------------------------------------- |
| **Input Size (n)**           | Measure of the problem (e.g., number of items to sort).        |
| **Basic Operation**          | The operation contributing most to runtime (e.g., comparison). |
| **Counting Function (C(n))** | How many times the basic operation is executed.                |
| **Total Time (T(n))**        | Depends on number of basic operations and their cost.          |

[
T(n) = c \times C(n)
]

where ( c ) is the time for one basic operation.

---

## 🧮 **8. Example: Insertion Sort**

Let’s analyze performance roughly.

**Best case:** Already sorted list
→ Comparisons = n−1
→ Time = O(n)

**Worst case:** Reverse sorted
→ Comparisons ≈ n(n−1)/2
→ Time = O(n²)

**Average case:** Random order
→ Time = O(n²)

| Case    | Comparisons | Time Complexity |
| ------- | ----------- | --------------- |
| Best    | n-1         | O(n)            |
| Average | n²/4        | O(n²)           |
| Worst   | n²/2        | O(n²)           |

---

## ⚖️ **9. Relationship Between Time and Space**

Sometimes improving one affects the other:

| Algorithm           | Time        | Space                                |
| ------------------- | ----------- | ------------------------------------ |
| Recursive           | Higher time | More stack space                     |
| Iterative           | Lower time  | Less space                           |
| Dynamic Programming | Faster      | Uses more space (stores sub-results) |

This is known as the **Time–Space Tradeoff**.

---

## 🧩 **10. Steps in Performance Analysis**

| Step | Description                                              |
| ---- | -------------------------------------------------------- |
| 1️⃣  | Identify input size (n).                                 |
| 2️⃣  | Choose the basic operation (e.g., comparison, addition). |
| 3️⃣  | Count how many times it executes (C(n)).                 |
| 4️⃣  | Find time per operation (c).                             |
| 5️⃣  | Compute total time ( T(n) = c × C(n) ).                  |
| 6️⃣  | Express T(n) using asymptotic notation (Big O).          |

---

## 🏁 **11. Conclusion**

* **Performance analysis** evaluates an algorithm’s efficiency using **time** and **space**.
* **Time complexity** depends on input size and operations.
* **Space complexity** depends on memory requirements.
* It helps compare algorithms objectively — independent of hardware or language.

---

### ✅ **Key Takeaways**

* Time and space complexities together define an algorithm’s **performance**.
* Use **asymptotic notations (O, Ω, Θ)** to generalize performance.
* Real-world choice of algorithms depends on a **balance between time, space, and simplicity**.

---

# **Space Complexity**

---

## 🧩 **1. Introduction**

When we execute an algorithm, it uses **memory space** to store data and perform operations.
The **space complexity** of an algorithm measures **how much memory it needs** during its execution.

> 📘 **Definition:**
> **Space Complexity** is the total amount of memory space required by an algorithm to execute completely and produce the result.

It includes all the memory required for:

* Input and output data
* Variables
* Constants
* Recursion stack
* Temporary data structures

---

## ⚙️ **2. Components of Space Complexity**

The total space used by an algorithm can be expressed as:

[
S(P) = C + I + T + R
]

where:

| Symbol | Meaning                                                            |
| ------ | ------------------------------------------------------------------ |
| **C**  | Fixed part — memory for constants, simple variables, program code. |
| **I**  | Input space — memory to store input values.                        |
| **T**  | Temporary space — memory for temporary variables, arrays, etc.     |
| **R**  | Recursion space — memory used for recursive calls (stack).         |

So,
[
S(P) = C + S_{input} + S_{temporary} + S_{recursion}
]

---

## 🧮 **3. Example 1: Iterative Algorithm**

### Algorithm

```pseudo
Sum(A, n)
  total ← 0
  for i ← 1 to n do
      total ← total + A[i]
  return total
```

### Space Usage

| Memory Type | Description       | Space |
| ----------- | ----------------- | ----- |
| Constants   | `0`, `1`          | O(1)  |
| Variables   | `i`, `total`, `n` | O(1)  |
| Input Array | `A[n]`            | O(n)  |
| Temporary   | None              | O(1)  |
| Recursion   | None              | O(1)  |

So total space:

[
S(n) = O(n) + O(1) + O(1) + O(1) = O(n)
]

✅ **Space Complexity = O(n)**

---

## 🧮 **4. Example 2: Recursive Factorial**

### Algorithm

```pseudo
Factorial(n)
  if n = 0 then
      return 1
  else
      return n * Factorial(n - 1)
```

### Space Usage

Each recursive call adds one frame to the **function call stack**, storing:

* Return address
* Value of `n`
* Local variables

For `n` recursive calls → **stack depth = n**

| Component            | Space |
| -------------------- | ----- |
| Constants, variables | O(1)  |
| Recursion stack      | O(n)  |
| Input                | O(1)  |

✅ **Space Complexity = O(n)**

---

## 💾 **5. Components Explained in Detail**

| Component               | Explanation                                              | Example                     |
| ----------------------- | -------------------------------------------------------- | --------------------------- |
| **Fixed Part (C)**      | Independent of input size. Program code, constants, etc. | e.g., variable declarations |
| **Variable Part**       | Depends on the size of input and intermediate results.   | e.g., array `A[n]`          |
| **Input Space (I)**     | Memory to store the input data.                          | Storing list of `n` numbers |
| **Temporary Space (T)** | For intermediate calculations.                           | Temporary sum, product      |
| **Recursion Space (R)** | Stack space for recursive calls.                         | Recursive factorial         |

---

## 📊 **6. Graphical View**

```
Total Space
│
│        |<- Recursion Space (R)
│        |<- Temporary Variables (T)
│        |<- Input Space (I)
│        |<- Fixed Space (C)
│
└──────────────────────────────→ Time
```

As the program runs, temporary and recursive memory grows and shrinks dynamically.

---

## ⚖️ **7. Space-Time Tradeoff**

Sometimes, you can save **time** by using **extra memory**, or save **memory** by using **extra time**.

| Approach               | Space | Time | Example             |
| ---------------------- | ----- | ---- | ------------------- |
| **Pre-computation**    | More  | Less | Dynamic Programming |
| **In-place algorithm** | Less  | More | Selection Sort      |
| **Caching**            | More  | Less | Memoization         |

**Dynamic programming** is a common example:
It uses extra space to store results of subproblems → reduces time drastically.

---

## 🔍 **8. Example 3: Fibonacci**

### Recursive Version

```pseudo
Fib(n)
  if n <= 1 then return n
  else return Fib(n-1) + Fib(n-2)
```

* Each recursive call creates two more calls.
* Stack depth = n.
  ✅ Space complexity = O(n)

### Iterative Version

```pseudo
FibIterative(n)
  if n <= 1 return n
  a ← 0
  b ← 1
  for i ← 2 to n do
      c ← a + b
      a ← b
      b ← c
  return b
```

* Only few variables used (`a`, `b`, `c`, `i`)
  ✅ Space complexity = O(1)

🧠 **Observation:** Iterative version uses **less space**.

---

## 🧩 **9. Typical Space Complexities**

| Type of Algorithm                   | Typical Space Complexity |
| ----------------------------------- | ------------------------ |
| Constant variables only             | O(1)                     |
| Uses array or list                  | O(n)                     |
| Uses matrix                         | O(n²)                    |
| Uses recursion (depth n)            | O(n)                     |
| Dynamic programming                 | O(n) – O(n²)             |
| Graph algorithms (adjacency matrix) | O(V²)                    |

---

## 🧮 **10. Formula Summary**

[
S(n) = C + S_{input}(n) + S_{temporary}(n) + S_{recursion}(n)
]

In most cases, we consider the **asymptotic behavior**, so:
[
S(n) = O(f(n))
]
where ( f(n) ) describes the growth rate of memory use.

---

## 🏁 **11. Conclusion**

* **Space Complexity** measures how much memory an algorithm needs.
* It includes memory for **input, variables, and recursion stack**.
* **Recursive algorithms** usually take more space than **iterative** ones.
* Balancing **time vs. space** is crucial for efficient algorithm design.

---

### ✅ **Key Takeaways**

* ( S(P) = C + I + T + R )
* Recursive algorithms → stack grows → more space.
* Use **iterative methods** when memory is limited.
* Analyze both **time** and **space** to find the most optimal algorithm.

---

# **Time Complexity**

---

## 🧩 **1. Introduction**

Every algorithm performs a series of steps to solve a problem.
The **time complexity** of an algorithm measures **how long it takes** (in terms of number of basic operations) as the **input size increases**.

> 📘 **Definition:**
> **Time complexity** of an algorithm is the **total amount of time required** by the algorithm to execute completely, expressed as a function of the input size `n`.

---

## ⚙️ **2. Why We Need Time Complexity**

We can’t compare algorithms based on actual execution time because it depends on:

* CPU speed
* Programming language
* Compiler optimization
* System load

So instead of seconds, we measure **the number of basic operations** (like addition, comparison, assignment) that the algorithm performs — independent of hardware.

---

## 🧮 **3. Formal Definition**

If an algorithm performs **f(n)** basic operations for input size `n`,
then its **time complexity** is said to be:

[
T(n) = O(f(n))
]

Where:

* ( n ) → size of input
* ( f(n) ) → number of basic operations
* ( O(f(n)) ) → asymptotic upper bound (growth rate)

---

## 🔹 **4. Basic Operation**

A **basic operation** is the operation that contributes most to the total running time — typically the operation inside the **innermost loop**.

Example:
In linear search, the comparison `A[i] == x` is the basic operation.

---

## 🧩 **5. Counting Basic Operations**

Let’s analyze a few examples:

---

### **Example 1: Constant Time — O(1)**

```pseudo
sum ← a + b
```

Only one operation, independent of input size.

✅ **T(n) = O(1)** (Constant time)

---

### **Example 2: Linear Time — O(n)**

```pseudo
for i ← 1 to n do
    print(i)
```

Loop runs `n` times → total operations proportional to `n`.

✅ **T(n) = O(n)** (Linear time)

---

### **Example 3: Quadratic Time — O(n²)**

```pseudo
for i ← 1 to n do
    for j ← 1 to n do
        print(i, j)
```

Outer loop runs `n` times, inner loop runs `n` times → total = n × n.

✅ **T(n) = O(n²)** (Quadratic time)

---

### **Example 4: Logarithmic Time — O(log n)**

```pseudo
i ← 1
while i <= n do
    i ← i * 2
```

`i` doubles each iteration → runs about log₂(n) times.

✅ **T(n) = O(log n)** (Logarithmic time)

---

### **Example 5: Linearithmic Time — O(n log n)**

Merge Sort divides the array (log n times) and processes each element (n).

✅ **T(n) = O(n log n)**

---

## 📊 **6. Common Time Complexities**

| Time Complexity | Name         | Example                           |
| --------------- | ------------ | --------------------------------- |
| O(1)            | Constant     | Accessing array element           |
| O(log n)        | Logarithmic  | Binary search                     |
| O(n)            | Linear       | Linear search                     |
| O(n log n)      | Linearithmic | Merge sort, Quick sort (avg case) |
| O(n²)           | Quadratic    | Bubble sort, Insertion sort       |
| O(n³)           | Cubic        | Matrix multiplication             |
| O(2ⁿ)           | Exponential  | Recursive Fibonacci               |
| O(n!)           | Factorial    | Traveling Salesman (brute force)  |

📈 **Growth Rate Visualization**

```
Time
│
│                         O(2ⁿ)
│                      O(n!)
│                  O(n³)
│               O(n²)
│            O(n log n)
│          O(n)
│        O(log n)
│_____O(1)___________________________________→ n
```

---

## 🧠 **7. Types of Time Complexities**

| Type             | Description                         | Example                        |
| ---------------- | ----------------------------------- | ------------------------------ |
| **Best Case**    | Minimum time the algorithm can take | Searching first element        |
| **Average Case** | Expected time for random input      | Linear search (middle element) |
| **Worst Case**   | Maximum time for any input          | Searching element not present  |

---

## 🔍 **8. Example: Linear Search**

```pseudo
LinearSearch(A, n, x)
  for i ← 1 to n do
      if A[i] == x then
          return i
  return -1
```

| Case    | Comparisons | Time Complexity |
| ------- | ----------- | --------------- |
| Best    | 1           | O(1)            |
| Average | (n+1)/2     | O(n)            |
| Worst   | n           | O(n)            |

---

## 🧮 **9. Example: Nested Loops**

```pseudo
for i ← 1 to n do
    for j ← 1 to i do
        print(i, j)
```

Number of iterations:

[
1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}
]
So,
✅ **T(n) = O(n²)**

---

## 🧩 **10. Example: Recursive Algorithm (Fibonacci)**

```pseudo
Fib(n)
  if n <= 1 then return n
  else return Fib(n-1) + Fib(n-2)
```

Recurrence relation:

[
T(n) = T(n-1) + T(n-2) + c
]

Solution → ( T(n) = O(2^n) )

✅ Exponential growth.

---

## ⚙️ **11. Measuring Time in Practice**

When analyzing algorithms empirically:

1. Measure **execution time** for various input sizes.
2. Plot **input size vs execution time**.
3. Compare the **growth trend** with theoretical complexity.

---

## 🧮 **12. Relation Between Time and Input Size**

* Time increases as **input size increases**.
* Growth rate shows **how quickly** it increases.

| Input Size | O(1) | O(log n) | O(n)  | O(n²)     | O(2ⁿ)           |
| ---------- | ---- | -------- | ----- | --------- | --------------- |
| 10         | 1    | 3        | 10    | 100       | 1,024           |
| 100        | 1    | 7        | 100   | 10,000    | ~10³⁰           |
| 1,000      | 1    | 10       | 1,000 | 1,000,000 | astronomical 🚀 |

---

## 🧩 **13. Stepwise Procedure for Time Complexity Analysis**

| Step | Description                                 |
| ---- | ------------------------------------------- |
| 1️⃣  | Identify the basic operation.               |
| 2️⃣  | Determine how many times it executes.       |
| 3️⃣  | Express the count as a function of `n`.     |
| 4️⃣  | Simplify using asymptotic notation (Big O). |

---

## 🏁 **14. Conclusion**

* **Time complexity** measures how an algorithm’s runtime grows with input size.
* Expressed using **asymptotic notation** (Big O, Θ, Ω).
* Helps compare algorithms **independently of hardware**.
* Lower time complexity ⇒ **faster and more efficient algorithm**.

---

### ✅ **Key Takeaways**

* ( T(n) = O(f(n)) )
* Choose the **basic operation** wisely (usually innermost loop).
* Compare algorithms by **order of growth**, not raw time.
* Understand **best**, **average**, and **worst** cases.

---

# 🔹 **Asymptotic Notation**

**Asymptotic Notations** are mathematical tools used to describe the **efficiency** or **growth rate** of an algorithm’s running time (or sometimes space) as the **input size n** becomes very large.

They help compare algorithms **independently of hardware or implementation details**.

We focus on **how the runtime grows** with input size rather than exact values.

---

### 🧠 **Why Asymptotic Notation?**

Let’s say you have two algorithms:

| Algorithm | Time (sec) for n = 100 | Growth rate |
| --------- | ---------------------- | ----------- |
| A         | 0.001n²                | Quadratic   |
| B         | 1000n                  | Linear      |

At `n = 100`, A takes 10 sec, B takes 100,000 sec.
But at `n = 1,000,000`, A takes 10¹² sec, B takes 10⁹ sec — so A becomes **worse** for large n.

Hence, we use **asymptotic analysis** to see **behavior for large n**.

---

## ⚙️ **1. Big O Notation (O)**

### Definition

Big O gives the **upper bound** of the running time.
It describes the **worst-case** growth rate.

Formally:
$$
f(n) = O(g(n)) \text{ if } \exists c>0, n_0>0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0
$$

It means that **beyond some point n₀**, f(n) never grows faster than a constant multiple of g(n).

### Example

If an algorithm takes
$$
f(n) = 3n^2 + 5n + 2
$$
Then
$$
f(n) = O(n^2)
$$
because, for large n, the term `3n²` dominates, and constants are ignored.

---

### **Common Big O classes**

| Complexity | Name        | Example Algorithm                |
| ---------- | ----------- | -------------------------------- |
| O(1)       | Constant    | Accessing array element          |
| O(log n)   | Logarithmic | Binary Search                    |
| O(n)       | Linear      | Linear Search                    |
| O(n log n) | Log-linear  | Merge Sort                       |
| O(n²)      | Quadratic   | Bubble Sort                      |
| O(n³)      | Cubic       | Matrix Multiplication            |
| O(2ⁿ)      | Exponential | Subset generation                |
| O(n!)      | Factorial   | Traveling Salesman (Brute force) |

📊 **Graph of common growth rates:**

```
|
|                        O(2ⁿ)
|                 O(n²)
|           O(n log n)
|       O(n)
|   O(log n)
|_O(1)_________________________
              n →
```

---

## ⚙️ **2. Omega Notation (Ω)**

### Definition

Omega gives the **lower bound** of the running time — the **best-case** scenario.

Formally:
$$
f(n) = \Omega(g(n)) \text{ if } \exists c>0, n_0>0 \text{ such that } f(n) \ge c \cdot g(n) \text{ for all } n \ge n_0
$$

That means f(n) **never grows slower** than g(n).

### Example:

If
$$
f(n) = 3n^2 + 5n + 2
$$
then
$$
f(n) = \Omega(n^2)
$$
since for large n, n² is the dominant term.

---

## ⚙️ **3. Theta Notation (Θ)**

### Definition

Theta gives a **tight bound** — when the function grows **both upper and lower** like g(n).

Formally:
$$
f(n) = \Theta(g(n)) \text{ if } \exists c_1, c_2 > 0, n_0 > 0 \text{ such that } c_1g(n) \le f(n) \le c_2g(n) \text{ for all } n \ge n_0
$$

So, Θ means both `O(g(n))` and `Ω(g(n))` are true.

### Example:

$$
f(n) = 3n^2 + 5n + 2 = \Theta(n^2)
$$

---

## ⚙️ **4. Little o Notation (o)**

### Definition

Little o gives a **strict upper bound** — f(n) grows **slower than** g(n).

Formally:
$$
f(n) = o(g(n)) \text{ if } \forall c > 0, \exists n_0 > 0 \text{ such that } f(n) < c \cdot g(n) \text{ for all } n \ge n_0
$$

### Example:

$$
n = o(n^2)
$$
because for large n, n grows strictly slower than n².

So, f(n) = o(g(n)) means **f(n) is asymptotically smaller** than g(n).

---

## 🧩 **Comparison Summary**

| Notation | Meaning                   | Bound Type         | Used for           |
| -------- | ------------------------- | ------------------ | ------------------ |
| O(g(n))  | f(n) ≤ c·g(n)             | Upper Bound        | Worst Case         |
| Ω(g(n))  | f(n) ≥ c·g(n)             | Lower Bound        | Best Case          |
| Θ(g(n))  | c₁·g(n) ≤ f(n) ≤ c₂·g(n)  | Tight Bound        | Average/Exact Case |
| o(g(n))  | f(n) < c·g(n) for all c>0 | Strict Upper Bound | Precise comparison |

---

### 💻 **Example (with algorithm):**

```c
void example(int n) {
    for (int i = 0; i < n; i++) {       // O(n)
        for (int j = 0; j < n; j++) {   // O(n)
            printf("*");
        }
    }
}
```

Total operations = n × n = **n²**

✅ Time complexity:

* Big O: O(n²)
* Omega: Ω(n²)
* Theta: Θ(n²)

---

### ⚖️ **Example of asymptotic comparison**

| Function     | Order of growth |
| ------------ | --------------- |
| 2n + 10      | O(n)            |
| 10n log n    | O(n log n)      |
| 5n² + 3n + 8 | O(n²)           |
| 7 · 2ⁿ       | O(2ⁿ)           |

---

### 🧠 **Quick Intuition**

* **O** → at most grows like this
* **Ω** → at least grows like this
* **Θ** → grows exactly like this
* **o** → grows slower than this

---


| Notation    | Type of Bound      | Meaning                                          |
| ----------- | ------------------ | ------------------------------------------------ |
| **O(g(n))** | Upper Bound        | Function grows **no faster than** g(n)           |
| **Ω(g(n))** | Lower Bound        | Function grows **no slower than** g(n)           |
| **Θ(g(n))** | Tight Bound        | Function grows **exactly like** g(n) (same rate) |
| **o(g(n))** | Strict Upper Bound | Function grows **slower than** g(n)              |

---

## 📊 **1️⃣ Big O Notation (Upper Bound)**

### Example:

Let’s say
$$f(n) = 2n^2 + 3n + 10$$
We can say
$$f(n) = O(n^2)$$

### Graph:

```
|                 O(g(n))  = n²
|               /
|           f(n) = 2n² + 3n + 10
|         /
|       /
|_____n→________________________
```

✅ **Interpretation:**
For sufficiently large n, **f(n)** will **never exceed** a constant multiple of g(n).
So, `f(n)` lies **below or touches** `c·g(n)`.

---

## 📊 **2️⃣ Omega Notation (Lower Bound)**

### Example:

$$f(n) = 2n^2 + 3n + 10 = Ω(n^2)$$

### Graph:

```
|         f(n)
|       /
|     / 
|   /        Ω(g(n)) = n²
|__/___________________________ n →
```

✅ **Interpretation:**
For large n, `f(n)` is always **above** or equal to a constant multiple of g(n).
It **never grows slower** than g(n).

---

## 📊 **3️⃣ Theta Notation (Tight Bound)**

### Example:

$$f(n) = 3n^2 + 5n + 20 = Θ(n^2)$$

That means there exist constants `c₁` and `c₂` such that:

$$
c₁·n² ≤ f(n) ≤ c₂·n²
$$

### Graph:

```
|          c₂·n²  (Upper bound)
|         /
|        /  ← f(n)
|       /
|      c₁·n²  (Lower bound)
|_____/______________________ n →
```

✅ **Interpretation:**
`f(n)` is **sandwiched** between two constant multiples of `n²`.
This represents **tight bounding** — the actual growth is very close to `n²`.

---

## 📊 **4️⃣ Little o Notation (Strict Upper Bound)**

### Example:

$$f(n) = n = o(n^2)$$

That means f(n) grows **strictly slower** than n².

### Graph:

```
|               g(n) = n²
|           /
|         /
|     f(n) = n
|___/_________________________ n →
```

✅ **Interpretation:**
`f(n)` **never catches up** to any constant multiple of `g(n)` for large n.
It always grows **slower**, no matter the constant.

---

## 🔎 **Visual Summary:**

```
Growth comparison (for large n):

Θ(g(n))     → tightly hugs g(n)
O(g(n))     → stays below or equal to g(n)
Ω(g(n))     → stays above or equal to g(n)
o(g(n))     → strictly below g(n)
```

Or more intuitively:

| Notation    | Relationship between f(n) and g(n) | Visual Behavior   |
| ----------- | ---------------------------------- | ----------------- |
| **O(g(n))** | f(n) ≤ c·g(n)                      | Upper boundary    |
| **Ω(g(n))** | f(n) ≥ c·g(n)                      | Lower boundary    |
| **Θ(g(n))** | c₁·g(n) ≤ f(n) ≤ c₂·g(n)           | Between two lines |
| **o(g(n))** | f(n) < c·g(n) (strictly)           | Always under g(n) |

---

## 🧩 **Graphical Example Summary**

Let’s assume `g(n) = n²` and see where f(n) lies:

| f(n)         | Notation relation | Position                         |
| ------------ | ----------------- | -------------------------------- |
| 5n² + 3n + 2 | Θ(n²)             | tightly same curve               |
| n log n      | o(n²)             | below n²                         |
| n³           | Ω(n²)             | above n²                         |
| n² + 100n    | O(n²)             | below or equal to n² for large n |

---

# 🔹 **Recurrences**

## 🧠 **Definition**

A **recurrence relation** is a mathematical expression that describes the **running time** (or any quantity) of an algorithm **in terms of its value on smaller inputs**.

In simple words:

> A recurrence shows **how a problem’s solution depends on smaller subproblems.**

---

### 💡 Example

Consider the **recursive algorithm for factorial**:

```c
int fact(int n) {
    if (n <= 1) return 1;
    else return n * fact(n - 1);
}
```

If we measure the number of operations:

$$
T(n) = T(n - 1) + 1
$$
with base condition
$$
T(1) = 1
$$

👉 This means to compute `fact(n)`, we do one operation + the work of `fact(n-1)`.

---

## 🔹 **General Form of Recurrence**

Most recurrence relations have the general form:

$$
T(n) = a , T\left(\frac{n}{b}\right) + f(n)
$$

Where:

| Symbol   | Meaning                              |
| :------- | :----------------------------------- |
| **T(n)** | Time complexity of problem size `n`  |
| **a**    | Number of subproblems                |
| **n/b**  | Size of each subproblem              |
| **f(n)** | Cost of dividing + combining results |

---

### 🧩 **Examples**

| Algorithm                | Recurrence Relation     | Explanation                            |
| ------------------------ | ----------------------- | -------------------------------------- |
| **Binary Search**        | $T(n) = T(n/2) + c$     | Split into 1 subproblem of half size   |
| **Merge Sort**           | $T(n) = 2T(n/2) + O(n)$ | Two halves + merge step                |
| **Quick Sort (average)** | $T(n) = 2T(n/2) + O(n)$ | Same as merge sort on average          |
| **Tower of Hanoi**       | $T(n) = 2T(n-1) + 1$    | Two smaller recursive calls + one move |
| **Linear Recursion**     | $T(n) = T(n-1) + c$     | Single smaller subproblem              |

---

# 🔸 **Methods for Solving Recurrences**

There are three main methods to find **T(n)** from a recurrence:

---

## 🧮 **1. Substitution (Iteration) Method**

You **expand** the recurrence step by step until a pattern appears.

### Example:

$$
T(n) = T(n - 1) + n, \quad T(1) = 1
$$

**Expand:**

[
\begin{aligned}
T(n) &= T(n-1) + n \
&= (T(n-2) + (n-1)) + n \
&= T(n-2) + (n-1) + n \
&= T(n-3) + (n-2) + (n-1) + n \
&\vdots \
&= T(1) + (2 + 3 + 4 + ... + n)
\end{aligned}
]

Sum of first n numbers:
$$
1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}
$$

So,
$$
T(n) = O(n^2)
$$

✅ Hence, **T(n) = O(n²)**

---

## 🌲 **2. Recursion Tree Method**

Used to **visualize** how recursive calls divide the work.

### Example:

$$
T(n) = 2T(n/2) + n
$$

#### Step 1: Draw recursion tree

```
              T(n)
            /     \
       T(n/2)     T(n/2)
        /  \         /  \
   T(n/4) T(n/4)  T(n/4) T(n/4)
```

#### Step 2: Cost at each level

At level 0: work = `n`
At level 1: 2 × (n/2) = `n`
At level 2: 4 × (n/4) = `n`
...
All levels do `n` work.

Number of levels = log₂n

#### Step 3: Total cost

$$
T(n) = n \times (\log_2 n + 1) = O(n \log n)
$$

✅ So, **Merge Sort = O(n log n)**

---

## 📘 **3. Master Theorem**

Master Theorem provides a **direct formula** for solving:
$$
T(n) = aT\left(\frac{n}{b}\right) + f(n)
$$

### Compare:

* `a` = number of subproblems
* `n/b` = size of each subproblem
* `f(n)` = cost of work done outside recursion

---

### **Three Cases of Master Theorem**

| Case  | Condition                                                                  | Result                               |
| ----- | -------------------------------------------------------------------------- | ------------------------------------ |
| **1** | if $f(n) = O(n^{\log_b a - \epsilon})$ for some ε > 0                      | $T(n) = \Theta(n^{\log_b a})$        |
| **2** | if $f(n) = \Theta(n^{\log_b a})$                                           | $T(n) = \Theta(n^{\log_b a} \log n)$ |
| **3** | if $f(n) = \Omega(n^{\log_b a + \epsilon})$ and regularity condition holds | $T(n) = \Theta(f(n))$                |

---

### 💡 Examples using Master Theorem

| Algorithm               | Recurrence         | a | b | f(n)  | Case   | Result     |
| ----------------------- | ------------------ | - | - | ----- | ------ | ---------- |
| Binary Search           | T(n)=T(n/2)+1      | 1 | 2 | O(1)  | Case 1 | O(log n)   |
| Merge Sort              | T(n)=2T(n/2)+O(n)  | 2 | 2 | O(n)  | Case 2 | O(n log n) |
| Strassen’s Matrix Mult. | T(n)=7T(n/2)+O(n²) | 7 | 2 | O(n²) | Case 1 | O(n^2.81)  |

---

## 🧩 **Some Common Recurrences and Solutions**

| Recurrence            | Solution   | Example Algorithm         |
| --------------------- | ---------- | ------------------------- |
| T(n) = T(n-1) + c     | O(n)       | Linear recursion          |
| T(n) = T(n/2) + c     | O(log n)   | Binary search             |
| T(n) = 2T(n/2) + c    | O(n)       | Linear recursion doubling |
| T(n) = 2T(n/2) + O(n) | O(n log n) | Merge Sort                |
| T(n) = 2T(n/2) + O(1) | O(n)       | Tree traversal            |
| T(n) = 2T(n-1) + 1    | O(2ⁿ)      | Tower of Hanoi            |

---

## 🔍 **Visual Summary**

```
T(n) = aT(n/b) + f(n)
--------------------------------
Binary Search     →  T(n)=T(n/2)+1      →  O(log n)
Merge Sort        →  T(n)=2T(n/2)+n     →  O(n log n)
Tower of Hanoi    →  T(n)=2T(n-1)+1     →  O(2ⁿ)
Linear Recursion  →  T(n)=T(n-1)+n      →  O(n²)
```

---

## ✅ **Key Takeaways**

* **Recurrence** expresses **running time** in terms of smaller inputs.
* **Methods to solve:** Iteration, Recursion Tree, Master Theorem.
* **Common patterns** occur repeatedly in divide & conquer and recursion-based algorithms.
* **Master Theorem** gives a fast way to find time complexity for `T(n)=aT(n/b)+f(n)`.

---
