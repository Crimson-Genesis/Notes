# RDBMS  
---

# Unit -I  
### Introduction to Database System  
- Database and Users: Introduction (Basic Concepts: Data, Database, Database systems, Database Management Systems), Characteristics of Database Approach, Advantages of using the DBMS approach  
- Database System Concepts and Architecture: Data Models, Schemas, Instances, the three schema architectures and data independence, Database Languages and interfaces, Database System environment, Centralized and client / Server Architecture for DBMS, Classifications of Database Management Systems,  Integrity Rules and Theoretical Relational Languages,   
- Relational Model concepts: Relational Model concepts, Relational Model constraints and Relational Database Schemas  

---

### **Basic Concepts: Data, Database, Database System, DBMS**

#### **1. Data**
- **Definition**: Raw facts and figures without any context or meaning.
- **Example**: `98`, `John`, `5600` — these values alone don't convey much unless combined meaningfully.

#### **2. Database**
- **Definition**: An organized collection of related data, generally stored and accessed electronically from a computer system.
- **Purpose**: To manage large volumes of data efficiently.
- **Example**: A college database storing students’ names, IDs, marks, etc.

#### **3. Database System**
- **Definition**: The entire system that enables the collection, storage, management, and retrieval of data using hardware, software, and procedures.
- **Components**:
  - Hardware
  - Software (DBMS)
  - Data
  - Users
  - Procedures

#### **4. DBMS (Database Management System)**
- **Definition**: A software system that allows users to define, create, maintain, and control access to the database.
- **Popular DBMS**: Oracle, MySQL, PostgreSQL, SQL Server, SQLite.

#### **Example Scenario**
Imagine a university managing student records manually:
- **Without DBMS**: Data is stored in files and handled with file systems.
- **With DBMS**: All records are stored in a structured format, searchable and maintainable via software like MySQL.

---
### **Characteristics of the Database Approach**

The database approach introduces a centralized and organized way to manage data, contrasting the traditional file-processing systems. Here are its main characteristics:

---

#### **1. Self-describing Nature of a Database System**
- A DBMS contains not only the database itself but also a **metadata repository**, i.e., the data about the data (schemas, structure, constraints, etc.).
- This allows applications and users to interact with the DBMS without needing to know the low-level details.

#### **2. Insulation Between Programs and Data (Data Abstraction)**
- The DBMS provides a **layer of abstraction**—applications don't need to know how data is physically stored.
- Changes in the storage structure **don’t affect application programs**, ensuring flexibility and maintainability.

#### **3. Support for Multiple Views of Data**
- Different users can have **different perspectives (views)** of the same data depending on their needs.
- Example: A student sees only their marks; an admin sees everyone’s records.

#### **4. Sharing of Data and Multiuser Transaction Processing**
- **Concurrent Access**: Multiple users can access and manipulate the database **simultaneously**.
- **Transaction Management**: Ensures that all transactions are processed reliably and concurrently without data corruption.

#### **5. Data Integrity and Security**
- Enforces rules to maintain **data accuracy and consistency** (integrity constraints).
- Provides access controls, authentication, and authorization features to **protect data from unauthorized access**.

#### **6. Reduced Data Redundancy**
- Centralized database avoids **duplicate data** entries across departments or applications.
- This also saves space and improves data consistency.

#### **7. Data Independence**
- Logical and physical structure of data can be changed without affecting how applications interact with the data.

---

**Example:**
In a file-based system, if a student’s record structure changes (like adding a new field "blood group"), every application accessing student data must be modified.  
In a DBMS, only the schema changes, not the application logic.

---
### **Advantages of Using the DBMS Approach**

Using a Database Management System (DBMS) offers several benefits compared to traditional file-based systems:

---

#### **1. Improved Data Sharing**
- Multiple users and applications can access the same database, ensuring **controlled data sharing** across departments and systems.

#### **2. Data Security**
- A DBMS provides **authorization and access control mechanisms**, allowing different users to access only the data they’re permitted to.

#### **3. Better Data Integration**
- A DBMS allows the combination of data from multiple sources, providing a **unified view** for analysis and decision-making.

#### **4. Reduced Data Redundancy and Inconsistency**
- Since data is stored centrally, **redundant copies are minimized**, and changes made at one place are reflected everywhere—**ensuring consistency**.

#### **5. Improved Data Access**
- With powerful query languages like **SQL**, users can quickly and efficiently retrieve and manipulate data as needed.

#### **6. Improved Decision Making**
- Accurate, up-to-date, and integrated data helps in generating **reliable reports**, thereby assisting better decisions.

#### **7. Increased Productivity**
- Tools for data entry, report generation, query processing, etc., increase the productivity of users and developers.

#### **8. Data Backup and Recovery**
- DBMSs include **automatic backup and recovery mechanisms** to restore data in case of failure, ensuring reliability.

#### **9. Data Independence**
- Changes in data structure (schema) don’t affect application programs, leading to **flexibility and low maintenance**.

---

**Example Comparison:**

| Feature               | File System                     | DBMS                                 |
|-----------------------|----------------------------------|---------------------------------------|
| Data Sharing          | Limited                         | Multi-user and concurrent             |
| Redundancy            | High                            | Reduced                               |
| Query Support         | Manual                          | SQL and query languages               |
| Data Security         | Application-level only          | Built-in security mechanisms          |
| Backup/Recovery       | Manual or limited               | Automatic and robust                  |
| Integrity Constraints | Not supported                   | Enforced via rules                    |

---
### **Database System Concepts and Architecture**

---

#### **1. Data Models**

A **Data Model** is a collection of concepts used to describe the structure of a database.

**Types:**
- **Hierarchical Model**: Data organized in a tree-like structure.
- **Network Model**: Data represented as records connected by links (many-to-many).
- **Relational Model**: Data stored in tables (relations).
- **Object-oriented Model**: Data stored as objects (like in OOP).

---

#### **2. Schemas and Instances**

- **Schema**: The structure or blueprint of a database (defines tables, fields, relationships).  
  - *Example:* Table name, column names, data types.
- **Instance**: The actual content (data) of the database at a given time.

**Analogy**:  
*Schema = class definition in OOP*  
*Instance = objects created from the class*

---

#### **3. Three-Schema Architecture**

This provides **data abstraction** and separates user applications from physical database.

**Levels:**
1. **External Level**: User views (customized for each user).
2. **Conceptual Level**: Community view (logical structure of the entire database).
3. **Internal Level**: Physical storage structure.

**Benefit**: Independence between views and storage — changes in storage won’t affect user views.

---

#### **4. Data Independence**

- **Logical Data Independence**: Ability to change the conceptual schema without affecting external schemas or applications.
- **Physical Data Independence**: Ability to change the internal schema without changing the conceptual schema.

---

#### **5. Database Languages and Interfaces**

**Languages:**
- **DDL (Data Definition Language)**: Defines schema (CREATE, ALTER, DROP).
- **DML (Data Manipulation Language)**: Accesses and manipulates data (SELECT, INSERT, UPDATE, DELETE).
- **DCL (Data Control Language)**: Controls access (GRANT, REVOKE).
- **TCL (Transaction Control Language)**: Manages transactions (COMMIT, ROLLBACK).

**Interfaces:**
- **Menu-based** (e.g., ATM)
- **Forms-based** (data entry forms)
- **Graphical User Interfaces (GUI)** (drag & drop)
- **Natural language** (AI-like queries)
- **SQL command line**

---

#### **6. Database System Environment**

**Components:**
- **Hardware**: Physical devices.
- **Software**: DBMS software, OS, applications.
- **Data**: Stored and maintained.
- **Users**: DBA, developers, end-users.

---

#### **7. Centralized vs. Client/Server Architecture**

| Feature            | Centralized DBMS             | Client/Server DBMS                  |
|--------------------|------------------------------|-------------------------------------|
| Location           | Single site                  | Multiple systems over a network     |
| Control            | Central control              | Distributed control                 |
| Access             | Limited                      | Multi-user                          |
| Example            | Legacy systems               | MySQL, Oracle, SQL Server           |

---

#### **8. Classification of DBMSs**

- **Based on Data Model**: Relational, Object-oriented, Hierarchical
- **Based on Users**: Single-user, Multi-user
- **Based on Location**: Centralized, Distributed
- **Based on Usage**: OLTP (Online Transaction Processing), OLAP (Analytical Processing)

---
### **Integrity Rules and Theoretical Relational Languages**

---

#### **1. Integrity Rules in the Relational Model**

These rules ensure accuracy and consistency of data in a relational database.

##### **i. Domain Integrity**
- Each attribute must contain only atomic values from a defined domain.
- Example: Age column must have only integer values (like 20, 25), not text or decimals.

##### **ii. Entity Integrity**
- Every table must have a primary key, and it **cannot have NULL values**.
- Ensures that each row is uniquely identifiable.

##### **iii. Referential Integrity**
- A foreign key must match a primary key in another table or be NULL.
- Ensures consistency between related tables.

**Example**:  
If `student.course_id` is a foreign key referencing `course.course_id`,  
then each value in `student.course_id` must exist in the `course` table.

---

#### **2. Theoretical Relational Languages**

There are two formal languages used for theoretical understanding of relational databases:

##### **i. Relational Algebra**
- A **procedural language**: tells **how** to retrieve data.
- Operations take one or two relations and produce a new relation.

**Basic Operations:**
- **Select (σ)**: Filters rows.  
  `σ age > 20 (STUDENT)`
- **Project (π)**: Selects columns.  
  `π name, age (STUDENT)`
- **Union (∪)**: Combines tuples from two relations.
- **Set Difference (−)**: Returns tuples in one relation but not in another.
- **Cartesian Product (×)**: Combines every tuple of one relation with every tuple of another.
- **Rename (ρ)**: Renames relations or attributes.

**Advanced:**
- **Join**: Combines related tuples from different relations.

##### **ii. Relational Calculus**
- A **non-procedural language**: tells **what** data to retrieve, not how.
- Based on logic and predicates.

**Types:**
- **Tuple Relational Calculus (TRC)**:  
  `{ t | P(t) }` where `t` is a tuple and `P(t)` is a predicate.
- **Domain Relational Calculus (DRC)**:  
  `{ <x, y> | P(x, y) }` where x and y are domain variables.

**Example TRC**:  
`{ t | t ∈ STUDENT ∧ t.age > 20 }`

---
### **Relational Model Concepts, Constraints, and Relational Database Schemas**

---

#### **1. Relational Model Concepts**

The relational model represents data in the form of **tables (relations)**. Each table has:

- **Tuples (rows)**: Represent individual records.
- **Attributes (columns)**: Represent properties of records.
- **Relation**: A table with rows and columns.
- **Degree**: Number of attributes in a relation.
- **Cardinality**: Number of tuples in a relation.

**Example:**
```
STUDENT(Relation)
+------------+----------+--------+
| Student_ID | Name     | Age    |
+------------+----------+--------+
| 101        | Alice    | 20     |
| 102        | Bob      | 21     |
+------------+----------+--------+
```

---

#### **2. Relational Model Constraints**

Constraints ensure correctness and validity of data in the database.

##### **i. Domain Constraint**
- Specifies that each attribute must be of a specific type.
  - Example: Age must be an integer.

##### **ii. Key Constraint**
- A table must have a **Primary Key** (unique and non-null).
- Other types:
  - **Candidate Key**: A set of fields that can uniquely identify tuples.
  - **Super Key**: A set of attributes that uniquely identifies tuples (can be more than needed).
  - **Foreign Key**: An attribute that refers to a primary key in another relation.

##### **iii. Entity Integrity**
- No part of a primary key can be null.

##### **iv. Referential Integrity**
- A foreign key must match a primary key in another table or be null.

**Example of Referential Integrity Violation:**
If a student is assigned to a course ID that doesn’t exist in the `COURSE` table, the constraint is violated.

---

#### **3. Relational Database Schemas**

A **schema** defines the structure of a relation.

- **Relation Schema**: Specifies the relation name, attributes, and domains.
  - Example:  
    `STUDENT(Student_ID: int, Name: string, Age: int)`

- **Database Schema**: The collection of relation schemas for a database.

---

#### **Example Problem:**

**Q: Define the relational schema for a LIBRARY system with books and authors.**

**Answer:**

```sql
BOOK(Book_ID: int, Title: string, Author_ID: int)
AUTHOR(Author_ID: int, Name: string)
```

**Constraints:**
- `Book_ID` is Primary Key in BOOK.
- `Author_ID` is Primary Key in AUTHOR.
- `Author_ID` in BOOK is a Foreign Key referencing AUTHOR(Author_ID).

---

# Unit -II  
### Entity Relationship Diagram and Database   
- Design Using high level conceptual data models for database design (Design Phases of database design), Entity types, Entity Sets, Attributes and keys, Relationship Types, Relationship sets, Roles and structural constraints, Weak entity Types, Refining the ER diagram for company Database, Entity Relationship Diagram Naming conventions Design issues.  
- Informal Design Guidelines for Relational Schema, Functional Dependencies, Normal Forms based on Primary keys, General  
- definitions of 1NF, 2NF and 3NF, Boyce-Codd Normal Forms (BCNF), Multi-valued Dependency and Fourth Normal Form  

---

## **Entity-Relationship Diagram and Database Design**

### **1. Database Design Using High-Level Conceptual Data Models**

#### **Overview**
Database design is a systematic process of creating a database that accurately reflects the data needs of an organization. This process is divided into several phases, with the first being the **conceptual design**, often using **high-level data models** like the **Entity-Relationship (ER) Model**.

#### **Phases of Database Design**
1. **Requirements Analysis**:
   - Understand what data needs to be stored and how it will be used.
   - Includes interviews with users, studying documents, and understanding business rules.

2. **Conceptual Design**:
   - Build a high-level ER diagram to model the data.
   - This model includes **entities**, **attributes**, **relationships**, and **constraints**.

3. **Logical Design**:
   - Convert the ER model into a logical model suitable for the type of database (e.g., relational).
   - This involves converting entities into tables, attributes into columns, etc.

4. **Normalization**:
   - Apply normalization rules (1NF, 2NF, 3NF, etc.) to remove redundancy and ensure consistency.

5. **Physical Design**:
   - Decide on physical storage structures, indexing, partitioning, etc.
   - Optimize for performance, cost, and storage.

6. **Implementation**:
   - Create the actual database using SQL commands (CREATE TABLE, etc.).

#### **Example**:  
**Mini Case Study** – Designing a database for a **Library**  
- **Entities**: Book, Member, Borrowing  
- **Attributes**:  
   - Book: Book_ID, Title, Author, Publisher  
   - Member: Member_ID, Name, Address, Phone  
   - Borrowing: Borrowing_ID, Date_Issued, Date_Returned  

- **Relationships**:  
   - Member *borrows* Book  
   - Book *is borrowed through* Borrowing  

This phase would produce an ER diagram linking these entities.

---
### **2. Entity Types, Entity Sets, Attributes, and Keys**

---

#### **Entity Types**

An **Entity Type** is a collection of objects (called **entities**) that share the same properties or attributes. It represents a real-world object or concept in the database.

- **Examples**:  
  - `Student`, `Employee`, `Book`, `Product`

Each entity type will be represented as a **rectangle** in an ER diagram.

---

#### **Entity Sets**

An **Entity Set** is a collection of all entities of a particular entity type in the database at any point in time.

- Example:  
  If "Student" is an entity type, then all students currently stored in the database form the **entity set** `Students`.

---

#### **Attributes**

**Attributes** are properties or characteristics of an entity.

**Types of Attributes:**
1. **Simple / Atomic Attribute**: Cannot be divided further.  
   - Example: `Age`, `ID`
2. **Composite Attribute**: Can be divided into smaller subparts.  
   - Example: `Name` → `FirstName`, `LastName`
3. **Derived Attribute**: Can be calculated from other attributes.  
   - Example: `Age` derived from `Date of Birth`
4. **Multivalued Attribute**: Can have more than one value.  
   - Example: `PhoneNumbers`

Attributes are represented as **ellipses** connected to their entity in the ER diagram.

---

#### **Keys**

A **Key** is an attribute (or a set of attributes) that uniquely identifies each entity in the entity set.

**Types of Keys:**
- **Primary Key**: Uniquely identifies an entity. Cannot be null.
- **Candidate Key**: A set of attributes that can qualify as a unique key.
- **Super Key**: A set of attributes that uniquely identifies rows in a table.
- **Composite Key**: A key consisting of more than one attribute.

---

### **Example**

Let’s consider the **Student** entity:

- **Entity Type**: `Student`
- **Attributes**: `StudentID` (Primary Key), `Name` (Composite), `DateOfBirth`, `Email`, `PhoneNumbers` (Multivalued)
- **Entity Set**: All current students in the database

---

**ER Diagram Notation:**
- Rectangle: Entity (e.g., Student)
- Ellipse: Attribute
- Underlined Ellipse: Primary Key
- Double Ellipse: Multivalued Attribute
- Dashed Ellipse: Derived Attribute
- Connected lines: Show relationship

---
### **3. Relationship Types, Relationship Sets, Roles, and Structural Constraints**

---

#### **Relationship Types**

A **relationship type** defines an association among two or more entity types. It describes how entities are related to each other.

- **Example**:  
  A `Works_For` relationship between `Employee` and `Department` entities.  
  A `Enrolled_In` relationship between `Student` and `Course`.

In an ER diagram, relationships are represented by **diamonds**.

---

#### **Relationship Sets**

A **relationship set** is a collection of relationship instances of the same type.

- Each relationship instance associates entities from the participating entity sets.
- For the relationship type `Works_For`, the set of all `Employee`-`Department` associations at a given time is the **relationship set**.

---

#### **Degree of a Relationship**

- **Unary (Recursive)**: Relationship between entities of the same type.  
  *E.g.*: `Employee` supervises another `Employee`.

- **Binary**: Relationship between two entity types.  
  *E.g.*: `Student` enrolled in `Course`.

- **Ternary and Higher**: Relationships among three or more entity types.  
  *E.g.*: `Doctor` prescribes `Medicine` to `Patient`.

---

#### **Roles**

In relationships involving the same entity type more than once, **roles** clarify the function of each entity.

- Example: In a `Manages` relationship between employees, we may use roles like `manager` and `subordinate`.

---

#### **Structural Constraints**

Two key types of constraints define relationships:

1. **Cardinality Ratio (Multiplicity)**: Specifies the number of entity instances that can participate in a relationship.

   - **1:1** – One entity relates to only one other.
   - **1:N** – One entity relates to many others.
   - **M:N** – Many entities relate to many others.

2. **Participation Constraint**:
   - **Total Participation**: Every entity must participate in the relationship.
   - **Partial Participation**: Some entities may not participate.

---

### **Example**

For a university database:

- Entity Types: `Student`, `Course`
- Relationship: `Enrolled_In`
- Cardinality: Many-to-Many (M:N)
- Participation: A `Student` may or may not enroll in a course (partial), but every `Course` must have at least one student (total).

---
### **4. Weak Entity Types**

---

#### **Definition**

A **weak entity type** is an entity that **cannot be uniquely identified by its own attributes alone**. It relies on a **related strong entity type** (called the **owner**) for its identification. It does **not have a primary key** of its own but uses a **partial key** combined with the primary key of the related strong entity.

---

#### **Key Characteristics**

- Requires a **foreign key** reference to a strong entity for identification.
- Always **participates in a total (existence-dependent)** relationship with its owner.
- Represented in ER diagrams as:
  - **Double rectangles** for the weak entity.
  - **Double diamonds** for the identifying relationship.
  - **Dashed underline** for the partial key.

---

#### **Example**

Consider a **Payment** made by a **Customer**:

- `Customer` (Strong Entity): Identified by `CustomerID`
- `Payment` (Weak Entity): Identified by `PaymentNumber` (not unique alone)

To uniquely identify a payment:
```
Primary Key of Payment = (CustomerID, PaymentNumber)
```

So here:
- `PaymentNumber` is the **partial key**.
- The identifying relationship might be named `Makes`.

---

#### **ER Diagram Representation**

- **Customer** is drawn using a **single rectangle**.
- **Payment** is drawn using a **double rectangle**.
- The **relationship** `Makes` is a **double diamond**.
- The line connecting `Payment` to `Makes` is **bold** or **double**, indicating **total participation**.

---

#### **Use Cases**

Weak entities are often used when:

- An object’s existence is **meaningless without its parent**.
- The identification of the entity requires **contextual reference** (e.g., line items in an order, rooms in a hotel, dependents of employees).

---
### **5. Refining the ER Diagram for Company Database**

---

#### **Purpose of Refinement**

Refinement ensures that the ER model accurately represents real-world constraints and avoids common design issues like redundancy, incorrect cardinalities, and unclear relationships.

---

#### **Key Refinement Techniques**

1. **Attribute vs. Entity Decision**
   - Move attributes that have multiple values or complex structures into separate entities.
   - Example: If `Employee` has multiple `PhoneNumbers`, model `PhoneNumber` as a separate entity.

2. **Generalization / Specialization**
   - **Generalization**: Combine similar entities into a higher-level entity.
     - Example: `Engineer` and `Manager` → `Employee`
   - **Specialization**: Split a general entity into specialized sub-entities.
     - Example: `Employee` → `FullTimeEmployee`, `PartTimeEmployee`

3. **Aggregation**
   - Used when a relationship itself has attributes or participates in another relationship.
   - Example: If `Project` assigns `Employee` and also has a `Budget`, aggregate the `Works_On` relationship.

4. **Eliminating Redundant Relationships**
   - Remove relationships that can be derived from other relationships.
   - Example: If `Manages` and `Works_For` together imply `Oversees`, you may avoid modeling `Oversees`.

5. **Naming Conventions**
   - Use clear, meaningful names.
   - Entity names: Singular nouns (`Employee`, not `Employees`)
   - Attribute names: Clear and specific (`EmpName`, `EmpID`)
   - Relationship names: Verb phrases (`Works_On`, `Manages`)

---

#### **Example of Refinement**

Before Refinement:
- `Employee` has `ProjectName` as an attribute.

After Refinement:
- Create a `Project` entity.
- Use a `Works_On` relationship between `Employee` and `Project`.

---

#### **Benefits of Refinement**

- Eliminates data redundancy.
- Reduces ambiguity.
- Improves normalization and logical design.
- Prepares model for easier conversion to relational schema.

---
### **6. Entity Relationship Diagram (ERD) Naming Conventions & Design Issues**

---

#### **A. Naming Conventions**

Proper naming in ER diagrams ensures clarity, consistency, and easier translation into relational models.

**1. Entity Names**
- Use **singular** nouns (e.g., `Student`, `Course`, `Employee`)
- Should be **unique** and **descriptive**
- Capitalize first letters for clarity

**2. Attribute Names**
- Should be **unique** within the entity
- Use prefixes/suffixes when needed to avoid confusion (`Emp_ID`, `Emp_Name`)
- Use camel case or underscores for multi-word names (e.g., `FirstName` or `first_name`)

**3. Relationship Names**
- Use **verb phrases** describing the action (e.g., `Enrolled_In`, `Works_On`, `Manages`)
- Should be meaningful and consistent

**4. Key Conventions**
- Use suffix `_ID` for primary key attributes (`Student_ID`, `Course_ID`)
- Foreign keys usually use the same name as the referenced primary key

---

#### **B. Design Issues in ER Modeling**

These are common challenges to address when designing ER diagrams:

**1. Choosing Entity vs. Attribute**
- If data has **its own properties** or participates in relationships, make it an entity.
  - Example: `Address` might be an attribute or an entity depending on complexity.

**2. Choosing Entity vs. Relationship**
- If a relationship has **attributes**, model it as an entity (using aggregation or a linking entity).
  - Example: `Enrollment` between `Student` and `Course` with `Grade` as an attribute.

**3. Identifying Relationship Cardinalities**
- Define participation constraints carefully: One-to-One, One-to-Many, Many-to-Many.
- This affects foreign key design and data integrity.

**4. Handling Multi-valued Attributes**
- Convert into a separate entity and link with a one-to-many relationship.

**5. Handling Composite and Derived Attributes**
- Break **composite attributes** into sub-attributes (`FullName` → `FirstName`, `LastName`)
- Show **derived attributes** (like `Age`) with dashed ovals.

---

#### **Example: Good ER Design**

- `Student(Student_ID, Name, DOB)`
- `Course(Course_ID, Title)`
- `Enrolled(Student_ID, Course_ID, Grade)`

`Enrolled` is a relationship entity because it includes the attribute `Grade`.

---
### **7. Informal Design Guidelines for Relational Schemas**

---

To ensure a good relational database design, certain **informal guidelines** are followed before normalization. These help avoid redundancy, anomalies, and integrity problems.

---

#### **A. Semantics of Attributes**

- **Each attribute** must describe a property of the **entity or relationship** it belongs to.
- Do **not mix** attributes of different meanings in one relation.

**Bad Example:**

```
Student_Info(Student_ID, Name, Course_ID, Course_Name)
```

This mixes student and course information in one table — violating semantics.

**Good Design:**

```
Student(Student_ID, Name)
Course(Course_ID, Course_Name)
Enrollment(Student_ID, Course_ID)
```

---

#### **B. Reducing Redundancy**

- Redundancy causes **waste of space** and **update anomalies**.
- Store each piece of information only **once**.

**Example:**
- Storing a course name repeatedly for every enrolled student leads to redundancy.

---

#### **C. Avoiding Null Values**

- Minimize nulls wherever possible to avoid **ambiguity** (unknown vs. not applicable).
- Use separate relations or default values.

---

#### **D. Avoiding Spurious Tuples**

- Spurious tuples occur during **incorrect decomposition** and joining.
- Ensure **lossless decomposition** of tables using proper keys.

**Example:**

Decomposing incorrectly:
```
Employee(Emp_ID, Dept_Name, Salary)
→ Employee1(Emp_ID, Dept_Name)
→ Employee2(Emp_ID, Salary)
```

Joining Employee1 and Employee2 might produce **spurious combinations** unless Emp_ID is a key in both.

---

#### **E. Ensuring Functional Dependency Preservation**

- Decomposition should **preserve all dependencies** so constraints are not lost.

---
### **8. Functional Dependencies (FDs)**

---

A **Functional Dependency (FD)** is a constraint between two sets of attributes in a relation from a database.

---

#### **Definition:**

Let **R** be a relation and **X** and **Y** be subsets of attributes in R.  
FD **X → Y** means:

> If two tuples have the same values for **X**, they must also have the same values for **Y**.

This indicates **X functionally determines Y**.

---

#### **Example:**

In a table **Student(Student_ID, Name, Department)**:

- **Student_ID → Name**
- **Student_ID → Department**

Means: Student_ID uniquely identifies Name and Department.

---

#### **Types of Functional Dependencies:**

1. **Trivial FD:**  
   - Y ⊆ X  
   - Example: {Student_ID, Name} → Name

2. **Non-Trivial FD:**  
   - Y ⊄ X  
   - Example: Student_ID → Name

3. **Completely Non-Trivial FD:**  
   - X and Y have no attributes in common

---

#### **Properties of FDs (Armstrong's Axioms):**

These are used to **infer all possible FDs** from a given set:

1. **Reflexivity:** If Y ⊆ X, then X → Y  
2. **Augmentation:** If X → Y, then XZ → YZ  
3. **Transitivity:** If X → Y and Y → Z, then X → Z

---

#### **Derived Rules:**

- **Union:** If X → Y and X → Z, then X → YZ  
- **Decomposition:** If X → YZ, then X → Y and X → Z  
- **Pseudotransitivity:** If X → Y and YZ → W, then XZ → W

---

#### **Closure of FDs:**

- The **closure** of a set of attributes X, denoted **X⁺**, is the set of attributes that can be functionally determined by X using the FDs.

---

#### **Example Problem:**

**Given:**  
R(A, B, C, D) and F = {A → B, B → C}

**Find:** A⁺  
**Solution:**  
- Start with A⁺ = {A}  
- A → B ⇒ A⁺ = {A, B}  
- B → C ⇒ A⁺ = {A, B, C}  
- So, **A⁺ = {A, B, C}**

---
### **9. Normalization and Normal Forms**

---

**Normalization** is the process of organizing data in a database to reduce **redundancy** and improve **data integrity**. It divides large tables into smaller ones and defines relationships among them.

---

### **Objectives of Normalization:**

- Eliminate data redundancy.
- Avoid anomalies (insertion, deletion, update).
- Ensure data dependencies make sense.

---

## **1NF (First Normal Form)**

**Definition:**  
A relation is in **1NF** if:
- All attributes contain only **atomic (indivisible)** values.
- Each attribute contains only a **single value**, not a set or list.

**Violation Example:**

| Student_ID | Name     | Subjects          |
|------------|----------|-------------------|
| 1          | Alice    | Math, Physics     |

- `Subjects` is a multi-valued attribute → **Not in 1NF**

**Converted to 1NF:**

| Student_ID | Name     | Subject   |
|------------|----------|-----------|
| 1          | Alice    | Math      |
| 1          | Alice    | Physics   |

---

## **2NF (Second Normal Form)**

**Definition:**  
A relation is in **2NF** if:
- It is in 1NF.
- No **partial dependency** exists (i.e., no non-prime attribute is functionally dependent on part of a **candidate key**).

**Example:**

Given relation:  
**Student_Course(Student_ID, Course_ID, Student_Name, Course_Name)**  
Candidate key: (Student_ID, Course_ID)

- **Partial dependency:**  
  - Student_ID → Student_Name  
  - Course_ID → Course_Name  
  - Violates 2NF

**Decomposition:**

1. Student(Student_ID, Student_Name)  
2. Course(Course_ID, Course_Name)  
3. Student_Course(Student_ID, Course_ID)

---

## **3NF (Third Normal Form)**

**Definition:**  
A relation is in **3NF** if:
- It is in 2NF.
- No **transitive dependency** exists (i.e., no non-prime attribute depends on another non-prime attribute).

**Example:**

| Emp_ID | Emp_Name | Dept_ID | Dept_Name |
|--------|----------|---------|-----------|

FDs:
- Emp_ID → Emp_Name, Dept_ID  
- Dept_ID → Dept_Name

Here, Dept_Name is **transitively dependent** on Emp_ID → violates 3NF.

**Decomposition:**

1. Employee(Emp_ID, Emp_Name, Dept_ID)  
2. Department(Dept_ID, Dept_Name)

---

## **BCNF (Boyce-Codd Normal Form)**

**Definition:**  
A relation is in **BCNF** if:
- For every non-trivial FD **X → Y**, **X** is a **super key**.

**Example:**

| Course | Instructor | Room |
|--------|------------|------|
FDs:
- Course → Room  
- Room → Instructor

Candidate Key: (Course)

**Room → Instructor** violates BCNF because Room is not a super key.

**Decomposition:**

1. Room_Instructor(Room, Instructor)  
2. Course_Room(Course, Room)

---

### **Comparison Table**

| Normal Form | Problem Addressed         | Key Rule                                 |
|-------------|----------------------------|-------------------------------------------|
| 1NF         | Multi-valued attributes    | Atomic values only                        |
| 2NF         | Partial dependency         | No partial dependency on candidate key    |
| 3NF         | Transitive dependency      | Non-prime attribute only depends on keys  |
| BCNF        | Superkey violations        | LHS of every FD is a superkey             |

---
### **10. Multivalued Dependency (MVD) and Fourth Normal Form (4NF)**

---

### **Multivalued Dependency (MVD):**

A **Multivalued Dependency (MVD)** occurs when:
- For a single value of **attribute A**, there are **multiple independent values** of **attribute B** and **attribute C**.

**Notation:**  
If for a relation **R**, attribute **A** multidetermines **B**, it is denoted as:  
**A ↠ B**

This means:  
- For each value of A, the set of values of B is independent of the set of values of C (other non-key attributes).

---

### **Example of MVD:**

| Student_ID | Course   | Hobby     |
|------------|----------|-----------|
| 1          | Math     | Painting  |
| 1          | Math     | Singing   |
| 1          | Science  | Painting  |
| 1          | Science  | Singing   |

Here:
- A = Student_ID  
- B = Course  
- C = Hobby  

Student 1 takes **both Math and Science** and has **both Painting and Singing** as hobbies.  
→ **Student_ID ↠ Course** and **Student_ID ↠ Hobby** (independently)

---

### **Fourth Normal Form (4NF):**

**Definition:**  
A relation is in **4NF** if:
- It is in **BCNF**.
- There are **no non-trivial multivalued dependencies**, except those in which the left-hand side is a **super key**.

---

### **Why 4NF?**

BCNF does not eliminate **multivalued redundancy**.  
4NF ensures **data is fully atomic** and **multivalued dependencies are removed**.

---

### **Converting to 4NF:**

Using the previous example:

**Relation R(Student_ID, Course, Hobby)** violates 4NF.

**Decompose into:**

1. R1(Student_ID, Course)  
2. R2(Student_ID, Hobby)

Now:
- Each relation has only one multivalued attribute dependent on the key → in 4NF.

---

### **Summary Table of Normal Forms:**

| Normal Form | Handles                | Condition                                      |
|-------------|------------------------|------------------------------------------------|
| 1NF         | Atomicity              | No repeating groups or multi-valued attributes |
| 2NF         | Partial dependency     | Fully dependent on entire candidate key        |
| 3NF         | Transitive dependency  | Non-prime attributes only depend on keys       |
| BCNF        | Superkey condition     | LHS of every FD must be a superkey             |
| 4NF         | Multivalued dependency| No MVD unless LHS is a superkey                |

---

# Unit -III  
### SQL Concepts  
- Basics of SQL: DDL,DML,DCL   
- Oracle Tables: DDL: Naming Rules and conventions , Data Types, Constraints, Creating Oracle Table, Displaying Table Information, Altering an Existing Table, Dropping, Renaming, Truncating Table, Table Types, Spooling, Error codes.  
- Working with Oracle Tables : Working with Table: Data Management and Retrieval: DML, adding a new Row/Record, Customized Prompts, Updating and Deleting an Existing Rows/Records, retrieving Data from Table, Arithmetic  Operations, restricting Data with WHERE clause, Sorting, Revisiting Substitution Variables, DEFINE command, CASE structure.   

---
### Structured Query Language (SQL)  
SQL is the standard language used to communicate with relational databases. It allows users to create, retrieve, update, and delete data, as well as manage database structures and access controls.

---

#### A. **Data Definition Language (DDL)**

DDL commands define and modify the structure of database objects like tables, views, schemas, etc.

- **CREATE**: Creates a new database object.
  ```sql
  CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50),
      age INT
  );
  ```

- **ALTER**: Modifies an existing database object.
  ```sql
  ALTER TABLE students ADD email VARCHAR(100);
  ```

- **DROP**: Deletes an object from the database.
  ```sql
  DROP TABLE students;
  ```

- **TRUNCATE**: Deletes all rows from a table but keeps its structure.
  ```sql
  TRUNCATE TABLE students;
  ```

- **RENAME**: Renames a database object.
  ```sql
  RENAME students TO learners;
  ```

---

#### B. **Data Manipulation Language (DML)**

DML commands are used to manipulate data within the tables.

- **INSERT**: Adds new records.
  ```sql
  INSERT INTO students (id, name, age) VALUES (1, 'John', 20);
  ```

- **UPDATE**: Modifies existing records.
  ```sql
  UPDATE students SET age = 21 WHERE id = 1;
  ```

- **DELETE**: Deletes specific records.
  ```sql
  DELETE FROM students WHERE id = 1;
  ```

---

#### C. **Data Control Language (DCL)**

DCL commands are used to control access to data.

- **GRANT**: Gives privileges to users.
  ```sql
  GRANT SELECT, INSERT ON students TO user1;
  ```

- **REVOKE**: Removes access rights.
  ```sql
  REVOKE SELECT, INSERT ON students FROM user1;
  ```

---

### Example Summary

| Command | Purpose | Example |
|--------|---------|---------|
| CREATE | Create object | `CREATE TABLE ...` |
| INSERT | Add data | `INSERT INTO ...` |
| SELECT | View data | `SELECT * FROM ...` |
| UPDATE | Modify data | `UPDATE ... SET` |
| DELETE | Remove data | `DELETE FROM ...` |
| GRANT | Access control | `GRANT SELECT ON ...` |

---
### **Data Types in Oracle SQL**

Oracle supports several built-in data types that can be used while defining the structure of a table. These are categorized as:

---

#### **1. Character Data Types**
Used to store alphanumeric strings.

- **CHAR(n)**: Fixed-length character data. If you insert a string shorter than `n`, Oracle pads it with spaces.
  - Example: `CHAR(10)`
  - `'hi'` will be stored as `'hi        '` (8 spaces).
- **VARCHAR2(n)**: Variable-length character data. Only uses as much space as needed.
  - Example: `VARCHAR2(20)`
  - `'hi'` will be stored as `'hi'`.

**Example**:
```sql
CREATE TABLE employee (
  name VARCHAR2(30),
  code CHAR(5)
);
```

---

#### **2. Numeric Data Types**
Used to store numbers.

- **NUMBER(p, s)**: `p` is precision (total digits), `s` is scale (digits after decimal).
  - Example: `NUMBER(5,2)` stores `999.99` but not `1000.00`.
- **INTEGER**: Synonym for `NUMBER(38)`.
- **FLOAT(p)**: Approximate numeric values.

**Example**:
```sql
CREATE TABLE salary (
  emp_id NUMBER,
  basic_pay NUMBER(8,2)
);
```

---

#### **3. Date/Time Data Types**
Used for storing dates and times.

- **DATE**: Stores date and time (`DD-MON-YY HH:MI:SS`).
- **TIMESTAMP**: Stores fractional seconds as well.
- **INTERVAL**: Stores time durations (e.g., 5 days, 3 hours).

**Example**:
```sql
CREATE TABLE project (
  proj_id NUMBER,
  start_date DATE,
  deadline TIMESTAMP
);
```

---

#### **4. Large Object (LOB) Types**
Used for large data storage (e.g., images, videos, long text).

- **BLOB**: Binary Large Object.
- **CLOB**: Character Large Object.
- **NCLOB**: Multilingual text.
- **BFILE**: Binary file stored outside DB.

---

#### **5. RAW and LONG**
Used for binary or long character data.

- **RAW(n)**: Stores binary data up to 2000 bytes.
- **LONG**: Stores variable-length character data (up to 2 GB, deprecated).

---

#### **Usage Summary Table**

| Data Type   | Description                              |
|-------------|------------------------------------------|
| CHAR(n)     | Fixed-length string                      |
| VARCHAR2(n) | Variable-length string                   |
| NUMBER(p,s) | Fixed precision number                   |
| DATE        | Date and time                            |
| TIMESTAMP   | Date with fractional seconds             |
| CLOB        | Large text                               |
| BLOB        | Large binary data                        |

---

#### **Sample Table Using All Data Types**:
```sql
CREATE TABLE test_all_datatypes (
  emp_id NUMBER(5),
  name VARCHAR2(50),
  doj DATE,
  profile_pic BLOB,
  salary NUMBER(10,2),
  description CLOB
);
```
---
### **Constraints in SQL**

Constraints are rules enforced on data columns to ensure the integrity, validity, and accuracy of the data within a database table. Oracle allows various types of constraints to be defined at the column level or the table level.

---

### **1. Types of Constraints**

| Constraint      | Description |
|----------------|-------------|
| **NOT NULL**     | Ensures that a column cannot have `NULL` values. |
| **UNIQUE**       | Ensures that all values in a column are different. |
| **PRIMARY KEY**  | Uniquely identifies each row; combines `UNIQUE` and `NOT NULL`. |
| **FOREIGN KEY**  | Links two tables; ensures referential integrity. |
| **CHECK**        | Ensures that values in a column meet a specific condition. |
| **DEFAULT**      | Assigns a default value if no value is provided. |

---

### **2. Adding Constraints While Creating Table**

**Example 1: Column-Level Constraints**
```sql
CREATE TABLE student (
  roll_no NUMBER PRIMARY KEY,
  name VARCHAR2(50) NOT NULL,
  age NUMBER CHECK (age >= 18),
  email VARCHAR2(100) UNIQUE,
  course_id NUMBER REFERENCES course(course_id)
);
```

**Example 2: Table-Level Constraints**
```sql
CREATE TABLE student (
  roll_no NUMBER,
  name VARCHAR2(50),
  age NUMBER,
  email VARCHAR2(100),
  course_id NUMBER,
  CONSTRAINT pk_student PRIMARY KEY (roll_no),
  CONSTRAINT chk_age CHECK (age >= 18),
  CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES course(course_id),
  CONSTRAINT uq_email UNIQUE (email)
);
```

---

### **3. Adding Constraints to Existing Tables**

**Add a NOT NULL constraint:**
```sql
ALTER TABLE student MODIFY name VARCHAR2(50) NOT NULL;
```

**Add a CHECK constraint:**
```sql
ALTER TABLE student ADD CONSTRAINT chk_age CHECK (age >= 18);
```

**Add a FOREIGN KEY:**
```sql
ALTER TABLE student ADD CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES course(course_id);
```

---

### **4. Dropping Constraints**

**Drop a constraint by name:**
```sql
ALTER TABLE student DROP CONSTRAINT fk_course;
```

---

### **5. Naming Conventions**

While naming constraints:
- Use `pk_` prefix for primary keys (`pk_student`)
- Use `fk_` for foreign keys (`fk_course`)
- Use `chk_` for check constraints (`chk_age`)
- Use `uq_` for unique constraints (`uq_email`)

---

### **6. Constraint Violations Example**

**Try to insert a NULL into a NOT NULL column:**
```sql
INSERT INTO student (roll_no, name) VALUES (101, NULL);
-- Error: cannot insert NULL into ("NAME")
```

**Try to insert a duplicate in UNIQUE column:**
```sql
INSERT INTO student (roll_no, name, email) VALUES (102, 'Tom', 'jane@example.com');
INSERT INTO student (roll_no, name, email) VALUES (103, 'Tim', 'jane@example.com');
-- Error: unique constraint violated
```

---
### **Creating Oracle Tables**

Creating tables is the first step in defining a database schema. You use the `CREATE TABLE` statement to define a new table with columns, data types, and optional constraints.

---

### **1. Syntax**

```sql
CREATE TABLE table_name (
  column1 datatype [constraint],
  column2 datatype [constraint],
  ...
);
```

---

### **2. Example: Simple Table Creation**

```sql
CREATE TABLE department (
  dept_id NUMBER PRIMARY KEY,
  dept_name VARCHAR2(50) NOT NULL,
  location VARCHAR2(100)
);
```

```sql
CREATE TABLE employee (
  emp_id NUMBER PRIMARY KEY,
  emp_name VARCHAR2(50) NOT NULL,
  salary NUMBER(10, 2),
  dept_id NUMBER,
  CONSTRAINT fk_dept FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);
```

---

### **3. Displaying Table Information**

You can view a table's structure and metadata using these commands:

```sql
-- View column details
DESC employee;

-- View all user tables
SELECT table_name FROM user_tables;

-- View constraints on a table
SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'EMPLOYEE';
```

---

### **4. Altering an Existing Table**

You can use the `ALTER TABLE` statement to modify the structure of a table after creation.

- **Add a column:**
```sql
ALTER TABLE employee ADD (email VARCHAR2(100));
```

- **Modify a column datatype:**
```sql
ALTER TABLE employee MODIFY (salary NUMBER(12, 2));
```

- **Drop a column:**
```sql
ALTER TABLE employee DROP COLUMN email;
```

- **Rename a column (starting from newer versions):**
```sql
ALTER TABLE employee RENAME COLUMN emp_name TO full_name;
```

---

### **5. Dropping, Renaming, and Truncating Tables**

- **Drop a table (deletes structure and data):**
```sql
DROP TABLE employee;
```

- **Rename a table:**
```sql
RENAME department TO dept;
```

- **Truncate a table (deletes all rows but keeps structure):**
```sql
TRUNCATE TABLE dept;
```

> **Note:** `DROP` is irreversible. `TRUNCATE` is faster than `DELETE` and cannot be rolled back.

---

### **6. Table Types**

| Type | Description |
|------|-------------|
| Permanent | Regular tables storing persistent data |
| Temporary | Data persists only during session or transaction |
| External | Tables mapping to external flat files |
| Global Temporary | Data is private to session |

**Example: Creating a Temporary Table**

```sql
CREATE GLOBAL TEMPORARY TABLE temp_employee (
  emp_id NUMBER,
  emp_name VARCHAR2(50)
) ON COMMIT DELETE ROWS;
```

---

### **7. Spooling in SQL\***

Spooling is used to save the output of SQL commands into a file.

```sql
SPOOL 'D:\sql_output.txt';

SELECT * FROM employee;

SPOOL OFF;
```

---

### **8. Common Error Codes**

| Error Code | Description |
|------------|-------------|
| ORA-00001  | Unique constraint violated |
| ORA-00904  | Invalid column name |
| ORA-00942  | Table or view does not exist |
| ORA-01400  | Cannot insert NULL |
| ORA-02291  | Integrity constraint violated - parent key not found |
| ORA-02292  | Integrity constraint violated - child record exists |

---
### **Working with Oracle Tables – DML Operations and Data Retrieval**

---

## **1. DML (Data Manipulation Language)**

DML commands let you manipulate data in existing tables:
- `INSERT` – Add new records
- `UPDATE` – Modify existing records
- `DELETE` – Remove records
- `SELECT` – Retrieve records

---

### **2. Adding a New Row (INSERT)**

```sql
-- Insert a full row
INSERT INTO employee (emp_id, emp_name, salary, dept_id)
VALUES (101, 'Arjun Reddy', 55000, 1);

-- Insert only specific columns (others will be NULL)
INSERT INTO employee (emp_id, emp_name)
VALUES (102, 'Sita Kumari');
```

---

### **3. Customized Prompts (for SQL\*Plus environments)**

You can use substitution variables to enter values dynamically:

```sql
-- This will prompt the user for values
INSERT INTO employee (emp_id, emp_name, salary, dept_id)
VALUES (&eid, '&ename', &sal, &did);
```

Use:
```sql
SET VERIFY ON;
```
To show the substituted values before execution.

---

### **4. Updating Existing Records (UPDATE)**

```sql
-- Give a raise to employee 101
UPDATE employee
SET salary = salary + 5000
WHERE emp_id = 101;
```

---

### **5. Deleting Records (DELETE)**

```sql
-- Remove employee with ID 102
DELETE FROM employee
WHERE emp_id = 102;
```

**Note**: Always use a `WHERE` clause to avoid deleting all rows.

---

### **6. Retrieving Data (SELECT)**

```sql
-- Retrieve all rows
SELECT * FROM employee;

-- Retrieve specific columns
SELECT emp_name, salary FROM employee;

-- Retrieve with condition
SELECT * FROM employee WHERE salary > 50000;

-- Using column aliases
SELECT emp_name AS "Employee Name", salary AS "Monthly Salary" FROM employee;
```

---

### **7. Arithmetic Operations in SELECT**

```sql
-- Add 500 to all salaries in the result
SELECT emp_name, salary, salary + 500 AS "Increased Salary"
FROM employee;
```

---

### **8. Restricting Data with WHERE Clause**

```sql
-- Fetch employees in department 1
SELECT * FROM employee WHERE dept_id = 1;

-- Use multiple conditions
SELECT * FROM employee
WHERE salary > 40000 AND dept_id = 2;
```

Operators: `=`, `>`, `<`, `>=`, `<=`, `!=`, `BETWEEN`, `LIKE`, `IN`, `IS NULL`

---

### **9. Sorting Data (ORDER BY)**

```sql
-- Sort by salary in ascending order
SELECT * FROM employee ORDER BY salary;

-- Sort by salary descending, then by name ascending
SELECT * FROM employee ORDER BY salary DESC, emp_name ASC;
```

---

### **10. Substitution Variables & DEFINE**

```sql
-- Substitution variable
SELECT * FROM employee WHERE emp_id = &empid;

-- DEFINE can set default values
DEFINE deptno = 1
SELECT * FROM employee WHERE dept_id = &deptno;
```

---

### **11. CASE Structure in SELECT**

```sql
SELECT emp_id, emp_name, salary,
  CASE
    WHEN salary >= 50000 THEN 'High'
    WHEN salary >= 30000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_grade
FROM employee;
```

---

# Unit -IV  
### SQL Concepts and  PL/SQL  
- Functions - aggregate functions, Built-in functions –numeric, date, string functions, set operations, sub-queries, correlated sub-queries, Use of group by, having, order by, join and its types, Exist, Any, All , view and its types. Transaction control commands – Commit, Rollback, Savepoint.  
- PL/SQL: A Programming Language: History, Fundamentals, Block Structure, Comments, Data Types, Other Data Types, Declaration, Assignment operation, Bind variables, Substitution Variables, Printing, Arithmetic Operators.   
- PL/SQL Control Structures and Embedded SQL : Control Structures, Nested Blocks, SQL in PL/SQL, Data Manipulation, Transaction Control statements.   
- PL/SQL Cursors and Exceptions: Cursors, Implicit & Explicit Cursors and Attributes, Cursor FOR loops, Cursor with Parameters, Cursor Variables, Exceptions, Types of Exceptions. Named Blocks: Procedures, Functions Packages, Triggers, Data Dictionary Views.  

---

### **Functions in SQL**

SQL provides several types of **functions** that can be used to manipulate and retrieve data efficiently. These functions are divided into two main categories:

#### 1. **Aggregate Functions**  
These operate on sets of rows and return a single result. Common aggregate functions:

| Function | Description |
|---------|-------------|
| `COUNT()` | Returns the number of rows |
| `SUM()` | Returns the total sum of a numeric column |
| `AVG()` | Returns the average value |
| `MAX()` | Returns the highest value |
| `MIN()` | Returns the lowest value |

**Example:**
```sql
SELECT COUNT(*) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MAX(hire_date) FROM employees;
```

---

#### 2. **Built-in Functions**

These work on individual row values and return a value for each row.

---

### **a. Numeric Functions**

| Function | Description |
|----------|-------------|
| `ABS(n)` | Absolute value of `n` |
| `CEIL(n)` | Smallest integer >= `n` |
| `FLOOR(n)` | Largest integer <= `n` |
| `MOD(m, n)` | Remainder of `m/n` |
| `ROUND(n, d)` | Rounds number `n` to `d` decimal places |
| `TRUNC(n, d)` | Truncates number `n` to `d` decimal places |
| `POWER(m, n)` | Returns m raised to the power n |

**Example:**
```sql
SELECT ABS(-10), MOD(17,5), POWER(2, 3) FROM dual;
```

---

### **b. Date Functions**

| Function | Description |
|----------|-------------|
| `SYSDATE` | Current date and time |
| `CURRENT_DATE` | Current date in session time zone |
| `ADD_MONTHS(date, n)` | Adds `n` months to a date |
| `MONTHS_BETWEEN(date1, date2)` | Returns months between two dates |
| `NEXT_DAY(date, 'DAY')` | Returns the next occurrence of the specified day |
| `LAST_DAY(date)` | Last day of the month of `date` |

**Example:**
```sql
SELECT SYSDATE, LAST_DAY(SYSDATE), ADD_MONTHS(SYSDATE, 2) FROM dual;
```

---

### **c. String Functions**

| Function | Description |
|----------|-------------|
| `UPPER(str)` | Converts to uppercase |
| `LOWER(str)` | Converts to lowercase |
| `INITCAP(str)` | Capitalizes first letter of each word |
| `LENGTH(str)` | Length of string |
| `SUBSTR(str, start, len)` | Substring |
| `INSTR(str, sub)` | Position of substring |
| `CONCAT(str1, str2)` | Concatenates two strings |
| `REPLACE(str, old, new)` | Replaces substring |

**Example:**
```sql
SELECT UPPER('oracle'), LENGTH('oracle'), SUBSTR('oracle', 2, 3) FROM dual;
```
---

### **Set Operations in SQL**

Set operations allow you to combine results from multiple `SELECT` queries. The number and order of columns must be the same in both queries.

#### 1. **UNION**
Combines results from two queries and removes duplicates.

```sql
SELECT dept_id FROM employees
UNION
SELECT dept_id FROM departments;
```

#### 2. **UNION ALL**
Combines results including duplicates.

```sql
SELECT dept_id FROM employees
UNION ALL
SELECT dept_id FROM departments;
```

#### 3. **INTERSECT**
Returns only the common rows.

```sql
SELECT dept_id FROM employees
INTERSECT
SELECT dept_id FROM departments;
```

#### 4. **MINUS**
Returns rows from the first query not found in the second.

```sql
SELECT dept_id FROM employees
MINUS
SELECT dept_id FROM departments;
```

---

### **Subqueries**

A **subquery** is a query nested inside another query.

#### a. **Simple Subquery**

```sql
SELECT * FROM employees
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'Sales');
```

#### b. **Correlated Subquery**
Executes once for each row in the outer query.

```sql
SELECT e1.emp_id, e1.name
FROM employees e1
WHERE salary > (SELECT AVG(salary)
                FROM employees e2
                WHERE e1.dept_id = e2.dept_id);
```

---

### **GROUP BY, HAVING, and ORDER BY**

#### `GROUP BY` groups rows with same values.
```sql
SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id;
```

#### `HAVING` filters grouped rows.
```sql
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 5;
```

#### `ORDER BY` sorts results.
```sql
SELECT * FROM employees
ORDER BY salary DESC;
```

---

### **JOINS in SQL**

Joins are used to retrieve related data from multiple tables.

#### a. **INNER JOIN**
Returns matching rows.

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

#### b. **LEFT OUTER JOIN**
Returns all rows from the left table and matching from right.

```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

#### c. **RIGHT OUTER JOIN**
Returns all from right, matching from left.

```sql
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

#### d. **FULL OUTER JOIN**
Returns all rows from both tables.

```sql
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;
```

---

### **Operators: EXISTS, ANY, ALL**

#### `EXISTS`
Checks for the existence of rows in a subquery.

```sql
SELECT name
FROM departments d
WHERE EXISTS (
  SELECT * FROM employees e
  WHERE e.dept_id = d.dept_id
);
```

#### `ANY` and `ALL`
Used with comparison operators.

```sql
-- ANY: if at least one row matches
SELECT name
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = 10);

-- ALL: if all rows match
SELECT name
FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 10);
```

---

### **Views and Its Types**

A **View** is a virtual table created using a SQL query. It doesn't store data but provides a window to access data from one or more tables.

#### **Creating a View**

```sql
CREATE VIEW emp_dept_view AS
SELECT e.emp_id, e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

#### **Querying a View**

```sql
SELECT * FROM emp_dept_view;
```

#### **Types of Views**

1. **Simple View**  
   - Based on a single table  
   - Does not contain functions or group functions  
   - Can perform DML (Insert, Update, Delete)

   ```sql
   CREATE VIEW emp_simple_view AS
   SELECT emp_id, name FROM employees;
   ```

2. **Complex View**  
   - Based on multiple tables  
   - May contain group functions or joins  
   - DML operations are usually restricted

   ```sql
   CREATE VIEW high_salary_view AS
   SELECT dept_id, AVG(salary) AS avg_salary
   FROM employees
   GROUP BY dept_id
   HAVING AVG(salary) > 50000;
   ```

#### **Modifying a View**

```sql
CREATE OR REPLACE VIEW emp_dept_view AS
SELECT e.emp_id, e.name, e.salary, d.dept_name, d.location
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

#### **Dropping a View**

```sql
DROP VIEW emp_dept_view;
```

---

### **Transaction Control Commands**

Transactions are sequences of SQL statements treated as a single unit. Transaction control commands manage changes made by DML statements.

#### 1. **COMMIT**
Saves all changes made in the current transaction.

```sql
DELETE FROM employees WHERE dept_id = 20;
COMMIT;
```

#### 2. **ROLLBACK**
Undoes all changes since the last COMMIT.

```sql
DELETE FROM employees WHERE dept_id = 30;
ROLLBACK;
```

#### 3. **SAVEPOINT**
Marks a point to which you can roll back.

```sql
SAVEPOINT before_delete;
DELETE FROM employees WHERE dept_id = 40;
ROLLBACK TO before_delete;
```

#### 4. **AUTOCOMMIT in SQL Developer/Tools**
By default, some tools auto-commit changes after each DML unless explicitly turned off. Use manual `COMMIT` or `ROLLBACK` when needed.

---

That finishes the SQL portion.  
Shall we move into **PL/SQL** now? It’s about programming inside the database with blocks, variables, loops, cursors, exceptions, and more. Ready?

Perfect! Let’s begin the **PL/SQL** section of **Unit IV** and follow your content list exactly. We’ll go step by step and in **extreme detail**.

---

## **PL/SQL: A Programming Language**

---

### **1. History of PL/SQL**

- **PL/SQL** stands for **Procedural Language/Structured Query Language**.
- Developed by Oracle to provide procedural capabilities (like loops, conditions) to SQL.
- Introduced in Oracle version 6.
- It combines the **data manipulation power of SQL** with **the procedural power of programming languages** like Ada, Pascal, etc.

---

### **2. Fundamentals of PL/SQL**

PL/SQL is structured into **blocks**. Each block has:

- **Declaration section** (optional)
- **Execution section** (mandatory)
- **Exception handling section** (optional)

#### **Basic Block Structure**

```sql
DECLARE
   -- Declarations (variables, types, etc.)
BEGIN
   -- Executable statements
EXCEPTION
   -- Exception handling
END;
```

---

### **3. Comments in PL/SQL**

You can use comments for code clarity:

```sql
-- Single line comment

/*
Multi-line
comment
*/
```

---

### **4. Data Types in PL/SQL**

PL/SQL supports the following data types:

- `NUMBER(n, d)` – Fixed-point number
- `VARCHAR2(size)` – Variable-length string
- `CHAR(size)` – Fixed-length string
- `DATE` – Date and time
- `BOOLEAN` – True/False/NULL
- `%TYPE` – Adopts the data type of a column or variable
- `%ROWTYPE` – Record type matching a table’s row structure

#### **Example:**

```sql
DECLARE
   emp_name VARCHAR2(50);
   emp_salary NUMBER(7,2);
   hire_date DATE;
   is_active BOOLEAN := TRUE;
BEGIN
   NULL;
END;
```

---

### **5. Declaration and Assignment**

#### **Declaration**

```sql
DECLARE
   emp_id NUMBER;
   emp_name VARCHAR2(30);
```

#### **Assignment using `:=`**

```sql
BEGIN
   emp_id := 101;
   emp_name := 'Amit';
```

You can also assign values from SQL queries:

```sql
SELECT name INTO emp_name FROM employees WHERE emp_id = 101;
```

---

### **6. Bind Variables vs Substitution Variables**

#### **Bind Variables (`:`)**

- Used in tools like SQL*Plus and SQL Developer for passing values to PL/SQL blocks.
- Good for performance (prevent parsing overhead).

```sql
VARIABLE emp_id NUMBER;
BEGIN
   :emp_id := 100;
END;
```

#### **Substitution Variables (`&`)**

- Used for user input at runtime.

```sql
DECLARE
   name VARCHAR2(20);
BEGIN
   name := '&Enter_name';
   DBMS_OUTPUT.PUT_LINE('Hello, ' || name);
END;
```

---

### **7. Printing Output**

Use `DBMS_OUTPUT.PUT_LINE` to display values:

```sql
BEGIN
   DBMS_OUTPUT.PUT_LINE('Hello from PL/SQL!');
END;
```

**Enable Output:**

```sql
SET SERVEROUTPUT ON;
```

---

### **8. Arithmetic Operators**

PL/SQL supports common arithmetic operations:

| Operator | Description    |
|----------|----------------|
| `+`      | Addition        |
| `-`      | Subtraction     |
| `*`      | Multiplication  |
| `/`      | Division        |
| `**`     | Exponentiation  |

#### **Example:**

```sql
DECLARE
   a NUMBER := 10;
   b NUMBER := 5;
   c NUMBER;
BEGIN
   c := a + b;
   DBMS_OUTPUT.PUT_LINE('Sum = ' || c);
END;
```

---

## **PL/SQL Control Structures and Embedded SQL**

This section introduces programming logic into PL/SQL through **conditional branching**, **loops**, and **embedding SQL** statements inside PL/SQL.

---

### **1. Control Structures**

PL/SQL supports the following control structures:

---

#### **1.1 IF Statement**

Used to execute a block of code conditionally.

##### **Syntax:**

```sql
IF condition THEN
   -- statements
END IF;
```

##### **IF-ELSE:**

```sql
IF condition THEN
   -- true block
ELSE
   -- false block
END IF;
```

##### **IF-ELSIF-ELSE:**

```sql
IF condition1 THEN
   -- block 1
ELSIF condition2 THEN
   -- block 2
ELSE
   -- default block
END IF;
```

##### **Example:**

```sql
DECLARE
   marks NUMBER := 85;
BEGIN
   IF marks >= 90 THEN
      DBMS_OUTPUT.PUT_LINE('Grade: A');
   ELSIF marks >= 75 THEN
      DBMS_OUTPUT.PUT_LINE('Grade: B');
   ELSE
      DBMS_OUTPUT.PUT_LINE('Grade: C');
   END IF;
END;
```

---

#### **1.2 CASE Statement**

##### **Simple CASE**

```sql
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

##### **Searched CASE**

```sql
DECLARE
   salary NUMBER := 60000;
BEGIN
   CASE
      WHEN salary > 80000 THEN DBMS_OUTPUT.PUT_LINE('High salary');
      WHEN salary > 50000 THEN DBMS_OUTPUT.PUT_LINE('Medium salary');
      ELSE DBMS_OUTPUT.PUT_LINE('Low salary');
   END CASE;
END;
```

---

### **2. Loops in PL/SQL**

Loops help repeat a block of code multiple times.

---

#### **2.1 Simple LOOP**

```sql
DECLARE
   i NUMBER := 1;
BEGIN
   LOOP
      DBMS_OUTPUT.PUT_LINE('i = ' || i);
      i := i + 1;
      EXIT WHEN i > 5;
   END LOOP;
END;
```

---

#### **2.2 WHILE LOOP**

```sql
DECLARE
   i NUMBER := 1;
BEGIN
   WHILE i <= 5 LOOP
      DBMS_OUTPUT.PUT_LINE('i = ' || i);
      i := i + 1;
   END LOOP;
END;
```

---

#### **2.3 FOR LOOP**

```sql
BEGIN
   FOR i IN 1..5 LOOP
      DBMS_OUTPUT.PUT_LINE('i = ' || i);
   END LOOP;
END;
```

---

### **3. Nested Blocks**

PL/SQL supports nesting of blocks.

```sql
DECLARE
   x NUMBER := 10;
BEGIN
   DBMS_OUTPUT.PUT_LINE('Outer Block');
   DECLARE
      x NUMBER := 20;
   BEGIN
      DBMS_OUTPUT.PUT_LINE('Inner x = ' || x);  -- 20
   END;
   DBMS_OUTPUT.PUT_LINE('Outer x = ' || x);      -- 10
END;
```

---

### **4. Embedded SQL in PL/SQL**

You can use SQL statements like **SELECT**, **INSERT**, **UPDATE**, **DELETE** inside PL/SQL.

---

#### **SELECT INTO (for single row fetch)**

```sql
DECLARE
   emp_name employees.name%TYPE;
BEGIN
   SELECT name INTO emp_name
   FROM employees
   WHERE emp_id = 101;

   DBMS_OUTPUT.PUT_LINE('Employee Name: ' || emp_name);
END;
```

> Important: Always make sure SELECT INTO returns exactly one row, or it throws `NO_DATA_FOUND` or `TOO_MANY_ROWS`.

---

#### **INSERT in PL/SQL**

```sql
BEGIN
   INSERT INTO employees(emp_id, name, salary)
   VALUES(111, 'Sneha', 50000);
END;
```

---

#### **UPDATE in PL/SQL**

```sql
BEGIN
   UPDATE employees
   SET salary = salary + 5000
   WHERE emp_id = 111;
END;
```

---

#### **DELETE in PL/SQL**

```sql
BEGIN
   DELETE FROM employees
   WHERE emp_id = 111;
END;
```

---

#### **Transaction Control**

Use these statements in PL/SQL as needed:

```sql
COMMIT;
ROLLBACK;
SAVEPOINT before_change;
ROLLBACK TO before_change;
```

---

## **PL/SQL Cursors and Exceptions**

This section is crucial for handling **multi-row queries** (via cursors) and **error handling** (via exceptions) in PL/SQL.

---

## **1. Cursors in PL/SQL**

A **cursor** is a pointer to the result set of a query. When a SELECT statement returns more than one row, you must use a cursor to process each row.

---

### **Types of Cursors**

- **Implicit Cursor** – Used by default for single-row DML operations.
- **Explicit Cursor** – Declared by the programmer for handling multi-row queries.
- **Cursor FOR Loop** – Simplified syntax for looping through a cursor.
- **Cursor with Parameters** – Used to pass values to a cursor.
- **Cursor Variables** – Also known as REF cursors, useful for dynamic queries.

---

### **1.1 Implicit Cursor**

PL/SQL automatically declares an implicit cursor for **INSERT**, **UPDATE**, **DELETE**, and **SELECT INTO** statements.

```sql
BEGIN
   UPDATE employees SET salary = salary + 5000 WHERE emp_id = 101;

   IF SQL%ROWCOUNT > 0 THEN
      DBMS_OUTPUT.PUT_LINE('Record updated successfully.');
   ELSE
      DBMS_OUTPUT.PUT_LINE('No record updated.');
   END IF;
END;
```

---

### **1.2 Explicit Cursor**

You declare an explicit cursor when you want to process multiple rows one by one.

#### **Steps:**
1. Declare the cursor.
2. Open the cursor.
3. Fetch from the cursor.
4. Close the cursor.

```sql
DECLARE
   CURSOR emp_cursor IS
      SELECT emp_id, name FROM employees;
   v_id employees.emp_id%TYPE;
   v_name employees.name%TYPE;
BEGIN
   OPEN emp_cursor;
   LOOP
      FETCH emp_cursor INTO v_id, v_name;
      EXIT WHEN emp_cursor%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE('ID: ' || v_id || ', Name: ' || v_name);
   END LOOP;
   CLOSE emp_cursor;
END;
```

---

### **1.3 Cursor FOR Loop**

A shortcut to handle open, fetch, and close steps automatically.

```sql
BEGIN
   FOR emp_rec IN (SELECT emp_id, name FROM employees) LOOP
      DBMS_OUTPUT.PUT_LINE('ID: ' || emp_rec.emp_id || ', Name: ' || emp_rec.name);
   END LOOP;
END;
```

---

### **1.4 Cursor with Parameters**

Allows passing values dynamically to the cursor.

```sql
DECLARE
   CURSOR emp_cursor (p_dept_id NUMBER) IS
      SELECT emp_id, name FROM employees WHERE dept_id = p_dept_id;
   v_id employees.emp_id%TYPE;
   v_name employees.name%TYPE;
BEGIN
   OPEN emp_cursor(10);
   LOOP
      FETCH emp_cursor INTO v_id, v_name;
      EXIT WHEN emp_cursor%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE('ID: ' || v_id || ', Name: ' || v_name);
   END LOOP;
   CLOSE emp_cursor;
END;
```

---

### **1.5 Cursor Attributes**

| Attribute         | Description                                     |
|------------------|-------------------------------------------------|
| `%FOUND`         | Returns TRUE if fetch returns a row             |
| `%NOTFOUND`      | Returns TRUE if fetch does NOT return a row     |
| `%ROWCOUNT`      | Returns number of rows fetched so far           |
| `%ISOPEN`        | Returns TRUE if cursor is open                  |

---

## **2. Exceptions in PL/SQL**

**Exception**: An error condition during program execution.

PL/SQL has two types of exceptions:
- **Predefined (Standard)** – Built-in exceptions like `NO_DATA_FOUND`, `TOO_MANY_ROWS`, etc.
- **User-defined** – Custom exceptions declared by the programmer.

---

### **2.1 Predefined Exceptions**

```sql
BEGIN
   SELECT salary INTO v_sal FROM employees WHERE emp_id = 999;
   DBMS_OUTPUT.PUT_LINE('Salary: ' || v_sal);
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Employee not found!');
   WHEN TOO_MANY_ROWS THEN
      DBMS_OUTPUT.PUT_LINE('More than one employee found!');
END;
```

---

### **2.2 User-defined Exceptions**

```sql
DECLARE
   insufficient_salary EXCEPTION;
   salary NUMBER := 1000;
BEGIN
   IF salary < 2000 THEN
      RAISE insufficient_salary;
   END IF;
EXCEPTION
   WHEN insufficient_salary THEN
      DBMS_OUTPUT.PUT_LINE('Salary too low!');
END;
```

---

### **2.3 RAISE_APPLICATION_ERROR**

Used to raise custom error codes and messages.

```sql
BEGIN
   RAISE_APPLICATION_ERROR(-20001, 'This is a user-defined error.');
END;
```

---

## **PL/SQL Named Blocks: Procedures, Functions, Packages, Triggers, Data Dictionary Views**

Named blocks are reusable, stored blocks of PL/SQL code in the database that can be invoked when needed. This makes code modular, organized, and optimized for performance.

---

## **1. Procedures**

A **procedure** is a subprogram that performs an action. It may or may not take parameters, and it **does not return** a value (unlike functions).

### **Syntax**
```sql
CREATE OR REPLACE PROCEDURE procedure_name (
   param1 IN datatype,
   param2 OUT datatype
) IS
BEGIN
   -- procedure body
END;
```

### **Example**
```sql
CREATE OR REPLACE PROCEDURE update_salary (
   p_emp_id IN employees.emp_id%TYPE,
   p_increment IN NUMBER
) IS
BEGIN
   UPDATE employees SET salary = salary + p_increment WHERE emp_id = p_emp_id;
   DBMS_OUTPUT.PUT_LINE('Salary Updated');
END;
```

### **To Execute:**
```sql
BEGIN
   update_salary(101, 5000);
END;
```

---

## **2. Functions**

A **function** is similar to a procedure, but it **returns a single value**.

### **Syntax**
```sql
CREATE OR REPLACE FUNCTION function_name (
   param1 IN datatype
) RETURN return_type IS
BEGIN
   -- function body
   RETURN some_value;
END;
```

### **Example**
```sql
CREATE OR REPLACE FUNCTION get_salary (
   p_emp_id IN employees.emp_id%TYPE
) RETURN NUMBER IS
   v_salary NUMBER;
BEGIN
   SELECT salary INTO v_salary FROM employees WHERE emp_id = p_emp_id;
   RETURN v_salary;
END;
```

### **To Call in SQL or PL/SQL:**
```sql
BEGIN
   DBMS_OUTPUT.PUT_LINE('Salary: ' || get_salary(101));
END;
```

---

## **3. Packages**

A **package** is a group of related procedures, functions, variables, and cursors stored together as a single unit.

### **Components:**
- **Package Specification** – Declares procedures/functions.
- **Package Body** – Defines the logic.

### **Example**
```sql
-- Specification
CREATE OR REPLACE PACKAGE employee_pkg IS
   PROCEDURE update_salary(p_emp_id IN NUMBER, p_increment IN NUMBER);
   FUNCTION get_salary(p_emp_id IN NUMBER) RETURN NUMBER;
END employee_pkg;
```

```sql
-- Body
CREATE OR REPLACE PACKAGE BODY employee_pkg IS

   PROCEDURE update_salary(p_emp_id IN NUMBER, p_increment IN NUMBER) IS
   BEGIN
      UPDATE employees SET salary = salary + p_increment WHERE emp_id = p_emp_id;
   END;

   FUNCTION get_salary(p_emp_id IN NUMBER) RETURN NUMBER IS
      v_salary NUMBER;
   BEGIN
      SELECT salary INTO v_salary FROM employees WHERE emp_id = p_emp_id;
      RETURN v_salary;
   END;

END employee_pkg;
```

---

## **4. Triggers**

A **trigger** is a stored block that is automatically executed **in response to a specific event** (e.g., INSERT, UPDATE, DELETE) on a table or view.

### **Syntax**
```sql
CREATE OR REPLACE TRIGGER trigger_name
BEFORE INSERT ON table_name
FOR EACH ROW
BEGIN
   -- trigger body
END;
```

### **Example**
```sql
CREATE OR REPLACE TRIGGER before_insert_employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
   DBMS_OUTPUT.PUT_LINE('Inserting new employee: ' || :NEW.name);
END;
```

---

## **5. Data Dictionary Views**

These are **read-only system views** that provide metadata (data about the database structure).

### **Common Views:**

| View Name | Purpose |
|-----------|---------|
| `USER_TABLES` | Shows tables owned by the current user |
| `ALL_TABLES` | Shows tables accessible to the user |
| `DBA_TABLES` | Shows all tables in the database (admin only) |
| `USER_TAB_COLUMNS` | Shows column info for user's tables |
| `USER_CONSTRAINTS` | Info about constraints |
| `USER_TRIGGERS` | Info about triggers |
| `USER_PROCEDURES` | Lists all stored procedures |
| `USER_VIEWS` | Info about user-defined views |

### **Example**
```sql
SELECT table_name FROM user_tables;
SELECT column_name, data_type FROM user_tab_columns WHERE table_name = 'EMPLOYEES';
```

---

