# Mathamatics  

---
# Unit -I  
### Set Theory, Relation and Functions  
- Introduction, Basic concepts of sets, and its types, Operations on sets, Venn diagrams, Some basic set identities, Cardinal number and its problems. Cartesian products , Relations, Properties of relations, Equivalence relation, Relation matrix and the Graph of binary relation, Partition set, POSET. Hasse Diagram. Functions and its types, Composition of a functions and Inverse functions, Recursive function.  
---

## 📘 **Introduction to Set Theory**

### 🔹 What is Set Theory?

Set Theory is a **branch of mathematical logic** that deals with the study of sets, which are **collections of objects**. These objects can be **numbers, letters, symbols, or anything** that is clearly defined and distinct.

Set theory provides a **foundation for most of mathematics**, especially for data handling, logic, computer science, and functions.

---

### 🔹 Historical Note
- Set theory was **introduced by Georg Cantor** in the late 19th century.
- It forms the basis for many **mathematical structures** like relations, functions, graphs, etc.

---

### 🔹 Importance in Computer Applications:
- Helps in **database theory** (like queries using union, intersection).
- Basis for **logic circuits** and **Boolean algebra**.
- Essential in **data structures** like sets, maps, hash tables.
- Used in **software testing, AI, automata theory**, and more.

---

### 🔹 Basic Terminology:
- **Element / Member**: An object in the set.
- **Set**: A collection of elements, written in curly brackets `{}`.
  - Example: A = {1, 2, 3}

---

### 🔹 Summary:
| Term        | Meaning                     |
|-------------|-----------------------------|
| Set         | Collection of distinct items |
| Element     | An item in the set           |
| Set Theory  | Study of sets and operations |

---

## 📘 **Basic Concepts of Sets and Its Types**

---

### 🔹 What is a Set?

A **set** is a collection of **well-defined, distinct objects**, considered as a single entity.

Examples:
- A = {2, 4, 6, 8}
- B = {x | x is a vowel in the English alphabet}

> The objects inside a set are called **elements** or **members** of the set.

---

### 🔹 Notation and Representation of Sets

1. **Roster/Tabular Form**  
   All elements are listed inside curly brackets:  
   A = {1, 2, 3, 4}

2. **Set Builder Form**  
   Describes elements with a property:  
   B = {x | x is a natural number less than 5}  
   ⇒ B = {1, 2, 3, 4}

---

### 🔹 Membership

- If `a` is an element of set A: `a ∈ A`
- If `b` is not an element of A: `b ∉ A`

---

### 🔹 Types of Sets

| Type of Set        | Definition                                                                 | Example                              |
|--------------------|---------------------------------------------------------------------------|--------------------------------------|
| **Finite Set**      | Set with a **countable** number of elements                               | A = {1, 2, 3}                         |
| **Infinite Set**    | Set with **uncountable** elements                                          | N = {1, 2, 3, …}                      |
| **Empty/Null Set**  | Set with **no elements**, denoted as **Ø** or `{}`                        | B = {x | x < 0, x ∈ Natural numbers} |
| **Singleton Set**   | A set with **exactly one element**                                        | A = {0}                              |
| **Equal Sets**      | Two sets with **exactly the same elements**                              | A = {1, 2}, B = {2, 1} ⇒ A = B        |
| **Subset**          | If all elements of A are in B: `A ⊆ B`                                    | A = {1, 2}, B = {1, 2, 3}             |
| **Proper Subset**   | A subset that is **not equal** to the original set: `A ⊂ B`               | {1, 2} ⊂ {1, 2, 3}                    |
| **Universal Set**   | A set containing **all elements under consideration**, denoted `U`        | U = {1, 2, 3, 4, 5}                   |
| **Disjoint Sets**   | Two sets with **no common elements** ⇒ A ∩ B = Ø                          | A = {1, 2}, B = {3, 4}                |
| **Power Set**       | Set of **all subsets** of a set A, denoted as **P(A)**                    | A = {a, b} ⇒ P(A) = {Ø, {a}, {b}, {a, b}} |
| **Complement Set**  | Elements in U but **not** in A, denoted A′ or Aᶜ                          | U = {1,2,3,4}, A = {1,2} ⇒ Aᶜ = {3,4} |

---

🧠 **Quick Facts**:
- If set A has **n elements**, then Power set P(A) has **2ⁿ elements**
- Every set is a **subset** of itself
- Ø is a subset of **every set**

---
## Operations on Sets

---

### 🔹 Union (A ∪ B)

All elements that are in A or in B or in both.

**Formula**:  
A ∪ B = {x | x ∈ A or x ∈ B}

**Example**:  
A = {1, 2, 3}, B = {3, 4, 5}  
A ∪ B = {1, 2, 3, 4, 5}

---

### 🔹 Intersection (A ∩ B)

All elements common to both sets.

**Formula**:  
A ∩ B = {x | x ∈ A and x ∈ B}

**Example**:  
A = {1, 2, 3}, B = {3, 4, 5}  
A ∩ B = {3}

---

### 🔹 Difference (A – B)

Elements in A but not in B.

**Formula**:  
A – B = {x | x ∈ A and x ∉ B}

**Example**:  
A = {1, 2, 3}, B = {3, 4}  
A – B = {1, 2}

---

### 🔹 Symmetric Difference (A Δ B)

Elements in either A or B but not both.

**Formula**:  
A Δ B = (A – B) ∪ (B – A)

**Example**:  
A = {1, 2, 3}, B = {3, 4, 5}  
A Δ B = {1, 2, 4, 5}

---

### 🔹 Complement (Aᶜ)

Elements in the universal set U that are not in A.

**Formula**:  
Aᶜ = U – A

**Example**:  
U = {1, 2, 3, 4, 5}, A = {2, 3}  
Aᶜ = {1, 4, 5}

---

### 🔹 Cartesian Product (A × B)

Set of all **ordered pairs (a, b)** where `a ∈ A` and `b ∈ B`.

**Formula**:  
A × B = {(a, b) | a ∈ A, b ∈ B}

**Example**:  
A = {1, 2}, B = {x, y}  
A × B = {(1, x), (1, y), (2, x), (2, y)}

---

### Properties

| Property                | Formula                          |
|-------------------------|----------------------------------|
| Commutative Law (Union) | A ∪ B = B ∪ A                    |
| Commutative Law (Int.)  | A ∩ B = B ∩ A                    |
| Associative (Union)     | A ∪ (B ∪ C) = (A ∪ B) ∪ C        |
| Associative (Int.)      | A ∩ (B ∩ C) = (A ∩ B) ∩ C        |
| Distributive            | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)  |
|                         | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)  |

---
## Venn Diagrams

---

### 🔹 What is a Venn Diagram?

A **Venn Diagram** is a pictorial representation of sets using circles to show the relationships between different sets.

---

### 🔹 Notations in Venn Diagram

| Notation     | Meaning                             |
|--------------|-------------------------------------|
| A ∪ B        | Union of sets A and B               |
| A ∩ B        | Intersection of sets A and B        |
| A - B        | Elements in A but not in B          |
| Aᶜ           | Complement of set A                 |
| U            | Universal set (everything in the context) |

---

### 🔹 Venn Diagram of Two Sets

Let A = Students who play Cricket  
Let B = Students who play Football

- **A ∪ B**: All students who play either Cricket or Football or both  
- **A ∩ B**: Students who play both Cricket and Football  
- **A - B**: Students who play only Cricket  
- **B - A**: Students who play only Football  
- **(A ∪ B)ᶜ**: Students who play neither Cricket nor Football

---

### 🔹 Example

Let  
- U = {1, 2, 3, 4, 5, 6, 7, 8}  
- A = {1, 2, 3, 4}  
- B = {3, 4, 5, 6}

Then:  
- A ∪ B = {1, 2, 3, 4, 5, 6}  
- A ∩ B = {3, 4}  
- A - B = {1, 2}  
- B - A = {5, 6}  
- Aᶜ = {5, 6, 7, 8}  
- Bᶜ = {1, 2, 7, 8}

---

### 🔹 Uses of Venn Diagrams

- To verify set identities visually  
- To solve problems in probability, logic, and algebra  
- Useful in competitive exams for reasoning and aptitude  

---
## Some Basic Set Identities (with Examples)

---

### 🔹 Identity Laws
- **A ∪ ∅ = A**  
- **A ∩ U = A**

**Example:**
Let A = {1, 2, 3}, U = {1, 2, 3, 4, 5}, ∅ = {}  
Then:  
A ∪ ∅ = {1, 2, 3}  
A ∩ U = {1, 2, 3}

---

### 🔹 Domination Laws
- **A ∪ U = U**  
- **A ∩ ∅ = ∅**

**Example:**
A = {2, 4}, U = {1, 2, 3, 4, 5}  
A ∪ U = {1, 2, 3, 4, 5} = U  
A ∩ ∅ = ∅

---

### 🔹 Idempotent Laws
- **A ∪ A = A**  
- **A ∩ A = A**

**Example:**
A = {5, 6, 7}  
A ∪ A = {5, 6, 7}  
A ∩ A = {5, 6, 7}

---

### 🔹 Complement Laws
- **A ∪ Aᶜ = U**  
- **A ∩ Aᶜ = ∅**

**Example:**
A = {1, 2}, U = {1, 2, 3, 4} ⇒ Aᶜ = {3, 4}  
A ∪ Aᶜ = {1, 2, 3, 4} = U  
A ∩ Aᶜ = ∅

---

### 🔹 Commutative Laws
- **A ∪ B = B ∪ A**  
- **A ∩ B = B ∩ A**

**Example:**
A = {1, 2}, B = {2, 3}  
A ∪ B = {1, 2, 3} = B ∪ A  
A ∩ B = {2} = B ∩ A

---

### 🔹 Associative Laws
- **A ∪ (B ∪ C) = (A ∪ B) ∪ C**  
- **A ∩ (B ∩ C) = (A ∩ B) ∩ C**

**Example:**
A = {1}, B = {1, 2}, C = {1, 3}  
Left side: A ∪ (B ∪ C) = {1} ∪ {1, 2, 3} = {1, 2, 3}  
Right side: (A ∪ B) ∪ C = {1, 2} ∪ {1, 3} = {1, 2, 3}

---

### 🔹 Distributive Laws
- **A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)**  
- **A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)**

**Example:**
A = {1, 2}, B = {2, 3}, C = {2, 4}  
B ∩ C = {2}, A ∪ {2} = {1, 2}  
A ∪ B = {1, 2, 3}, A ∪ C = {1, 2, 4}  
(A ∪ B) ∩ (A ∪ C) = {1, 2}

So:  
A ∪ (B ∩ C) = {1, 2}  
(A ∪ B) ∩ (A ∪ C) = {1, 2}

---

### 🔹 De Morgan’s Laws
- **(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ**  
- **(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ**

**Example:**
U = {1, 2, 3, 4}, A = {1, 2}, B = {2, 3}  
A ∪ B = {1, 2, 3}, ⇒ (A ∪ B)ᶜ = {4}  
Aᶜ = {3, 4}, Bᶜ = {1, 4} ⇒ Aᶜ ∩ Bᶜ = {4} ✅

---
## Cardinal Number and Its Problems (with Examples)

---

### 🔹 Cardinal Number

The **cardinal number** (or cardinality) of a set is the number of distinct elements in the set.

- **Notation:** If A is a set, then its cardinal number is denoted by **n(A)**.
- For a finite set, cardinality is simply the count of elements.

**Example 1:**
Let A = {2, 4, 6, 8}, then  
n(A) = 4 ✅

---

### 🔹 Inclusion-Exclusion Principle

For **two finite sets A and B**, the total number of elements in their union is:  
**n(A ∪ B) = n(A) + n(B) – n(A ∩ B)**

#### ✅ Example 2:
Let:  
- A = students who like Python → n(A) = 25  
- B = students who like Java → n(B) = 20  
- Students who like both → n(A ∩ B) = 5

Then:  
**n(A ∪ B) = 25 + 20 – 5 = 40**  
✅ So, 40 students like either Python or Java or both.

---

### 🔹 For Three Sets

**n(A ∪ B ∪ C) = n(A) + n(B) + n(C) – n(A ∩ B) – n(B ∩ C) – n(C ∩ A) + n(A ∩ B ∩ C)**

#### ✅ Example 3:
Let:  
- A = Students who know C, n(A) = 15  
- B = Students who know C++, n(B) = 10  
- C = Students who know Java, n(C) = 12  
- n(A ∩ B) = 5, n(B ∩ C) = 4, n(C ∩ A) = 3, n(A ∩ B ∩ C) = 2

Then:  
n(A ∪ B ∪ C) = 15 + 10 + 12 – 5 – 4 – 3 + 2  
= 37 – 12 + 2 = **27**

✅ So, 27 students know at least one of the three languages.

---

### 🔹 Venn Diagram Use (for Visualization)

In competitive or final exams, these types of problems are best solved using **Venn diagrams** to avoid over-counting.

---
## Cartesian Products, Relations, and Properties of Relations (with Examples)

---

### 🔹 Cartesian Product

Given two sets A and B, their **Cartesian product** is the set of all ordered pairs (a, b) such that a ∈ A and b ∈ B.  
- **Notation:** A × B = {(a, b) | a ∈ A, b ∈ B}

#### ✅ Example 1:  
Let A = {1, 2}, B = {x, y}  
Then A × B = {(1, x), (1, y), (2, x), (2, y)}  
⇒ n(A × B) = 2 × 2 = 4 elements ✅

---

### 🔹 Relation

A **relation** R from set A to set B is a **subset of the Cartesian product** A × B.

- A relation **on a set A** is a subset of A × A.

#### ✅ Example 2:  
Let A = {1, 2, 3}, and define R = {(1, 2), (2, 3)}  
Then R is a relation from A to A.

---

### 🔹 Properties of Relations

Let R be a relation on set A. R may have these properties:

1. **Reflexive:** (a, a) ∈ R for all a ∈ A  
2. **Symmetric:** If (a, b) ∈ R, then (b, a) ∈ R  
3. **Transitive:** If (a, b) ∈ R and (b, c) ∈ R ⇒ (a, c) ∈ R  
4. **Antisymmetric:** If (a, b) ∈ R and (b, a) ∈ R ⇒ a = b

---

#### ✅ Example 3:  
Let A = {1, 2, 3}, and R = {(1, 1), (2, 2), (3, 3)}  
Check properties:  
- Reflexive ✅ (all (a, a) are present)  
- Symmetric ✅ (since no (a, b) with a ≠ b)  
- Transitive ✅ (no chain to break transitivity)

So, R is **Reflexive, Symmetric, and Transitive** ⇒ it's an **Equivalence Relation**.

---

#### ✅ Example 4:  
Let A = {1, 2, 3}, and R = {(1, 2), (2, 3), (1, 3)}  
- Not reflexive ❌  
- Not symmetric ❌ (since (2, 1) not present)  
- Transitive ✅ because (1, 2), (2, 3) ⇒ (1, 3) present

---
## Equivalence Relation, Relation Matrix, and Graph of a Binary Relation (with Examples)

---

### 🔹 Equivalence Relation

A **relation R on set A** is called an **equivalence relation** if it satisfies:

1. **Reflexive:** ∀a ∈ A, (a, a) ∈ R  
2. **Symmetric:** ∀a, b ∈ A, (a, b) ∈ R ⇒ (b, a) ∈ R  
3. **Transitive:** ∀a, b, c ∈ A, (a, b) ∈ R ∧ (b, c) ∈ R ⇒ (a, c) ∈ R

Such a relation groups the set into **equivalence classes**.

---

#### ✅ Example 1:  
Let A = {1, 2, 3} and define R = {(1, 1), (2, 2), (3, 3)}  
- Reflexive: Yes  
- Symmetric: Yes  
- Transitive: Yes  
⇒ R is an equivalence relation.

---

#### ✅ Example 2:  
Let A = ℤ (integers), and R = {(a, b) | a ≡ b mod 3}  
This means a and b leave same remainder when divided by 3.

Let’s check:
- Reflexive: a ≡ a mod 3 ⇒ true  
- Symmetric: If a ≡ b ⇒ b ≡ a  
- Transitive: If a ≡ b and b ≡ c ⇒ a ≡ c

✅ So, it’s an **equivalence relation**, and the equivalence classes are:  
…{-6, -3, 0, 3, 6}, {-5, -2, 1, 4, 7}, {-4, -1, 2, 5, 8}…

---

### 🔹 Relation Matrix (Adjacency Matrix)

Let A = {a₁, a₂, ..., aₙ}, and R be a relation on A. Then the **relation matrix** M(R) is an n×n matrix where:  
- M[i][j] = 1 if (aᵢ, aⱼ) ∈ R  
- M[i][j] = 0 otherwise

---

#### ✅ Example 3:  
Let A = {1, 2, 3}, and R = {(1, 2), (2, 3), (3, 1)}

Then matrix:

```
     1 2 3
   --------
1 | 0 1 0
2 | 0 0 1
3 | 1 0 0
```

---

### 🔹 Graph of a Binary Relation

Each element of the set becomes a **node**, and for every (a, b) ∈ R, draw a **directed edge** from a → b.

---

#### ✅ Example 4:  
Same set A = {1, 2, 3}, R = {(1, 2), (2, 3), (3, 1)}

Graph:
```
1 → 2  
2 → 3  
3 → 1  
```

This forms a **cycle**. Binary relation graphs are often used to visualize relation properties like **reflexivity (self-loops), symmetry (bidirectional edges), and transitivity (path existence)**.

---
## Partition Set, POSET, and Hasse Diagram (with Examples)

---

### 🔹 Partition of a Set

A **partition** of a set A is a collection of **non-empty, disjoint subsets** {A₁, A₂, ..., Aₙ} such that:

- Every element of A belongs to **exactly one** of the subsets
- A = A₁ ∪ A₂ ∪ ... ∪ Aₙ  
- Aᵢ ∩ Aⱼ = ∅ for i ≠ j

---

#### ✅ Example:

Let A = {1, 2, 3, 4, 5, 6}  
Partition P = {{1, 4}, {2, 5}, {3, 6}}  

- Each subset is non-empty  
- Subsets are disjoint  
- Union of subsets = A  
✅ Valid partition

**Note:** Equivalence relations naturally define partitions (equivalence classes).

---

### 🔹 POSET (Partially Ordered Set)

A **partially ordered set** (POSET) is a set A with a binary relation ≤ satisfying:

1. **Reflexive:** a ≤ a  
2. **Antisymmetric:** if a ≤ b and b ≤ a, then a = b  
3. **Transitive:** if a ≤ b and b ≤ c, then a ≤ c  

---

#### ✅ Example:

Set A = {1, 2, 3, 4, 6}, Relation ≤ (divides)

So:

- 1 divides 2, 3, 4, 6  
- 2 divides 4 and 6  
- 3 divides 6  

Valid POSET because:
- Reflexive: Each number divides itself  
- Antisymmetric: If a divides b and b divides a ⇒ a = b  
- Transitive: If a divides b and b divides c ⇒ a divides c

---

### 🔹 Hasse Diagram

A **Hasse diagram** is a graphical representation of a POSET that:

- Omits self-loops (reflexivity)  
- Omits transitive edges  
- Draws elements with lower ones below higher ones  

---

#### ✅ Example:

POSET: Set A = {1, 2, 4, 8}, with relation “divides” (|)

Hasse Diagram:

```
    8
    |
    4
    |
    2
    |
    1
```

Each edge shows an **immediate relation** (covering relation). The diagram **visualizes hierarchy** and helps with **least upper bound / greatest lower bound** concepts.

---
## Functions and Its Types, Composition and Inverse, Recursive Function (with Examples)

---

### 🔹 Functions and Its Types

A **function** f from A to B (written as f: A → B) is a rule that assigns **each element** in A **exactly one** element in B.

Let A = domain, B = codomain.

---

#### ✅ Example:

Let A = {1, 2, 3}, B = {4, 5, 6}  
f: A → B, defined by  
f(1) = 4, f(2) = 5, f(3) = 6

This is a valid function.

---

### Types of Functions:

1. **One-to-One (Injective):**  
   No two inputs map to the same output  
   - f(x) = 2x, domain: ℝ → ℝ is injective  
   - f(1) = 2, f(2) = 4 ✅ (distinct inputs → distinct outputs)

2. **Onto (Surjective):**  
   Every element in codomain is mapped by some input  
   - f(x) = x² from ℝ → ℝ⁺ is not onto (negative values not covered)

3. **Bijective:**  
   Both injective and surjective  
   - f(x) = x + 1 from ℝ → ℝ is bijective  

---

### 🔹 Composition of Functions

Given:
- f: A → B  
- g: B → C  
Then **composition g∘f**: A → C is defined as  
(g∘f)(x) = g(f(x))

---

#### ✅ Example:

Let f(x) = x + 2, g(x) = x²  
Then:

(g∘f)(x) = g(f(x)) = g(x + 2) = (x + 2)²

So, (g∘f)(3) = (3 + 2)² = 25

---

### 🔹 Inverse of a Function

The inverse of a function f: A → B is f⁻¹: B → A such that  
f(f⁻¹(y)) = y and f⁻¹(f(x)) = x

**Exists only if f is bijective.**

---

#### ✅ Example:

f(x) = 2x + 3  
To find f⁻¹(x):

Let y = 2x + 3 → Solve for x:  
x = (y - 3)/2

∴ f⁻¹(x) = (x - 3)/2

Check:  
f(f⁻¹(x)) = 2((x - 3)/2) + 3 = x ✅

---

### 🔹 Recursive Function

A function is **recursive** if it's defined in terms of itself.

---

#### ✅ Example:

**Factorial** using recursion:

- Base case: 0! = 1  
- Recursive: n! = n × (n−1)!

**Code:**

```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
```

fact(4) → 4 × 3 × 2 × 1 = **24**

---
# Unit -II  
- Predictive modelling and Analysis - Regression Analysis, Correlation analysis, Rank correlation coefficient, multiple correlation, least square, Curve fitting and goodness of fit.  
---
---

## 🔹 Predictive Modelling and Analysis

**Predictive Modelling** is the process of using data and statistical algorithms to predict future outcomes based on historical data.

---

## 1. **Regression Analysis**

**Definition:**  
Regression analysis estimates the relationship between a dependent variable (Y) and one or more independent variables (X).

### 🔸 Types:
- **Simple Linear Regression**: One independent variable  
  Equation: **Y = a + bX**
- **Multiple Linear Regression**: More than one independent variable  
  Equation: **Y = a + b₁X₁ + b₂X₂ + ... + bₙXₙ**

---

### ✅ Example Problem:

**Given:**
X = [1, 2, 3, 4, 5]  
Y = [2, 4, 5, 4, 5]

Find the regression line **Y = a + bX**

#### Step 1: Compute the means
$$
\bar{X} = \frac{1+2+3+4+5}{5} = 3,\quad \bar{Y} = \frac{2+4+5+4+5}{5} = 4
$$

#### Step 2: Compute b (slope)
$$
b = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}
= \frac{(1-3)(2-4)+(2-3)(4-4)+(3-3)(5-4)+(4-3)(4-4)+(5-3)(5-4)}{(1-3)^2+(2-3)^2+(3-3)^2+(4-3)^2+(5-3)^2}
= \frac{4}{10} = 0.4
$$

#### Step 3: Compute a (intercept)
$$
a = \bar{Y} - b\bar{X} = 4 - 0.4×3 = 2.8
$$

#### ✅ Regression Line:  
**Y = 2.8 + 0.4X**

---
---

## 2. **Correlation Analysis**

**Definition:**  
Correlation measures the strength and direction of a linear relationship between two variables.

---

### 🔸 Pearson’s Correlation Coefficient (r)

$$
r = \frac{n \sum XY - \sum X \sum Y}{\sqrt{(n \sum X^2 - (\sum X)^2)(n \sum Y^2 - (\sum Y)^2)}}
$$

- **r = 1**: Perfect positive correlation  
- **r = -1**: Perfect negative correlation  
- **r = 0**: No correlation  

---

### ✅ Example Problem:

**Given:**

| X   | Y   |
| --- | --- |
| 1   | 2   |
| 2   | 4   |
| 3   | 5   |
| 4   | 4   |
| 5   | 5   |

#### Step 1: Calculate necessary sums

$$
\sum X = 15,\quad \sum Y = 20,\quad \sum XY = 66,\quad \sum X^2 = 55,\quad \sum Y^2 = 86,\quad n = 5
$$

#### Step 2: Apply formula

$$
r = \frac{5(66) - (15)(20)}{\sqrt{(5)(55) - (15)^2)(5)(86) - (20)^2}}
= \frac{330 - 300}{\sqrt{(275 - 225)(430 - 400)}}
= \frac{30}{\sqrt{50×30}} = \frac{30}{\sqrt{1500}} ≈ \frac{30}{38.73} ≈ 0.775
$$

#### ✅ Interpretation:
There is a **strong positive correlation** between X and Y.

---
---

## 3. **Rank Correlation Coefficient (Spearman’s rho)**

### 🔸 Definition:
Used to measure the correlation between **ranks** of two variables (especially when data is not normally distributed or not linear).

$$
\rho = 1 - \frac{6 \sum d^2}{n(n^2 - 1)}
$$

Where:  
- $d$ = difference between ranks  
- $n$ = number of data pairs  

---

### ✅ Example Problem:

**Given:**

| X   | Y   |
| --- | --- |
| 80  | 100 |
| 60  | 90  |
| 70  | 80  |
| 90  | 70  |
| 50  | 60  |

#### Step 1: Assign ranks to X and Y (highest value = rank 1)

| X   | Rank(X) | Y   | Rank(Y) | d   | d²  |
| --- | ------- | --- | ------- | --- | --- |
| 80  | 2       | 100 | 1       | 1   | 1   |
| 60  | 4       | 90  | 2       | 2   | 4   |
| 70  | 3       | 80  | 3       | 0   | 0   |
| 90  | 1       | 70  | 4       | -3  | 9   |
| 50  | 5       | 60  | 5       | 0   | 0   |

$$
\sum d^2 = 14,\quad n = 5
$$

#### Step 2: Apply formula

$$
\rho = 1 - \frac{6 \times 14}{5(5^2 - 1)} = 1 - \frac{84}{120} = 1 - 0.7 = 0.3
$$

#### ✅ Interpretation:
There is a **low positive correlation** between X and Y ranks.

---
---

## 4. **Multiple Correlation**

### 🔸 Definition:
Multiple correlation measures the strength of the relationship between **one dependent variable** and **two or more independent variables**.

- It is denoted by **R** (uppercase), unlike simple correlation which is **r**.
- The square of multiple correlation coefficient $R^2$ indicates how well the independent variables explain the variance in the dependent variable.

---

### 🔹 Formula (for three variables):
If we have variables $X_1$, $X_2$, and $Y$, then:

$$
R_{Y.X_1X_2} = \sqrt{ \frac{r_{Y,X_1}^2 + r_{Y,X_2}^2 - 2r_{Y,X_1}r_{Y,X_2}r_{X_1,X_2}}{1 - r_{X_1,X_2}^2} }
$$

Where:  
- $r_{Y,X_1}$ = correlation between $Y$ and $X_1$  
- $r_{Y,X_2}$ = correlation between $Y$ and $X_2$  
- $r_{X_1,X_2}$ = correlation between $X_1$ and $X_2$

---

### ✅ Example Problem:

Let’s say we are given the following correlation coefficients:  
- $r_{Y,X_1} = 0.8$  
- $r_{Y,X_2} = 0.6$  
- $r_{X_1,X_2} = 0.5$

Substitute into the formula:

$$
R_{Y.X_1X_2} = \sqrt{ \frac{(0.8)^2 + (0.6)^2 - 2(0.8)(0.6)(0.5)}{1 - (0.5)^2} }
$$

$$
= \sqrt{ \frac{0.64 + 0.36 - 0.48}{1 - 0.25} } = \sqrt{ \frac{0.52}{0.75} } = \sqrt{0.6933} ≈ 0.8326
$$

---

### ✅ Interpretation:
The **multiple correlation coefficient R ≈ 0.83** indicates a **strong relationship** between the dependent variable $Y$ and the independent variables $X_1$ and $X_2$.

---
---

## 5. **Least Squares Method**

### 🔸 Definition:
The **least squares method** is a standard approach in regression analysis to **find the line of best fit** by minimizing the sum of the squares of the vertical deviations (errors) of the points from the line.

---

### 🔹 Line of Best Fit (for Simple Linear Regression):

$$
y = a + bx
$$

Where:  
- \( y \): dependent variable  
- \( x \): independent variable  
- \( a \): y-intercept  
- \( b \): slope of the line

---

### 🔹 Formulas to Find \( a \) and \( b \):

$$
b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2}
$$

$$
a = \frac{\sum y - b \sum x}{n}
$$

---

### ✅ Example Problem:

Fit a line using the least square method for the data:

| x   | y   |
| --- | --- |
| 1   | 2   |
| 2   | 3   |
| 3   | 5   |
| 4   | 4   |
| 5   | 6   |

#### Step 1: Calculate required sums

$$
n = 5, \quad \sum x = 15, \quad \sum y = 20
$$

$$
\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
$$

$$
\sum xy = (1)(2) + (2)(3) + (3)(5) + (4)(4) + (5)(6) = 2 + 6 + 15 + 16 + 30 = 69
$$

#### Step 2: Calculate slope (b)

$$
b = \frac{5(69) - 15(20)}{5(55) - (15)^2} = \frac{345 - 300}{275 - 225} = \frac{45}{50} = 0.9
$$

#### Step 3: Calculate intercept (a)

$$
a = \frac{20 - 0.9(15)}{5} = \frac{20 - 13.5}{5} = \frac{6.5}{5} = 1.3
$$

#### Final equation of best fit line:

$$
y = 1.3 + 0.9x
$$

---

### ✅ Interpretation:
The line \( y = 1.3 + 0.9x \) best fits the data, minimizing the total squared error between predicted and actual values.

---
---

## 6. **Curve Fitting and Goodness of Fit**

---

### 🔸 Curve Fitting:

Curve fitting is the process of constructing a curve (or mathematical function) that best fits a series of data points.

- **Linear fit**: \( y = a + bx \)
- **Polynomial fit**: \( y = a + bx + cx^2 + \ldots \)
- **Exponential fit**: \( y = ab^x \) or \( \ln y = \ln a + x \ln b \)
- **Power fit**: \( y = ax^b \)

---

### 🔹 Method: Least Squares

We use the **least squares method** to find the parameters of the function (constants like \( a \), \( b \), etc.) that minimize the sum of squares of errors between actual and predicted values.

---

### ✅ Example: Exponential Curve Fitting

Fit an exponential curve of the form \( y = ab^x \) to the following data:

| x | y   |
|---|-----|
| 1 | 2.7 |
| 2 | 7.4 |
| 3 | 20.1|

---

### 🔹 Step 1: Take logarithm on both sides:

$$
\log y = \log a + x \log b
$$

Let \( Y = \log y, A = \log a, B = \log b \)

Now we have:  
$$
Y = A + Bx \quad \text{(a linear equation)}
$$

So now fit a straight line to the transformed data:

| x | y   | \( \log y \) |
|---|-----|--------------|
| 1 | 2.7 | 0.431        |
| 2 | 7.4 | 0.869        |
| 3 | 20.1| 1.303        |

Compute:
- \( \sum x = 6 \)
- \( \sum Y = 2.603 \)
- \( \sum xY = 1(0.431) + 2(0.869) + 3(1.303) = 0.431 + 1.738 + 3.909 = 6.078 \)
- \( \sum x^2 = 14 \)

Now apply least square formula:

$$
B = \frac{n\sum xY - \sum x \sum Y}{n\sum x^2 - (\sum x)^2} = \frac{3(6.078) - 6(2.603)}{3(14) - 36} = \frac{18.234 - 15.618}{42 - 36} = \frac{2.616}{6} = 0.436
$$

$$
A = \frac{\sum Y - B\sum x}{n} = \frac{2.603 - 0.436 \cdot 6}{3} = \frac{2.603 - 2.616}{3} = -0.0043
$$

So:
- \( \log a = A = -0.0043 \Rightarrow a = 10^{-0.0043} \approx 0.990 \)
- \( \log b = B = 0.436 \Rightarrow b = 10^{0.436} \approx 2.73 \)

Final curve:
$$
y = 0.990 \cdot (2.73)^x
$$

---

### 🔸 Goodness of Fit:

Measures how well the fitted curve matches the actual data.

#### Common metrics:
- **R² (coefficient of determination)**: Closer to 1 means better fit.
- **Sum of Squares Error (SSE)**: Lower is better.
- **Mean Absolute Error (MAE)** or **Root Mean Square Error (RMSE)**.

---

# Unit -III  
### Random Variable and Probability Distribution:  
- Introduction probability and its property, Random variable, its types DRV, CRV and its distributions, two dimensional R V, joint probability function, marginal density function.  Some special probability distribution- Binomial, Poison, Uniform, Exponential and Normal Distribution.  

---

## 1. **Introduction to Probability and Its Properties**

---

### 🔸 What is Probability?

Probability is the measure of the likelihood of an event occurring. It lies between 0 and 1.

$$
P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}
$$

---

### 🔹 Properties of Probability:

1. **Non-negativity**:  
   $$
   0 \leq P(E) \leq 1
   $$
2. **Normalization**:  
   $$
   P(S) = 1 \quad \text{(S is the sample space)}
   $$
3. **Additivity**: For mutually exclusive events \( A \) and \( B \),  
   $$
   P(A \cup B) = P(A) + P(B)
   $$
4. **Complementary Rule**:  
   $$
   P(\bar{A}) = 1 - P(A)
   $$

---

### ✅ Example Problem:

**Question:**  
A card is drawn from a well-shuffled deck of 52 cards. What is the probability that the card is:
1. A heart?
2. A queen?

---

**Solution:**

1. Total outcomes = 52  
   - Favourable outcomes for a heart = 13  
   $$
   P(\text{Heart}) = \frac{13}{52} = \frac{1}{4}
   $$

2. Favourable outcomes for a queen = 4  
   $$
   P(\text{Queen}) = \frac{4}{52} = \frac{1}{13}
   $$

---

## 2. **Random Variable and Its Types**

---

### 🔸 What is a Random Variable?

A **random variable (RV)** is a function that assigns a real number to each outcome in a sample space.

---

### 🔹 Types of Random Variables:

1. **Discrete Random Variable (DRV)**:
   - Takes only **finite/countable** values.
   - Example: Number of heads in 3 coin tosses.

2. **Continuous Random Variable (CRV)**:
   - Takes **infinite and uncountable** values within a range.
   - Example: Height of students, time taken to run 100m.

---

### ✅ Example Problem:

**Question:**  
A coin is tossed 3 times. Let \( X \) be the number of heads. Is \( X \) a random variable? If so, list its possible values.

---

**Solution:**

Possible outcomes:  
- HHH → 3 heads  
- HHT, HTH, THH → 2 heads  
- HTT, THT, TTH → 1 head  
- TTT → 0 heads  

So, possible values of \( X \) = {0, 1, 2, 3}  
→ This is a **Discrete Random Variable**

---

## 3. **Two-Dimensional Random Variables (Joint Distribution)**

---

### 🔸 What is a Two-Dimensional Random Variable?

A **two-dimensional random variable** is a pair \( (X, Y) \) of random variables defined on the same sample space.

---

### 🔹 Joint Probability Function (Discrete Case)

Let \( X \) and \( Y \) be discrete random variables. The **joint probability function** is:

$$
P(X = x_i, Y = y_j) = p_{ij}
$$

Where:

- \( \sum_i \sum_j p_{ij} = 1 \)
- \( p_{ij} \geq 0 \)

---

### 🔹 Marginal Probability Function

- For \( X \):  
  $$
  P(X = x_i) = \sum_j P(X = x_i, Y = y_j)
  $$
- For \( Y \):  
  $$
  P(Y = y_j) = \sum_i P(X = x_i, Y = y_j)
  $$

---

### ✅ Example Problem:

**Given**: The joint distribution of \( X \) and \( Y \) is:

| Y \ X | 0   | 1   |
|------|-----|-----|
| 0    | 0.2 | 0.3 |
| 1    | 0.1 | 0.4 |

---

**Find**:  
(a) \( P(X = 1) \)  
(b) \( P(Y = 0) \)

---

**Solution**:

(a) \( P(X = 1) = P(X=1, Y=0) + P(X=1, Y=1) = 0.3 + 0.4 = 0.7 \)  
(b) \( P(Y = 0) = P(X=0, Y=0) + P(X=1, Y=0) = 0.2 + 0.3 = 0.5 \)

---

## 4. **Special Probability Distributions – Binomial Distribution**

---

### 🔸 What is a Binomial Distribution?

A **binomial distribution** models the number of **successes** in a fixed number of **independent Bernoulli trials**, each with the same probability of success.

---

### 🔹 Formula:

If \( X \sim B(n, p) \), then:

$$
P(X = r) = \binom{n}{r} p^r (1-p)^{n-r}
$$

Where:  
- \( n \) = number of trials  
- \( p \) = probability of success in each trial  
- \( r \) = number of successes (r = 0, 1, ..., n)

---

### 🔹 Mean and Variance:

- \( \mu = np \)  
- \( \sigma^2 = np(1-p) \)

---

### ✅ Example Problem:

A fair coin is tossed 5 times. What is the probability of getting exactly 3 heads?

**Solution**:  
Here,  
- \( n = 5 \)  
- \( p = 0.5 \) (since the coin is fair)  
- \( r = 3 \)

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^2 = 10 \times 0.125 \times 0.25 = 0.3125
$$

📌 **Answer**: \( P(X = 3) = 0.3125 \)

---

## 5. **Special Probability Distributions – Poisson Distribution**

---

### 🔸 What is a Poisson Distribution?

The **Poisson distribution** models the number of times an event occurs in a **fixed interval** of time or space, provided the events occur with a known constant mean rate and independently of the time since the last event.

---

### 🔹 Formula:

If \( X \sim \text{Poisson}(\lambda) \), then:

$$
P(X = r) = \frac{e^{-\lambda} \lambda^r}{r!}
$$

Where:  
- \( \lambda \) = average number of occurrences (rate)  
- \( r \) = number of occurrences (r = 0, 1, 2, ...)

---

### 🔹 Mean and Variance:

- \( \mu = \lambda \)  
- \( \sigma^2 = \lambda \)

---

### ✅ Example Problem:

A call center receives an average of 6 calls per hour. What is the probability that they receive exactly 4 calls in an hour?

**Solution**:  
Here,  
- \( \lambda = 6 \),  
- \( r = 4 \)

$$
P(X = 4) = \frac{e^{-6} \cdot 6^4}{4!} = \frac{e^{-6} \cdot 1296}{24}
$$

Using \( e^{-6} \approx 0.00247875 \):

$$
P(X = 4) \approx \frac{0.00247875 \cdot 1296}{24} \approx \frac{3.211}{24} \approx 0.1338
$$

📌 **Answer**: \( P(X = 4) \approx 0.1338 \)

---

## 6. **Special Probability Distributions – Uniform Distribution**

---

### 🔸 What is a Uniform Distribution?

A **Uniform distribution** is one in which **all outcomes are equally likely** within a certain interval.

There are two types:

- **Discrete Uniform Distribution**: Finite number of equally likely outcomes.
- **Continuous Uniform Distribution**: Any value within an interval is equally likely.

---

### 🔹 Continuous Uniform Distribution

If a random variable \( X \sim U(a, b) \), then:

$$
f(x) = 
\begin{cases}
\frac{1}{b-a} & \text{for } a \le x \le b \\
0 & \text{otherwise}
\end{cases}
$$

---

### 🔹 Mean and Variance

- Mean: \( \mu = \frac{a + b}{2} \)  
- Variance: \( \sigma^2 = \frac{(b - a)^2}{12} \)

---

### ✅ Example Problem

A bus arrives every 20 minutes. A person arrives at a random time. What is the probability that they wait less than 5 minutes?

**Solution**:  
Let \( X \sim U(0, 20) \), and we want \( P(X < 5) \):

$$
P(X < 5) = \int_0^5 \frac{1}{20} dx = \frac{5}{20} = 0.25
$$

📌 **Answer**: \( P(X < 5) = 0.25 \)

---

## 7. **Special Probability Distributions – Exponential Distribution**

---

### 🔸 What is the Exponential Distribution?

The **Exponential Distribution** models the **time between events** in a Poisson process (i.e., events occurring independently at a constant average rate).

It is **memoryless**, meaning the probability of an event occurring in the future is independent of the past.

---

### 🔹 Probability Density Function (PDF)

$$
f(x; \lambda) = 
\begin{cases}
\lambda e^{-\lambda x} & x \ge 0 \\
0 & x < 0
\end{cases}
$$

Where:
- \( \lambda > 0 \): rate parameter (events per unit time)
- \( x \): time between events

---

### 🔹 Mean and Variance

- Mean: \( \mu = \frac{1}{\lambda} \)
- Variance: \( \sigma^2 = \frac{1}{\lambda^2} \)

---

### ✅ Example Problem

If the average number of phone calls at a call center is **5 per hour**, what is the probability that the **next call comes within 10 minutes**?

---

### 🔹 Solution:

- Convert 10 minutes to hours: \( x = \frac{10}{60} = \frac{1}{6} \)
- Rate: \( \lambda = 5 \)
- Use cumulative probability:

$$
P(X \le \frac{1}{6}) = 1 - e^{-\lambda x} = 1 - e^{-5 \cdot \frac{1}{6}} = 1 - e^{-\frac{5}{6}} \approx 1 - 0.434 = 0.566
$$

📌 **Answer**: ~56.6% chance the next call comes within 10 minutes.

---

## 8. **Special Probability Distributions – Normal Distribution**

---

### 🔸 What is the Normal Distribution?

The **Normal distribution** (or Gaussian distribution) is a continuous probability distribution that is **symmetrical** around the mean, representing real-valued random variables with a bell-shaped curve.

---

### 🔹 Probability Density Function (PDF)

$$
f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \cdot e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

Where:
- \( \mu \) = Mean
- \( \sigma^2 \) = Variance
- \( \sigma \) = Standard deviation

---

### 🔹 Properties of Normal Distribution

- Bell-shaped and symmetric about the mean
- Mean = Median = Mode
- Total area under the curve = 1
- 68% of values lie within 1σ, 95% within 2σ, and 99.7% within 3σ

---

### 🔹 Standard Normal Distribution

If \( \mu = 0 \) and \( \sigma = 1 \), then it's called the **Standard Normal Distribution**.

Any normal distribution can be **standardized** using:

$$
Z = \frac{X - \mu}{\sigma}
$$

---

### ✅ Example Problem

**Q:** Heights of students are normally distributed with a mean of 170 cm and standard deviation of 10 cm. What is the probability that a randomly selected student is taller than 185 cm?

---

### 🔹 Solution:

Given:
- \( \mu = 170 \)
- \( \sigma = 10 \)
- \( X = 185 \)

Step 1: Convert to Z-score  
$$
Z = \frac{185 - 170}{10} = \frac{15}{10} = 1.5
$$

Step 2: Find \( P(Z > 1.5) \)

Using Z-table:  
$$
P(Z < 1.5) = 0.9332 \Rightarrow P(Z > 1.5) = 1 - 0.9332 = 0.0668
$$

📌 **Answer**: There's a **6.68%** chance that a student is taller than 185 cm.

---
# Unit -IV  
### Hypothesis Testing :  
- Introduction Sampling, Sampling distribution, one and two tailed test, Test of significance, (mean, difference of means), confidence interval  1% and 5% level of significance - Design of Experiments, one way classification, two way classification, ANOVA.  
---

## 1. **Introduction to Sampling**

---

### 🔸 What is Sampling?

**Sampling** is the process of selecting a subset (sample) from a larger population to estimate characteristics of the whole population.

---

### 🔹 Key Terms

- **Population**: The entire group under study.
- **Sample**: A subset drawn from the population.
- **Sampling Distribution**: The probability distribution of a statistic (like mean or proportion) over all possible samples of a given size.

---

### 🔹 Importance of Sampling

- Reduces time and cost
- Makes analysis feasible
- Helps in estimating population parameters

---

### 🔹 Types of Sampling Methods

1. **Random Sampling** – Every element has equal chance (e.g., lottery)
2. **Stratified Sampling** – Population divided into subgroups (strata)
3. **Systematic Sampling** – Every kth element is selected
4. **Cluster Sampling** – Groups (clusters) are selected randomly
5. **Convenience Sampling** – Non-random; based on availability

---

### ✅ Example Problem

**Q:** A company wants to estimate the average salary of its 1,000 employees. They randomly select 50 employees. What is this process called?

**A:** This is **Random Sampling**, and the average salary of the 50 employees will be a sample mean used to estimate the population mean.

---

### 🔹 Central Limit Theorem (CLT)

If sample size is large (n ≥ 30), the **sampling distribution** of the sample mean approaches a **normal distribution**, regardless of the population's distribution.

---

Ready for the next topic: **One-tailed and Two-tailed Tests**?---

## 1. **Introduction to Sampling**

---

### 🔸 What is Sampling?

**Sampling** is the process of selecting a subset (sample) from a larger population to estimate characteristics of the whole population.

---

### 🔹 Key Terms

- **Population**: The entire group under study.
- **Sample**: A subset drawn from the population.
- **Sampling Distribution**: The probability distribution of a statistic (like mean or proportion) over all possible samples of a given size.

---

### 🔹 Importance of Sampling

- Reduces time and cost
- Makes analysis feasible
- Helps in estimating population parameters

---

### 🔹 Types of Sampling Methods

1. **Random Sampling** – Every element has equal chance (e.g., lottery)
2. **Stratified Sampling** – Population divided into subgroups (strata)
3. **Systematic Sampling** – Every kth element is selected
4. **Cluster Sampling** – Groups (clusters) are selected randomly
5. **Convenience Sampling** – Non-random; based on availability

---

### ✅ Example Problem

**Q:** A company wants to estimate the average salary of its 1,000 employees. They randomly select 50 employees. What is this process called?

**A:** This is **Random Sampling**, and the average salary of the 50 employees will be a sample mean used to estimate the population mean.

---

### 🔹 Central Limit Theorem (CLT)

If sample size is large (n ≥ 30), the **sampling distribution** of the sample mean approaches a **normal distribution**, regardless of the population's distribution.

---

## 2. **One-tailed and Two-tailed Tests**

---

### 🔸 What is Hypothesis Testing?

Hypothesis testing is a **statistical method** used to make decisions about population parameters based on sample data.

- **Null Hypothesis (H₀)**: No effect or no difference.
- **Alternative Hypothesis (H₁ or Hₐ)**: There is an effect or difference.

---

### 🔹 One-tailed Test

- **Used when the direction of the effect is specified.**
- Tests for either greater than or less than.

#### 🧠 Example:
> H₀: μ = 50  
> H₁: μ > 50 (right-tailed test)  
> or  
> H₁: μ < 50 (left-tailed test)

---

### 🔹 Two-tailed Test

- **Used when direction is NOT specified.**
- Tests whether a value is **significantly different** (either higher or lower).

#### 🧠 Example:
> H₀: μ = 50  
> H₁: μ ≠ 50

---

### 🔸 Test Statistic (Z or t)

$$
Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \quad \text{(for known population std. dev.)}
$$
$$
t = \frac{\bar{x} - \mu}{s / \sqrt{n}} \quad \text{(when population std. dev. is unknown)}
$$

---

### ✅ Example Problem (Two-tailed Z-test)

A machine fills juice bottles. The company claims it fills **500 ml** on average. A sample of **36 bottles** has a mean of **492 ml** with standard deviation **15 ml**. Test the claim at **5% significance level**.

#### ➤ Given:
- μ = 500 (claimed mean)
- x̄ = 492  
- σ = 15  
- n = 36  
- α = 0.05 (two-tailed) ⇒ critical Z = ±1.96

$$
Z = \frac{492 - 500}{15/\sqrt{36}} = \frac{-8}{2.5} = -3.2
$$

#### ➤ Since -3.2 < -1.96 ⇒ **Reject H₀**

📌 **Conclusion**: The average fill is significantly different from 500 ml.

---

## 3. **Test of Significance (Mean, Difference of Means)**

---

### 🔹 A. **Test of Significance for a Single Mean**

Used to determine if the **sample mean** significantly differs from the **population mean**.

#### ✅ Formula:

$$
Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \quad \text{(if } \sigma \text{ is known)}
$$
or  
$$
t = \frac{\bar{x} - \mu}{s / \sqrt{n}} \quad \text{(if } \sigma \text{ is unknown)}
$$

---

#### 🧠 Example (Z-test for Mean):

A sample of 64 students has a mean score of 72. The population mean is 75 with σ = 8. Test if the sample differs at 5% significance.

$$
Z = \frac{72 - 75}{8/\sqrt{64}} = \frac{-3}{1} = -3
$$

Critical Z (two-tailed at α = 0.05) = ±1.96

👉 Since -3 < -1.96 → **Reject H₀**

📌 **Conclusion**: There is significant difference from population mean.

---

### 🔹 B. **Test for Difference of Two Means (Independent Samples)**

Checks if the means of **two different populations** are significantly different.

---

#### ✅ Formula (Z-test):

$$
Z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}
$$

---

#### 🧠 Example:

- Sample 1: n₁ = 50, x̄₁ = 70, σ₁ = 8  
- Sample 2: n₂ = 60, x̄₂ = 65, σ₂ = 6  

$$
Z = \frac{70 - 65}{\sqrt{\frac{8^2}{50} + \frac{6^2}{60}}} = \frac{5}{\sqrt{1.28 + 0.6}} = \frac{5}{\sqrt{1.88}} ≈ \frac{5}{1.372} ≈ 3.64
$$

Critical Z = ±1.96 ⇒ **Reject H₀**

📌 **Conclusion**: The two sample means are significantly different.

---

## 4. **Confidence Interval (1% and 5% Level of Significance)**

---

### 🔹 What is a Confidence Interval?

A **confidence interval (CI)** estimates a range within which the **true population parameter** (like mean or proportion) lies, with a certain level of confidence.

Common confidence levels:
- **95% CI → α = 0.05**
- **99% CI → α = 0.01**

---

### ✅ Formula for Confidence Interval of Mean:

If population standard deviation **σ is known**:
$$
\text{CI} = \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

If **σ is unknown**, and sample size is small → use **t-distribution**:
$$
\text{CI} = \bar{x} \pm t_{\alpha/2, \, df} \cdot \frac{s}{\sqrt{n}}
$$

Where:
- $\bar{x}$ = sample mean  
- $n$ = sample size  
- $s$ = sample standard deviation  
- $Z_{\alpha/2}$ = Z-critical value  
- $t_{\alpha/2, \, df}$ = t-critical value with degrees of freedom  

---

### 📘 Z-critical values:
- **95% CI → Z = 1.96**
- **99% CI → Z = 2.576**

---

### 🧠 Example 1: (95% CI with known σ)

A sample of 100 items has mean 60, and population σ = 10. Find 95% CI for the mean.

$$
CI = 60 \pm 1.96 \cdot \frac{10}{\sqrt{100}} = 60 \pm 1.96 \cdot 1 = 60 \pm 1.96
$$

📌 **Answer**: (58.04, 61.96)

---

### 🧠 Example 2: (99% CI with unknown σ, use t-test)

A sample of 10 values has mean 20, and standard deviation 4. Find 99% CI.

Degrees of freedom = 9, from t-table: $t_{0.005, 9} ≈ 3.25$

$$
CI = 20 \pm 3.25 \cdot \frac{4}{\sqrt{10}} ≈ 20 \pm 3.25 \cdot 1.264 = 20 \pm 4.113
$$

📌 **Answer**: (15.887, 24.113)

---

## 5. **Design of Experiments (DOE)**

---

### 🔹 What is DOE?

**Design of Experiments** is a branch of applied statistics used to **plan, conduct, analyze, and interpret** controlled tests to evaluate factors that control the value of a parameter or group of parameters.

It helps in:
- Reducing variability
- Improving product/process quality
- Identifying cause-effect relationships

---

### 🔹 Key Concepts

| Term                  | Description |
|-----------------------|-------------|
| **Factors**            | Variables that are changed in an experiment |
| **Levels**             | Settings of each factor (e.g., low/high) |
| **Treatment**          | Combination of factor levels |
| **Response Variable**  | Output that is measured |
| **Replication**        | Repeating the experiment to reduce error |
| **Randomization**      | Randomly assigning treatments to avoid bias |
| **Blocking**           | Grouping similar experimental units to reduce variability |

---

### 🧪 Types of Designs

1. **Completely Randomized Design (CRD)**  
2. **Randomized Block Design (RBD)**  
3. **Latin Square Design**  
4. **Factorial Design** (2-level factorials, full factorial, fractional)

---

### 📘 Example:

Suppose we want to test the effect of **2 fertilizers (F1, F2)** on crop yield.  
We randomly assign 5 plots to F1 and 5 plots to F2 (CRD).  
We then measure the yield (response variable) and use statistical tests like **ANOVA** to check if the difference is significant.

---

### 🧠 Mini Problem:

**Q**: You are testing 3 teaching methods on student performance. Each method is used on 4 students. What design is this?

**A**: Completely Randomized Design (CRD)  
Each method is a **treatment**, and students are randomly assigned.

---

## 6. **One-Way Classification (ANOVA - Single Factor)**

---

### 🔹 What is One-Way Classification?

One-way classification is a **type of ANOVA (Analysis of Variance)** used to test whether **means of several groups** are equal, based on **one independent variable (factor)**.

---

### 🔹 Use Case

You want to compare **k group means** to see if at least one is significantly different.

For example:
- Comparing test scores of students from **3 different teaching methods**.
- Comparing crop yields using **3 different fertilizers**.

---

### 🔹 Hypotheses

- **Null Hypothesis (H₀):** All group means are equal.  
  $H_0: \mu_1 = \mu_2 = \cdots = \mu_k$
  
- **Alternate Hypothesis (H₁):** At least one group mean is different.

---

### 🔹 ANOVA Table Format

| Source of Variation | Sum of Squares (SS) | Degrees of Freedom (df) | Mean Squares (MS) | F-Ratio |
|---------------------|---------------------|--------------------------|--------------------|---------|
| Between Groups      | SS<sub>Between</sub> | k - 1                    | MS<sub>B</sub> = SS<sub>B</sub> / (k - 1) | F = MS<sub>B</sub> / MS<sub>W</sub> |
| Within Groups       | SS<sub>Within</sub>  | N - k                    | MS<sub>W</sub> = SS<sub>W</sub> / (N - k) |         |
| Total               | SS<sub>Total</sub>   | N - 1                    |                    |         |

---

### 🔹 Decision Rule

Compare F-calculated with F-critical from F-table:
- If **F-cal > F-table**, reject H₀.
- Else, do not reject H₀.

---

### 📘 Example Problem

**Problem**: Compare mean marks of students taught with 3 methods.

| Method | Marks       |
|--------|-------------|
| A      | 82, 85, 88  |
| B      | 75, 78, 74  |
| C      | 90, 92, 95  |

**Step 1**: Calculate group means and overall mean.  
**Step 2**: Compute SS<sub>Between</sub>, SS<sub>Within</sub>, then MS and F.  
**Step 3**: Check F with F-critical (from table, at 5% significance).  

Let’s say:  
- F<sub>calculated</sub> = 7.9  
- F<sub>critical</sub> (df₁ = 2, df₂ = 6) ≈ 5.14

✅ Since 7.9 > 5.14 → **Reject H₀**: There’s a significant difference in means.

---

## 7. **Two-Way Classification (Two-Factor ANOVA)**

---

### 🔹 What is Two-Way Classification?

Two-way classification is an **extension of one-way ANOVA**, where **two independent variables (factors)** are studied simultaneously to observe their effects on a dependent variable.

---

### 🔹 Use Case

To test:
- The **individual effect** of each factor.
- The **interaction effect** between factors.

For example:  
Studying the effect of:
- **Teaching Method** (Factor A)  
- **Gender** (Factor B)  
on **Student Scores**.

---

### 🔹 Assumptions

- The samples are random and independent.
- Each group is normally distributed.
- Variances are equal.

---

### 🔹 Hypotheses

- $H_0^A$: No significant effect of Factor A  
- $H_0^B$: No significant effect of Factor B  
- $H_0^{AB}$: No interaction effect between A and B

---

### 🔹 Two-Way ANOVA Table

| Source of Variation | Sum of Squares (SS) | df           | Mean Square (MS)        | F-Ratio                     |
|---------------------|---------------------|--------------|--------------------------|-----------------------------|
| Factor A            | SSA                 | a - 1        | MSA = SSA / (a - 1)      | F<sub>A</sub> = MSA / MSE   |
| Factor B            | SSB                 | b - 1        | MSB = SSB / (b - 1)      | F<sub>B</sub> = MSB / MSE   |
| Interaction AB      | SSAB                | (a - 1)(b - 1)| MSAB = SSAB / (a−1)(b−1) | F<sub>AB</sub> = MSAB / MSE |
| Error               | SSE                 | ab(n − 1)    | MSE = SSE / ab(n − 1)    |                             |
| Total               | SST                 | N − 1        |                          |                             |

Where:  
- **a** = number of levels in Factor A  
- **b** = number of levels in Factor B  
- **n** = number of observations per cell  
- **N = abn**

---

### 🔹 Decision Rule

Compare the F-ratios with F-critical values.  
- If **F > F<sub>critical</sub>**, reject the corresponding null hypothesis.

---

### 📘 Example Problem

**Problem**: A company tests productivity (scores) using 2 Machines (A1, A2) and 3 Shifts (S1, S2, S3).  

|         | S1 | S2 | S3 |
|---------|----|----|----|
| A1      | 20 | 25 | 23 |
| A2      | 27 | 30 | 29 |

**Steps**:
1. Calculate row (machine), column (shift) means and grand mean.
2. Compute SS for machine, shift, interaction, and error.
3. Construct the ANOVA table.
4. Calculate F-values.
5. Compare with F-table values.

Let’s say:
- $F_A = 10.2 > F_{crit} = 4.26$ → Reject $H_0^A$
- $F_B = 5.3 > F_{crit} = 3.89$ → Reject $H_0^B$
- $F_{AB} = 1.1 < F_{crit} = 3.2$ → Do not reject $H_0^{AB}$

✅ So, both machine type and shift significantly affect productivity, but there’s **no interaction** effect.

---

## 📘 **Types of Errors in Hypothesis Testing**

### 🔹 Type I Error (False Positive)
- **Definition**: Rejecting the null hypothesis ($H_0$) when it is **actually true**.
- **Symbol**: $\alpha$ (alpha)  
- **Also Called**: Significance Level of the test
- **Example**: Declaring a person guilty when they are innocent.
- **Control**: Reduce $\alpha$ to lower Type I error.

> If $\alpha = 0.05$, there is a **5% chance** of making a Type I error.

---

### 🔹 Type II Error (False Negative)
- **Definition**: Failing to reject the null hypothesis ($H_0$) when it is **actually false**.
- **Symbol**: $\beta$ (beta)
- **Example**: Declaring a person innocent when they are actually guilty.
- **Control**: Increase sample size or improve test power to reduce $\beta$.

---

### 🔹 Power of a Test
- **Definition**: Probability of correctly rejecting a false null hypothesis.
- **Formula**:  
  $$ \text{Power} = 1 - \beta $$
- **Interpretation**: Higher power means better ability to detect an actual effect.

---

### 🔹 Summary Table

| Decision / Truth       | $H_0$ is True            | $H_0$ is False           |
|------------------------|--------------------------|--------------------------|
| **Reject $H_0$**       | **Type I Error ($\alpha$)** | **Correct Decision** (Power) |
| **Fail to Reject $H_0$** | **Correct Decision**      | **Type II Error ($\beta$)**  |

---

# Formulas:-
## 📘 **Unit I: Set Theory, Relations, and Functions**

### 🔹 Set Theory  
- $n(A \cup B) = n(A) + n(B) - n(A \cap B)$  
- $n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$  
- Complement: $A' = U - A$  
- De Morgan's Laws:  
  - $(A \cup B)' = A' \cap B'$  
  - $(A \cap B)' = A' \cup B'$  

### 🔹 Relations  
- **Cartesian Product**: $A \times B = \{(a, b) \mid a \in A, b \in B\}$  
- **Equivalence Relation**: Must be Reflexive, Symmetric, and Transitive  

### 🔹 Functions  
- Composition: $(f \circ g)(x) = f(g(x))$  
- Inverse: $f(f^{-1}(x)) = x$  
- Recursive: $f(n) = f(n-1) + f(n-2)$ (example for Fibonacci)

---

## 📘 **Unit II: Predictive Modelling & Regression**

### 🔹 Correlation  
- **Karl Pearson’s r**:  
  $$ r = \frac{n\sum xy - \sum x \sum y}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}} $$  
- **Spearman Rank Correlation**:  
  $$ r_s = 1 - \frac{6\sum d^2}{n(n^2 - 1)} $$  
  Where $d$ = difference in ranks  

### 🔹 Regression Equations  
- $y = a + bx$  
- Slope:  
  $$ b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2} $$  
- Intercept:  
  $$ a = \bar{y} - b\bar{x} $$  

### 🔹 Least Squares & Curve Fitting  
- **Straight Line Fit**: $y = a + bx$  
- **Normal Equations**:  
  $$ \sum y = na + b\sum x $$  
  $$ \sum xy = a\sum x + b\sum x^2 $$  

---

## 📘 **Unit III: Probability and Distributions**

### 🔹 Basic Probability  
- $P(E) = \frac{n(E)}{n(S)}$  
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$  
- Conditional: $P(A|B) = \frac{P(A \cap B)}{P(B)}$  
- Bayes’ Theorem:  
  $$ P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_{j} P(A_j)P(B|A_j)} $$  

### 🔹 Expected Value and Variance  
- $E(X) = \sum x \cdot P(x)$  
- $Var(X) = E(X^2) - [E(X)]^2$  

### 🔹 Discrete Distributions  
- **Binomial**:  
  $$ P(X = r) = \binom{n}{r} p^r q^{n-r} $$  
  Mean: $np$, Variance: $npq$  

- **Poisson**:  
  $$ P(X = r) = \frac{e^{-m}m^r}{r!} $$  
  Mean = Variance = $m$

### 🔹 Continuous Distributions  
- **Uniform**:  
  $$ f(x) = \frac{1}{b - a}, \quad a \le x \le b $$  
  Mean = $\frac{a + b}{2}$, Variance = $\frac{(b - a)^2}{12}$  

- **Exponential**:  
  $$ f(x) = \lambda e^{-\lambda x}, \quad x \ge 0 $$  
  Mean = $\frac{1}{\lambda}$, Variance = $\frac{1}{\lambda^2}$  

- **Normal**:  
  $$ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x - \mu)^2}{2\sigma^2}} $$  
  Z-score:  
  $$ Z = \frac{X - \mu}{\sigma} $$  

---

## 📘 **Unit IV: Hypothesis Testing and ANOVA**

### 🔹 Sampling and Testing  
- **Z-test (Large Samples)**:  
  $$ Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}} $$  
- **t-test (Small Samples)**:  
  $$ t = \frac{\bar{x} - \mu}{s/\sqrt{n}} $$  
- **Two Sample t-test**:  
  $$ t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $$  

### 🔹 Confidence Interval  
- 95% CI: $\bar{x} \pm 1.96 \cdot \frac{\sigma}{\sqrt{n}}$  
- 99% CI: $\bar{x} \pm 2.58 \cdot \frac{\sigma}{\sqrt{n}}$  

### 🔹 ANOVA (One-Way)  
- SST = Total Sum of Squares  
- SSB = Sum of Squares Between Groups  
- SSW = Sum of Squares Within Groups  
-  
  $$
  F = \frac{\text{MSB}}{\text{MSW}} = \frac{\text{SSB}/(k-1)}{\text{SSW}/(N-k)}
  $$

### 🔹 Two-Way ANOVA  
Similar to One-Way but includes interaction:

$$
F_A = \frac{MS_A}{MS_E}, \quad
F_B = \frac{MS_B}{MS_E}, \quad
F_{AB} = \frac{MS_{AB}}{MS_E}
$$

---

# Difference:- 
## 📘 **Unit I: Set Theory, Relations & Functions**

### 🔹 Difference between Set and Subset  
| Set | Subset |
|------|--------|
| A collection of well-defined elements | A set contained within another set |
| Denoted as $A = \{1,2,3\}$ | $B = \{1,2\} \subset A$ |

---

### 🔹 Difference between Relation and Function  
| Relation | Function |
|----------|----------|
| Any subset of Cartesian product | Special type of relation where each input has exactly one output |
| Can have multiple outputs for an input | Only one output per input |

---

### 🔹 One-One vs Onto vs Bijective  
| Type | Definition |
|------|------------|
| One-One (Injective) | Every element of domain maps to a unique element in codomain |
| Onto (Surjective) | Every element of codomain is mapped by at least one domain element |
| Bijective | Both One-One and Onto |

---

### 🔹 POSET vs Equivalence Relation  
| POSET (Partially Ordered Set) | Equivalence Relation |
|-------------------------------|----------------------|
| Reflexive, Antisymmetric, Transitive | Reflexive, Symmetric, Transitive |

---

## 📘 **Unit II: Regression, Correlation, Curve Fitting**

### 🔹 Difference between Correlation and Regression  
| Correlation | Regression |
|-------------|------------|
| Measures strength & direction of relationship | Predicts value of dependent variable based on independent variable |
| Symmetrical | Asymmetrical |
| $r$ (correlation coefficient) | Equation like $y = a + bx$ |

---

### 🔹 Pearson vs Spearman Correlation  
| Pearson | Spearman |
|---------|----------|
| Measures linear correlation | Measures rank-based correlation |
| Requires normal distribution | Can be used for ordinal data |

---

### 🔹 Curve Fitting vs Least Squares  
| Curve Fitting | Least Squares |
|---------------|----------------|
| General process of finding curve for data | Specific method minimizing squared error |

---

## 📘 **Unit III: Probability & Distributions**

### 🔹 Discrete vs Continuous Random Variable  
| Discrete RV | Continuous RV |
|-------------|---------------|
| Countable outcomes | Infinite outcomes in a range |
| Example: Number of heads | Example: Temperature |

---

### 🔹 PDF vs PMF  
| PDF (Probability Density Function) | PMF (Probability Mass Function) |
|-----------------------------------|---------------------------------|
| Used for continuous RVs | Used for discrete RVs |
| Area under curve gives probability | Direct values are probabilities |

---

### 🔹 Binomial vs Poisson Distribution  
| Binomial | Poisson |
|----------|---------|
| Fixed number of trials | No fixed number of trials |
| Probability of success remains same | Rare events in a fixed interval |

---

### 🔹 Poisson vs Exponential  
| Poisson | Exponential |
|---------|-------------|
| Discrete distribution | Continuous distribution |
| Measures number of events | Measures time between events |

---

## 📘 **Unit IV: Hypothesis Testing & ANOVA**

### 🔹 One-tailed vs Two-tailed Test  
| One-tailed | Two-tailed |
|------------|------------|
| Checks deviation in one direction | Checks deviation in both directions |
| Critical region on one side | Critical regions on both sides |

---

### 🔹 Z-test vs t-test  
| Z-test | t-test |
|--------|--------|
| Known population SD, large sample ($n > 30$) | Unknown SD, small sample ($n < 30$) |
| Uses normal distribution | Uses t-distribution |

---

### 🔹 Parametric vs Non-parametric Test  
| Parametric | Non-parametric |
|------------|----------------|
| Assumes underlying distribution | No assumption of distribution |
| Example: Z-test, t-test | Example: Chi-square, Mann-Whitney |

---

### 🔹 One-way ANOVA vs Two-way ANOVA  
| One-way ANOVA | Two-way ANOVA |
|---------------|----------------|
| One factor/independent variable | Two factors |
| Tests difference between group means | Tests individual and interaction effects |

---

