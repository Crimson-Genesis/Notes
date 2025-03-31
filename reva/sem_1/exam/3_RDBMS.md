# RDBMS
## **Unit 2: ER Diagram and Database Design**
### **Entity-Relationship (ER) Model**  

The **Entity-Relationship (ER) model** is a conceptual framework used to design and visualize the structure of a database. It represents entities, their attributes, and the relationships between them.

---

## **1. Basic Components of ER Model**  

### **A. Entities**  
An **entity** is a real-world object that can have data stored in the database.  

📌 **Example:**  
- A **Student** is an entity in a university database.  
- A **Car** is an entity in a vehicle registration system.  

👉 **Types of Entities:**  
1. **Strong Entity:** Has a **primary key** to uniquely identify records.  
   - **Example:** "Student" with a **Student_ID** as the primary key.  
2. **Weak Entity:** Does not have a sufficient primary key and depends on a **strong entity**.  
   - **Example:** "Dependent" (child of an employee) relies on "Employee" for identification.  

---

### **B. Attributes**  
Attributes define the properties of an entity.  

📌 **Example:**  
For a **Student** entity, attributes can be:  
- **Student_ID** (Primary Key)  
- **Name**  
- **Date of Birth**  
- **Email**  

👉 **Types of Attributes:**  
1. **Simple Attribute:** Cannot be divided further (e.g., Age, Name).  
2. **Composite Attribute:** Can be divided into smaller attributes (e.g., "Full Name" into "First Name" and "Last Name").  
3. **Derived Attribute:** Computed from other attributes (e.g., "Age" derived from "Date of Birth").  
4. **Multi-valued Attribute:** Can have multiple values (e.g., "Phone Numbers" for a student).  

---

### **C. Keys**  
Keys uniquely identify an entity.  

📌 **Types of Keys:**  
1. **Primary Key (PK):** Uniquely identifies a record (e.g., Student_ID).  
2. **Candidate Key:** A set of attributes that can be a primary key.  
3. **Foreign Key (FK):** A reference to the primary key of another table.  
4. **Super Key:** A set of attributes that uniquely identify an entity but may have extra attributes.  

---

## **2. ER Diagram Representation**
An **ER Diagram** is a graphical representation of the database schema.  

### **Symbols in ER Diagram**
| Component | Symbol |
|-----------|--------|
| Entity | Rectangle 🟦 |
| Weak Entity | Double Rectangle ⏹️ |
| Attribute | Oval 🔵 |
| Relationship | Diamond ♦️ |
| Primary Key | Underlined Attribute |

📌 **Example ER Diagram: Student-Department**  

```
   +-------------+         +------------------+
   |  Student    |         |  Department      |
   |-------------|         |------------------|
   | Student_ID (PK)  ◄─── | Dept_ID (PK)     |
   | Name                |  | Dept_Name       |
   | DOB                 |  
   +-------------+         
        | (belongs to)   
        ▼  
  +----------------+
  |  Enrollment    |
  |----------------|
  | Student_ID (FK)|
  | Dept_ID (FK)   |
  | Year          |
  +----------------+
```

👉 Here,  
- **Student** and **Department** are entities.  
- **Enrollment** represents the **relationship** between students and departments.  

---
### **Entity Types, Attributes, and Keys**  

In the **ER model**, entities, attributes, and keys play a crucial role in designing a well-structured database. Let's go through them in detail.

---

## **1. Entity Types**  

An **entity type** defines a collection of similar entities that share the same attributes.  

📌 **Example:**  
- A **Student** entity type consists of individual students (John, Alice, etc.).
- An **Employee** entity type consists of different employees (E101, E102, etc.).

### **Types of Entity Types**  
1. **Strong Entity Type:**  
   - Can exist independently.  
   - Has a **primary key** that uniquely identifies each record.  
   - **Example:** "Student" entity with **Student_ID** as the primary key.  

2. **Weak Entity Type:**  
   - Cannot exist independently.  
   - Depends on a **strong entity** and has a **foreign key** reference.  
   - **Example:** "Dependent" (child of an employee) depends on "Employee."  

---

## **2. Attributes in ER Model**  

An **attribute** defines the properties of an entity. Each entity has a **set of attributes** associated with it.  

📌 **Example:**  
For an **Employee** entity, attributes can be:  
- **Employee_ID (PK)**  
- **Name**  
- **Date of Birth**  
- **Salary**  

### **Types of Attributes**  

| Attribute Type | Description | Example |
|---------------|------------|---------|
| **Simple Attribute** | Cannot be broken down further. | Age, Name |
| **Composite Attribute** | Can be divided into smaller attributes. | Full Name → First Name + Last Name |
| **Derived Attribute** | Computed from other attributes. | Age (calculated from Date of Birth) |
| **Multi-valued Attribute** | Can have multiple values. | Phone Numbers (Work, Personal) |
| **Stored Attribute** | Directly stored in the database. | Date of Birth |
| **Key Attribute** | Used to uniquely identify an entity. | Employee_ID |

📌 **Example of a Composite Attribute:**
```
Full Name → {First Name, Middle Name, Last Name}
```

📌 **Example of a Multi-valued Attribute:**
```
Phone Numbers → {+91-9876543210, +91-9123456789}
```

---

## **3. Keys in ER Model**  

### **A. Primary Key (PK)**  
- Uniquely identifies an entity.  
- **Example:** **Student_ID** in the Student table.  

### **B. Candidate Key**  
- A set of attributes that can be a primary key.  
- **Example:** A table with **Roll_No** and **Aadhar_No**—both can be candidate keys.  

### **C. Super Key**  
- A **set of attributes** that uniquely identifies a record.  
- It **may contain extra attributes** beyond the minimum required.  

📌 **Example of Super Key:**  
```
(Employee_ID, Email) → Can uniquely identify an Employee
```
But **Employee_ID** alone is enough, so it is a **Candidate Key**.

### **D. Foreign Key (FK)**  
- Establishes a relationship between two tables.  
- A foreign key in one table is a **primary key in another table**.  

📌 **Example:**  
In an **Order Table**, `Customer_ID` is a **foreign key** referencing `Customer(Customer_ID)`.  
```
Customer (Customer_ID, Name, Email)
Order (Order_ID, Order_Date, Customer_ID)  ← (FK)
```

---

## **ER Diagram Example with Keys**
### **Consider a University Database**
📌 **Entities:**
- **Student (Student_ID, Name, DOB, Phone)**
- **Course (Course_ID, Course_Name)**
- **Enrollment (Enroll_ID, Student_ID (FK), Course_ID (FK), Year)**

📌 **ER Diagram:**
```
   +-------------+         +------------------+
   |  Student    |         |  Course          |
   |-------------|         |------------------|
   | Student_ID (PK)  ◄─── | Course_ID (PK)   |
   | Name                |  | Course_Name     |
   | DOB                 |  
   +-------------+         
        | (Enrolls in)   
        ▼  
  +----------------+
  |  Enrollment    |
  |----------------|
  | Enroll_ID (PK) |
  | Student_ID (FK)|
  | Course_ID (FK) |
  | Year          |
  +----------------+
```

---
### **Generalization, Specialization, and Aggregation in ER Model**  

These concepts help in refining entity relationships by grouping or breaking down entities based on shared characteristics.

---

## **1. Generalization**  

📌 **Definition:**  
Generalization is the process of **combining multiple lower-level entities** into a single higher-level entity.  

🔹 **It moves from specific to general.**  
🔹 It reduces redundancy by capturing common features in a superclass.  

### **Example:**  
- Consider **Car, Bike, and Truck** as entities.  
- They share common attributes like **Vehicle_ID, Brand, and Color**.  
- Using **generalization**, we define a single entity **Vehicle** to represent all of them.  

📌 **ER Representation:**  
```
       +-----------------+
       |   Vehicle       |  ← Generalized Entity
       |-----------------|
       | Vehicle_ID (PK) |
       | Brand          |
       | Color          |
       +-----------------+
             ▲
    ------------------
    |       |        |
  Car     Bike    Truck
```
---
## **2. Specialization**  

📌 **Definition:**  
Specialization is the opposite of generalization. It **divides a higher-level entity** into two or more lower-level entities based on unique characteristics.  

🔹 **It moves from general to specific.**  
🔹 Each specialized entity inherits attributes from the general entity.  

### **Example:**  
- A **Person** can be a **Student** or an **Employee**.  
- Both have attributes like **Name, Age, and Address**.  
- But **Students** have **Roll_No**, and **Employees** have **Employee_ID**.  

📌 **ER Representation:**  
```
             +----------------+
             |   Person       |
             |----------------|
             | Person_ID (PK) |
             | Name          |
             | Age           |
             +----------------+
                  ▲
         -------------------
         |                 |
    +------------+   +------------+
    |  Student   |   |  Employee  |
    |------------|   |------------|
    | Roll_No (PK)|   | Emp_ID (PK) |
    +------------+   +------------+
```
---
## **3. Aggregation**  

📌 **Definition:**  
Aggregation is the process of **treating a relationship as an entity**.  
🔹 Used when a relationship itself needs attributes.  

### **Example:**  
- Consider **a doctor treating multiple patients in a hospital.**  
- The **Treats** relationship between **Doctor** and **Patient** needs an attribute like **Treatment_Date**.  
- We create a new entity **Treatment** to store additional information.

📌 **ER Representation:**  
```
      +------------+          +------------+
      |  Doctor    |          |  Patient   |
      |------------|          |------------|
      | Doc_ID (PK)|          | Pat_ID (PK)|
      +------------+          +------------+
             \                      /
              \    +---------------+
               ----|   Treatment   |  ← Aggregated Entity
                   |---------------|
                   | Treatment_Date |
                   +---------------+
```

---

### **Comparison Table**

| Concept          | Direction  | Example |
|-----------------|------------|---------|
| **Generalization** | Bottom-up (Specific → General) | **Car, Bike → Vehicle** |
| **Specialization** | Top-down (General → Specific) | **Person → Student, Employee** |
| **Aggregation** | Relationship as an Entity | **Doctor treats Patient → Treatment** |

---
### **Functional Dependencies & Multi-Valued Dependencies**  

These concepts help in understanding data relationships within a database and play a crucial role in **Normalization**.  

---

## **1. Functional Dependencies (FDs)**  

📌 **Definition:**  
A functional dependency (FD) **describes the relationship between attributes in a relation**. If **X → Y**, then **X uniquely determines Y**.  

🔹 It ensures **data consistency** and **reduces redundancy**.  
🔹 Used for **Normalization (1NF, 2NF, 3NF, BCNF, etc.)**.  

### **Example:**  
Consider a **Student table:**  

| Roll_No (X) | Name (Y)  | Dept (Z)  |  
|-------------|----------|----------|  
| 101         | Alice    | CSE      |  
| 102         | Bob      | ECE      |  
| 103         | Charlie  | CSE      |  

Here,  
- **Roll_No → Name** (Each Roll_No has exactly one Name)  
- **Roll_No → Dept** (Each Roll_No belongs to exactly one Dept)  

**So,** `Roll_No → {Name, Dept}` (Roll_No functionally determines both Name and Dept).  

📌 **Types of Functional Dependencies:**  
1️⃣ **Trivial FD:** If **Y ⊆ X**, then `X → Y` is trivial.  
   - Example: `{Roll_No, Name} → Name` (because Name is already in X).  

2️⃣ **Non-Trivial FD:** If **Y is NOT a subset of X**, then `X → Y` is non-trivial.  
   - Example: `Roll_No → Dept`  

3️⃣ **Transitive FD:** If `X → Y` and `Y → Z`, then `X → Z`.  
   - Example: `Roll_No → Dept` and `Dept → HOD`, so `Roll_No → HOD`.  

---

## **2. Multi-Valued Dependencies (MVDs)**  

📌 **Definition:**  
A **Multi-Valued Dependency (MVD)** occurs when **one attribute in a table determines multiple independent values of another attribute**.  

🔹 Occurs in cases where one attribute **determines multiple values of another, independently of other attributes**.  
🔹 Used to identify **4NF violations** and remove redundancy.  

### **Example:**  
Consider a **Student table** where each student can have multiple **Phone Numbers** and **Email IDs**.  

| Roll_No | Phone         | Email            |  
|---------|--------------|------------------|  
| 101     | 9876543210   | alice@mail.com   |  
| 101     | 8765432109   | alice@mail.com   |  
| 101     | 9876543210   | alice@uni.com    |  

Here,  
- **Roll_No →→ Phone** (A student can have multiple Phone Numbers).  
- **Roll_No →→ Email** (A student can have multiple Email IDs).  

📌 **Rule:** **MVD exists when for a given X, Y values are independent of Z values**.  

💡 **Solution:** Split into two separate tables:  

**Student_Phone Table:**  

| Roll_No | Phone         |  
|---------|--------------|  
| 101     | 9876543210   |  
| 101     | 8765432109   |  

**Student_Email Table:**  

| Roll_No | Email            |  
|---------|------------------|  
| 101     | alice@mail.com   |  
| 101     | alice@uni.com    |  

🔹 **Now, redundancy is removed, and the database is in 4NF.**  

---

### **Key Differences:**

| Functional Dependency (FD) | Multi-Valued Dependency (MVD) |
|--------------------------|----------------------------|
| Ensures **one-to-one** relationship | Ensures **one-to-many** relationship |
| Helps in **3NF, BCNF** | Helps in **4NF** |
| Example: `Roll_No → Name` | Example: `Roll_No →→ Phone` |

---
## **Normalization: 1NF, 2NF, 3NF, BCNF, 4NF**  

🔹 **Normalization** is the process of organizing data in a database to reduce **redundancy** and improve **data integrity**.  
🔹 It involves decomposing a table into smaller tables **without losing information**.  

---

## **1. First Normal Form (1NF)**
📌 **Rule:** **Eliminate Repeating Groups**  
- A table is in **1NF** if **all attributes contain atomic (indivisible) values**.  
- Each column must contain **only single values** (no multiple values or arrays).  

### ❌ **Violating 1NF:**  
| Student_ID | Name  | Phone Numbers     |  
|-----------|------|----------------|  
| 101       | Alice | 9876543210, 8765432109 |  
| 102       | Bob   | 9876543211 |  

Here, **Phone Numbers** contain multiple values → **NOT in 1NF**.  

### ✅ **Convert to 1NF:**  
| Student_ID | Name  | Phone Number  |  
|-----------|------|-------------|  
| 101       | Alice | 9876543210  |  
| 101       | Alice | 8765432109  |  
| 102       | Bob   | 9876543211  |  

---

## **2. Second Normal Form (2NF)**
📌 **Rule:** **Eliminate Partial Dependencies**  
- A table is in **2NF** if it is in **1NF** and **all non-key attributes depend on the entire primary key**.  
- It removes **partial dependencies** (where a non-key attribute depends on only a part of a composite key).  

### ❌ **Violating 2NF:**  
| Order_ID | Product_ID | Product_Name | Quantity |  
|---------|-----------|-------------|---------|  
| 1       | P001      | Laptop      | 2       |  
| 1       | P002      | Mouse       | 1       |  

🔹 **Problem:**  
- **Primary Key:** `(Order_ID, Product_ID)`  
- `Product_Name` depends **only on Product_ID**, not on `Order_ID`. → **Partial Dependency**  

### ✅ **Convert to 2NF:**  
🔹 **Decompose into two tables:**  

**Orders Table:**  
| Order_ID | Product_ID | Quantity |  
|---------|-----------|---------|  
| 1       | P001      | 2       |  
| 1       | P002      | 1       |  

**Products Table:**  
| Product_ID | Product_Name |  
|-----------|-------------|  
| P001      | Laptop      |  
| P002      | Mouse       |  

---

## **3. Third Normal Form (3NF)**
📌 **Rule:** **Eliminate Transitive Dependencies**  
- A table is in **3NF** if it is in **2NF** and **there are no transitive dependencies**.  
- Transitive Dependency: If `A → B` and `B → C`, then `A → C` (indirect dependency).  

### ❌ **Violating 3NF:**  
| Employee_ID | Employee_Name | Dept_ID | Dept_Name |  
|-----------|--------------|--------|----------|  
| 101       | Alice        | D01    | HR       |  
| 102       | Bob          | D02    | IT       |  

🔹 **Problem:**  
- **Primary Key:** `Employee_ID`  
- `Dept_Name` depends on `Dept_ID`, not directly on `Employee_ID`.  
- `Employee_ID → Dept_ID` and `Dept_ID → Dept_Name`, so **Employee_ID → Dept_Name** (transitive dependency).  

### ✅ **Convert to 3NF:**  
🔹 **Decompose into two tables:**  

**Employees Table:**  
| Employee_ID | Employee_Name | Dept_ID |  
|-----------|--------------|--------|  
| 101       | Alice        | D01    |  
| 102       | Bob          | D02    |  

**Departments Table:**  
| Dept_ID | Dept_Name |  
|--------|----------|  
| D01    | HR       |  
| D02    | IT       |  

---

## **4. Boyce-Codd Normal Form (BCNF)**
📌 **Rule:** **Every determinant must be a candidate key**  
- A table is in **BCNF** if it is in **3NF**, and **every determinant is a candidate key**.  
- **Stronger than 3NF**, used when **one non-trivial FD violates the candidate key rule**.  

### ❌ **Violating BCNF:**  
| Student_ID | Course | Instructor |  
|-----------|--------|------------|  
| 101       | Math   | Prof. A    |  
| 101       | CS     | Prof. B    |  

🔹 **Problem:**  
- **Primary Key:** `(Student_ID, Course)`  
- **Instructor → Course**, but Instructor is not a candidate key → **BCNF violation**  

### ✅ **Convert to BCNF:**  
🔹 **Decompose into two tables:**  

**Student_Course Table:**  
| Student_ID | Course |  
|-----------|--------|  
| 101       | Math   |  
| 101       | CS     |  

**Course_Instructor Table:**  
| Course | Instructor |  
|--------|------------|  
| Math   | Prof. A    |  
| CS     | Prof. B    |  

---

## **5. Fourth Normal Form (4NF)**
📌 **Rule:** **Eliminate Multi-Valued Dependencies**  
- A table is in **4NF** if it is in **BCNF** and **contains no multi-valued dependencies**.  

### ❌ **Violating 4NF:**  
| Student_ID | Course | Hobby |  
|-----------|--------|-------|  
| 101       | Math   | Chess |  
| 101       | Math   | Music |  

🔹 **Problem:**  
- **Multi-Valued Dependency:** A student has multiple hobbies **independent of the course**.  

### ✅ **Convert to 4NF:**  
🔹 **Decompose into two tables:**  

**Student_Course Table:**  
| Student_ID | Course |  
|-----------|--------|  
| 101       | Math   |  

**Student_Hobby Table:**  
| Student_ID | Hobby |  
|-----------|-------|  
| 101       | Chess |  
| 101       | Music |  

---

## **Summary of Normal Forms**

| Normal Form | Rule |
|------------|------|
| **1NF** | No repeating groups (Atomic values only) |
| **2NF** | No **partial** dependency (All non-key attributes depend on the whole primary key) |
| **3NF** | No **transitive** dependency (No indirect dependencies) |
| **BCNF** | Every **determinant** is a candidate key |
| **4NF** | No **multi-valued dependencies** |

---
## **Lossless Decomposition & Dependency Preservation**  

When we normalize a database, we **split tables** to remove redundancy while maintaining the original data integrity. Two essential properties in decomposition are:  

1️⃣ **Lossless (Non-Loss) Decomposition**  
2️⃣ **Dependency Preservation**  

---

## **1. Lossless (Non-Loss) Decomposition**  
📌 **Definition:** A decomposition is **lossless** if we can **reconstruct** the original table **without losing any information** after decomposition.  

🔹 **Lossless decomposition ensures that when we join decomposed tables, we get back the original relation.**  

### **Example of Lossless Decomposition**  
Consider a relation **R(Student_ID, Name, Course, Instructor)** with the following **functional dependencies**:  
- `Student_ID → Name`  
- `Course → Instructor`  

If we decompose `R` into:  
1. **R1(Student_ID, Name)**  
2. **R2(Student_ID, Course, Instructor)**  

🔹 When we **JOIN R1 and R2**, we get back the **original relation R** → **Lossless Decomposition** ✅  

✅ **Conditions for Lossless Decomposition:**  
A decomposition `{R1, R2}` of `R` is **lossless** if:  
- `R1 ∩ R2` contains a **candidate key** of `R`.  

🔹 **Mathematical condition:**  
If `R` is decomposed into `R1` and `R2`, then `R1 ∩ R2 → R1` OR `R1 ∩ R2 → R2` must hold.  

---

## **2. Dependency Preservation**  
📌 **Definition:** Dependency preservation means that **all functional dependencies** from the original table are **preserved** after decomposition **without needing joins**.  

🔹 If we decompose a table into `R1, R2, ...`, we should be able to enforce the **original dependencies** on individual tables **without** recombining them.  

### **Example of Dependency Preservation**  
Consider a relation **R(Employee_ID, Name, Dept_ID, Dept_Name)** with dependencies:  
- `Employee_ID → Name, Dept_ID`  
- `Dept_ID → Dept_Name`  

If we decompose `R` into:  
1. **R1(Employee_ID, Name, Dept_ID)**  
2. **R2(Dept_ID, Dept_Name)**  

✅ **Dependency Preservation:**  
- `Employee_ID → Name, Dept_ID` is in `R1`  
- `Dept_ID → Dept_Name` is in `R2`  
🔹 **All dependencies are preserved** → **Dependency Preservation achieved!** ✅  

---

## **Lossless vs. Dependency Preservation**
| Property | Definition | Importance |
|----------|------------|------------|
| **Lossless Decomposition** | Ensures no data is lost when splitting a table | Required for correctness |
| **Dependency Preservation** | Ensures all functional dependencies are maintained after decomposition | Helps in enforcing constraints without joins |

---

### **Can a Decomposition be Lossless but Not Dependency-Preserving?**  
Yes! A decomposition can be **lossless** but **not dependency-preserving** if some functional dependencies are lost and require joins to enforce them.  

🔹 Example: Suppose we decompose `R(A, B, C)` with `A → B` and `B → C` into:  
1. **R1(A, B)**  
2. **R2(B, C)**  

✅ This decomposition is **lossless** (since `B` acts as a key in both tables).  
❌ But **it is not dependency-preserving** because we lost `A → C`, which must be checked by **joining R1 and R2**.  

---

## **Conclusion**
✔ **A good decomposition should be both Lossless & Dependency-Preserving.**  
✔ **Sometimes we may need to compromise dependency preservation to achieve lossless decomposition.**  

---
## **Indexing in Databases (B+ Trees, Hash Indexing)**  

Indexing improves **query performance** by reducing the amount of data that needs to be scanned. The two common types of indexing are:  
1️⃣ **B+ Tree Indexing** (Ordered Indexing)  
2️⃣ **Hash Indexing** (Unordered Indexing)  

---

## **1. B+ Tree Indexing**  
📌 **Definition:** A **B+ Tree** is a **self-balancing** tree structure used for indexing in databases.  

✅ **Why B+ Trees?**  
- **Efficient search, insert, delete operations** in **O(log n)** time.  
- **Balanced structure** → No node is too deep.  
- **Sequential access** is fast because **all data is stored at leaf nodes**.  
- Used in **multi-level indexing** (B-trees extendable to large databases).  

---

### **📌 Structure of a B+ Tree**  
- **Internal Nodes** → Store **only keys** (guide search).  
- **Leaf Nodes** → Store **actual data** and are **linked together**.  
- **Every leaf node has a pointer to the next leaf node** → Supports **range queries** efficiently.  

#### **Example of a B+ Tree (Order 3)**
```
         [30 | 60]
        /        \
   [10 | 20]   [30 | 40 | 50]   [60 | 70 | 80]
```
- Internal nodes only contain **keys** (not data).
- Leaf nodes contain **actual data values** in sorted order.

✅ **Operations on B+ Trees:**  
- **Insertion:** Adds a key to the correct leaf node; may cause **splitting** if full.  
- **Deletion:** Removes a key; may cause **merging** if underfull.  
- **Search:** Follows the tree structure **from root to leaves** (O(log n)).  
- **Range Queries:** Fast due to **linked leaf nodes**.  

📌 **Where is B+ Tree Used?**  
- Used in **databases (MySQL, PostgreSQL)**  
- **File systems (NTFS, HFS+ on Mac)**  

---

## **2. Hash Indexing**  
📌 **Definition:** Hash Indexing uses a **hash function** to compute the location of a record **directly** in memory.  

✅ **Why Hash Indexing?**  
- **Fast lookups (O(1) on average)**.  
- Used for **equality searches** (e.g., "Find Employee_ID = 123").  
- **Not efficient for range queries** (no ordering).  

---

### **📌 How Hash Indexing Works?**  
1️⃣ A **hash function** takes a key as input and computes a **hash value**.  
2️⃣ This hash value maps to a **bucket** in the index table.  
3️⃣ The bucket stores **pointers** to actual records.  

#### **Example of Hashing (Employee Table)**
```
Key: Employee_ID → Hash Function → Bucket in Hash Table
```
| Employee_ID | Hash Function | Hash Bucket |
|------------|--------------|------------|
| 101        | h(101) = 2   | Bucket 2   |
| 202        | h(202) = 4   | Bucket 4   |
| 303        | h(303) = 1   | Bucket 1   |

✅ **Operations on Hash Indexing:**  
- **Insertion:** Compute hash → Insert into corresponding bucket.  
- **Search:** Compute hash → Find bucket → Retrieve record.  
- **Deletion:** Compute hash → Remove from bucket.  

---

## **📌 B+ Tree vs. Hash Indexing**
| Feature | B+ Tree Indexing | Hash Indexing |
|---------|-----------------|--------------|
| **Efficiency** | O(log n) | O(1) (average case) |
| **Best for** | **Range queries**, ordered searches | **Equality searches** |
| **Structure** | Tree (Hierarchical) | Hash table (Key-Value) |
| **Supports Range Queries?** | ✅ Yes | ❌ No |
| **Insertion/Deletion Complexity** | Moderate | Fast |

✅ **When to Use What?**  
- **Use B+ Trees** when range-based searching is needed.  
- **Use Hash Indexing** when only direct lookups (equality conditions) are required.  

---

### **🔹 Conclusion**
✔ **B+ Trees** are best for **ordered searches & range queries**.  
✔ **Hash Indexing** is best for **direct key lookups** but does **not support range queries**.  

---

##  **Unit 4: SQL & PL/SQL**
## **SQL Functions: Aggregate, Numeric, Date, and String Functions**  

SQL functions help perform calculations, format data, and manipulate strings, numbers, and dates.  

---

## **1️⃣ Aggregate Functions**  
📌 **Definition:** Aggregate functions operate on multiple rows and return a **single summarized value**.  

| Function | Description | Example |
|----------|------------|---------|
| **COUNT()** | Returns the number of rows | `SELECT COUNT(*) FROM employees;` |
| **SUM()** | Returns the total sum | `SELECT SUM(salary) FROM employees;` |
| **AVG()** | Returns the average value | `SELECT AVG(salary) FROM employees;` |
| **MAX()** | Returns the maximum value | `SELECT MAX(salary) FROM employees;` |
| **MIN()** | Returns the minimum value | `SELECT MIN(salary) FROM employees;` |

✅ **Example:**  
```sql
SELECT department, COUNT(*) AS total_employees, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department;
```
☑ Groups employees by department and calculates the **count and average salary**.

---

## **2️⃣ Numeric Functions**  
📌 **Definition:** Numeric functions perform operations on **numerical values**.  

| Function | Description | Example |
|----------|------------|---------|
| **ABS(x)** | Absolute value | `SELECT ABS(-10);` → **10** |
| **ROUND(x, d)** | Rounds x to d decimal places | `SELECT ROUND(3.14159, 2);` → **3.14** |
| **CEIL(x)** | Rounds x up to the nearest integer | `SELECT CEIL(4.3);` → **5** |
| **FLOOR(x)** | Rounds x down to the nearest integer | `SELECT FLOOR(4.9);` → **4** |
| **MOD(x, y)** | Returns remainder (x % y) | `SELECT MOD(10, 3);` → **1** |
| **POWER(x, y)** | x raised to power y | `SELECT POWER(2, 3);` → **8** |

✅ **Example:**  
```sql
SELECT name, salary, CEIL(salary) AS rounded_salary 
FROM employees;
```
☑ Rounds salary up to the nearest integer.

---

## **3️⃣ Date Functions**  
📌 **Definition:** Date functions help manipulate **dates and time values**.  

| Function | Description | Example |
|----------|------------|---------|
| **CURRENT_DATE()** | Returns today’s date | `SELECT CURRENT_DATE();` |
| **CURRENT_TIME()** | Returns current time | `SELECT CURRENT_TIME();` |
| **NOW()** | Returns current date and time | `SELECT NOW();` |
| **DATE_ADD(date, INTERVAL x unit)** | Adds time to a date | `SELECT DATE_ADD('2025-03-31', INTERVAL 10 DAY);` |
| **DATE_SUB(date, INTERVAL x unit)** | Subtracts time from a date | `SELECT DATE_SUB('2025-03-31', INTERVAL 1 MONTH);` |
| **DATEDIFF(date1, date2)** | Returns difference in days | `SELECT DATEDIFF('2025-03-31', '2025-03-01');` |
| **DAYNAME(date)** | Returns weekday name | `SELECT DAYNAME('2025-03-31');` → **Monday** |

✅ **Example:**  
```sql
SELECT name, hire_date, DATEDIFF(CURRENT_DATE(), hire_date) AS days_worked
FROM employees;
```
☑ Finds how many days an employee has worked.

---

## **4️⃣ String Functions**  
📌 **Definition:** String functions manipulate **character/text data**.  

| Function | Description | Example |
|----------|------------|---------|
| **LENGTH(str)** | Returns string length | `SELECT LENGTH('Hello');` → **5** |
| **UPPER(str)** | Converts to uppercase | `SELECT UPPER('hello');` → **HELLO** |
| **LOWER(str)** | Converts to lowercase | `SELECT LOWER('HELLO');` → **hello** |
| **SUBSTRING(str, start, length)** | Extracts part of a string | `SELECT SUBSTRING('HelloWorld', 1, 5);` → **Hello** |
| **CONCAT(str1, str2)** | Joins two strings | `SELECT CONCAT('Hello', 'World');` → **HelloWorld** |
| **TRIM(str)** | Removes spaces | `SELECT TRIM('  Hello  ');` → **Hello** |
| **REPLACE(str, old, new)** | Replaces substring | `SELECT REPLACE('HelloWorld', 'World', 'SQL');` → **HelloSQL** |

✅ **Example:**  
```sql
SELECT name, UPPER(name) AS uppercase_name, LENGTH(name) AS name_length
FROM employees;
```
☑ Converts names to uppercase and finds name length.

---

## **🔹 Summary**
✔ **Aggregate Functions** → Used for calculations on multiple rows (**SUM, COUNT, AVG, MIN, MAX**).  
✔ **Numeric Functions** → Perform mathematical operations (**ABS, ROUND, CEIL, FLOOR**).  
✔ **Date Functions** → Work with dates and time (**CURRENT_DATE, DATE_ADD, DATEDIFF**).  
✔ **String Functions** → Manipulate text values (**LENGTH, UPPER, LOWER, CONCAT, TRIM**).  

---
## **Set Operations in SQL (UNION, INTERSECT, MINUS)**  

SQL **set operations** combine results from multiple queries, treating them as sets. The key operations are:  

- **UNION** → Combines results and removes duplicates  
- **UNION ALL** → Combines results and keeps duplicates  
- **INTERSECT** → Returns common records  
- **MINUS (EXCEPT in some databases)** → Returns records in one set but not the other  

---

## **1️⃣ UNION & UNION ALL**  
📌 **Definition:** Combines results from two queries with the same number of columns and data types.  

| Operator | Removes Duplicates? | Example |
|----------|---------------------|---------|
| **UNION** | ✅ Yes | `SELECT name FROM students UNION SELECT name FROM teachers;` |
| **UNION ALL** | ❌ No | `SELECT name FROM students UNION ALL SELECT name FROM teachers;` |

✅ **Example:**  
```sql
SELECT name FROM students
UNION
SELECT name FROM teachers;
```
☑ Returns a list of unique names from both tables.  

```sql
SELECT name FROM students
UNION ALL
SELECT name FROM teachers;
```
☑ Returns all names, including duplicates.  

---

## **2️⃣ INTERSECT**  
📌 **Definition:** Returns only the **common records** between two queries.  

✅ **Example:**  
```sql
SELECT name FROM students
INTERSECT
SELECT name FROM teachers;
```
☑ Returns names that are present in **both** tables.  

⛔ **Note:** `INTERSECT` is not supported in MySQL but works in PostgreSQL, Oracle, and SQL Server. MySQL alternative:  
```sql
SELECT name FROM students 
WHERE name IN (SELECT name FROM teachers);
```

---

## **3️⃣ MINUS (EXCEPT in SQL Server & PostgreSQL)**  
📌 **Definition:** Returns records in the **first query** but **not in the second query**.  

✅ **Example:**  
```sql
SELECT name FROM students
MINUS
SELECT name FROM teachers;
```
☑ Returns names that exist in **students** but not in **teachers**.  

⛔ **MySQL Alternative:**  
```sql
SELECT name FROM students 
WHERE name NOT IN (SELECT name FROM teachers);
```

---

## **🔹 Summary**
✔ **UNION** → Combines results, removes duplicates  
✔ **UNION ALL** → Combines results, keeps duplicates  
✔ **INTERSECT** → Returns common rows  
✔ **MINUS (EXCEPT in SQL Server & PostgreSQL)** → Returns unique rows from the first query  

---
## **Joins in SQL (Inner Join, Outer Join, Natural Join, Self Join)**  

Joins are used to **combine data from multiple tables** based on a related column.  

---

### **1️⃣ INNER JOIN**  
📌 **Definition:** Returns only the matching rows between two tables based on a common column.  

✅ **Example:**  
```sql
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.course_id = courses.course_id;
```
☑ This retrieves only students **who are enrolled in a course**.  

📝 **Key Points:**  
- Excludes unmatched rows from both tables.  
- Requires a common key (`course_id` in this case).  

---

### **2️⃣ OUTER JOIN**  
📌 **Definition:** Returns **matching records + unmatched records** from one or both tables.  
There are **three types** of outer joins:  

#### **🔹 LEFT OUTER JOIN (or LEFT JOIN)**  
📌 Returns **all records** from the left table + matching records from the right table.  

✅ **Example:**  
```sql
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses ON students.course_id = courses.course_id;
```
☑ Returns all students, even those **not enrolled in any course** (with `NULL` values for `course_name`).  

#### **🔹 RIGHT OUTER JOIN (or RIGHT JOIN)**  
📌 Returns **all records** from the right table + matching records from the left table.  

✅ **Example:**  
```sql
SELECT students.name, courses.course_name
FROM students
RIGHT JOIN courses ON students.course_id = courses.course_id;
```
☑ Returns all courses, even those **with no students enrolled** (with `NULL` values for `name`).  

#### **🔹 FULL OUTER JOIN**  
📌 Returns **all records** from both tables, filling `NULL` where there’s no match.  

✅ **Example:**  
```sql
SELECT students.name, courses.course_name
FROM students
FULL OUTER JOIN courses ON students.course_id = courses.course_id;
```
☑ Shows **all students and all courses**, including those that have no matches.  
⛔ **Not supported in MySQL** (use `LEFT JOIN` + `RIGHT JOIN` with `UNION`).  

---

### **3️⃣ NATURAL JOIN**  
📌 **Definition:** A join that **automatically matches columns** with the **same name and data type** in both tables.  

✅ **Example:**  
```sql
SELECT students.name, courses.course_name
FROM students
NATURAL JOIN courses;
```
☑ If both tables have `course_id`, it automatically joins using that column.  
🚨 **Risk:** If column names change, the query may break.  

---

### **4️⃣ SELF JOIN**  
📌 **Definition:** A join where a table is joined **with itself**.  

✅ **Example:** Find employees and their managers from the same `employees` table:  
```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;
```
☑ Matches employees (`e1`) with their managers (`e2`).  

---

## **🔹 Summary**
✔ **INNER JOIN** → Only matching records  
✔ **LEFT JOIN** → All left-table records + matching right-table records  
✔ **RIGHT JOIN** → All right-table records + matching left-table records  
✔ **FULL JOIN** → All records from both tables  
✔ **NATURAL JOIN** → Automatic column matching  
✔ **SELF JOIN** → Join within the same table  

---
## **Subqueries and Nested Queries in SQL**  

📌 **Definition:**  
A **subquery** (or **nested query**) is a query inside another query. It helps in fetching results dynamically based on another query.  

---

### **1️⃣ Types of Subqueries**
SQL subqueries can be categorized into:  
✅ **Single-row subqueries** → Returns **one value**  
✅ **Multi-row subqueries** → Returns **multiple values**  
✅ **Correlated subqueries** → Uses outer query values for each row  

---

### **2️⃣ Single-Row Subqueries**  
Returns **one value** (e.g., a single `MAX`, `COUNT`, or specific row).  

✅ **Example:** Find the student **with the highest marks**  
```sql
SELECT name FROM students  
WHERE marks = (SELECT MAX(marks) FROM students);
```
☑ **Explanation:** The inner query finds the `MAX(marks)`, and the outer query selects the student.  

---

### **3️⃣ Multi-Row Subqueries**  
Returns **multiple values** (used with `IN`, `ANY`, `ALL`).  

✅ **Example:** Find students **enrolled in any course offered by 'CS Department'**  
```sql
SELECT name FROM students  
WHERE course_id IN (SELECT course_id FROM courses WHERE department = 'CS');
```
☑ **Explanation:** The subquery fetches `course_id`s from CS, and the main query selects students with those `course_id`s.  

📌 **Using `ANY` and `ALL`**  
✅ **Example:** Find students **with marks greater than the lowest mark in Class A**  
```sql
SELECT name FROM students  
WHERE marks > ANY (SELECT marks FROM students WHERE class = 'A');
```
☑ **ANY** → Compares against **any single value** from the subquery results.  
☑ **ALL** → Requires the condition to be **true for all values** returned.  

---

### **4️⃣ Correlated Subqueries**  
Uses values from the outer query for **each row** in the subquery.  

✅ **Example:** Find students who have **higher marks than the average marks of their own class**  
```sql
SELECT name FROM students s1  
WHERE marks > (SELECT AVG(marks) FROM students s2 WHERE s1.class = s2.class);
```
☑ **Explanation:** The subquery calculates the average for **each class separately**.  

---

## **🔹 Summary**
✔ **Single-row subquery** → `=, >, <` operators (returns **one** value)  
✔ **Multi-row subquery** → `IN, ANY, ALL` operators (returns **multiple** values)  
✔ **Correlated subquery** → Executes for **each row** in the outer query  

---
## **Transactions & ACID Properties**  

📌 **Definition:**  
A **transaction** in a database is a sequence of one or more SQL statements executed as a **single unit of work**. It ensures data consistency, integrity, and reliability.  

---

### **1️⃣ Transaction Control Commands**
SQL provides commands to manage transactions:  
✅ `COMMIT` → Saves all changes permanently  
✅ `ROLLBACK` → Reverts all changes since the last `COMMIT`  
✅ `SAVEPOINT` → Creates a point in a transaction to **rollback partially**  

---

### **2️⃣ ACID Properties of Transactions**
To ensure reliability, transactions follow **ACID** principles:  

| **Property** | **Description** | **Example** |
|-------------|----------------|-------------|
| **A**tomicity | Transaction is **all or nothing** | If a money transfer fails, no partial deduction should happen. |
| **C**onsistency | Database remains in a **valid state** | A record can’t violate constraints (e.g., a negative balance). |
| **I**solation | Transactions execute **independently** | Two users transferring money don’t interfere with each other. |
| **D**urability | Changes are **permanent** after `COMMIT` | Once transferred, money **stays transferred** even after failure. |

---

### **3️⃣ Example of Transaction Control**
✅ **Example:** Money Transfer Between Two Accounts  
```sql
START TRANSACTION;  

UPDATE accounts SET balance = balance - 500 WHERE account_id = 1;  
UPDATE accounts SET balance = balance + 500 WHERE account_id = 2;  

COMMIT;  -- Saves the transaction permanently
```
☑ **Explanation:** If any of the `UPDATE` statements fail, the transaction won’t be committed.  

---

### **4️⃣ Using `ROLLBACK` and `SAVEPOINT`**
✅ **Example:** Using `SAVEPOINT` for partial rollback  
```sql
START TRANSACTION;  

UPDATE accounts SET balance = balance - 500 WHERE account_id = 1;  
SAVEPOINT before_transfer;  

UPDATE accounts SET balance = balance + 500 WHERE account_id = 2;  

ROLLBACK TO before_transfer;  -- Undo only the second update  
COMMIT;  -- Saves the first update  
```
☑ **Explanation:** The rollback **undoes only the last update**, keeping the first intact.  

---

## **🔹 Summary**
✔ **ACID** ensures reliability (**Atomicity, Consistency, Isolation, Durability**)  
✔ `COMMIT` → Saves changes permanently  
✔ `ROLLBACK` → Undoes changes (since last `COMMIT`)  
✔ `SAVEPOINT` → Allows partial rollback  

---
## **PL/SQL (Procedural SQL Programming)**  

📌 **Definition:**  
PL/SQL (Procedural Language for SQL) is an **extension of SQL** that allows procedural programming features like loops, conditions, and exception handling.  

---

### **1️⃣ PL/SQL Block Structure**  
A PL/SQL program consists of **four sections**:  

```plsql
DECLARE  
   -- Declaration section (Variables, Cursors, Exceptions)  
BEGIN  
   -- Execution section (SQL statements, loops, conditions)  
EXCEPTION  
   -- Exception handling section (Handling runtime errors)  
END;  
```

---

### **2️⃣ Variables in PL/SQL**
✅ Declaring variables:  
```plsql
DECLARE  
   emp_name VARCHAR2(50);  
   emp_salary NUMBER(10,2);  
BEGIN  
   emp_name := 'John';  
   emp_salary := 50000;  
END;
```
☑ **Explanation:** `VARCHAR2(50)` stores a string up to 50 characters, and `NUMBER(10,2)` stores a decimal number.  

---

### **3️⃣ Control Structures (IF, CASE, Loops)**  

✅ **IF-ELSE Condition**  
```plsql
DECLARE  
   salary NUMBER := 60000;  
BEGIN  
   IF salary > 50000 THEN  
      DBMS_OUTPUT.PUT_LINE('High Salary');  
   ELSE  
      DBMS_OUTPUT.PUT_LINE('Low Salary');  
   END IF;  
END;
```

✅ **CASE Statement**  
```plsql
DECLARE  
   grade CHAR(1) := 'A';  
BEGIN  
   CASE grade  
      WHEN 'A' THEN DBMS_OUTPUT.PUT_LINE('Excellent');  
      WHEN 'B' THEN DBMS_OUTPUT.PUT_LINE('Good');  
      ELSE DBMS_OUTPUT.PUT_LINE('Needs Improvement');  
   END CASE;  
END;
```

✅ **Loop Example (FOR Loop)**  
```plsql
BEGIN  
   FOR i IN 1..5 LOOP  
      DBMS_OUTPUT.PUT_LINE('Iteration: ' || i);  
   END LOOP;  
END;
```
☑ **Explanation:** Loops **repeat actions** multiple times until a condition is met.  

---

### **4️⃣ Cursors in PL/SQL**  
📌 **Definition:** A **cursor** is a temporary memory area that allows row-by-row processing of query results.  

✅ **Implicit Cursor Example** (Automatic for `SELECT INTO`)  
```plsql
DECLARE  
   emp_name employees.name%TYPE;  
BEGIN  
   SELECT name INTO emp_name FROM employees WHERE emp_id = 101;  
   DBMS_OUTPUT.PUT_LINE('Employee Name: ' || emp_name);  
END;
```

✅ **Explicit Cursor Example** (Manual control over fetching rows)  
```plsql
DECLARE  
   CURSOR emp_cursor IS SELECT name FROM employees;  
   emp_name employees.name%TYPE;  
BEGIN  
   OPEN emp_cursor;  
   LOOP  
      FETCH emp_cursor INTO emp_name;  
      EXIT WHEN emp_cursor%NOTFOUND;  
      DBMS_OUTPUT.PUT_LINE('Employee: ' || emp_name);  
   END LOOP;  
   CLOSE emp_cursor;  
END;
```
☑ **Explanation:** `OPEN`, `FETCH`, and `CLOSE` manually control data retrieval.  

---

### **5️⃣ Exception Handling in PL/SQL**  
📌 **Definition:** PL/SQL exceptions **handle runtime errors** like division by zero, invalid data, or constraint violations.  

✅ **Predefined Exception Example (`ZERO_DIVIDE`)**  
```plsql
DECLARE  
   num NUMBER := 10;  
   result NUMBER;  
BEGIN  
   result := num / 0;  -- Causes error  
EXCEPTION  
   WHEN ZERO_DIVIDE THEN  
      DBMS_OUTPUT.PUT_LINE('Error: Division by zero!');  
END;
```

✅ **User-Defined Exception Example**  
```plsql
DECLARE  
   emp_not_found EXCEPTION;  
BEGIN  
   IF (SELECT COUNT(*) FROM employees WHERE emp_id = 999) = 0 THEN  
      RAISE emp_not_found;  
   END IF;  
EXCEPTION  
   WHEN emp_not_found THEN  
      DBMS_OUTPUT.PUT_LINE('Employee not found!');  
END;
```
☑ **Explanation:** `RAISE` manually triggers an error when an employee is missing.  

---

## **🔹 Summary**
✔ **PL/SQL adds procedural features to SQL**  
✔ Supports **Variables, Conditions, Loops, Cursors, and Exception Handling**  
✔ **Cursors** allow row-by-row processing of results  
✔ **Exception Handling** prevents runtime errors  

---
## **Stored Procedures & Functions in PL/SQL**  

📌 **Definition:**  
- **Stored Procedures** and **Functions** are named PL/SQL blocks that execute a sequence of SQL and PL/SQL statements.
- They **improve performance**, **reduce redundancy**, and **increase reusability**.

---

## **1️⃣ Stored Procedures**  

📌 **Definition:**  
A **Stored Procedure** is a set of SQL statements **stored in the database** and executed when called.  
It can accept **parameters** and perform **DML (Data Manipulation Language) operations**.  

✅ **Syntax of a Stored Procedure**  
```plsql
CREATE OR REPLACE PROCEDURE procedure_name  
(param1 datatype, param2 datatype)  
IS  
BEGIN  
   -- SQL statements  
END procedure_name;
```

✅ **Example: Procedure to Insert an Employee**  
```plsql
CREATE OR REPLACE PROCEDURE add_employee  
(emp_id NUMBER, emp_name VARCHAR2, emp_salary NUMBER)  
IS  
BEGIN  
   INSERT INTO employees (id, name, salary) VALUES (emp_id, emp_name, emp_salary);  
   COMMIT;  
END add_employee;
```
☑ **Explanation:**  
- `CREATE OR REPLACE PROCEDURE` defines the procedure.  
- `INSERT INTO` adds a new row to the `employees` table.  
- `COMMIT` saves the changes.  

✅ **Calling the Procedure**  
```plsql
BEGIN  
   add_employee(101, 'John Doe', 50000);  
END;
```

---

## **2️⃣ Functions in PL/SQL**  

📌 **Definition:**  
A **Function** is similar to a stored procedure but **must return a value**.  

✅ **Syntax of a Function**  
```plsql
CREATE OR REPLACE FUNCTION function_name  
(param1 datatype, param2 datatype)  
RETURN return_datatype  
IS  
BEGIN  
   -- SQL statements  
   RETURN some_value;  
END function_name;
```

✅ **Example: Function to Calculate Bonus**  
```plsql
CREATE OR REPLACE FUNCTION calculate_bonus  
(emp_salary NUMBER)  
RETURN NUMBER  
IS  
   bonus NUMBER;  
BEGIN  
   bonus := emp_salary * 0.10;  -- 10% bonus  
   RETURN bonus;  
END calculate_bonus;
```
☑ **Explanation:**  
- `CREATE OR REPLACE FUNCTION` defines the function.  
- `RETURN NUMBER` specifies the return type.  
- The function calculates **10% of salary** as a bonus.  

✅ **Calling the Function**  
```plsql
DECLARE  
   emp_bonus NUMBER;  
BEGIN  
   emp_bonus := calculate_bonus(50000);  
   DBMS_OUTPUT.PUT_LINE('Bonus: ' || emp_bonus);  
END;
```
☑ **Output:**  
```
Bonus: 5000
```

---

## **3️⃣ Differences: Procedure vs. Function**  

| Feature        | Procedure | Function |
|---------------|-----------|-----------|
| Returns a value? | No | Yes |
| Used in SELECT? | No | Yes |
| Can modify data (INSERT, UPDATE, DELETE)? | Yes | No |
| Can have multiple OUT parameters? | Yes | No |
| Called using? | `EXEC procedure_name` | `SELECT function_name(args) FROM dual;` |

---

## **🔹 Summary**
✔ **Stored Procedures** execute multiple SQL statements and **do not return a value**.  
✔ **Functions** return a single value and can be used in **SELECT statements**.  
✔ Both **improve code reusability and performance**.  

---
## **Triggers in PL/SQL**  

📌 **Definition:**  
A **Trigger** is a stored PL/SQL block that is **automatically executed** when a specified event occurs in a table.  

📌 **Key Features:**  
- Executes **before or after** an event (**INSERT, UPDATE, DELETE**).  
- Can be **Row-Level** (for each row) or **Statement-Level** (once per operation).  
- Helps in **maintaining data integrity** and **enforcing business rules**.

---

## **1️⃣ Types of Triggers**  

| Trigger Type | Description |
|-------------|-------------|
| **BEFORE Trigger** | Executes **before** the triggering event (e.g., before inserting a row). |
| **AFTER Trigger** | Executes **after** the triggering event (e.g., after updating a row). |
| **INSTEAD OF Trigger** | Used for **views** to handle **DML operations indirectly**. |
| **ROW-Level Trigger** | Executes **for each row** affected by a DML statement. |
| **STATEMENT-Level Trigger** | Executes **once per statement**, regardless of the number of affected rows. |

---

## **2️⃣ Row-Level Triggers**  

📌 **Example: Before Insert Trigger to Auto-Generate Employee ID**  
```plsql
CREATE OR REPLACE TRIGGER before_insert_employee  
BEFORE INSERT ON employees  
FOR EACH ROW  
BEGIN  
   SELECT NVL(MAX(id), 0) + 1 INTO :NEW.id FROM employees;  
END;
```
☑ **Explanation:**  
- **BEFORE INSERT**: Runs before a new employee record is inserted.  
- **FOR EACH ROW**: Executes for each new row.  
- **:NEW.id**: Assigns the next available ID.  

✅ **Test the Trigger:**  
```plsql
INSERT INTO employees(name, salary) VALUES ('Alice', 60000);
SELECT * FROM employees;
```

---

## **3️⃣ Statement-Level Triggers**  

📌 **Example: After Delete Trigger to Log Deleted Rows**  
```plsql
CREATE OR REPLACE TRIGGER after_delete_employee  
AFTER DELETE ON employees  
BEGIN  
   INSERT INTO log_table (operation, timestamp)  
   VALUES ('DELETE', SYSTIMESTAMP);  
END;
```
☑ **Explanation:**  
- **AFTER DELETE**: Runs after deleting any employee record.  
- **Logs the event** into `log_table`.  

✅ **Test the Trigger:**  
```plsql
DELETE FROM employees WHERE id = 101;
SELECT * FROM log_table;
```

---

## **4️⃣ INSTEAD OF Triggers (For Views)**  

📌 **Example: Handling Insert on a View**  
```plsql
CREATE OR REPLACE TRIGGER instead_of_insert_view  
INSTEAD OF INSERT ON employee_view  
FOR EACH ROW  
BEGIN  
   INSERT INTO employees (id, name, salary) VALUES (:NEW.id, :NEW.name, :NEW.salary);  
END;
```
☑ **Explanation:**  
- **INSTEAD OF INSERT**: Runs when inserting into a **view**.  
- Redirects data to the `employees` table.  

---

## **5️⃣ Trigger vs. Procedure vs. Function**  

| Feature | Trigger | Procedure | Function |
|---------|----------|------------|-----------|
| Execution | **Automatic** | **Manually Called** | **Manually Called** |
| Returns a Value? | No | No | Yes |
| Can Modify Data? | No | Yes | No |
| Runs on Events? | Yes | No | No |

---

## **🔹 Summary**
✔ **Triggers** automate actions **before or after** DML operations.  
✔ **Row-Level Triggers** execute for **each row**, while **Statement-Level Triggers** execute **once per transaction**.  
✔ **INSTEAD OF Triggers** help perform **DML on views**.  

---

