# Unit - 3

## Greedy Technique, Dynamic Programming
- Prim's Algorithm
- Kruskal's Algorithm
- Dijkstra's Algorithm
- Huffmann Trees
- Computing a Binomial Coefficient
- Warshall's and Floyd'a Algorithms
- The Knapsack Problem
- Memory Functions

---
---

# 🌳 **Prim’s Algorithm**

### 🔹 **Introduction**

Prim’s Algorithm is a **greedy algorithm** that finds a **Minimum Spanning Tree (MST)** for a **weighted, connected, undirected graph**.

* **Minimum Spanning Tree (MST)** is a subset of the edges that connects all vertices together, without any cycles, and with the **minimum total edge weight**.
* It works **by growing the MST one vertex at a time**, always choosing the **minimum-weight edge** that connects a vertex in the MST to one outside.

---

### 🔹 **Key Idea (Greedy Approach)**

At each step:

1. Pick the **smallest edge** that connects a **vertex in the tree** to a **vertex outside the tree**.
2. Add that vertex and edge to the tree.
3. Repeat until all vertices are included.

---

### 🔹 **Algorithm (Step-by-Step)**

**Input:**

* Weighted, connected, undirected graph `G(V, E)`
* Number of vertices: `V`
* Weight matrix or adjacency list

**Output:**

* Minimum Spanning Tree (MST) and its total cost

---

### 🧠 **Pseudocode**

```text
PRIM(G, n):
1. Choose any vertex u to start.
2. Mark u as visited.
3. Repeat (n-1) times:
     a. Find the smallest edge (u, v) such that
        - u is visited, and
        - v is unvisited.
     b. Add (u, v) to the MST.
     c. Mark v as visited.
4. Stop when all vertices are visited.
```

---

### 🧩 **Example**

#### Graph:

| Edge | Weight |
| ---- | ------ |
| A-B  | 2      |
| A-C  | 3      |
| B-C  | 1      |
| B-D  | 4      |
| C-D  | 5      |

#### Step-by-Step Execution

1. **Start from A** (arbitrary)

   * Available edges: A-B(2), A-C(3)
   * Choose **A-B(2)** → MST = {A-B}, cost = 2

2. **Visited:** {A, B}

   * Available edges: A-C(3), B-C(1), B-D(4)
   * Choose **B-C(1)** → MST = {A-B, B-C}, cost = 3

3. **Visited:** {A, B, C}

   * Available edges: B-D(4), C-D(5)
   * Choose **B-D(4)** → MST = {A-B, B-C, B-D}, cost = 7

✅ **Total MST cost = 7**

---

### 🕸️ **Graphical Representation**

```
Initial Graph:
    (2)
 A ------- B
 | \       |
(3) \      | (4)
 |   \     |
 |    \    |
 C ---- D
    (5)

Prim’s Progress:
Step 1: A-B(2)
Step 2: B-C(1)
Step 3: B-D(4)

Final MST:
A--B--C
   |
   D
```

---

### ⏱️ **Time Complexity**

| Implementation                  | Time Complexity |
| ------------------------------- | --------------- |
| Using Adjacency Matrix          | O(V²)           |
| Using Min Heap + Adjacency List | O(E log V)      |

---

### 💾 **Space Complexity**

* **O(V + E)** (for storing the graph)

---

### 🔍 **Characteristics**

| Property | Description                     |
| -------- | ------------------------------- |
| Type     | Greedy Algorithm                |
| Graph    | Undirected, Connected, Weighted |
| Result   | Minimum Spanning Tree           |
| Optimal  | Yes                             |
| Cycle    | No cycles allowed               |

---

### ⚖️ **Comparison: Prim’s vs Kruskal’s**

| Feature         | Prim’s Algorithm          | Kruskal’s Algorithm                   |
| --------------- | ------------------------- | ------------------------------------- |
| Approach        | Grows MST from one vertex | Adds edges in increasing weight order |
| Data Structure  | Adjacency matrix / list   | Edge list + Union-Find                |
| Suitable For    | Dense graphs              | Sparse graphs                         |
| Time Complexity | O(E log V) (with Heap)    | O(E log E)                            |

---

### 🧮 **C Implementation Example**

```c
#include <stdio.h>
#define INF 9999
#define V 5

void prim(int G[V][V]) {
    int selected[V] = {0};
    int no_edge = 0;
    selected[0] = 1;

    printf("Edge : Weight\n");
    while (no_edge < V - 1) {
        int min = INF, x = 0, y = 0;
        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    if (!selected[j] && G[i][j]) {
                        if (min > G[i][j]) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }
        printf("%d - %d : %d\n", x, y, G[x][y]);
        selected[y] = 1;
        no_edge++;
    }
}

int main() {
    int G[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };
    prim(G);
    return 0;
}
```

---

### ✅ **Final MST Output**

```
Edge : Weight
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
```

🔹 **Total cost = 16**

---

### 🧾 **Summary**

| Concept         | Explanation                                                 |
| --------------- | ----------------------------------------------------------- |
| Algorithm Type  | Greedy                                                      |
| Input           | Weighted, connected, undirected graph                       |
| Output          | Minimum Spanning Tree                                       |
| Key Step        | Select minimum-weight edge connecting visited and unvisited |
| Time Complexity | O(E log V)                                                  |
| Best Use Case   | Dense graphs                                                |

---

# 🌳 **Kruskal’s Algorithm**

### 🔹 **Introduction**

Kruskal’s Algorithm finds a **Minimum Spanning Tree (MST)** by:

* Sorting all edges in **increasing order of their weights**, and
* Adding edges to the MST one by one, **avoiding cycles** using the **Disjoint Set (Union-Find)** technique.

✅ It is **edge-based**, while Prim’s Algorithm is **vertex-based**.

---

### 🔹 **Basic Concepts**

* **Minimum Spanning Tree (MST):**
  A subset of edges that connects all vertices with minimum possible total edge weight and **no cycles**.

* **Greedy Approach:**
  At every step, select the **smallest weight edge** that doesn’t form a cycle.

---

### 🔹 **Algorithm Steps**

1. **Sort** all edges in **non-decreasing order** of their weights.
2. **Initialize** an empty set for the MST.
3. **For each edge (u, v)** in sorted order:

   * If adding (u, v) **does not form a cycle**, add it to the MST.
   * Otherwise, **discard** it.
4. **Stop** when MST has (V – 1) edges.

---

### 🧠 **Pseudocode**

```text
KRUSKAL(G):
1.  A ← ∅    // MST set
2.  for each vertex v ∈ G.V:
3.      MAKE-SET(v)
4.  sort edges of G in non-decreasing order by weight
5.  for each edge (u, v) in sorted order:
6.      if FIND-SET(u) ≠ FIND-SET(v):
7.          A ← A ∪ {(u, v)}
8.          UNION(u, v)
9.  return A
```

---

### 🧩 **Example**

#### Graph:

| Edge | Weight |
| ---- | ------ |
| A-B  | 4      |
| A-H  | 8      |
| B-H  | 11     |
| B-C  | 8      |
| C-D  | 7      |
| C-F  | 4      |
| D-E  | 9      |
| D-F  | 14     |
| E-F  | 10     |
| F-G  | 2      |
| G-H  | 1      |

---

#### Step 1️⃣ — Sort all edges by weight

| Edge | Weight |
| ---- | ------ |
| G-H  | 1      |
| F-G  | 2      |
| C-F  | 4      |
| A-B  | 4      |
| C-D  | 7      |
| A-H  | 8      |
| B-C  | 8      |
| D-E  | 9      |
| E-F  | 10     |
| B-H  | 11     |
| D-F  | 14     |

---

#### Step 2️⃣ — Start with an empty MST

Now add edges one by one (avoiding cycles):

| Step | Edge Added | Cycle?        | MST Edges                           | Total Weight |
| ---- | ---------- | ------------- | ----------------------------------- | ------------ |
| 1    | G-H(1)     | No            | {G-H}                               | 1            |
| 2    | F-G(2)     | No            | {G-H, F-G}                          | 3            |
| 3    | C-F(4)     | No            | {G-H, F-G, C-F}                     | 7            |
| 4    | A-B(4)     | No            | {G-H, F-G, C-F, A-B}                | 11           |
| 5    | C-D(7)     | No            | {G-H, F-G, C-F, A-B, C-D}           | 18           |
| 6    | A-H(8)     | No            | {G-H, F-G, C-F, A-B, C-D, A-H}      | 26           |
| 7    | B-C(8)     | ❌ Yes (cycle) | Skipped                             | -            |
| 8    | D-E(9)     | No            | {G-H, F-G, C-F, A-B, C-D, A-H, D-E} | 35           |

✅ **MST has 7 edges (for 8 vertices).**

---

### 🕸️ **Graphical View (Simplified)**

```
Original Graph:
A--4--B--8--C--7--D--9--E
|     |     |     |
8     11    4     14
|     |     |     |
H--1--G--2--F--10--E

Final MST:
A--4--B
|     |
8     8
|     |
H--1--G--2--F--4--C--7--D--9--E
```

---

### ⏱️ **Time Complexity**

| Step                      | Operation      | Complexity |
| ------------------------- | -------------- | ---------- |
| Sorting edges             | O(E log E)     |            |
| Union-Find (Disjoint Set) | O(E log V)     |            |
| **Total**                 | **O(E log V)** |            |

> ✅ Faster than Prim’s for **sparse graphs**.

---

### 💾 **Space Complexity**

* **O(V + E)** (for storing edges and disjoint sets)

---

### ⚙️ **Union-Find (Cycle Detection)**

To avoid cycles efficiently:

* Use **Disjoint Set Data Structure** with:

  * **Find()** → Find the root of the set
  * **Union()** → Merge two sets
* With **path compression** and **union by rank**, the complexity is nearly **O(1)** per operation.

---

### 🧮 **C Implementation Example**

```c
#include <stdio.h>
#include <stdlib.h>

#define V 5

typedef struct {
    int u, v, w;
} Edge;

int parent[V];

int find(int i) {
    while (i != parent[i])
        i = parent[i];
    return i;
}

void unionSets(int u, int v) {
    int rootU = find(u);
    int rootV = find(v);
    parent[rootU] = rootV;
}

void kruskal(Edge edges[], int E) {
    int i, j, cost = 0;

    // Initialize parent
    for (i = 0; i < V; i++)
        parent[i] = i;

    // Sort edges by weight
    for (i = 0; i < E - 1; i++)
        for (j = 0; j < E - i - 1; j++)
            if (edges[j].w > edges[j + 1].w) {
                Edge temp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = temp;
            }

    printf("Edge : Weight\n");
    for (i = 0; i < E; i++) {
        int u = find(edges[i].u);
        int v = find(edges[i].v);
        if (u != v) {
            printf("%d - %d : %d\n", edges[i].u, edges[i].v, edges[i].w);
            cost += edges[i].w;
            unionSets(u, v);
        }
    }
    printf("Total cost = %d\n", cost);
}

int main() {
    Edge edges[] = {
        {0, 1, 4}, {0, 2, 2}, {1, 2, 1}, {1, 3, 5}, {2, 3, 8}
    };
    int E = 5;
    kruskal(edges, E);
    return 0;
}
```

---

### 🧾 **Output**

```
Edge : Weight
1 - 2 : 1
0 - 2 : 2
0 - 1 : 4
1 - 3 : 5
Total cost = 12
```

---

### ⚖️ **Comparison: Prim’s vs Kruskal’s**

| Feature         | **Prim’s Algorithm**       | **Kruskal’s Algorithm** |
| --------------- | -------------------------- | ----------------------- |
| Approach        | Vertex-based               | Edge-based              |
| Graph Type      | Dense graphs               | Sparse graphs           |
| Sorting         | Not required               | Required                |
| Cycle Detection | Not required               | Required (Union-Find)   |
| Time Complexity | O(E log V)                 | O(E log V)              |
| Implementation  | Easier with adjacency list | Easier with edge list   |

---

### ✅ **Summary**

| Concept         | Explanation                               |
| --------------- | ----------------------------------------- |
| Algorithm Type  | Greedy                                    |
| Input           | Weighted, connected, undirected graph     |
| Output          | Minimum Spanning Tree (MST)               |
| Key Step        | Add smallest edge without forming a cycle |
| Data Structure  | Union-Find (Disjoint Set)                 |
| Time Complexity | O(E log V)                                |
| Best Use Case   | Sparse graphs                             |

---

# 🧭 **Dijkstra’s Algorithm**

### 🔹 **Introduction**

* **Type:** Greedy Algorithm
* **Purpose:** To find the **shortest path** from a **source node** to **all other nodes** in a **weighted graph**.
* **Applicable only for:** Graphs with **non-negative edge weights**.

---

### 🔹 **Real-Life Analogy**

Think of Dijkstra’s algorithm like **Google Maps** calculating the **shortest route** from your location to all other nearby places — minimizing total travel distance or time.

---

### 🔹 **Key Idea**

At each step:

1. Choose the **vertex with the smallest known distance**.
2. Update distances to its **unvisited neighbors**.
3. Mark the vertex as **visited** (its shortest path is finalized).
4. Repeat until all vertices are processed.

---

### 🔹 **Algorithm Steps**

**Input:** Weighted graph `G(V, E)`, and source vertex `S`
**Output:** Shortest distance from `S` to every vertex

---

### 🧠 **Pseudocode**

```text
DIJKSTRA(G, S):
1. for each vertex v in G:
2.     dist[v] = ∞
3.     visited[v] = false
4. dist[S] = 0
5. for i = 1 to |V| - 1:
6.     u = vertex with minimum dist[u] not visited
7.     visited[u] = true
8.     for each neighbor v of u:
9.         if not visited[v] and dist[u] + weight(u,v) < dist[v]:
10.             dist[v] = dist[u] + weight(u,v)
11. return dist[]
```

---

### 🧩 **Example**

#### Graph:

```
Vertices: A, B, C, D, E
Edges:
A → B = 4
A → C = 2
B → C = 3
B → D = 2
B → E = 3
C → D = 4
C → E = 5
D → E = 1
```

#### Step-by-Step Execution (Source = A)

| Step | Visited | Distance from A                      | Explanation            |
| ---- | ------- | ------------------------------------ | ---------------------- |
| Init | -       | A=0, B=∞, C=∞, D=∞, E=∞              | Start at A             |
| 1    | A       | B=4, C=2                             | Update from A          |
| 2    | C       | D=6, E=7                             | C gives better paths   |
| 3    | B       | D=6 (via B=4+2=6), E=7 (via B=4+3=7) | No better path         |
| 4    | D       | E=7 (via D=6+1=7)                    | No change              |
| 5    | E       | Done                                 | All vertices processed |

✅ **Final Shortest Distances:**

```
A → A = 0
A → B = 4
A → C = 2
A → D = 6
A → E = 7
```

---

### 🧮 **Working Visualization**

```
        (4)
    A ------- B
    | \       |
   (2) \      | (3)
    |   \     |
    |    \    |
    C---- D -- E
   (4)\   |(1)
     \ \  |
     (5)\ |
         \|
          E

Shortest Path Tree:
A → C → D → E
```

---

### ⚙️ **Table Representation**

| Vertex | Current Distance | Finalized | Previous Vertex |
| ------ | ---------------- | --------- | --------------- |
| A      | 0                | ✅         | -               |
| B      | 4                | ✅         | A               |
| C      | 2                | ✅         | A               |
| D      | 6                | ✅         | C               |
| E      | 7                | ✅         | D               |

---

### ⏱️ **Time Complexity**

| Implementation                  | Time Complexity |
| ------------------------------- | --------------- |
| Using Adjacency Matrix          | O(V²)           |
| Using Min Heap + Adjacency List | O(E log V)      |

---

### 💾 **Space Complexity**

* **O(V)** for distance array
* **O(V)** for visited array
* **O(V + E)** for adjacency list

---

### 🧮 **C Implementation Example**

```c
#include <stdio.h>
#include <limits.h>

#define V 5
#define INF INT_MAX

int minDistance(int dist[], int visited[]) {
    int min = INF, min_index;
    for (int v = 0; v < V; v++)
        if (!visited[v] && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

void dijkstra(int graph[V][V], int src) {
    int dist[V];
    int visited[V];

    for (int i = 0; i < V; i++) {
        dist[i] = INF;
        visited[i] = 0;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, visited);
        visited[u] = 1;

        for (int v = 0; v < V; v++)
            if (!visited[v] && graph[u][v] && dist[u] != INF &&
                dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

    printf("Vertex \t Distance from Source\n");
    for (int i = 0; i < V; i++)
        printf("%d \t\t %d\n", i, dist[i]);
}

int main() {
    int graph[V][V] = {
        {0, 4, 2, 0, 0},
        {4, 0, 3, 2, 3},
        {2, 3, 0, 4, 5},
        {0, 2, 4, 0, 1},
        {0, 3, 5, 1, 0}
    };
    dijkstra(graph, 0);
    return 0;
}
```

---

### 🧾 **Output**

```
Vertex   Distance from Source
0        0
1        4
2        2
3        6
4        7
```

✅ Matches our earlier manual calculation.

---

### ⚖️ **Comparison with Bellman-Ford**

| Feature                  | **Dijkstra’s Algorithm**           | **Bellman-Ford Algorithm**   |
| ------------------------ | ---------------------------------- | ---------------------------- |
| Type                     | Greedy                             | Dynamic Programming          |
| Handles Negative Weights | ❌ No                               | ✅ Yes                        |
| Complexity               | O(E log V)                         | O(VE)                        |
| Implementation           | Priority Queue                     | Simple Loops                 |
| Use Case                 | Dense graphs, non-negative weights | Graphs with negative weights |

---

### ✅ **Summary**

| Concept          | Explanation                                |
| ---------------- | ------------------------------------------ |
| Algorithm Type   | Greedy                                     |
| Goal             | Shortest path from single source           |
| Graph Type       | Directed/Undirected (Non-negative weights) |
| Data Structure   | Min Heap / Priority Queue                  |
| Time Complexity  | O(E log V)                                 |
| Space Complexity | O(V + E)                                   |
| Limitation       | Cannot handle negative weights             |

---

### 📘 **Key Takeaway**

> Dijkstra’s Algorithm **greedily** picks the nearest unvisited vertex and expands outward, ensuring the shortest known path to each node is finalized only once.

---

# 🧩 **Huffman Trees (Huffman Coding Algorithm)**

### 🧠 **Introduction**

* **Huffman Tree** is a **binary tree** used for **data compression**.
* It is used in **Huffman Coding**, a **lossless compression algorithm** developed by **David A. Huffman (1952)**.
* The main goal is to **assign variable-length binary codes** to input characters, **shorter codes to frequent characters** and **longer codes to infrequent ones**.

---

### ⚙️ **Basic Idea**

Given a set of characters and their frequencies,
we build a **binary tree** where:

* Each **leaf node** represents a character.
* The **path** from the root to a leaf gives the **binary code** for that character.

The **total cost (Weighted Path Length)** is minimized:
[
\text{Cost} = \sum (frequency \times code_length)
]

---

### 🧩 **Steps of Huffman’s Algorithm**

| Step | Action                                                                                                                                                                                                                                                                                    |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1️⃣  | Create a **leaf node** for each character and its frequency.                                                                                                                                                                                                                              |
| 2️⃣  | Insert all nodes into a **min-priority queue** (sorted by frequency).                                                                                                                                                                                                                     |
| 3️⃣  | **Repeat until one node remains:** <br> a. Remove two nodes with the **lowest frequencies**.<br> b. Create a **new internal node** with frequency = sum of both nodes.<br> c. Assign left = smaller frequency, right = larger frequency.<br> d. Insert this new node back into the queue. |
| 4️⃣  | The **remaining node** is the **root** of the Huffman Tree.                                                                                                                                                                                                                               |
| 5️⃣  | Assign **binary codes**: left edge → `0`, right edge → `1`.                                                                                                                                                                                                                               |
| 6️⃣  | Traverse from root to each leaf to get character codes.                                                                                                                                                                                                                                   |

---

### 📊 **Example**

#### Given Characters and Frequencies

| Character | Frequency |
| --------- | --------- |
| A         | 5         |
| B         | 9         |
| C         | 12        |
| D         | 13        |
| E         | 16        |
| F         | 45        |

---

### 🪜 **Step-by-Step Construction**

1. **List and Sort:**

   ```
   A(5), B(9), C(12), D(13), E(16), F(45)
   ```

2. **Combine A(5) and B(9):**

   * New node = (A+B) = 14
     → Remaining: C(12), D(13), E(16), F(45), (A+B)(14)

3. **Combine C(12) and D(13):**

   * New node = (C+D) = 25
     → Remaining: E(16), F(45), (A+B)(14), (C+D)(25)

4. **Combine (A+B)(14) and E(16):**

   * New node = 30
     → Remaining: F(45), (C+D)(25), (A+B+E)(30)

5. **Combine (C+D)(25) and (A+B+E)(30):**

   * New node = 55
     → Remaining: F(45), (ABCDE)(55)

6. **Combine F(45) and (ABCDE)(55):**

   * New node = 100 (Root)

---

### 🌳 **Huffman Tree Diagram**

```
                 (100)
               /      \
           (45)F       (55)
                      /    \
                   (25)     (30)
                  /   \     /   \
               (12)C (13)D (14)  (16)E
                         / \
                       (5)A (9)B
```

---

### 💻 **Huffman Codes Generated**

| Character | Code |
| --------- | ---- |
| F         | 0    |
| C         | 100  |
| D         | 101  |
| A         | 1100 |
| B         | 1101 |
| E         | 111  |

---

### 📉 **Compression Example**

**Original Data:**
`AAAAABBBBCCCCDDDEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF`

If using **fixed 8-bit encoding** for 6 characters → 8 bits × 50 = 400 bits.
Using **Huffman Codes**, total bits =
`5×4 + 9×4 + 12×3 + 13×3 + 16×3 + 45×1 = 224 bits.`

✅ **Compression ratio = 224 / 400 = 56%**

---

### 🧮 **Mathematical Representation**

If characters are $c_i$ with frequencies $f_i$ and code lengths $l_i$:
[
\text{Average Code Length } = \frac{\sum f_i l_i}{\sum f_i}
]
The **Huffman Tree minimizes this value**.

---

### ⏱ **Time Complexity**

| Operation            | Complexity                            |
| -------------------- | ------------------------------------- |
| Building Tree        | $O(n \log n)$ (due to priority queue) |
| Encoding each symbol | $O(1)$ (after tree is built)          |
| Decoding each symbol | $O(1)$ (tree traversal)               |

---

### 📦 **Applications**

✅ **File Compression** → ZIP, GZIP
✅ **Multimedia** → JPEG, MP3
✅ **Data Transmission** → Minimizing bandwidth
✅ **Embedded Systems** → Efficient storage and encoding

---

### ⚔️ **Comparison Table**

| Algorithm           | Type              | Compression | Loss |
| ------------------- | ----------------- | ----------- | ---- |
| Huffman Coding      | Variable-length   | High        | None |
| Run-Length Encoding | Repetition-based  | Medium      | None |
| Arithmetic Coding   | Probability-based | Very High   | None |

---

### 💡 **Key Takeaways**

* Huffman algorithm **assigns shorter codes to frequent symbols**.
* It ensures **prefix-free property** — no code is a prefix of another.
* Provides **optimal prefix code** (no better code exists for same frequency set).
* Used in **lossless compression standards**.

---

# 🧮 **Computing a Binomial Coefficient**

---

### 📘 **Introduction**

The **Binomial Coefficient**, denoted as
[
C(n, k) \quad \text{or} \quad \binom{n}{k}
]
represents the **number of ways to choose** `k` elements out of `n` elements, **without regard to order**.

It is widely used in:

* **Combinatorics**
* **Probability**
* **Pascal’s Triangle**
* **Dynamic Programming**
* **Divide and Conquer algorithms**

---

### 🔢 **Mathematical Definition**

[
C(n, k) = \frac{n!}{k! \times (n - k)!}
]

where `n!` means the factorial of `n`
→ `n! = n × (n−1) × (n−2) × ... × 1`

---

### 🧠 **Example**

[
C(5, 2) = \frac{5!}{2!(5-2)!} = \frac{120}{2 \times 6} = 10
]

There are **10 ways** to select 2 items from 5.

---

### ⚙️ **Recursive Property**

The binomial coefficients satisfy the **Pascal’s Identity**:

[
C(n, k) = C(n-1, k-1) + C(n-1, k)
]

with **base cases:**

[
C(n, 0) = C(n, n) = 1
]

---

### 🌳 **Recursive Explanation (Pascal’s Triangle View)**

Pascal’s Triangle is built using this identity:

```
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5  10  10   5   1
```

Each number is the sum of the **two numbers above it**.

Thus:

```
C(5, 2) = C(4, 1) + C(4, 2)
```

---

### 🧩 **Recursive Algorithm**

#### **Pseudocode**

```
Algorithm BinomialCoefficient(n, k)
1. if k = 0 or k = n then
2.     return 1
3. else
4.     return BinomialCoefficient(n-1, k-1) + BinomialCoefficient(n-1, k)
```

#### **Example for C(4, 2)**

```
C(4,2)
= C(3,1) + C(3,2)
= (C(2,0)+C(2,1)) + (C(2,1)+C(2,2))
= (1+2) + (2+1)
= 6
```

---

### 🧮 **Recursive Tree Visualization**

```
              C(4,2)
             /      \
         C(3,1)     C(3,2)
        /    \       /    \
    C(2,0) C(2,1) C(2,1) C(2,2)
     |       |       |      |
     1       2       2      1
```

Sum of leaf nodes = **6**

---

### 🚀 **Dynamic Programming Approach**

Recursive computation is **exponential** due to repeated subproblems.

We can use **DP (bottom-up table)** to compute efficiently.

#### **Formula**

[
C[n][k] = C[n-1][k-1] + C[n-1][k]
]

#### **Pseudocode (DP Method)**

```
Algorithm BinomialDP(n, k)
1. Create array C[0…n][0…k]
2. for i = 0 to n do
3.     for j = 0 to min(i, k) do
4.         if j == 0 or j == i then
5.             C[i][j] = 1
6.         else
7.             C[i][j] = C[i-1][j-1] + C[i-1][j]
8. return C[n][k]
```

---

### 💻 **C Program (Dynamic Programming)**

```c
#include <stdio.h>

int binomialCoeff(int n, int k) {
    int C[n + 1][k + 1];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= (i < k ? i : k); j++) {
            if (j == 0 || j == i)
                C[i][j] = 1;
            else
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
    return C[n][k];
}

int main() {
    int n = 5, k = 2;
    printf("C(%d, %d) = %d\n", n, k, binomialCoeff(n, k));
    return 0;
}
```

**Output:**

```
C(5, 2) = 10
```

---

### 📊 **Table (Pascal’s Triangle till n=5)**

| n | k | C(n,k) |
| - | - | ------ |
| 0 | 0 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |
| 2 | 0 | 1      |
| 2 | 1 | 2      |
| 2 | 2 | 1      |
| 3 | 0 | 1      |
| 3 | 1 | 3      |
| 3 | 2 | 3      |
| 3 | 3 | 1      |
| 4 | 0 | 1      |
| 4 | 1 | 4      |
| 4 | 2 | 6      |
| 4 | 3 | 4      |
| 4 | 4 | 1      |
| 5 | 2 | 10     |

---

### ⏱ **Time and Space Complexity**

| Method       | Time Complexity | Space Complexity     |
| ------------ | --------------- | -------------------- |
| Recursive    | $O(2^n)$        | $O(n)$ (stack depth) |
| DP (Table)   | $O(nk)$         | $O(nk)$              |
| Optimized DP | $O(nk)$         | $O(k)$               |

*(Optimized version uses 1D array to save space.)*

---

### 🧮 **Optimized Space Version**

[
C(k) = C(k) + C(k-1)
]

(Iterate backwards for `k` to reuse array space.)

---

### 🎯 **Applications**

✅ In **Combinatorics** → counting combinations
✅ In **Pascal’s Triangle** generation
✅ In **Binomial Theorem**:
[
(a + b)^n = \sum_{k=0}^{n} C(n, k) a^{n-k} b^k
]
✅ In **Dynamic Programming problems** (e.g., subset problems, lattice paths)
✅ In **Probability and Statistics** (e.g., Binomial Distribution)

---

### ⚔️ **Comparison Table**

| Approach     | Idea              | Pros            | Cons             |
| ------------ | ----------------- | --------------- | ---------------- |
| Recursive    | Direct definition | Simple, clear   | Exponential time |
| DP           | Bottom-up reuse   | Efficient       | Needs table      |
| Optimized DP | Uses 1D array     | Space-efficient | Slightly complex |

---

### 💡 **Key Takeaways**

* Binomial Coefficient counts combinations: “ways to choose k items from n.”
* Recursive definition comes from Pascal’s Identity.
* DP gives polynomial-time solution.
* Foundational in combinatorics, probability, and algorithm analysis.

---

# 🧭 **Warshall’s and Floyd’s Algorithms**

---

## 🔹 Introduction

Both algorithms work on **graphs represented as adjacency matrices**, but they solve **different problems**:

| Algorithm                              | Purpose                                                                 | Output                             |
| -------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------- |
| **Warshall’s Algorithm**               | Finds *reachability* between all pairs of vertices (Transitive Closure) | Boolean matrix (reachable or not)  |
| **Floyd’s Algorithm** (Floyd–Warshall) | Finds *shortest path distances* between all pairs of vertices           | Weighted matrix (minimum distance) |

---

## 🧩 **1. Warshall’s Algorithm (Transitive Closure)**

### 🧠 **Goal**

To find **if there exists a path** between every pair of vertices `(i, j)` in a **directed graph**.

---

### 🧮 **Input**

An **adjacency matrix A** of size `n × n`:

[
A[i][j] =
\begin{cases}
1, & \text{if there is an edge from } i \text{ to } j \
0, & \text{otherwise}
\end{cases}
]

---

### ⚙️ **Concept**

We gradually allow intermediate vertices one by one to find **indirect paths**.

Let:

[
R^{(k)}[i][j] = 1 \text{ if there exists a path from i to j using only vertices } {1, 2, …, k}.
]

---

### 🧩 **Recursive Formula**

[
R^{(k)}[i][j] = R^{(k-1)}[i][j] ; \text{OR} ; (R^{(k-1)}[i][k] ; \text{AND} ; R^{(k-1)}[k][j])
]

---

### 🧰 **Algorithm (Pseudocode)**

```
Algorithm Warshall(A, n)
Input: Adjacency matrix A[1..n][1..n]
Output: Transitive closure matrix A

for k = 1 to n do
    for i = 1 to n do
        for j = 1 to n do
            A[i][j] = A[i][j] OR (A[i][k] AND A[k][j])
return A
```

---

### 📊 **Example**

Given directed graph:

```
A → B → C
↑         ↓
└─────────┘
```

Adjacency matrix:

|   | A | B | C |
| - | - | - | - |
| A | 0 | 1 | 0 |
| B | 0 | 0 | 1 |
| C | 1 | 0 | 0 |

Now, we apply Warshall’s algorithm step by step (for k = 1, 2, 3).

After completion, we get:

|   | A | B | C |
| - | - | - | - |
| A | 1 | 1 | 1 |
| B | 1 | 1 | 1 |
| C | 1 | 1 | 1 |

✅ **Every node is reachable from every other node.**

---

### 🕒 **Complexity**

| Measure   | Complexity |
| --------- | ---------- |
| **Time**  | $O(n^3)$   |
| **Space** | $O(n^2)$   |

---

### 🧮 **Output Interpretation**

`A[i][j] = 1` → There exists a path from vertex `i` to `j`.

---

## 🔹 **2. Floyd’s Algorithm (All-Pairs Shortest Path)**

Also known as the **Floyd–Warshall Algorithm**, it extends Warshall’s idea —
but instead of **reachability**, it computes **minimum path weights** between all pairs of vertices.

---

### 🧠 **Goal**

To find the **shortest distance** between every pair of vertices in a **weighted directed graph** (can have negative weights but **no negative cycles**).

---

### 🧮 **Input**

A weighted adjacency matrix `D[1..n][1..n]`:

[
D[i][j] =
\begin{cases}
w(i, j), & \text{if edge } (i,j) \text{ exists} \
0, & \text{if } i = j \
∞, & \text{if no edge exists}
\end{cases}
]

---

### ⚙️ **Concept**

Let:
[
D^{(k)}[i][j] = \text{length of shortest path from } i \text{ to } j \text{ using vertices } {1, 2, …, k}.
]

Recursive relation:
[
D^{(k)}[i][j] = \min\big( D^{(k-1)}[i][j], ; D^{(k-1)}[i][k] + D^{(k-1)}[k][j] \big)
]

---

### 🧰 **Algorithm (Pseudocode)**

```
Algorithm Floyd(D, n)
Input: Distance matrix D[1..n][1..n]
Output: Shortest path distances between all pairs

for k = 1 to n do
    for i = 1 to n do
        for j = 1 to n do
            if D[i][k] + D[k][j] < D[i][j] then
                D[i][j] = D[i][k] + D[k][j]
return D
```

---

### 📊 **Example**

Given weighted graph:

| From | To | Weight |
| ---- | -- | ------ |
| A    | B  | 3      |
| A    | C  | ∞      |
| B    | C  | 1      |
| C    | A  | 2      |

Matrix form:

|   | A | B | C |
| - | - | - | - |
| A | 0 | 3 | ∞ |
| B | ∞ | 0 | 1 |
| C | 2 | ∞ | 0 |

After applying Floyd’s algorithm step by step, we get:

|   | A | B | C |
| - | - | - | - |
| A | 0 | 3 | 4 |
| B | 3 | 0 | 1 |
| C | 2 | 5 | 0 |

✅ Shortest paths between every vertex pair are computed.

---

### 🕒 **Complexity**

| Measure   | Complexity |
| --------- | ---------- |
| **Time**  | $O(n^3)$   |
| **Space** | $O(n^2)$   |

---

### 💻 **C Program (Floyd’s Algorithm)**

```c
#include <stdio.h>
#define INF 99999
#define N 4

void floydWarshall(int graph[N][N]) {
    int dist[N][N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            dist[i][j] = graph[i][j];

    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    printf("Shortest distance matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            if (dist[i][j] == INF) printf("INF ");
            else printf("%3d ", dist[i][j]);
        printf("\n");
    }
}

int main() {
    int graph[N][N] = {
        {0, 3, INF, 5},
        {2, 0, INF, 4},
        {INF, 1, 0, INF},
        {INF, INF, 2, 0}
    };

    floydWarshall(graph);
    return 0;
}
```

---

### 🧩 **Output (for above program)**

```
Shortest distance matrix:
0   3   7   5
2   0   6   4
3   1   0   5
5   3   2   0
```

---

### 🔍 **Comparison: Warshall vs Floyd**

| Feature                  | **Warshall’s Algorithm**          | **Floyd’s Algorithm**       |
| ------------------------ | --------------------------------- | --------------------------- |
| Purpose                  | Transitive closure (reachability) | All-pairs shortest paths    |
| Works on                 | Unweighted directed graph         | Weighted directed graph     |
| Operation                | Logical OR / AND                  | Arithmetic MIN / +          |
| Output                   | Boolean matrix                    | Distance matrix             |
| Handles negative weights | Not applicable                    | Yes (if no negative cycles) |
| Complexity               | $O(n^3)$                          | $O(n^3)$                    |
| Type                     | Boolean Dynamic Programming       | Numeric Dynamic Programming |

---

### 🧠 **Key Takeaways**

✅ Both algorithms use **Dynamic Programming**.
✅ **Warshall** → reachability (paths exist or not).
✅ **Floyd–Warshall** → minimum distances between all pairs.
✅ Both use the same three nested loop structure with different operations (logical vs arithmetic).
✅ Complexity is the same: $O(n^3)$.

---

# 🧩 The Knapsack Problem

#### 🔹 Definition

The **Knapsack Problem** is a **combinatorial optimization** problem where we must choose a subset of items to include in a **knapsack** so that the **total value is maximized**, but the **total weight does not exceed the capacity** of the knapsack.

It models real-world resource allocation problems where you must make trade-offs between **value (profit)** and **weight (cost or resource usage)**.

---

### 🧠 Types of Knapsack Problems

1. **0/1 Knapsack Problem** – Each item can either be **included (1)** or **excluded (0)**; cannot be broken into parts.
2. **Fractional Knapsack Problem** – Items can be **divided** into smaller fractions.
3. **Multiple Knapsack Problem** – There are **multiple knapsacks** with different capacities.

---

### ⚙️ 0/1 Knapsack Problem (Dynamic Programming Approach)

#### 🧾 Problem Statement

Given:

* `n` items, each with a **value** `v[i]` and a **weight** `w[i]`
* Knapsack capacity = `W`

Find:

* The **maximum value** that can be obtained by selecting items such that total weight ≤ `W`.

---

### 🧩 Recursive Formula

Let
`K[i][w]` = Maximum value that can be obtained using first `i` items and capacity `w`.

Then:
[
K[i][w] =
\begin{cases}
0 & \text{if } i=0 \text{ or } w=0 \
K[i-1][w] & \text{if } w_i > w \
\max(v_i + K[i-1][w-w_i],\ K[i-1][w]) & \text{if } w_i \le w
\end{cases}
]

---

### 🧮 Algorithm (Dynamic Programming)

```c
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapSack(int W, int wt[], int val[], int n) {
    int K[n + 1][W + 1];
    
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf("Maximum value = %d", knapSack(W, wt, val, n));
    return 0;
}
```

---

### 🧩 Output

```
Maximum value = 220
```

---

### ⏱️ Time and Space Complexity

| Complexity | Description                         |
| ---------- | ----------------------------------- |
| Time       | O(n × W)                            |
| Space      | O(n × W) (can be optimized to O(W)) |

---

### ⚙️ Fractional Knapsack (Greedy Approach)

* Sort items by **value/weight ratio**.
* Pick the **highest ratio item** until the knapsack is full.
* If an item can’t fit fully, take **fractional part**.

---

### 🧮 Example

| Item | Value | Weight | Value/Weight |
| ---- | ----- | ------ | ------------ |
| 1    | 60    | 10     | 6            |
| 2    | 100   | 20     | 5            |
| 3    | 120   | 30     | 4            |

Capacity = 50
→ Take item 1 (10), item 2 (20), and ⅔ of item 3 (20 weight).
→ Total value = 60 + 100 + 80 = **240**

---

### 🧩 Applications

* Resource allocation
* Budget management
* Load optimization
* Portfolio selection
* Cloud resource scheduling

---

# 🧠 Memory Functions (in Algorithms and Data Structures)

#### 🔹 Definition

**Memory functions** (also called **memoization functions**) are a **programming technique** used to improve the efficiency of recursive algorithms by **storing previously computed results** and **reusing them** instead of recalculating.

They are a **key concept in Dynamic Programming (DP)** — where overlapping subproblems occur frequently.

---

### 🧩 Concept Explanation

Many recursive problems re-compute the same subproblems multiple times.
For example, in the **Fibonacci sequence**, `fib(5)` calls `fib(4)` and `fib(3)`,
but `fib(4)` again calls `fib(3)` — causing redundant work.

#### ⚙️ Without Memoization:

```
fib(5)
├─ fib(4)
│  ├─ fib(3)
│  │  ├─ fib(2)
│  │  └─ fib(1)
│  └─ fib(2)
└─ fib(3)
```

➡️ Many subproblems (`fib(3)`, `fib(2)`) are repeated.

#### ⚙️ With Memoization:

* Store results of each computed function call in a **table (array or dictionary)**.
* Next time, if the same subproblem is required, **fetch the stored result** instead of recomputing.

---

### 🧮 Example: Fibonacci Series Using Memory Function

```c
#include <stdio.h>

#define MAX 100
int fibTable[MAX];

int fib(int n) {
    if (fibTable[n] != -1)
        return fibTable[n];
    if (n <= 1)
        fibTable[n] = n;
    else
        fibTable[n] = fib(n - 1) + fib(n - 2);
    return fibTable[n];
}

int main() {
    int n = 10;
    for (int i = 0; i < MAX; i++)
        fibTable[i] = -1;  // initialize table with -1 (uncomputed)
    printf("Fibonacci(%d) = %d\n", n, fib(n));
    return 0;
}
```

---

### 🧩 Output

```
Fibonacci(10) = 55
```

---

### 🧠 Working Principle

1. **Initialization** – Create a table to store computed results.
2. **Check before compute** – Before computing `f(n)`, check if it’s already in the table.
3. **Store result** – After computing, store the result in the table for future use.
4. **Reuse** – Retrieve from memory instead of recalculating.

---

### ⏱️ Complexity Comparison

| Approach                           | Time Complexity | Space Complexity |
| ---------------------------------- | --------------- | ---------------- |
| Naive recursion                    | O(2ⁿ)           | O(n)             |
| With memory function (memoization) | O(n)            | O(n)             |

---

### 🧩 General Form of a Memory Function

```
M(n):
    if table[n] is filled:
        return table[n]
    else:
        compute M(n)
        store in table[n]
        return table[n]
```

---

### 🧩 Examples of Problems Using Memory Functions

* Fibonacci numbers
* Factorial
* Binomial coefficient
* Matrix chain multiplication
* Longest common subsequence
* Knapsack problem
* Shortest path algorithms (e.g., Floyd–Warshall with memoization)

---

### ⚙️ Difference Between Dynamic Programming and Memory Functions

| Feature         | Memory Function       | Dynamic Programming    |
| --------------- | --------------------- | ---------------------- |
| Approach        | **Top-down**          | **Bottom-up**          |
| Uses recursion  | ✅ Yes                 | ❌ No                   |
| Storage         | Memoization table     | DP table               |
| Execution order | As needed (on-demand) | Systematic (iterative) |

---

### 🧩 Summary

* Memory functions = **recursion + caching**.
* They **avoid recomputation**, saving time and improving efficiency.
* Used widely in **Dynamic Programming** to solve overlapping subproblems.

---

