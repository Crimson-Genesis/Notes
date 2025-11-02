# Unit - 2

## Brute Force, Divide-and-Conquer, Decrease-and-Conquer, Input Enhancement
- Selection Sort and Bubble Sort
- Sequential Search
- Exhaustive search
- String matching
- Meargesort
- QuichSort
- Binary Search
- Insertion Sort
- Depth First and Breadth First Search
- Thoplogical Sorting
- String Matching Algorithms
- Horpool's Algorithm
- Boyer Moore Algorithm

---
---

# 🔹 **1. Selection Sort**

## 🧠 **Concept**

Selection Sort works by **repeatedly selecting the smallest (or largest)** element from the **unsorted part** of the array and placing it in the **correct position** in the sorted part.

It divides the list into two parts:

* **Sorted portion** (initially empty)
* **Unsorted portion** (initially the whole array)

Then, in each iteration:

1. Find the **minimum element** in the unsorted array.
2. Swap it with the **first unsorted element**.
3. Increase the boundary of the sorted portion.

---

## 🔧 **Algorithm Steps**

For an array `A` of size `n`:

1. For each position `i = 0` to `n-2`

   * Assume `A[i]` is the minimum.
   * Compare it with all elements after it.
   * If any smaller element is found, mark its index.
   * Swap the smallest found element with `A[i]`.

---

### 💻 **Pseudocode**

```text
SelectionSort(A, n)
1. for i ← 0 to n-2 do
2.     minIndex ← i
3.     for j ← i+1 to n-1 do
4.         if A[j] < A[minIndex] then
5.             minIndex ← j
6.     swap(A[i], A[minIndex])
```

---

### 🧩 **Example**

Let’s sort:
**A = [64, 25, 12, 22, 11]**

| Pass | Array                | Minimum | Swap    | Result               |
| ---- | -------------------- | ------- | ------- | -------------------- |
| 1    | [64, 25, 12, 22, 11] | 11      | 11 ↔ 64 | [11, 25, 12, 22, 64] |
| 2    | [11, 25, 12, 22, 64] | 12      | 12 ↔ 25 | [11, 12, 25, 22, 64] |
| 3    | [11, 12, 25, 22, 64] | 22      | 22 ↔ 25 | [11, 12, 22, 25, 64] |
| 4    | [11, 12, 22, 25, 64] | 25      | 25 ↔ 25 | [11, 12, 22, 25, 64] |

✅ **Sorted Array:** [11, 12, 22, 25, 64]

---

### ⏱ **Complexity Analysis**

| Case       | Comparisons | Swaps | Time Complexity |
| ---------- | ----------- | ----- | --------------- |
| Best Case  | n(n-1)/2    | n-1   | **O(n²)**       |
| Worst Case | n(n-1)/2    | n-1   | **O(n²)**       |
| Average    | —           | —     | **O(n²)**       |
| Space      | —           | —     | **O(1)**        |

📘 **Stable?** ❌ *No* (because swapping may change the relative order).
📘 **In-place?** ✅ *Yes*

---

## 🔹 Visual Diagram of Selection Sort

```
Unsorted: [64, 25, 12, 22, 11]
            ↓
Find min → [11, 25, 12, 22, 64]
               ↓
Next min → [11, 12, 25, 22, 64]
                   ↓
Next min → [11, 12, 22, 25, 64]
```

---

# 🔹 **2. Bubble Sort**

## 🧠 **Concept**

Bubble Sort repeatedly **compares adjacent elements** and **swaps them if they are in the wrong order**.
In each pass, the **largest element “bubbles up”** to the end of the array.

---

## 🔧 **Algorithm Steps**

1. Compare each adjacent pair.
2. Swap them if they are in the wrong order.
3. After the first pass, the largest element is at the end.
4. Repeat the process for remaining unsorted elements.

---

### 💻 **Pseudocode**

```text
BubbleSort(A, n)
1. for i ← 0 to n-2 do
2.     for j ← 0 to n-i-2 do
3.         if A[j] > A[j+1] then
4.             swap(A[j], A[j+1])
```

---

### 🧩 **Example**

**A = [5, 1, 4, 2, 8]**

| Pass | Comparisons             | Result after pass        |
| ---- | ----------------------- | ------------------------ |
| 1    | (5>1),(5>4),(5>2),(5<8) | [1, 4, 2, 5, 8]          |
| 2    | (1<4),(4>2),(4<5)       | [1, 2, 4, 5, 8]          |
| 3    | (1<2),(2<4)             | [1, 2, 4, 5, 8]          |
| 4    | (no swaps)              | [1, 2, 4, 5, 8] ✅ sorted |

---

### 🧩 **Optimized Bubble Sort**

We can **stop early** if in a pass no swaps occur — means array is already sorted.

```text
BubbleSort(A, n)
1. for i ← 0 to n-2 do
2.     swapped ← false
3.     for j ← 0 to n-i-2 do
4.         if A[j] > A[j+1] then
5.             swap(A[j], A[j+1])
6.             swapped ← true
7.     if swapped = false then
8.         break
```

---

### ⏱ **Complexity Analysis**

| Case               | Comparisons | Time Complexity         |
| ------------------ | ----------- | ----------------------- |
| Best Case (sorted) | n-1         | **O(n)** (if optimized) |
| Worst Case         | n(n-1)/2    | **O(n²)**               |
| Average Case       | —           | **O(n²)**               |
| Space              | —           | **O(1)**                |

📘 **Stable?** ✅ *Yes* (equal elements retain order)
📘 **In-place?** ✅ *Yes*

---

## 🔹 **Visualization**

```
Pass 1: [5, 1, 4, 2, 8]
          ↕  ↕  ↕  ↕
        [1, 4, 2, 5, 8]  ← 8 bubbled up

Pass 2: [1, 4, 2, 5, 8]
            ↕  ↕  ↕
        [1, 2, 4, 5, 8]  ← 5 bubbled up
```

✅ Sorted array after 2 passes.

---

## ⚖️ **Comparison Table**

| Feature    | Selection Sort                      | Bubble Sort                |
| ---------- | ----------------------------------- | -------------------------- |
| Approach   | Find min and swap                   | Compare & swap adjacent    |
| Best Case  | O(n²)                               | O(n) (optimized)           |
| Worst Case | O(n²)                               | O(n²)                      |
| Stable     | ❌ No                                | ✅ Yes                      |
| In-place   | ✅ Yes                               | ✅ Yes                      |
| Swaps      | n-1                                 | Many                       |
| Use Case   | Small arrays, when swaps are costly | Teaching, simple demo sort |

---

## 🔍 **Summary Diagram**

```
Selection Sort → Select minimum → Swap → Repeat → O(n²)
Bubble Sort    → Compare + Swap Adjacent → Repeat → O(n²)
```

---

# 🔹 Sequential Search (Linear Search)

### 🔸 Definition

Sequential Search (also called **Linear Search**) is the **simplest searching algorithm**.
It checks each element in a list or array **one by one** until the desired element (called the *key*) is found or the list ends.

---

### 🔸 Working Principle

1. Start from the **first element** of the array.
2. Compare it with the **key** to be searched.
3. If it matches, **return the position (index)**.
4. If not, move to the **next element**.
5. Repeat steps 2–4 until the end of the array.
6. If the key is not found, return **“Not Found”**.

---

### 🔸 Example

Suppose we have an array:

| Index |  0  |  1  |  2  |  3  |  4  |
| :---- | :-: | :-: | :-: | :-: | :-: |
| Value |  15 |  8  |  23 |  42 |  9  |

We want to search for **key = 42**

**Step-by-step process:**

| Step | Current Element | Comparison | Result           |
| :--: | :-------------- | :--------- | :--------------- |
|   1  | 15              | 15 ≠ 42    | Continue         |
|   2  | 8               | 8 ≠ 42     | Continue         |
|   3  | 23              | 23 ≠ 42    | Continue         |
|   4  | 42              | 42 = 42    | Found at index 3 |

✅ **Output:** Element found at index 3.

---

### 🔸 Diagram Representation

```
Array: [15] [8] [23] [42] [9]
Key = 42

↓ Start scanning left to right
15 ≠ 42  →  8 ≠ 42  →  23 ≠ 42  →  ✅ 42 = 42 → Found!
```

---

### 🔸 Algorithm (Pseudocode)

```
Algorithm SequentialSearch(A, n, key)
Input: Array A of size n, key to search
Output: Index of key if found, else -1

1. for i ← 0 to n-1 do
2.     if A[i] = key then
3.         return i
4. return -1
```

---

### 🔸 C Code Example

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i; // Found
    }
    return -1; // Not found
}

int main() {
    int arr[] = {15, 8, 23, 42, 9};
    int n = 5, key = 42;
    
    int result = linearSearch(arr, n, key);
    
    if (result == -1)
        printf("Element not found\n");
    else
        printf("Element found at index %d\n", result);
    
    return 0;
}
```

---

### 🔸 Time Complexity

| Case             | Description                                 | Comparisons | Time Complexity |
| :--------------- | :------------------------------------------ | :---------- | :-------------- |
| **Best Case**    | Element found at first position             | 1           | **O(1)**        |
| **Worst Case**   | Element found at last position or not found | n           | **O(n)**        |
| **Average Case** | Element in middle on average                | n/2         | **O(n)**        |

---

### 🔸 Space Complexity

* No extra space used (apart from a few variables)
  ✅ **Space Complexity = O(1)**

---

### 🔸 Advantages

* Simple and easy to implement.
* Works on **unsorted** data.
* No need for additional memory.

### 🔸 Disadvantages

* Very **slow** for large data sets.
* Inefficient compared to binary search for sorted arrays.

---

### 🔹 Summary Table

| Property           | Linear (Sequential) Search                  |
| :----------------- | :------------------------------------------ |
| Type               | Brute force                                 |
| Works on           | Sorted/Unsorted data                        |
| Best Case          | O(1)                                        |
| Average/Worst Case | O(n)                                        |
| Space              | O(1)                                        |
| Stable             | Yes                                         |
| Example            | Searching roll number in a list of students |

---

# 🔹 Exhaustive Search

### 🔸 Definition

**Exhaustive Search** is a **brute-force** method of solving problems by **enumerating all possible solutions** and selecting the one that satisfies the problem's constraints (or gives the best result).

In simple words:

> Exhaustive Search tries **every possible combination or arrangement** until it finds the correct or optimal one.

It guarantees a correct answer — but it can be **extremely slow** for large input sizes.

---

### 🔸 Characteristics

| Property         | Description                                             |
| :--------------- | :------------------------------------------------------ |
| **Approach**     | Tries all possible cases (brute-force)                  |
| **Completeness** | Always finds a solution if one exists                   |
| **Optimality**   | Finds the best solution (since all are checked)         |
| **Efficiency**   | Usually inefficient (very high time complexity)         |
| **Use Case**     | When input size is small or optimization is not crucial |

---

### 🔸 Example 1: Finding an Element (Simple Search)

If we want to find an element in a list, exhaustive search means:

> Check **every element** one by one until the target is found or the list ends.

✅ This is exactly what **Sequential Search** does — a simple form of Exhaustive Search.

---

### 🔸 Example 2: The Traveling Salesman Problem (TSP)

Given a set of cities and distances between them, find the shortest route that visits all cities exactly once and returns to the start.

**Exhaustive Search Approach:**

1. Generate **all possible permutations** of the cities.
2. For each permutation, calculate the **total travel cost**.
3. Choose the permutation with the **minimum cost**.

If there are `n` cities, there are `n!` (factorial) permutations —
so time complexity = **O(n!)**

#### Diagrammatically:

```
Cities: A, B, C, D
All possible routes:
A → B → C → D → A
A → B → D → C → A
A → C → B → D → A
...
Check all 24 (=4!) routes → Pick shortest
```

---

### 🔸 Example 3: Subset Sum Problem

Given a set of numbers, find if there exists a subset whose sum equals a given number `K`.

**Input:**
S = {3, 4, 5, 2}, K = 7

**Exhaustive Search Method:**
Generate all subsets and check their sums:

| Subset | Sum |
| :----- | :-- |
| { }    | 0   |
| {3}    | 3   |
| {4}    | 4   |
| {5}    | 5   |
| {2}    | 2   |
| {3,4}  | 7 ✅ |
| ...    | ... |

✅ Found a subset `{3,4}` that sums to 7.

---

### 🔸 Algorithm (Pseudocode for Subset Sum)

```
Algorithm ExhaustiveSubsetSum(S, n, K)
Input: Set S of n numbers, Target K
Output: True if subset sum = K exists, else False

1. for each subset of S do
2.     total ← sum of elements in subset
3.     if total = K then
4.         return True
5. return False
```

---

### 🔸 Real-World Applications

| Area                           | Example                              |
| :----------------------------- | :----------------------------------- |
| **Combinatorial Optimization** | Traveling Salesman, Knapsack Problem |
| **Cryptography**               | Brute-force key cracking             |
| **Game Solving**               | Trying all moves (e.g., Tic-Tac-Toe) |
| **Scheduling**                 | Trying all job assignments           |
| **Puzzle Solving**             | Sudoku brute-force solver            |

---

### 🔸 Time Complexity

Let the total number of possible solutions = `n`.

| Type                 | Description                            | Complexity                                              |
| :------------------- | :------------------------------------- | :------------------------------------------------------ |
| **General Case**     | Try all possible combinations          | **O(n!)**, **O(2ⁿ)**, or **O(n²)** depending on problem |
| **Space Complexity** | Depends on recursion or subset storage | Often **O(n)** or **O(2ⁿ)**                             |

---

### 🔸 Advantages

✅ Simple and easy to implement
✅ Always gives **correct and optimal** result
✅ Works for both **optimization** and **decision** problems

---

### 🔸 Disadvantages

❌ Very **slow** for large input sizes
❌ Consumes **high memory and computation**
❌ Impractical for real-time systems

---

### 🔸 Comparison: Exhaustive Search vs Optimized Search

| Criteria     | Exhaustive Search              | Optimized/Heuristic Search                |
| :----------- | :----------------------------- | :---------------------------------------- |
| **Method**   | Try all possibilities          | Use logic or pruning                      |
| **Accuracy** | 100% accurate                  | May approximate                           |
| **Speed**    | Very slow                      | Faster                                    |
| **Example**  | Subset generation, brute force | Dynamic Programming, Greedy, Backtracking |

---

### 🔹 Summary

> **Exhaustive Search** = “Try everything until something works.”

* Guarantees correctness ✅
* Extremely inefficient ❌
* Used when problem size is small or optimization is unnecessary.
* Forms the **foundation** for advanced techniques like:

  * **Backtracking**
  * **Branch and Bound**
  * **Dynamic Programming**

---

# 🔹 String Matching

### 🔸 Definition

**String Matching** (also called **Pattern Matching**) is the process of **finding occurrences of a pattern string** (called **Pattern `P`**) within a **larger text string** (called **Text `T`**).

In short:

> It checks **where and how many times a pattern appears** inside a text.

---

### 🔸 Example

#### 🧩 Example 1:

```
Text (T):     A B A C A B A B A
Pattern (P):      A B A
```

✅ The pattern `ABA` occurs **3 times** in the text (at indices 0, 4, and 6).

---

### 🔸 Applications of String Matching

| Area               | Example                              |
| :----------------- | :----------------------------------- |
| **Text Editors**   | “Find” and “Replace” operations      |
| **Search Engines** | Keyword matching                     |
| **Compilers**      | Lexical analysis (token recognition) |
| **Bioinformatics** | DNA pattern detection                |
| **Cybersecurity**  | Malware signature detection          |

---

## 🔹 Types of String Matching Algorithms

String matching algorithms are broadly divided into two types:

| Type                        | Description                                         | Example Algorithms                     |
| :-------------------------- | :-------------------------------------------------- | :------------------------------------- |
| **1. Naïve (Brute-Force)**  | Check pattern at every position in text             | Naïve algorithm                        |
| **2. Advanced (Optimized)** | Use preprocessing or heuristics to skip comparisons | KMP, Rabin-Karp, Boyer-Moore, Horspool |

---

## 🔹 1️⃣ Naïve (Brute-Force) String Matching Algorithm

### 🔸 Idea

Compare the pattern with every substring of the text of the same length.

### 🔸 Steps

1. Let `n` = length of Text `T`, `m` = length of Pattern `P`
2. For every possible shift `s` from `0` to `n-m`

   * Compare characters of `T[s...s+m-1]` with `P[0...m-1]`
3. If all characters match → record `s` as a **match position**.

---

### 🔸 Example

```
T = A B A C A B A B A
P = A B A
```

| Shift (s) | Substring of T | Match? |
| :-------: | :------------- | :----- |
|     0     | A B A          | ✅ Yes  |
|     1     | B A C          | ❌ No   |
|     2     | A C A          | ❌ No   |
|     3     | C A B          | ❌ No   |
|     4     | A B A          | ✅ Yes  |
|     5     | B A B          | ❌ No   |
|     6     | A B A          | ✅ Yes  |

✅ Matches found at positions **0, 4, and 6**

---

### 🔸 Pseudocode

```
Algorithm NaiveStringMatch(T, P)
Input: Text T of length n, Pattern P of length m
Output: All positions where P occurs in T

1. for s ← 0 to n - m do
2.     j ← 0
3.     while j < m and T[s + j] = P[j] do
4.         j ← j + 1
5.     if j = m then
6.         print "Pattern found at shift", s
```

---

### 🔸 Time Complexity

| Case             | Explanation                                       | Time                   |
| :--------------- | :------------------------------------------------ | :--------------------- |
| **Best Case**    | First characters don’t match                      | **O(n)**               |
| **Worst Case**   | Many partial matches (e.g., “AAAAA…A” vs “AAA…A”) | **O(m × n)**           |
| **Average Case** | Random text                                       | **O(m + n)** (approx.) |

**Space Complexity:** O(1)

---

### 🔸 Visualization Diagram

```
T: A B A C A B A B A
P: A B A
   ↑
→ Compare window with text, slide one position each time.
```

---

## 🔹 2️⃣ Optimized String Matching Algorithms (Overview)

These are improved versions of the naïve approach that **reduce unnecessary comparisons**.

| Algorithm                    | Core Idea                                                | Time Complexity       |
| :--------------------------- | :------------------------------------------------------- | :-------------------- |
| **Knuth–Morris–Pratt (KMP)** | Uses prefix table (partial match table) to skip rechecks | O(n + m)              |
| **Rabin–Karp**               | Uses hash values of substrings to match faster           | O(n + m), O(nm) worst |
| **Boyer–Moore**              | Starts comparison from the **end** of the pattern        | O(n/m) best           |
| **Horspool**                 | Simplified Boyer–Moore                                   | O(n) average          |

---

## 🔹 3️⃣ Real-Life Analogy

Think of finding a word in a book:

* **Naïve method:** Check every letter in every line.
* **Optimized methods (KMP/Boyer–Moore):**
  Use knowledge of what has already been matched to skip unnecessary checks.

---

## 🔹 Comparison of String Matching Algorithms

| Algorithm       | Approach                 | Preprocessing | Average Time | Worst Time |
| :-------------- | :----------------------- | :------------ | :----------- | :--------- |
| **Naïve**       | Brute-force              | None          | O(nm)        | O(nm)      |
| **KMP**         | Prefix-function          | O(m)          | O(n+m)       | O(n+m)     |
| **Rabin–Karp**  | Hashing                  | O(m)          | O(n+m)       | O(nm)      |
| **Boyer–Moore** | Right-to-left comparison | O(m+σ)        | O(n/m)       | O(nm)      |
| **Horspool**    | Simplified Boyer–Moore   | O(m+σ)        | O(n)         | O(nm)      |

(σ = alphabet size)

---

## 🔹 Advantages & Disadvantages

| Advantages                           | Disadvantages                         |
| :----------------------------------- | :------------------------------------ |
| Simple to implement (Naïve)          | Slow for large text                   |
| Works for all data types             | Repetitive comparisons                |
| Optimized methods (KMP, BM) are fast | Require preprocessing or extra memory |

---

## 🔹 Summary

| Concept                  | Meaning                                           |
| :----------------------- | :------------------------------------------------ |
| **Text (T)**             | The main string in which we search                |
| **Pattern (P)**          | The substring we want to find                     |
| **Naïve Matching**       | Check every position                              |
| **Efficient Algorithms** | KMP, Boyer–Moore, Rabin–Karp                      |
| **Best Use Case**        | Text search, pattern detection, token recognition |

---

# 🔹 Merge Sort

### 🔸 Definition

**Merge Sort** is a **Divide and Conquer sorting algorithm** that:

1. **Divides** the array into smaller subarrays,
2. **Sorts** each subarray,
3. **Merges** the sorted subarrays into one sorted array.

---

### 🔸 Core Idea (Divide and Conquer)

1. **Divide** – Split the array into two halves.
2. **Conquer** – Recursively sort both halves.
3. **Combine** – Merge the two sorted halves into one sorted array.

---

### 🔸 Example

#### Input:

```
[38, 27, 43, 3, 9, 82, 10]
```

#### Step 1: Divide

Split repeatedly into halves:

```
[38, 27, 43, 3, 9, 82, 10]
→ [38, 27, 43, 3] and [9, 82, 10]
→ [38, 27], [43, 3], [9, 82], [10]
→ [38], [27], [43], [3], [9], [82], [10]
```

#### Step 2: Conquer (Sort and Merge)

Now merge and sort each pair:

```
[38] [27] → [27, 38]
[43] [3]  → [3, 43]
[9] [82]  → [9, 82]
[10]      → [10]
```

#### Step 3: Combine (Merge)

Now merge sorted pairs again:

```
[27, 38] [3, 43] → [3, 27, 38, 43]
[9, 82] [10] → [9, 10, 82]
```

Finally merge both halves:

```
[3, 27, 38, 43] and [9, 10, 82]
→ [3, 9, 10, 27, 38, 43, 82]
```

✅ **Final Sorted Array: [3, 9, 10, 27, 38, 43, 82]**

---

### 🔸 Visualization Diagram

```
              [38,27,43,3,9,82,10]
                     /      \
           [38,27,43,3]     [9,82,10]
             /      \          /     \
         [38,27]  [43,3]    [9,82]  [10]
          /  \      /  \     /  \      \
        [38][27] [43][3]  [9][82]    [10]
          ↓    ↓    ↓   ↓    ↓   ↓      ↓
        [27,38] [3,43] [9,82] [10]
           ↓       ↓      ↓      ↓
        [3,27,38,43] [9,10,82]
               ↓         ↓
       [3,9,10,27,38,43,82]
```

---

## 🔹 Algorithm (Pseudocode)

```
Algorithm MergeSort(A, left, right)
1. if left < right then
2.     mid ← (left + right) / 2
3.     MergeSort(A, left, mid)
4.     MergeSort(A, mid+1, right)
5.     Merge(A, left, mid, right)

Algorithm Merge(A, left, mid, right)
1. Create two temporary arrays L[] and R[]
2. Copy data from A[left...mid] into L[]
   and A[mid+1...right] into R[]
3. i ← 0, j ← 0, k ← left
4. while i < size(L) and j < size(R)
       if L[i] ≤ R[j]
           A[k] ← L[i]; i++
       else
           A[k] ← R[j]; j++
       k++
5. Copy remaining elements of L[] or R[] if any
```

---

## 🔹 C Program Implementation

```c
#include <stdio.h>

void merge(int arr[], int left, int mid, int right) {
    int i = left, j = mid + 1, k = 0;
    int temp[right - left + 1];

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while (i <= mid)
        temp[k++] = arr[i++];
    while (j <= right)
        temp[k++] = arr[j++];

    for (i = left, k = 0; i <= right; i++, k++)
        arr[i] = temp[k];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

---

## 🔹 Time and Space Complexity

| Operation            | Complexity | Explanation                       |
| :------------------- | :--------- | :-------------------------------- |
| **Best Case**        | O(n log n) | Divide always happens             |
| **Average Case**     | O(n log n) | Independent of input order        |
| **Worst Case**       | O(n log n) | Always splits and merges          |
| **Space Complexity** | O(n)       | Temporary arrays used in merging  |
| **Stability**        | Stable     | Order of equal elements preserved |

---

### 🔸 Why O(n log n)?

Each level of recursion divides the array → `log₂n` levels
Each level processes all `n` elements (during merge)
So total = **n × log₂n**

---

### 🔸 Advantages

✅ Very stable and consistent O(n log n) performance
✅ Works efficiently on **large datasets**
✅ Excellent for **linked lists** (no random access issues)
✅ Can be easily parallelized

---

### 🔸 Disadvantages

❌ Requires **extra space** (O(n))
❌ Recursive overhead
❌ Not good for small arrays (Insertion Sort may be faster there)

---

## 🔹 Summary Table

| Property                    | Merge Sort                             |
| :-------------------------- | :------------------------------------- |
| **Algorithm Type**          | Divide and Conquer                     |
| **Best / Worst / Avg Time** | O(n log n)                             |
| **Space**                   | O(n)                                   |
| **In-place?**               | No                                     |
| **Stable?**                 | Yes                                    |
| **Recursive?**              | Yes                                    |
| **Use Case**                | Sorting linked lists, external sorting |

---

# **Quick Sort – Detailed Explanation**

### **1. Introduction**

Quick Sort is a **Divide and Conquer** sorting algorithm developed by **Tony Hoare** in 1960.
It is one of the most efficient sorting algorithms for large datasets.

---

### **2. Working Principle**

Quick Sort works in three major steps:

1. **Divide:** Select a pivot element from the array.
2. **Partition:** Rearrange elements so that:

   * All elements **less than pivot** go to the left.
   * All elements **greater than pivot** go to the right.
3. **Conquer:** Recursively apply the same process to the left and right subarrays.

---

### **3. Algorithm (Pseudo Code)**

```text
QuickSort(A, low, high)
1. if low < high then
2.     pivot ← Partition(A, low, high)
3.     QuickSort(A, low, pivot - 1)
4.     QuickSort(A, pivot + 1, high)
```

**Partition Function:**

```text
Partition(A, low, high)
1. pivot ← A[high]
2. i ← low - 1
3. for j ← low to high - 1 do
4.     if A[j] ≤ pivot then
5.         i ← i + 1
6.         swap A[i] ↔ A[j]
7. swap A[i + 1] ↔ A[high]
8. return i + 1
```

---

### **4. Example**

Let’s sort the array `[8, 4, 7, 3, 10, 2]`.

**Step 1:** Choose pivot = 2 (last element)
After partition → `[2, 4, 7, 3, 10, 8]`
Pivot (2) placed in correct position (index 0)

**Step 2:** Apply QuickSort on `[4, 7, 3, 10, 8]`
Choose pivot = 8 → after partition `[4, 7, 3, 8, 10]`

**Step 3:** Recursively repeat until sorted → `[2, 3, 4, 7, 8, 10]`

---

### **5. Characteristics**

| Feature             | Description              |
| ------------------- | ------------------------ |
| **Type**            | Divide and Conquer       |
| **In-place**        | Yes                      |
| **Stable**          | No                       |
| **Recursion**       | Used                     |
| **Pivot Selection** | Critical for performance |

---

### **6. Time Complexity Analysis**

| Case             | Description                               | Time Complexity |
| ---------------- | ----------------------------------------- | --------------- |
| **Best Case**    | Pivot divides array into two equal halves | $O(n \log n)$   |
| **Average Case** | Random pivot selections                   | $O(n \log n)$   |
| **Worst Case**   | Pivot always smallest/largest element     | $O(n^2)$        |

---

### **7. Space Complexity**

* **Auxiliary Space:** $O(\log n)$ (for recursion stack)
* **In-place sorting:** Yes (no extra array used)

---

### **8. Advantages**

✅ Faster than Merge Sort and Heap Sort in practice
✅ In-place sorting (no extra memory)
✅ Divide-and-conquer principle makes it efficient

---

### **9. Disadvantages**

❌ Not stable (relative order not preserved)
❌ Worst-case $O(n^2)$ time if pivot selection is poor

---

### **10. Applications**

* Used in system libraries (C, C++, Java)
* Suitable for **large datasets**
* Used in quickselect (to find kth smallest/largest element)

---

### **Graphical Representation (Conceptual)**

```
              [8, 4, 7, 3, 10, 2]
                      |
                     (2)
                    /   \
                 []     [4,7,3,10,8]
                         |
                        (8)
                       /   \
                [4,7,3]    [10]
                   |
                  (3)
                 /   \
              []     [4,7]
                      |
                     (7)
                    /   \
                 [4]    []
```

---

# **Binary Search – Detailed Explanation**

---

### **1. Introduction**

**Binary Search** is a highly efficient algorithm used to find an element in a **sorted array**.
It works on the **Divide and Conquer** principle — repeatedly dividing the search interval in half.

---

### **2. Working Principle**

1. Start with the **middle element** of the array.
2. If the target value equals the middle element → **found**.
3. If the target value is **less than** the middle element → search in the **left half**.
4. If the target value is **greater than** the middle element → search in the **right half**.
5. Repeat until the element is found or the search range becomes empty.

---

### **3. Algorithm (Pseudo Code)**

#### **Iterative Version**

```text
BinarySearch(A, n, key)
1. low ← 0
2. high ← n - 1
3. while low ≤ high do
4.     mid ← (low + high) / 2
5.     if A[mid] = key then
6.         return mid
7.     else if A[mid] < key then
8.         low ← mid + 1
9.     else
10.        high ← mid - 1
11. return -1  // not found
```

#### **Recursive Version**

```text
BinarySearchRecursive(A, low, high, key)
1. if low > high then
2.     return -1
3. mid ← (low + high) / 2
4. if A[mid] = key then
5.     return mid
6. else if A[mid] < key then
7.     return BinarySearchRecursive(A, mid + 1, high, key)
8. else
9.     return BinarySearchRecursive(A, low, mid - 1, key)
```

---

### **4. Example**

Array: `[2, 4, 6, 8, 10, 12, 14, 16]`
Key to find = `10`

| Step | low | high | mid | A[mid] | Action            |
| ---- | --- | ---- | --- | ------ | ----------------- |
| 1    | 0   | 7    | 3   | 8      | 10 > 8 → go right |
| 2    | 4   | 7    | 5   | 12     | 10 < 12 → go left |
| 3    | 4   | 4    | 4   | 10     | Found ✅           |

**Result:** Element `10` found at index `4`.

---

### **5. Time Complexity**

| Case             | Complexity  | Description                         |
| ---------------- | ----------- | ----------------------------------- |
| **Best Case**    | $O(1)$      | Element found at the first check    |
| **Average Case** | $O(\log n)$ | Divides array into halves each step |
| **Worst Case**   | $O(\log n)$ | Element not found after all splits  |

---

### **6. Space Complexity**

* **Iterative Version:** $O(1)$
* **Recursive Version:** $O(\log n)$ (due to recursion stack)

---

### **7. Important Characteristics**

| Property          | Description                  |
| ----------------- | ---------------------------- |
| **Works on**      | Sorted arrays only           |
| **Technique**     | Divide and Conquer           |
| **In-place**      | Yes                          |
| **Stability**     | Not applicable (not sorting) |
| **Deterministic** | Yes                          |

---

### **8. Advantages**

✅ Very fast compared to Linear Search
✅ Reduces the number of comparisons to logarithmic order
✅ Efficient for large datasets

---

### **9. Disadvantages**

❌ Requires the array to be sorted beforehand
❌ Not suitable for dynamic or unsorted data

---

### **10. Graphical Representation**

```
Array: [2, 4, 6, 8, 10, 12, 14, 16]
Target: 10

Step 1: mid = 3 → A[mid] = 8 → search right
          [2, 4, 6, (8), 10, 12, 14, 16]
                         ↑

Step 2: mid = 5 → A[mid] = 12 → search left
          [2, 4, 6, 8, (10), 12, 14, 16]
                        ↑

Found 10 at index 4 ✅
```

---

### **11. Real-Life Applications**

* Searching names in a **dictionary** or **contacts list**
* Looking up records in a **sorted database**
* Finding elements in **sorted arrays** (used in libraries, e.g., `bisect` in Python, `std::binary_search` in C++)

---

# 🧩 **Insertion Sort – Detailed Explanation**

---

### **1. Introduction**

**Insertion Sort** is a simple sorting algorithm based on the way we **sort playing cards** in our hands — one card at a time.
It is part of the **Decrease and Conquer** strategy family.

The algorithm builds the **sorted list one element at a time**, by picking the next element and **inserting** it into the correct position within the already-sorted part.

---

### **2. Working Principle**

1. Start from the **second element** (index = 1).
2. Compare the current element with the elements **before it**.
3. **Shift** all elements greater than the current element to the right.
4. Insert the current element into its **correct position**.
5. Repeat until all elements are sorted.

---

### **3. Pseudocode**

```text
InsertionSort(A, n)
1. for i ← 1 to n-1 do
2.     key ← A[i]
3.     j ← i - 1
4.     while j ≥ 0 and A[j] > key do
5.         A[j + 1] ← A[j]      // shift right
6.         j ← j - 1
7.     A[j + 1] ← key
8. end for
```

---

### **4. Example**

Let’s sort this array:
`A = [8, 5, 3, 9, 1]`

| Pass | Key | Comparison                                                 | Array after pass |
| ---- | --- | ---------------------------------------------------------- | ---------------- |
| 1    | 5   | 8 > 5 → shift                                              | [5, 8, 3, 9, 1]  |
| 2    | 3   | 8 > 3 → shift, 5 > 3 → shift                               | [3, 5, 8, 9, 1]  |
| 3    | 9   | 8 < 9 → no shift                                           | [3, 5, 8, 9, 1]  |
| 4    | 1   | 9 > 1 → shift, 8 > 1 → shift, 5 > 1 → shift, 3 > 1 → shift | [1, 3, 5, 8, 9]  |

✅ Final Sorted Array: `[1, 3, 5, 8, 9]`

---

### **5. Diagrammatic Representation**

```
Initial: [8, 5, 3, 9, 1]

Pass 1: [5, 8, 3, 9, 1]
Pass 2: [3, 5, 8, 9, 1]
Pass 3: [3, 5, 8, 9, 1]  (no change)
Pass 4: [1, 3, 5, 8, 9]
```

---

### **6. Time Complexity**

| Case             | Comparisons & Shifts                            | Time Complexity |
| ---------------- | ----------------------------------------------- | --------------- |
| **Best Case**    | $(n - 1)$ comparisons (already sorted)          | **O(n)**        |
| **Average Case** | About $\dfrac{n^2}{4}$ comparisons              | **O(n²)**       |
| **Worst Case**   | $\dfrac{n(n-1)}{2}$ comparisons (reverse order) | **O(n²)**       |

---

### **7. Space Complexity**

* **O(1)** (in-place sorting, no extra memory used)

---

### **8. Characteristics**

| Property              | Description                                   |
| --------------------- | --------------------------------------------- |
| **Algorithm Type**    | Decrease and Conquer                          |
| **In-place**          | ✅ Yes                                         |
| **Stable**            | ✅ Yes (does not change equal elements’ order) |
| **Adaptive**          | ✅ Performs better on partially sorted data    |
| **Recursive version** | Possible but less common                      |

---

### **9. Advantages**

✅ Simple and easy to implement
✅ Efficient for **small** or **partially sorted arrays**
✅ Requires **no extra memory**
✅ **Stable sorting**

---

### **10. Disadvantages**

❌ Inefficient for **large datasets** (O(n²))
❌ Slower than more advanced sorts like **Merge Sort** or **Quick Sort**

---

### **11. Real-Life Analogy**

> Sorting cards in your hand —
> You pick one card at a time and insert it into its correct position relative to already sorted cards.

---

### **12. Turbo C Compatible C Program**

```c
#include <stdio.h>

void insertionSort(int a[], int n) {
    int i, j, key;
    for (i = 1; i < n; i++) {
        key = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

int main() {
    int a[5] = {8, 5, 3, 9, 1};
    int n = 5;

    printf("Before sorting: ");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);

    insertionSort(a, n);

    printf("\nAfter sorting:  ");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);

    return 0;
}
```

---

### **13. Output**

```
Before sorting: 8 5 3 9 1
After sorting:  1 3 5 8 9
```

---

### **14. Comparison Table**

| Algorithm          | Technique          | Best Case | Average Case | Worst Case | Space | Stable |
| ------------------ | ------------------ | --------- | ------------ | ---------- | ----- | ------ |
| **Selection Sort** | Brute Force        | O(n²)     | O(n²)        | O(n²)      | O(1)  | ❌      |
| **Bubble Sort**    | Brute Force        | O(n)      | O(n²)        | O(n²)      | O(1)  | ✅      |
| **Insertion Sort** | Decrease & Conquer | O(n)      | O(n²)        | O(n²)      | O(1)  | ✅      |

---

# 🧭 **Depth First Search (DFS) and Breadth First Search (BFS)**

---

## 🌐 **1. Introduction**

Both **DFS** and **BFS** are **graph traversal algorithms** — methods to **visit all the vertices (nodes)** of a graph systematically.

They differ in the **order** in which nodes are explored:

| Traversal | Strategy                                                  |
| --------- | --------------------------------------------------------- |
| **DFS**   | Explore **as deep as possible** before backtracking       |
| **BFS**   | Explore **all immediate neighbors first**, then go deeper |

---

## 🧩 **2. Representing a Graph**

A graph `G` can be represented using:

1. **Adjacency Matrix**

   * A 2D array where `A[i][j] = 1` if there’s an edge from vertex `i` to `j`.
2. **Adjacency List**

   * An array of linked lists or vectors where each list represents connected vertices.

Example Graph:

```
A ---- B
|      |
|      |
C ---- D
```

Adjacency List:

```
A: B, C
B: A, D
C: A, D
D: B, C
```

---

## 🔍 **3. Depth First Search (DFS)**

### **Concept:**

DFS starts from a vertex and explores **as far as possible** along each branch before **backtracking**.

It uses a **stack** (explicitly or via recursion).

---

### **Algorithm (Recursive Pseudocode)**

```text
DFS(G, v)
1. mark v as visited
2. for each vertex u in adjacency list of v do
3.     if u is not visited then
4.         DFS(G, u)
```

---

### **Algorithm (Iterative Pseudocode)**

```text
DFS_Iterative(G, v)
1. create an empty stack S
2. push v into S
3. while S is not empty do
4.     node ← pop(S)
5.     if node not visited then
6.         mark node visited
7.         push all unvisited neighbors of node into S
```

---

### **Example**

Graph:

```
     A
   /   \
  B     C
  |     |
  D-----E
```

Adjacency List:

```
A: B, C
B: A, D
C: A, E
D: B, E
E: C, D
```

**Starting Vertex:** A

**DFS Traversal Order:**
A → B → D → E → C

---

### **DFS Visualization**

```
A
|
B
|
D
|
E
|
C
```

(DFS goes deep, visiting one path before trying another)

---

### **Time and Space Complexity**

| Operation | Complexity                   |
| --------- | ---------------------------- |
| **Time**  | O(V + E)                     |
| **Space** | O(V) (stack + visited array) |

---

## 🧭 **4. Breadth First Search (BFS)**

### **Concept:**

BFS starts from a vertex and explores **all neighbors first**, before going deeper into their neighbors.

It uses a **queue** data structure.

---

### **Algorithm (Pseudocode)**

```text
BFS(G, start)
1. create a queue Q
2. mark start as visited
3. enqueue(start)
4. while Q not empty do
5.     v ← dequeue(Q)
6.     for each neighbor u of v do
7.         if u not visited then
8.             mark u visited
9.             enqueue(u)
```

---

### **Example**

Using the same graph:

```
     A
   /   \
  B     C
  |     |
  D-----E
```

**Starting Vertex:** A

**BFS Traversal Order:**
A → B → C → D → E

---

### **BFS Visualization**

```
Level 0: A
Level 1: B, C
Level 2: D, E
```

(Visits all vertices at the same depth first, before moving to the next)

---

### **Time and Space Complexity**

| Operation | Complexity                   |
| --------- | ---------------------------- |
| **Time**  | O(V + E)                     |
| **Space** | O(V) (queue + visited array) |

---

## ⚖️ **5. DFS vs BFS Comparison**

| Feature              | **DFS**                                            | **BFS**                                                  |
| -------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| **Data Structure**   | Stack / Recursion                                  | Queue                                                    |
| **Approach**         | Depth-wise                                         | Level-wise                                               |
| **Use Case**         | Path finding, cycle detection, topological sorting | Shortest path (unweighted graphs), level order traversal |
| **Space Efficiency** | Better for sparse graphs                           | Better for dense graphs                                  |
| **Completeness**     | May not find shortest path                         | Always finds shortest path (unweighted)                  |
| **Implementation**   | Recursive or Iterative                             | Iterative                                                |

---

## 💡 **6. Example Programs in C**

### **(a) DFS (Recursive)**

```c
#include <stdio.h>

int adj[10][10], visited[10], n;

void DFS(int v) {
    visited[v] = 1;
    printf("%d ", v);
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i])
            DFS(i);
    }
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    printf("DFS Traversal starting from vertex 0: ");
    DFS(0);
    return 0;
}
```

---

### **(b) BFS**

```c
#include <stdio.h>

int adj[10][10], visited[10], n;

void BFS(int start) {
    int queue[10], front = 0, rear = -1;
    visited[start] = 1;
    queue[++rear] = start;

    while (front <= rear) {
        int v = queue[front++];
        printf("%d ", v);
        for (int i = 0; i < n; i++) {
            if (adj[v][i] && !visited[i]) {
                queue[++rear] = i;
                visited[i] = 1;
            }
        }
    }
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    printf("BFS Traversal starting from vertex 0: ");
    BFS(0);
    return 0;
}
```

---

### **Example Input (Adjacency Matrix)**

```
5
0 1 1 0 0
1 0 0 1 0
1 0 0 0 1
0 1 0 0 1
0 0 1 1 0
```

**DFS Output:** `0 1 3 4 2`
**BFS Output:** `0 1 2 3 4`

---

## 🧠 **7. Real-Life Applications**

| Algorithm | Real-life Use                                                       |
| --------- | ------------------------------------------------------------------- |
| **DFS**   | Solving mazes, topological sorting, cycle detection, puzzle solving |
| **BFS**   | Finding shortest path in unweighted graphs (e.g., maps, networks)   |

---

## 🧭 **8. Visual Comparison Diagram**

```
Graph:
    A
   / \
  B   C
  |   |
  D - E

DFS: A → B → D → E → C
BFS: A → B → C → D → E
```

---

# 🧩 **Topological Sorting (Topological Order)**

---

## 🧠 **1. Introduction**

**Topological Sorting** is a **linear ordering** of the **vertices** of a **Directed Acyclic Graph (DAG)** such that:

> For every directed edge **u → v**, vertex **u** appears **before** vertex **v** in the ordering.

---

### ⚙️ **Example:**

If there’s an edge `A → B`,
then in the topological order, `A` **must come before** `B`.

---

### ✅ **Applicable Only To:**

* **Directed** graphs
* **Acyclic** graphs (no cycles)

If a cycle exists → **Topological sort is not possible**.

---

## 📘 **2. Real-Life Example**

Topological sorting is used when one task **depends** on another.
For example:

| Task         | Depends on     |
| ------------ | -------------- |
| Build walls  | Lay foundation |
| Paint walls  | Build walls    |
| Install roof | Build walls    |

One valid **topological order** is:
`Lay foundation → Build walls → Paint walls → Install roof`

---

## 🔢 **3. Algorithm Approaches**

There are **two major algorithms** for Topological Sorting:

| Method                  | Based on                 |
| ----------------------- | ------------------------ |
| **1. DFS-Based Method** | Uses recursion and stack |
| **2. Kahn’s Algorithm** | Uses indegree and queue  |

---

## ⚙️ **4. DFS-Based Topological Sort**

### **Concept:**

1. Perform **DFS** on the graph.
2. After exploring all edges from a vertex `v`, **push `v` onto a stack**.
3. When DFS finishes for all vertices, **pop all vertices** from the stack → gives **topological order**.

---

### **Pseudocode**

```text
TopologicalSort_DFS(G)
1. Mark all vertices as not visited
2. For each vertex v in G:
3.     if v not visited:
4.         DFS(v)

DFS(v)
1. Mark v as visited
2. For each neighbor u of v:
3.     if u not visited:
4.         DFS(u)
5. Push v onto stack
```

Finally, pop all elements from the stack to get the **topological order**.

---

### **Example**

Graph:

```
   5 → 0 ← 4
   ↓
   2 → 3 → 1
```

Adjacency List:

```
5: 0, 2
4: 0, 1
2: 3
3: 1
0: -
1: -
```

---

#### **Step-by-step DFS traversal**

| Step                   | Visited                         | Stack                      |
| ---------------------- | ------------------------------- | -------------------------- |
| Visit 5 → 0, 2         | 5, 0, 2                         |                            |
| 2 → 3 → 1              | 5, 0, 2, 3, 1                   |                            |
| Backtrack & Push order | Push in order: 1, 3, 2, 0, 4, 5 | Stack = [1, 3, 2, 0, 4, 5] |

**Topological Order:**
`5 → 4 → 2 → 3 → 1 → 0`

(One of many possible valid orders)

---

### **Visualization**

```
5 → 0
↓
2 → 3 → 1
4 → 0
4 → 1
```

Topological order ensures:

* 5 appears before 0, 2
* 2 appears before 3
* 3 appears before 1
* 4 appears before 0, 1

---

## 🧮 **5. Kahn’s Algorithm (BFS-Based Approach)**

### **Concept:**

Uses the idea of **in-degree** (number of incoming edges).

Steps:

1. Compute **in-degree** of all vertices.
2. Enqueue all vertices with in-degree **0**.
3. Dequeue vertex `v` → output it.
4. For every neighbor `u` of `v`, **reduce in-degree** of `u` by 1.
5. If any vertex’s in-degree becomes 0 → enqueue it.
6. Repeat until the queue is empty.

If all vertices are output → topological sort successful.
If not → graph has a **cycle**.

---

### **Pseudocode**

```text
Kahn_Topological_Sort(G)
1. Compute indegree[v] for all vertices
2. Enqueue all vertices with indegree[v] = 0
3. while queue not empty:
4.     v = dequeue()
5.     print v
6.     for each neighbor u of v:
7.         indegree[u]--
8.         if indegree[u] == 0:
9.             enqueue(u)
```

---

### **Example**

Using the same graph:

```
5 → 0 ← 4
↓
2 → 3 → 1
```

| Vertex | In-degree |
| ------ | --------- |
| 0      | 2         |
| 1      | 2         |
| 2      | 1         |
| 3      | 1         |
| 4      | 0         |
| 5      | 0         |

**Initial Queue:** [4, 5]

**Processing Steps:**

| Step | Dequeued | Queue | Output        | Updated In-degree |
| ---- | -------- | ----- | ------------- | ----------------- |
| 1    | 4        | [5]   | [4]           | 0:1, 1:1          |
| 2    | 5        | []    | [4,5]         | 0:0, 2:0          |
| 3    | 0        | [2]   | [4,5,0]       | —                 |
| 4    | 2        | []    | [4,5,0,2]     | 3:0               |
| 5    | 3        | []    | [4,5,0,2,3]   | 1:0               |
| 6    | 1        | []    | [4,5,0,2,3,1] | —                 |

✅ **Topological Order:** `4 → 5 → 0 → 2 → 3 → 1`

---

## ⏱️ **6. Time and Space Complexity**

| Method           | Time     | Space                   |
| ---------------- | -------- | ----------------------- |
| **DFS-Based**    | O(V + E) | O(V) (stack + visited)  |
| **Kahn’s (BFS)** | O(V + E) | O(V) (queue + indegree) |

---

## ⚖️ **7. Comparison: DFS vs Kahn’s**

| Feature             | **DFS Method**             | **Kahn’s Algorithm**                |
| ------------------- | -------------------------- | ----------------------------------- |
| **Approach**        | Uses recursion + stack     | Uses queue + in-degree              |
| **Implementation**  | Easier recursively         | Easier iteratively                  |
| **Cycle Detection** | Indirect                   | Direct (if not all nodes processed) |
| **Memory Use**      | Stack                      | Queue                               |
| **Order**           | Reverse of finishing times | Order of zero in-degree             |

---

## 🧠 **8. Applications**

✅ **Task scheduling** (e.g., compiler dependency resolution)
✅ **Build systems** (resolving file compile order)
✅ **Course prerequisite ordering**
✅ **Dependency management** (e.g., package installation order)
✅ **Finding cycles** in directed graphs

---

## 💻 **9. Turbo C Compatible Program (DFS Method)**

```c
#include <stdio.h>

int adj[10][10], visited[10], n;
int stack[10], top = -1;

void DFS(int v) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i])
            DFS(i);
    }
    stack[++top] = v;
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    for (int i = 0; i < n; i++)
        visited[i] = 0;

    for (int i = 0; i < n; i++)
        if (!visited[i])
            DFS(i);

    printf("Topological Order: ");
    while (top != -1)
        printf("%d ", stack[top--]);

    return 0;
}
```

---

### **Example Input:**

```
6
0 0 0 0 0 0
1 0 0 0 0 0
1 1 0 0 0 0
0 1 1 0 0 0
0 0 1 1 0 0
0 0 0 1 1 0
```

### **Output:**

```
Topological Order: 5 4 3 2 1 0
```

---

## 🎯 **10. Summary Table**

| Concept          | Description                       |
| ---------------- | --------------------------------- |
| Graph Type       | Directed Acyclic Graph (DAG)      |
| Goal             | Linear order of vertices          |
| Techniques       | DFS (stack) or Kahn’s (queue)     |
| Time Complexity  | O(V + E)                          |
| Space Complexity | O(V)                              |
| Applications     | Scheduling, dependency resolution |

---

# **String Matching Algorithms**

## **1. Introduction**

**String Matching** (also known as **Pattern Matching**) is the process of finding occurrences of a **substring (pattern)** within a **larger string (text)**.

### **Example**

```
Text:     A B C D A B C A B D
Pattern:      A B C
```

✅ Occurrences of the pattern “ABC” in the text start at index **0** and **4**.

String matching is fundamental in:

* Text editors (search operations)
* Search engines
* DNA sequence analysis
* Network intrusion detection
* Data mining

---

## **2. Classification of String Matching Algorithms**

String matching algorithms can be divided into two main types:

| **Type**                 | **Description**                                              | **Examples**                                                |
| ------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------- |
| **Naïve / Brute Force**  | Checks for the pattern starting at each position in the text | Naïve String Matching                                       |
| **Efficient / Advanced** | Uses preprocessing to skip unnecessary comparisons           | Knuth–Morris–Pratt (KMP), Boyer–Moore, Rabin–Karp, Horspool |

---

## **3. Naïve String Matching Algorithm**

### **Idea:**

Simply slide the pattern one by one and check for a match at every position.

### **Pseudocode:**

```text
NaiveStringMatch(T, P)
Input: Text T of length n, Pattern P of length m
Output: All starting indices where P is found in T

for i = 0 to n - m
    j = 0
    while (j < m) and (T[i + j] == P[j])
        j = j + 1
    if j == m
        print "Pattern found at index", i
```

### **Example:**

```
Text   = A B A B A B A
Pattern= A B A

→ Compare from i = 0:
   A B A ✅ match (index 0)
→ i = 1: B A B ❌
→ i = 2: A B A ✅ match (index 2)
→ i = 3: B A B ❌
→ i = 4: A B A ✅ match (index 4)
```

### **Time Complexity:**

* **Best Case:** O(n)
* **Worst Case:** O(n × m)
* **Space Complexity:** O(1)

---

## **4. Efficient String Matching Algorithms**

To improve efficiency, more advanced algorithms avoid redundant comparisons.

---

### **4.1. Rabin–Karp Algorithm**

Uses **hashing** for faster pattern comparison.

### **Idea:**

Compute hash values for the pattern and for substrings of the text of the same length.
If hashes match, then compare the actual strings.

### **Pseudocode:**

```text
RabinKarp(T, P, d, q)
n ← length(T)
m ← length(P)
h ← d^(m-1) mod q
p ← 0
t0 ← 0

for i = 0 to m-1
    p ← (d*p + P[i]) mod q
    t0 ← (d*t0 + T[i]) mod q

for s = 0 to n - m
    if p == ts
        if P[0..m-1] == T[s..s+m-1]
            print "Pattern found at shift", s
    if s < n - m
        ts+1 ← (d*(ts - T[s]*h) + T[s+m]) mod q
```

### **Complexity:**

* **Average Case:** O(n + m)
* **Worst Case:** O(nm)

---

### **4.2. Knuth–Morris–Pratt (KMP) Algorithm**

Avoids re-checking characters that have already matched.

### **Idea:**

Preprocess the pattern to compute a **prefix table (LPS array)** that indicates how many characters can be skipped when a mismatch occurs.

#### **Example:**

```
Pattern: A B A B A C
LPS:     0 0 1 2 3 0
```

### **Pseudocode:**

```text
KMP(T, P)
Compute LPS array for pattern P
i ← 0, j ← 0
while i < length(T)
    if P[j] == T[i]
        i++, j++
        if j == length(P)
            print "Pattern found at", i-j
            j ← LPS[j-1]
    else
        if j != 0
            j ← LPS[j-1]
        else
            i++
```

### **Complexity:**

* **Preprocessing:** O(m)
* **Matching:** O(n)
* **Total:** O(n + m)

---

### **4.3. Boyer–Moore Algorithm**

This is one of the **fastest string-matching algorithms** in practice.

### **Idea:**

Compare pattern characters from **right to left**.
Use two heuristics:

1. **Bad Character Rule** – if a mismatch occurs, shift pattern so that mismatched character aligns with last occurrence of that character in the pattern.
2. **Good Suffix Rule** – use information about matched suffixes to skip comparisons.

### **Example Diagram:**

```
Text:    A B A A B A C A B A B A
Pattern:     A B A C
             ↑ mismatch (compare from right)
```

When mismatch occurs, shift pattern intelligently instead of moving just one step.

### **Complexity:**

* **Best Case:** O(n/m)
* **Worst Case:** O(n + m)
* **Practical Performance:** Very fast on large texts.

---

### **4.4. Horspool’s Algorithm**

A **simplified version** of Boyer–Moore using only the **bad character rule**.

---

## **5. Comparison Table**

| Algorithm   | Best Case | Worst Case | Average  | Technique                          |
| ----------- | --------- | ---------- | -------- | ---------------------------------- |
| Naïve       | O(n)      | O(nm)      | O(nm)    | Brute Force                        |
| Rabin–Karp  | O(n + m)  | O(nm)      | O(n + m) | Hashing                            |
| KMP         | O(n + m)  | O(n + m)   | O(n + m) | Prefix Table                       |
| Boyer–Moore | O(n/m)    | O(n + m)   | O(n/m)   | Heuristic (Bad Char + Good Suffix) |
| Horspool    | O(n/m)    | O(nm)      | O(n/m)   | Simplified Heuristic               |

---

## **6. Visualization (Comparison of Shifts)**

```
Text:   A B C A B A B C A B A C
Pattern:    A B A C

Naïve:   Shifts 1 by 1  → O(nm)
KMP:     Skips using prefix table → O(n+m)
BM:      Large jumps on mismatch → Fastest in practice
```

---

## **7. Summary**

| Concept         | Description                                     |
| --------------- | ----------------------------------------------- |
| **Goal**        | Find pattern occurrences in text                |
| **Naïve**       | Simple, slow                                    |
| **KMP**         | Efficient for predictable patterns              |
| **Rabin–Karp**  | Uses hashing for multiple pattern matching      |
| **Boyer–Moore** | Best in practice, skips unnecessary comparisons |
| **Horspool**    | Simplified Boyer–Moore                          |

---

# 🧩 **Horspool’s Algorithm (Simplified Boyer–Moore Algorithm)**

---

## **1. Introduction**

The **Horspool Algorithm** is an **improved string matching algorithm**, derived from the **Boyer–Moore algorithm**.

It is **simpler** and **faster** in most practical cases, especially when working with **large texts** and **small patterns**.

---

## **2. Idea / Intuition**

Instead of comparing the pattern from **left to right**, Horspool compares it **right to left**, and when a mismatch happens —
it **skips multiple characters** based on the **bad character rule**.

It **uses only one heuristic** from Boyer–Moore:

> 🔹 **Bad Character Heuristic**

This makes it easy to implement and efficient.

---

## **3. Basic Terminology**

Let’s define:

* `T` → **Text** of length `n`
* `P` → **Pattern** of length `m`
* Alphabet set → Σ (e.g., A–Z)

The algorithm tries to align the pattern `P` with `T` and compares from **rightmost character** to **leftmost**.

---

## **4. Preprocessing Step: Shift Table**

Horspool precomputes a **shift table** that tells how far to move the pattern when a mismatch occurs.

### **Computation Rule:**

For every character `c` in the alphabet:

```
shift[c] = m
```

Then for each character in the pattern **except the last one**:

```
shift[P[i]] = m - i - 1
```

---

### **Example:**

Let

```
Pattern P = "TEST"
Length m = 4
```

| Character | Index (i) | Shift Value = m - i - 1 |
| --------- | --------- | ----------------------- |
| T         | 0         | 3                       |
| E         | 1         | 2                       |
| S         | 2         | 1                       |

Then fill others (not in pattern) as `m = 4`.

✅ **Final Shift Table:**

| Character | Shift |
| --------- | ----- |
| T         | 3     |
| E         | 2     |
| S         | 1     |
| Others    | 4     |

---

## **5. Matching Phase (Right-to-Left Comparison)**

### **Steps:**

1. Align the pattern `P` with the start of the text `T`.
2. Compare characters from **right to left**.
3. If a **mismatch** occurs, look up the **shift value** for the mismatched text character.
4. Shift the pattern accordingly.
5. Repeat until the text ends.

---

### **Example**

```
Text   = G O T O T E S T E R
Pattern=     T E S T
```

### Step-by-step:

| Step | Comparison                                  | Mismatch | Shift (from table) | New Position |
| ---- | ------------------------------------------- | -------- | ------------------ | ------------ |
| 1    | Compare TEST with GOTO → mismatch at T vs O | O        | shift['O'] = 4     | Move 4 right |
| 2    | Compare TEST with OTES → mismatch at T vs O | O        | shift['O'] = 4     | Move 4 right |
| 3    | Compare TEST with TEST → ✅ full match       | —        | Print position     | Move 4 right |
| 4    | Compare TEST with STER → mismatch at T vs R | R        | shift['R'] = 4     | Move 4 right |
| —    | End                                         | —        | —                  | —            |

✅ **Match found at position 4.**

---

## **6. Algorithm (Pseudocode)**

```text
Horspool_String_Match(T, P)
Input: Text T of length n, Pattern P of length m
Output: All occurrences of P in T

1. Construct shift table for pattern P
2. s ← 0
3. while s ≤ n - m do
4.     j ← m - 1
5.     while j ≥ 0 and P[j] == T[s + j] do
6.         j ← j - 1
7.     if j < 0 then
8.         print "Pattern found at shift", s
9.     s ← s + shift[T[s + m - 1]]
```

---

## **7. Example Walkthrough**

Let’s use:

```
Text:     A B C D A B C A B D
Pattern:  A B C
```

### **Shift Table**

| Char   | Shift |
| ------ | ----- |
| A      | 2     |
| B      | 1     |
| C      | 3     |
| Others | 3     |

---

### **Tracing**

```
i = 0: compare ABC vs ABC ✅ match (index 0)
Shift = shift['C'] = 3
i = 3: compare DAB vs ABC ❌ mismatch at B vs A
Shift = shift['B'] = 1
i = 4: compare ABC vs ABC ✅ match (index 4)
Shift = shift['C'] = 3
i = 7: beyond limit → stop
```

✅ Matches at indices **0** and **4**.

---

## **8. Time Complexity**

| Case                 | Description                         | Complexity                      |
| -------------------- | ----------------------------------- | ------------------------------- |
| **Best Case**        | Pattern found quickly (large skips) | O(n/m)                          |
| **Average Case**     | Typical case                        | O(n)                            |
| **Worst Case**       | Repeated characters (e.g., AAAAA)   | O(n × m)                        |
| **Space Complexity** | Shift table                         | O(k) where k = size of alphabet |

---

## **9. Advantages**

✅ Simple to implement
✅ Fast in practice for large text and small patterns
✅ Uses minimal preprocessing

---

## **10. Limitations**

❌ Inefficient when alphabet is small (like binary data)
❌ Doesn’t use the “good suffix” heuristic of Boyer–Moore
❌ Can still be slower for certain repetitive patterns

---

## **11. Comparison Table**

| Algorithm   | Uses Bad Character | Uses Good Suffix | Complexity | Remarks                      |
| ----------- | ------------------ | ---------------- | ---------- | ---------------------------- |
| Naïve       | ❌                  | ❌                | O(nm)      | Basic                        |
| KMP         | ❌                  | ❌                | O(n+m)     | Deterministic                |
| Boyer–Moore | ✅                  | ✅                | O(n/m)     | Best theoretical             |
| Horspool    | ✅                  | ❌                | O(n)       | Simplified, fast in practice |

---

## **12. Visualization**

```
Text:   H E L L O W O R L D
Pattern:    W O R L D
Compare from rightmost character (D)
↓
Mismatch? → Shift using table value.
Match? → Report index.
```

---

## ✅ **Summary**

| Concept                     | Description                                     |
| --------------------------- | ----------------------------------------------- |
| **Type**                    | Simplified Boyer–Moore                          |
| **Heuristic Used**          | Bad Character                                   |
| **Direction of Comparison** | Right → Left                                    |
| **Preprocessing**           | Shift Table                                     |
| **Time Complexity**         | O(n) average                                    |
| **Applications**            | Search engines, word processors, bioinformatics |

---

# Boyer–Moore Algorithm — complete, practical explanation

Boyer–Moore (BM) is one of the fastest practical string-matching algorithms. It compares the pattern to the text **right-to-left** and uses **two powerful heuristics** to skip large parts of the text:

* **Bad-character rule** — when a mismatch occurs, shift the pattern so the mismatched text character aligns with its last occurrence in the pattern (or skip past it if it doesn’t occur).
* **Good-suffix rule** — when a suffix of the pattern matched but a mismatch happens before it, shift the pattern so that a matching occurrence of that suffix (or a border of it) lines up, or shift to align the longest prefix if no occurrence exists.

When both heuristics are implemented properly, Boyer–Moore is very fast in practice (often sublinear on average) and can be implemented to run in **linear time** (O(n + m)) in the usual model.

---

## 1. Notation

* `T` — text of length `n` (indices 0..n-1)
* `P` — pattern of length `m` (indices 0..m-1)
* We attempt alignments `s` meaning `P[0..m-1]` aligned with `T[s..s+m-1]`.

---

## 2. Bad-character rule (last occurrence table)

Precompute:

```
last[c] = index of rightmost occurrence of character c in P (or -1 if none)
```

On mismatch at pattern index `j` (comparing P[j] with T[s+j]), we can shift by:

```
shift_bad = j - last[T[s + j]]
```

(if `last[...] = -1`, shift_bad = j - (-1) = j+1)

This often gives large jumps because we compared from right to left.

---

## 3. Good-suffix rule (strong / full shift)

Intuition: suppose the suffix `P[j+1..m-1]` matched T, but P[j] ≠ T[s+j]. We want to shift the pattern right so that:

* either some earlier occurrence of that matched suffix in P aligns with T (so we don't re-compare the suffix), or
* if no such occurrence, align the longest prefix of P that is a suffix of the matched suffix.

We precompute a `shift_good[j]` (or `good[j]`) giving how far to shift when mismatch at `j`. There are standard linear-time preprocessing algorithms for this (compute `suffix` and `prefix` arrays). The typical result:

* `good[j]` = smallest shift `k>0` such that `P[j+1..m-1]` matches a suffix of `P[0..m-1-k]`, or if none, shift so that a prefix of P aligns with the matched suffix.

(This is explained with standard `suffix` and `prefix` arrays below.)

---

## 4. Combined shift

When mismatch at `j`, compute:

```
shift = max(shift_bad, shift_good[j])
```

and advance `s += shift`. Using the maximum ensures we don't miss any matches.

---

## 5. Complexity (intuitive)

* **Preprocessing:** O(m + |Σ|) (|Σ| is alphabet size; often 256 for ASCII)
* **Matching average:** sublinear (≈ O(n / m) in many practical texts and patterns)
* **Matching worst-case:** with full, correct good-suffix implementation BM can be made to run in **O(n + m)** — i.e., linear time. (Naive incomplete BM implementations can hit O(n·m) in adversarial inputs.)

---

## 6. Example (trace)

Text `T = "HERE IS A SIMPLE EXAMPLE"`
Pattern `P = "EXAMPLE"` (m = 7)

1. Precompute `last[c]` for characters in pattern (E→6, X→5, A→4, M→3, P→2, L→1, E already 6).
2. Start alignment `s = 0`: compare from rightmost (j = 6) downwards; most characters will mismatch near start → use bad-character shifts to jump.
3. Eventually find alignment at the correct s and report match.

(Real traces usually show large jumps early, then a match.)

---

## 7. Preprocessing details (good-suffix arrays)

A standard way to compute `good[j]` uses two auxiliary arrays:

* `suffix[k]` = the starting index of the longest suffix of `P[0..k]` that is also a suffix of `P` (or -1). Often computed from right to left.
* `prefix[k]` = boolean: whether `P[0..k]` is a prefix of `P`.

From these you compute `good[j]` for each `j` (0..m-1). Pseudocode below in the code implementation.

---

## 8. Pseudocode (high level)

```
Preprocess:
  compute last[c] for c in alphabet
  compute good[j] for j = 0..m-1   // good-suffix shifts

Search:
  s = 0
  while s <= n - m:
    j = m - 1
    while j >= 0 and P[j] == T[s + j]:
      j -= 1
    if j < 0:
      report occurrence at s
      s += good[0]             // or shift by 1 or by full rule
    else:
      shift_bad = j - last[T[s + j]]
      shift_good = good[j]
      s += max(1, max(shift_bad, shift_good))
```

Note: `max(1, ...)` ensures forward progress.

---

## 9. Working C implementation (classic, readable)

Below is a C implementation that includes:

* `last` table for ASCII,
* `preprocess_good_suffix` computing the `suffix` and `good` arrays,
* the main Boyer–Moore search.

You can compile in Turbo C / GCC with minor adjustments.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ALPHABET 256

/* Preprocess last occurrence (bad character) */
void preprocess_last(const unsigned char *P, int m, int last[ALPHABET]) {
    int i;
    for (i = 0; i < ALPHABET; ++i) last[i] = -1;
    for (i = 0; i < m; ++i) last[P[i]] = i;
}

/* Preprocess for good-suffix rule (computes good[j]) */
/* Implementation based on standard textbooks */
void preprocess_good_suffix(const unsigned char *P, int m, int *good) {
    int i, j;
    int *suffix = (int*)malloc(sizeof(int) * m);
    for (i = 0; i < m; ++i) suffix[i] = -1;

    /* 1) compute suffix[k] = starting index of the longest suffix of P[0..k] that is also a suffix of P */
    suffix[m-1] = m - 1;
    for (i = m - 2; i >= 0; --i) {
        j = i;
        while (j >= 0 && P[j] == P[m - 1 - (i - j)]) {
            j--;
        }
        suffix[i] = j + 1; /* starting index of matched suffix, or 0..m-1 */
    }

    /* initialize good[] to default shift (m) */
    for (i = 0; i < m; ++i) good[i] = m;

    /* Case 1: if substring P[j+1..m-1] matches prefix of P, set good[j] accordingly */
    for (i = m - 1; i >= 0; --i) {
        /* if suffix[i] == 0, P[i+1..m-1] is prefix of P */
        if (suffix[i] == 0) {
            for (j = 0; j <= m - 1 - i; ++j) {
                if (good[j] == m)
                    good[j] = m - 1 - i;
            }
        }
    }

    /* Case 2: find other occurrences of suffixes inside pattern */
    for (i = 0; i < m - 1; ++i) {
        int slen = m - 1 - i; /* length of suffix P[i+1..m-1] */
        int pos = suffix[i];
        if (pos > 0) {
            /* Align the suffix occurrence: shift so suffix at pos aligns with suffix at m-slen */
            good[m - 1 - pos] = m - 1 - i;
        }
    }

    free(suffix);
}

/* Simpler and safer good-suffix preprocess (textbook approach).
   We'll implement standard approach that computes suff[] and then good[] properly.
*/
void preprocess_good_suffix2(const unsigned char *P, int m, int *good) {
    int i, j;
    int *suff = (int*)malloc(sizeof(int) * m);

    /* compute suff[]: suff[i] is length of longest suffix of P[i..m-1] that is also suffix of P */
    suff[m-1] = m;
    int g = m - 1, f = 0;
    for (i = m - 2; i >= 0; --i) {
        if (i > g && suff[i + m - 1 - f] < i - g) {
            suff[i] = suff[i + m - 1 - f];
        } else {
            if (i < g) g = i;
            f = i;
            while (g >= 0 && P[g] == P[g + m - 1 - f]) g--;
            suff[i] = f - g;
        }
    }

    for (i = 0; i < m; ++i) good[i] = m;
    int jpos = 0;
    for (i = m - 1; i >= 0; --i) {
        if (suff[i] == i + 1) {
            for (j = 0; j < m - 1 - i; ++j)
                if (good[j] == m) good[j] = m - 1 - i;
        }
    }
    for (i = 0; i <= m - 2; ++i) {
        good[m - 1 - suff[i]] = m - 1 - i;
    }
    free(suff);
}

/* Boyer–Moore search: prints all matches */
void boyer_moore_search(const unsigned char *T, int n, const unsigned char *P, int m) {
    int last[ALPHABET];
    preprocess_last(P, m, last);

    int *good = (int*)malloc(sizeof(int) * m);
    preprocess_good_suffix2(P, m, good);

    int s = 0;
    while (s <= n - m) {
        int j = m - 1;
        while (j >= 0 && P[j] == T[s + j]) j--;
        if (j < 0) {
            printf("Pattern occurs at shift %d\n", s);
            s += good[0]; /* shift by good[0] after a match */
        } else {
            int bc_shift = j - last[T[s + j]];
            int gs_shift = good[j];
            int shift = (bc_shift > gs_shift) ? bc_shift : gs_shift;
            if (shift < 1) shift = 1;
            s += shift;
        }
    }
    free(good);
}

/* Demo main */
int main(void) {
    const unsigned char text[] = "HERE IS A SIMPLE EXAMPLE";
    const unsigned char pattern[] = "EXAMPLE";
    int n = strlen((const char*)text);
    int m = strlen((const char*)pattern);
    boyer_moore_search(text, n, pattern, m);
    return 0;
}
```

> Notes about the code:
>
> * `preprocess_good_suffix2` is a robust textbook routine (computes `suff[]`, then `good[]`) — avoids subtle bugs.
> * `last` table uses ALPHABET = 256 (ASCII). For Unicode you’d adapt accordingly.
> * After a full match we used `s += good[0]` (typical). Some implementations do `s += 1` too.

---

## 10. Trace example (small)

Text: `T = "ABABABCA"`
Pattern: `P = "ABABC"`

Pattern m = 5

* `last`: A→2, B→3, C→4 (example values)
* Start s=0: compare from j=4 downwards:

  * j=4: P[4]='C' vs T[4]='B' → mismatch at T[4]='B'
  * `bc_shift = 4 - last['B']` = 4 - 3 = 1
  * `gs_shift = good[4]` (computed) — maybe greater or smaller
  * shift = max(bc_shift, gs_shift) → move s accordingly
* Following shifts skip several alignments compared to naive algorithm.

The key point is mismatch near right end leads to possibly large jumps.

---

## 11. Advantages & use cases

* **Very fast in practice** for natural-language/text search.
* **Sublinear average behavior**: often examines much fewer than n characters.
* Widely used in text editors, grep-like tools, search libraries.

---

## 12. Pitfalls & implementation notes

* Implementing **good-suffix** correctly is the tricky part — use a tested snippet (above) or a library.
* If you only implement **bad-character** rule, you still get a good algorithm (Horspool), but not the full power of BM.
* For small patterns or tiny alphabets, BM’s advantage may diminish.
* When pattern is short and many random characters, BM is very fast.

---

## 13. Summary (short)

* **Boyer–Moore** compares pattern right-to-left and uses **bad-character** + **good-suffix** heuristics to skip text.
* **Preprocessing:** O(m + |Σ|).
* **Matching:** very fast average; with full preprocessing it can be made **linear** O(n + m) worst-case.
* Use BM when you need a very fast text search in large texts and have moderate pattern lengths.

---

