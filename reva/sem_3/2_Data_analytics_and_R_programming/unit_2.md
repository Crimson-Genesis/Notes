# Unit - 2

## introduction To Technology Landscape and Maperduce Programming
- NoSQL
- Comparison of SQL and NoSQL
- Hadoop
- RDBMS Versus Hadoop
- Distributed Computing Challenges
- Hadoop Overview
- Hadoop Distributed File System
- Processing Data with Hadoop
- Managing Resources and Applications with Hadoop YARN
- Interacting with Hadoop Ecosystem

- MapRdeuce
- Mapper - Reducer - Combiner - Partitioner - Searching - Sorting - Compression

---
---

# 🧩 **NoSQL (Not Only SQL)**

### 🧠 **Definition**

**NoSQL** is a type of **database management system** that provides a **mechanism for storage and retrieval of data that is not modeled in traditional tabular (row-column) format**.
It is designed to handle:

* **Unstructured, semi-structured, or hierarchical data**
* **Large-scale distributed data**
* **High-velocity (fast-changing) information**

> 💡 “NoSQL” means *Not Only SQL* — it supports non-relational data storage, but may still use some SQL-like queries.

---

## 🏗️ **Why NoSQL?**

Traditional relational databases (RDBMS) struggle with **big data** because:

* They require a **fixed schema** (rigid structure).
* They scale **vertically** (by increasing hardware power).
* They are not ideal for **real-time web, IoT, or social media data**.

**NoSQL** databases solve this by being:

* **Schema-less**
* **Horizontally scalable**
* **High-performance** across distributed systems

---

## 🧱 **Types of NoSQL Databases**

| **Type**                   | **Data Model**                | **Description**                                                                                           | **Examples**          |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------- |
| **1. Key–Value Store**     | Key–value pairs               | Each record has a unique key and a value (like a dictionary). Best for caching and session data.          | Redis, Riak, DynamoDB |
| **2. Document Store**      | JSON, BSON, XML               | Stores documents that can have flexible structure. Great for content management, catalogs, user profiles. | MongoDB, CouchDB      |
| **3. Column-Family Store** | Columns grouped into families | Data stored in columns rather than rows. Good for analytics and time-series data.                         | Cassandra, HBase      |
| **4. Graph Database**      | Nodes and edges               | Designed for relationships and networks (social networks, recommendations).                               | Neo4j, OrientDB       |

---

### 📘 **Diagram — Types of NoSQL Databases**

```
                   ┌─────────────────────────────────┐
                   │           NoSQL DBs             │
                   └─────────────────────────────────┘
                               │
     ┌────────────┬────────────┬──────────────┬──────────────┐
     │            │            │              │              │
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Key-Value│ │ Document │ │ Column   │ │ Graph    │
│   Store  │ │   Store  │ │   Store  │ │ Database │
└──────────┘ └──────────┘ └──────────┘ └──────────┘
     │            │            │              │
 Redis,      MongoDB,     Cassandra,       Neo4j,
 DynamoDB    CouchDB      HBase            OrientDB
```

---

## ⚡ **Advantages of NoSQL**

* **Scalable:** Can add more servers easily (horizontal scaling).
* **Flexible Schema:** Supports changing data structures without altering schema.
* **High Performance:** Optimized for fast reads/writes.
* **Handles Big Data:** Works efficiently with large, distributed datasets.
* **Supports Different Data Types:** JSON, key-value, documents, graphs, etc.

---

## ⚠️ **Limitations**

* **No standard query language** (though many use SQL-like syntax).
* **Limited ACID transactions** (some only support eventual consistency).
* **Complex for beginners** to design data models.

---

## 💻 **Example — MongoDB (Document Store)**

```js
// Insert document
db.students.insertOne({
  name: "Yuvraj",
  course: "MCA",
  marks: 92,
  skills: ["Python", "Big Data"]
});

// Query document
db.students.find({ marks: { $gt: 80 } });
```

**Explanation:**

* `insertOne()` → inserts a JSON-like document
* `find()` → retrieves documents matching condition (`marks > 80`)

---

## 🚀 **When to Use NoSQL**

* Handling **large-scale data** with **high velocity**
* Storing **unstructured data** (social media, IoT, documents)
* When **flexibility and performance** are more important than strict consistency

---

# 🆚 **Comparison of SQL and NoSQL**

---

## 🧠 **Introduction**

Both **SQL** (Structured Query Language) and **NoSQL** databases are used to store and retrieve data,
but they differ **in how data is structured, stored, scaled, and queried**.

---

## 📋 **Comparison Table: SQL vs NoSQL**

| **Feature**         | **SQL (Relational Database)**                                    | **NoSQL (Non-Relational Database)**                                       |
| ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Full Form**       | Structured Query Language                                        | Not Only SQL                                                              |
| **Data Model**      | Tabular (Rows and Columns)                                       | Non-tabular (Key–Value, Document, Column, Graph)                          |
| **Schema**          | Fixed schema (predefined structure)                              | Dynamic / Schema-less                                                     |
| **Scalability**     | Vertical (add more CPU/RAM)                                      | Horizontal (add more servers/nodes)                                       |
| **Storage**         | Centralized storage                                              | Distributed storage                                                       |
| **Transactions**    | Follows **ACID** (Atomicity, Consistency, Isolation, Durability) | Follows **BASE** (Basically Available, Soft state, Eventually consistent) |
| **Query Language**  | SQL (standardized and declarative)                               | No standard — depends on database (MongoDB Query, CQL, Gremlin, etc.)     |
| **Joins**           | Supports joins between multiple tables                           | Usually does not support joins (denormalized data)                        |
| **Best Suited For** | Structured data, complex queries, transactional systems          | Unstructured or semi-structured data, flexible and large-scale systems    |
| **Examples**        | MySQL, PostgreSQL, Oracle, MS SQL Server                         | MongoDB, Cassandra, CouchDB, HBase, Neo4j                                 |
| **Use Cases**       | Banking, ERP, Inventory, CRM                                     | Social media, IoT, Big Data analytics, real-time apps                     |

---

## 🧩 **ACID vs BASE Concept**

| **Property** | **SQL (ACID)**                               | **NoSQL (BASE)**                                            |
| ------------ | -------------------------------------------- | ----------------------------------------------------------- |
| **A**        | Atomicity – all-or-nothing transactions      | Basically Available – system guarantees availability        |
| **C**        | Consistency – data remains valid             | Soft state – state may change over time                     |
| **I**        | Isolation – transactions occur independently | Eventually consistent – data becomes consistent after delay |
| **D**        | Durability – data survives failures          | —                                                           |

📘 **Explanation:**

* SQL ensures **data correctness**.
* NoSQL ensures **speed and scalability** with **eventual consistency**.

---

## 🧱 **Diagram — SQL vs NoSQL Architecture**

```
      SQL (RDBMS)                        NoSQL (Distributed)

   ┌──────────────┐                ┌──────────────┐   ┌──────────────┐
   │  Application │                │   Node 1     │   │   Node 2     │
   └──────┬───────┘                └──────┬───────┘   └──────┬───────┘
          │                                  │               │
   ┌──────▼──────┐                     ┌─────▼──────┐  ┌─────▼──────┐
   │  SQL Server │  (Centralized)      │  NoSQL DB  │  │  NoSQL DB  │  (Distributed)
   └─────────────┘                     └────────────┘  └────────────┘
```

---

## 💻 **Code Comparison**

### 🔹 SQL Example (MySQL)

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(20),
  marks INT
);

INSERT INTO students VALUES (1, 'Yuvraj', 'MCA', 95);

SELECT * FROM students WHERE marks > 80;
```

### 🔹 NoSQL Example (MongoDB)

```js
db.students.insertOne({
  id: 1,
  name: "Yuvraj",
  course: "MCA",
  marks: 95
});

db.students.find({ marks: { $gt: 80 } });
```

**👉 Difference:**

* SQL: Structured table with schema
* NoSQL: Document with flexible fields

---

## ⚙️ **When to Use Which?**

| **Use SQL When**                                           | **Use NoSQL When**                                                        |
| ---------------------------------------------------------- | ------------------------------------------------------------------------- |
| Data is **structured and consistent**                      | Data is **unstructured or semi-structured**                               |
| You need **complex joins and transactions**                | You need **fast access and scalability**                                  |
| Application is **business-critical** (banking, accounting) | Application is **data-heavy and evolving** (social media, IoT, analytics) |

---

## 📌 **Summary**

* SQL = **Structure, Reliability, Transactions**
* NoSQL = **Flexibility, Scalability, Speed**

---

# 🐘 **Hadoop — Introduction**

---

## 🧠 **Definition**

**Hadoop** is an **open-source framework** developed by the **Apache Software Foundation** that allows for **distributed storage** and **parallel processing** of **large datasets** across clusters of computers.

> 💡 Simply put: Hadoop helps store and process *huge amounts of data* using many inexpensive machines working together.

---

## ⚙️ **Core Idea**

Instead of using one powerful computer, Hadoop **divides** big data into smaller parts and **processes them in parallel** across many cheap computers (nodes).

---

## 🧩 **Main Components of Hadoop Ecosystem**

| **Component**                                 | **Description**                                                                                                                | **Analogy**                                                                          |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **1. HDFS (Hadoop Distributed File System)**  | A distributed file system that stores large data files by splitting them into blocks and spreading them across multiple nodes. | Like splitting a big movie file into parts and storing them on different USB drives. |
| **2. YARN (Yet Another Resource Negotiator)** | Handles resource management and job scheduling across the cluster.                                                             | Like a traffic controller that assigns tasks to available workers.                   |
| **3. MapReduce**                              | A programming model for processing data in parallel across nodes.                                                              | Like dividing work among friends — each works on a part and combines results.        |
| **4. Hadoop Common (Libraries)**              | Set of Java-based utilities and libraries that support the other modules.                                                      | Like the shared tools everyone uses in a workshop.                                   |

---

## 🧱 **Hadoop Architecture Diagram**

```
                 ┌───────────────────────────────┐
                 │       Hadoop Cluster          │
                 └───────────────────────────────┘
                               │
        ┌──────────────────────┴──────────────────────┐
        │                                             │
 ┌─────────────┐                              ┌─────────────┐
 │ NameNode    │─── Manages metadata ───────▶ │ DataNodes   │
 │ (Master)    │                              │ (Slaves)    │
 └─────────────┘                              └─────────────┘
        │                                             │
        │        YARN ResourceManager                 │
        │────────────────────────────────────────────▶│
        │        (Job scheduling + Monitoring)        │
        │                                             │
        │                MapReduce Jobs               │
        └────────────────────────────────────────────▶│
```

**Explanation:**

* **NameNode**: Stores metadata (where data blocks are stored).
* **DataNode**: Actually stores the data blocks.
* **YARN**: Manages job scheduling and system resources.
* **MapReduce**: Executes data processing tasks in parallel.

---

## 🔍 **How Hadoop Works (Step-by-Step)**

1. **Data Input** – Large dataset is divided into smaller chunks (blocks of 128 MB or 256 MB).
2. **Storage in HDFS** – These blocks are stored across multiple DataNodes (with replication).
3. **Processing (MapReduce)** – Each node processes its local data (Map phase).
4. **Shuffling & Reducing** – Results are combined and summarized (Reduce phase).
5. **Output** – Final processed data is written back to HDFS.

---

## 📦 **Example**

Let’s say we want to **count how many times each word appears** in a huge text file.

* **Map Phase:**
  Split data → Map function counts words in each chunk.

* **Reduce Phase:**
  Combine results from all mappers → Output final counts.

📘 Example in pseudo-code:

```java
map(String key, String value):
    for each word in value:
        emit(word, 1);

reduce(String key, Iterator values):
    int sum = 0;
    for each v in values:
        sum += v;
    emit(key, sum);
```

---

## ⚡ **Key Features of Hadoop**

| **Feature**        | **Description**                                                           |
| ------------------ | ------------------------------------------------------------------------- |
| **Scalable**       | Can handle petabytes of data by adding more nodes.                        |
| **Fault-Tolerant** | Data is replicated (default: 3 copies) to avoid data loss.                |
| **Cost-Effective** | Runs on commodity (cheap) hardware.                                       |
| **Flexible**       | Can process any data type — structured, unstructured, or semi-structured. |
| **Open Source**    | Free and maintained by Apache Foundation.                                 |

---

## 🚀 **Advantages**

* Handles **massive volumes** of data efficiently
* **Parallel processing** improves speed
* **High availability** even when nodes fail
* Integrates with tools like **Hive, Pig, Spark**

---

## ⚠️ **Limitations**

* **High latency** (batch-oriented, not real-time)
* **Complex setup** and maintenance
* **Not ideal for small datasets**

---

## 🌐 **Real-World Use Cases**

* **Facebook:** Logs and user activity analysis
* **Yahoo!:** Search index building (original creator)
* **Netflix:** Recommendation systems
* **Government agencies:** Large-scale data analytics

---

## 🧭 **Summary Diagram**

```
         ┌──────────────┐
         │   HDFS        │  ← Storage Layer
         └──────────────┘
                 │
         ┌──────────────┐
         │   YARN        │  ← Resource Management Layer
         └──────────────┘
                 │
         ┌──────────────┐
         │ MapReduce     │  ← Processing Layer
         └──────────────┘
                 │
         ┌──────────────┐
         │  Tools: Hive, │
         │  Pig, Spark   │  ← Ecosystem
         └──────────────┘
```

---

# 🆚 **RDBMS vs Hadoop**

---

## 🧠 **1. Concept Overview**

| **Term**                                          | **Definition**                                                                                                                                                |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RDBMS (Relational Database Management System)** | A database system based on relational (table-based) data model using SQL. Stores structured data in fixed schemas.                                            |
| **Hadoop**                                        | An open-source distributed framework for storing and processing massive datasets (structured, semi-structured, or unstructured) across clusters of computers. |

---

## ⚙️ **2. Core Difference Table**

| **Feature**           | **RDBMS**                                                   | **Hadoop**                                                                             |
| --------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Data Type**         | Structured data only (tables, rows, columns).               | Structured, semi-structured, and unstructured data (text, images, logs, videos, etc.). |
| **Storage Mechanism** | Centralized database on a single or few servers.            | Distributed storage system (HDFS) across multiple nodes.                               |
| **Schema**            | Schema-on-write (data must fit the table before inserting). | Schema-on-read (structure applied when reading).                                       |
| **Processing**        | Uses SQL queries.                                           | Uses MapReduce, Spark, or other distributed engines.                                   |
| **Scalability**       | Scales **vertically** (upgrade server CPU/RAM).             | Scales **horizontally** (add more nodes).                                              |
| **Fault Tolerance**   | Limited — single point of failure possible.                 | High — automatic data replication across nodes.                                        |
| **Cost**              | Expensive (licensed, high-end hardware).                    | Cost-effective (open-source + commodity hardware).                                     |
| **Speed**             | Faster for small datasets.                                  | Optimized for very large datasets (parallel processing).                               |
| **Real-time Support** | Designed for real-time transaction systems.                 | Mostly batch-oriented (though modern tools like Spark add real-time ability).          |
| **Examples**          | MySQL, Oracle, PostgreSQL, MS SQL Server                    | Hadoop (HDFS + YARN + MapReduce), Spark, Hive, Pig                                     |

---

## 🏗️ **3. Architectural Difference Diagram**

```
          ┌─────────────────────────────┐
          │         RDBMS System        │
          └─────────────────────────────┘
                       │
                       ▼
          ┌─────────────────────────────┐
          │ Centralized Database Server │
          │ (Single or limited nodes)   │
          └─────────────────────────────┘
                       │
             ┌─────────┴─────────┐
             │ SQL Query Engine  │
             └───────────────────┘


                🆚  Versus


          ┌──────────────────────────────┐
          │           Hadoop             │
          └──────────────────────────────┘
                       │
     ┌─────────────────┴─────────────────┐
     │             HDFS                  │
     │  (Distributed Storage Layer)      │
     └───────────────────────────────────┘
                       │
     ┌─────────────────┴─────────────────┐
     │             YARN                  │
     │ (Resource Management Layer)       │
     └───────────────────────────────────┘
                       │
     ┌─────────────────┴─────────────────┐
     │           MapReduce               │
     │ (Parallel Processing Engine)      │
     └───────────────────────────────────┘
```

---

## 🔍 **4. Detailed Explanation**

### 🧱 **RDBMS:**

* Uses **structured schema** → Every record must follow the same table design.
* Performs best when dealing with **moderate, consistent, transactional** data.
* Supports **ACID properties** → Ensures accurate transactions.
* Example use cases:

  * Banking systems
  * Employee management systems
  * Inventory and ERP software

### 🐘 **Hadoop:**

* Can store **any type of data** (logs, audio, video, text, etc.).
* Designed for **Big Data analytics**, not small transactions.
* Provides **fault tolerance** via **data replication** (usually 3 copies).
* Uses **MapReduce** for parallel processing of huge datasets.
* Example use cases:

  * Analyzing social media data
  * Processing IoT or sensor data
  * Recommender systems (Netflix, Amazon)

---

## 🧩 **5. Example Scenario**

| **Scenario**                                           | **Best Option** |
| ------------------------------------------------------ | --------------- |
| Storing customer transaction data for a bank           | ✅ **RDBMS**     |
| Analyzing terabytes of clickstream logs from a website | ✅ **Hadoop**    |
| Real-time billing system                               | ✅ **RDBMS**     |
| Batch processing of social media trends                | ✅ **Hadoop**    |

---

## ⚡ **6. Summary**

| **Aspect**    | **RDBMS**    | **Hadoop**  |
| ------------- | ------------ | ----------- |
| Transactional | ✅            | ❌           |
| Analytical    | ⚠️ Limited   | ✅ Excellent |
| Real-time     | ✅            | ⚠️ Partial  |
| Cost          | 💰 High      | 💸 Low      |
| Data Size     | Small–Medium | Very Large  |

---

## 📘 **In Simple Words**

> **RDBMS = System of Record (for transactions)**
> **Hadoop = System of Analysis (for massive data analytics)**

---

## 🧭 **Summary Diagram: Relationship**

```
RDBMS  →  Stores business transactions (OLTP)
Hadoop →  Analyzes massive raw data (OLAP)
```

They can also **work together**:

* Data moves from RDBMS → Hadoop (ETL process)
* Hadoop analyzes → sends insights back to RDBMS dashboards

---

# 🧠 **Distributed Computing Challenges**

---

### 🌍 **Introduction**

Distributed computing refers to a system where **multiple computers (nodes)** work together to perform tasks as a **single cohesive unit**.
Examples include **Hadoop clusters**, **Google File System (GFS)**, and **Apache Spark environments**.

While distributed systems provide **scalability**, **fault tolerance**, and **high availability**, they also introduce **several challenges** due to the **complexity of coordination, synchronization, and communication** across nodes.

---

## ⚙️ **Major Challenges in Distributed Computing**

---

### 1. 🕸️ **Network Issues**

* **Description:** Nodes in a distributed system communicate via a network (LAN/WAN).
  Network latency, packet loss, and varying bandwidth cause performance degradation.
* **Problems:**

  * Delays in data transfer between nodes.
  * Network congestion leading to timeout or dropped messages.
  * Uneven data processing speeds across nodes.
* **Example:** In Hadoop, if one node is slow due to poor network, the whole MapReduce job may slow down.

---

### 2. 🧩 **Data Distribution and Partitioning**

* **Description:** Distributing large data sets efficiently among multiple nodes is complex.
* **Problems:**

  * Uneven partitioning → some nodes get too much data while others stay idle.
  * Maintaining data **locality** (keeping computation close to data) is difficult.
* **Example:** Hadoop uses **HDFS** to split data into blocks and replicate them, but ensuring **balanced workloads** remains a challenge.

---

### 3. 🔄 **Consistency and Synchronization**

* **Description:** Ensuring all nodes have the same data view at any given time.
* **Problems:**

  * Concurrent writes or updates can cause **inconsistent data**.
  * **Clock synchronization** issues (since each node has its own clock).
* **Example:** CAP Theorem states that in distributed systems, you can only guarantee **two** of three:

  * **Consistency**, **Availability**, **Partition Tolerance**.

---

### 4. ⚡ **Fault Tolerance and Recovery**

* **Description:** Nodes can fail unexpectedly, and the system must recover without losing data.
* **Problems:**

  * Detecting failed nodes quickly.
  * Redistributing their tasks to other nodes.
  * Recovering lost data from replicas.
* **Example:** Hadoop’s **NameNode** maintains metadata — if it fails, the whole cluster may go down unless High Availability (HA) is configured.

---

### 5. 🔐 **Security Challenges**

* **Description:** Data is transferred and stored across many machines — increasing security risks.
* **Problems:**

  * Unauthorized access to nodes or data.
  * Data leakage during transmission.
  * Implementing authentication and encryption across the network.
* **Example:** Hadoop provides **Kerberos authentication**, but configuring it correctly is complex.

---

### 6. 🧠 **Programming Complexity**

* **Description:** Writing parallel and distributed algorithms is more complex than traditional sequential programs.
* **Problems:**

  * Managing concurrency and synchronization.
  * Handling communication and data sharing between nodes.
  * Debugging distributed code is harder since failures can happen anywhere.
* **Example:** MapReduce simplifies this with `map()` and `reduce()` functions, but designing jobs efficiently still requires deep understanding.

---

### 7. ⚖️ **Scalability and Load Balancing**

* **Description:** The system must handle growth in data and users efficiently.
* **Problems:**

  * Uneven load among nodes.
  * Adding or removing nodes dynamically without downtime.
* **Example:** Hadoop and Spark use resource managers (like YARN) to distribute load across nodes.

---

### 8. 🧮 **Resource Management**

* **Description:** Managing CPU, memory, and storage across hundreds or thousands of machines.
* **Problems:**

  * Resource contention between multiple jobs.
  * Efficient scheduling to maximize utilization.
* **Example:** YARN (Yet Another Resource Negotiator) allocates cluster resources to applications dynamically.

---

### 9. 📊 **Monitoring and Debugging**

* **Description:** Tracking system performance and finding bottlenecks is difficult.
* **Problems:**

  * Failures occur at random nodes and times.
  * Logs are distributed, making error tracking hard.
* **Example:** Tools like **Ambari**, **Cloudera Manager**, and **Ganglia** help monitor Hadoop clusters.

---

### 10. 💾 **Data Movement and Latency**

* **Description:** Large-scale data transfer between nodes consumes time and bandwidth.
* **Problems:**

  * Moving petabytes of data can be very slow.
  * Increases I/O bottlenecks.
* **Example:** Hadoop’s MapReduce minimizes data movement by sending computation to where data is stored (Data Locality Principle).

---

## 🧭 **Summary Table**

| Challenge              | Description                           | Example                 |
| ---------------------- | ------------------------------------- | ----------------------- |
| Network Issues         | Latency and packet loss between nodes | Slow job completion     |
| Data Partitioning      | Uneven data split across nodes        | Some nodes idle         |
| Consistency            | Keeping all replicas identical        | CAP theorem             |
| Fault Tolerance        | Handling node failures gracefully     | HDFS replication        |
| Security               | Protecting distributed data           | Kerberos in Hadoop      |
| Programming Complexity | Difficult to write parallel code      | MapReduce jobs          |
| Scalability            | Handling more nodes/users             | YARN scheduling         |
| Resource Management    | Efficient CPU/memory allocation       | YARN Resource Manager   |
| Monitoring             | Tracking failures across nodes        | Ambari, Ganglia         |
| Data Movement          | Large data transfer between nodes     | Data locality in Hadoop |

---

## 💡 **Real-World Analogy**

Think of a distributed system like a **team project** with many students:

* If the **internet connection** (network) is bad, they can’t communicate well.
* If one student **drops out** (node failure), others must handle the extra load.
* Keeping everyone’s **document version same** (consistency) is hard.
* The **teacher (resource manager)** must ensure everyone has enough tasks but not too many.

That’s exactly what happens in distributed systems — but at **massive computational scale**.

---

## 🧾 **Conclusion**

Distributed computing powers modern data systems like **Hadoop**, **Spark**, and **Google Cloud**.
However, it brings challenges in **data management**, **fault recovery**, **security**, and **synchronization** that must be carefully handled through:

* Efficient design principles
* Redundancy and replication
* Strong monitoring and management tools

---

# 🧱 **Hadoop Distributed File System (HDFS)**

---

## 🌍 **Introduction**

**HDFS** (Hadoop Distributed File System) is the **storage layer** of the **Hadoop ecosystem**.
It is designed to store **large data files** across multiple machines in a **distributed** and **fault-tolerant** manner.

HDFS is based on **Google File System (GFS)** and optimized for **high throughput** rather than low latency.

---

## 🎯 **Goals of HDFS**

* Store **huge files** (in GBs, TBs, or PBs)
* Provide **high fault tolerance**
* Enable **parallel access** to data
* Support **data locality** (move computation near data)
* Allow **horizontal scalability** (add more machines easily)

---

## 🧩 **HDFS Architecture Overview**

HDFS uses a **Master–Slave Architecture** consisting of:

1. **NameNode** (Master)
2. **DataNodes** (Slaves)
3. **Secondary NameNode** (Checkpoint Node)

---

### 🖥️ **HDFS Architecture Diagram**

```
                 +-------------------------+
                 |       NameNode          |
                 | (Master – stores metadata) |
                 +-----------+-------------+
                             |
      -------------------------------------------------
      |                       |                       |
+-------------+        +-------------+         +-------------+
|   DataNode 1|        |   DataNode 2|         |   DataNode 3|
| (Stores Blocks)       | (Stores Blocks)       | (Stores Blocks)
+-------------+        +-------------+         +-------------+
```

---

## ⚙️ **Components of HDFS**

| Component              | Role                  | Description                                                                       |
| ---------------------- | --------------------- | --------------------------------------------------------------------------------- |
| **NameNode**           | Master                | Manages **metadata** — file names, locations of blocks, replication info, etc.    |
| **DataNode**           | Worker                | Actually **stores data blocks** on local disks.                                   |
| **Secondary NameNode** | Checkpoint node       | Periodically merges NameNode’s metadata with its edit logs to prevent corruption. |
| **Block**              | Basic unit of storage | Files are divided into **fixed-size blocks** (default 128 MB or 256 MB).          |

---

## 📦 **How HDFS Stores Data**

When a file is stored in HDFS:

1. The file is **split into blocks** (e.g., 256 MB each).
2. Each block is **replicated** (default replication factor = 3).
3. The **NameNode** records where each block is stored.
4. The **DataNodes** store the actual blocks.

📘 Example:

```
File: "data.txt" (512 MB)
Blocks: B1, B2
Replication: 3

Block B1 → DataNode1, DataNode2, DataNode3  
Block B2 → DataNode2, DataNode3, DataNode4
```

---

## 🔁 **Data Flow in HDFS**

### **1️⃣ Write Operation**

```
Client → NameNode → DataNodes
```

Steps:

1. Client requests NameNode to write a file.
2. NameNode responds with available DataNodes.
3. Client splits file into blocks.
4. Each block is written and **replicated** to multiple DataNodes.

---

### **2️⃣ Read Operation**

```
Client → NameNode → DataNodes → Client
```

Steps:

1. Client requests NameNode to read a file.
2. NameNode sends block locations.
3. Client directly contacts nearest DataNode (for speed).
4. Data is streamed back in parallel from multiple DataNodes.

---

## 💥 **Fault Tolerance in HDFS**

HDFS ensures **data reliability** even when nodes fail:

* Each block is **replicated** across multiple DataNodes.
* If a DataNode fails, NameNode automatically re-replicates the lost blocks on other healthy nodes.
* Heartbeat signals between NameNode and DataNodes help track failures.

---

## 🧮 **Replication Example**

| Block | Replica 1 | Replica 2 | Replica 3 |
| ----- | --------- | --------- | --------- |
| B1    | Node1     | Node2     | Node3     |
| B2    | Node2     | Node3     | Node4     |
| B3    | Node3     | Node4     | Node1     |

🧠 **Benefit:** Even if Node2 crashes, all blocks still exist elsewhere.

---

## 📊 **Advantages of HDFS**

| Advantage           | Description                             |
| ------------------- | --------------------------------------- |
| **Scalable**        | Add more nodes easily for more storage  |
| **Fault-tolerant**  | Automatic replication and recovery      |
| **Cost-effective**  | Runs on inexpensive commodity hardware  |
| **High throughput** | Parallel read/write from multiple nodes |
| **Data locality**   | Processing occurs near data location    |

---

## ⚠️ **Limitations of HDFS**

| Limitation                       | Description                                                  |
| -------------------------------- | ------------------------------------------------------------ |
| **Not suitable for small files** | Too much metadata overhead                                   |
| **Not for real-time access**     | Optimized for batch processing                               |
| **Single NameNode bottleneck**   | Centralized metadata manager (improved in HA configurations) |

---

## 🧰 **Real-World Example**

Imagine Netflix storing **movies** (each several GBs):

* Each movie is split into chunks (blocks).
* Each block is stored in multiple nodes.
* Even if one node fails, the movie can still be streamed without interruption.

---

## 🧠 **In Short**

| Concept                 | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| **File Split**          | Large files are broken into blocks                    |
| **Replication**         | Each block stored on multiple nodes                   |
| **Fault Tolerance**     | Data automatically recovered on failure               |
| **Master-Slave**        | NameNode manages, DataNodes store                     |
| **Parallel Processing** | Multiple nodes handle different blocks simultaneously |

---

# ⚙️ **Processing Data with Hadoop**

---

## 🌍 **Introduction**

Storing data in **HDFS** is only the first step.
To actually **analyze** and **gain insights** from that data, Hadoop provides a **data processing framework** called **MapReduce**.

So, **processing data with Hadoop** essentially means using:

> 🧠 **HDFS (Storage)** + ⚙️ **MapReduce (Processing)**

Together, they form the **core of Hadoop’s Big Data engine**.

---

## 🧩 **Data Processing Flow in Hadoop**

Here’s how data flows through the system:

```
          ┌─────────────┐
          │   Input Data│
          │ (in HDFS)   │
          └──────┬──────┘
                 │
           1. Split into Blocks
                 │
                 ▼
          ┌─────────────┐
          │ Map Phase   │
          │ (Processing │
          │  per block) │
          └──────┬──────┘
                 │
         2. Intermediate Key-Value Pairs
                 │
                 ▼
          ┌─────────────┐
          │ Shuffle &   │
          │ Sort Phase  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │ Reduce Phase│
          │ (Aggregation│
          │   Results)  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │ Output Data │
          │  (HDFS)     │
          └─────────────┘
```

---

## 🧠 **Step-by-Step Explanation**

### **1️⃣ Input Phase**

* Input data is stored in **HDFS**.
* Hadoop divides the file into **fixed-size blocks** (128 MB or 256 MB).
* Each block is processed by a **Mapper** running on a **DataNode** where the block physically resides.
* This ensures **data locality** (move computation to data, not data to computation).

📘 Example:
If you have a 512 MB log file and block size is 128 MB →
4 Mappers will run in parallel, one per block.

---

### **2️⃣ Map Phase**

* The **Map function** takes input data and converts it into **key-value pairs**.
* It performs filtering, sorting, or transformation tasks.

📄 Example: Word Count Mapper

```java
public class WordMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {
        for (String word : value.toString().split(" ")) {
            context.write(new Text(word), new IntWritable(1));
        }
    }
}
```

🧩 Output Example:

```
Input: "Hadoop is fast Hadoop is scalable"
Mapper Output:
(Hadoop,1), (is,1), (fast,1), (Hadoop,1), (is,1), (scalable,1)
```

---

### **3️⃣ Shuffle and Sort Phase**

* Hadoop automatically **groups and sorts** the intermediate key-value pairs.
* All identical keys are collected together before going to the **Reducer**.

🧮 Example:

```
Before Shuffle: (Hadoop,1), (is,1), (fast,1), (Hadoop,1)
After Shuffle:  (Hadoop,[1,1]), (is,[1,1]), (fast,[1])
```

---

### **4️⃣ Reduce Phase**

* The **Reducer** aggregates, summarizes, or combines the data.
* The final output is stored back in **HDFS**.

📄 Example: Word Count Reducer

```java
public class WordReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values)
            sum += val.get();
        context.write(key, new IntWritable(sum));
    }
}
```

🧩 Output Example:

```
(Hadoop,2), (is,2), (fast,1), (scalable,1)
```

---

### **5️⃣ Output Phase**

* The **Reducer’s output** is written back to **HDFS**.
* Each Reducer writes one output file.

📁 Example:

```
/user/hadoop/output/part-r-00000
```

---

## ⚙️ **Execution Flow Diagram**

```
Client
  │
  ▼
Job Submission
  │
  ▼
Resource Manager (YARN)
  │
  ▼
Application Master
  │
  ▼
DataNodes → Map Tasks → Shuffle/Sort → Reduce Tasks
  │
  ▼
Output Stored in HDFS
```

---

## 🚀 **Advantages of Hadoop Data Processing**

| Feature                 | Description                                                    |
| ----------------------- | -------------------------------------------------------------- |
| **Parallel Processing** | Multiple nodes process data simultaneously                     |
| **Scalability**         | Add more nodes to process larger datasets                      |
| **Fault Tolerance**     | If a node fails, Hadoop reruns the task on another node        |
| **Data Locality**       | Reduces network bottleneck by processing data where it resides |
| **Cost-Effective**      | Runs on commodity hardware                                     |

---

## 💡 **Real-World Example**

Let’s say you have **1 TB of web server logs**, and you want to find the **most visited pages**:

1. Store logs in HDFS.
2. Mapper extracts page URLs.
3. Reducer counts occurrences.
4. Output gives you the most popular URLs.

✅ You processed **1 TB of data** in minutes — distributed across 50–100 nodes.

---

## 🧾 **Summary**

| Step | Phase        | Description                            |
| ---- | ------------ | -------------------------------------- |
| 1    | Input        | Data stored and divided in HDFS blocks |
| 2    | Map          | Key–value pair generation              |
| 3    | Shuffle/Sort | Grouping by key                        |
| 4    | Reduce       | Aggregation of values                  |
| 5    | Output       | Final data written back to HDFS        |

---

In short:

> **“HDFS stores big data, MapReduce processes it efficiently and reliably.”**

---

# ⚙️ **Managing Resources and Applications with Hadoop YARN**

---

## 🌍 **Introduction**

**YARN** stands for

> **Yet Another Resource Negotiator**

It is the **resource management and job scheduling layer** of Hadoop — introduced in **Hadoop v2.0**.

Before YARN, the **JobTracker** (in Hadoop v1) handled **both resource management and job scheduling**, which became a bottleneck for large clusters.
YARN **separates these two concerns** — making Hadoop **faster, more scalable, and multi-framework capable** (it can run MapReduce, Spark, Tez, etc.).

---

## 🧠 **What YARN Does**

YARN is responsible for:

1. **Managing resources** (CPU, memory) across all cluster nodes.
2. **Scheduling jobs** — deciding where and when tasks should run.
3. **Monitoring tasks** and restarting them in case of failure.

---

## 🏗️ **YARN Architecture**

YARN follows a **Master–Slave Architecture** consisting of **four main components:**

| Component                  | Type            | Role                                                             |
| -------------------------- | --------------- | ---------------------------------------------------------------- |
| **ResourceManager (RM)**   | Master          | Allocates cluster resources among applications.                  |
| **NodeManager (NM)**       | Slave           | Runs on each DataNode to manage local resources.                 |
| **ApplicationMaster (AM)** | Per Application | Manages lifecycle of one user application/job.                   |
| **Container**              | Resource Unit   | The actual environment where a task runs (includes CPU, memory). |

---

## 🧩 **YARN Architecture Diagram**

```
                    ┌────────────────────────────────────┐
                    │          ResourceManager            │
                    │------------------------------------│
                    │  Scheduler + Application Manager    │
                    └───────────────┬────────────────────┘
                                    │
                     ┌──────────────┴───────────────┐
                     │                              │
       ┌────────────────────┐        ┌────────────────────┐
       │    NodeManager 1   │        │    NodeManager 2   │
       │ (on DataNode 1)    │        │ (on DataNode 2)    │
       ├────────────────────┤        ├────────────────────┤
       │  Container 1       │        │  Container 2       │
       │  Container 3       │        │  Container 4       │
       └────────────────────┘        └────────────────────┘
```

---

## ⚙️ **Working of YARN — Step by Step**

Let’s see how YARN executes a Hadoop job:

### **1️⃣ Client Submits Job**

* The client submits a job to the **ResourceManager (RM)**.

---

### **2️⃣ ResourceManager Starts ApplicationMaster**

* RM assigns the job to an available **NodeManager (NM)**.
* It launches an **ApplicationMaster (AM)** inside a **container** on that node.

---

### **3️⃣ ApplicationMaster Requests Resources**

* AM negotiates with RM for required **resources** (CPU, memory) to execute tasks.
* RM allocates containers on various **NodeManagers**.

---

### **4️⃣ Containers Launch Tasks**

* NM launches **containers**, each running **map or reduce tasks** (or Spark executors, etc.).
* Containers report their **status** to AM.

---

### **5️⃣ Monitoring and Completion**

* AM continuously monitors task progress.
* After completion, AM informs RM and shuts down.
* RM marks resources as free again.

---

## 🧮 **Detailed Component Functions**

### 🔹 **1. ResourceManager (RM)**

* The **central authority** of the cluster.
* Two main subcomponents:

  * **Scheduler** → Allocates resources based on policies (capacity, fair, FIFO).
  * **Application Manager** → Manages job submissions and ApplicationMasters.

---

### 🔹 **2. NodeManager (NM)**

* Runs on every DataNode.
* Reports available resources to RM.
* Launches and monitors **containers** assigned by RM.
* Sends **heartbeats** to RM (to indicate it’s alive).

---

### 🔹 **3. ApplicationMaster (AM)**

* One AM per application.
* Negotiates resources from RM.
* Monitors the application execution.
* Requests containers from NM.
* Can recover from failures by restarting tasks.

---

### 🔹 **4. Container**

* A container is a **logical unit of resource allocation** (e.g., 2 GB RAM, 1 CPU).
* NMs create containers and isolate them using **Linux cgroups**.
* Containers can run any type of task — MapReduce, Spark, Hive, etc.

---

## 💻 **Example – MapReduce on YARN**

Let’s say you run a **WordCount job**:

1. Job submitted to **ResourceManager**.
2. RM launches **ApplicationMaster**.
3. AM requests containers for mappers and reducers.
4. NMs launch those containers.
5. Map tasks read data from **HDFS**.
6. Intermediate data shuffled → reduce tasks aggregate → results written back to **HDFS**.
7. AM reports completion → containers released.

---

## 🧭 **Advantages of YARN**

| Feature                         | Description                                                |
| ------------------------------- | ---------------------------------------------------------- |
| **Scalability**                 | Supports thousands of nodes and concurrent applications    |
| **Multi-tenancy**               | Can run different frameworks (MapReduce, Spark, Tez, etc.) |
| **Better Resource Utilization** | Dynamically allocates CPU and memory                       |
| **Fault Tolerance**             | Automatically restarts failed containers or AM             |
| **Decoupled Architecture**      | Separates job scheduling from resource management          |
| **High Cluster Utilization**    | Efficiently uses all cluster resources                     |

---

## ⚠️ **Limitations of YARN**

| Limitation                  | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| **Complex Configuration**   | Managing RM, NM, AM can be difficult                                |
| **Single Point of Failure** | ResourceManager can still be a bottleneck (unless HA is configured) |
| **Monitoring Overhead**     | Many moving parts → higher operational complexity                   |

---

## 📊 **Comparison: JobTracker (Old) vs YARN (New)**

| Feature                 | Hadoop v1 (JobTracker)               | Hadoop v2 (YARN)                  |
| ----------------------- | ------------------------------------ | --------------------------------- |
| **Architecture**        | Single JobTracker                    | RM + NM + AM                      |
| **Scalability**         | Limited to ~4000 nodes               | >10,000 nodes                     |
| **Resource Management** | Combined with scheduling             | Separated (YARN)                  |
| **Framework Support**   | Only MapReduce                       | Multiple (Spark, Tez, Hive, etc.) |
| **Fault Tolerance**     | JobTracker failure = cluster failure | AM restarts automatically         |
| **Utilization**         | Poor                                 | Dynamic & efficient               |

---

## 💡 **Real-World Example**

In a company like **Netflix**:

* Hadoop YARN allocates containers to **Spark streaming jobs**, **Hive queries**, and **MapReduce ETL pipelines** all at the same time.
* YARN ensures that no single job consumes all cluster resources.
* It dynamically manages memory and CPU based on real-time needs.

---

## 🧾 **Summary**

| Concept             | Description                                  |
| ------------------- | -------------------------------------------- |
| **YARN Full Form**  | Yet Another Resource Negotiator              |
| **Main Role**       | Resource management & job scheduling         |
| **Main Components** | RM, NM, AM, Containers                       |
| **Key Benefit**     | Multi-framework support and scalability      |
| **Introduced In**   | Hadoop 2.0                                   |
| **Replaces**        | JobTracker/TaskTracker model from Hadoop 1.x |

---

✅ **In short:**

> YARN = Hadoop’s **Operating System** for Big Data clusters — managing **resources, scheduling, and applications** efficiently.

---

# 🧠 **Interacting with the Hadoop Ecosystem**

### 🌍 What is the Hadoop Ecosystem?

The **Hadoop Ecosystem** refers to a collection of **tools and frameworks** built around **Hadoop Core Components** to handle **data storage**, **data processing**, **data analysis**, and **data management** in a distributed environment.

Hadoop itself has two main parts:

* **HDFS (Hadoop Distributed File System)** – for distributed storage.
* **MapReduce** – for distributed data processing.

However, real-world Big Data projects require much more than just storage and processing.
That’s where the **Hadoop Ecosystem** comes in — tools like Hive, Pig, Sqoop, HBase, Spark, and Oozie extend Hadoop’s capabilities.

---

### ⚙️ **Core Hadoop Components**

| Component     | Description                                        |
| ------------- | -------------------------------------------------- |
| **HDFS**      | Distributed storage system for large datasets.     |
| **YARN**      | Resource management and job scheduling framework.  |
| **MapReduce** | Programming model for parallel processing of data. |

---

### 🧩 **Key Components in Hadoop Ecosystem**

Below is a breakdown of the main tools and their purpose:

| Category                       | Tool                                   | Purpose                                                      |
| ------------------------------ | -------------------------------------- | ------------------------------------------------------------ |
| **Data Storage**               | **HDFS**, **HBase**                    | Store structured and unstructured data in distributed form.  |
| **Data Ingestion**             | **Sqoop**, **Flume**, **Kafka**        | Bring data into Hadoop from various sources.                 |
| **Data Processing**            | **MapReduce**, **Spark**, **Tez**      | Process large datasets efficiently.                          |
| **Data Querying & Analysis**   | **Hive**, **Pig**, **Impala**          | SQL-like querying and high-level data analysis.              |
| **Data Access & Search**       | **HBase**, **Solr**, **ElasticSearch** | Provide fast data retrieval and indexing.                    |
| **Workflow Scheduling**        | **Oozie**, **Azkaban**, **Airflow**    | Manage and automate complex data pipelines.                  |
| **Data Governance & Metadata** | **Zookeeper**, **Ambari**, **Atlas**   | Handle configuration, coordination, and metadata management. |
| **Machine Learning**           | **Mahout**, **MLlib (Spark)**          | Perform machine learning and data mining.                    |

---

### 🧭 **Typical Hadoop Ecosystem Architecture Diagram**

```
                     +-----------------------------+
                     |     Data Sources (RDBMS,    |
                     |   IoT Devices, Logs, APIs)  |
                     +-------------+---------------+
                                   |
                    +--------------v--------------+
                    |  Data Ingestion Layer        |
                    | (Sqoop, Flume, Kafka)        |
                    +--------------+---------------+
                                   |
                    +--------------v--------------+
                    |  Storage Layer (HDFS, HBase) |
                    +--------------+---------------+
                                   |
                    +--------------v--------------+
                    |  Processing Layer            |
                    | (MapReduce, Spark, Tez)      |
                    +--------------+---------------+
                                   |
                    +--------------v--------------+
                    |  Query Layer (Hive, Pig)     |
                    +--------------+---------------+
                                   |
                    +--------------v--------------+
                    |  Visualization (Tableau, BI) |
                    +--------------+---------------+
```

---

### 💡 **How to Interact with the Hadoop Ecosystem**

1. **Using Command Line (CLI):**

   * Hadoop provides shell commands for interacting with HDFS.

   ```bash
   hdfs dfs -ls /user/
   hdfs dfs -put localfile.txt /user/hadoop/
   hdfs dfs -cat /user/hadoop/localfile.txt
   ```

2. **Using Hive (SQL-like Interface):**

   * Hive allows querying HDFS data using SQL syntax.

   ```sql
   SELECT department, AVG(salary)
   FROM employees
   GROUP BY department;
   ```

3. **Using Pig (Script-based Interface):**

   * Pig uses Pig Latin, a scripting language for data transformation.

   ```pig
   A = LOAD 'data/employees.csv' USING PigStorage(',') AS (id:int, name:chararray, dept:chararray);
   B = GROUP A BY dept;
   C = FOREACH B GENERATE group, COUNT(A);
   DUMP C;
   ```

4. **Using Spark (In-Memory Processing):**

   * Spark provides APIs in Python, Java, Scala for fast processing.

   ```python
   from pyspark import SparkContext
   sc = SparkContext("local", "WordCount")
   text = sc.textFile("hdfs://localhost:9000/data/file.txt")
   counts = text.flatMap(lambda x: x.split(" ")) \
                .map(lambda x: (x, 1)) \
                .reduceByKey(lambda a, b: a + b)
   counts.saveAsTextFile("hdfs://localhost:9000/output")
   ```

5. **Using REST APIs:**

   * Many Hadoop tools (like HDFS, YARN) expose REST APIs for automation and monitoring.

---

### 🧠 **Interdependencies Between Components**

| Tool      | Depends On            | Purpose                   |
| --------- | --------------------- | ------------------------- |
| **Hive**  | HDFS, MapReduce/Spark | Query structured data     |
| **Pig**   | HDFS, MapReduce       | Data flow scripting       |
| **Sqoop** | HDFS, RDBMS           | Import/export data        |
| **Flume** | HDFS, Kafka           | Stream data ingestion     |
| **Spark** | HDFS, YARN            | In-memory data processing |
| **Oozie** | All                   | Workflow management       |

---

### 🧾 **Advantages of the Hadoop Ecosystem**

* **Scalable** — Handles petabytes of data easily.
* **Cost-effective** — Open-source and runs on commodity hardware.
* **Fault-tolerant** — Data is replicated across nodes.
* **Flexible** — Handles structured, semi-structured, and unstructured data.
* **Extensible** — Supports multiple tools and programming models.

---

### 🧩 **Example Use Case:**

**Scenario:** An e-commerce company wants to analyze customer behavior.

| Stage           | Hadoop Component         | Description                  |
| --------------- | ------------------------ | ---------------------------- |
| Data Collection | **Flume**, **Kafka**     | Collect clickstream data     |
| Storage         | **HDFS**, **HBase**      | Store customer logs          |
| Processing      | **MapReduce**, **Spark** | Process logs for patterns    |
| Analysis        | **Hive**, **Pig**        | Generate reports             |
| Scheduling      | **Oozie**                | Automate daily analysis jobs |

---

✅ **In summary:**
The Hadoop Ecosystem acts like a **modular toolkit** — where each component specializes in a specific part of data management.
By interacting through **command line**, **scripts**, or **programmatic APIs**, users can build powerful, large-scale data analytics pipelines.

---

# 🧠 **MapReduce**

---

## 📘 **Introduction**

**MapReduce** is a **programming model** and **processing framework** introduced by Google and later implemented in Hadoop to process **large-scale datasets** in a **distributed** and **parallel** manner.

It divides a task into **two main phases**:

1. **Map Phase** → Processes input data and converts it into key-value pairs.
2. **Reduce Phase** → Aggregates, filters, or summarizes the mapped data.

This model allows Hadoop to process **terabytes or petabytes of data** efficiently across **many nodes** in a cluster.

---

## ⚙️ **How MapReduce Works**

### 📊 **Step-by-Step Data Flow**

```
        +-------------------+
        |  Input Data (HDFS)|
        +-------------------+
                    |
                    v
        +-------------------+
        |    Splitting      |  --> Divides data into Input Splits
        +-------------------+
                    |
                    v
        +-------------------+
        |      Mapping      |  --> Mapper processes data and emits key-value pairs
        +-------------------+
                    |
                    v
        +-------------------+
        |     Shuffling     |  --> Keys are sorted and grouped
        +-------------------+
                    |
                    v
        +-------------------+
        |      Reducing     |  --> Reducer aggregates results
        +-------------------+
                    |
                    v
        +-------------------+
        |  Output (HDFS)    |
        +-------------------+
```

---

## 🧩 **Key Phases of MapReduce**

| Phase                      | Description                                                                                          | Example                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **1. Input Splitting**     | Large data files are split into smaller chunks (InputSplits). Each split is processed by one Mapper. | A 1TB file might be split into 64MB chunks.        |
| **2. Mapping**             | Each Mapper processes an input split and emits key-value pairs.                                      | `("word", 1)` for each word.                       |
| **3. Shuffling & Sorting** | Groups all values by their keys and sends them to the appropriate Reducer.                           | All pairs for `"word"` go to the same reducer.     |
| **4. Reducing**            | Aggregates or summarizes data (e.g., counting, averaging).                                           | Adds all `"word"` counts to get total occurrences. |
| **5. Output**              | The final output is stored in HDFS.                                                                  | `("word", 120)`                                    |

---

## 🧮 **Example: Word Count Program**

Let’s take a classic MapReduce example — counting word occurrences in a text file.

### 🧩 Input Data

```
Hello Hadoop
Hello Big Data
```

### 🗺️ Mapper Phase

Each line is split into words and emits:

```
("Hello", 1)
("Hadoop", 1)
("Hello", 1)
("Big", 1)
("Data", 1)
```

### 🔁 Shuffle & Sort

Grouped by key:

```
"Big" -> [1]
"Data" -> [1]
"Hadoop" -> [1]
"Hello" -> [1, 1]
```

### 🧾 Reducer Phase

Sum up values:

```
("Big", 1)
("Data", 1)
("Hadoop", 1)
("Hello", 2)
```

### 📤 Output (HDFS)

```
Big     1
Data    1
Hadoop  1
Hello   2
```

---

## 💻 **Word Count MapReduce Program (in Java)**

```java
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    // Mapper Class
    public static class TokenizerMapper
         extends Mapper<Object, Text, Text, IntWritable>{

        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }
    }

    // Reducer Class
    public static class IntSumReducer
         extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    // Main Method
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

## 🧱 **Components of MapReduce**

| Component        | Description                                                              |
| ---------------- | ------------------------------------------------------------------------ |
| **Mapper**       | Processes input splits and produces key-value pairs.                     |
| **Reducer**      | Processes keys and aggregates values.                                    |
| **Combiner**     | Optional mini-reducer that runs on Mapper output to reduce network load. |
| **Partitioner**  | Decides which reducer a given key-value pair should go to.               |
| **InputFormat**  | Defines how input data is split and read.                                |
| **OutputFormat** | Defines how output data is written to HDFS.                              |

---

## 🗺️ **MapReduce Cluster Architecture**

```
          +-------------------------+
          |     Client Program      |
          +-----------+-------------+
                      |
                      v
          +-----------+-------------+
          |     Job Tracker / YARN   |
          |   (Job Scheduling)       |
          +-----------+-------------+
                      |
        +-------------+-------------+
        |                           |
+-------v--------+        +----------v-------+
|  Task Tracker  |        |   Task Tracker   |
| (Mapper/Reducer)|       | (Mapper/Reducer) |
+----------------+        +------------------+
```

---

## ⚡ **Advantages of MapReduce**

✅ **Scalable** – Handles petabytes of data efficiently.
✅ **Parallel Processing** – Splits workload across nodes.
✅ **Fault Tolerant** – Retries failed tasks automatically.
✅ **Data Locality** – Moves computation near data, not vice versa.
✅ **Cost Effective** – Works on commodity hardware.

---

## ⚠️ **Limitations of MapReduce**

❌ Batch-oriented (not suitable for real-time processing).
❌ High disk I/O overhead due to reading/writing between stages.
❌ Complex to write low-level Java code for simple queries.
❌ Slow for iterative algorithms (like machine learning).

---

## 🔁 **When to Use MapReduce**

| Use Case               | Example                                     |
| ---------------------- | ------------------------------------------- |
| **Log Processing**     | Analyzing web server logs                   |
| **Indexing**           | Building search indexes                     |
| **Data Summarization** | Counting and grouping operations            |
| **ETL Operations**     | Extract, transform, and load large datasets |

---

## 📈 **Comparison: MapReduce vs Spark**

| Feature         | MapReduce          | Spark                  |
| --------------- | ------------------ | ---------------------- |
| **Processing**  | Disk-based (batch) | In-memory (fast)       |
| **Speed**       | Slower             | Up to 100x faster      |
| **Ease of Use** | Complex (Java)     | Easy (Python, Scala)   |
| **Iteration**   | Not efficient      | Very efficient         |
| **Use Case**    | Batch jobs         | Real-time + batch jobs |

---

✅ **In short:**

> **MapReduce** is the *engine* that powers Hadoop’s distributed processing.
> It turns big data tasks into manageable **map** and **reduce** operations that can run **in parallel** across many nodes.

---

# 🧩 **Mapper - Reducer - Combiner - Partitioner - Searching - Sorting - Compression**

---

## 🧠 1️⃣ **Mapper**

### 🧾 **Definition**

A **Mapper** is the **first phase** in the MapReduce framework.
It takes **input data** (from HDFS) and transforms it into a **set of key–value pairs (K, V)**.

Each **input split** is processed by **one Mapper task**.

---

### ⚙️ **Working**

1. Input data is split into records (usually lines).
2. Each record is processed by the `map()` function.
3. Mapper emits intermediate `(key, value)` pairs.

---

### 🧮 **Example**

#### Input file:

```
apple banana apple orange
banana orange apple
```

#### Mapper output:

```
("apple", 1)
("banana", 1)
("apple", 1)
("orange", 1)
("banana", 1)
("orange", 1)
("apple", 1)
```

---

### 💻 **Java Mapper Example**

```java
public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {
        String[] tokens = value.toString().split("\\s+");
        for (String token : tokens) {
            word.set(token);
            context.write(word, one);
        }
    }
}
```

---

### 📊 **Diagram: Mapper Phase**

```
        Input Split 1              Input Split 2
     +------------------+      +------------------+
     |apple banana apple|      |banana orange apple|
     +--------+---------+      +---------+---------+
              |                         |
              v                         v
        Mapper Task 1             Mapper Task 2
              |                         |
              v                         v
       ("apple",1)                ("banana",1)
       ("banana",1)               ("orange",1)
       ("apple",1)                ("apple",1)
```

---

## 🧠 2️⃣ **Reducer**

### 🧾 **Definition**

A **Reducer** takes the intermediate `(key, value)` pairs from the Mapper phase,
**groups all values by their key**, and performs **aggregation or computation**.

---

### ⚙️ **Working**

1. Collects all values for the same key.
2. Applies reduce logic (e.g., summation, averaging).
3. Emits final output `(key, value)`.

---

### 💡 **Example**

Mapper output:

```
("apple", 1)
("apple", 1)
("banana", 1)
("banana", 1)
("orange", 1)
```

Reducer output:

```
("apple", 2)
("banana", 2)
("orange", 1)
```

---

### 💻 **Reducer Example**

```java
public static class IntSumReducer
       extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        result.set(sum);
        context.write(key, result);
    }
}
```

---

### 📊 **Diagram: Shuffle, Sort, Reduce**

```
Mapper Outputs          Shuffle & Sort           Reducer Output
("apple",1)        →     "apple" → [1,1,1]    →   ("apple",3)
("banana",1)       →     "banana" → [1,1]     →   ("banana",2)
("orange",1)       →     "orange" → [1]       →   ("orange",1)
```

---

## 🧠 3️⃣ **Combiner**

### 🧾 **Definition**

A **Combiner** is an **optional** mini-reducer that runs **after the Mapper phase**
to perform **local aggregation** before data is sent to Reducers.

It helps **reduce network traffic** during the shuffle phase.

---

### ⚙️ **Purpose**

* Minimize data transfer between Mapper and Reducer.
* Perform **partial reduction** locally on each node.

---

### 💡 **Example**

Without combiner:

```
Mapper → ("apple",1), ("apple",1), ("banana",1)
```

Sent to Reducer (3 pairs)

With combiner:

```
Combiner → ("apple",2), ("banana",1)
```

Only 2 pairs sent → less network usage ✅

---

### 💻 **Combiner Example**

Usually, you can use the same class as Reducer:

```java
job.setCombinerClass(IntSumReducer.class);
```

---

### 📊 **Diagram: Combiner**

```
Mapper Output → Combiner → Reducer

("apple",1)    → ("apple",3) → ("apple",6)
("apple",1)
("apple",1)
```

---

## 🧠 4️⃣ **Partitioner**

### 🧾 **Definition**

The **Partitioner** controls **which Reducer** will receive a given key.

Default behavior:

* Hadoop uses **HashPartitioner** which assigns keys based on:

  ```
  partition = (key.hashCode() & Integer.MAX_VALUE) % numReducers
  ```

---

### ⚙️ **Why It Matters**

* Ensures even distribution of data across reducers.
* Prevents one reducer from being overloaded.

---

### 💡 **Example**

If there are **3 reducers**, and keys are distributed as:

```
apple  → Reducer 0
banana → Reducer 1
cherry → Reducer 2
```

---

### 💻 **Custom Partitioner Example**

```java
public static class CustomPartitioner
       extends Partitioner<Text, IntWritable> {
    public int getPartition(Text key, IntWritable value, int numPartitions) {
        if (key.toString().startsWith("a"))
            return 0;
        else if (key.toString().startsWith("b"))
            return 1;
        else
            return 2 % numPartitions;
    }
}
```

---

### 📊 **Diagram: Partitioner**

```
Mapper Output:
("apple",3), ("banana",2), ("cherry",1)

Partitioner:
→ Reducer 0: ("apple",3)
→ Reducer 1: ("banana",2)
→ Reducer 2: ("cherry",1)
```

---

## 🧠 5️⃣ **Searching in MapReduce**

### 🧾 **Definition**

Searching means finding **specific records** or **patterns** in large datasets using MapReduce.

---

### 💡 **Example – Searching for “Hadoop” in files**

#### Mapper:

Emits filename if line contains “Hadoop”.

```java
public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException {
    if (value.toString().contains("Hadoop")) {
        context.write(new Text("Found in:"), new Text(fileName));
    }
}
```

#### Reducer:

Collects all file names where “Hadoop” appeared.

---

### 📊 **Conceptual Flow**

```
Input:
file1: Hadoop is great
file2: Big data with Hadoop

Output:
Found in: file1
Found in: file2
```

---

## 🧠 6️⃣ **Sorting in MapReduce**

### 🧾 **Definition**

Sorting is **automatically handled** by Hadoop between the Map and Reduce phases
during the **Shuffle and Sort** stage.

---

### ⚙️ **Types of Sorting**

| Type                  | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| **Sort by Key**       | Default behavior; sorts all keys before sending to Reducer. |
| **Secondary Sorting** | Custom logic for sorting values within the same key.        |

---

### 💡 **Example**

Mapper emits:

```
("apple", 1)
("banana", 1)
("apple", 1)
```

Before reducing, keys are sorted:

```
("apple", [1,1])
("banana", [1])
```

---

### 💻 **Custom Sort Example**

To sort keys in reverse order:

```java
job.setSortComparatorClass(DescendingKeyComparator.class);
```

---

### 📊 **Sorting Flow Diagram**

```
Mapper Output → Shuffle → Sort → Group → Reducer
```

---

## 🧠 7️⃣ **Compression in MapReduce**

### 🧾 **Definition**

Compression reduces the **size of data** transferred and stored between Hadoop stages,
thus improving **performance and efficiency**.

---

### ⚙️ **Compression Can Be Applied:**

| Stage         | Example                         |
| ------------- | ------------------------------- |
| Input Data    | Compressed HDFS files           |
| Mapper Output | Compressed intermediate results |
| Final Output  | Compressed reducer output       |

---

### 💡 **Supported Codecs**

| Codec           | Format                     | Extension |
| --------------- | -------------------------- | --------- |
| **GzipCodec**   | Fast compression           | `.gz`     |
| **BZip2Codec**  | Higher compression ratio   | `.bz2`    |
| **SnappyCodec** | Very fast, low compression | `.snappy` |
| **LZOCodec**    | Good balance               | `.lzo`    |

---

### 💻 **Enable Compression in Code**

```java
conf.setBoolean("mapreduce.output.fileoutputformat.compress", true);
conf.setClass("mapreduce.output.fileoutputformat.compress.codec",
              org.apache.hadoop.io.compress.GzipCodec.class,
              org.apache.hadoop.io.compress.CompressionCodec.class);
```

---

### 📈 **Benefits of Compression**

✅ Faster job execution (less I/O).
✅ Reduced storage space.
✅ Lower network bandwidth usage.

---

### ⚠️ **Considerations**

* CPU overhead for compression/decompression.
* Choose codec depending on the use case (Snappy for speed, BZip2 for ratio).

---

## 🧾 **Summary Table**

| Concept         | Purpose                   | Example Output            |
| --------------- | ------------------------- | ------------------------- |
| **Mapper**      | Generates key-value pairs | (“apple”, 1)              |
| **Reducer**     | Aggregates values         | (“apple”, 3)              |
| **Combiner**    | Reduces local data volume | (“apple”, 2)              |
| **Partitioner** | Routes data to reducers   | Key-based assignment      |
| **Searching**   | Finds patterns in data    | Lines containing “Hadoop” |
| **Sorting**     | Orders keys before reduce | (“apple”, then “banana”)  |
| **Compression** | Reduces data size         | Output stored as `.gz`    |

---

✅ **In summary:**

> MapReduce is like a production line —
> **Mapper** breaks data into pieces, **Combiner** tidies up locally,
> **Partitioner** routes it properly, **Reducer** assembles results,
> and **Sorting/Compression** optimize the flow.

---

