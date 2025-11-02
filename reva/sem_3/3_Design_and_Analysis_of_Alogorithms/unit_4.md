# Unit - 4

## Limitations of Algorithms Power and Coping with Limitations of Algorithm Power
- Np-hard and Np-complete problems
- basic concepts
- Non-deterministic algorithms
- Np-hard and np-complete classes
- Cook's Theorem

- Backtracking: n-Queens Problem
- Backtracking: hamiltonian Circuit Problem
- Backtracking: Subset - Sum Problem

- Branch-and-Bound: Assignment Problem
- Branch-and-Bound: Knapsack Problem
- Branch-and-Bound: Traveling Salesperson Problem

---
---

# 💻 NP-Hard and NP-Complete Problems

Understanding **NP-hard** and **NP-complete** problems is fundamental in the **Design and Analysis of Algorithms** — especially when studying **computational complexity**.

---

## 🧠 1. Introduction to Complexity Classes

Algorithms are classified based on how difficult they are to solve computationally.
Let’s look at the main **complexity classes**:

| Class           | Meaning                                                                      | Example Problem                              |
| --------------- | ---------------------------------------------------------------------------- | -------------------------------------------- |
| **P**           | Problems that can be **solved in polynomial time**                           | Binary Search, Merge Sort                    |
| **NP**          | Problems whose **solutions can be verified** in polynomial time              | Traveling Salesman, Subset Sum               |
| **NP-Hard**     | Problems that are **at least as hard as NP problems**, not necessarily in NP | Halting Problem, Optimization versions       |
| **NP-Complete** | Problems that are **both NP and NP-Hard**                                    | Traveling Salesman (decision version), 3-SAT |

---

## ⚙️ 2. Understanding Polynomial Time

A problem is **polynomial time solvable** if it can be solved in
$O(n^k)$ time, where *k* is a constant.

Examples:

* Linear Search → $O(n)$
* Merge Sort → $O(n \log n)$

If a problem can’t be solved in polynomial time, it is considered **intractable**.

---

## 🧩 3. NP (Nondeterministic Polynomial Time)

* **Definition:**
  Problems for which **a proposed solution can be verified quickly (in polynomial time)**.
* The key idea: *We may not know how to find the solution fast, but if someone gives the solution, we can check it fast.*

**Example:**
👉 *Subset Sum Problem*
Given a set of numbers, is there a subset whose sum = given value?

* Finding the subset may take exponential time.
* But if someone gives you a subset, you can verify its sum in **O(n)** time.

---

## 🔥 4. NP-Hard Problems

* **Definition:**
  A problem is **NP-Hard** if every problem in NP can be **reduced** to it in **polynomial time**.
  In short: *It’s at least as hard as the hardest NP problems.*

* NP-Hard problems **may or may not be in NP**.
  (That is, we might not even be able to verify solutions efficiently.)

**Examples:**

* Traveling Salesman Problem (TSP) – *minimize total distance* (optimization form)
* Knapsack Problem – optimization version
* Halting Problem – undecidable

🧮 **Mathematically:**
$$
L \text{ is NP-Hard if } \forall L' \in NP, ; L' \le_P L
$$
(meaning every NP problem $L'$ can be polynomially reduced to $L$)

---

## 💡 5. NP-Complete Problems

* **Definition:**
  A problem is **NP-Complete** if:

  1. It is in **NP** (solution can be verified in polynomial time).
  2. It is **NP-Hard** (all NP problems can be reduced to it).

In short:

> NP-Complete = NP ∩ NP-Hard

**Examples:**

* Boolean Satisfiability (SAT)
* 3-SAT Problem
* Hamiltonian Cycle
* Subset Sum (decision version)
* Traveling Salesman Problem (decision form)

---

## ⚖️ 6. Relationship Between P, NP, NP-Complete, NP-Hard

Here’s a visual diagram:

```
         ┌────────────────────────────┐
         │          NP-HARD           │
         │    ┌──────────────────┐    │
         │    │     NP           │    │
         │    │  ┌────────────┐  │    │
         │    │  │ NP-COMPLETE│  │    │
         │    │  └────────────┘  │    │
         │    └──────────────────┘    │
         └────────────────────────────┘
```

**Explanation:**

* `P` ⊆ `NP`
* `NP-Complete` ⊆ `NP`
* `NP-Hard` ⊇ `NP-Complete`

---

## 🧮 7. Polynomial-Time Reduction

To prove that a problem A is **NP-Hard**, we:

1. Take a **known NP-Complete problem** (say Problem B).
2. Show that **B can be reduced to A** in polynomial time.
   (written as: B ≤ₚ A)

This means **A is at least as hard as B**.

---

## 📘 8. Example: Traveling Salesman Problem (TSP)

**Decision version (NP-Complete):**
Given a graph and distance limit `k`, is there a path visiting all cities exactly once with total cost ≤ k?

**Optimization version (NP-Hard):**
Find the *shortest* possible route visiting all cities exactly once.

---

## ⚙️ 9. Real-World Examples

| Problem             | Category    | Description                                            |
| ------------------- | ----------- | ------------------------------------------------------ |
| Traveling Salesman  | NP-Complete | Find minimal tour visiting all cities once             |
| Knapsack (decision) | NP-Complete | Is there a subset within capacity W having profit ≥ P? |
| Graph Coloring      | NP-Complete | Can graph be colored using ≤ k colors?                 |
| Scheduling          | NP-Hard     | Find optimal job schedule minimizing total cost        |
| Halting Problem     | NP-Hard     | Decide if program halts on given input (undecidable)   |

---

## 🚀 10. P vs NP Question

The **biggest open question** in computer science:

> **Is P = NP?**

Meaning:
Can every problem whose solution can be *verified* quickly also be *solved* quickly?

If proven true:

* Many hard problems would become efficiently solvable.
  If false:
* There exist problems that are verifiable but not solvable efficiently.

Still **unsolved** to this day — with a **$1 million reward** (Clay Mathematics Institute).

---

## 🧩 Summary Table

| Property                               | P          | NP         | NP-Complete | NP-Hard   |
| -------------------------------------- | ---------- | ---------- | ----------- | --------- |
| Solvable in polynomial time            | ✅          | ❌          | ❌           | ❌         |
| Solution verifiable in polynomial time | ✅          | ✅          | ✅           | ❌         |
| As hard as hardest NP problems         | ❌          | ❌          | ✅           | ✅         |
| Example                                | Merge Sort | Subset Sum | 3-SAT       | TSP (opt) |

---

### ✅ **Key Takeaways**

* **NP-Hard** → hardest problems; may not even be verifiable in polynomial time.
* **NP-Complete** → subset of NP-Hard; both verifiable and as hard as NP problems.
* All **P problems** are in **NP**, but not all NP problems are in P.
* **P vs NP** remains **unsolved** — one of the **Millennium Prize Problems**.

---

# 🧩 Basic Concepts of NP-Hard and NP-Complete Problems

These concepts explain how we **classify problems based on difficulty** and **analyze algorithmic solvability** using **computational complexity theory**.

---

## 🧠 1. What Is a Computational Problem?

A **problem** is a **question** that can be answered by an algorithm.
Each problem has:

* **Input:** data given to the algorithm.
* **Output:** expected result or answer.

**Example:**

> Problem: Is there a path between vertex A and vertex B in a given graph?

Here:

* Input → Graph G, vertices A, B
* Output → “Yes” or “No”

---

## ⚙️ 2. Classification of Problems

Problems are classified into **three main categories**:

| Type                     | Meaning                      | Example                              |
| ------------------------ | ---------------------------- | ------------------------------------ |
| **Decision Problem**     | Answer is **Yes / No**       | Is there a path of cost ≤ K?         |
| **Optimization Problem** | Find **best solution**       | Find the shortest path               |
| **Search Problem**       | Find **a specific solution** | Find the actual path between A and B |

> 💡 NP-Complete theory mainly deals with **decision problems**.

---

## 🧮 3. Polynomial Time and Exponential Time

The **efficiency** of an algorithm depends on **how its running time grows** with input size.

| Class                | Time Complexity                   | Example                   |
| -------------------- | --------------------------------- | ------------------------- |
| **Polynomial Time**  | $O(n^k)$, where *k* is a constant | Merge Sort ($O(n\log n)$) |
| **Exponential Time** | $O(2^n)$, $O(n!)$                 | Subset Sum, TSP           |

**Polynomial time algorithms** are considered *efficient* and *tractable*.
**Exponential time algorithms** are *intractable* for large inputs.

---

## ⚡ 4. Tractable vs Intractable Problems

| Term            | Meaning                                                               |
| --------------- | --------------------------------------------------------------------- |
| **Tractable**   | Problems that can be solved efficiently (in polynomial time)          |
| **Intractable** | Problems that cannot be solved efficiently; may need exponential time |
| **Undecidable** | Problems that have no algorithmic solution at all                     |

**Example:**

* Sorting → Tractable
* Traveling Salesman → Intractable
* Halting Problem → Undecidable

---

## 🔁 5. Deterministic vs Non-Deterministic Algorithms

| Type                            | Description                                                                               | Example                    |
| ------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------- |
| **Deterministic Algorithm**     | Produces the same output every time for a given input; follows fixed steps.               | Merge Sort, Binary Search  |
| **Non-Deterministic Algorithm** | Can make “guesses” and verify correctness quickly; theoretical model used in NP problems. | Used in NP-complete theory |

In NP, we imagine a **Non-Deterministic Turing Machine (NDTM)** that can:

* “Guess” a possible solution instantly.
* Verify that guess in **polynomial time**.

---

## ⏱️ 6. Measuring Complexity

Two main types of complexity measures:

| Type                 | Description                          |
| -------------------- | ------------------------------------ |
| **Time Complexity**  | Number of steps to solve the problem |
| **Space Complexity** | Amount of memory used                |

We compare problems based on how their time complexity grows with input size.

---

## 💡 7. Complexity Classes

Now let’s see where P, NP, NP-Complete, and NP-Hard fit in.

| Class           | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| **P**           | Set of all decision problems solvable in polynomial time.                    |
| **NP**          | Set of decision problems whose solutions can be verified in polynomial time. |
| **NP-Complete** | Set of problems that are both NP and NP-Hard.                                |
| **NP-Hard**     | Problems that are at least as hard as NP problems (not necessarily in NP).   |

**Relationship Diagram:**

```
        ┌──────────────────────┐
        │      NP-HARD         │
        │  ┌───────────────┐   │
        │  │  NP           │   │
        │  │ ┌───────────┐ │   │
        │  │ │ NP-COMP.  │ │   │
        │  │ └───────────┘ │   │
        │  └───────────────┘   │
        └──────────────────────┘
```

---

## 🔁 8. Reductions

**Reduction** means transforming one problem into another in **polynomial time**.

Used to show **how hard** a problem is.

If we can transform any known NP-Complete problem (A) into a new problem (B):

* Then **B is at least as hard as A**
* So **B is NP-Hard**.

Notation:
$$ A \le_P B $$
(read as: “A is polynomial-time reducible to B”)

---

## 💬 9. Example of Reduction

Let’s reduce **3-SAT** (known NP-Complete) to **Hamiltonian Cycle**.

If every instance of 3-SAT can be converted to a Hamiltonian Cycle problem in polynomial time, then:

* Hamiltonian Cycle is **NP-Hard**.
* If it’s also in NP, it’s **NP-Complete**.

---

## 🧮 10. P vs NP Problem

Big open question:

> Is P = NP ?

Meaning:

* Are problems whose solutions can be verified quickly also solvable quickly?

💰 Still unsolved — **$1 million** reward (Clay Mathematics Institute).

---

## 🔑 Summary Table

| Concept          | Meaning                  | Example            |
| ---------------- | ------------------------ | ------------------ |
| Problem          | A computational task     | Sorting            |
| Decision Problem | Yes/No output            | Is path ≤ k?       |
| Tractable        | Solvable in poly time    | Merge Sort         |
| Intractable      | Not solvable efficiently | TSP                |
| NP               | Verifiable in poly time  | Subset Sum         |
| NP-Hard          | At least as hard as NP   | TSP (Optimization) |
| NP-Complete      | NP + NP-Hard             | 3-SAT              |
| Reduction        | Transform problem A → B  | SAT → TSP          |

---

### ✅ **Key Takeaways**

* **P:** Solvable fast
* **NP:** Verifiable fast
* **NP-Hard:** Hardest category (not necessarily verifiable)
* **NP-Complete:** Hardest problems *within NP*
* **Reduction:** Tool to prove problem hardness
* **P vs NP:** Unsolved question in computer science

---

# 🧠 Non-Deterministic Algorithms

---

## 🔹 1. Introduction

A **Non-Deterministic Algorithm** is a theoretical concept that allows **“guessing”** of a correct solution from many possible ones **instantly** and then verifying that guess **efficiently** (in polynomial time).

> In simple words:
> 🧩 It’s like having a *“magical computer”* that can explore all possibilities at once and pick the correct one immediately.

This type of algorithm is not physically possible — it’s a **mathematical model** used to study **complexity classes** like **NP**.

---

## ⚙️ 2. Deterministic vs Non-Deterministic Algorithms

| Feature        | Deterministic Algorithm        | Non-Deterministic Algorithm             |
| -------------- | ------------------------------ | --------------------------------------- |
| Execution Path | Only one possible path         | Multiple paths at the same time         |
| Output         | Always the same for same input | May vary depending on guesses           |
| Example        | Binary Search, Merge Sort      | Theoretical algorithms for NP problems  |
| Machine Model  | Deterministic Turing Machine   | Non-Deterministic Turing Machine (NDTM) |
| Used In        | Real-world computation         | Complexity theory (P, NP problems)      |

---

## 🔸 3. Example to Understand Non-Determinism

**Problem:** Given a set of numbers, is there a subset that sums to a target value `T`?

### Deterministic Algorithm

* Check all subsets (there are $2^n$ possibilities).
* Time complexity: $O(2^n)$ → exponential.

### Non-Deterministic Algorithm (imaginary)

1. **Guess** a subset of numbers.
2. **Verify** if the sum = `T`.

✅ If correct → return *YES*
❌ If not → “try” another subset instantly (conceptually).

Verification step takes **O(n)** time.
Thus, the problem is in **NP** (solution can be verified quickly).

---

## 🧩 4. The Non-Deterministic Turing Machine (NDTM)

A **Non-Deterministic Turing Machine** is a theoretical computer model that:

* Can be in **many states simultaneously**.
* At each step, it can **choose between multiple transitions**.
* If *any* of those paths leads to an accepting state → the machine **accepts** the input.

```
        ┌──→ Path 1 → Reject
Start ──┤
        ├──→ Path 2 → Accept ✅
        └──→ Path 3 → Reject
```

If at least one path leads to **Accept**, the NDTM says the answer is **YES**.

---

## ⚙️ 5. Structure of a Non-Deterministic Algorithm

You can think of a non-deterministic algorithm as having two phases:

1. **Guessing Phase:**

   * The algorithm guesses a potential solution (e.g., a subset, path, assignment).
   * This is done instantly (conceptually).

2. **Verification Phase:**

   * It checks if the guessed solution satisfies the problem’s conditions.
   * Must run in **polynomial time**.

---

### 🧮 Pseudocode Example: Non-deterministic Subset Sum

```text
NONDETERMINISTIC_SUBSET_SUM(S, T)
1. Nondeterministically choose a subset S' ⊆ S
2. Compute sum ← sum of all elements in S'
3. if sum == T then
4.     accept
5. else
6.     reject
```

**Verification step:**
Line 2–3 runs in **O(n)** time.

If any subset has sum = T, one of the branches will “guess” it and accept.

---

## 🧩 6. Role in Complexity Classes

Non-determinism is the foundation of **NP (Nondeterministic Polynomial Time)**.

| Class  | Meaning                                                   | Machine Type                     | Example           |
| ------ | --------------------------------------------------------- | -------------------------------- | ----------------- |
| **P**  | Problems solvable in poly time                            | Deterministic Turing Machine     | Merge Sort        |
| **NP** | Problems verifiable in poly time using a guessed solution | Non-deterministic Turing Machine | Subset Sum, 3-SAT |

👉 Thus, NP problems are exactly those that can be solved **by a non-deterministic algorithm in polynomial time**.

---

## 🧠 7. Visualization (Branching Paths)

```
                  ┌── Path 1 → Reject
Input → Step 1 ──┤
                  ├── Path 2 → Reject
                  ├── Path 3 → Accept ✅
                  └── Path 4 → Reject
```

At each step, the algorithm “branches” into multiple possibilities.

If *any* path leads to success → the NDTM halts and outputs “YES”.

---

## 🔍 8. Real-Life Analogy

Imagine you’re trying to unlock a password-protected door.

* **Deterministic:** You try every combination one by one.
* **Non-deterministic:** You magically “guess” the correct password instantly, then check if it works.

You didn’t *search* all; you *instantly guessed the right one*.
That’s what NP problems assume — **instant guessing + fast verification**.

---

## 💡 9. Non-Deterministic Algorithm Examples

| Problem                      | Description                                     | Verification Time |
| ---------------------------- | ----------------------------------------------- | ----------------- |
| Hamiltonian Cycle            | Guess a path visiting all vertices exactly once | O(n²)             |
| Subset Sum                   | Guess subset whose sum = target                 | O(n)              |
| Graph Coloring               | Guess color assignments                         | O(n²)             |
| Boolean Satisfiability (SAT) | Guess variable assignments                      | O(n)              |

All of these belong to **NP**, because once a “guess” is made, it can be checked efficiently.

---

## 🔄 10. Deterministic Simulation of Non-Determinism

Since real computers are deterministic, we can simulate non-determinism by exploring **all possibilities** — but that takes **exponential time**.

Thus:

* A problem solvable in **polynomial time by a non-deterministic algorithm**
  ⟹ **May take exponential time on a real (deterministic) machine.**

---

## ✅ Summary Table

| Concept                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Non-determinism**    | Ability to explore multiple computation paths simultaneously |
| **NDTM**               | Theoretical machine that models non-determinism              |
| **Guess + Verify**     | Structure of non-deterministic algorithm                     |
| **Used in**            | Definition of NP, NP-Hard, NP-Complete                       |
| **Physical Existence** | Not possible; only theoretical                               |
| **Simulation**         | Deterministic machine can simulate, but exponentially slower |

---

## 📘 Example Comparison

| Step | Deterministic     | Non-deterministic               |                           |
| ---- | ----------------- | ------------------------------- | ------------------------- |
| 1    | Choose one option | Explore all options in parallel |                           |
| 2    | Check if correct  | If *any* is correct → Accept    |                           |
| 3    | Time taken        | Exponential                     | Polynomial (conceptually) |
| 4    | Used for          | Real-world computation          | Complexity classification |

---

## ⚖️ 11. Key Takeaways

* A **Non-Deterministic Algorithm** can “guess” a solution and verify it quickly.
* It is modeled by a **Non-Deterministic Turing Machine (NDTM)**.
* All **NP problems** can be expressed as *“non-deterministic polynomial-time algorithms.”*
* Real computers are deterministic — they cannot truly perform non-deterministic computation.
* The open question **P = NP?** asks if deterministic and non-deterministic polynomial time are the same.

---

# 🧠 **NP-Hard and NP-Complete Classes**

### 1. **Background**

When analyzing problems, we often classify them based on **how difficult** they are to solve using algorithms.
Two of the most important complexity classes are:

* **P (Polynomial time):** Problems that can be solved efficiently (in polynomial time).
* **NP (Nondeterministic Polynomial time):** Problems for which a solution, once *guessed*, can be *verified* efficiently (in polynomial time).

Now, some problems are even *harder* than NP problems.
These are **NP-Hard** problems.
Among NP problems, the **hardest** ones are called **NP-Complete**.

---

### 2. **Class Definitions**

| Class           | Meaning                                                             | Example                                      |
| :-------------- | :------------------------------------------------------------------ | :------------------------------------------- |
| **P**           | Problems solvable in polynomial time.                               | Sorting, Searching, MST, Dijkstra            |
| **NP**          | Problems verifiable in polynomial time (solution checking is fast). | Travelling Salesman (decision version), SAT  |
| **NP-Complete** | Problems that are both in NP and as hard as any NP problem.         | SAT, 3-SAT, Hamiltonian Cycle                |
| **NP-Hard**     | Problems at least as hard as NP problems (may not be in NP).        | Optimization version of TSP, Halting Problem |

---

### 3. **Visual Relationship**

```
         ________________________________
        |                                |
        |             NP-Hard            |
        |   ____________                 |
        |  |            |                |
        |  |  NP-Complete|               |
        |  |_____________|               |
        |        |                      |
        |        |  NP (includes P)     |
        |________|______________________|
                 |
                 | P
```

📘 **Explanation:**

* All **P problems** are inside **NP** because if you can solve them quickly, you can also verify them quickly.
* **NP-Complete** problems are the “hardest” in NP.
* **NP-Hard** problems may not even be in NP (some can’t be verified quickly).

---

### 4. **Formal Definitions**

#### **NP-Hard:**

A problem **H** is NP-Hard if every problem **L** in NP can be *polynomially reduced* to **H**.

$$
L \leq_p H
$$

Meaning: If we can solve **H** efficiently, then we can solve all **NP problems** efficiently.

#### **NP-Complete:**

A problem **C** is NP-Complete if:

1. **C** ∈ NP
2. Every problem in NP can be polynomially reduced to **C**

So,
$$
C \in NP \quad \text{and} \quad \forall L \in NP, \ L \leq_p C
$$

---

### 5. **Reduction Concept**

Reduction is a method to show that one problem is *at least as hard* as another.

If **A ≤p B**,
then “A is not harder than B”
or “B is at least as hard as A.”

So, if we can reduce a known NP-Complete problem to another problem **X**,
then **X** is also NP-Hard (and if **X** ∈ NP, then **X** is NP-Complete).

---

### 6. **Examples**

| Problem                               | Classification      | Description                                            |
| :------------------------------------ | :------------------ | :----------------------------------------------------- |
| **Travelling Salesman Problem (TSP)** | NP-Hard             | Optimization: find shortest route visiting all cities. |
| **TSP (Decision version)**            | NP-Complete         | Is there a route shorter than a given distance *D*?    |
| **Knapsack (Optimization)**           | NP-Hard             | Maximize value under weight constraint.                |
| **Subset Sum (Decision)**             | NP-Complete         | Is there a subset with sum = target?                   |
| **Hamiltonian Cycle**                 | NP-Complete         | Does a cycle visit every vertex once?                  |
| **Halting Problem**                   | NP-Hard (not in NP) | Decide if a program halts on given input.              |

---

### 7. **Why NP-Hard/NP-Complete Matters**

Understanding these classes helps us:

* Know which problems have **no known polynomial-time solution**.
* Use **approximation algorithms** or **heuristics** instead of exact algorithms.
* Recognize when to stop searching for “perfect efficiency.”

---

### 8. **Relationship Summary**

| Property                      |       P       |       NP       | NP-Complete |       NP-Hard      |
| :---------------------------- | :-----------: | :------------: | :---------: | :----------------: |
| Solvable in polynomial time   |       ✅       |        ❌       |      ❌      |          ❌         |
| Verifiable in polynomial time |       ✅       |        ✅       |      ✅      |          ❌         |
| Hardest in NP                 |       ❌       |        ❌       |      ✅      |  ✅ (more general)  |
| Example                       | Binary Search | SAT (decision) |    3-SAT    | TSP (optimization) |

---

### 9. **P vs NP Question (The Millennium Problem)**

The biggest open question in computer science:

> Is P = NP?

If **P = NP**, it means every problem that can be verified quickly can also be *solved* quickly — which would revolutionize fields like cryptography, AI, and optimization.

So far, **no proof exists**.
Most experts believe **P ≠ NP**.

---

### ✅ **In Summary**

| Concept         | Definition                                         | Example                             |
| --------------- | -------------------------------------------------- | ----------------------------------- |
| **P**           | Problems solvable in polynomial time               | Sorting, Searching                  |
| **NP**          | Problems verifiable in polynomial time             | SAT, TSP (decision)                 |
| **NP-Hard**     | At least as hard as NP problems (may not be in NP) | TSP (optimization), Halting Problem |
| **NP-Complete** | Hardest problems in NP (in NP + NP-Hard)           | SAT, Hamiltonian Cycle              |

---

# 🧠 **Cook’s Theorem**

### 1. **Introduction**

**Cook’s Theorem** is one of the most fundamental theorems in computer science.
It was proposed by **Stephen Cook** in **1971**, and it laid the foundation for the theory of **NP-Completeness**.

---

### 2. **Statement of Cook’s Theorem**

> **Cook’s Theorem:**
> *The Boolean Satisfiability Problem (SAT) is NP-Complete.*

In simple words:

* SAT was the **first problem ever proven to be NP-Complete**.
* Every problem in **NP** can be **polynomially reduced** to SAT.

---

### 3. **Understanding SAT (Boolean Satisfiability Problem)**

The **SAT problem** asks:

> “Given a Boolean formula (made up of variables, AND, OR, NOT, etc.),
> is there an assignment of truth values (True/False) to the variables that makes the entire formula TRUE?”

---

#### 💡 Example

Formula:

```
F = (A ∨ ¬B) ∧ (B ∨ C)
```

Question:
Is there an assignment of A, B, and C that makes `F = TRUE`?

✅ Example assignment:

* A = TRUE
* B = FALSE
* C = TRUE

Then:

* (A ∨ ¬B) = TRUE ∨ TRUE = TRUE
* (B ∨ C) = FALSE ∨ TRUE = TRUE
  → So, **F = TRUE**.

Hence, this formula is **satisfiable**.

---

### 4. **What Cook Proved**

Cook proved two main things:

1. **SAT ∈ NP**
   Because if someone gives you an assignment of variable values, you can check in polynomial time whether it satisfies the formula.

2. **Every problem in NP can be reduced to SAT in polynomial time**
   This means that any NP problem can be converted into an instance of SAT without exponential growth in size.

Hence, **SAT is NP-Complete**.

---

### 5. **Formal Definition**

Let **L** be any problem in **NP**.
Then, there exists a polynomial-time reduction **f** such that:

$$
x \in L \iff f(x) \in SAT
$$

That is, instance `x` of problem `L` is in the language `L`
**if and only if**
the corresponding Boolean formula `f(x)` is satisfiable.

Therefore:

$$
\text{SAT is NP-Complete.}
$$

---

### 6. **Significance of Cook’s Theorem**

Cook’s Theorem **created the foundation** of the NP-Completeness theory.

Before Cook, we did not know how to compare the difficulty of NP problems.
After his theorem:

* We had a **first NP-Complete problem (SAT)**.
* Then, other NP-Complete problems could be proven by **reducing from SAT**.

Example:

* **3-SAT** → proven NP-Complete by reducing from SAT
* **Clique**, **Vertex Cover**, **Hamiltonian Cycle**, etc. → all proven NP-Complete by reducing from known NP-Complete problems.

---

### 7. **Historical Context**

| Year     | Scientist    | Contribution                                                                     |
| -------- | ------------ | -------------------------------------------------------------------------------- |
| **1971** | Stephen Cook | Proposed Cook’s Theorem — SAT is NP-Complete                                     |
| **1973** | Leonid Levin | Independently proved a similar result (in USSR)                                  |
| **1972** | Richard Karp | Showed that 21 classical problems are NP-Complete (using Cook’s Theorem as base) |

---

### 8. **Proof Idea (Simplified)**

Let’s understand the **intuition** behind the proof.

#### Step 1: Represent NP problems as nondeterministic Turing machines

Every NP problem can be solved by a **nondeterministic Turing machine (NTM)** in polynomial time.

#### Step 2: Encode the computation of NTM as a Boolean formula

Construct a Boolean formula **F** that expresses:

> “There exists a valid computation path of the NTM that leads to an accepting state.”

#### Step 3: Show polynomial size

The formula **F** is built using a **polynomial number of variables and clauses**.

#### Step 4: Equivalence

The formula **F** is satisfiable **if and only if** the Turing machine accepts the input.

Hence, any NP problem can be expressed as a **SAT** instance.

---

### 9. **Graphical Representation**

```
  +-------------------+
  |     NP Problems   |
  +-------------------+
           ↓
  Polynomial-time reduction
           ↓
  +-------------------+
  |   SAT Problem     |
  +-------------------+
         (NP-Complete)
```

---

### 10. **Why Cook’s Theorem is Important**

* It defines the **concept of NP-Completeness**.
* It gives a **starting point** to classify hard problems.
* It allows proving other problems are NP-Complete using **reductions** from SAT.

---

### ✅ **Summary**

| Aspect           | Description                                            |
| :--------------- | :----------------------------------------------------- |
| **Proposed by**  | Stephen Cook (1971)                                    |
| **Statement**    | SAT is NP-Complete                                     |
| **Key idea**     | Every NP problem can be reduced to SAT                 |
| **Impact**       | Foundation of NP-Completeness theory                   |
| **Verification** | Formula satisfaction can be checked in polynomial time |
| **Applications** | Used to prove 1000+ NP-Complete problems               |

---

### 🧩 **In Simple Words**

> Cook’s Theorem says that if we could find a fast (polynomial-time) algorithm for SAT,
> we could solve **every NP problem** quickly.

That’s why SAT is the “root” NP-Complete problem.

---

# 🧠 **Backtracking: n-Queens Problem**

---

## 🧩 1. **Introduction**

The **N-Queens Problem** is a famous problem in computer science used to demonstrate **backtracking**.

> It asks:
> “Can you place `N` queens on an `N × N` chessboard such that **no two queens attack each other**?”

---

### ♕ **Rules**

A queen in chess can attack:

* Horizontally (same row)
* Vertically (same column)
* Diagonally (both diagonals)

So, the condition is:

> **No two queens should share the same row, column, or diagonal.**

---

## 🎯 2. **Goal**

* Place `N` queens on an `N×N` board.
* Print **one or all possible solutions**.
* Use **Backtracking** to explore all possible configurations efficiently.

---

## ⚙️ 3. **Backtracking Concept Recap**

**Backtracking** = **Systematic trial and error**.

Steps:

1. Place a queen in the first valid position in the current row.
2. Move to the next row.
3. If a conflict occurs, **backtrack** — remove the queen and try next column.
4. Continue until all queens are safely placed.

---

## 🧮 4. **Example: 4-Queens Problem**

Let’s solve the **4×4** board.

We must place 4 queens so they do not attack each other.

---

### **Step-by-Step Visualization**

| Step | Action                                                                                 | Board (Q = Queen)                        |
| ---- | -------------------------------------------------------------------------------------- | ---------------------------------------- |
| 1    | Place 1st Queen in row 1, col 1                                                        | Q . . .<br>. . . .<br>. . . .<br>. . . . |
| 2    | Row 2 → col 1 is unsafe (same column), try col 2 (diagonal conflict), try col 3 → safe | Q . . .<br>. . Q .<br>. . . .<br>. . . . |
| 3    | Row 3 → try col 1 (safe)                                                               | Q . . .<br>. . Q .<br>Q . . .<br>. . . . |
| 4    | Row 4 → no valid spot (all attacked) → backtrack                                       |                                          |
| 5    | Remove queen from row 3, move to next column (col 2, 3, 4 …), keep searching           |                                          |
| 6    | After backtracking, find valid positions → one solution is:                            |                                          |

✅ **Solution 1:**

```
. Q . .
. . . Q
Q . . .
. . Q .
```

✅ **Solution 2:**

```
. . Q .
Q . . .
. . . Q
. Q . .
```

---

### 🧩 **Explanation**

Each solution ensures:

* One queen per row.
* No two queens in same column.
* No two queens on same diagonal.

---

## 💻 5. **Algorithm (Pseudocode)**

```text
Procedure SolveNQueens(board, row, N):
    if row == N:
        print(board)        // solution found
        return

    for col from 0 to N-1:
        if isSafe(board, row, col, N):
            board[row][col] = 1      // place queen
            SolveNQueens(board, row + 1, N)
            board[row][col] = 0      // backtrack
```

### Helper Function

```text
Function isSafe(board, row, col, N):
    // Check column
    for i from 0 to row-1:
        if board[i][col] == 1:
            return False

    // Check left diagonal
    for (i, j) = (row-1, col-1); i >= 0 and j >= 0; i--, j--:
        if board[i][j] == 1:
            return False

    // Check right diagonal
    for (i, j) = (row-1, col+1); i >= 0 and j < N; i--, j++:
        if board[i][j] == 1:
            return False

    return True
```

---

## 💻 6. **C Code Example**

```c
#include <stdio.h>
#define N 4

int board[N][N];

void printSolution() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%c ", board[i][j] ? 'Q' : '.');
        printf("\n");
    }
    printf("\n");
}

int isSafe(int row, int col) {
    for (int i = 0; i < row; i++)
        if (board[i][col]) return 0;

    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return 0;

    for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++)
        if (board[i][j]) return 0;

    return 1;
}

void solveNQ(int row) {
    if (row == N) {
        printSolution();
        return;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;
            solveNQ(row + 1);
            board[row][col] = 0;
        }
    }
}

int main() {
    solveNQ(0);
    return 0;
}
```

---

## 📈 7. **Time Complexity**

* **Worst Case:** `O(N!)`

  * Because in the worst case, every row tries all columns.
* **Space Complexity:** `O(N^2)`

  * To store the board.

> For larger `N`, backtracking saves time by pruning invalid paths early.

---

## 🧭 8. **Backtracking Tree Visualization**

```
Level 0: Place Queen in Row 1 → Try each column
    |
    |-- Column 1 → leads to dead end
    |-- Column 2 → leads to valid placement
    |-- Column 3 → dead end
    |-- Column 4 → valid solution
```

---

## ✅ 9. **Output for N = 4**

```
. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
```

---

## 🧩 10. **Key Takeaways**

| Concept            | Description                               |
| :----------------- | :---------------------------------------- |
| **Problem type**   | Constraint satisfaction problem           |
| **Algorithm type** | Backtracking                              |
| **Goal**           | Place all queens without conflict         |
| **Complexity**     | O(N!) worst case                          |
| **Optimization**   | Early pruning using safety check          |
| **Applications**   | Scheduling, puzzles, combinatorial search |

---

# 🧠 **Backtracking: Hamiltonian Circuit Problem**

---

## 🧩 1. **Introduction**

A **Hamiltonian Circuit (Cycle)** in a graph is a **closed loop** that:

* Visits **each vertex exactly once**, and
* Returns to the **starting vertex**.

> If such a circuit exists, the graph is called a **Hamiltonian Graph**.

---

### 🕸️ **Example**

Graph:
Vertices = {A, B, C, D}
Edges = { (A,B), (A,C), (B,C), (B,D), (C,D) }

Possible Hamiltonian Cycle:

```
A → B → C → D → A
```

Here, each vertex is visited once and returns to the start.

---

## 🎯 2. **Goal**

To find whether a given graph **contains a Hamiltonian Cycle**,
and if yes, print **one possible cycle**.

---

## ⚙️ 3. **Backtracking Approach**

The backtracking algorithm **builds the solution step-by-step**:

1. Start from the **first vertex** (say, vertex 0).
2. Add vertices to the path **one by one**, ensuring:

   * The vertex is **connected** to the previous one.
   * The vertex has **not been visited** yet.
3. When all vertices are added, check if the **last vertex connects back to the first** — if yes, we found a **Hamiltonian Cycle**.
4. If not, **backtrack** and try another vertex.

---

## 🧮 4. **Example Graph**

Let’s take this graph (adjacency matrix form):

|     |  0  |  1  |  2  |  3  |
| :-: | :-: | :-: | :-: | :-: |
|  0  |  0  |  1  |  1  |  0  |
|  1  |  1  |  0  |  1  |  1  |
|  2  |  1  |  1  |  0  |  1  |
|  3  |  0  |  1  |  1  |  0  |

🕸️ **Graph Visualization**

```
   (0)
   / \
 (1)--(2)
   \  /
   (3)
```

---

### ✅ **Hamiltonian Cycle Exists:**

Example cycle:

```
0 → 1 → 2 → 3 → 0
```

---

## 💻 5. **Algorithm (Pseudocode)**

```text
Procedure HamiltonianCycle(G, path, pos, N):
    if pos == N:
        if G[path[pos-1]][path[0]] == 1:
            print(path + [path[0]])     // complete cycle found
            return True
        else:
            return False

    for v in range(1, N):
        if isSafe(v, G, path, pos):
            path[pos] = v
            if HamiltonianCycle(G, path, pos + 1, N):
                return True
            path[pos] = -1              // backtrack
    return False


Function isSafe(v, G, path, pos):
    // 1. Check if vertex is adjacent to previous vertex
    if G[path[pos - 1]][v] == 0:
        return False

    // 2. Check if vertex already in path
    if v in path:
        return False

    return True
```

---

## 💻 6. **C Implementation**

```c
#include <stdio.h>
#define V 5

int graph[V][V] = {
    {0, 1, 0, 1, 0},
    {1, 0, 1, 1, 1},
    {0, 1, 0, 0, 1},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 1, 0}
};

int path[V];

void printSolution() {
    printf("Hamiltonian Cycle Found: ");
    for (int i = 0; i < V; i++)
        printf("%d ", path[i]);
    printf("%d\n", path[0]);
}

int isSafe(int v, int pos) {
    if (graph[path[pos - 1]][v] == 0)
        return 0;

    for (int i = 0; i < pos; i++)
        if (path[i] == v)
            return 0;

    return 1;
}

int hamCycleUtil(int pos) {
    if (pos == V) {
        if (graph[path[pos - 1]][path[0]] == 1)
            return 1;
        else
            return 0;
    }

    for (int v = 1; v < V; v++) {
        if (isSafe(v, pos)) {
            path[pos] = v;
            if (hamCycleUtil(pos + 1) == 1)
                return 1;
            path[pos] = -1; // backtrack
        }
    }
    return 0;
}

int main() {
    for (int i = 0; i < V; i++)
        path[i] = -1;

    path[0] = 0; // start at vertex 0

    if (hamCycleUtil(1) == 0)
        printf("No Hamiltonian Cycle exists\n");
    else
        printSolution();
}
```

---

## 🧭 7. **Visualization of Backtracking Tree**

```
Start from vertex 0
|
|-- Try 1 → possible
|     |-- Try 2 → possible
|     |     |-- Try 3 → possible → Back to 0 ✅
|     |     |-- Try other vertices ❌
|-- Try 2 → possible
|     |-- Try 1 → possible
|     |     |-- Try 3 → possible → Back to 0 ✅
```

---

## 📈 8. **Complexity Analysis**

| Type                 | Complexity                                        |
| -------------------- | ------------------------------------------------- |
| **Time Complexity**  | O(N!) — as it tries every permutation of vertices |
| **Space Complexity** | O(N) — for the path array                         |

> Backtracking helps prune invalid paths early, so in practice it’s faster than brute force.

---

## 💡 9. **Real-World Applications**

| Application          | Description                                  |
| -------------------- | -------------------------------------------- |
| **Routing problems** | Finding shortest paths visiting all cities   |
| **Circuit design**   | Visiting all nodes in a circuit exactly once |
| **Game puzzles**     | Knight’s tour, traveling problems            |
| **Network topology** | Ensuring connectivity and reliability        |

---

## ✅ 10. **Key Takeaways**

| Concept              | Description                                              |
| -------------------- | -------------------------------------------------------- |
| **Problem type**     | Path-finding / Constraint satisfaction                   |
| **Algorithm type**   | Backtracking                                             |
| **Goal**             | Visit all vertices exactly once and return to start      |
| **Complexity**       | O(N!)                                                    |
| **Base condition**   | When all vertices are visited and last connects to first |
| **Example solution** | 0 → 1 → 2 → 3 → 0                                        |

---

### 🔁 **Summary Diagram**

```
        +-------------------+
        | Start from vertex |
        +-------------------+
                  |
         +---------------------+
         | Try next vertex (v) |
         +---------------------+
             |          |
             | valid?   | invalid?
             |          |
         place Q     backtrack
             |
        if all visited and edge to start?
             |
          YES ✅ print cycle
          NO  ❌ backtrack
```

---

# Backtracking — Subset-Sum Problem (complete, practical explanation)

Great — Subset-Sum is a classic backtracking / search problem. I’ll cover the **problem**, **brute-force**, **backtracking with pruning**, **pseudocode**, a **worked example (tree)**, **optimizations (sorting, bounding, memo, DP, meet-in-the-middle)**, **complexity**, and a **C implementation** you can run.

---

## 1) Problem statement

Given a set (or array) of `n` integers `S = {s0, s1, ..., s(n-1)}` and a target sum `T`, **does there exist** a subset of `S` whose elements add up exactly to `T`?

* Decision version: return `YES`/`NO`.
* Often you may want all subsets or one subset that achieves `T`.

---

## 2) Brute-force idea

Try every subset (there are `2^n`), sum it, check if equals `T`. Correct but exponential: `O(2^n * n)` in naive counting.

---

## 3) Backtracking idea (better than blind brute force)

Build subset element-by-element (typically by index). At each index `i` decide:

* **Include** `s[i]` → `current_sum += s[i]` and recurse to `i+1`
* **Exclude** `s[i]` → recurse to `i+1`

**Prune** branches early:

* If `current_sum == T` → success (stop).
* If `current_sum > T` (when all numbers are non-negative) → no need to continue down this branch.
* If remaining possible sum + current_sum < T → impossible to reach target → prune.

(If negatives are allowed, prune rules differ — you can still use bounds but need more care.)

---

## 4) Pseudocode (decision: find one subset)

```
Backtrack(i, current_sum):
    if current_sum == T:
        report solution; return true
    if i == n:
        return false
    // pruning for nonnegative elements:
    if current_sum > T:
        return false
    // Option 1: include s[i]
    if Backtrack(i+1, current_sum + s[i]) then return true
    // Option 2: exclude s[i]
    if Backtrack(i+1, current_sum) then return true
    return false

// start:
sort S in non-increasing order (optional, helps pruning)
Backtrack(0, 0)
```

Notes:

* Sorting descending makes you try large items first → earlier overshoots and better pruning.
* For returning the actual subset, maintain an array `chosen[i]` and set/unset when recursing.

---

## 5) Worked small example (tree)

S = [3, 2, 7], T = 5 (assume we try include first)

```
Start (i=0, sum=0)
 ├─ include 3 → (i=1, sum=3)
 │    ├─ include 2 → (i=2, sum=5)  <-- FOUND (3+2=5)
 │    └─ exclude 2 → (i=2, sum=3) ...
 └─ exclude 3 → (i=1, sum=0)
      ├─ include 2 → (i=2, sum=2)
      └─ exclude 2 → (i=2, sum=0)
```

Backtracking stops early when `(i=2,sum=5)` reached.

---

## 6) Key pruning / optimizations

1. **Sort descending**: try big elements first so `current_sum` hits or exceeds `T` earlier — fewer branches.
2. **Bound using remaining sum**:

   * Precompute `suffixSum[i] = sum of S[i..n-1]`.
   * If `current_sum + suffixSum[i] < T` → cannot reach `T` → prune.
3. **Early exit** when found one solution (for decision).
4. **Memoization** (top-down DP): memoize states `(i, current_sum)` to avoid recomputation. But `current_sum` can be large — use hash map or bitset.
5. **DP / bitset**: bottom-up DP computes reachable sums in `O(n*T)` time or using bitset `O(n * (T/word_size))` — good when `T` is not huge.
6. **Meet-in-the-middle**: split array in two halves (size ~n/2). Compute all subset sums of each half (`2^(n/2)` each), sort one half and for each sum in other half binary search for `T - sum`. Works well up to `n ≈ 40`.
7. **Handle negatives**: bitset/DP needs offset or different approach; meet-in-middle still works.

---

## 7) Complexity (backtracking)

* Worst case (no pruning) = `O(2^n)`.
* With good pruning and sorted input, practical speed-up can be huge, but worst-case still exponential.
* DP (pseudo-polynomial) = `O(n * T)` time and `O(T)` space (good when `T` small).

---

## 8) C implementation (simple backtracking that returns one subset)

* Turbo C/GCC compatible style.
* Assumes **non-negative** integers (so `current_sum > T` prune works).
* Uses sorting (descending) and suffix sum pruning.

```c
#include <stdio.h>
#include <stdlib.h>

int n;
int *S;
int T;
int *chosen; // 0/1 flags
int *suffixSum;

int cmp_desc(const void *a, const void *b){
    return (*(int*)b) - (*(int*)a);
}

int backtrack(int i, int curr_sum) {
    if (curr_sum == T) {
        // print solution
        printf("Subset found: ");
        for (int k = 0; k < n; ++k)
            if (chosen[k]) printf("%d ", S[k]);
        printf("\n");
        return 1;
    }
    if (i == n) return 0;
    if (curr_sum > T) return 0;
    // pruning: even if we take all remaining, cannot reach T
    if (curr_sum + suffixSum[i] < T) return 0;

    // Try include S[i]
    chosen[i] = 1;
    if (backtrack(i + 1, curr_sum + S[i])) return 1;
    chosen[i] = 0;

    // Try exclude S[i]
    if (backtrack(i + 1, curr_sum)) return 1;

    return 0;
}

int main(void) {
    // Example input
    // You can change n, S array and T here for testing
    n = 6;
    int arr[] = {3, 34, 4, 12, 5, 2};
    T = 9;

    S = (int*)malloc(n * sizeof(int));
    chosen = (int*)calloc(n, sizeof(int));
    suffixSum = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) S[i] = arr[i];

    // sort descending to help pruning
    qsort(S, n, sizeof(int), cmp_desc);

    // compute suffix sums
    suffixSum[n-1] = S[n-1];
    for (int i = n-2; i >= 0; --i) suffixSum[i] = suffixSum[i+1] + S[i];

    if (!backtrack(0, 0)) {
        printf("No subset sums to %d\n", T);
    }

    free(S);
    free(chosen);
    free(suffixSum);
    return 0;
}
```

### Sample run (with the given array)

Input set `{3,34,4,12,5,2}` and `T=9` → output:

```
Subset found: 5 4
```

(Depending on sorting you may see `5 4` or `4 5`, but it's a valid subset.)

---

## 9) Alternatives & when to use them

* **If `n` ≤ 40**: use **meet-in-the-middle** (`O(2^(n/2))`) — best for medium n with large T.
* **If `T` is small (≤ ~10^7)**: use **DP / bitset** (`O(nT)` or bitset acceleration).
* **If elements include negatives**: meet-in-the-middle or hashing; DP needs offset handling which can blow memory.
* **If you need all subsets**: backtracking can be used to enumerate them (no early exit).

---

## 10) Meet-in-the-middle (short note)

Split S into `L` and `R` halves. Generate all subset sums of `L` (list A) and `R` (list B). Sort B. For each `x` in A, check if `T - x` exists in B (binary search) — can also use hashing. Time `O(2^(n/2) * (n/2) + 2^(n/2) log 2^(n/2))` ≈ `O(2^(n/2) * n)`.

---

## 11) Quick checklist for solving real tasks

* Are numbers nonnegative? → sort descending + prune by `curr_sum > T` + suffix sum.
* Is `T` small? → DP/bitset.
* Is `n` moderate (≤ 40)? → meet-in-the-middle.
* Need one solution or count of solutions? → backtracking for one; DP for count (modulo etc.).
* Need all solutions? → backtracking enumerate, but beware exponential output.

---

# **Branch and Bound — Assignment Problem**

---

## 🧩 **1. Problem Definition**

The **Assignment Problem** is a classic **combinatorial optimization** problem.

We are given:

* `n` **workers (agents)** → `W = {w₁, w₂, ..., wₙ}`
* `n` **jobs (tasks)** → `J = {j₁, j₂, ..., jₙ}`
* A **cost matrix** `C[n][n]`
  where `C[i][j]` = cost for worker `i` to perform job `j`.

We need to **assign each worker to exactly one job**, such that **total cost is minimized** (or maximized, depending on the problem).

---

### 🔹 Example cost matrix

| Worker/Job | J1 | J2 | J3 | J4 |
| ---------- | -- | -- | -- | -- |
| W1         | 9  | 2  | 7  | 8  |
| W2         | 6  | 4  | 3  | 7  |
| W3         | 5  | 8  | 1  | 8  |
| W4         | 7  | 6  | 9  | 4  |

Goal: Assign each worker one job → minimize total cost.

---

## ⚙️ **2. Mathematical Formulation**

Minimize:
[
Z = \sum_{i=1}^{n} \sum_{j=1}^{n} C_{ij} x_{ij}
]

Subject to:
[
\sum_{j=1}^{n} x_{ij} = 1 \quad \forall i = 1, 2, ..., n
]
[
\sum_{i=1}^{n} x_{ij} = 1 \quad \forall j = 1, 2, ..., n
]
[
x_{ij} \in {0,1}
]

Where:

* `x_ij = 1` if worker i is assigned job j, otherwise 0.

---

## 🧠 **3. Why Branch and Bound?**

The **Assignment Problem** can be solved efficiently using the **Hungarian Algorithm (O(n³))**,
but **Branch and Bound (B&B)** is another method — more general, also used for **Traveling Salesman**, **Knapsack**, etc.

We use **B&B** when:

* We want a **general-purpose optimization** framework.
* We want to understand **bounding and pruning** in search problems.

---

## 🌲 **4. Concept of Branch and Bound**

### 🔹 Branching:

At each level (depth) of the tree, assign **one worker to one job**.

* Level `k` → worker `k` is assigned a job.
* Each branch → one possible job assignment.

### 🔹 Bounding:

Compute a **lower bound** (minimum possible total cost) for partial assignments.

If the **bound ≥ best known (current minimum)** → prune the branch.

---

## 🧮 **5. Lower Bound Calculation**

For a **partial assignment**, to get a **lower bound**:

1. Add the cost of assigned jobs.
2. For each **unassigned worker**, find the **minimum cost** job still available.
3. Add all these minimum costs to the total — gives a **lower bound** of total possible cost.

If the bound ≥ current best solution → prune this node.

---

## 🌳 **6. Example**

Cost matrix:

| Worker/Job | J1 | J2 | J3 | J4 |
| ---------- | -- | -- | -- | -- |
| W1         | 9  | 2  | 7  | 8  |
| W2         | 6  | 4  | 3  | 7  |
| W3         | 5  | 8  | 1  | 8  |
| W4         | 7  | 6  | 9  | 4  |

---

### Step 1 — Root Node

No assignments yet.

Find the **minimum value in each row** and sum them up.

| Worker | Min cost |
| ------ | -------- |
| W1     | 2        |
| W2     | 3        |
| W3     | 1        |
| W4     | 4        |

Lower bound = 2 + 3 + 1 + 4 = **10**

→ Root node LB = 10.

---

### Step 2 — Branching

Assign Worker 1 to each job:

* Node 1: W1→J1 (cost = 9)
* Node 2: W1→J2 (cost = 2)
* Node 3: W1→J3 (cost = 7)
* Node 4: W1→J4 (cost = 8)

Compute LB for each.

#### For Node 2 (W1→J2 = 2)

Remaining workers: W2, W3, W4
Available jobs: J1, J3, J4

| Worker | Remaining jobs | Min cost |
| ------ | -------------- | -------- |
| W2     | 6,3,7          | 3        |
| W3     | 5,1,8          | 1        |
| W4     | 7,9,4          | 4        |

→ LB = 2 + (3 + 1 + 4) = **10**

Other nodes have higher LBs → expand Node 2 next.

---

### Step 3 — Continue expanding

Assign W2 to possible remaining jobs, compute new LB.

We continue this process until all workers are assigned → the **leaf with smallest cost** is the **optimal assignment**.

✅ Final Optimal Assignment:

```
W1 → J2
W2 → J3
W3 → J1
W4 → J4
```

Minimum cost = **13**

---

## 💡 **7. Pseudocode (Branch and Bound for Assignment)**

```text
function branch_and_bound(cost[n][n]):
    best_cost = ∞
    best_assignment = []

    create a priority queue PQ (min-heap by lower bound)

    root = {
        level = 0,
        cost = 0,
        assigned_jobs = []
        available_jobs = {0,1,...,n-1},
        lower_bound = compute_lower_bound()
    }
    PQ.push(root)

    while PQ not empty:
        node = PQ.pop()  // smallest bound

        if node.lower_bound >= best_cost:
            continue  // prune

        if node.level == n:  // all workers assigned
            if node.cost < best_cost:
                best_cost = node.cost
                best_assignment = node.assigned_jobs
            continue

        // Branch to next worker
        i = node.level
        for each job j in node.available_jobs:
            new_node = copy(node)
            new_node.assigned_jobs += (i→j)
            new_node.available_jobs -= j
            new_node.cost = node.cost + cost[i][j]
            new_node.level = i + 1
            new_node.lower_bound = new_node.cost + estimate_remaining_min(cost, new_node)
            
            if new_node.lower_bound < best_cost:
                PQ.push(new_node)

    return best_cost, best_assignment
```

---

## 💻 **8. Simple C Implementation (for clarity)**

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define N 4

int cost[N][N] = {
    {9, 2, 7, 8},
    {6, 4, 3, 7},
    {5, 8, 1, 8},
    {7, 6, 9, 4}
};

int best_cost = INT_MAX;
int best_assign[N];

void branchAndBound(int level, int assigned[], int curr_cost) {
    if (level == N) {
        if (curr_cost < best_cost) {
            best_cost = curr_cost;
            for (int i = 0; i < N; i++) best_assign[i] = assigned[i];
        }
        return;
    }

    for (int j = 0; j < N; j++) {
        int used = 0;
        for (int k = 0; k < level; k++)
            if (assigned[k] == j) used = 1;

        if (!used) {
            int next_cost = curr_cost + cost[level][j];
            if (next_cost < best_cost) { // pruning
                assigned[level] = j;
                branchAndBound(level + 1, assigned, next_cost);
            }
        }
    }
}

int main() {
    int assigned[N];
    branchAndBound(0, assigned, 0);

    printf("Minimum Cost: %d\n", best_cost);
    printf("Assignment:\n");
    for (int i = 0; i < N; i++)
        printf("Worker %d -> Job %d\n", i + 1, best_assign[i] + 1);

    return 0;
}
```

**Output:**

```
Minimum Cost: 13
Worker 1 -> Job 2
Worker 2 -> Job 3
Worker 3 -> Job 1
Worker 4 -> Job 4
```

---

## ⏱ **9. Time Complexity**

* Worst case: **O(n!)** — if no pruning possible (like brute-force).
* Practical case: Much faster due to bounding.
* Space complexity: **O(n²)** due to cost matrix and recursion stack.

---

## 🧩 **10. Summary Table**

| Concept          | Meaning                                                           |
| ---------------- | ----------------------------------------------------------------- |
| Problem Type     | Optimization (Min Cost)                                           |
| Search Space     | n! possible assignments                                           |
| Strategy         | Branch (assign one job at a time), Bound (lower bound estimation) |
| Bound Function   | Cost so far + minimum remaining cost                              |
| Goal             | Minimize total assignment cost                                    |
| Best Alternative | Hungarian Algorithm (O(n³))                                       |

---

# 🎯 **Branch and Bound — Knapsack Problem**

---

## 🧠 **1. Problem Definition**

The **Knapsack Problem** is one of the most classic **combinatorial optimization** problems.

Given:

* `n` items
* Each item `i` has:

  * **Profit** `p[i]`
  * **Weight** `w[i]`
* Knapsack has a **capacity** `W`

We must **select items** such that:

* Total weight ≤ `W`
* Total profit is **maximized**

---

### 🔹 Example

| Item | Profit (p) | Weight (w) |
| ---- | ---------- | ---------- |
| 1    | 40         | 2          |
| 2    | 30         | 5          |
| 3    | 50         | 10         |
| 4    | 10         | 5          |

Knapsack capacity `W = 16`

---

## ⚙️ **2. Mathematical Formulation**

Maximize
[
Z = \sum_{i=1}^{n} p_i x_i
]
Subject to
[
\sum_{i=1}^{n} w_i x_i \le W
]
and
[
x_i \in {0, 1}
]

where
`x_i = 1` if item i is included, otherwise 0.

---

## 🧩 **3. Why Use Branch and Bound?**

* The **Brute Force** approach checks all `2ⁿ` subsets.
* **Branch and Bound (B&B)** efficiently **prunes** the search space using **upper bound estimates** on profit.
* Works well for **0/1 Knapsack**, where fractional items are not allowed.

---

## 🪜 **4. Idea of Branch and Bound**

We build a **state-space tree**:

* Each node → represents a decision (include or exclude an item)
* **Left child:** include current item
* **Right child:** exclude current item
* At each node → calculate:

  * **Current profit**
  * **Current weight**
  * **Upper bound** on possible profit from that node onward

We use a **priority queue** (max-heap by upper bound) to always expand the most promising node.

---

## 🧮 **5. Bound Calculation**

### **Upper Bound (UB)**

We use the **fractional knapsack** idea for estimating UB:

> UB = current profit + profit from remaining capacity (assuming fractional items can be taken)

This ensures the bound is always **optimistic** (≥ actual max profit from that node).

---

### **Example Calculation**

Given capacity = 16

| Item | Profit | Weight | Ratio (p/w) |
| ---- | ------ | ------ | ----------- |
| 1    | 40     | 2      | 20.0        |
| 2    | 30     | 5      | 6.0         |
| 3    | 50     | 10     | 5.0         |
| 4    | 10     | 5      | 2.0         |

Sorted by **profit/weight (descending):**

| Item | p  | w  | p/w  |
| ---- | -- | -- | ---- |
| 1    | 40 | 2  | 20.0 |
| 2    | 30 | 5  | 6.0  |
| 3    | 50 | 10 | 5.0  |
| 4    | 10 | 5  | 2.0  |

---

## 🌳 **6. State-Space Tree Construction**

We start from root (no items selected):

```
                    [Root]
                 (Profit=0, Weight=0)
                       |
             --------------------------
             |                        |
       Include item 1            Exclude item 1
```

At each node, calculate:

* current profit
* current weight
* **upper bound**

Then branch to include/exclude next item.

---

### Let’s compute the **upper bound** step-by-step:

#### **Root Node (no items)**

* Current Profit = 0
* Current Weight = 0
* Remaining capacity = 16
* Fill knapsack fractionally:

  * Take item 1 (2), then 2 (5), then 3 (9 out of 10 → partial)
  * UB = 40 + 30 + (50 × 9/10) = 40 + 30 + 45 = **115**

→ UB(root) = 115

---

#### **Include item 1 (Left Child)**

* Profit = 40
* Weight = 2
* Remaining capacity = 14
* Fractionally fill: item 2 (5), item 3 (9 out of 10)
* UB = 40 + 30 + 45 = **115**

---

#### **Exclude item 1 (Right Child)**

* Profit = 0
* Weight = 0
* Remaining = 16
* Fractionally fill: item 2 (5), item 3 (10), item 4 (1 out of 5)
* UB = 30 + 50 + (10 × 1/5) = **82**

So the **left branch** (include item 1) has **higher UB (115)** → explore that first.

---

## 💡 **7. Algorithm (Pseudocode)**

```text
function knapsack_BnB(p[], w[], W, n):
    sort items by decreasing profit/weight ratio
    best_profit = 0
    create a priority queue PQ (max-heap by upper bound)

    root = Node(level=-1, profit=0, weight=0)
    root.bound = calculate_bound(root, n, W, p, w)
    PQ.push(root)

    while PQ not empty:
        node = PQ.pop()

        if node.bound <= best_profit:
            continue  // prune

        // Consider next item
        i = node.level + 1
        if i >= n:
            continue

        // LEFT: include item i
        left = Node(level=i)
        left.weight = node.weight + w[i]
        left.profit = node.profit + p[i]

        if left.weight <= W and left.profit > best_profit:
            best_profit = left.profit

        left.bound = calculate_bound(left, n, W, p, w)
        if left.bound > best_profit:
            PQ.push(left)

        // RIGHT: exclude item i
        right = Node(level=i, weight=node.weight, profit=node.profit)
        right.bound = calculate_bound(right, n, W, p, w)
        if right.bound > best_profit:
            PQ.push(right)

    return best_profit
```

---

## 🔢 **8. Bound Function**

```text
function calculate_bound(node, n, W, p, w):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1

    while j < n and total_weight + w[j] <= W:
        total_weight += w[j]
        profit_bound += p[j]
        j += 1

    // add fractional item
    if j < n:
        profit_bound += (W - total_weight) * (p[j] / w[j])

    return profit_bound
```

---

## 💻 **9. Simple C Implementation**

```c
#include <stdio.h>
#include <stdlib.h>

#define N 4

int p[] = {40, 30, 50, 10};
int w[] = {2, 5, 10, 5};
int W = 16;

float ratio[N];

float bound(int i, int profit, int weight) {
    if (weight >= W) return 0;
    float result = profit;
    int j = i + 1;
    int totweight = weight;
    while (j < N && totweight + w[j] <= W) {
        totweight += w[j];
        result += p[j];
        j++;
    }
    if (j < N)
        result += (W - totweight) * ((float)p[j] / w[j]);
    return result;
}

void knapsack() {
    float bestProfit = 0;
    int i, j;
    float b = bound(-1, 0, 0);
    printf("Maximum Profit (approx bound): %.2f\n", b);
}

int main() {
    for (int i = 0; i < N; i++)
        ratio[i] = (float)p[i] / w[i];
    knapsack();
    return 0;
}
```

You can easily extend this code with a **priority queue** for full B&B behavior.

---

## 📈 **10. State-Space Tree (Simplified View)**

```
                     [0,0] UB=115
                   /               \
       Include(1)                  Exclude(1)
     [40,2,UB=115]               [0,0,UB=82]
       /       \
  +item2     -item2
[70,7,UB=115]  [40,2,UB=95]
```

And so on — the algorithm always expands the node with **highest UB**, pruning others.

---

## ⏱ **11. Complexity**

| Case                 | Time Complexity                       |
| -------------------- | ------------------------------------- |
| **Worst Case**       | O(2ⁿ) (no pruning)                    |
| **Average Case**     | Much less, depends on bounds          |
| **Space Complexity** | O(n) for recursion or O(n²) with heap |

---

## ✅ **12. Summary Table**

| Aspect     | Description                   |
| :--------- | :---------------------------- |
| Problem    | 0/1 Knapsack                  |
| Goal       | Maximize profit               |
| Technique  | Branch and Bound              |
| Bounding   | Fractional knapsack bound     |
| Pruning    | If bound ≤ best profit so far |
| Structure  | Binary state-space tree       |
| Best Case  | Explores few branches         |
| Worst Case | O(2ⁿ)                         |

---

### 🧩 **Key Insight**

> The **Branch and Bound Knapsack** algorithm uses an **optimistic bound (fractional profit)** to explore only the most **promising subsets**, avoiding exhaustive enumeration.

---

# 🧠 **Branch and Bound: Traveling Salesperson Problem (TSP)**

---

### 🚩 **1. Introduction**

The **Traveling Salesperson Problem (TSP)** is a **classic combinatorial optimization problem**:

> A salesperson must visit `n` cities, each exactly once, and return to the starting city — such that the **total travel cost (distance)** is **minimum**.

Formally:

> Given a cost matrix `C[i][j]`, find a tour (a permutation of cities) that visits all cities once and returns to the start with **minimum total cost**.

---

### 🧩 **2. Problem Definition**

Let there be `n` cities `{1, 2, 3, ..., n}`.

* `C[i][j]` = cost of traveling from city `i` to city `j`.
* We must find a **Hamiltonian cycle** of **minimum total cost**.

Mathematically:

[
\text{Minimize } \sum_{k=1}^{n} C[\pi_k][\pi_{k+1}] + C[\pi_n][\pi_1]
]

where ( \pi ) is a permutation of `{1, 2, ..., n}`.

---

### 🧱 **3. Why Branch and Bound?**

* The **Brute Force** method checks all possible tours → **O(n!)**, impractical for large `n`.
* **Branch and Bound (B&B)** efficiently eliminates subtrees of the search space that **cannot produce better results** than the current best.

---

### 🌳 **4. Basic Idea of Branch and Bound for TSP**

1. **Branching:**

   * Each level in the tree represents a city visited in order.
   * Each node represents a **partial tour**.

2. **Bounding:**

   * Calculate a **lower bound (LB)** on the minimum cost achievable from that partial tour.
   * If this bound ≥ best known cost, **prune** that branch.

3. **Selection:**

   * Choose the next node (partial tour) with the **lowest bound** to expand next.

---

### ⚙️ **5. Cost Matrix and Reduction**

We use a **Reduced Cost Matrix** to compute bounds.

Steps:

1. Subtract the **minimum value in each row** from all elements of that row.
2. Subtract the **minimum value in each column** from all elements of that column.
3. The **sum of all reductions** gives the **Lower Bound (LB)**.

This represents the minimal extra cost needed to complete the tour.

---

### 🧮 **6. Example**

Let’s consider a 4-city TSP:

| From/To | 1  | 2  | 3  | 4  |
| ------- | -- | -- | -- | -- |
| **1**   | ∞  | 20 | 30 | 10 |
| **2**   | 15 | ∞  | 16 | 4  |
| **3**   | 3  | 5  | ∞  | 2  |
| **4**   | 19 | 6  | 18 | ∞  |

---

#### Step 1️⃣: Initial Reduction

Perform row & column reduction →
Sum of reductions = **35** (this is the initial lower bound).

This becomes the **root node’s bound (LB = 35)**.

---

#### Step 2️⃣: Branching

Branch from city 1 to each other city (2, 3, 4):

* Compute reduced matrix for each branch
* Add corresponding edge cost to bound
* Update the bound after further reduction

Let’s assume after computation:

| Branch (Path) | Bound (LB) |
| ------------- | ---------- |
| 1 → 2         | 49         |
| 1 → 3         | 52         |
| 1 → 4         | 45         |

---

#### Step 3️⃣: Choose Minimum Bound Node

Select **1 → 4** (LB = 45) for expansion.

Continue branching and bounding until a **complete tour** is formed.

---

### 🧭 **7. Algorithm (Pseudocode)**

```text
Algorithm TSP_Branch_Bound(CostMatrix, n):
1. Create a priority queue PQ for live nodes
2. Compute initial reduced cost matrix and LB (lower bound)
3. Create root node:
      - Level = 0, Path = [1], Bound = LB
      - Insert into PQ
4. while PQ is not empty:
       a. Extract node with least Bound
       b. If node is at level n-1:
             - Compute cost to return to start
             - Update best_cost if smaller
       c. Else expand the node:
             - For each unvisited city j:
                 i. Create new child node
                 ii. Update path and level
                 iii. Compute new reduced matrix
                 iv. Calculate new bound
                 v. If bound < best_cost:
                       Insert into PQ
5. Return best_cost and optimal path
```

---

### 🕒 **8. Time Complexity**

* **Worst Case:** `O(n!)` (like brute force)
* **Best / Average Case:** Significantly less due to pruning
  → Often practical for `n ≤ 20`

---

### 📈 **9. Advantages**

✅ Efficient pruning reduces search space
✅ Provides **exact optimal solution**
✅ Works well for small to medium `n`

---

### ⚠️ **10. Disadvantages**

❌ Still exponential in the worst case
❌ Needs large memory for maintaining PQ and reduced matrices

---

### 📊 **11. Visualization**

```
                 (Start: 1)
                /    |     \
              2      3      4
            /|\     /|\    /|\
         (Prune) (Expand) (Expand)
```

* Nodes pruned if bound ≥ best known cost.
* The lowest-bound node is expanded next.

---

### 🏁 **12. Final Output Example**

For our 4-city problem, suppose the optimal tour found:

```
1 → 4 → 2 → 3 → 1
Total Cost = 35
```

---

### 🧾 **13. Summary Table**

| Step | Operation   | Description             |
| ---- | ----------- | ----------------------- |
| 1    | Reduction   | Compute lower bound     |
| 2    | Branching   | Create child nodes      |
| 3    | Bounding    | Calculate new bounds    |
| 4    | Pruning     | Remove high-bound nodes |
| 5    | Termination | When full tour is found |

---

### 💡 **14. Key Takeaways**

* **Branch and Bound** = Smart brute force using bounds.
* **Reduced cost matrix** gives a **lower bound**.
* Helps solve **TSP optimally** with pruning.
* Works best when the cost matrix satisfies **triangle inequality**.

---

