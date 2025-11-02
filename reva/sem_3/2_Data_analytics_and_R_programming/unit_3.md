# Unit - 3

## Introduction to Hive and Pig
- Hive: introduction
- Architecture
- Data types
- File Formats
- Hive Query
- Language Statements
- Partitions
- Bucketing
- Views
- Sub-Query
- Joins
- Aggregations
- Group by and Having
- RC File Implementation
- Hive User Defined Function

- Serialization and Deserialization
- Pig: Introduction
- Anatomy
- Features
- Philosophy
- Use Case for Pig
- Pig Latin Overview
- Pig Primitive Data Types
- Running Pig
- Execution Modes of Pig
- HDFS commands
- Relational Operators
- Eval Function
- Complen Data Types
- Piggy bank
- User-Defined Functions
- Parameter Substitution
- Diagonstic Operators
- Word Count Example using Pig
- Pig at Yahoo!
- Pig Versus Hive

---
---

# 🐝 **Hive: Introduction**

### 🧩 **What is Apache Hive?**

* **Hive** is a **data warehousing and SQL-like query system** built on top of **Hadoop**.
* It allows users to **analyze large datasets** stored in **HDFS (Hadoop Distributed File System)** using a language similar to SQL, known as **HiveQL**.
* Developed originally by **Facebook**, later **open-sourced by Apache**.

---

### ⚙️ **Key Features**

1. **SQL-like Interface** → Uses HiveQL for querying instead of complex Java MapReduce code.
2. **Data Warehouse Infrastructure** → Designed for summarization, querying, and analysis.
3. **Scalability** → Handles large datasets efficiently.
4. **Extensibility** → Supports user-defined functions (UDFs) for custom operations.
5. **Integration with Hadoop Ecosystem** → Runs on top of HDFS and uses MapReduce, Tez, or Spark as execution engines.
6. **Schema-on-Read** → Defines schema at query time, making it flexible for unstructured data.

---

### 🧠 **How Hive Works**

1. **HiveQL Query** → User writes SQL-like query.
2. **Compiler** → Converts HiveQL into **MapReduce**, **Tez**, or **Spark** jobs.
3. **Execution Engine** → Executes the jobs on **Hadoop cluster**.
4. **Results** → Output returned to the user.

---

### 🏗️ **Hive Components**

* **Metastore** → Stores metadata (table schema, partitions, etc.)
* **Driver** → Manages session and query execution.
* **Compiler** → Converts HiveQL into execution plan.
* **Execution Engine** → Submits jobs to Hadoop.
* **CLI / JDBC / ODBC Interface** → For user interaction.

---

### 📂 **Hive Data Model**

* **Database** → Collection of tables.
* **Table** → Data stored in rows and columns (like SQL).
* **Partition** → Divides tables based on column values for faster access.
* **Bucket** → Subdivides partitions for more fine-grained management.

---

### 📊 **Use Cases**

* Log analysis
* Data summarization
* Business intelligence reporting
* ETL (Extract, Transform, Load) processes

---

### 💡 **Example**

```sql
CREATE TABLE sales (
    id INT,
    product STRING,
    amount FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

SELECT product, SUM(amount)
FROM sales
GROUP BY product;
```

---

### 🧾 **In Short**

> **Hive = SQL interface for Hadoop**
> It simplifies Big Data querying and analytics by turning SQL queries into MapReduce or Spark jobs.

---

# 🏗️ **Hive Architecture**

Apache **Hive Architecture** defines how Hive interacts with the **Hadoop ecosystem** to store, process, and analyze large datasets.

---

### 🧩 **Overview**

Hive follows a **client–server architecture**, where users submit **HiveQL queries** through an interface, and Hive converts those queries into **MapReduce**, **Tez**, or **Spark** jobs executed on **Hadoop**.

---

### ⚙️ **Main Components of Hive Architecture**

#### 1. **User Interface (UI)**

* Provides different ways for users to interact with Hive:

  * **CLI (Command Line Interface)**
  * **Web UI**
  * **JDBC/ODBC Drivers**
* Users submit **HiveQL** queries using these interfaces.

---

#### 2. **Driver**

* The **controller** that manages the entire query execution process.
* Responsibilities:

  * Receives queries from the user.
  * Sends them to the **compiler**.
  * Maintains session handles and execution states.
  * Collects results and returns them to the user.

---

#### 3. **Compiler**

* **Parses**, **analyzes**, and **compiles** HiveQL queries.
* Converts HiveQL into **execution plans** (DAG of MapReduce, Tez, or Spark jobs).
* Performs **semantic analysis** and interacts with the **Metastore** to validate table and column names.

---

#### 4. **Optimizer**

* Applies **optimization techniques** to the execution plan such as:

  * Predicate pushdown
  * Partition pruning
  * Join optimization
* Goal: Improve performance and minimize data movement.

---

#### 5. **Metastore**

* A **central repository** that stores **metadata** about Hive objects.
* Information stored includes:

  * Table names, columns, and data types
  * Database schemas
  * Table location in HDFS
  * Partition and bucket details
* Typically uses **RDBMS** like MySQL or Derby to store metadata.

---

#### 6. **Execution Engine**

* The component that **executes the execution plan** generated by the compiler.
* Communicates with Hadoop components such as:

  * **JobTracker / ResourceManager (YARN)** – for job scheduling.
  * **TaskTracker / NodeManager** – for task execution.
* Translates the plan into a series of **MapReduce**, **Tez**, or **Spark** tasks.

---

#### 7. **HDFS (Hadoop Distributed File System)**

* The **storage layer** for Hive.
* All Hive tables and data files are stored in **HDFS**.
* Provides **fault tolerance**, **scalability**, and **high throughput** access to data.

---

### 🔄 **Data Flow in Hive**

1. User submits a **HiveQL query** via CLI or another interface.
2. **Driver** sends the query to the **Compiler**.
3. **Compiler** checks metadata from the **Metastore** and generates an execution plan.
4. **Execution Engine** executes the plan as MapReduce (or Tez/Spark) jobs on **HDFS**.
5. Results are fetched back and displayed to the user.

---

### 🧠 **Hive Architecture Diagram (Text-based)**

```
+----------------------------+
|        User Interface      |
| (CLI / Web UI / JDBC/ODBC) |
+-------------+--------------+
              |
              v
+----------------------------+
|          Driver            |
| (Session & Query Manager)  |
+-------------+--------------+
              |
              v
+----------------------------+
|          Compiler          |
|  (Parse, Plan, Optimize)   |
+-------------+--------------+
              |
              v
+----------------------------+
|        Execution Engine    |
| (MapReduce / Tez / Spark)  |
+-------------+--------------+
              |
              v
+----------------------------+
|         Hadoop HDFS        |
|   (Storage for Data Files) |
+----------------------------+
              ^
              |
+----------------------------+
|         Metastore          |
| (Metadata about Tables)    |
+----------------------------+
```

---

### 🧾 **In Summary**

| **Component**        | **Function**                       |
| -------------------- | ---------------------------------- |
| **User Interface**   | Accepts HiveQL queries             |
| **Driver**           | Manages execution flow             |
| **Compiler**         | Converts query into execution plan |
| **Metastore**        | Stores metadata                    |
| **Execution Engine** | Executes jobs on Hadoop            |
| **HDFS**             | Stores actual data                 |

---

## 🧮 **Hive Data Types**

Hive supports a wide range of **data types** that are used to define the structure of tables, columns, and expressions.
They are mainly categorized into **Primitive**, **Complex**, and **Collection** types.

---

### 🧱 **1. Primitive Data Types**

Primitive data types are the **basic building blocks** used to store single values like numbers, strings, or dates.

| **Category**        | **Data Type** | **Description**                           | **Example**                 |
| ------------------- | ------------- | ----------------------------------------- | --------------------------- |
| **Numeric Types**   | `TINYINT`     | 1-byte integer (-128 to 127)              | 120                         |
|                     | `SMALLINT`    | 2-byte integer                            | 25000                       |
|                     | `INT`         | 4-byte integer                            | 123456                      |
|                     | `BIGINT`      | 8-byte integer                            | 1234567890                  |
|                     | `FLOAT`       | Single precision (4-byte) floating number | 10.5                        |
|                     | `DOUBLE`      | Double precision (8-byte) floating number | 1234.567                    |
| **String Types**    | `STRING`      | Sequence of characters (variable length)  | 'hello'                     |
|                     | `CHAR(n)`     | Fixed-length string                       | 'abc' (CHAR(5)) → `'abc  '` |
|                     | `VARCHAR(n)`  | Variable-length string (max length = n)   | 'hive'                      |
| **Date/Time Types** | `DATE`        | Stores date (YYYY-MM-DD)                  | '2025-11-01'                |
|                     | `TIMESTAMP`   | Stores date and time                      | '2025-11-01 14:20:00'       |
|                     | `INTERVAL`    | Time intervals                            | `INTERVAL '2' DAYS`         |
| **Boolean Type**    | `BOOLEAN`     | True or False value                       | TRUE                        |
| **Binary Type**     | `BINARY`      | Byte array for binary data                | (e.g., image bytes)         |

---

### 🧩 **2. Complex Data Types**

Complex data types in Hive allow **nested or structured data** — useful for representing JSON-like or hierarchical data.

| **Data Type** | **Description**                                 | **Example**                           |
| ------------- | ----------------------------------------------- | ------------------------------------- |
| **ARRAY**     | Ordered collection of elements of the same type | `ARRAY('CSE','ECE','ME')`             |
| **MAP**       | Key-value pairs (keys are unique)               | `MAP('name','Yuvraj','age','21')`     |
| **STRUCT**    | Group of different types (like a record)        | `STRUCT('Yuvraj',21,'India')`         |
| **UNIONTYPE** | Holds one value from a list of possible types   | `create uniontype<int,double,string>` |

---

### 🧰 **3. Collection Data Types (User-defined structures)**

These are combinations of the above **complex types**, often used to represent real-world structured data.

Example:

```sql
CREATE TABLE student (
  id INT,
  name STRING,
  marks ARRAY<INT>,
  address STRUCT<city:STRING, pincode:INT>,
  phone MAP<STRING, STRING>
);
```

Here:

* `marks` → array of integers
* `address` → struct with two fields
* `phone` → map with key-value pairs like `'home' → '9999999999'`

---

### 📘 **Example: Using Data Types in Hive**

```sql
CREATE TABLE employee (
  emp_id INT,
  emp_name STRING,
  salary DOUBLE,
  doj DATE,
  skills ARRAY<STRING>,
  address STRUCT<city:STRING, state:STRING, zip:INT>,
  certifications MAP<STRING, STRING>
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
MAP KEYS TERMINATED BY ':';
```

**Explanation:**

* Each employee has multiple `skills` → stored in an array.
* Their `address` is structured.
* `certifications` are stored as key-value pairs.

---

### 🧠 **Visualization of Complex Data**

```
Employee Record
{
  emp_id: 101,
  emp_name: "Yuvraj",
  salary: 75000.0,
  doj: "2023-06-10",
  skills: ["Python", "Hive", "Hadoop"],
  address: {
    city: "Bengaluru",
    state: "Karnataka",
    zip: 560064
  },
  certifications: {
    "AWS": "2024",
    "Azure": "2023"
  }
}
```

---

### ✅ **In Summary**

| **Category**   | **Data Types**                            | **Purpose**                  |
| -------------- | ----------------------------------------- | ---------------------------- |
| **Primitive**  | INT, STRING, FLOAT, DOUBLE, DATE, BOOLEAN | Store basic values           |
| **Complex**    | ARRAY, MAP, STRUCT, UNIONTYPE             | Store nested data            |
| **Collection** | Combinations of complex types             | Real-world hierarchical data |

---

## 🗃️ **Hive File Formats**

Hive supports multiple **file formats** for storing data in **HDFS (Hadoop Distributed File System)**.
Choosing the right file format affects **performance, storage efficiency, and query speed**.

---

### 🧩 **1. What is a File Format in Hive?**

A **file format** determines **how data is stored** on disk and **how Hive reads/writes** that data.

It defines:

* Data **serialization and deserialization** (SerDe)
* **Compression** techniques
* **Storage structure** (row-based or column-based)

---

### 🧱 **2. Types of File Formats in Hive**

| **Category**         | **File Format**  | **Storage Type** | **Description**                                                           |
| -------------------- | ---------------- | ---------------- | ------------------------------------------------------------------------- |
| **Text-based**       | **TEXTFILE**     | Row-based        | Default format, simple to use, human-readable.                            |
|                      | **CSVFILE**      | Row-based        | Stores comma-separated values, easy for import/export.                    |
| **Binary Row-based** | **SEQUENCEFILE** | Row-based        | Binary format with key-value pairs; supports compression.                 |
| **Columnar Formats** | **RCFILE**       | Column-based     | Splits data into columns for efficient reads.                             |
|                      | **ORCFILE**      | Column-based     | Highly optimized, supports compression, indexing, and predicate pushdown. |
|                      | **PARQUET**      | Column-based     | Cross-platform format (used in Spark, Impala, Hive); great for analytics. |
| **JSON Format**      | **JSONFILE**     | Row-based        | Stores data in JSON structure (semi-structured data).                     |
| **AVRO Format**      | **AVRO**         | Row-based        | Schema evolution support, used in data serialization between systems.     |

---

### 🧠 **3. Detailed Explanation of Each File Format**

#### 📝 **a) TEXTFILE**

* Default Hive file format.
* Stores data as plain text — one record per line.
* **Advantages:**

  * Easy to read and debug.
  * Supported by most tools.
* **Disadvantages:**

  * Large size, no compression.
  * Slower query performance.

**Example:**

```sql
CREATE TABLE employees (
  id INT, name STRING, salary DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

---

#### 📄 **b) SEQUENCEFILE**

* Binary key-value format from Hadoop.
* Stores data in **binary format** for faster read/write.
* Supports **block-level compression**.
* Used internally by Hadoop and MapReduce.

**Example:**

```sql
CREATE TABLE seq_emp (
  id INT, name STRING
)
STORED AS SEQUENCEFILE;
```

---

#### 🧱 **c) RCFILE (Record Columnar File)**

* First **column-oriented** file format in Hive.
* Stores data in **columnar chunks** within row groups.
* Improves read efficiency when only a few columns are needed.
* Supports **compression and skipping** of irrelevant data blocks.

**Best for:** Analytical workloads with selective queries.

**Example:**

```sql
CREATE TABLE rc_emp (
  id INT, name STRING, dept STRING
)
STORED AS RCFILE;
```

---

#### ⚙️ **d) ORC (Optimized Row Columnar)**

* Developed by Hortonworks for **high performance**.
* Highly **optimized columnar storage**.
* Features:

  * **Compression (Snappy, Zlib, LZO)**
  * **Predicate Pushdown** (reads only needed data)
  * **Indexes and lightweight metadata**
  * **Splittable** for parallel processing

**Advantages:**

* Faster query performance.
* Smaller storage footprint.
* Best suited for large data warehouses.

**Example:**

```sql
CREATE TABLE orc_emp (
  id INT, name STRING, dept STRING
)
STORED AS ORC;
```

---

#### 🧩 **e) PARQUET**

* Open-source **columnar format** developed by Cloudera and Twitter.
* Used across multiple ecosystems: Spark, Impala, Hive, etc.
* Supports **nested data** and **schema evolution**.
* Provides **efficient compression** and **fast columnar access**.

**Example:**

```sql
CREATE TABLE parquet_emp (
  id INT, name STRING, dept STRING
)
STORED AS PARQUET;
```

---

#### 🧠 **f) AVRO**

* Row-based binary format with **self-describing schema** (schema stored with data).
* Great for **data exchange** between systems.
* Supports **schema evolution** (fields can be added/removed safely).

**Example:**

```sql
CREATE TABLE avro_emp (
  id INT, name STRING, dept STRING
)
STORED AS AVRO;
```

---

#### 🌐 **g) JSON**

* Stores semi-structured data as JSON records.
* Ideal for applications generating JSON logs.
* Slower compared to ORC/Parquet for large datasets.

**Example:**

```sql
CREATE TABLE json_emp (
  id INT, name STRING, dept STRING
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE;
```

---

### 📊 **4. Comparison Table of File Formats**

| **Format**   | **Storage Type** | **Compression**   | **Performance** | **Readability** | **Use Case**             |
| ------------ | ---------------- | ----------------- | --------------- | --------------- | ------------------------ |
| TEXTFILE     | Row              | None (manual)     | Low             | High            | Simple datasets          |
| SEQUENCEFILE | Row              | Yes               | Medium          | Low             | Key-value storage        |
| RCFILE       | Column           | Yes               | Medium          | Low             | Columnar queries         |
| ORC          | Column           | Yes (Snappy/Zlib) | Very High       | Low             | Large analytics tables   |
| PARQUET      | Column           | Yes (Snappy/Gzip) | Very High       | Low             | Cross-platform analytics |
| AVRO         | Row              | Yes               | High            | Medium          | Schema evolution         |
| JSON         | Row              | No                | Low             | High            | Semi-structured data     |

---

### 🔍 **5. Choosing the Right File Format**

| **Goal**                                | **Recommended Format** |
| --------------------------------------- | ---------------------- |
| Human-readable, simple files            | TEXTFILE / CSV         |
| Efficient analytics & query performance | ORC / PARQUET          |
| Cross-platform compatibility            | PARQUET                |
| Schema evolution                        | AVRO                   |
| Key-value data storage                  | SEQUENCEFILE           |

---

### 🧠 **Summary**

* Hive supports **row-based and column-based** file formats.
* **ORC** and **Parquet** are **best for big data analytics** due to compression and query optimization.
* Choosing the right file format improves both **storage efficiency** and **processing speed**.

---

## 🐝 **Hive Query Language (HQL)**

Hive uses a **SQL-like language** called **HQL (Hive Query Language)** to interact with data stored in Hadoop.
It allows you to **create**, **query**, **analyze**, and **manage** large datasets stored in **HDFS** using simple SQL-style commands.

---

### 🧩 **1. What is Hive Query Language (HQL)?**

* HQL is similar to **SQL (Structured Query Language)** used in RDBMS.
* It provides **abstraction** over **MapReduce**, meaning users write queries in HQL, and Hive automatically converts them into **MapReduce / Tez / Spark jobs** for execution on Hadoop.

---

### ⚙️ **2. Hive Query Execution Flow**

When you execute an HQL query:

1. The query is submitted through the **Hive interface (CLI or JDBC)**.
2. Hive **parses** and **compiles** the query.
3. Hive **translates** the query into **MapReduce jobs** (or Tez/Spark tasks).
4. Results are **retrieved** from **HDFS** and displayed to the user.

---

### 🧱 **3. Types of Hive Queries**

Hive queries can be categorized as:

| **Type**                             | **Purpose**                                  | **Examples**                        |
| ------------------------------------ | -------------------------------------------- | ----------------------------------- |
| **DDL (Data Definition Language)**   | Define or modify schema and table structures | CREATE, ALTER, DROP                 |
| **DML (Data Manipulation Language)** | Manage and modify table data                 | LOAD, INSERT, DELETE                |
| **DQL (Data Query Language)**        | Retrieve and analyze data                    | SELECT, WHERE, GROUP BY             |
| **DCL (Data Control Language)**      | Manage access permissions                    | GRANT, REVOKE (limited use in Hive) |

---

### 🧰 **4. Basic Hive Query Syntax**

```sql
SELECT [ALL | DISTINCT] column1, column2, ...
FROM table_name
WHERE [conditions]
GROUP BY column
HAVING [conditions]
ORDER BY column [ASC|DESC]
LIMIT number;
```

---

### 🧮 **5. Common Hive Queries**

#### 🧱 **a) Create Database**

```sql
CREATE DATABASE company_db;
SHOW DATABASES;
USE company_db;
```

---

#### 📋 **b) Create Table**

```sql
CREATE TABLE employees (
  emp_id INT,
  emp_name STRING,
  dept STRING,
  salary DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

---

#### 📥 **c) Load Data into Table**

```sql
LOAD DATA LOCAL INPATH '/home/hadoop/emp.csv'
INTO TABLE employees;
```

* `LOCAL` → file from local system
* Without `LOCAL` → file from HDFS

---

#### 🔍 **d) Select Query**

```sql
SELECT emp_id, emp_name, dept
FROM employees
WHERE salary > 50000;
```

---

#### 🧠 **e) Grouping & Aggregation**

```sql
SELECT dept, COUNT(*) AS total_employees, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept;
```

---

#### 🎯 **f) Filtering with HAVING**

```sql
SELECT dept, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept
HAVING avg_salary > 60000;
```

---

#### 🔄 **g) Insert Data**

```sql
INSERT INTO TABLE employees
VALUES (106, 'Ravi', 'IT', 55000);
```

Or insert data from another table:

```sql
INSERT OVERWRITE TABLE high_paid
SELECT * FROM employees WHERE salary > 80000;
```

---

#### 🧾 **h) Drop Table**

```sql
DROP TABLE employees;
```

---

#### 🧱 **i) Describe Table**

```sql
DESCRIBE employees;
```

---

#### 🧮 **j) Joins in Hive**

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON (e.dept_id = d.dept_id);
```

Hive supports:

* **INNER JOIN**
* **LEFT OUTER JOIN**
* **RIGHT OUTER JOIN**
* **FULL OUTER JOIN**

---

#### 📊 **k) Sorting and Ordering**

```sql
SELECT emp_name, salary
FROM employees
ORDER BY salary DESC;
```

---

#### ⏳ **l) Limiting Results**

```sql
SELECT * FROM employees LIMIT 5;
```

---

### 🧠 **6. Hive Query Execution Diagram**

```
+------------------------+
|  User (HQL Query)      |
+-----------+------------+
            |
            v
+------------------------+
|  Hive Compiler         |
| (Parse & Optimize)     |
+-----------+------------+
            |
            v
+------------------------+
|  Execution Engine      |
| (MapReduce / Tez Job)  |
+-----------+------------+
            |
            v
+------------------------+
|  HDFS Data Storage     |
| (Input / Output Files) |
+------------------------+
```

---

### 📘 **7. Example: Word Count in Hive**

Suppose you have a text file with words in HDFS.
You can count occurrences of each word using Hive:

```sql
CREATE TABLE words (word STRING);
LOAD DATA INPATH '/user/hive/words.txt' INTO TABLE words;

SELECT word, COUNT(*) AS count
FROM words
GROUP BY word
ORDER BY count DESC;
```

This internally runs a **MapReduce job** for grouping and counting.

---

### ⚡ **8. Advantages of Hive Query Language**

* SQL-like syntax — easy to learn for anyone with SQL knowledge.
* Automatically translates to MapReduce — no need for Java coding.
* Supports **partitioning**, **bucketing**, and **complex types**.
* Integrates with **HDFS**, **HBase**, **ORC**, **Parquet**, etc.
* Scalable for **petabytes of data**.

---

### ✅ **In Summary**

| **Feature**         | **Hive Query Language**                              |
| ------------------- | ---------------------------------------------------- |
| **Language Type**   | SQL-like (Declarative)                               |
| **Execution Model** | Translates into MapReduce/Tez/Spark                  |
| **Primary Goal**    | Data summarization, analysis, and querying           |
| **Strength**        | Handles massive datasets in distributed environments |
| **Limitation**      | Not suitable for real-time queries (batch-oriented)  |

---

### **Hive Language Statements** 🐝

Hive provides a **query language similar to SQL**, called **HiveQL**, which allows users to manage and analyze data stored in Hadoop (HDFS).
These statements are categorized into **five main types**:

---

## 🧱 1. **Data Definition Language (DDL)**

Used to define and manage the **structure** of tables and databases.

| **Command**         | **Purpose**                    | **Example**                                                  |
| ------------------- | ------------------------------ | ------------------------------------------------------------ |
| **CREATE DATABASE** | Creates a new database         | `CREATE DATABASE sales_db;`                                  |
| **DROP DATABASE**   | Deletes a database             | `DROP DATABASE sales_db;`                                    |
| **CREATE TABLE**    | Creates a new table            | `CREATE TABLE customers (id INT, name STRING, city STRING);` |
| **DROP TABLE**      | Deletes an existing table      | `DROP TABLE customers;`                                      |
| **ALTER TABLE**     | Changes the table structure    | `ALTER TABLE customers ADD COLUMNS (age INT);`               |
| **SHOW TABLES**     | Lists all tables in a database | `SHOW TABLES;`                                               |
| **DESCRIBE TABLE**  | Displays table schema          | `DESCRIBE customers;`                                        |

---

## 📦 2. **Data Manipulation Language (DML)**

Used to **load, insert, and query** data within Hive tables.

| **Command**          | **Purpose**                                            | **Example**                                                    |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **LOAD DATA**        | Loads data into a table from HDFS or local file system | `LOAD DATA INPATH '/data/customers.csv' INTO TABLE customers;` |
| **INSERT INTO**      | Inserts data into an existing table                    | `INSERT INTO TABLE sales SELECT * FROM temp_sales;`            |
| **INSERT OVERWRITE** | Replaces existing data in a table                      | `INSERT OVERWRITE TABLE sales SELECT * FROM new_sales;`        |
| **EXPORT / IMPORT**  | Transfers table data between clusters                  | `EXPORT TABLE sales TO '/backup/sales/';`                      |
| **TRUNCATE TABLE**   | Removes all data but keeps structure                   | `TRUNCATE TABLE customers;`                                    |

---

## 🧮 3. **Data Query Language (DQL)**

Used for **querying and analyzing data** using HiveQL (similar to SQL).

| **Command**  | **Purpose**                        | **Example**                                                                |
| ------------ | ---------------------------------- | -------------------------------------------------------------------------- |
| **SELECT**   | Retrieves data from tables         | `SELECT name, city FROM customers WHERE city='Bangalore';`                 |
| **WHERE**    | Filters rows based on conditions   | `SELECT * FROM sales WHERE amount > 1000;`                                 |
| **GROUP BY** | Groups rows for aggregation        | `SELECT city, COUNT(*) FROM customers GROUP BY city;`                      |
| **ORDER BY** | Sorts the result set               | `SELECT * FROM sales ORDER BY amount DESC;`                                |
| **LIMIT**    | Restricts number of rows returned  | `SELECT * FROM sales LIMIT 10;`                                            |
| **JOIN**     | Combines rows from multiple tables | `SELECT a.name, b.amount FROM customers a JOIN sales b ON a.id=b.cust_id;` |

---

## ⚙️ 4. **Data Control Language (DCL)**

Manages **access control and permissions** on databases and tables.

| **Command** | **Purpose**               | **Example**                                       |
| ----------- | ------------------------- | ------------------------------------------------- |
| **GRANT**   | Gives privileges to users | `GRANT SELECT ON TABLE sales TO USER analyst;`    |
| **REVOKE**  | Removes privileges        | `REVOKE SELECT ON TABLE sales FROM USER analyst;` |

> ⚠️ DCL commands may depend on the **Hive security configuration** (e.g., integration with Ranger or Sentry).

---

## 🚀 5. **Utility and Administrative Commands**

Used for **metadata management** and **optimization**.

| **Command**           | **Purpose**                          | **Example**                               |
| --------------------- | ------------------------------------ | ----------------------------------------- |
| **SHOW DATABASES**    | Lists all databases                  | `SHOW DATABASES;`                         |
| **USE**               | Switches between databases           | `USE sales_db;`                           |
| **MSCK REPAIR TABLE** | Repairs partitions                   | `MSCK REPAIR TABLE logs;`                 |
| **ANALYZE TABLE**     | Collects statistics for optimization | `ANALYZE TABLE sales COMPUTE STATISTICS;` |
| **SET**               | Displays or changes configuration    | `SET hive.exec.dynamic.partition=true;`   |

---

### 🧭 Summary

| **Category** | **Purpose**                              |
| ------------ | ---------------------------------------- |
| **DDL**      | Define structure of databases and tables |
| **DML**      | Load and modify data                     |
| **DQL**      | Query and analyze data                   |
| **DCL**      | Manage permissions and access            |
| **Utility**  | Optimize and manage Hive environment     |

---

### **Hive Partitions** 🧩

In Hive, **partitions** are a way to **divide a large dataset into smaller, manageable parts** based on the values of one or more columns.
This helps improve **query performance** and **data organization** when working with **massive datasets** stored in HDFS.

---

## 🧠 **Concept Overview**

When you create a Hive table, you can **partition it** using one or more columns.
Each partition corresponds to a **subdirectory** in HDFS, containing only the data relevant to that partition key.

Example:
If you partition a table by **year** and **month**, Hive creates directories like:

```
/data/sales/year=2024/month=01/
/data/sales/year=2024/month=02/
/data/sales/year=2025/month=01/
```

Each directory stores only the rows belonging to that year and month.

---

## ⚙️ **Types of Partitioning**

### 1. **Static Partitioning**

* You **manually specify** the partition column value when loading data.
* Common when you already know where each record belongs.

**Example:**

```sql
CREATE TABLE sales (
  id INT,
  amount FLOAT
)
PARTITIONED BY (year INT, month INT)
STORED AS TEXTFILE;

LOAD DATA INPATH '/data/jan_sales.csv'
INTO TABLE sales
PARTITION (year=2024, month=1);
```

👉 The data is stored in HDFS path:
`/user/hive/warehouse/sales/year=2024/month=1/`

---

### 2. **Dynamic Partitioning**

* Hive **automatically determines** the partition based on column values in the dataset.
* Very useful when inserting large datasets with multiple partition keys.

**Example:**

```sql
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;

INSERT INTO TABLE sales
PARTITION (year, month)
SELECT id, amount, year, month FROM temp_sales;
```

👉 Hive automatically creates directories like:
`year=2024/month=1/`, `year=2024/month=2/`, etc.

---

## 🚀 **Advantages of Partitioning**

| **Advantage**                    | **Explanation**                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| **Improved Query Performance**   | Queries can skip irrelevant partitions (called *partition pruning*).                       |
| **Efficient Storage Management** | Data is neatly organized in HDFS by partition keys.                                        |
| **Faster Data Loading**          | Data for specific partitions can be added or replaced without touching the entire dataset. |
| **Ease of Maintenance**          | Old partitions can be archived or dropped easily.                                          |

---

## ⚠️ **Limitations of Partitioning**

| **Limitation**                               | **Description**                                                                                      |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Too Many Partitions**                      | Creating too many small partitions (e.g., one per user) can slow Hive due to high metadata overhead. |
| **Static Partitioning Manual Effort**        | Requires manually defining partition values each time.                                               |
| **Inefficient for High Cardinality Columns** | Not ideal for columns with too many unique values (like user IDs).                                   |

---

## 🧩 **Partition Pruning (Query Optimization)**

Hive uses **partition pruning** to read only relevant data.
Example:

```sql
SELECT * FROM sales WHERE year=2024 AND month=1;
```

Hive will only scan data under:

```
/sales/year=2024/month=1/
```

Instead of the entire table — making it **much faster**.

---

## 🔍 **Viewing and Managing Partitions**

| **Command**                    | **Purpose**                                | **Example**                                               |
| ------------------------------ | ------------------------------------------ | --------------------------------------------------------- |
| **SHOW PARTITIONS**            | Lists all partitions of a table            | `SHOW PARTITIONS sales;`                                  |
| **ALTER TABLE ADD PARTITION**  | Adds a new partition manually              | `ALTER TABLE sales ADD PARTITION (year=2025, month=2);`   |
| **ALTER TABLE DROP PARTITION** | Removes a partition                        | `ALTER TABLE sales DROP PARTITION (year=2023, month=12);` |
| **MSCK REPAIR TABLE**          | Recovers partitions added directly in HDFS | `MSCK REPAIR TABLE sales;`                                |

---

### 🧭 **Summary**

| **Feature**      | **Static Partitioning**          | **Dynamic Partitioning**                  |
| ---------------- | -------------------------------- | ----------------------------------------- |
| **Data Loading** | Manual                           | Automatic                                 |
| **Control**      | Full user control                | Determined by data values                 |
| **Use Case**     | Small number of known partitions | Large datasets with many partition values |
| **Performance**  | High (for limited partitions)    | High (with proper pruning)                |

---

### 🪣 **Hive Bucketing**

**Bucketing** in Hive is a technique used to **divide large datasets into smaller, more manageable parts (buckets)** based on the **hash of a column’s value**.
It is similar to partitioning, but **more fine-grained** — it helps in **efficient query execution, joins, and sampling**.

---

## 🧠 **Concept Overview**

When you create a bucketed table, Hive uses the **hash function** on the column you specify and assigns each row to a **bucket (file)** based on that hash result.

Example:
If you bucket by `customer_id` into 4 buckets, Hive distributes rows as:

```
Bucket 1 → hash(customer_id) % 4 == 0  
Bucket 2 → hash(customer_id) % 4 == 1  
Bucket 3 → hash(customer_id) % 4 == 2  
Bucket 4 → hash(customer_id) % 4 == 3  
```

This ensures **even data distribution** and **faster joins** when both tables are bucketed on the same key.

---

## ⚙️ **Syntax: Creating a Bucketed Table**

```sql
CREATE TABLE customer_buckets (
  customer_id INT,
  name STRING,
  age INT,
  city STRING
)
CLUSTERED BY (customer_id)
INTO 4 BUCKETS
STORED AS ORC;
```

✅ `CLUSTERED BY` specifies the **column used for bucketing**.
✅ `INTO 4 BUCKETS` means Hive will create **4 output files (buckets)**.
✅ You can also **combine partitions + buckets** for hybrid performance.

---

## ⚙️ **Loading Data into a Bucketed Table**

Before loading data into a bucketed table, enable bucketing properties:

```sql
SET hive.enforce.bucketing = true;

INSERT OVERWRITE TABLE customer_buckets
SELECT * FROM customers;
```

Hive ensures that data is divided correctly among the specified buckets.

---

## 📊 **Difference Between Partitioning and Bucketing**

| **Aspect**            | **Partitioning**                                  | **Bucketing**                                     |
| --------------------- | ------------------------------------------------- | ------------------------------------------------- |
| **Basis**             | Divides data based on column values (directories) | Divides data based on hash of column (files)      |
| **Storage Structure** | Each partition → separate HDFS directory          | Each bucket → separate file within a partition    |
| **Granularity**       | Coarse                                            | Fine                                              |
| **Metadata Overhead** | High (if many partitions)                         | Low                                               |
| **Use Case**          | For high-level filtering (e.g., by date, region)  | For joins, sampling, and hashing-based operations |

---

## 🧩 **Combining Partitioning + Bucketing**

You can **partition first**, then **bucket** within each partition.

```sql
CREATE TABLE sales (
  id INT,
  amount FLOAT,
  region STRING
)
PARTITIONED BY (year INT)
CLUSTERED BY (region)
INTO 4 BUCKETS
STORED AS ORC;
```

Here:

* Data is divided by **year** (partition).
* Within each year, data is further divided into **4 buckets** based on region hash.

---

## ⚙️ **Advantages of Bucketing**

| **Advantage**               | **Explanation**                                                                  |
| --------------------------- | -------------------------------------------------------------------------------- |
| **Efficient Joins**         | Hive can perform *bucket map joins* when tables are bucketed on the same column. |
| **Sampling**                | You can easily select a sample of buckets for analysis.                          |
| **Reduced Data Skew**       | Hash-based distribution ensures even data spread across files.                   |
| **Faster Query Processing** | Optimized data read due to smaller files.                                        |

---

## 🧠 **Example: Bucket Sampling**

Suppose you bucketed the table into 8 buckets.
You can select a sample bucket like this:

```sql
SELECT * FROM customer_buckets TABLESAMPLE(BUCKET 3 OUT OF 8 ON customer_id);
```

👉 This reads only **bucket 3** instead of all 8 — useful for **quick analysis**.

---

## 🏗️ **Hive Bucketing Process Diagram**

```
           +------------------------+
           |     Input Dataset      |
           +------------------------+
                        |
                        v
           +------------------------+
           |  Hash(customer_id) % 4 |
           +------------------------+
              |      |      |      |
              v      v      v      v
        Bucket1  Bucket2  Bucket3  Bucket4
```

Each bucket corresponds to a **file** in HDFS.

For example:

```
/warehouse/customer_buckets/000000_0
/warehouse/customer_buckets/000001_0
/warehouse/customer_buckets/000002_0
/warehouse/customer_buckets/000003_0
```

---

## ⚠️ **Things to Remember**

1. **Bucket number** must be defined while creating the table.
2. To enforce bucketing during data load:

   ```sql
   SET hive.enforce.bucketing = true;
   ```
3. **Bucketing is static** — you can’t change the number of buckets after creation.
4. Use **ORC** or **Parquet** format for efficient storage and read performance.

---

### ✅ **Summary**

| **Feature**       | **Explanation**                                     |
| ----------------- | --------------------------------------------------- |
| **Purpose**       | Divide data into smaller, hash-based files          |
| **Key Clause**    | `CLUSTERED BY (col) INTO n BUCKETS`                 |
| **Best Use Case** | Optimized joins and sampling                        |
| **Storage**       | Each bucket → separate file                         |
| **Combination**   | Often used with partitioning for hybrid performance |

---

### 🧩 **Hive Views**

In **Apache Hive**, a **View** is a **virtual table** created using the result of a **SELECT query**.
It does **not store data physically**, but acts as a **logical layer** built on top of existing tables.

This concept is similar to **SQL Views** in traditional RDBMS — providing data abstraction, simplified queries, and better security.

---

## 🧠 **Concept Overview**

A **View** behaves like a table in Hive — you can:

* Query it using `SELECT` statements,
* Join it with other tables,
* Filter or aggregate data through it.

However, the **data is not stored separately**; it’s fetched dynamically from the **underlying base tables** whenever the view is queried.

---

## ⚙️ **Syntax of Creating a View**

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM base_table
WHERE condition;
```

✅ The query defines what the view will show.
✅ Hive stores the **query definition**, not the data.

---

## 🧩 **Example: Simple View**

Let’s say you have a sales table:

```sql
CREATE TABLE sales (
  id INT,
  product STRING,
  price FLOAT,
  region STRING,
  year INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

You can create a view to display only sales from 2024:

```sql
CREATE VIEW sales_2024 AS
SELECT id, product, price, region
FROM sales
WHERE year = 2024;
```

Now, you can query this view like a regular table:

```sql
SELECT * FROM sales_2024 WHERE region = 'South';
```

👉 Hive internally runs:

```sql
SELECT id, product, price, region
FROM sales
WHERE year = 2024 AND region = 'South';
```

---

## ⚙️ **Types of Views in Hive**

| **Type**              | **Description**                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| **Standard View**     | A normal view defined by a `SELECT` query.                                                         |
| **Materialized View** | A view that **physically stores** the result set for faster performance (introduced in Hive 2.3+). |

---

### 🧱 **1. Standard View Example**

```sql
CREATE VIEW product_summary AS
SELECT product, SUM(price) AS total_sales
FROM sales
GROUP BY product;
```

This view dynamically calculates `total_sales` whenever queried.

---

### ⚡ **2. Materialized View Example**

Materialized views **store precomputed results** (useful for large datasets).

```sql
CREATE MATERIALIZED VIEW mv_sales_summary
AS
SELECT region, SUM(price) AS total_sales
FROM sales
GROUP BY region;
```

Hive stores the summarized data.
You can **refresh** it when base data changes:

```sql
ALTER MATERIALIZED VIEW mv_sales_summary REBUILD;
```

---

## 🧠 **Advantages of Using Views**

| **Advantage**           | **Explanation**                                                         |
| ----------------------- | ----------------------------------------------------------------------- |
| **Data Abstraction**    | Hides the complexity of SQL joins or filters from users.                |
| **Security**            | Restricts access to specific columns or rows.                           |
| **Reusability**         | Reuse common queries multiple times without rewriting.                  |
| **Simplified Analysis** | Analysts can work with views instead of full raw datasets.              |
| **Maintenance**         | Changing a view definition automatically updates all dependent queries. |

---

## ⚠️ **Limitations**

| **Limitation**              | **Description**                                                       |
| --------------------------- | --------------------------------------------------------------------- |
| **Performance**             | Regular views are not stored — each query re-runs the underlying SQL. |
| **No Indexing**             | Views cannot have indexes.                                            |
| **Cannot Load Data**        | You cannot use `LOAD DATA` into a view (since it stores no data).     |
| **Dependent on Base Table** | Dropping or altering the base table may break the view.               |

---

## 🧮 **Diagram: Hive View Concept**

```
          +---------------------+
          |     sales table     |
          +---------------------+
                    |
                    |  (SELECT id, product, price, region WHERE year=2024)
                    v
          +---------------------+
          |    sales_2024 view  |
          +---------------------+
                    |
                    |  SELECT * FROM sales_2024 WHERE region='South';
                    v
          +---------------------+
          |   Query Result Set  |
          +---------------------+
```

---

## 🧾 **View Management Commands**

| **Command**                            | **Usage**                                |
| -------------------------------------- | ---------------------------------------- |
| `SHOW VIEWS;`                          | Lists all views in the current database. |
| `SHOW CREATE TABLE view_name;`         | Displays the SQL definition of a view.   |
| `DROP VIEW view_name;`                 | Deletes a view.                          |
| `ALTER VIEW view_name AS <new_query>;` | Redefines an existing view.              |

---

## 🧭 **Real-World Example**

**Scenario:**
A retail company stores millions of records in the `sales` table.
Analysts only need the last year’s data for dashboards.

**Solution:**
Create a view for the recent year:

```sql
CREATE VIEW last_year_sales AS
SELECT *
FROM sales
WHERE year = 2024;
```

Now analysts simply query:

```sql
SELECT region, SUM(price)
FROM last_year_sales
GROUP BY region;
```

instead of writing filters every time.
👉 Cleaner, faster, and easier maintenance.

---

## ✅ **Summary Table**

| **Feature**       | **Description**                                                                    |
| ----------------- | ---------------------------------------------------------------------------------- |
| **Definition**    | Logical table based on a query                                                     |
| **Storage**       | No physical data stored (except materialized views)                                |
| **Use Case**      | Simplify complex queries and control access                                        |
| **Performance**   | On-demand computation (slower for complex queries)                                 |
| **Best Practice** | Use for abstraction and access control; use materialized view for frequent queries |

---

### 🧠 **Hive Sub-Query**

A **Subquery** in Hive is a **query nested inside another query**.
It helps break complex operations into smaller steps — making queries **easier to write**, **read**, and **optimize**.

Subqueries can appear in the `SELECT`, `FROM`, or `WHERE` clause of a HiveQL statement.

---

## ⚙️ **Basic Syntax**

```sql
SELECT column_list
FROM table_name
WHERE column_name IN (SELECT column_name FROM other_table WHERE condition);
```

👉 The inner query (inside parentheses) runs first.
👉 The outer query then uses the result of the inner query.

---

## 🧩 **Types of Subqueries in Hive**

| **Type**                         | **Description**                                                  |
| -------------------------------- | ---------------------------------------------------------------- |
| **Scalar Subquery**              | Returns a single value (one row, one column).                    |
| **IN / NOT IN Subquery**         | Used in `WHERE` clause to filter results based on another query. |
| **EXISTS / NOT EXISTS Subquery** | Checks for existence of rows satisfying a condition.             |
| **FROM Clause Subquery**         | The subquery acts like a temporary table (inline view).          |

---

## 🧱 **1️⃣ Scalar Subquery Example**

A scalar subquery returns exactly one value.

```sql
SELECT *
FROM sales
WHERE price > (SELECT AVG(price) FROM sales);
```

🧮 **Explanation:**

* Inner query → Calculates the average price from all sales.
* Outer query → Returns all rows where `price` is greater than the average.

---

## 🧱 **2️⃣ IN / NOT IN Subquery Example**

Used to filter rows based on another table’s data.

```sql
SELECT customer_id, product
FROM sales
WHERE customer_id IN (
  SELECT customer_id
  FROM customer
  WHERE region = 'South'
);
```

🧮 **Explanation:**

* Inner query gets IDs of all customers from the “South” region.
* Outer query returns sales data for those customers only.

---

## 🧱 **3️⃣ EXISTS Subquery Example**

Used to check **if at least one row exists** in the subquery result.

```sql
SELECT customer_id, name
FROM customer c
WHERE EXISTS (
  SELECT 1
  FROM sales s
  WHERE s.customer_id = c.customer_id
);
```

🧮 **Explanation:**

* Hive checks if a customer has made at least one sale.
* Returns only those customers that exist in both tables.

---

## 🧱 **4️⃣ Subquery in FROM Clause (Inline View)**

You can use a subquery as a **temporary table** inside the `FROM` clause.

```sql
SELECT region, SUM(total_sales) AS total
FROM (
  SELECT region, price AS total_sales
  FROM sales
  WHERE year = 2024
) temp
GROUP BY region;
```

🧮 **Explanation:**

* Inner query (alias `temp`) filters data for 2024.
* Outer query aggregates it by region.
* This is very useful for **stepwise aggregation or filtering**.

---

## ⚙️ **Example: Multiple Nested Subqueries**

```sql
SELECT *
FROM (
  SELECT region, SUM(price) AS total_sales
  FROM sales
  GROUP BY region
) AS region_sales
WHERE total_sales > (
  SELECT AVG(total_sales)
  FROM (
    SELECT region, SUM(price) AS total_sales
    FROM sales
    GROUP BY region
  ) AS sub_avg
);
```

🧮 **Explanation:**

1. Inner subquery → calculates sales per region.
2. Second subquery → computes the average of total regional sales.
3. Outer query → filters only regions with above-average sales.

---

## 📊 **Diagram: How Hive Executes a Subquery**

```
+--------------------------------------+
| Outer Query                          |
| SELECT region, total_sales           |
| FROM (Inner Query) AS temp           |
| WHERE total_sales > 10000;           |
+--------------------------------------+
                ↑
                |
+--------------------------------------+
| Inner Query                          |
| SELECT region, SUM(price) AS total   |
| FROM sales GROUP BY region;          |
+--------------------------------------+
```

✅ Hive first executes the **inner query**,
✅ Stores the result in memory or a temporary table,
✅ Then the **outer query** runs on that result.

---

## ⚡ **Performance Tips**

| **Tip**                                    | **Reason**                                                 |
| ------------------------------------------ | ---------------------------------------------------------- |
| Avoid too many nested subqueries           | Each level creates a temporary dataset, slowing execution. |
| Use `WITH` clause (CTE) for readability    | Easier to manage complex multi-level queries.              |
| Combine subqueries with partitions/buckets | Improves read speed in large datasets.                     |
| Use appropriate file formats (ORC/Parquet) | Speeds up filtering and projection in subqueries.          |

---

## 🧠 **Common Use Cases**

| **Use Case**                    | **Description**                                                 |
| ------------------------------- | --------------------------------------------------------------- |
| **Filtering Data**              | Using subquery in `WHERE` to limit results based on conditions. |
| **Aggregations**                | Using subquery in `FROM` to perform intermediate aggregations.  |
| **Correlated Subqueries**       | When inner query depends on the outer query column.             |
| **Simplifying Complex Queries** | Breaking long joins and filters into readable layers.           |

---

## 🧮 **Correlated Subquery Example**

A **correlated subquery** refers to columns from the outer query inside the inner query.

```sql
SELECT c.name, c.region
FROM customer c
WHERE c.age > (
  SELECT AVG(age)
  FROM customer
  WHERE region = c.region
);
```

🧩 **Explanation:**

* For each region, Hive calculates the average age.
* Then it returns customers older than that regional average.

---

## ✅ **Summary Table**

| **Feature**            | **Description**                                       |
| ---------------------- | ----------------------------------------------------- |
| **Definition**         | Query inside another query                            |
| **Executed First**     | Inner (subquery)                                      |
| **Stored Physically?** | No — runs dynamically                                 |
| **Use Case**           | Filtering, aggregation, comparison                    |
| **Example Clauses**    | `WHERE`, `FROM`, `EXISTS`, `IN`                       |
| **Performance**        | Slower than joins on very large data if nested deeply |

---

### **Joins in Hive**

Joins in Hive are used to **combine rows from two or more tables** based on a related column between them — typically a **key field**. Hive supports several types of joins similar to SQL, but because Hive operates on large distributed datasets, its joins are implemented using **MapReduce or Tez** under the hood.

---

### **1. Types of Joins in Hive**

#### **a. INNER JOIN**

* Returns only those rows where there is a **match in both tables**.
* Equivalent to SQL’s inner join.
* **Syntax:**

  ```sql
  SELECT a.id, a.name, b.salary
  FROM employee a
  INNER JOIN salary b
  ON (a.id = b.emp_id);
  ```
* **Output:** Rows where `a.id = b.emp_id`.

---

#### **b. LEFT OUTER JOIN**

* Returns all rows from the **left table**, and the **matched rows** from the right table.
* If no match is found, **NULLs** are returned for right table columns.
* **Syntax:**

  ```sql
  SELECT a.id, a.name, b.salary
  FROM employee a
  LEFT OUTER JOIN salary b
  ON (a.id = b.emp_id);
  ```
* **Output:** All employees (even if they don’t have salary info).

---

#### **c. RIGHT OUTER JOIN**

* Returns all rows from the **right table**, and the **matched rows** from the left table.
* **Syntax:**

  ```sql
  SELECT a.id, a.name, b.salary
  FROM employee a
  RIGHT OUTER JOIN salary b
  ON (a.id = b.emp_id);
  ```
* **Output:** All salaries (even if there’s no matching employee).

---

#### **d. FULL OUTER JOIN**

* Returns all rows from **both tables**.
* Rows with no match in either table will contain **NULLs** for missing fields.
* **Syntax:**

  ```sql
  SELECT a.id, a.name, b.salary
  FROM employee a
  FULL OUTER JOIN salary b
  ON (a.id = b.emp_id);
  ```

---

#### **e. CROSS JOIN (Cartesian Join)**

* Returns the **Cartesian product** of both tables — every row of one table is joined with every row of the other.
* **Syntax:**

  ```sql
  SELECT a.id, b.dept
  FROM employee a
  CROSS JOIN department b;
  ```
* **Output:** If `employee` has 5 rows and `department` has 3, result = 15 rows.

---

### **2. Join Conditions**

Joins can use **equality conditions**:

```sql
ON (table1.col1 = table2.col2)
```

or more complex conditions (less common):

```sql
ON (table1.col1 > table2.col2)
```

---

### **3. Join Optimization in Hive**

Hive uses several techniques to optimize joins:

* **Map-side Join:** Loads small tables into memory and joins them with larger ones on the map side.

  ```sql
  SELECT /*+ MAPJOIN(small_table) */ a.id, b.value
  FROM large_table a
  JOIN small_table b
  ON (a.key = b.key);
  ```
* **Bucketed Map Join:** Uses table bucketing to perform faster joins.
* **Sort-Merge Join:** Used when both tables are sorted and bucketed on the join keys.

---

### **4. Performance Considerations**

* The **smaller table** should be on the **right side** of the join.
* For multiple joins, Hive executes them **left to right**.
* Use **map joins** for small lookup tables to avoid full shuffles.
* Hive 3.x supports **dynamic partition pruning** for efficient joins on partitioned tables.

---

### **5. Example:**

```sql
CREATE TABLE emp (id INT, name STRING, dept_id INT);
CREATE TABLE dept (dept_id INT, dept_name STRING);

SELECT e.name, d.dept_name
FROM emp e
JOIN dept d
ON (e.dept_id = d.dept_id);
```

**Result:** Combines employee names with their department names.

---

### **Aggregations in Hive**

Aggregation in Hive refers to the process of **computing summary statistics** from data, such as sums, averages, counts, and maximum/minimum values.
It is similar to SQL aggregation but optimized for distributed processing in the Hadoop ecosystem.

---

## 🧩 **1. What Are Aggregations?**

Aggregation combines multiple rows of data into a single result based on a **grouping condition** or across the entire dataset.

For example:

```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept;
```

This query finds the **average salary** for each department.

---

## ⚙️ **2. Common Aggregate Functions**

| Function           | Description                                            | Example              |
| ------------------ | ------------------------------------------------------ | -------------------- |
| **COUNT()**        | Returns the number of rows.                            | `COUNT(*)`           |
| **SUM()**          | Returns the sum of values.                             | `SUM(salary)`        |
| **AVG()**          | Returns the average of values.                         | `AVG(age)`           |
| **MIN()**          | Returns the minimum value.                             | `MIN(salary)`        |
| **MAX()**          | Returns the maximum value.                             | `MAX(salary)`        |
| **COLLECT_SET()**  | Returns unique values as an array.                     | `COLLECT_SET(dept)`  |
| **COLLECT_LIST()** | Returns all values (including duplicates) as an array. | `COLLECT_LIST(name)` |

---

## 🧮 **3. GROUP BY Clause**

The `GROUP BY` clause groups rows that have the same values in specified columns and then applies aggregate functions.

**Example:**

```sql
SELECT dept, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept;
```

**Result:**
Each department’s employee count and average salary.

---

## 🧱 **4. HAVING Clause**

The `HAVING` clause filters results **after aggregation** (unlike `WHERE`, which filters before aggregation).

**Example:**

```sql
SELECT dept, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept
HAVING AVG(salary) > 50000;
```

**Explanation:**
Shows only departments with an average salary greater than ₹50,000.

---

## 📊 **5. Aggregation Without GROUP BY**

When `GROUP BY` is omitted, Hive aggregates across the **entire table**.

**Example:**

```sql
SELECT COUNT(*) AS total_employees, AVG(salary) AS avg_salary
FROM employees;
```

**Result:**
Single row summary of the table.

---

## ⚡ **6. Multiple Aggregate Functions**

You can use multiple aggregate functions in the same query:

```sql
SELECT dept, 
       COUNT(*) AS emp_count,
       SUM(salary) AS total_salary,
       MAX(salary) AS highest_salary
FROM employees
GROUP BY dept;
```

---

## 🧠 **7. DISTINCT in Aggregations**

`DISTINCT` removes duplicates before aggregation.

**Example:**

```sql
SELECT COUNT(DISTINCT dept) AS unique_departments
FROM employees;
```

---

## 🏗️ **8. Aggregate Functions with Joins**

Aggregates can be applied on joined tables:

```sql
SELECT d.dept_name, AVG(e.salary)
FROM employees e
JOIN department d
ON (e.dept_id = d.dept_id)
GROUP BY d.dept_name;
```

---

## 🚀 **9. Advanced Aggregation Features in Hive**

* **ROLLUP:** Generates subtotals and grand totals.

  ```sql
  SELECT dept, designation, SUM(salary)
  FROM employees
  GROUP BY dept, designation WITH ROLLUP;
  ```

* **CUBE:** Generates all possible combinations of groupings.

  ```sql
  SELECT dept, designation, SUM(salary)
  FROM employees
  GROUP BY dept, designation WITH CUBE;
  ```

---

## 🧰 **10. Optimization Tips**

* Use **`GROUP BY` on partitioned columns** for faster performance.
* Combine small aggregations using **MapReduce combiner phase**.
* Use **`LIMIT`** when exploring large aggregated datasets.
* Prefer **`COUNT(1)`** instead of `COUNT(*)` for better optimization.

---

### ✅ **Summary**

| Concept           | Purpose                                     | Example                     |
| ----------------- | ------------------------------------------- | --------------------------- |
| **Aggregation**   | Summarize data                              | `AVG(salary)`               |
| **GROUP BY**      | Group data by key                           | `GROUP BY dept`             |
| **HAVING**        | Filter aggregated results                   | `HAVING SUM(sales) > 1000`  |
| **DISTINCT**      | Remove duplicates                           | `COUNT(DISTINCT city)`      |
| **ROLLUP / CUBE** | Hierarchical & multidimensional aggregation | `WITH ROLLUP` / `WITH CUBE` |

---

### **GROUP BY and HAVING in Hive**

The `GROUP BY` and `HAVING` clauses in Hive are essential for **aggregating data** and **filtering aggregated results**.
They are similar to SQL but optimized for **large-scale distributed data** processing in Hadoop.

---

## 🧩 **1. GROUP BY Clause**

The `GROUP BY` clause is used to **group rows** that have the same values in one or more columns.
It helps you perform **aggregate operations** (like `SUM`, `AVG`, `COUNT`, etc.) on each group.

---

### 🧠 **Syntax**

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name;
```

---

### 🧮 **Example**

Consider a table `employees`:

| emp_id | emp_name | dept    | salary |
| :----: | :------- | :------ | -----: |
|    1   | Alice    | IT      |  70000 |
|    2   | Bob      | HR      |  50000 |
|    3   | Carol    | IT      |  80000 |
|    4   | Dave     | HR      |  55000 |
|    5   | Eve      | Finance |  60000 |

---

### 🧾 **Query**

```sql
SELECT dept, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept;
```

---

### 📊 **Output**

| dept    | emp_count | avg_salary |
| :------ | --------: | ---------: |
| IT      |         2 |      75000 |
| HR      |         2 |      52500 |
| Finance |         1 |      60000 |

---

### 🧠 **Explanation**

* Hive first **groups** rows by department (`dept`).
* Then applies aggregate functions like:

  * `COUNT(*)` → Number of employees in each department.
  * `AVG(salary)` → Average salary per department.

---

## 🔍 **2. Multiple Columns in GROUP BY**

You can group by **multiple columns**.

```sql
SELECT dept, job_role, AVG(salary)
FROM employees
GROUP BY dept, job_role;
```

This groups data first by department, then by job role.

---

## ⚙️ **3. HAVING Clause**

The `HAVING` clause filters results **after aggregation**.
Unlike `WHERE`, which filters rows **before** aggregation, `HAVING` filters **after** the `GROUP BY` has been applied.

---

### 🧠 **Syntax**

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
HAVING condition;
```

---

### 🧾 **Example**

```sql
SELECT dept, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept
HAVING AVG(salary) > 60000;
```

---

### 📊 **Output**

| dept | avg_salary |
| :--- | ---------: |
| IT   |      75000 |

---

### 🧠 **Explanation**

* First, Hive groups rows by department.
* Then calculates the average salary for each group.
* Finally, it **filters** groups whose average salary is **greater than ₹60,000**.

---

## ⚖️ **4. WHERE vs HAVING**

| Feature                 | WHERE                            | HAVING                               |
| ----------------------- | -------------------------------- | ------------------------------------ |
| **Purpose**             | Filters **rows** before grouping | Filters **groups** after aggregation |
| **Used With**           | All SQL statements               | Only with GROUP BY                   |
| **Aggregate Functions** | ❌ Not allowed                    | ✅ Allowed                            |
| **Example**             | `WHERE salary > 50000`           | `HAVING AVG(salary) > 50000`         |

---

### 🧩 **Example Combining WHERE, GROUP BY, and HAVING**

```sql
SELECT dept, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
WHERE salary > 50000
GROUP BY dept
HAVING COUNT(*) >= 2;
```

**Explanation:**

* `WHERE salary > 50000`: Filters out low-salary employees first.
* `GROUP BY dept`: Groups the remaining rows by department.
* `HAVING COUNT(*) >= 2`: Keeps only departments with at least 2 employees.

---

## 📘 **5. Practical Example with Sales Data**

**Table:** `sales`

| region | product | revenue |
| :----- | :------ | ------: |
| North  | A       |    2000 |
| South  | A       |    1500 |
| North  | B       |    3000 |
| East   | A       |    1200 |
| West   | B       |    1800 |
| South  | B       |    2200 |

---

**Query:**

```sql
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
HAVING SUM(revenue) > 2500;
```

**Output:**

| region | total_revenue |
| :----- | ------------: |
| North  |          5000 |
| South  |          3700 |

---

## 🧱 **6. Diagram — GROUP BY and HAVING Workflow**

```
Raw Data → (WHERE) → Group Rows (GROUP BY) → Apply Aggregate Functions → (HAVING) → Final Output
```

```
Example:
   [employees table]
        ↓
   WHERE salary > 50000
        ↓
   GROUP BY dept
        ↓
   HAVING COUNT(*) >= 2
        ↓
   Result: Filtered summarized output
```

---

## ✅ **Summary**

| Clause       | Role                            | Stage              | Example                      |
| ------------ | ------------------------------- | ------------------ | ---------------------------- |
| **GROUP BY** | Groups rows for aggregation     | During aggregation | `GROUP BY dept`              |
| **HAVING**   | Filters aggregated results      | After aggregation  | `HAVING AVG(salary) > 50000` |
| **WHERE**    | Filters rows before aggregation | Before aggregation | `WHERE salary > 50000`       |

---


# 🧱 What is RCFile?

**RCFile (Record Columnar File)** is an early columnar storage format for Hive.
It stores table data in **row groups** on disk, but **within each row group it stores data column-wise** — giving many of the benefits of columnar storage (better I/O when you read a few columns) while staying compatible with Hive’s MapReduce execution.

RCFile was widely used **before ORC/Parquet** became common. It’s still supported but usually **outperformed** by ORC/Parquet today.

---

## 🏗️ RCFile physical layout (conceptual)

```
RCFile (file)
 ├─ Header / Magic bytes
 ├─ RowGroup 1
 │   ├─ Column-1 block (len, data, maybe compressed)
 │   ├─ Column-2 block
 │   ├─ Column-3 block
 │   └─ RowGroup footer (sync marker, metadata)
 ├─ RowGroup 2
 │   └─ ...
 └─ Footer / Sync
```

* A **row group** contains a fixed number of rows (a block).
* Within each row group the bytes for each *column* are stored together (columnar inside block).
* Column blocks can be **compressed** independently (block-level compression).
* RCFile uses a **columnar SerDe** to serialize/deserialize.

---

## ✅ Advantages

* **Better I/O than TEXT/SEQFILE** when queries read a subset of columns.
* **Block-level compression** reduces storage and network I/O.
* Works well with older Hive versions and MapReduce-based stacks.
* Simpler than building a full columnar engine (was a first step toward ORC/Parquet).

## ❌ Limitations

* **No rich metadata / indexing** like ORC (no min/max stats, no lightweight indexing, weaker predicate pushdown).
* **Less efficient** than ORC/Parquet for analytics (compression ratio, vectorized reads, predicate pushdown).
* Column blocks are per row-group — still not as optimal for complex nested types.
* Fewer ecosystem optimizations (Spark/Impala prefer Parquet).

---

## ⚙️ How Hive reads/writes RCFile

* **SerDe** used: `org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe`
* **InputFormat / OutputFormat**: Hive uses `RCFileInputFormat` and `RCFileOutputFormat` under the hood when you `STORED AS RCFILE`.
* Hive automatically handles serialization/deserialization; users work with HiveQL.

---

##  ✍️ Create / Use RCFile — practical examples

### 1) Create an RCFile table

```sql
CREATE TABLE sales_rc (
  id INT,
  product STRING,
  qty INT,
  price DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe'
STORED AS RCFILE;
```

> The `ROW FORMAT SERDE ...` line is optional in many Hive installs; `STORED AS RCFILE` sets the input/output formats.

### 2) Load data (from local or HDFS)

```sql
-- from local
LOAD DATA LOCAL INPATH '/home/hadoop/sales.csv' INTO TABLE sales_rc;

-- or from HDFS path (already uploaded)
LOAD DATA INPATH '/user/hadoop/raw/sales.csv' INTO TABLE sales_rc;
```

> Typical pattern: load into a staging text table, then `INSERT OVERWRITE` into RC table to pack into RCFile format.

### 3) Convert an existing table into RCFile

```sql
CREATE TABLE sales_txt (
  id INT, product STRING, qty INT, price DOUBLE
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- load raw csv to sales_txt then:
INSERT OVERWRITE TABLE sales_rc
SELECT * FROM sales_txt;
```

### 4) Querying (normal HiveQL)

```sql
SELECT product, SUM(qty) AS units
FROM sales_rc
WHERE price > 100
GROUP BY product;
```

---

## 🔧 Enabling compression for RCFile

You typically enable compression in Hive/YARN settings before writing:

```sql
SET hive.exec.compress.output=true;
SET mapreduce.output.fileoutputformat.compress=true;
SET mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.SnappyCodec;
-- or Gzip: org.apache.hadoop.io.compress.GzipCodec
```

When you `INSERT OVERWRITE` into an RCFile table after these settings, the column blocks will be compressed using the codec.

---

## 🧪 Example: Full flow (create, insert, query)

```sql
-- 1) create RC table
CREATE TABLE user_events_rc (
  user_id INT,
  event_type STRING,
  event_time TIMESTAMP,
  metadata STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe'
STORED AS RCFILE;

-- 2) create staging text table and load CSV
CREATE TABLE user_events_txt (
  user_id INT,
  event_type STRING,
  event_time STRING,
  metadata STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/hadoop/user_events.csv' INTO TABLE user_events_txt;

-- 3) convert (this will pack into columnar RC layout)
SET hive.exec.compress.output=true;
SET mapreduce.output.fileoutputformat.compress=true;
SET mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.SnappyCodec;

INSERT OVERWRITE TABLE user_events_rc SELECT user_id, event_type, CAST(event_time AS TIMESTAMP), metadata FROM user_events_txt;

-- 4) query
SELECT event_type, COUNT(*) FROM user_events_rc GROUP BY event_type;
```

---

## 🔎 Performance & tuning tips

* **Use RCFile when** you need columnar benefits but run on older stacks where ORC/Parquet aren’t available. For new projects prefer **ORC or Parquet**.
* **Choose a reasonable row-group size**: too small → many small blocks; too large → less columnar benefit. RCFile internal block sizing is controlled by the underlying filesystem block and Hive settings.
* **Enable compression** (Snappy for speed, Gzip for ratio) — compression reduces network I/O during shuffle.
* **Combine with partitioning**: Use partitioning (e.g., by date) to avoid scanning irrelevant rowgroups.
* **Use bucketing** if you need faster joins (bucketed tables can be written as RCFile too).

---

## 🔁 RCFile vs ORC / Parquet (short)

* **ORC / Parquet**: newer, columnar, have statistics, indexes, predicate pushdown, vectorized readers → **better** for analytics.
* **RCFile**: earlier columnar approach, block-level compression, simpler — still okay but usually **suboptimal** compared to ORC/Parquet.

---

## 🧾 When to use RCFile

* You are on an **older Hive/MapReduce stack** where ORC/Parquet are not available or fully supported.
* You want a **quick columnar improvement** over TEXT/SEQFILE without changing much in job flow.
* Otherwise, pick ORC (Hive-heavy) or Parquet (multi-engine Spark/Impala) for modern workloads.

---

# 🧠 What is a Hive UDF?

A **User Defined Function (UDF)** in Hive is a **custom function written by the user** to extend Hive’s built-in functionality.

Hive already provides many functions like `SUM()`, `LOWER()`, `CONCAT()`, etc., but sometimes you need logic not covered by these — so you can write your own **UDF** in **Java** (or Python through custom integrations).

---

## ⚙️ **1. Why Use UDFs?**

* To perform **custom calculations** or data transformations.
* To **simplify complex logic** used across multiple queries.
* To **extend HiveQL** with domain-specific logic.
* To **reuse code** instead of writing the same logic in queries repeatedly.

---

## 🧩 **2. Types of User Defined Functions**

| Type     | Full Name                              | Purpose                                                                          |
| :------- | :------------------------------------- | :------------------------------------------------------------------------------- |
| **UDF**  | User Defined Function                  | Operates on a **single row**, returns one value.                                 |
| **UDAF** | User Defined Aggregate Function        | Aggregates **multiple rows** into one (like `SUM`, `AVG`).                       |
| **UDTF** | User Defined Table-Generating Function | Takes one row as input and returns **multiple rows/columns** (like `explode()`). |

---

## 🧱 **3. Architecture Overview**

```
Hive Query → Execution Engine → UDF (custom Java class)
                   ↓
         UDF processes row(s)
                   ↓
          Returns result to Hive
```

When you run a query that uses your UDF, Hive passes the input values to your Java method, executes it, and gets back the result for each row.

---

## 🧮 **4. Writing a Simple UDF (Java)**

### Example: Create a function to reverse a string

#### 🧰 Step 1 — Create a Java class

```java
package com.example.hiveudf;

import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.Text;

public class ReverseStringUDF extends UDF {
    public Text evaluate(Text input) {
        if (input == null) return null;
        return new Text(new StringBuilder(input.toString()).reverse().toString());
    }
}
```

### 🧠 Explanation:

* The class extends `UDF`.
* The method `evaluate()` is called automatically by Hive for each row.
* It takes input (a `Text` type) and returns a `Text` output.

---

#### 🧰 Step 2 — Compile and Package into a JAR

```bash
# Compile
javac -cp $(hadoop classpath):$(hive --auxpath) ReverseStringUDF.java

# Package into jar
jar -cvf ReverseStringUDF.jar com/example/hiveudf/ReverseStringUDF.class
```

---

#### 🧰 Step 3 — Add the JAR to Hive

Start Hive shell and load your JAR:

```sql
ADD JAR /home/hadoop/udfs/ReverseStringUDF.jar;
```

---

#### 🧰 Step 4 — Create a Temporary Function

```sql
CREATE TEMPORARY FUNCTION reverse_str AS 'com.example.hiveudf.ReverseStringUDF';
```

---

#### 🧰 Step 5 — Use it in Query

```sql
SELECT reverse_str(name) FROM employees;
```

✅ **Result:**
If `name = "Alice"`, → output is `"ecilA"`.

---

## 🧪 **5. Example — Numeric Custom Function**

### Example: UDF to Square a Number

```java
package com.example.hiveudf;

import org.apache.hadoop.hive.ql.exec.UDF;

public class SquareUDF extends UDF {
    public Double evaluate(Double num) {
        if (num == null) return null;
        return num * num;
    }
}
```

**Hive Usage:**

```sql
ADD JAR /home/hadoop/udfs/SquareUDF.jar;
CREATE TEMPORARY FUNCTION square AS 'com.example.hiveudf.SquareUDF';
SELECT id, square(salary) AS squared_salary FROM employees;
```

---

## 🧠 **6. Persistent vs Temporary Functions**

| Type                   | Definition                  | Lifetime                  | Stored In                |
| :--------------------- | :-------------------------- | :------------------------ | :----------------------- |
| **Temporary Function** | Created for current session | Ends when session closes  | In-memory                |
| **Permanent Function** | Registered permanently      | Available across sessions | Stored in Hive Metastore |

**Example of permanent function:**

```sql
CREATE FUNCTION mydb.reverse_str AS 'com.example.hiveudf.ReverseStringUDF'
USING JAR 'hdfs:///user/hive/udfs/ReverseStringUDF.jar';
```

---

## 🧩 **7. UDF Error Handling**

You can handle invalid inputs or exceptions in your `evaluate()` method:

```java
public Text evaluate(Text input) {
    try {
        if (input == null) return null;
        return new Text(input.toString().toUpperCase());
    } catch (Exception e) {
        return new Text("ERROR");
    }
}
```

---

## 🧱 **8. Internal Data Flow Diagram**

```
┌──────────────────┐
│  Hive Query       │
│ SELECT reverse(name) FROM emp; │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────┐
│  Hive Execution Engine       │
│  passes row values to UDF    │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│  User Defined Function (Java)│
│  → executes evaluate()       │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────┐
│  Hive Output Row │
└──────────────────┘
```

---

## 💡 **9. Best Practices**

* Always **handle nulls** and invalid inputs.
* Keep your UDFs **lightweight** (avoid large data structures).
* Store **JAR files on HDFS** for multi-node access.
* Use **meaningful names** for functions.
* Prefer **built-in functions** unless truly necessary.

---

## ✅ **Summary Table**

| Aspect       | Description                   | Example                           |
| :----------- | :---------------------------- | :-------------------------------- |
| **Purpose**  | Extend Hive with custom logic | Reverse a string, square a number |
| **Language** | Java (most common)            |                                   |
| **Method**   | Must implement `evaluate()`   |                                   |
| **Register** | `ADD JAR` + `CREATE FUNCTION` |                                   |
| **Use**      | As a normal Hive function     | `SELECT reverse_str(name)`        |
| **Types**    | UDF, UDAF, UDTF               | Row, Aggregate, Table-generating  |

---

# **Serialization and Deserialization in Hive**

Serialization and Deserialization (often abbreviated as **SerDe**) are essential mechanisms in **Apache Hive** that define how Hive reads and writes data stored in HDFS.

---

## **1. Introduction to SerDe**

* **SerDe** stands for **Serialization/Deserialization**.
* It tells Hive **how to interpret the data** (when reading from files) and **how to write it back** (when saving results).
* Hive itself **does not understand raw file formats** like text, Avro, or Parquet — it relies on SerDe classes to handle them.

---

## **2. Key Concepts**

| Process             | Description                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Serialization**   | Converting structured Hive data into a storage format for HDFS (e.g., converting table rows into text or binary format).                           |
| **Deserialization** | Converting data stored in HDFS into a structured format that Hive can process (e.g., reading text files and converting them into Hive table rows). |

---

## **3. Why SerDe is Needed**

* Hive can process different file types — text, ORC, Parquet, JSON, etc.
* Each format stores data differently.
* SerDe defines **how Hive should parse and store data** for each format.
* Without SerDe, Hive wouldn’t know how to interpret file contents.

---

## **4. Common Built-in SerDes in Hive**

| **File Format / Data Type** | **SerDe Class**                                               | **Description**                                                 |
| --------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------- |
| Text File                   | `org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe`          | Default SerDe for plain text files. Supports custom delimiters. |
| CSV                         | `org.apache.hadoop.hive.serde2.OpenCSVSerde`                  | Reads CSV data where fields are separated by commas.            |
| JSON                        | `org.apache.hive.hcatalog.data.JsonSerDe`                     | Parses JSON-formatted data.                                     |
| ORC                         | `org.apache.hadoop.hive.ql.io.orc.OrcSerde`                   | For optimized ORC file format (columnar storage).               |
| Parquet                     | `org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe` | For reading/writing Parquet files.                              |
| Avro                        | `org.apache.hadoop.hive.serde2.avro.AvroSerDe`                | For Avro file format (schema-based binary format).              |
| RegEx                       | `org.apache.hadoop.hive.serde2.RegexSerDe`                    | Parses text using regular expressions.                          |

---

## **5. Example: Using a Custom SerDe**

### **Example 1 – CSV SerDe**

```sql
CREATE TABLE employees (
  id INT,
  name STRING,
  salary FLOAT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/employees';
```

* Here, the **OpenCSVSerde** tells Hive how to interpret CSV-formatted data.

---

### **Example 2 – JSON SerDe**

```sql
CREATE TABLE student_json (
  id INT,
  name STRING,
  department STRING
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/user/hive/warehouse/student_json';
```

* This allows Hive to automatically parse JSON objects into columns.

---

## **6. Custom SerDe**

* Developers can write **custom SerDe classes** in Java.
* Used when:

  * You have a **custom file format** not supported by built-in SerDes.
  * You want to **optimize performance** for specialized data storage.

---

## **7. Key Differences: Serialization vs. Deserialization**

| **Aspect**          | **Serialization**                                | **Deserialization**                            |
| ------------------- | ------------------------------------------------ | ---------------------------------------------- |
| **Purpose**         | Converts Hive rows → storage format              | Converts storage format → Hive rows            |
| **When it happens** | During `INSERT`, `WRITE`, or `EXPORT` operations | During `SELECT`, `LOAD`, or `QUERY` operations |
| **Direction**       | Output to HDFS                                   | Input from HDFS                                |

---

## **8. Summary**

| **Feature**         | **Description**                                   |
| ------------------- | ------------------------------------------------- |
| **SerDe Full Form** | Serialization and Deserialization                 |
| **Purpose**         | Define how Hive reads/writes various file formats |
| **Default SerDe**   | `LazySimpleSerDe` (for text files)                |
| **Supports**        | Text, CSV, JSON, Avro, ORC, Parquet, etc.         |
| **Custom SerDe**    | Allows user-defined format handling               |

---

## **9. Real-world Use Case**

Imagine you receive JSON data logs from an application:

```json
{"id": 1, "name": "Alice", "score": 98}
{"id": 2, "name": "Bob", "score": 87}
```

You can use a JSON SerDe to easily query it:

```sql
SELECT name, score FROM student_json WHERE score > 90;
```

Without the SerDe, Hive wouldn’t understand how to map JSON keys to columns.

---

# **Pig: Introduction**

---

## **1. What is Apache Pig?**

* **Apache Pig** is a **high-level platform** developed by **Yahoo!** for **analyzing large datasets** in the **Hadoop ecosystem**.
* It provides a **simple scripting language** called **Pig Latin** to process and analyze data stored in **HDFS** (Hadoop Distributed File System).
* Pig converts the scripts written in Pig Latin into a series of **MapReduce jobs** that run on a Hadoop cluster.

---

## **2. Need for Pig**

Before Pig, developers had to write **complex Java MapReduce programs** to process data in Hadoop — which was **time-consuming** and **hard to debug**.
Pig simplifies this process by providing:

* A **scripting interface** instead of Java.
* Automatic handling of **MapReduce job generation**.
* Faster **data manipulation and transformation**.

---

## **3. Key Features of Apache Pig**

| **Feature**                      | **Description**                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| **High-Level Language**          | Pig Latin is easy to read, similar to SQL but more procedural.                          |
| **Simplified Data Processing**   | Handles complex data operations like joins, filters, and grouping easily.               |
| **Extensible**                   | Users can create **User Defined Functions (UDFs)** in Java, Python, or other languages. |
| **Handles Semi-Structured Data** | Works well with unstructured or semi-structured data like logs, JSON, XML.              |
| **Automatic Optimization**       | Pig automatically optimizes execution plans.                                            |
| **Scalable**                     | Built on Hadoop, so it scales to process **terabytes or petabytes** of data.            |

---

## **4. What is Pig Latin?**

* **Pig Latin** is the **data flow language** used in Apache Pig.
* It describes a **series of steps** to load, transform, and store data.
* Unlike SQL (which is declarative), Pig Latin is **procedural**, meaning you describe *how* data should be processed step by step.

---

### **Example: Word Count in Pig Latin**

```pig
-- Load the input file from HDFS
lines = LOAD '/user/data/input.txt' AS (line:chararray);

-- Split each line into words
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) AS word;

-- Group similar words
grouped_words = GROUP words BY word;

-- Count occurrences
wordcount = FOREACH grouped_words GENERATE group, COUNT(words);

-- Store the output back into HDFS
STORE wordcount INTO '/user/data/output';
```

✅ **Explanation:**

* This program counts the frequency of words in a text file — just like a MapReduce job — but with **simple, readable commands**.

---

## **5. Pig Architecture**

Apache Pig operates in **two modes**:

1. **Local Mode** – Runs on a single machine using the local file system (useful for testing).
2. **MapReduce Mode (Cluster Mode)** – Runs on a Hadoop cluster and uses HDFS for storage.

### **Pig Components**

| **Component**        | **Description**                                          |
| -------------------- | -------------------------------------------------------- |
| **Parser**           | Checks syntax of Pig Latin and generates a logical plan. |
| **Optimizer**        | Optimizes the logical plan for efficiency.               |
| **Compiler**         | Converts logical plan to physical plan (MapReduce jobs). |
| **Execution Engine** | Executes MapReduce jobs on Hadoop.                       |

---

## **6. Data Types in Pig**

| **Type**  | **Description**       | **Example**                  |
| --------- | --------------------- | ---------------------------- |
| **Atom**  | Single value          | `'Alice'`, `42`              |
| **Tuple** | Ordered set of fields | `(1, 'Alice', 25)`           |
| **Bag**   | Collection of tuples  | `{(1, 'A'), (2, 'B')}`       |
| **Map**   | Key-value pairs       | `[‘name’#‘Alice’, ‘age’#25]` |

---

## **7. Pig vs MapReduce**

| **Aspect**            | **MapReduce**  | **Pig**                   |
| --------------------- | -------------- | ------------------------- |
| **Language**          | Java           | Pig Latin (scripting)     |
| **Ease of Use**       | Complex        | Simple and readable       |
| **Development Time**  | Long           | Short                     |
| **Data Type Support** | Primitive only | Complex (tuple, bag, map) |
| **Optimization**      | Manual         | Automatic                 |

---

## **8. Pig vs Hive**

| **Aspect**    | **Pig**                    | **Hive**                       |
| ------------- | -------------------------- | ------------------------------ |
| **Language**  | Pig Latin (procedural)     | HiveQL (SQL-like, declarative) |
| **Use Case**  | Data flow & ETL operations | Querying structured data       |
| **Users**     | Programmers                | Analysts                       |
| **Execution** | MapReduce jobs             | MapReduce/Tez/Spark            |
| **Schema**    | Schema optional            | Schema mandatory               |

---

## **9. Advantages of Pig**

* Shorter and cleaner scripts compared to MapReduce.
* Supports **complex data transformations**.
* **Extensible** with custom UDFs.
* **Automatic optimization** improves performance.
* **Interoperates** with HDFS, HBase, and other Hadoop tools.

---

## **10. Limitations of Pig**

* **Not suitable for real-time processing** (batch-oriented).
* **Slower than Spark** or modern frameworks.
* Requires some understanding of **data flow concepts**.
* Lacks strong **interactive querying** capabilities.

---

## **11. Real-world Use Cases**

* **Data Cleaning**: Removing duplicates, filtering logs.
* **ETL (Extract, Transform, Load)**: Transforming data before loading into warehouses.
* **Log Analysis**: Analyzing server or clickstream logs.
* **Data Sampling**: Preparing datasets for machine learning.

---

### **Summary**

| **Feature**          | **Description**                              |
| -------------------- | -------------------------------------------- |
| **Developed By**     | Yahoo!                                       |
| **Language**         | Pig Latin                                    |
| **Execution Engine** | MapReduce                                    |
| **Use Case**         | Batch processing & ETL                       |
| **Data Format**      | Structured, semi-structured, or unstructured |
| **Modes**            | Local and MapReduce                          |
| **Output**           | Stored in HDFS                               |

---

# 🧩 **Anatomy of Apache Pig**

---

## **1. Overview**

The **anatomy of Pig** refers to how Pig processes a Pig Latin script — from **loading the data** to **executing MapReduce jobs** on a Hadoop cluster.

Apache Pig is made up of several **components** that work together to:

1. Parse and validate the script,
2. Optimize the data flow, and
3. Convert it into **MapReduce jobs** for execution.

---

## **2. Pig Architecture Diagram**

```
          ┌────────────────────────────┐
          │     Pig Latin Script       │
          └────────────┬───────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │        Parser           │
            │  (Syntax & Semantic)    │
            └────────────┬────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │     Logical Plan        │
            └────────────┬────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │     Optimizer           │
            │ (Logical Plan Optim.)   │
            └────────────┬────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │     Physical Plan       │
            └────────────┬────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │  MapReduce Compiler     │
            │ (Converts to MR jobs)   │
            └────────────┬────────────┘
                       │
                       ▼
            ┌────────────────────────┐
            │   Execution Engine      │
            │ (Executes on Hadoop)    │
            └────────────────────────┘
```

---

## **3. Components of Pig Architecture**

### **(a) Pig Latin Script**

* The user writes a **Pig Latin script** that describes the data flow — for example:

  ```pig
  A = LOAD 'input.txt' AS (word:chararray);
  B = GROUP A BY word;
  C = FOREACH B GENERATE group, COUNT(A);
  STORE C INTO 'output';
  ```
* This script defines **how data moves** from one operation to another.

---

### **(b) Parser**

* **Function:** Checks **syntax** and **data types** in the Pig Latin script.
* **Output:** Generates a **Logical Plan** — a DAG (Directed Acyclic Graph) representation of all operations.
* **Tasks:**

  * Tokenizes and parses the script.
  * Validates syntax.
  * Checks schema compatibility.

🧠 **Example:**
If you wrote:

```pig
A = LOAD 'data.txt' AS (name:int);
```

but the data is actually a string — the parser detects a **type mismatch error**.

---

### **(c) Logical Plan**

* Represents **what needs to be done**, not **how**.
* Describes operations in logical sequence (like SQL execution plan).
* Independent of Hadoop or MapReduce at this stage.

🧩 Example:
`LOAD → FILTER → GROUP → FOREACH → STORE`

---

### **(d) Optimizer**

* Optimizes the **logical plan** to improve performance.
* **Tasks:**

  * Removes unnecessary operations (projection pushdown).
  * Combines operations when possible (e.g., merging filters).
  * Reorders data flow for efficiency.

💡 **Example:** If two filters can be combined into one, Pig’s optimizer will do that automatically.

---

### **(e) Physical Plan**

* The optimized logical plan is translated into a **physical plan**,
  which defines **how** the operations will be executed.
* Breaks down steps into **physical operators** like `POLoad`, `POFilter`, `POJoin`, etc.

---

### **(f) MapReduce Compiler**

* Converts the **physical plan** into a series of **MapReduce jobs**.
* Each **Pig operation** (like GROUP BY or JOIN) becomes a **MapReduce task**.
* Handles **job scheduling**, **data shuffling**, and **task dependencies**.

🧠 **Example:**
If your Pig script has two GROUP BY operations, the compiler might generate two separate MapReduce jobs that run sequentially.

---

### **(g) Execution Engine**

* Submits MapReduce jobs to the **Hadoop cluster**.
* Monitors progress and collects results from **HDFS**.
* If running in **local mode**, it executes jobs directly on your local file system.

---

## **4. Execution Modes**

| **Mode**                         | **Description**                                                                                | **Command Example**       |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| **Local Mode**                   | Runs on a single JVM and uses the local file system. Useful for development or small datasets. | `pig -x local script.pig` |
| **MapReduce Mode (Hadoop Mode)** | Default mode — runs on Hadoop cluster using HDFS. Used for processing huge datasets.           | `pig script.pig`          |

---

## **5. Data Flow in Pig**

| **Step** | **Process**                     | **Component**          |
| -------- | ------------------------------- | ---------------------- |
| 1        | User writes Pig Latin script    | Pig Latin Interface    |
| 2        | Script is parsed and validated  | Parser                 |
| 3        | Logical plan is created         | Logical Plan Generator |
| 4        | Logical plan optimized          | Optimizer              |
| 5        | Physical plan generated         | Compiler               |
| 6        | Converted into MapReduce jobs   | MR Compiler            |
| 7        | Jobs executed on Hadoop cluster | Execution Engine       |

---

## **6. Example Flow**

Let’s take this Pig Latin code:

```pig
A = LOAD '/user/data/input.txt' AS (line:chararray);
B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;
C = GROUP B BY word;
D = FOREACH C GENERATE group, COUNT(B);
STORE D INTO '/user/data/output';
```

**Flow Explanation:**

| **Step** | **Action**                                         | **Stage**        |
| -------- | -------------------------------------------------- | ---------------- |
| 1        | Script parsed                                      | Parser           |
| 2        | Logical Plan built: Load → Foreach → Group → Store | Logical Plan     |
| 3        | Optimized plan created                             | Optimizer        |
| 4        | Converted to MR Jobs                               | MR Compiler      |
| 5        | Jobs executed on Hadoop                            | Execution Engine |

---

## **7. Summary Table**

| **Component**        | **Purpose**                            |
| -------------------- | -------------------------------------- |
| **Parser**           | Checks syntax and builds logical plan  |
| **Optimizer**        | Improves plan efficiency               |
| **Compiler**         | Converts logical plan to physical plan |
| **MR Compiler**      | Generates MapReduce jobs               |
| **Execution Engine** | Runs jobs on Hadoop and stores results |

---

✅ **In short:**

> Pig Latin → Parser → Logical Plan → Optimizer → Physical Plan → MapReduce Compiler → Execution Engine (Hadoop)

---

# 🧠 **Features of Apache Pig**

---

Apache **Pig** is designed to simplify **big data processing** in the **Hadoop ecosystem**.
Its features make it easy for developers to handle **large, complex, and semi-structured datasets** without writing low-level MapReduce code.

---

## 🧩 **1. High-Level Data Flow Language (Pig Latin)**

* Pig uses a **high-level scripting language** called **Pig Latin**.
* It allows users to express **data transformations and computations** easily.
* Pig Latin is **procedural** — meaning it describes *how* data flows, step by step.

📘 **Example:**

```pig
data = LOAD '/data/sales.txt' AS (item:chararray, price:int);
filtered = FILTER data BY price > 100;
grouped = GROUP filtered BY item;
result = FOREACH grouped GENERATE group, COUNT(filtered);
DUMP result;
```

✅ This script:

* Loads sales data
* Filters out cheap items
* Groups by item
* Counts how many times each item appears

No Java or MapReduce code needed!

---

## ⚙️ **2. Handles Both Structured and Semi-Structured Data**

* Pig can process:

  * **Structured data** (like tables, CSV)
  * **Semi-structured data** (like logs, JSON, XML)
  * **Unstructured data** (like plain text)

🧠 **Why it matters:**
Unlike SQL or Hive (which prefer structured data), Pig can **handle data with irregular formats**, making it ideal for web logs, clickstreams, and social media feeds.

---

## ⚡ **3. Extensibility**

Pig supports **User Defined Functions (UDFs)** written in:

* **Java**
* **Python**
* **JavaScript**
* **Ruby**

You can create custom logic for:

* Filtering data
* Transforming fields
* Aggregations or complex calculations

📘 **Example:**

```python
# Python UDF (for Pig)
@outputSchema("word:chararray")
def to_upper(word):
    return word.upper()
```

You can register this in your Pig script:

```pig
REGISTER 'udf.py' USING jython AS myfuncs;
A = LOAD 'input.txt' AS (w:chararray);
B = FOREACH A GENERATE myfuncs.to_upper(w);
DUMP B;
```

---

## 🧮 **4. Optimized Execution (Automatic Optimization)**

* Pig optimizes your scripts **automatically** before converting them to MapReduce jobs.
* The **optimizer**:

  * Removes redundant operations
  * Pushes filters earlier in the pipeline (projection pushdown)
  * Merges jobs when possible

✅ **Result:** Faster execution without manual tuning.

---

## 🗂️ **5. Multi-Language Support**

* UDFs can be written in **Java**, **Python (Jython)**, **Ruby**, or **Groovy**.
* This makes Pig flexible and accessible to non-Java developers.

---

## 💾 **6. Schema Flexibility**

* Pig doesn’t require a **fixed schema** like RDBMS or Hive.
* It can infer schema dynamically at runtime.
* This helps when dealing with data that changes structure frequently.

📘 **Example:**

```pig
A = LOAD 'data.txt' AS (name, age);
```

If one record is missing `age`, Pig still processes the rest — it just marks missing values as `null`.

---

## 🧩 **7. Ease of Programming**

* Pig scripts are **much shorter** than equivalent MapReduce programs.
* Developers focus on **data flow**, not on **boilerplate Java code**.
* Less prone to human error, and easier to debug and test.

---

## ☁️ **8. Integration with Hadoop Ecosystem**

Pig works **seamlessly** with:

* **HDFS** – to store and retrieve data
* **HBase** – for reading/writing NoSQL tables
* **HCatalog** – for metadata management
* **Hive** – for shared schema access
* **Oozie** – for workflow automation

✅ You can use Pig in the same environment as Hive, Spark, and other Hadoop tools.

---

## 🧰 **9. Multiple Execution Modes**

Pig supports two modes:

| **Mode**                         | **Description**                                  | **Use Case**                     |
| -------------------------------- | ------------------------------------------------ | -------------------------------- |
| **Local Mode**                   | Runs using the local file system and single JVM. | For testing small data locally.  |
| **MapReduce Mode (Hadoop Mode)** | Runs on Hadoop cluster using HDFS.               | For large-scale data processing. |

🔹 Example:

```bash
pig -x local script.pig      # Local mode
pig script.pig               # Hadoop mode
```

---

## 📊 **10. Complex Data Type Support**

Pig supports **advanced data types**:

| **Type**  | **Description**      | **Example**                  |
| --------- | -------------------- | ---------------------------- |
| **Atom**  | Single value         | `'Alice'`, `42`              |
| **Tuple** | Ordered fields       | `(1, 'Bob', 25)`             |
| **Bag**   | Collection of tuples | `{(1, 'A'), (2, 'B')}`       |
| **Map**   | Key-value pairs      | `[‘name’#‘Alice’, ‘age’#25]` |

✅ This flexibility allows Pig to handle **nested and irregular data**, unlike SQL.

---

## 🚀 **11. Fault Tolerance**

* Since Pig runs on top of Hadoop, it inherits **HDFS fault tolerance**.
* If a node fails, tasks are automatically re-executed on another node.
* Data remains **safe and consistent** across the cluster.

---

## 🧩 **12. Open Source and Extensible**

* Developed by **Yahoo!** and maintained by the **Apache Software Foundation**.
* Completely **open-source** and free to use.
* Has an **active community** contributing UDFs and performance improvements.

---

## 💡 **13. Lazy Evaluation**

* Pig doesn’t execute commands immediately.
* It builds an **execution plan** first, and only runs it when an action (like `DUMP` or `STORE`) is called.

📘 **Example:**

```pig
A = LOAD 'data.txt';
B = FILTER A BY $1 > 100;
C = GROUP B BY $0;
DUMP C;     -- execution starts here
```

✅ All steps before `DUMP` are *planned*, not executed.

---

## 🧾 **14. Data Lineage (Tracking Data Flow)**

* Pig maintains **metadata** about how data is processed through each stage.
* This helps in **debugging**, **auditing**, and **understanding data transformations**.

---

## 🏁 **15. Parallel Execution**

* Pig supports **parallelism** — multiple reducers or tasks can process data simultaneously.
* This increases performance and scalability for massive datasets.

---

### 🧠 **Summary of Apache Pig Features**

| **Feature**                   | **Description**                           |
| ----------------------------- | ----------------------------------------- |
| High-level scripting language | Simplifies data transformation            |
| Extensible                    | Supports UDFs in multiple languages       |
| Works with all data types     | Structured, semi-structured, unstructured |
| Automatic optimization        | Improves efficiency automatically         |
| Flexible schema               | Doesn’t require fixed structure           |
| Fault tolerant                | Inherits from Hadoop                      |
| Lazy evaluation               | Executes only when needed                 |
| Multiple execution modes      | Local or Hadoop cluster                   |
| Complex data types            | Tuples, Bags, Maps supported              |
| Parallel execution            | Processes data faster                     |

---

✅ **In Short:**

> Apache Pig = Simplicity of scripting + Power of Hadoop + Flexibility of schema + Scalability for big data.

---

# **Pig: Philosophy**

**Apache Pig Philosophy** revolves around **simplicity, scalability, and extensibility** for big data processing on Hadoop. It was created by Yahoo! to make working with Hadoop easier for non-Java developers and data analysts.

---

### 🧠 **Core Philosophy of Pig**

1. **High-Level Data Flow Language (Pig Latin)**

   * Pig provides **Pig Latin**, a scripting language that describes **data flow**, not **map-reduce logic**.
   * Instead of writing complex Java MapReduce programs, users write simple scripts that define how data should be read, transformed, and stored.

2. **Abstraction from MapReduce**

   * Pig hides the **complexities of Hadoop’s MapReduce**.
   * Each Pig Latin command is automatically converted into one or more **MapReduce jobs** internally.

3. **Optimization Opportunities**

   * The Pig engine optimizes the execution automatically.
   * This allows **logical optimization** (e.g., filter before join) and **physical optimization** (e.g., using combiners).

4. **Extensibility**

   * Pig allows **User Defined Functions (UDFs)** written in Java, Python, or other languages.
   * Users can define their own data processing logic easily.

5. **Schema Flexibility**

   * Pig can handle both **structured** and **semi-structured** data.
   * Schema is **optional** — Pig can infer structure dynamically.

6. **Parallel Execution**

   * Pig automatically handles **data parallelization** by splitting work across multiple nodes in the Hadoop cluster.

7. **Support for Iterative and Ad-hoc Processing**

   * Ideal for **data scientists** and **analysts** who experiment with datasets interactively.
   * Quick scripting and modification are possible without recompilation.

---

### ⚙️ **Pig Philosophy vs SQL Philosophy**

| Concept               | Pig Philosophy                               | SQL Philosophy                    |
| --------------------- | -------------------------------------------- | --------------------------------- |
| **Language Type**     | Procedural (step-by-step flow)               | Declarative (what to do, not how) |
| **Abstraction Level** | High-level over MapReduce                    | High-level over RDBMS             |
| **Data Type Support** | Semi-structured and unstructured             | Strictly structured               |
| **Optimization**      | Logical and physical plan-based              | Query optimizer in DB engine      |
| **Execution Engine**  | Hadoop MapReduce (can also use Tez or Spark) | Relational Database Engine        |

---

### 💡 **Example**

```pig
-- Load data
data = LOAD 'students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);

-- Filter and group
top_students = FILTER data BY marks > 80;
grouped = GROUP top_students BY name;

-- Generate result
result = FOREACH grouped GENERATE group AS student_name, COUNT(top_students);
DUMP result;
```

➡️ Pig translates this into multiple optimized MapReduce jobs automatically.

---

### 🧩 **Summary**

* Pig simplifies Hadoop programming using **data flow scripting**.
* It embodies the philosophy of **simplified coding, flexible data handling, and automatic optimization**.
* Ideal for **data preprocessing, ETL, and exploration tasks** in big data environments.

---

# **Pig: Use Cases**

Apache Pig is widely used in **Big Data ecosystems** for **data transformation, cleaning, and preparation** tasks before data is loaded into analytics systems. It is most suitable for **ETL (Extract, Transform, Load)** operations and **large-scale data processing**.

---

### 🧩 **1. Data Transformation and Cleaning**

* **Purpose:** Convert raw, unstructured, or semi-structured data into a clean, structured format.
* **Example:**

  * Remove duplicates, null values, or outliers from web log data.
  * Convert inconsistent formats (e.g., “male/female” → “M/F”).

**Example Pig Script:**

```pig
logs = LOAD 'access_logs.txt' USING PigStorage(' ') AS (ip:chararray, status:int);
cleaned = FILTER logs BY status == 200;
STORE cleaned INTO 'clean_logs' USING PigStorage(',');
```

✅ *Pig’s data flow model is perfect for sequential transformations like filtering, grouping, and aggregating.*

---

### 🧾 **2. ETL (Extract, Transform, Load) Processing**

* **Purpose:** Process raw data from multiple sources and load it into a data warehouse like Hive or HDFS.
* **Example:**

  * Extract from CSV/JSON, transform with Pig scripts, and store the output in Hive for analytics.

**Pipeline Example:**

```
Raw Logs (HDFS) → Pig Transformations → Hive Table (for Analysis)
```

✅ *Pig acts as the middle layer for heavy data processing before storage.*

---

### 📊 **3. Log Analysis**

* **Purpose:** Analyze web server logs, clickstream data, or social media logs.
* **Example:**

  * Count how many times each page was visited.
  * Identify the most active users.

**Example Pig Script:**

```pig
logs = LOAD 'web_logs' USING PigStorage(' ') AS (user:chararray, page:chararray);
grouped = GROUP logs BY page;
page_counts = FOREACH grouped GENERATE group, COUNT(logs);
DUMP page_counts;
```

✅ *Used by Yahoo!, LinkedIn, and Twitter for large-scale log analysis.*

---

### 💬 **4. Data Sampling and Debugging**

* **Purpose:** Create smaller representative datasets for testing or model training.
* **Example:** Randomly select 1% of user data for model validation.

```pig
data = LOAD 'users' USING PigStorage(',') AS (id:int, name:chararray, country:chararray);
sample = SAMPLE data 0.01;
DUMP sample;
```

✅ *Efficiently handles sampling on petabyte-scale datasets.*

---

### 🧮 **5. Data Aggregation and Reporting**

* **Purpose:** Summarize data by performing groupings and aggregations.
* **Example:**

  * Calculate average sales per region or total clicks per ad campaign.

```pig
sales = LOAD 'sales_data.csv' USING PigStorage(',') AS (region:chararray, amount:double);
grouped = GROUP sales BY region;
summary = FOREACH grouped GENERATE group, SUM(sales.amount);
STORE summary INTO 'sales_summary';
```

✅ *Pig simplifies complex aggregation workflows using minimal code.*

---

### 🤖 **6. Machine Learning Preprocessing**

* **Purpose:** Prepare data for ML algorithms — feature extraction, normalization, and joining multiple data sources.
* **Example:** Clean and combine customer and transaction data before feeding it to ML models in Spark or Python.

✅ *Pig handles the preprocessing while computation-heavy tasks can later run in Spark or Python.*

---

### 🏭 **7. Data Migration Between Systems**

* **Purpose:** Move and reformat data between systems (e.g., HDFS → Hive → HBase).
* **Example:** Convert JSON data to tabular Hive-compatible format.

✅ *Pig acts as a flexible data converter between heterogeneous storage systems.*

---

### 💡 **Summary**

| **Use Case**     | **Description**                            |
| ---------------- | ------------------------------------------ |
| Data Cleaning    | Remove invalid, duplicate, or null records |
| ETL Workflows    | Transform and load data into warehouses    |
| Log Analysis     | Process massive web and system logs        |
| Sampling         | Create smaller representative datasets     |
| Aggregation      | Summarize data (sum, avg, count, etc.)     |
| ML Preprocessing | Prepare large datasets for training        |
| Data Migration   | Reformat and move data across systems      |

---

# 🐷 **Pig Latin Overview**

**Pig Latin** is the **data flow language** used in **Apache Pig** for analyzing large data sets.
It is a **high-level scripting language** designed to simplify the process of writing **MapReduce programs**.

Instead of manually coding in Java for Hadoop MapReduce, Pig Latin allows you to express the same logic in **simple, SQL-like scripts**.

---

## 🔹 **1. What is Pig Latin?**

* Pig Latin is a **procedural language** that describes **how** data flows from input to output.
* Each Pig Latin statement represents a **step** in a data transformation process.
* The **Pig engine** internally converts Pig Latin scripts into **MapReduce jobs**, which are then executed on Hadoop.

✅ **In short:**
Pig Latin = Simplified data flow programming over Hadoop MapReduce.

---

## 🔹 **2. Example of a Pig Latin Script**

Let’s understand with an example.

```pig
-- Load the data
students = LOAD 'students.csv' USING PigStorage(',') 
            AS (id:int, name:chararray, marks:int);

-- Filter students who scored above 70
toppers = FILTER students BY marks > 70;

-- Group by name
grouped = GROUP toppers BY name;

-- Count how many times each name appears
name_count = FOREACH grouped GENERATE group, COUNT(toppers);

-- Store the output
STORE name_count INTO 'output' USING PigStorage(',');
```

🔸 **What happens here:**

* `LOAD` → reads data from HDFS or local.
* `FILTER` → applies condition (marks > 70).
* `GROUP` → groups by column (name).
* `FOREACH...GENERATE` → applies transformation on each group.
* `STORE` → writes results back to HDFS.

---

## 🔹 **3. Pig Latin Data Model**

Pig works on **nested data structures**, unlike traditional RDBMS.

| **Type**  | **Description**               | **Example**                |
| --------- | ----------------------------- | -------------------------- |
| **Atom**  | Single value (number, string) | `'John'`, `25`             |
| **Tuple** | Ordered set of fields         | `(‘John’, 25, ‘CS’)`       |
| **Bag**   | Collection of tuples          | `{(‘John’,25),(‘Sam’,30)}` |
| **Map**   | Key-value pairs               | `['name'#'John','age'#25]` |

✅ This flexibility allows Pig to handle **semi-structured data** (like JSON or logs).

---

## 🔹 **4. Features of Pig Latin**

1. **Data Flow Language:**

   * You define a *series of transformations* that form a directed data flow graph.

2. **Extensible:**

   * You can define your own **User Defined Functions (UDFs)** in Java, Python, or other languages.

3. **Parallel Execution:**

   * Pig automatically distributes operations over Hadoop cluster nodes.

4. **Schema Flexibility:**

   * You can process **unstructured or partially structured data** easily.

5. **Optimization:**

   * Pig optimizes the data flow internally before running it as MapReduce jobs.

---

## 🔹 **5. Important Pig Latin Commands**

| **Category**         | **Command**                         | **Purpose**             |
| -------------------- | ----------------------------------- | ----------------------- |
| **Load/Store**       | `LOAD`, `STORE`, `DUMP`             | Read/write data         |
| **Filter/Transform** | `FILTER`, `FOREACH`, `DISTINCT`     | Modify or clean data    |
| **Grouping/Joining** | `GROUP`, `JOIN`, `COGROUP`          | Combine datasets        |
| **Sorting**          | `ORDER`, `LIMIT`, `SAMPLE`          | Organize or reduce data |
| **Aggregation**      | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` | Summarize data          |

---

## 🔹 **6. Pig Latin vs SQL**

| **Aspect**             | **Pig Latin**                     | **SQL**                     |
| ---------------------- | --------------------------------- | --------------------------- |
| **Nature**             | Procedural                        | Declarative                 |
| **Processing**         | Step-by-step data flow            | Query-based                 |
| **Schema**             | Optional (schema on read)         | Mandatory (schema on write) |
| **Complex Data Types** | Supports nested (bag, map, tuple) | Flat only                   |
| **Use Case**           | ETL, data transformation          | Querying relational data    |

✅ *Pig Latin tells how to process data (procedural)*
✅ *SQL tells what data is needed (declarative)*

---

## 🔹 **7. Execution Flow of a Pig Script**

1. **Parsing:**

   * Pig validates the syntax.

2. **Logical Plan Generation:**

   * Pig builds a logical flow of operations.

3. **Optimization:**

   * Combines and optimizes logical steps.

4. **Physical Plan:**

   * Converts logic to executable steps.

5. **MapReduce Jobs:**

   * Executes the final plan on Hadoop.

---

## 🧠 **Example Summary**

| **Task**    | **SQL Approach**                         | **Pig Latin Approach**                             |
| ----------- | ---------------------------------------- | -------------------------------------------------- |
| Select rows | `SELECT * FROM students WHERE marks>70;` | `FILTER students BY marks>70;`                     |
| Group by    | `GROUP BY name;`                         | `GROUP students BY name;`                          |
| Aggregate   | `COUNT(name)`                            | `FOREACH grouped GENERATE group, COUNT(students);` |

---

## 🧩 **Key Takeaway**

* Pig Latin is **simpler than Java MapReduce** and **more flexible than SQL**.
* It enables **fast, iterative data transformations** for **Big Data processing**.
* Used by organizations like **Yahoo!, Twitter, and LinkedIn** for scalable data analysis.

---

# 🐷 Pig Primitive Data Types

---

## 🔹 **1. Overview**

In **Apache Pig**, every piece of data is represented in a **data model** composed of:

1. **Primitive Data Types** → simple atomic values (numbers, strings, etc.)
2. **Complex Data Types** → combinations of primitive ones (tuple, bag, map)

We’ll focus on **primitive data types** here — these are **the smallest units** of data in Pig Latin.

---

## 🔹 **2. List of Pig Primitive Data Types**

| **Data Type**  | **Description**                    | **Example**              | **Internal Representation**         |
| -------------- | ---------------------------------- | ------------------------ | ----------------------------------- |
| **int**        | 32-bit signed integer              | `123`                    | `java.lang.Integer`                 |
| **long**       | 64-bit signed integer              | `9876543210L`            | `java.lang.Long`                    |
| **float**      | 32-bit floating point number       | `3.14F`                  | `java.lang.Float`                   |
| **double**     | 64-bit floating point number       | `123.456`                | `java.lang.Double`                  |
| **chararray**  | Sequence of characters (string)    | `'hello'`                | `java.lang.String`                  |
| **bytearray**  | Raw binary data (unknown schema)   | `b'11001010'`            | `org.apache.pig.data.DataByteArray` |
| **boolean**    | Logical true/false                 | `true`, `false`          | `java.lang.Boolean`                 |
| **datetime**   | Timestamp value                    | `'2024-03-21T10:15:30Z'` | `org.joda.time.DateTime`            |
| **biginteger** | Arbitrary large integer            | `1234567890123456789`    | `java.math.BigInteger`              |
| **bigdecimal** | Arbitrary precision decimal number | `12345.6789`             | `java.math.BigDecimal`              |

---

## 🔹 **3. Type Inference Example**

Pig tries to **infer** (auto-detect) data type when you load data.

Example:

```pig
data = LOAD 'numbers.txt' USING PigStorage(',')
       AS (id:int, price:float, name:chararray);
```

📄 **numbers.txt**

```
1,45.5,Book
2,60.0,Pen
3,30.5,Pencil
```

Here:

* `id` → `int`
* `price` → `float`
* `name` → `chararray`

If you don’t specify data types, Pig treats all fields as `bytearray` by default.

---

## 🔹 **4. Type Conversion in Pig**

Sometimes you need to convert between types using **casting**.

### Example:

```pig
A = LOAD 'data.csv' USING PigStorage(',') AS (x:chararray, y:chararray);
B = FOREACH A GENERATE (int)x AS id, (float)y AS value;
```

➡ Converts strings (`chararray`) into integers and floats.

---

## 🔹 **5. Null Values Handling**

* Pig represents missing or invalid data as **`null`**.
* If a type conversion fails (e.g., converting "abc" to int), it becomes **`null`**.

Example:

```pig
A = LOAD 'data.txt' AS (name:chararray, age:int);
```

If `age` is missing for a record → Pig assigns **null** automatically.

---

## 🔹 **6. Quick Recap Table**

| **Type Category** | **Data Type**                                    | **Example**              | **Used For**          |
| ----------------- | ------------------------------------------------ | ------------------------ | --------------------- |
| **Numeric**       | int, long, float, double, biginteger, bigdecimal | `12`, `3.14`, `100000L`  | Arithmetic operations |
| **String**        | chararray                                        | `'Pig Latin'`            | Text data             |
| **Binary**        | bytearray                                        | `b'001001'`              | Raw or unknown format |
| **Logical**       | boolean                                          | `true`, `false`          | Conditions            |
| **Temporal**      | datetime                                         | `'2025-11-01T14:30:00Z'` | Timestamps            |

---

## 🧠 **Tip**

* Use **chararray** for text fields.
* Use **bytearray** when data schema is not fixed (e.g., logs or raw files).
* Use **casting** to ensure correct data types before performing aggregations or joins.

---

## 🧩 **Visual Summary**

```
Pig Data Types
│
├── Primitive
│   ├── Numeric → int, long, float, double, biginteger, bigdecimal
│   ├── Character → chararray
│   ├── Binary → bytearray
│   ├── Boolean → boolean
│   └── Temporal → datetime
│
└── Complex
    ├── Tuple
    ├── Bag
    └── Map
```

---

# 🐷 Running Pig

---

## 🔹 **1. What Does "Running Pig" Mean?

Running Pig means **executing Pig Latin scripts** — either interactively or in batch — to process data using the **Pig engine**.

Apache Pig can be run in **two main modes**:

1. **Local Mode** (for testing/debugging on a single machine)
2. **MapReduce Mode** (for large-scale distributed processing on Hadoop)

---

## 🔹 **2. Pig Execution Flow**

Whenever you run a Pig script, these steps occur internally:

```
Pig Latin Script
       │
       ▼
   Parsing (Syntax check)
       │
       ▼
  Logical Plan Creation
       │
       ▼
  Optimization
       │
       ▼
  Physical Plan Creation
       │
       ▼
   MapReduce Job Execution
```

So, even if you’re writing high-level Pig Latin, Pig **automatically converts** your code into **MapReduce jobs** for Hadoop.

---

## 🔹 **3. Different Ways to Run Pig**

Apache Pig can be run in **three ways**:

| **Mode**                      | **How to Start**                            | **Purpose**                               |
| ----------------------------- | ------------------------------------------- | ----------------------------------------- |
| **Interactive (Grunt Shell)** | `pig` command                               | Execute Pig commands one-by-one manually. |
| **Batch (Script Mode)**       | `pig myscript.pig`                          | Run a pre-written script file.            |
| **Embedded (Programmatic)**   | Run Pig inside Java using `PigServer` class | Integrate Pig logic into Java code.       |

---

## 🔹 **4. Modes of Execution**

Pig supports two main **execution environments** depending on your setup.

---

### 🧩 **(a) Local Mode**

* Executes Pig scripts **on a single JVM** — no Hadoop cluster needed.
* Input/output are taken from the **local filesystem**.
* Ideal for **small data** or **testing** scripts before deploying to Hadoop.

#### ▶️ Run Command:

```bash
pig -x local
```

#### ▶️ Example:

```bash
pig -x local student_data.pig
```

#### ▶️ Pig Script Example:

```pig
data = LOAD 'students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
top = FILTER data BY marks > 70;
DUMP top;
```

#### ▶️ Output:

```
(1,John,85)
(4,Alice,90)
```

---

### 🧩 **(b) MapReduce Mode (Hadoop Cluster)**

* Default mode when running Pig on a **Hadoop cluster**.
* Pig translates your script into **MapReduce jobs** executed across cluster nodes.
* Uses **HDFS** for reading/writing data.

#### ▶️ Run Command:

```bash
pig -x mapreduce
```

#### ▶️ Example:

```bash
pig -x mapreduce sales_analysis.pig
```

#### ▶️ Workflow Diagram:

```
Pig Script (.pig)
   │
   ▼
   Pig Engine
   │
   ├──> MapReduce Job 1
   ├──> MapReduce Job 2
   └──> ...
   │
   ▼
   HDFS Output
```

---

### 🧠 **Quick Comparison**

| **Aspect**                | **Local Mode**          | **MapReduce Mode**                |
| ------------------------- | ----------------------- | --------------------------------- |
| **Execution Environment** | Local machine           | Hadoop cluster                    |
| **Input/Output**          | Local filesystem        | HDFS                              |
| **Data Size**             | Small                   | Large (terabytes/petabytes)       |
| **Speed**                 | Faster (no network I/O) | Slower (distributed coordination) |
| **Use Case**              | Debugging and testing   | Production data processing        |

---

## 🔹 **5. Running Pig in Grunt Shell (Interactive Mode)**

The **Grunt shell** is Pig’s interactive command-line environment.

### ▶️ Start Grunt:

```bash
pig
```

You’ll see:

```
grunt>
```

Now you can type Pig Latin commands one by one:

```pig
grunt> A = LOAD 'input.txt' AS (x:int, y:int);
grunt> B = FILTER A BY y > 100;
grunt> DUMP B;
```

📌 **Tip:** Use `DUMP` to print data to the console and `STORE` to save output into HDFS.

---

## 🔹 **6. Running Pig Scripts (Batch Mode)**

If you have a `.pig` file, run it directly:

#### Example Script: `wordcount.pig`

```pig
lines = LOAD 'input.txt' AS (line:chararray);
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) AS word;
grouped = GROUP words BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(words);
STORE wordcount INTO 'output' USING PigStorage(',');
```

#### Run Command:

```bash
pig wordcount.pig
```

---

## 🔹 **7. Example: Local Mode Run**

### Input (`students.txt`)

```
1,John,85
2,Ravi,45
3,Alice,90
4,Neha,72
```

### Pig Script (`filter_top.pig`)

```pig
data = LOAD 'students.txt' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
top = FILTER data BY marks >= 70;
STORE top INTO 'output' USING PigStorage(',');
```

### Run:

```bash
pig -x local filter_top.pig
```

### Output (`output/part-m-00000`)

```
1,John,85
3,Alice,90
4,Neha,72
```

---

## 🔹 **8. Logs and Output**

* **Logs** are stored in: `/tmp/pig-log/`
* **Output data** is stored in:

  * Local mode → your local directory
  * MapReduce mode → HDFS path specified in `STORE`

---

## 🔹 **9. Troubleshooting Tips**

| **Issue**                   | **Reason**                      | **Fix**                          |
| --------------------------- | ------------------------------- | -------------------------------- |
| `Input path does not exist` | Wrong file path                 | Check HDFS/local path            |
| `Permission denied`         | HDFS access issue               | Use correct user or permissions  |
| `NullPointerException`      | Schema mismatch or missing data | Use default type `bytearray`     |
| `Class not found`           | Missing JAR in cluster          | Add JAR using `REGISTER` command |

---

## 🧩 **Visual Summary**

```
          ┌───────────────────┐
          │  Pig Latin Script │
          └───────┬───────────┘
                  │
                  ▼
           ┌─────────────┐
           │   Pig Engine│
           └───────┬─────┘
       ┌───────────┴───────────┐
       │                       │
       ▼                       ▼
 Local Mode               MapReduce Mode
 (Single JVM)             (Hadoop Cluster)
```

---

## ✅ **Key Takeaways**

* Pig can run **locally** (no Hadoop) or in **MapReduce** mode (on Hadoop).
* **Grunt shell** allows interactive use; **scripts** allow batch processing.
* Pig converts Pig Latin → **MapReduce jobs** automatically.
* Ideal for both **development** and **large-scale production data** workflows.

---

# 🐷 **Execution Modes of Pig**

Apache Pig supports **two main execution modes** for running Pig Latin scripts depending on your environment setup and data size.

---

## 🔹 **1. What are Execution Modes?

**Execution mode** defines *where and how* your Pig scripts are executed —
whether on a **local machine** or a **distributed Hadoop cluster**.

Pig has **two core execution modes**:

1. **Local Mode** 🧩
2. **MapReduce Mode (Hadoop Cluster Mode)** 🧠

---

## 🔹 **2. Local Mode**

### ✅ **Definition**

* In Local Mode, Pig runs **entirely on a single JVM** (your local computer).
* Both the **Pig engine** and the **data** are local (no Hadoop cluster).
* It does **not** use HDFS or MapReduce framework.

---

### ⚙️ **Command to Run**

```bash
pig -x local
```

or inside a Pig script:

```bash
SET execution.type local;
```

---

### 📦 **Workflow**

```
Pig Script (.pig)
     │
     ▼
  Pig Engine
     │
     ▼
  Local File System (Data Input/Output)
```

---

### 🧠 **Use Cases**

* Small datasets
* Debugging or testing Pig scripts before deploying
* Learning Pig without Hadoop installation

---

### 🧾 **Example**

**Input file: `students.csv`**

```
1,John,85
2,Ravi,45
3,Alice,90
4,Neha,72
```

**Script: `filter_top.pig`**

```pig
data = LOAD 'students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
top = FILTER data BY marks >= 70;
DUMP top;
```

**Run Command:**

```bash
pig -x local filter_top.pig
```

**Output:**

```
(1,John,85)
(3,Alice,90)
(4,Neha,72)
```

---

### 🧩 **Advantages**

| Feature             | Description                                               |
| ------------------- | --------------------------------------------------------- |
| 🏃 Fast             | Runs in a single JVM — no cluster communication overhead. |
| 🧠 Easy to use      | Ideal for learning and script testing.                    |
| 💾 No HDFS required | Works with local file paths.                              |

---

### ⚠️ **Limitations**

| Limitation        | Description                              |
| ----------------- | ---------------------------------------- |
| 🚫 Not scalable   | Can’t handle large datasets.             |
| 💻 Single machine | Limited by your system’s memory and CPU. |
| 🧮 No parallelism | Does not distribute data processing.     |

---

## 🔹 **3. MapReduce Mode (Hadoop Mode)**

### ✅ **Definition**

* This is the **default mode** of Pig.
* Pig converts your Pig Latin script into **one or more MapReduce jobs**.
* Jobs are submitted to a **Hadoop cluster**, and data is read from & written to **HDFS**.

---

### ⚙️ **Command to Run**

```bash
pig -x mapreduce
```

or in Pig script:

```bash
SET execution.type mapreduce;
```

---

### 📦 **Workflow Diagram**

```
Pig Latin Script
       │
       ▼
   Pig Engine
       │
       ▼
 Converts to MapReduce Jobs
       │
       ▼
     Hadoop Cluster (HDFS)
```

---

### 🧠 **Use Cases**

* Processing **very large datasets** (GBs or TBs)
* Production data pipelines
* Integration with Hadoop ecosystem (Hive, HBase, HDFS)

---

### 🧾 **Example**

**Input file in HDFS:**

```
/user/hadoop/input/sales.csv
```

**Script: `sales_analysis.pig`**

```pig
data = LOAD '/user/hadoop/input/sales.csv' USING PigStorage(',') AS (id:int, product:chararray, price:float);
expensive = FILTER data BY price > 1000;
STORE expensive INTO '/user/hadoop/output/expensive_sales' USING PigStorage(',');
```

**Run Command:**

```bash
pig -x mapreduce sales_analysis.pig
```

**Result:**
Pig automatically creates and executes MapReduce jobs in Hadoop.

---

### 🧩 **Advantages**

| Feature                   | Description                   |
| ------------------------- | ----------------------------- |
| ⚡ Highly Scalable         | Runs on multiple nodes.       |
| 🧮 Distributed Processing | Uses Hadoop’s MapReduce.      |
| 🧰 Ecosystem Integration  | Works with Hive, HBase, HDFS. |

---

### ⚠️ **Limitations**

| Limitation            | Description                                     |
| --------------------- | ----------------------------------------------- |
| 🕒 Slower             | Job setup and MapReduce overhead.               |
| 🧱 Cluster Dependency | Requires Hadoop to be installed and configured. |
| 🧾 Complex Logs       | Debugging takes more effort.                    |

---

## 🔹 **4. Switching Between Modes**

You can easily switch between modes by:

### ✅ **Option 1: Command Line**

```bash
pig -x local script.pig
pig -x mapreduce script.pig
```

### ✅ **Option 2: Inside Script**

```pig
SET execution.type local;
-- or
SET execution.type mapreduce;
```

---

## 🔹 **5. Configuration Files**

Pig uses configuration files from:

* `pig.properties` → contains environment setup
* `mapred-site.xml`, `core-site.xml`, `hdfs-site.xml` → for Hadoop integration

You can edit these files to define default execution mode, file paths, etc.

---

## 🔹 **6. Quick Comparison Table**

| **Feature**               | **Local Mode**       | **MapReduce Mode**      |
| ------------------------- | -------------------- | ----------------------- |
| **Command**               | `pig -x local`       | `pig -x mapreduce`      |
| **Execution Engine**      | Single JVM           | Hadoop MapReduce        |
| **Input/Output Location** | Local filesystem     | HDFS                    |
| **Data Volume**           | Small                | Large                   |
| **Performance**           | Fast for small data  | Slower due to setup     |
| **Dependency**            | No Hadoop            | Hadoop cluster required |
| **Use Case**              | Testing, development | Production, big data    |

---

## 🔹 **7. Visual Summary Diagram**

```
             ┌───────────────────────────────┐
             │          Pig Script           │
             └───────────────────────────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
     ┌───────────────┐         ┌────────────────┐
     │   Local Mode  │         │ MapReduce Mode │
     └───────────────┘         └────────────────┘
        │      │                  │          │
   Local FS  JVM             Hadoop Cluster  HDFS
```

---

## ✅ **Key Takeaways**

* Pig supports **two execution modes**: **Local** and **MapReduce**.
* Use **Local Mode** for small-scale testing and debugging.
* Use **MapReduce Mode** for large-scale distributed data processing.
* Both can be run interactively (via **Grunt**) or as batch **.pig scripts**.

---

# 🧩 **HDFS Commands (Hadoop Distributed File System)**

HDFS (Hadoop Distributed File System) commands are used to **store, manage, and retrieve data** from the Hadoop file system.
These commands are similar to Linux file commands but prefixed with `hadoop fs` or `hdfs dfs`.

---

### 🧠 **Basic Syntax**

```bash
hdfs dfs -<command> <path>
# or
hadoop fs -<command> <path>
```

---

## 📁 **Commonly Used HDFS Commands**

| **Command**      | **Description**                                       | **Example**                                         |
| ---------------- | ----------------------------------------------------- | --------------------------------------------------- |
| `-mkdir`         | Creates a directory in HDFS.                          | `hdfs dfs -mkdir /user/data`                        |
| `-ls`            | Lists files and directories.                          | `hdfs dfs -ls /user`                                |
| `-put`           | Uploads files from local to HDFS.                     | `hdfs dfs -put localfile.txt /user/data/`           |
| `-get`           | Downloads files from HDFS to local.                   | `hdfs dfs -get /user/data/file.txt ./`              |
| `-cat`           | Displays contents of a file.                          | `hdfs dfs -cat /user/data/file.txt`                 |
| `-copyFromLocal` | Same as `-put`.                                       | `hdfs dfs -copyFromLocal input.txt /user/input/`    |
| `-copyToLocal`   | Same as `-get`.                                       | `hdfs dfs -copyToLocal /user/output/result.txt ./`  |
| `-rm`            | Deletes a file.                                       | `hdfs dfs -rm /user/data/file.txt`                  |
| `-rm -r`         | Deletes a directory recursively.                      | `hdfs dfs -rm -r /user/data/`                       |
| `-rmdir`         | Removes an empty directory.                           | `hdfs dfs -rmdir /user/temp`                        |
| `-du`            | Shows disk usage for files/directories.               | `hdfs dfs -du /user/data`                           |
| `-count`         | Displays number of directories, files, and bytes.     | `hdfs dfs -count /user/data`                        |
| `-moveFromLocal` | Moves a file from local to HDFS (deletes local copy). | `hdfs dfs -moveFromLocal local.txt /user/data/`     |
| `-mv`            | Moves or renames files in HDFS.                       | `hdfs dfs -mv /user/data/file1 /user/archive/file1` |
| `-cp`            | Copies files within HDFS.                             | `hdfs dfs -cp /user/data/file1 /user/backup/file1`  |
| `-test`          | Tests the existence of a path.                        | `hdfs dfs -test -e /user/data/file.txt`             |
| `-chmod`         | Changes permissions.                                  | `hdfs dfs -chmod 755 /user/data/file.txt`           |
| `-chown`         | Changes owner of a file/directory.                    | `hdfs dfs -chown user1:group1 /user/data/file.txt`  |

---

### ⚙️ **Example Workflow**

```bash
hdfs dfs -mkdir /user/yuvraj/input
hdfs dfs -put dataset.csv /user/yuvraj/input/
hdfs dfs -ls /user/yuvraj/input
hdfs dfs -cat /user/yuvraj/input/dataset.csv
```

---

### 🧾 **Note**

* The prefix `hdfs dfs` is **recommended** (newer).
* The prefix `hadoop fs` is **generic**, works across other Hadoop-compatible file systems.

---

# 🔹 **Relational Operators in Apache Pig**

### 🧠 **Introduction**

Relational operators in **Pig Latin** are used to **manipulate and transform data sets**.
They operate on **relations (tables)** — similar to SQL operations on tables.

These operators form the **core of Pig Latin scripts** for data processing.

---

## 📊 **Common Relational Operators**

| **Operator**             | **Description**                                                | **Example**                                                                                       |
| ------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **LOAD**                 | Loads data from HDFS or local file system into a Pig relation. | `A = LOAD '/user/data/student.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);` |
| **STORE**                | Stores the results of Pig relations into HDFS or local.        | `STORE A INTO '/user/output/' USING PigStorage(',');`                                             |
| **DUMP**                 | Displays relation content on the screen (stdout).              | `DUMP A;`                                                                                         |
| **FILTER**               | Selects tuples that meet a specific condition.                 | `B = FILTER A BY marks > 60;`                                                                     |
| **FOREACH ... GENERATE** | Transforms each record and produces a new relation.            | `C = FOREACH A GENERATE name, marks;`                                                             |
| **GROUP**                | Groups records having the same key.                            | `D = GROUP A BY id;`                                                                              |
| **COGROUP**              | Groups two or more relations on a common field.                | `E = COGROUP A BY id, B BY id;`                                                                   |
| **JOIN**                 | Joins two or more relations based on a common field.           | `F = JOIN A BY id, B BY id;`                                                                      |
| **CROSS**                | Computes the Cartesian product of two relations.               | `G = CROSS A, B;`                                                                                 |
| **ORDER**                | Sorts a relation based on one or more fields.                  | `H = ORDER A BY marks DESC;`                                                                      |
| **DISTINCT**             | Removes duplicate tuples.                                      | `I = DISTINCT A;`                                                                                 |
| **LIMIT**                | Restricts the number of tuples in output.                      | `J = LIMIT A 5;`                                                                                  |
| **UNION**                | Merges two or more relations with same schema.                 | `K = UNION A, B;`                                                                                 |
| **SPLIT**                | Divides a relation into two or more based on condition.        | `SPLIT A INTO B IF marks > 60, C IF marks <= 60;`                                                 |
| **DESCRIBE**             | Displays the schema of a relation.                             | `DESCRIBE A;`                                                                                     |
| **ILLUSTRATE**           | Shows step-by-step execution plan with sample data.            | `ILLUSTRATE A;`                                                                                   |
| **EXPLAIN**              | Displays the logical, physical, and MapReduce execution plan.  | `EXPLAIN A;`                                                                                      |

---

### ⚙️ **Example Pig Script**

```pig
students = LOAD '/user/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
top_students = FILTER students BY marks > 75;
sorted = ORDER top_students BY marks DESC;
DUMP sorted;
```

---

### 🧩 **Key Points**

* All operations in Pig are **lazy-evaluated** (executed only when `DUMP` or `STORE` is called).
* Each operator creates a **new relation**.
* Pig operators are **pipeline-oriented**, meaning output of one can be directly fed into the next.

---

# 🔹 **Eval Functions in Pig**

### 🧠 **What are Eval Functions?**

**Eval (Evaluation) functions** in Apache Pig are **built-in functions** used to **manipulate and transform data** within relations.
They are applied using the `FOREACH … GENERATE` statement.

Eval functions help you:

* Perform **arithmetic** and **string operations**
* **Extract**, **aggregate**, or **transform** data
* Work with **dates**, **collections**, and **bags**

---

## ⚙️ **Syntax**

```pig
relation2 = FOREACH relation1 GENERATE <Eval Function>(column_name);
```

---

## 🧩 **Types of Eval Functions**

Let’s explore them with **examples and output**.

---

### 1. **Mathematical Functions**

| **Function** | **Description**           | **Example**  | **Result** |
| ------------ | ------------------------- | ------------ | ---------- |
| `ABS(x)`     | Absolute value            | `ABS(-5)`    | `5`        |
| `ROUND(x)`   | Rounds to nearest integer | `ROUND(3.6)` | `4`        |
| `CEIL(x)`    | Next highest integer      | `CEIL(3.2)`  | `4`        |
| `FLOOR(x)`   | Next lowest integer       | `FLOOR(3.8)` | `3`        |
| `SQRT(x)`    | Square root               | `SQRT(16)`   | `4`        |
| `EXP(x)`     | Exponential value         | `EXP(2)`     | `7.389`    |
| `LOG(x)`     | Natural logarithm         | `LOG(10)`    | `2.302`    |

📘 **Example:**

```pig
numbers = LOAD '/user/data/numbers.txt' USING PigStorage(',') AS (x:double);
result = FOREACH numbers GENERATE x, SQRT(x), CEIL(x), FLOOR(x);
DUMP result;
```

---

### 2. **String Functions**

| **Function**                 | **Description**        | **Example**                          | **Result**  |
| ---------------------------- | ---------------------- | ------------------------------------ | ----------- |
| `CONCAT(a,b)`                | Joins two strings      | `CONCAT('Big','Data')`               | `BigData`   |
| `LOWER(str)`                 | Converts to lowercase  | `LOWER('HELLO')`                     | `hello`     |
| `UPPER(str)`                 | Converts to uppercase  | `UPPER('hello')`                     | `HELLO`     |
| `TRIM(str)`                  | Removes spaces         | `TRIM(' hi ')`                       | `hi`        |
| `SUBSTRING(str, start, end)` | Extracts substring     | `SUBSTRING('Hadoop',0,4)`            | `Hado`      |
| `INDEXOF(str, char, start)`  | Finds position of char | `INDEXOF('Pig', 'i', 0)`             | `1`         |
| `REPLACE(str, old, new)`     | Replace text           | `REPLACE('big data','data','world')` | `big world` |

📘 **Example:**

```pig
A = LOAD '/user/data/words.txt' USING PigStorage(',') AS (text:chararray);
B = FOREACH A GENERATE UPPER(text), SUBSTRING(text,0,3), REPLACE(text,'a','@');
DUMP B;
```

---

### 3. **Date and Time Functions**

| **Function**          | **Description**         | **Example**                                  | **Result**             |
| --------------------- | ----------------------- | -------------------------------------------- | ---------------------- |
| `ToDate(str, format)` | Converts string to date | `ToDate('2025-11-01','yyyy-MM-dd')`          | `2025-11-01T00:00:00Z` |
| `GetYear(date)`       | Extracts year           | `GetYear(ToDate('2025-11-01','yyyy-MM-dd'))` | `2025`                 |
| `GetMonth(date)`      | Extracts month          | `GetMonth(date)`                             | `11`                   |
| `GetDay(date)`        | Extracts day            | `GetDay(date)`                               | `1`                    |
| `DaysBetween(d1, d2)` | Number of days between  | `DaysBetween(d1, d2)`                        | Integer                |

📘 **Example:**

```pig
D = LOAD '/user/data/date.csv' USING PigStorage(',') AS (dt:chararray);
E = FOREACH D GENERATE ToDate(dt,'yyyy-MM-dd') AS date, GetYear(ToDate(dt,'yyyy-MM-dd')) AS year;
DUMP E;
```

---

### 4. **Bag and Tuple Functions**

| **Function**       | **Description**                      | **Example**          |
| ------------------ | ------------------------------------ | -------------------- |
| `SIZE(bag)`        | Number of tuples in a bag            | `SIZE(mybag)`        |
| `TOTUPLE(fields…)` | Creates a tuple                      | `TOTUPLE('a',1)`     |
| `TOBAG(fields…)`   | Creates a bag                        | `TOBAG('a','b','c')` |
| `FLATTEN(bag)`     | Expands a bag into individual tuples | `FLATTEN(mybag)`     |

📘 **Example:**

```pig
records = LOAD '/user/data/names.txt' USING PigStorage(',') AS (name:chararray, age:int);
grouped = GROUP records ALL;
flattened = FOREACH grouped GENERATE FLATTEN(records);
DUMP flattened;
```

---

### 5. **Conditional Functions**

| **Function**                                  | **Description**       | **Example**                                | **Output** |
| --------------------------------------------- | --------------------- | ------------------------------------------ | ---------- |
| `CASE ... WHEN`                               | Conditional branching | `CASE marks WHEN 90 THEN 'A' ELSE 'B' END` | `'A'`      |
| `DECODE(expr, value1, return1, ..., default)` | Matches and returns   | `DECODE(marks,90,'A',80,'B','C')`          | `'A'`      |
| `NULLIF(expr1, expr2)`                        | Returns NULL if equal | `NULLIF(a,b)`                              | `NULL`     |

---

### ✅ **Key Points**

* Eval functions are **used inside FOREACH...GENERATE**.
* They provide **built-in transformations** similar to SQL functions.
* You can create **UDFs (User Defined Functions)** if the built-in ones don’t meet your needs.

---

### 📊 **Example: Complete Script**

```pig
data = LOAD '/user/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
high_scorers = FILTER data BY marks > 70;
summary = FOREACH high_scorers GENERATE UPPER(name) AS NAME, ROUND(marks/10.0)*10 AS GRADE_RANGE;
DUMP summary;
```

🧾 **Output Example:**

```
(ALEX, 80)
(JOHN, 90)
(MARY, 70)
```

---

# 🔹 **Complex Data Types in Apache Pig**

### 🧠 **What Are Complex Data Types?**

Unlike SQL, where data is usually stored in flat tables, **Pig can handle nested and hierarchical data** using **complex types**.
These allow Pig to process **semi-structured** or **unstructured** data (like logs, JSON, XML).

---

## 🧩 **Three Main Complex Data Types**

| **Type**  | **Structure**               | **Description**                                                     |
| --------- | --------------------------- | ------------------------------------------------------------------- |
| **Tuple** | `(field1, field2, …)`       | An **ordered collection** of fields — similar to a row in a table.  |
| **Bag**   | `{(tuple1), (tuple2), …}`   | An **unordered collection of tuples**, like a table within a table. |
| **Map**   | `[key#value, key#value, …]` | A **key-value pair collection**, like a dictionary or JSON object.  |

---

## 🧩 **1️⃣ Tuple**

### 📘 **Definition:**

A **tuple** is a **single record** containing one or more fields.

📊 **Example:**

```
(101, 'Alice', 85)
```

Each field can be of **any data type** (int, chararray, etc.).

### 📜 **Pig Example:**

```pig
students = LOAD '/user/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
```

Each line in the file is a **tuple** like:

```
(1, 'John', 78)
(2, 'Alice', 90)
```

---

## 🧩 **2️⃣ Bag**

### 📘 **Definition:**

A **bag** is a **collection of tuples**.
Bags can be **nested**, meaning you can have **bags inside other bags**.

📊 **Example:**

```
{
  (1, 'John', 78),
  (2, 'Alice', 90),
  (3, 'Bob', 67)
}
```

### 📜 **Pig Example:**

```pig
students = LOAD '/user/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
grouped = GROUP students BY name;
DUMP grouped;
```

**Output:**

```
(John, {(1, 'John', 78)})
(Alice, {(2, 'Alice', 90)})
```

💡 **Note:**
Each group creates a **bag** of tuples that share the same key.

---

## 🧩 **3️⃣ Map**

### 📘 **Definition:**

A **map** is a **set of key-value pairs**, similar to a Python dictionary or JSON object.
Keys are **strings**, and values can be of **any data type**.

📊 **Example:**

```
[name#'John', marks#78, subject#'Math']
```

### 📜 **Pig Example:**

```pig
student_map = LOAD '/user/data/student_map.txt' USING PigStorage(',') AS (info:map[]);
```

If file contains:

```
[name#John,marks#85,subject#Math]
[name#Alice,marks#92,subject#Science]
```

You can access fields as:

```pig
result = FOREACH student_map GENERATE info#'name', info#'marks';
DUMP result;
```

**Output:**

```
(John, 85)
(Alice, 92)
```

---

## 🧩 **📊 Diagram — Complex Data Type Relationship**

```
Relation (like a table)
│
├── Tuple  → (id:int, name:chararray, marks:int)
│
├── Bag    → { (1, 'Alice', 85), (2, 'Bob', 78), (3, 'John', 90) }
│
└── Map    → [name#'Alice', marks#85, subject#'Math']
```

---

## 💻 **Combined Example**

### Input file: `school.txt`

```
1,Alice,Math:85,Science:90
2,Bob,Math:70,Science:75
```

### Pig Script:

```pig
data = LOAD 'school.txt' USING PigStorage(',') 
       AS (id:int, name:chararray, subjects:map[]);

marks = FOREACH data GENERATE 
         name, 
         subjects#'Math' AS math_marks, 
         subjects#'Science' AS science_marks;

DUMP marks;
```

**Output:**

```
(Alice, 85, 90)
(Bob, 70, 75)
```

---

## ✅ **Key Points Summary**

| Feature           | Tuple          | Bag                            | Map                 |
| ----------------- | -------------- | ------------------------------ | ------------------- |
| **Definition**    | Ordered fields | Unordered collection of tuples | Key-value pairs     |
| **Similar To**    | Row            | Table                          | Dictionary          |
| **Duplicates**    | Not allowed    | Allowed                        | Keys must be unique |
| **Access Method** | By position    | Iterative                      | By key              |

---

## 🧠 **When to Use What**

| **Scenario**                                    | **Use Data Type** |
| ----------------------------------------------- | ----------------- |
| You have single records like rows               | **Tuple**         |
| You have multiple records grouped together      | **Bag**           |
| You need to store flexible key-value attributes | **Map**           |

---

# 🐷 **Piggy Bank in Apache Pig**

---

### 🧠 **What is Piggy Bank?**

**Piggy Bank** is a **repository (library) of User Defined Functions (UDFs)** contributed by the **Apache Pig community**.
It contains **pre-written and reusable functions** that are **not part of Pig’s core**, but are very useful in data processing.

Think of it as a **plugin collection** or **toolbox** that extends Pig’s functionality.

---

### 📦 **Location and Installation**

Piggy Bank comes as part of the Pig source code distribution:

```
$PIG_HOME/contrib/piggybank/java/
```

To use it, you first **build the JAR** (if not already present):

```bash
cd $PIG_HOME/contrib/piggybank/java
ant
```

This creates:

```
$PIG_HOME/contrib/piggybank/java/piggybank.jar
```

---

### ⚙️ **Loading Piggy Bank in Your Script**

Once the JAR is ready, you can load it in your Pig script using:

```pig
REGISTER /path/to/piggybank.jar;
```

This makes all Piggy Bank functions available for use.

---

### 🧩 **Commonly Used Piggy Bank Functions**

| **Category**         | **Function Name**         | **Description**                                                  |
| -------------------- | ------------------------- | ---------------------------------------------------------------- |
| **CSV / JSON / XML** | `CSVExcelStorage()`       | Load and store CSV files with Excel-like escaping.               |
|                      | `JsonLoader()`            | Load JSON data into Pig.                                         |
|                      | `JsonStorage()`           | Store data in JSON format.                                       |
|                      | `XMLLoader()`             | Load XML data into Pig.                                          |
| **Text Processing**  | `TOKENIZE()`              | Splits a string into tokens (words).                             |
|                      | `REGEX_EXTRACT_ALL()`     | Extracts all regex matches from a string.                        |
|                      | `LOWER()` / `UPPER()`     | Converts text to lower or upper case.                            |
| **Math Functions**   | `ABS()`, `LOG()`, `EXP()` | Advanced math functions not in core Pig.                         |
| **Datetime**         | `ToDate()`                | Convert string to date.                                          |
|                      | `DaysBetween()`           | Find days between two dates.                                     |
| **Storage**          | `MultiStorage()`          | Store data in multiple directories automatically based on a key. |

---

### 📘 **Example 1 – Loading JSON Data**

**Input (`students.json`):**

```json
{"id":1, "name":"Alice", "marks":88}
{"id":2, "name":"Bob", "marks":92}
```

**Pig Script:**

```pig
REGISTER /usr/lib/pig/piggybank.jar;

students = LOAD 'students.json' USING org.apache.pig.piggybank.storage.JsonLoader('id:int, name:chararray, marks:int');

top = FILTER students BY marks > 90;
DUMP top;
```

✅ **Output:**

```
(2, Bob, 92)
```

---

### 📘 **Example 2 – Tokenizing Text**

**Input (`lines.txt`):**

```
big data analytics
hadoop pig hive
```

**Pig Script:**

```pig
REGISTER /usr/lib/pig/piggybank.jar;

lines = LOAD 'lines.txt' AS (sentence:chararray);
words = FOREACH lines GENERATE flatten(org.apache.pig.piggybank.evaluation.string.TOKENIZE(sentence)) AS word;
DUMP words;
```

✅ **Output:**

```
(big)
(data)
(analytics)
(hadoop)
(pig)
(hive)
```

---

### 📘 **Example 3 – MultiStorage**

**Purpose:** Automatically store output in separate directories based on a field value.

```pig
REGISTER /usr/lib/pig/piggybank.jar;

A = LOAD 'students.csv' USING PigStorage(',') AS (id:int, name:chararray, dept:chararray, marks:int);
STORE A INTO '/output/departments' USING org.apache.pig.piggybank.storage.MultiStorage('/output/departments', '0', ',', 10);
```

➡️ This creates directories like:

```
/output/departments/CS
/output/departments/IT
/output/departments/ME
```

Each folder stores data for that department.

---

### 🧩 **Diagram – Piggy Bank Overview**

```
          ┌─────────────────────┐
          │  Pig Latin Script   │
          └───────┬─────────────┘
                  │  (REGISTER)
                  ▼
          ┌─────────────────────┐
          │   piggybank.jar     │
          │  (Community UDFs)   │
          └───────┬─────────────┘
                  │
                  ▼
          ┌─────────────────────┐
          │  Hadoop Execution   │
          │  with Extended Fns  │
          └─────────────────────┘
```

---

### ✅ **Key Points Summary**

| **Feature**          | **Details**                                                  |
| -------------------- | ------------------------------------------------------------ |
| **Purpose**          | Extends Pig’s functionality using external UDFs              |
| **File**             | `piggybank.jar`                                              |
| **Register Command** | `REGISTER /path/to/piggybank.jar;`                           |
| **Contains**         | JSON, CSV, XML loaders, math & text UDFs, MultiStorage, etc. |
| **Location**         | `$PIG_HOME/contrib/piggybank/java/`                          |

---

### 💡 **When to Use Piggy Bank**

* When core Pig lacks a feature (like JSON parsing or regex extraction).
* For advanced file formats or text processing.
* For simplifying multi-output storage or data tokenization.

---

# **Parameter Substitution in Apache Pig**

---

#### **Introduction**

* **Parameter Substitution** in Pig allows users to **write flexible and reusable scripts** by substituting variables or parameters at runtime.
* It works similarly to variable substitution in programming languages, where placeholders are replaced with actual values during execution.

---

#### **Need for Parameter Substitution**

* Pig scripts often use **paths**, **file names**, **thresholds**, or **filter values** that may change frequently.
* Instead of modifying the script each time, you can pass these values dynamically using parameters.

---

#### **Syntax**

You define parameters in your Pig script using **`$parameter_name`**, and provide their values at runtime using:

* **Parameter file (`-param_file`)**
* **Command-line arguments (`-param`)**

---

#### **Example 1: Using `-param`**

**Script (sales.pig):**

```pig
sales_data = LOAD '$input' USING PigStorage(',') AS (id:int, product:chararray, amount:double);
filtered_sales = FILTER sales_data BY amount > $threshold;
STORE filtered_sales INTO '$output' USING PigStorage(',');
```

**Running the script:**

```bash
pig -param input=/data/sales.csv -param output=/result/high_sales -param threshold=500 sales.pig
```

✅ Pig replaces:

* `$input` → `/data/sales.csv`
* `$output` → `/result/high_sales`
* `$threshold` → `500`

---

#### **Example 2: Using `-param_file`**

**Parameter file (params.txt):**

```
input=/data/sales.csv
output=/result/high_sales
threshold=500
```

**Run the script:**

```bash
pig -param_file params.txt sales.pig
```

✅ This method is useful when you have many parameters or multiple scripts sharing common values.

---

#### **Rules for Parameter Substitution**

1. Parameters are **referenced using `$`** followed by the variable name (e.g., `$input`).
2. Parameter values **must not contain spaces** unless enclosed in quotes.
3. If a parameter is missing, Pig throws an **error** unless default values are provided.

---

#### **Default Values**

You can set default values in your script like this:

```pig
%default threshold 100
```

If the user doesn’t pass a value for `threshold`, Pig automatically uses `100`.

---

#### **Advantages**

* **Reusability:** The same script can handle different datasets or parameters.
* **Flexibility:** Easy to change input, output, or logic without editing code.
* **Maintainability:** Simplifies management of large data workflows.

---

#### **Example with Default and File Parameters**

**Script (filter_data.pig):**

```pig
%default threshold 100
data = LOAD '$input' USING PigStorage(',') AS (id:int, value:int);
filtered = FILTER data BY value > $threshold;
STORE filtered INTO '$output';
```

**Parameter file (values.txt):**

```
input=/input/data.csv
output=/output/result
```

**Run command:**

```bash
pig -param_file values.txt filter_data.pig
```

---

#### **Summary**

| **Aspect**   | **Description**                           |
| ------------ | ----------------------------------------- |
| **Purpose**  | Replaces variable placeholders at runtime |
| **Syntax**   | `$parameter_name`                         |
| **Methods**  | `-param` and `-param_file`                |
| **Defaults** | Defined using `%default`                  |
| **Benefit**  | Reusable, dynamic, and clean Pig scripts  |

---

# **Diagnostic Operators in Apache Pig**

---

#### **Introduction**

* **Diagnostic Operators** in Pig are used to **inspect, debug, and understand** data as it flows through a Pig script.
* They help developers **verify intermediate outputs**, **validate schema**, and **troubleshoot errors** before executing large jobs on Hadoop.

---

#### **Why Use Diagnostic Operators?**

* To check if **data loading** was successful.
* To **verify transformations** such as `FILTER`, `JOIN`, or `GROUP`.
* To **inspect schemas and sample outputs** before running heavy operations.
* To **debug errors** and **optimize data pipelines**.

---

#### **Common Diagnostic Operators**

| **Operator**     | **Purpose**                                                                                                     | **Example**     |
| ---------------- | --------------------------------------------------------------------------------------------------------------- | --------------- |
| **`DUMP`**       | Displays the contents of a relation on the console.                                                             | `DUMP A;`       |
| **`DESCRIBE`**   | Shows the **schema** (fields, types, and structure) of a relation.                                              | `DESCRIBE A;`   |
| **`EXPLAIN`**    | Displays the **logical, physical, and MapReduce execution plan** for debugging and optimization.                | `EXPLAIN A;`    |
| **`ILLUSTRATE`** | Simulates execution on a **sample dataset** to show data flow and transformations without running the full job. | `ILLUSTRATE A;` |

---

#### **1. DUMP**

* **Purpose:** Prints the data of a relation to the terminal.
* **Usage:**

  ```pig
  data = LOAD '/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
  DUMP data;
  ```
* **Output:**

  ```
  (1,John,85)
  (2,Alice,92)
  (3,Bob,76)
  ```
* **Note:** DUMP executes the entire job and retrieves the results — use carefully for large datasets.

---

#### **2. DESCRIBE**

* **Purpose:** Displays the **schema** of a relation.
* **Usage:**

  ```pig
  DESCRIBE data;
  ```
* **Output:**

  ```
  data: {id: int, name: chararray, marks: int}
  ```
* Helps ensure the data fields and types are correctly interpreted.

---

#### **3. EXPLAIN**

* **Purpose:** Prints the **execution plan** (logical, physical, and MapReduce stages).
* Useful for **performance tuning** and **debugging**.
* **Usage:**

  ```pig
  EXPLAIN data;
  ```
* **Output (simplified):**

  ```
  Logical Plan:
  Load -> Filter -> Store

  Physical Plan:
  Load -> Filter -> Store (MapReduce job)
  ```

---

#### **4. ILLUSTRATE**

* **Purpose:** Demonstrates how data is **transformed step-by-step** through the script using **sample records**.
* **Usage:**

  ```pig
  filtered = FILTER data BY marks > 80;
  ILLUSTRATE filtered;
  ```
* **Output (simplified):**

  ```
  Example Input:
  (1,John,85)
  (2,Alice,92)
  (3,Bob,76)

  Output of Filter:
  (1,John,85)
  (2,Alice,92)
  ```

---

#### **Comparison Table**

| **Operator**   | **Description**           | **Executes Job?**        | **Output Type**         |
| -------------- | ------------------------- | ------------------------ | ----------------------- |
| **DUMP**       | Displays relation data    | ✅ Yes                    | Actual data             |
| **DESCRIBE**   | Shows schema              | ❌ No                     | Schema structure        |
| **EXPLAIN**    | Shows execution plan      | ❌ No                     | Logical + Physical plan |
| **ILLUSTRATE** | Simulates transformations | ⚙️ Partial (sample only) | Sample data flow        |

---

#### **Best Practices**

* Use `DESCRIBE` after loading data to confirm schema.
* Use `ILLUSTRATE` before running large operations to check logic.
* Use `EXPLAIN` to understand and optimize query performance.
* Use `DUMP` only for small or sample data (to avoid huge console output).

---

#### **Example Workflow**

```pig
data = LOAD '/data/students.csv' USING PigStorage(',') AS (id:int, name:chararray, marks:int);
DESCRIBE data;
ILLUSTRATE data;
filtered = FILTER data BY marks > 80;
EXPLAIN filtered;
DUMP filtered;
```

---

#### **Summary**

| **Operator**   | **Main Use**                    | **When to Use**                |
| -------------- | ------------------------------- | ------------------------------ |
| **DUMP**       | View actual output              | For small/test datasets        |
| **DESCRIBE**   | Check schema                    | After `LOAD` or transformation |
| **EXPLAIN**    | Debug/optimize job flow         | Before execution               |
| **ILLUSTRATE** | Understand data transformations | During development/testing     |

---

# 🧠 **Word Count Example Using Apache Pig**

---

#### **📘 Introduction**

The **Word Count** problem is the **"Hello World"** of Big Data processing — it demonstrates how data flows through the Pig framework.

👉 **Goal:** Count the number of occurrences of each word in a text file.

Pig provides a **high-level scripting language (Pig Latin)** that makes such operations easier than writing Java MapReduce code manually.

---

### 🗂️ **Input File**

Let's say we have a file named `input.txt` stored in HDFS:

```
Hadoop is fast
Hadoop is powerful
Pig runs on Hadoop
```

---

### ⚙️ **Steps in Word Count Using Pig**

Below is a full **Pig Latin script** for the word count problem:

```pig
-- Step 1: Load the data from HDFS
lines = LOAD '/user/hadoop/input.txt' USING TextLoader AS (line:chararray);

-- Step 2: Split each line into words
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) AS word;

-- Step 3: Group the words
grouped = GROUP words BY word;

-- Step 4: Count the number of occurrences for each word
wordcount = FOREACH grouped GENERATE group AS word, COUNT(words) AS count;

-- Step 5: Store the result back to HDFS
STORE wordcount INTO '/user/hadoop/output_wordcount' USING PigStorage('\t');
```

---

### 🧩 **Step-by-Step Explanation**

| **Step** | **Operation**     | **Pig Latin Command** | **Purpose**                                        |
| -------- | ----------------- | --------------------- | -------------------------------------------------- |
| 1        | Load data         | `LOAD`                | Reads text data from HDFS.                         |
| 2        | Tokenize lines    | `TOKENIZE`            | Splits each line into individual words.            |
| 3        | Flatten list      | `FLATTEN`             | Expands nested collections into individual tuples. |
| 4        | Group by words    | `GROUP BY`            | Groups identical words together.                   |
| 5        | Count occurrences | `COUNT()`             | Counts how many times each word appears.           |
| 6        | Store results     | `STORE`               | Saves the final output into HDFS.                  |

---

### 📊 **Diagram — Word Count Flow in Pig**

```
+--------------------+
| Input Text (HDFS)  |
+---------+----------+
          |
          v
+--------------------+
| Load Lines         |  --> lines = LOAD ...
+--------------------+
          |
          v
+--------------------+
| Tokenize Words     |  --> TOKENIZE(line)
+--------------------+
          |
          v
+--------------------+
| Group by Word      |  --> GROUP words BY word
+--------------------+
          |
          v
+--------------------+
| Count Occurrences  |  --> COUNT(words)
+--------------------+
          |
          v
+--------------------+
| Store Output       |  --> STORE wordcount ...
+--------------------+
```

---

### 📤 **Expected Output**

After running the Pig script, the output in `/user/hadoop/output_wordcount` will be something like:

```
(Hadoop,3)
(is,2)
(fast,1)
(powerful,1)
(Pig,1)
(runs,1)
(on,1)
```

---

### 🧠 **Notes**

* **`TOKENIZE()`** — splits a string into a bag (list) of words.
* **`FLATTEN()`** — converts the bag into separate tuples (one word per row).
* **`COUNT()`** — returns the number of elements in each group.
* **`PigStorage('\t')`** — stores output as tab-separated values.

---

### 🧩 **Optional Optimization Using Combiner**

Pig automatically uses the **combiner function** in backend MapReduce during aggregation (like COUNT, SUM), improving performance by partially reducing data before sending it to reducers.

---

### 💡 **Example Using Local Mode**

You can test it locally before using Hadoop:

```bash
pig -x local wordcount.pig
```

Then check output in:

```
/user/hadoop/output_wordcount
```

---

### ✅ **Summary Table**

| **Feature**    | **Description**                                          |
| -------------- | -------------------------------------------------------- |
| Input Data     | Text file (`input.txt`)                                  |
| Output         | Word counts per unique word                              |
| Tools          | Pig Latin, Hadoop, HDFS                                  |
| Execution Mode | Local or MapReduce                                       |
| Key Functions  | `LOAD`, `TOKENIZE`, `FLATTEN`, `GROUP`, `COUNT`, `STORE` |

---

### 🐖 **Pig at Yahoo! — The Birthplace and Real-World Use of Apache Pig**

---

#### 🏁 **Introduction**

* **Apache Pig** was originally **developed at Yahoo!** around **2006** to simplify **data processing on Hadoop**.
* Yahoo! engineers realized that **writing Java MapReduce programs** for every data analysis task was **slow, repetitive, and complex**, so they created **Pig**, a **high-level data flow language** (Pig Latin) to make big data analytics **simpler and faster**.

---

# ⚙️ **Why Yahoo! Needed Pig**

#### **Problem Before Pig:**

* Yahoo! had **thousands of Hadoop jobs** running daily (for web indexing, ad optimization, user behavior analytics, etc.).
* Writing MapReduce code in Java was:

  * **Time-consuming**
  * **Hard to debug**
  * **Hard to reuse**
  * **Error-prone**
* Data analysts needed a way to **express transformations and aggregations** without deep programming knowledge.

#### **Solution:**

* **Pig Latin** was designed — a **scripting language** that translates into **MapReduce jobs** internally.
* This allowed analysts to:

  * Write data analysis **scripts instead of Java code**.
  * Execute them on **Hadoop clusters** with minimal coding effort.

---

### 🏗️ **Architecture of Yahoo!’s Pig Usage**

```
+---------------------------------------------------+
|                    Yahoo! Users                   |
| (Data Scientists, Analysts, Engineers)            |
+---------------------------------------------------+
                     |
                     v
+--------------------+------------------------------+
|                Pig Latin Scripts                  |
|  (High-Level Data Flow Language)                  |
+--------------------+------------------------------+
                     |
                     v
+---------------------------------------------------+
|         Pig Engine (Parser + Optimizer)           |
|   → Converts scripts into MapReduce Jobs          |
+---------------------------------------------------+
                     |
                     v
+---------------------------------------------------+
|                 Hadoop Cluster                    |
|   (HDFS for Storage + MapReduce for Execution)    |
+---------------------------------------------------+
```

---

### 💡 **Use Cases of Pig at Yahoo!**

| **Use Case**               | **Description**                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| **Ad Targeting**           | Processing terabytes of clickstream data to understand user behavior and optimize advertisements. |
| **Web Indexing**           | Analyzing crawled web pages to build Yahoo’s search index faster.                                 |
| **User Behavior Analysis** | Tracking user actions to improve recommendation systems and personalized experiences.             |
| **Spam Filtering**         | Detecting spam activity by analyzing large mail datasets.                                         |
| **Log Analysis**           | Parsing and summarizing massive server log files.                                                 |

---

### 📈 **Performance Gains at Yahoo!**

| **Task**                | **Java MapReduce Lines of Code** | **Pig Latin Lines of Code** | **Development Time Reduction** |
| ----------------------- | -------------------------------- | --------------------------- | ------------------------------ |
| Log Parsing Job         | ~1,200 LOC                       | ~60 LOC                     | 95%                            |
| Clickstream Analysis    | ~900 LOC                         | ~50 LOC                     | 94%                            |
| Ad Conversion Analytics | ~1,500 LOC                       | ~70 LOC                     | 96%                            |

✅ **Result:** Faster development, easier debugging, and more experimentation with data models.

---

### 🧠 **Key Contributions by Yahoo!**

| **Contribution**            | **Description**                                                                 |
| --------------------------- | ------------------------------------------------------------------------------- |
| **Initial Development**     | Pig was built internally and later **donated to Apache Foundation** in 2007.    |
| **Extensive Testing**       | Used on **multi-petabyte clusters**, ensuring scalability and reliability.      |
| **User Community**          | Yahoo! engineers were core contributors to the Pig open-source ecosystem.       |
| **Integration with Hadoop** | Pig became a standard tool in Yahoo’s **Hadoop-based data analytics pipeline**. |

---

### 🚀 **Scale of Pig at Yahoo!**

* Yahoo! had **over 40,000 nodes** running Hadoop clusters.
* Pig processed **terabytes to petabytes of data daily**.
* Thousands of Pig scripts executed each day across **different business units**.

---

### 💬 **Quote from Yahoo! Engineer**

> “Pig allows us to **think in terms of data flows**, not Java code.
> It turned weeks of development into hours of scripting.”
> — *Christopher Olston, Yahoo! Research*

---

### 🔍 **Pig’s Legacy After Yahoo!**

Even after Yahoo!, **Pig became a standard tool** across organizations using Hadoop, such as:

* LinkedIn
* Twitter
* eBay
* Spotify

It influenced modern data frameworks like:

* **Apache Spark (DataFrame API)**
* **Hive (Declarative SQL-like approach)**
* **Flink and Beam (Dataflow models)**

---

### 🧩 **Summary Table**

| **Aspect**        | **Details**                           |
| ----------------- | ------------------------------------- |
| **Developed by**  | Yahoo! Research                       |
| **Year**          | 2006–2007                             |
| **Purpose**       | Simplify Hadoop data processing       |
| **Language Used** | Pig Latin                             |
| **Replaced**      | Manual MapReduce Java programs        |
| **Donated To**    | Apache Software Foundation (2007)     |
| **Adopted By**    | Yahoo!, LinkedIn, Twitter, eBay, etc. |

---

### 🖼️ **Visual Summary**

```
Yahoo! Data (Logs, Clicks, Emails)
         |
         v
+-----------------------+
| Pig Latin Scripts     |
| (Data Transformation) |
+-----------------------+
         |
         v
+-----------------------+
| Pig Execution Engine  |
| Converts to MapReduce |
+-----------------------+
         |
         v
+-----------------------+
| Hadoop Cluster (HDFS) |
| Stores & Processes    |
+-----------------------+
```

---

# 🐖🐝 **Pig vs Hive — A Complete Comparison**

---

#### 🧠 **Introduction**

Both **Apache Pig** and **Apache Hive** are high-level frameworks built on top of **Hadoop** to simplify **big data analysis** — but they serve **different user groups** and **different purposes**.

| **Aspect**               | **Pig**                | **Hive**                    |
| ------------------------ | ---------------------- | --------------------------- |
| **Created By**           | Yahoo!                 | Facebook                    |
| **Language**             | Pig Latin              | HiveQL (SQL-like)           |
| **Users**                | Programmers            | Analysts                    |
| **Processing Model**     | Data Flow (Procedural) | Query-based (Declarative)   |
| **Underlying Execution** | MapReduce              | MapReduce / Tez / Spark     |
| **Primary Use**          | ETL, Data Pipelines    | Data Warehousing, Reporting |

---

### ⚙️ **Concept Overview**

#### 🐖 **Apache Pig**

* A **data flow scripting language** built to handle **large-scale data transformation**.
* Users write **Pig Latin** scripts describing how data should flow from input → transformation → output.
* Suitable for **programmers** who are comfortable with **step-by-step procedural logic**.

#### 🐝 **Apache Hive**

* A **data warehouse infrastructure** that provides a **SQL-like interface** (HiveQL) to query data stored in Hadoop.
* Users write queries similar to SQL, and Hive converts them into **MapReduce jobs** internally.
* Suitable for **analysts** or **data scientists** with **SQL knowledge**.

---

### ⚖️ **Detailed Comparison**

| **Feature**                       | **Apache Pig**                     | **Apache Hive**                               |
| --------------------------------- | ---------------------------------- | --------------------------------------------- |
| **Type**                          | Data Flow Language                 | Query Language                                |
| **Language Used**                 | Pig Latin (procedural)             | HiveQL (declarative SQL-like)                 |
| **Developed By**                  | Yahoo!                             | Facebook                                      |
| **Use Case**                      | Data cleaning, ETL, transformation | Data summarization, ad-hoc queries, reporting |
| **User Type**                     | Programmers                        | Analysts                                      |
| **Execution Engine**              | MapReduce                          | MapReduce / Tez / Spark                       |
| **Data Model**                    | Sequence of data transformations   | Tables with rows and columns                  |
| **Schema**                        | Schema on read (can be flexible)   | Schema on read (structured schema)            |
| **Ease of Use**                   | Requires scripting                 | Easier for SQL users                          |
| **UDF Support**                   | Supports Java, Python, etc.        | Supports Java, Python, etc.                   |
| **Joins and Grouping**            | Supported with custom syntax       | SQL-style joins and grouping                  |
| **Data Loading**                  | `LOAD` statement                   | `CREATE TABLE` and `LOAD DATA`                |
| **Output**                        | Files in HDFS                      | Tables (managed/external)                     |
| **Optimization**                  | Limited, mostly manual             | Cost-based optimizer in Hive                  |
| **Real-Time Queries**             | Not supported                      | Supported in Hive LLAP                        |
| **UDFs (User Defined Functions)** | Custom functions easily added      | UDFs supported but slightly more complex      |
| **Data Storage**                  | HDFS files (any format)            | Hive tables (structured)                      |
| **Typical File Formats**          | Text, JSON, Avro, Parquet          | ORC, Parquet, RCFile                          |
| **Interactive Mode**              | Yes (`Grunt shell`)                | Yes (`Hive shell`, Beeline)                   |

---

### 🧩 **Programming Approach Comparison**

#### 🔸 Pig (Procedural / Data Flow)

You specify **how** data should be processed — step by step.

```pig
data = LOAD '/data/sales.csv' USING PigStorage(',') AS (product, amount);
grouped = GROUP data BY product;
sum_data = FOREACH grouped GENERATE group, SUM(data.amount);
DUMP sum_data;
```

#### 🔹 Hive (Declarative / SQL-like)

You specify **what** result you want — not how to get it.

```sql
SELECT product, SUM(amount)
FROM sales
GROUP BY product;
```

---

### 🧠 **When to Use Which**

| **Scenario**                       | **Preferred Tool** | **Reason**                                          |
| ---------------------------------- | ------------------ | --------------------------------------------------- |
| **ETL and Data Preparation**       | Pig                | Handles complex transformations, unstructured data  |
| **Business Reporting and BI**      | Hive               | Easy SQL-like queries                               |
| **Iterative Data Flow Jobs**       | Pig                | Step-wise control over processing                   |
| **Interactive Querying**           | Hive               | Hive supports fast query engines (LLAP, Tez)        |
| **Complex Joins and Aggregations** | Hive               | SQL-like syntax is simpler                          |
| **Scripting and Automation**       | Pig                | Better for scripting pipelines                      |
| **Data Science Integration**       | Hive               | Integrates easily with tools like Tableau, Power BI |

---

### 🏗️ **Diagram — Pig vs Hive Workflow**

```
          +------------------+                      +-----------------+
          |    Pig Latin     |                      |     HiveQL      |
          +---------+--------+                      +--------+--------+
                    |                                        |
                    v                                        v
          +------------------+                      +-----------------+
          | Pig Interpreter  |                      | Hive Compiler   |
          | (Generates MR)   |                      | (Generates MR)  |
          +------------------+                      +-----------------+
                    |                                        |
                    v                                        v
          +------------------+                      +-----------------+
          | Hadoop MapReduce |   <---- Common ---->  | Hadoop MapReduce |
          +------------------+                      +-----------------+
```

---

### 📊 **Performance and Flexibility**

| **Aspect**                       | **Pig**                             | **Hive**                                 |
| -------------------------------- | ----------------------------------- | ---------------------------------------- |
| **Performance (Raw Processing)** | Faster for raw data transformations | Optimized for queries, slower for ETL    |
| **Flexibility**                  | High — supports complex logic       | Moderate — SQL syntax limits flexibility |
| **Ease of Learning**             | Medium (custom syntax)              | Easy (SQL-like syntax)                   |

---

### 🧩 **Example Use Cases**

| **Company / Project** | **Pig Usage**             | **Hive Usage**                           |
| --------------------- | ------------------------- | ---------------------------------------- |
| **Yahoo!**            | Clickstream analysis, ETL | Reporting dashboard                      |
| **Facebook**          | (Initially not used)      | Developed and used Hive for ad analytics |
| **Twitter**           | Log processing            | Trend analytics                          |
| **eBay**              | Data transformation jobs  | SQL-style data warehouse                 |

---

### 🧠 **Quick Summary Table**

| **Category** | **Pig**            | **Hive**                  |
| ------------ | ------------------ | ------------------------- |
| Language     | Pig Latin          | HiveQL                    |
| Nature       | Procedural         | Declarative               |
| Best For     | ETL, data pipeline | Data warehouse, analytics |
| Data Type    | Semi/unstructured  | Structured                |
| Users        | Programmers        | Analysts                  |
| Developed By | Yahoo!             | Facebook                  |

---

### 🧾 **Conclusion**

* Use **Pig** when you need **fine-grained data flow control** and handle **semi-structured/unstructured** data.
* Use **Hive** when you need **easy SQL-based querying** and **data summarization**.
* Both tools **complement each other** and can be **used together** in the same Hadoop ecosystem — Pig for **data preparation**, Hive for **analysis and reporting**.

---
