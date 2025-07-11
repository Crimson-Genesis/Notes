# Unit - 2 -> Algorithms for Query Processing and Optimization
Introduction to Translating SQL Queries into Relational Algebra, Algorithms for External Sorting; Algorithms for SELECT and JOIN Operations,
Combining Operations Using Pipelining, Using Heuristics in Query Optimization; Using Selectivity and Cost Estmates in Query Optimization(T1).

## Content ->
### Introduction to Translating SQL Queries into Relational Algebra — Detailed Explanation

#### 1. **Purpose of Translation**

* The SQL queries written by users are declarative and need to be converted into a procedural form for execution.
* Relational Algebra provides a set of operations that define how data is retrieved and manipulated.
* Translation allows the DBMS to optimize and execute SQL efficiently.

---

#### 2. **SQL vs Relational Algebra**

| SQL                            | Relational Algebra                                |
| ------------------------------ | ------------------------------------------------- |
| Declarative (what to retrieve) | Procedural (how to retrieve it)                   |
| User-friendly                  | Formal and precise                                |
| Used for writing queries       | Used for internal query processing & optimization |

---

#### 3. **Translation Process Steps**

##### a) **Parsing**

* SQL query is parsed to check for syntax and semantic correctness.
* Query is converted into a **parse tree**.

##### b) **Logical Plan Generation**

* Parse tree is transformed into a **logical query plan** using relational algebra.
* Represents the logical sequence of operations (selection, projection, join, etc.).

##### c) **Optimization**

* The logical plan is optimized by reordering operations, pushing selections, and choosing efficient algorithms.

##### d) **Physical Plan Generation**

* Logical operators are mapped to actual physical algorithms (e.g., index scan, nested loop join).
* Results in an executable query plan.

---

#### 4. **Basic Relational Algebra Operations for Translation**

| SQL Clause          | Relational Algebra Operation                                        |
| ------------------- | ------------------------------------------------------------------- |
| `SELECT` (columns)  | **π (Projection)**                                                  |
| `FROM` (tables)     | **× (Cartesian Product)** or **⨝ (Join)**                           |
| `WHERE` (condition) | **σ (Selection)**                                                   |
| `GROUP BY`          | **γ (Grouping/Aggregation)**                                        |
| `DISTINCT`          | **δ (Duplicate Elimination)**                                       |
| `ORDER BY`          | Not directly in standard algebra, implemented later in query engine |

---

#### 5. **Example Translation**

**SQL Query:**

```sql
SELECT name
FROM employee
WHERE dept = 'HR';
```

**Relational Algebra Translation:**

```
π_name(σ_dept='HR'(employee))
```

* `σ_dept='HR'` → Select records where dept is 'HR'.
* `π_name` → Project only the name attribute.

---

#### 6. **Importance in DBMS**

* Translation forms the foundation for optimization.
* Enables query planners to analyze and choose efficient execution strategies.
* Helps DBMS to break complex SQL into fundamental operations.

---
### Algorithms for External Sorting — Detailed Explanation

#### 1. **Definition**

* **External sorting** refers to sorting large amounts of data that **do not fit entirely into main memory (RAM)**.
* Data is stored on disk and accessed in blocks.
* Efficient disk I/O management is crucial.

---

#### 2. **Why External Sorting Is Needed**

* Main memory has limited capacity.
* Sorting must be performed using disk storage (secondary storage).
* Goal: Minimize disk I/O operations.

---

#### 3. **Standard Algorithm: Multiway Merge Sort (External Merge Sort)**

##### **Phase 1: Sorting (Run Generation Phase)**

* Divide the unsorted file into **runs** (chunks) that fit into available memory (M blocks).
* Each run is loaded into memory, **sorted using an in-memory algorithm** (e.g., quicksort or heapsort).
* Sorted runs are written back to disk.

##### **Phase 2: Merging (Merge Phase)**

* Repeatedly merge multiple sorted runs into larger sorted runs.
* Use a **k-way merge** (merge k runs at a time using k input buffers and 1 output buffer).
* Continue merging until a single sorted run remains.

---

#### 4. **Parameters and Notation**

* **N:** Total number of blocks in the file.
* **M:** Number of blocks that can be loaded into memory at a time.
* **d:** Degree of merge (number of runs merged in one pass), typically `d = M - 1`.
* **Number of Passes:**

  * Pass 0: Initial run generation.
  * Pass 1 to k: Merging runs.
  * Total passes = `1 + ⌈log_d(⌈N/M⌉)⌉`

---

#### 5. **Example**

Suppose:

* File size = 1000 blocks
* Memory size = 100 blocks
* ⇒ Can generate 10 initial sorted runs in Pass 0

If `d = 99`, then:

* **Pass 1**: Merge all 10 runs → final sorted file
* **Total passes = 2**

---

#### 6. **Buffer Usage**

* For each run being merged: allocate 1 input buffer.
* Allocate 1 output buffer for the merged result.
* Total memory required = d input buffers + 1 output buffer ≤ M

---

#### 7. **Cost of External Sorting**

* **I/O cost per pass:** Read + Write = 2N blocks
* **Total I/O Cost:** `2N × number of passes`

---

#### 8. **Optimizations**

* Use **double buffering** to overlap I/O and computation.
* Increase **degree of merge** (d) by using more memory.
* Use **replacement selection** to generate longer initial runs.

---

#### 9. **Advantages**

* Scales to very large datasets.
* Efficient use of memory and disk I/O.

#### 10. **Disadvantages**

* Requires multiple passes over data.
* Slower than in-memory sorting for small datasets.

---

### Summary Table

| Phase          | Description                             |
| -------------- | --------------------------------------- |
| Run Generation | Sort M-sized chunks in memory           |
| Merge Phase    | Merge multiple runs using buffers       |
| Cost per pass  | 2N (read + write)                       |
| Total passes   | `1 + ⌈log_d(⌈N/M⌉)⌉`                    |
| Optimization   | Double buffering, replacement selection |

---
### Algorithms for SELECT Operation — Detailed Explanation

#### 1. **Purpose of SELECT Operation**

* The `SELECT` operation in relational algebra retrieves rows from a table that satisfy a given condition.
* In SQL: `SELECT * FROM R WHERE condition;`
* In Relational Algebra: `σ_condition(R)`

#### 2. **Types of Selection Conditions**

* **Equality selection:** `A = value`
* **Range selection:** `A > value`, `A < value`, etc.
* **Conjunctive selection:** `A = value AND B = value`
* **Disjunctive selection:** `A = value OR B = value`
* **Negation:** `NOT (A = value)`

---

#### 3. **Algorithms for SELECT Operation**

---

### **1. Linear (Sequential) Search**

* **Description:** Scan all records in the relation one-by-one.
* **When Used:** No index or hashing available.
* **Cost:** `b` block reads, where `b = number of blocks in the relation`.

**Advantages:**

* Simple to implement.
* Always works regardless of data organization.

**Disadvantages:**

* Very slow for large datasets.

---

### **2. Binary Search**

* **Description:** Use binary search on a **sorted file** based on the search key.
* **When Used:** File is ordered on the selection attribute.
* **Cost:**

  * `log₂(b)` to locate the block.
  * Then scan within the block and possibly adjacent ones for all matching records.

**Advantages:**

* Faster than linear search for sorted files.

**Disadvantages:**

* Only applicable if file is sorted on the selection attribute.

---

### **3. Index-Based Search**

* **Description:** Use an index to locate the record(s) satisfying the condition.
* **Index Types:** B+ Tree, Hash Index, ISAM, etc.

#### a) **Primary Index (Clustered) Search**

* **Used When:** Index is built on the primary key or clustered attribute.
* **Cost:**

  * Index traversal (usually 2–4 block reads).
  * Direct access to the block containing the record.

**Efficient for:** Equality and range queries.

---

#### b) **Secondary Index (Unclustered) Search**

* **Used When:** Index is on a non-primary or non-clustered attribute.
* **Cost:**

  * Index traversal.
  * Additional I/Os to fetch actual records.

**Drawback:** May require multiple I/Os if matching records are spread across many blocks.

---

#### c) **Hash-Based Search**

* **Used For:** Equality search using hash index.
* **Cost:**

  * Compute hash value.
  * Direct access to the bucket.

**Not suitable for:** Range queries.

---

#### 4. **Conjunctive and Disjunctive Selections**

* **Conjunctive (`AND`):**

  * Apply most selective condition first to reduce intermediate results.
  * Use index intersection if indexes exist on multiple attributes.

* **Disjunctive (`OR`):**

  * Use **index union** if indexes exist.
  * Otherwise, perform separate selections and take the union of results.

---

### Summary Table

| Algorithm         | When to Use                      | Suitable For   | Cost (Approx.)                  |
| ----------------- | -------------------------------- | -------------- | ------------------------------- |
| Linear Search     | No index, small file             | Any condition  | b block reads                   |
| Binary Search     | File sorted on attribute         | Equality/Range | log₂(b) + few extra reads       |
| Primary Index     | Index on search key (clustered)  | Equality/Range | Index traversal + 1 I/O         |
| Secondary Index   | Index on non-clustered attribute | Equality       | Index traversal + multiple I/Os |
| Hash-Based Search | Hash index on attribute          | Equality only  | 1–2 I/Os                        |

---

### Algorithms for JOIN Operations — Detailed Explanation

#### 1. **JOIN Operation Purpose**

* Combines related tuples from two relations based on a common attribute.
* SQL:

  ```sql
  SELECT * FROM R, S WHERE R.A = S.B;
  ```
* Relational Algebra:

  ```
  R ⨝ S
  ```

---

#### 2. **Types of Joins (based on conditions)**

* **Theta Join (`R ⨝θ S`)**: General join with condition (e.g., `R.A < S.B`)
* **Equi-Join**: Condition is equality (`R.A = S.B`)
* **Natural Join**: Equi-join on all attributes with the same name
* **Self Join**: Joining a relation with itself
* **Outer Joins**: Retain unmatched rows (not covered here unless asked)

---

#### 3. **Join Algorithms**

---

### **1. Nested Loop Join (NLJ)**

#### a) **Basic Nested Loop Join**

* For each tuple in relation **R**, scan all tuples in **S** and test the join condition.

**Cost:**

* `b_R + (n_R × b_S)`

  * `b_R` = blocks in R
  * `b_S` = blocks in S
  * `n_R` = number of tuples in R

**Advantage:**

* Simple and always applicable.

**Disadvantage:**

* Very slow for large relations.

---

#### b) **Block Nested Loop Join**

* Read one block of R into memory and for each block, scan entire S.

**Cost:**

* `b_R + (b_R × b_S)`

**Optimization:**

* If `M` is the number of available memory blocks:

  * `⌈b_R / (M-1)⌉ × b_S + b_R`

---

### **2. Index Nested Loop Join**

* For each tuple in **R**, use an index on **S** to find matching tuples.

**Requirements:**

* Index must exist on join attribute of **S**.

**Cost:**

* `b_R + n_R × cost of index lookup`

**Efficient when:**

* `R` is small and `S` has an index on join attribute.

---

### **3. Sort-Merge Join (SMJ)**

**Steps:**

1. Sort both **R** and **S** on join attributes.
2. Merge the sorted relations by scanning both together.

**Cost:**

* Sorting:

  * `R`: `b_R × log b_R`
  * `S`: `b_S × log b_S`
* Merging:

  * `b_R + b_S`

**Total Cost:**

* Sorting cost + merging cost

**Efficient when:**

* Inputs are already sorted.
* Good for range join conditions.

---

### **4. Hash Join (Grace Hash Join)**

**Steps:**

1. Partition both **R** and **S** using the same hash function on join attribute.
2. Match partitions pairwise using in-memory hash tables.

**Cost:**

* Partition Phase: `b_R + b_S`
* Probing Phase: `b_R + b_S`
* **Total:** `2(b_R + b_S)`

**Requirements:**

* Enough memory to hold at least one partition of R.

**Efficient for:**

* Large equi-joins with no existing indexes or sorting.

---

### Summary Table

| Join Algorithm         | Requirements                        | Best For                | Cost (approx)               |
| ---------------------- | ----------------------------------- | ----------------------- | --------------------------- |
| Nested Loop Join       | None                                | Small relations         | `b_R + (n_R × b_S)`         |
| Block Nested Loop Join | More memory blocks                  | Moderate size joins     | `b_R + (b_R × b_S)`         |
| Index Nested Loop Join | Index on join attribute of S        | Small R, indexed S      | `b_R + (n_R × index cost)`  |
| Sort-Merge Join        | Sorted inputs or large ranges       | Large datasets          | `Sort(R) + Sort(S) + Merge` |
| Hash Join              | Equi-join, enough memory partitions | Large unsorted datasets | `2(b_R + b_S)`              |

---

### Comparison: Algorithms for SELECT vs JOIN Operations — Detailed Explanation

| **Aspect**                  | **SELECT Operation**                                                                           | **JOIN Operation**                                                                 |
| --------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Definition**              | Retrieves tuples from a **single relation** that satisfy a condition.                          | Combines tuples from **two or more relations** based on a join condition.          |
| **Operation Type**          | Unary (operates on one relation).                                                              | Binary (operates on two relations).                                                |
| **Typical Use Case**        | Filter data using conditions (e.g., `WHERE age > 30`).                                         | Combine related data from different tables (e.g., `Employee ⨝ Department`).        |
| **Condition Types**         | - Equality<br>- Inequality<br>- Conjunctive<br>- Disjunctive<br>- Negation                     | - Equi-join<br>- Natural join<br>- Theta join<br>- Outer joins (left, right, full) |
| **Common Algorithms**       | - Linear (Sequential) Search<br>- Binary Search<br>- Index-based Search<br>- Hash-based Search | - Nested Loop Join<br>- Index Nested Loop Join<br>- Sort-Merge Join<br>- Hash Join |
| **Index Usage**             | Indexes can directly point to matching tuples.                                                 | Indexes on join attributes can improve lookup time in index nested loop join.      |
| **Complexity (I/O)**        | Typically low; proportional to number of blocks in a single relation.                          | Typically high; depends on sizes of both relations and algorithm used.             |
| **Memory Requirement**      | Minimal; single block buffer can suffice.                                                      | More memory required, especially for block nested loop and hash join.              |
| **Performance Factors**     | - Existence of indexes<br>- Selectivity of condition<br>- Sortedness of file                   | - Sizes of R and S<br>- Index availability<br>- Join type<br>- Memory availability |
| **Output Size**             | Number of matching tuples from one relation.                                                   | Cartesian-like product (filtered); size can be very large.                         |
| **Optimization Techniques** | - Selection pushdown<br>- Using most selective condition first<br>- Index scan                 | - Join reordering<br>- Choosing efficient join algorithm<br>- Using pipelining     |

---

### Example

**SELECT Example:**

```sql
SELECT * FROM Employee WHERE Dept = 'HR';
```

* Use linear or index-based search to retrieve matching tuples.

**JOIN Example:**

```sql
SELECT * FROM Employee E, Department D WHERE E.DeptID = D.DeptID;
```

* Use nested loop, sort-merge, or hash join to match tuples between `Employee` and `Department`.

---

### Conclusion

* **SELECT** operations are **simpler**, usually apply to **one relation**, and cost **less I/O**.
* **JOIN** operations are **more complex**, operate on **multiple relations**, and are **costlier**, requiring careful choice of algorithm and optimization.

---

### Combining Operations Using Pipelining — Detailed Explanation

#### 1. **Definition**

* **Pipelining** is a query processing technique where the output of one operation is **passed directly as input to the next** without storing intermediate results on disk.
* Reduces disk I/O and memory usage.
* Increases performance by overlapping execution of multiple operations.

---

#### 2. **Why Use Pipelining?**

* Avoids materializing (writing to disk) intermediate results.
* Saves time and disk space.
* Enables efficient evaluation of complex queries composed of multiple relational algebra operations.

---

#### 3. **Types of Pipelining**

##### a) **Tuple-at-a-Time (Demand-driven)**

* Also called **pull-based** or **iterator model**.
* Each operator pulls the next tuple from its input when needed.
* Example: `π_name(σ_dept='HR'(employee))` — projection pulls from selection, which pulls from scan.

##### b) **Block-at-a-Time**

* Operators pass **blocks of tuples** instead of one tuple at a time.
* Improves performance by reducing context-switching and function call overhead.

---

#### 4. **Pipelining vs Materialization**

| Aspect             | **Pipelining**                                   | **Materialization**                              |
| ------------------ | ------------------------------------------------ | ------------------------------------------------ |
| Storage            | No intermediate storage on disk                  | Intermediate results written to disk             |
| I/O Cost           | Reduced due to no disk writes                    | High due to disk reads/writes                    |
| Memory Requirement | Requires less memory                             | May require more memory and disk space           |
| Execution          | Operators work in a demand-driven manner         | Each operation completes before the next         |
| Performance        | Faster, especially for selective queries         | Slower due to materializing intermediate results |
| Suitability        | Best for **streaming data** or **small outputs** | Better when intermediate results are reused      |

---

#### 5. **Example**

**Query:**

```sql
SELECT name FROM employee WHERE dept = 'HR';
```

**Execution without pipelining (Materialization):**

* Selection (`σ_dept='HR'`) creates an intermediate relation on disk.
* Projection (`π_name`) reads from that intermediate relation.

**Execution with pipelining:**

* Projection pulls each matching tuple directly from selection operator.

---

#### 6. **Pipelining and Query Trees**

* Pipelining is naturally represented in **query trees**, where:

  * **Leaf nodes** = base table scans
  * **Internal nodes** = algebra operations
  * **Data flows upward** from child to parent operator

---

#### 7. **When Pipelining Is Not Possible**

* If the operation needs the entire input to produce output (e.g., `sort`, `group by`, `aggregate`), pipelining can't be used directly.
* In such cases, **materialization** is necessary.

---

### Summary Table

| Feature           | Pipelining                                                  |
| ----------------- | ----------------------------------------------------------- |
| Definition        | Passing output of one operator directly to the next         |
| Types             | Tuple-at-a-time, Block-at-a-time                            |
| Benefits          | Reduces disk I/O, memory usage, and improves performance    |
| Limitation        | Not suitable for operations needing full input (e.g., sort) |
| Example Operators | Selection, projection, index scan                           |

---

### Using Heuristics in Query Optimization — Detailed Explanation

#### 1. **Definition**

* **Heuristic-based query optimization** uses **rule-based transformations** to rewrite queries into a more efficient form **without evaluating actual execution cost**.
* Heuristics are **general guidelines or rules of thumb** derived from database theory and practical experience.

---

#### 2. **Goal**

* Improve query performance by **reordering operations** and **reducing intermediate result size**.
* Avoid expensive or inefficient execution plans by applying logical transformation rules.

---

#### 3. **Common Heuristics in Query Optimization**

---

### **Heuristic 1: Perform Selections Early**

* Apply **σ (selection)** as early as possible in the query tree.
* Reduces the number of tuples passed to later operations.
* Applies particularly to highly selective conditions.

**Example:**

```sql
SELECT name FROM employee WHERE salary > 50000 AND dept = 'HR';
```

**Relational Algebra (before):**

```
π_name(σ_salary>50000 AND dept='HR'(employee))
```

**After heuristic (pushing selection down):**

```
π_name(σ_dept='HR'(σ_salary>50000(employee)))
```

---

### **Heuristic 2: Perform Projections Early**

* Apply **π (projection)** early to reduce number of attributes carried through query.
* Minimizes size of intermediate relations.

**Example:**

```
π_name(σ_dept='HR'(employee))
```

* Only carry `name` and `dept` attributes, discard unnecessary ones early.

---

### **Heuristic 3: Combine Selections and Projections**

* Combine adjacent selections and projections into a **single operator** or push them as far down as possible.

**Example:**

```
π_name(σ_salary>50000(σ_dept='HR'(employee)))
```

* Combine into:

```
π_name(σ_salary>50000 AND dept='HR'(employee))
```

---

### **Heuristic 4: Replace Cartesian Product + Selection with JOIN**

* If a **σ condition** follows a **Cartesian product**, and the condition is a join condition, convert it to an explicit **join**.

**Example (before):**

```
σ_E.deptID = D.deptID (Employee × Department)
```

**After applying heuristic:**

```
Employee ⨝ Employee.deptID = Department.deptID Department
```

---

### **Heuristic 5: Perform Most Restrictive Joins First**

* Evaluate joins that produce the smallest intermediate results **earliest**.
* Reduces size of relations processed in later joins.

---

### **Heuristic 6: Use Indexes Where Possible**

* If selection or join condition uses an attribute with an **index**, choose index scan instead of full table scan.

---

### **Heuristic 7: Avoid Repeated Computation**

* Materialize or cache intermediate results if reused multiple times in the query.

---

#### 4. **Benefits of Heuristic Optimization**

* **Fast:** Does not require cost estimation.
* **Simple to implement:** Uses algebraic transformation rules.
* **Good enough:** Produces efficient plans in many practical scenarios.

---

#### 5. **Limitations**

* May not always produce the **most optimal** plan.
* Cannot account for **actual data statistics** (e.g., tuple counts, selectivity).
* Less effective for complex queries compared to cost-based optimization.

---

### Summary Table

| Heuristic Rule                                  | Purpose                                    |
| ----------------------------------------------- | ------------------------------------------ |
| Push selections down                            | Reduce number of tuples early              |
| Push projections down                           | Reduce number of attributes early          |
| Combine selections and projections              | Simplify query tree                        |
| Replace Cartesian product + selection with join | Avoid inefficient Cartesian operations     |
| Evaluate most selective joins first             | Reduce intermediate relation size          |
| Use indexes if available                        | Speed up data access                       |
| Avoid recomputation                             | Improve efficiency for repeated subqueries |

---

### Using Selectivity in Query Optimization — Detailed Explanation

#### 1. **Definition of Selectivity**

* **Selectivity** is a measure of **how many tuples** satisfy a condition **relative to the total number of tuples** in a relation.
* It is used in query optimization to **estimate the size of intermediate results**, which directly affects query cost and execution plan.

---

#### 2. **Formula for Selectivity**

$$
\text{Selectivity} = \frac{\text{Number of tuples satisfying condition}}{\text{Total number of tuples in relation}}
$$

* **Range:** 0 (no tuples satisfy) to 1 (all tuples satisfy).
* **Lower selectivity** means **more filtering** (fewer results).
* **Higher selectivity** means **less filtering** (more results).

---

#### 3. **Importance in Query Optimization**

* Helps the optimizer:

  * Estimate **intermediate result sizes**.
  * Choose **efficient join orders**.
  * Decide **whether to use an index** or a full scan.
  * Select the most **selective predicate to apply first**.

---

#### 4. **Examples**

##### a) **Simple Equality Predicate**

```sql
SELECT * FROM Employee WHERE gender = 'F';
```

* Assume 1000 employees, 500 are female:

$$
\text{Selectivity} = \frac{500}{1000} = 0.5
$$

##### b) **Highly Selective Condition**

```sql
SELECT * FROM Employee WHERE emp_id = 123;
```

* Only one match out of 1000:

$$
\text{Selectivity} = \frac{1}{1000} = 0.001
$$

* **Very selective** → good candidate to use **index scan**.

##### c) **Low Selectivity**

```sql
SELECT * FROM Employee WHERE salary > 10000;
```

* Assume 900 out of 1000 qualify:

$$
\text{Selectivity} = \frac{900}{1000} = 0.9
$$

* **Low filtering effect** → full scan may be better.

---

#### 5. **Types of Predicates and Selectivity Estimation**

| Predicate Type          | Estimated Selectivity                              |   |          |   |                                       |
| ----------------------- | -------------------------------------------------- | - | -------- | - | ------------------------------------- |
| Equality (`A = x`)      | \`1 /                                              | A | `(where` | A | \` is number of distinct values of A) |
| Range (`A > x`)         | Depends on value distribution; often `1/3` assumed |   |          |   |                                       |
| Conjunctive (`A AND B`) | `Sel(A) × Sel(B)` (assuming independence)          |   |          |   |                                       |
| Disjunctive (`A OR B`)  | `Sel(A) + Sel(B) – Sel(A) × Sel(B)`                |   |          |   |                                       |

---

#### 6. **Selectivity and Index Usage**

* **Low selectivity (close to 0):**

  * Few matching tuples.
  * **Use index scan** for efficient retrieval.

* **High selectivity (close to 1):**

  * Most tuples match.
  * **Avoid index**; use full scan to avoid random I/Os.

---

#### 7. **Use in Join Optimization**

* Helps choose the **order of joins**.
* Join the most **selective relations first** to minimize intermediate results.
* Reduce cost in multi-relation queries.

---

### Summary Table

| Concept          | Description                                       |
| ---------------- | ------------------------------------------------- |
| Selectivity      | Fraction of tuples satisfying a predicate         |
| Value Range      | Between 0 (none match) and 1 (all match)          |
| Low Selectivity  | Strong filtering; good for index usage            |
| High Selectivity | Weak filtering; better to use full scan           |
| Application      | Used in estimating query cost and optimizing plan |

---

### Cost Estimates in Query Optimization — Detailed Explanation

#### 1. **Definition**

* **Cost estimation** is the process of predicting the **resource usage** (mainly **I/O cost**, CPU, and memory) of various **query execution plans**.
* It helps the **query optimizer** choose the **most efficient execution plan** from alternatives.

---

#### 2. **Main Goal**

* **Minimize total cost** of executing a query.
* The optimizer evaluates different plans and selects the one with the **lowest estimated cost**.

---

#### 3. **Types of Costs Considered**

| Cost Type              | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| **Disk I/O Cost**      | Number of disk block reads/writes. **Most critical** in traditional DBMS. |
| **CPU Cost**           | Cost of processing tuples in memory (comparisons, hashing, etc.).         |
| **Memory Cost**        | Amount of RAM used by operations (e.g., for sorting, hashing, buffering). |
| **Communication Cost** | In distributed systems, cost of transferring data between nodes.          |

> **Note**: Disk I/O cost dominates in large datasets stored on disk.

---

#### 4. **Factors Influencing Cost Estimation**

##### a) **Size of Relations**

* Total number of **tuples** and **blocks** in each relation.

##### b) **Selectivity of Predicates**

* Helps estimate number of tuples output by `SELECT` or `JOIN` operations.

##### c) **Availability of Indexes**

* Indexes can reduce access time for selection and join operations.

##### d) **Join Order**

* Different join orders produce different intermediate result sizes.

##### e) **Join Algorithms**

* Nested loop, sort-merge, and hash join all have different cost profiles.

##### f) **Statistics**

* Number of distinct values in columns.
* Value distributions.
* Histograms and sampling are used to gather these.

---

#### 5. **Basic Cost Estimation Formulas**

| Operation                                 | Cost Estimate (I/O)                          |
| ----------------------------------------- | -------------------------------------------- |
| **Sequential Scan (SELECT)**              | `b_R` (number of blocks in relation R)       |
| **Index Scan (SELECT)**                   | `Index lookup cost + tuple fetch cost`       |
| **Nested Loop Join**                      | `b_R + (n_R × b_S)` or `b_R × b_S`           |
| **Block Nested Loop Join**                | `b_R + (b_R × b_S)` or optimized with memory |
| **Sort-Merge Join**                       | `Sort(R) + Sort(S) + b_R + b_S`              |
| **Hash Join**                             | `2 × (b_R + b_S)`                            |
| **Projection with Duplicate Elimination** | `Scan + Sort or Hash + Deduplication`        |

---

#### 6. **Example: SELECT Cost Estimation**

```sql
SELECT * FROM Employee WHERE dept = 'HR';
```

Assume:

* `b_Employee = 1000 blocks`
* No index on `dept`
* Selectivity = 0.1

→ **Cost = 1000 block reads** (linear scan)
→ Expected output: 10% of tuples

---

#### 7. **Example: JOIN Cost Estimation**

```sql
SELECT * FROM Employee E, Department D WHERE E.deptID = D.deptID;
```

Assume:

* `b_E = 1000`, `b_D = 100`
* No index, use block nested loop join

→ **Cost = 1000 + (1000 × 100) = 101,000 block reads**

If index on `D.deptID`:
→ Use **Index Nested Loop Join**
→ Cost = `1000 (read E) + 1000 × (index lookup + 1)`

---

#### 8. **Role in Query Optimizer**

* Cost estimates are used to:

  * Compare alternative query plans.
  * Reorder joins and filters.
  * Decide between full scan vs index scan.
  * Choose join algorithm (e.g., hash vs nested loop).
  * Select best physical access paths.

---

### Summary Table

| Component         | Description                                     |
| ----------------- | ----------------------------------------------- |
| Disk I/O Cost     | Main factor in traditional cost models          |
| Selectivity       | Used to estimate result sizes                   |
| Size of Relations | Affects scan and join cost                      |
| Statistics Used   | Tuple count, block count, distinct values       |
| Used In           | Join ordering, index usage, algorithm selection |

---

### **Using Selectivity vs Cost Estimates in Query Optimization — Detailed Comparison**

| **Aspect**              | **Selectivity**                                                                                                   | **Cost Estimates**                                                                 |            |   |                                       |                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------- | - | ------------------------------------- | ---------------------------------------------------- |
| **Definition**          | Fraction of tuples satisfying a condition in a relation.                                                          | Prediction of total resources (I/O, CPU, memory) needed to execute a query plan.   |            |   |                                       |                                                      |
| **Primary Purpose**     | Estimate **size of intermediate results**.                                                                        | Estimate **execution cost** of entire query plans.                                 |            |   |                                       |                                                      |
| **Type**                | **Logical metric** (data-level estimation).                                                                       | **Physical metric** (resource-level estimation).                                   |            |   |                                       |                                                      |
| **Range**               | Value between `0` and `1`.                                                                                        | Numerical cost values (e.g., number of disk I/Os, CPU cycles).                     |            |   |                                       |                                                      |
| **Used For**            | - Evaluating predicate filtering strength.<br>- Guiding join order.<br>- Deciding which condition to apply first. | - Comparing alternative execution plans.<br>- Selecting the lowest-cost plan.      |            |   |                                       |                                                      |
| **Influences**          | - Join ordering.<br>- Operator reordering.<br>- Index usage.<br>- Push-down strategies.                           | - Operator selection (e.g., hash join vs nested loop).<br>- Access path decisions. |            |   |                                       |                                                      |
| **Example Calculation** | \`Selectivity(A = 5) = 1 /                                                                                        | A                                                                                  | `, where ` | A | \` is number of distinct values in A. | `Cost(join) = b_R + n_R × b_S` for nested loop join. |
| **Dependencies**        | - Depends on **data distribution**.<br>- Requires **statistical metadata**.                                       | - Depends on **selectivity, block sizes, index availability, algorithm**.          |            |   |                                       |                                                      |
| **Result**              | Estimate of **how many** tuples will be output.                                                                   | Estimate of **how expensive** a query plan will be to run.                         |            |   |                                       |                                                      |
| **Measurement Unit**    | **Ratio** or **percentage**.                                                                                      | **Block I/Os**, **CPU time**, or **abstract cost unit**.                           |            |   |                                       |                                                      |
| **Used By**             | Logical optimizer / Selectivity estimator.                                                                        | Cost-based query optimizer.                                                        |            |   |                                       |                                                      |
| **Accuracy Importance** | Crucial for **accurate size prediction** of intermediate results.                                                 | Crucial for **choosing the optimal execution plan**.                               |            |   |                                       |                                                      |
| **Tool Support**        | - Histograms<br>- Sampling<br>- Catalog statistics                                                                | - Cost model<br>- Query optimizer engine                                           |            |   |                                       |                                                      |

---

### **How They Work Together**

* **Selectivity** is a **key input to cost estimation**.
* Cost estimation relies on **accurate selectivity** to predict:

  * Number of disk I/Os (for table scans or joins)
  * Number of tuples processed
  * Memory requirements
* If selectivity is wrong → cost estimation will be wrong → **suboptimal query plan** may be chosen.

---

### **Illustrative Example**

```sql
SELECT * FROM Employee WHERE gender = 'F';
```

* Assume:

  * Total tuples: 10,000
  * Matching tuples: 5,000 → **Selectivity = 0.5**
  * Relation occupies 1000 blocks
  * With no index → full scan → **Cost = 1000 I/Os**
  * With index → **Cost = 500 index lookups + 500 I/Os**

> Accurate selectivity helps choose index scan (if better), else stick with full scan.

---

### **Conclusion**

* **Selectivity** is a **component** of **cost estimation**.
* **Selectivity = logical filtering power**.
* **Cost Estimate = total execution effort**.
* **Both work together** to guide the optimizer in choosing efficient plans.

---

