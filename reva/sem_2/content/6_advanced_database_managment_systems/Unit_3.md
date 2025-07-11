# Unit - 3 -> Transaction Processing System & Schedules
Introduction to Transaction Concept, Transaction Processing and System: Transaction Concept, A Simple Transaction Model, Storage Sturcture(T2);
Introduction to Transaction Processsing : Single - User versus Multiuser Systems, Why Concurrency Control is Needed, Why Recovery Is Needed;
Transaction And System Concepts : Transaction States and Additional Operations; Desirable Properties of Transactions.

Concurrency Control Through Schedules: Taxonomy of Schedules - Characterizing Schedules Based On  Recoverability,
Characterizing Schedules Based on Serializbility(T1);
Transaction Isolation Levels(T2).

## Content -> 
### Introduction to Transaction Concept — Detailed Explanation

---

#### 1. **Definition of a Transaction**

* A **transaction** is a **logical unit of work** that consists of one or more **database operations** (e.g., read, write, update) executed as a single, indivisible sequence.
* It must be **executed fully or not at all** to maintain the **integrity of the database**.

---

#### 2. **Example of a Transaction**

**Bank Transfer Example**
Transferring ₹500 from Account A to Account B:

1. Read balance of Account A
2. Subtract ₹500 from A
3. Write new balance to Account A
4. Read balance of Account B
5. Add ₹500 to B
6. Write new balance to Account B

→ These steps together form **one transaction**.

---

#### 3. **Goals of a Transaction**

* Maintain **data consistency**
* Ensure **atomicity** of multiple database operations
* Support **concurrent access** to data
* Enable **recovery** from system failures

---

#### 4. **Transaction in SQL**

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 500 WHERE acc_id = 'A';
UPDATE accounts SET balance = balance + 500 WHERE acc_id = 'B';
COMMIT;
```

---

#### 5. **Properties of Transactions (ACID Properties)**

A well-formed transaction must satisfy the following:

| Property        | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| **Atomicity**   | All operations in the transaction are completed, or none are.        |
| **Consistency** | Database must move from one valid state to another.                  |
| **Isolation**   | Transactions must not interfere with each other during execution.    |
| **Durability**  | Once committed, changes made by the transaction persist permanently. |

---

#### 6. **Key Operations in a Transaction**

| Operation    | Description                                 |
| ------------ | ------------------------------------------- |
| **Read(X)**  | Read the value of data item X from database |
| **Write(X)** | Write a new value to data item X            |
| **Begin**    | Marks the start of the transaction          |
| **Commit**   | Successfully complete and save all changes  |
| **Abort**    | Cancel transaction and undo all changes     |

---

#### 7. **Importance of Transaction Concept**

* Maintains **data correctness** in presence of:

  * Concurrent access
  * System crashes
  * Logical errors
* Ensures **database reliability and robustness** in real-time applications like:

  * Banking
  * Online booking systems
  * Inventory management

---

#### 8. **Transaction Boundaries**

* **Begin** and **End** points of a transaction must be clearly defined.
* Can be **explicit** (via `BEGIN`, `COMMIT`, `ROLLBACK`) or **implicit** (autocommit mode).

---

#### 9. **Nested Transactions**

* One transaction may contain other sub-transactions.
* Used in advanced systems to allow partial work rollback.

---

#### 10. **Summary Table**

| Concept     | Description                                             |
| ----------- | ------------------------------------------------------- |
| Transaction | Logical unit of work                                    |
| ACID        | Ensures reliability and correctness                     |
| Operations  | Read, Write, Commit, Abort                              |
| Purpose     | Integrity, consistency, concurrency, and fault recovery |

---

### Transaction Processing — Detailed Explanation

---

#### 1. **Definition**

* **Transaction Processing** refers to the **execution of database transactions** in a **controlled, consistent, and reliable** manner.
* It ensures that **multiple users and operations** on a database can occur **safely and concurrently** without compromising data integrity.

---

#### 2. **Objectives of Transaction Processing**

* **Maintain ACID properties** (Atomicity, Consistency, Isolation, Durability)
* **Support multiple users** accessing the database concurrently
* **Handle failures** (e.g., crashes, power loss) gracefully
* **Ensure recovery** from incomplete or failed transactions

---

#### 3. **Transaction Processing System (TPS)**

* A **TPS** is a software component (usually part of a DBMS) that manages and controls the **execution of transactions**.
* Ensures that transactions are **executed in a serializable, recoverable, and isolated** manner.

---

#### 4. **Key Functionalities of TPS**

| Function                   | Description                                                               |
| -------------------------- | ------------------------------------------------------------------------- |
| **Concurrency Control**    | Manages simultaneous transactions to avoid data conflicts.                |
| **Logging**                | Keeps records of transaction operations for recovery.                     |
| **Recovery Management**    | Restores the database to a consistent state after failure.                |
| **Commit/Abort Handling**  | Ensures either all operations complete (commit) or none (abort/rollback). |
| **Transaction Scheduling** | Orders transactions to avoid deadlocks and maintain serializability.      |

---

#### 5. **Example: Bank Transfer Transaction**

**Transaction T1: Transfer ₹500 from A to B**

1. `Read(A)`
2. `A := A – 500`
3. `Write(A)`
4. `Read(B)`
5. `B := B + 500`
6. `Write(B)`
7. `COMMIT`

TPS ensures:

* If system crashes after step 3 → **rollback** changes to A
* If all steps succeed → **commit** permanently

---

#### 6. **Need for Transaction Processing**

* **Consistency**: Ensures DB constraints are not violated.
* **Atomicity**: All steps of a transaction execute, or none do.
* **Isolation**: Prevents interference from concurrent transactions.
* **Durability**: Committed data remains intact even after failure.

---

#### 7. **Concurrency in TPS**

* Transactions may run **simultaneously**, leading to:

  * **Lost updates**
  * **Temporary inconsistencies**
  * **Uncommitted data read (dirty reads)**
* TPS uses concurrency control (e.g., locking, timestamping) to prevent these.

---

#### 8. **Recovery in TPS**

* Uses **logs and checkpoints** to restore the database after a crash.
* Ensures:

  * **Committed changes** are not lost.
  * **Incomplete transactions** are undone.

---

#### 9. **Modes of Transaction Processing**

| Mode                     | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| **Single-user**          | One transaction at a time. No concurrency issues.                  |
| **Multi-user**           | Many users. Requires concurrency control and isolation mechanisms. |
| **Batch Processing**     | Processes large number of transactions at once.                    |
| **Real-time Processing** | Immediate response required (e.g., online banking, reservations).  |

---

#### 10. **Summary Table**

| Concept                | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| Transaction Processing | Execution & management of transactions               |
| TPS                    | Component managing transactions in DBMS              |
| Main Functions         | Logging, concurrency control, recovery, commit/abort |
| Goal                   | Ensure safe, consistent, and reliable data updates   |

---

### System — Detailed Explanation in Context of Transaction Processing System

---

#### 1. **Definition**

* In the context of transaction management, a **system** refers to the **software and hardware infrastructure** (usually the **DBMS** and **underlying operating system**) responsible for managing **transaction execution**, **data storage**, **recovery**, **concurrency control**, and **user interaction**.

---

#### 2. **Components of a Transaction Processing System (TPS)**

| Component                             | Description                                                             |
| ------------------------------------- | ----------------------------------------------------------------------- |
| **DBMS (Database Management System)** | Manages data, handles transactions, ensures ACID properties             |
| **Transaction Manager**               | Coordinates execution of transactions; enforces atomicity and isolation |
| **Concurrency Control Manager**       | Ensures correct execution of concurrent transactions                    |
| **Recovery Manager**                  | Restores consistent database state after failures                       |
| **Buffer Manager**                    | Manages in-memory data buffers and interaction with disk storage        |
| **Log Manager**                       | Maintains logs for all write actions to enable recovery                 |
| **Scheduler**                         | Orders execution of operations to ensure serializability                |

---

#### 3. **Role of the System in Transaction Processing**

##### a) **Start and Track Transactions**

* Assigns unique transaction ID
* Monitors execution until commit or abort

##### b) **Maintain Data Consistency**

* Verifies operations do not violate integrity constraints

##### c) **Enforce Concurrency Control**

* Uses locking, timestamp ordering, or multiversion techniques to manage multiple users

##### d) **Handle Failures**

* Detects crashes, power failures, or logical errors
* Uses log-based recovery to restore previous consistent state

##### e) **Ensure Durability**

* Uses stable storage (e.g., hard disk or SSD) and write-ahead logs to protect committed changes

---

#### 4. **System Architecture for Transaction Management**

```plaintext
        +---------------------+
        |   Application/User  |
        +---------------------+
                   ↓
        +---------------------+
        |   Transaction Manager|
        +---------------------+
         ↓          ↓         ↓
     Lock Mgr   Recovery Mgr  Scheduler
         ↓          ↓         ↓
     +--------------------------------+
     |        Storage Manager          |
     +--------------------------------+
                ↓
        +-----------------+
        |   Data Storage   |
        +-----------------+
```

---

#### 5. **Types of Systems**

| Type                   | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| **Single-user system** | Only one user interacts with the database at a time.       |
| **Multi-user system**  | Many users; system must manage concurrency and isolation.  |
| **Centralized system** | All processing happens on one machine.                     |
| **Distributed system** | Data and transactions are spread across multiple machines. |

---

#### 6. **Responsibilities of the System**

| Task                    | How it's Handled                                               |
| ----------------------- | -------------------------------------------------------------- |
| Begin/End Transaction   | Transaction manager tracks status                              |
| Concurrency Control     | Scheduler & lock/timestamp mechanisms                          |
| Logging and Recovery    | Log manager & recovery manager using Write-Ahead Logging (WAL) |
| Data Access and Storage | Buffer manager & storage manager                               |
| Failure Handling        | Checkpoints, redo/undo mechanisms                              |

---

#### 7. **Key System Tables and Structures**

| Structure             | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| **Transaction Table** | Tracks active transactions and their states          |
| **Log File**          | Records all operations for recovery                  |
| **Lock Table**        | Tracks current locks on data items                   |
| **Buffer Pool**       | Temporary memory holding disk blocks for fast access |

---

#### 8. **Summary Table**

| Concept       | Description                                                |
| ------------- | ---------------------------------------------------------- |
| System        | Full environment managing transaction execution            |
| Components    | Transaction mgr, concurrency mgr, recovery mgr, log mgr    |
| Functions     | Execute, control, recover transactions, maintain integrity |
| Architectures | Single-user, multi-user, centralized, distributed          |

---

### Transaction Processing vs System — Detailed Comparison

| **Aspect**                 | **Transaction Processing**                                                                | **System**                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Definition**             | The **execution and management** of transactions to ensure correct and reliable outcomes. | The **entire infrastructure** (hardware + software) responsible for handling transactions. |
| **Focus**                  | Logical and procedural handling of **individual transactions**.                           | Architectural and structural setup to **support transaction processing**.                  |
| **Functionality**          | - Enforces ACID properties<br>- Manages commit/abort<br>- Handles concurrent execution    | - Provides tools (e.g., DBMS components) to **implement and manage** transactions          |
| **Scope**                  | Narrow — deals with **how** a transaction is processed.                                   | Broad — encompasses the **entire environment** supporting transaction execution.           |
| **Main Activities**        | - Read/Write operations<br>- Begin, Commit, Abort<br>- Recovery on failure                | - Managing logs, buffers, locks, concurrency control, scheduling, and recovery mechanisms  |
| **Core Component**         | **Transaction Manager**                                                                   | **DBMS and OS** working together to provide a stable execution environment                 |
| **Concerned With**         | Logical correctness, isolation, durability of each transaction                            | Managing hardware resources, memory, disk, logs, concurrency, users                        |
| **Failure Handling**       | Handles **rollback/abort** of transactions                                                | Provides **recovery tools** like log manager, checkpoint, recovery manager                 |
| **Concurrency Control**    | Ensures one transaction doesn’t interfere with others                                     | Implements **concurrency algorithms** (e.g., locking, timestamp ordering)                  |
| **Durability Enforcement** | Ensures changes persist once committed                                                    | Provides **stable storage**, write-ahead logging, checkpointing                            |
| **Example**                | Transferring money between accounts using read/write and commit operations                | DBMS managing memory, logging, scheduling, and crash recovery during the transaction       |
| **Primary Goal**           | Ensure **correctness and reliability** of transaction logic                               | Provide **complete support** for transaction processing and database functionality         |

---

### Summary Table

| **Feature**     | **Transaction Processing**                             | **System**                                        |
| --------------- | ------------------------------------------------------ | ------------------------------------------------- |
| Unit of Work    | A **transaction**                                      | Multiple transactions                             |
| Primary Element | Logical steps and control flow of a transaction        | Infrastructure and supporting components          |
| Focus           | **Execution correctness**                              | **Execution support**                             |
| Handled by      | Transaction Manager                                    | DBMS and underlying OS components                 |
| Controls        | Read, write, commit, abort, recovery for a transaction | Locking, buffering, logging, scheduling, recovery |

---

**Conclusion:**

* **Transaction Processing** is the **process** of executing transactions.
* **System** is the **framework** (software/hardware) that **enables and manages** this process.

---

### Transaction Concept — Detailed Explanation

---

#### 1. **Definition of Transaction**

* A **transaction** is a **sequence of one or more database operations** (such as read, write, update, or delete) that form a **logical unit of work**.
* The entire sequence must be **executed completely or not at all**, maintaining the **integrity of the database**.

---

#### 2. **Key Characteristics**

* A transaction:

  * Groups **multiple operations** into a single unit.
  * Must ensure the **ACID properties**.
  * Is **atomic** — either **all operations succeed** or **none** do.
  * Is **isolated** — other transactions cannot see intermediate states.

---

#### 3. **Purpose**

* Maintain **data consistency**.
* Enable **multi-user access** without interference.
* Allow **system recovery** after failure.
* Protect the database against **errors or crashes** during operations.

---

#### 4. **ACID Properties (Essential for Transactions)**

| Property        | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| **Atomicity**   | All operations in a transaction are treated as a single unit — **all or none**.       |
| **Consistency** | Transaction takes the database from one **valid state to another** valid state.       |
| **Isolation**   | Transactions appear to run **independently** from one another.                        |
| **Durability**  | Once a transaction commits, its results are **permanently recorded** in the database. |

---

#### 5. **Example**

**Bank Transaction:** Transfer ₹500 from Account A to Account B.

Operations:

1. Read(A)
2. A = A – 500
3. Write(A)
4. Read(B)
5. B = B + 500
6. Write(B)

→ These steps must execute as **one transaction**.
→ If a crash happens after step 3, the system **rolls back** the transaction.

---

#### 6. **Transaction Operations**

| Operation    | Description                                 |
| ------------ | ------------------------------------------- |
| **Begin**    | Starts a new transaction                    |
| **Read(X)**  | Reads value of data item `X`                |
| **Write(X)** | Writes new value to data item `X`           |
| **Commit**   | Saves all changes made by the transaction   |
| **Abort**    | Undoes all operations if any failure occurs |

---

#### 7. **Transaction Boundaries**

| Boundary              | Description                                              |
| --------------------- | -------------------------------------------------------- |
| **Begin Transaction** | Marks the start of a transaction                         |
| **End Transaction**   | Marks either **commit** (success) or **abort** (failure) |

---

#### 8. **Nested Transactions**

* A transaction can **contain sub-transactions**.
* Useful in modular applications.
* Sub-transactions may commit independently but the parent controls the final result.

---

#### 9. **Use Cases**

* Banking systems
* Airline and railway reservations
* Online shopping carts
* Inventory management systems
* Any application that performs **multiple data operations together**

---

#### 10. **Summary Table**

| Term               | Description                                        |
| ------------------ | -------------------------------------------------- |
| Transaction        | Logical sequence of operations treated as one unit |
| ACID               | Atomicity, Consistency, Isolation, Durability      |
| Begin/Commit/Abort | Start, complete, or rollback a transaction         |
| Role               | Ensures reliable and consistent data operations    |

---

### A Simple Transaction Model — Detailed Explanation

---

#### 1. **Definition**

* A **Simple Transaction Model** defines the **internal structure and behavior** of a transaction in terms of its **read/write operations**, **states**, and **interaction** with the database.
* It represents the **abstract execution** of a transaction in a DBMS.

---

#### 2. **Basic Components of the Model**

| Component     | Description                                              |
| ------------- | -------------------------------------------------------- |
| **Read(X)**   | Reads the value of data item `X` from the database.      |
| **Write(X)**  | Writes a new value to data item `X` into the database.   |
| **Begin(T)**  | Marks the start of transaction `T`.                      |
| **Commit(T)** | Finalizes and saves all changes made by transaction `T`. |
| **Abort(T)**  | Cancels transaction `T` and rolls back all its changes.  |

---

#### 3. **Internal View of a Transaction**

Each transaction is viewed as a **sequence of operations**:

```text
BEGIN
  READ(X)
  X := X - 100
  WRITE(X)
  READ(Y)
  Y := Y + 100
  WRITE(Y)
COMMIT
```

> Example: Transfer ₹100 from Account X to Account Y.

---

#### 4. **Transaction States in the Model**

| **State**               | **Description**                                                        |
| ----------------------- | ---------------------------------------------------------------------- |
| **Active**              | Transaction is executing its operations (read, write, computation).    |
| **Partially Committed** | Last statement (e.g., commit) has been issued, but not yet finalized.  |
| **Committed**           | All effects of the transaction are permanently stored in the database. |
| **Failed**              | An error occurred; transaction must be rolled back.                    |
| **Aborted**             | All changes by the transaction are undone; DB state is restored.       |

---

#### 5. **Transaction Model with States Diagram**

```plaintext
       +--------+
       | Active |
       +--------+
           |
           v
+--------------------+
| Partially Committed |
+--------------------+
     |         |
     v         v
+--------+   +--------+
|Committed| |  Failed |
+--------+   +--------+
                   |
                   v
              +--------+
              | Aborted|
              +--------+
```

---

#### 6. **Assumptions in the Model**

* Transactions operate on **logical data items** (tuples, rows).
* The model abstracts **low-level storage details** (e.g., blocks, pages).
* Operations are assumed to be **serializable** unless otherwise specified.

---

#### 7. **Transaction Execution Example**

Transaction T1 (transfer ₹500 from A to B):

```
Begin(T1)
Read(A)
A := A - 500
Write(A)
Read(B)
B := B + 500
Write(B)
Commit(T1)
```

If system crashes after `Write(A)`, the transaction enters **Failed** state → moves to **Aborted** → rolls back `Write(A)`.

---

#### 8. **Advantages of the Simple Transaction Model**

* Simplifies understanding of **transaction logic**.
* Helps in **designing concurrency control and recovery mechanisms**.
* Provides a **standard execution structure** for various DBMSs.

---

#### 9. **Limitations**

* Doesn’t include **concurrent execution** by default (handled in advanced models).
* Assumes **atomicity** and **deterministic outcomes** for each operation.

---

#### 10. **Summary Table**

| Element              | Description                                             |
| -------------------- | ------------------------------------------------------- |
| Read(X), Write(X)    | Basic data access operations                            |
| Begin, Commit, Abort | Transaction lifecycle control commands                  |
| Transaction States   | Active, Partially Committed, Committed, Failed, Aborted |
| Use                  | Foundation for concurrency, recovery, and isolation     |

---

### Storage Structure (T2) — Detailed Explanation

---

#### 1. **Definition**

* **Storage structure** refers to the **hierarchical organization of memory and storage** in a database system.
* It defines **where and how data is stored**, accessed, and managed within different layers of memory and storage devices.

---

#### 2. **Goals of Storage Structure**

* Provide **efficient access** to data.
* Ensure **durability** and **reliability** of stored data.
* Support **fast recovery** after failures.
* Allow **scalability** for large datasets.

---

#### 3. **Types of Storage in a DBMS**

| Type of Storage          | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **Primary Storage**      | Main memory (RAM); volatile; holds intermediate data & buffers.       |
| **Secondary Storage**    | Non-volatile storage like hard disks; holds permanent database files. |
| **Tertiary Storage**     | Removable devices (e.g., tapes, optical disks); used for backups.     |
| **Volatile Storage**     | Loses content on power failure (e.g., RAM).                           |
| **Non-Volatile Storage** | Retains data even after power loss (e.g., HDD, SSD).                  |

---

#### 4. **Storage Hierarchy in a DBMS**

```plaintext
            [Fastest]         CPU Cache
                              ↓
                              RAM (Main Memory)
                              ↓
                              SSD / HDD (Disk Storage)
                              ↓
            [Slowest]         Tape / Cloud Archival Storage
```

* **Faster** = Lower capacity, higher cost.
* **Slower** = Higher capacity, lower cost.
* DBMS moves data between these layers using **buffer management**.

---

#### 5. **Database Storage Components**

| Component                 | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| **Data files**            | Store actual database tables, indexes, and metadata.             |
| **Redo/Write-Ahead Logs** | Store changes for recovery before they’re applied to data files. |
| **Undo Logs**             | Store old values to allow rollback of uncommitted transactions.  |
| **System Catalog**        | Stores metadata about tables, columns, indexes, users, etc.      |
| **Temporary Files**       | Store intermediate results during query processing.              |

---

#### 6. **Buffer Management**

* Buffers are pages of data **loaded into RAM** from disk.
* **Buffer Manager** handles:

  * **Loading pages** into memory when needed.
  * **Evicting** old pages (using replacement policies like LRU).
  * **Dirty page tracking** (modified pages that need to be flushed to disk).

---

#### 7. **Page and Block Concept**

| Term      | Description                                                     |
| --------- | --------------------------------------------------------------- |
| **Block** | Unit of data transfer between disk and main memory (e.g., 4KB). |
| **Page**  | Logical block of data used internally by the DBMS.              |

* All read/write operations happen **at block/page level**.
* Efficient page design reduces I/O overhead.

---

#### 8. **Storage Models in Databases**

| Model               | Description                                             |
| ------------------- | ------------------------------------------------------- |
| **Row-Oriented**    | Stores data row by row (good for OLTP systems).         |
| **Column-Oriented** | Stores data column by column (good for OLAP/analytics). |
| **Hybrid Storage**  | Combines both models depending on workload.             |

---

#### 9. **Mapping between Logical and Physical Storage**

| Level        | Example                   | Description                          |
| ------------ | ------------------------- | ------------------------------------ |
| **Logical**  | Table name, column names  | What users and queries interact with |
| **Physical** | Disk blocks, file offsets | How the data is stored internally    |

* DBMS translates **logical access to physical storage** via **file and buffer managers**.

---

#### 10. **Storage Structure Summary Table**

| Category           | Example Components           | Characteristics                                |
| ------------------ | ---------------------------- | ---------------------------------------------- |
| **Volatile**       | RAM, Cache                   | Fast, temporary, data lost on crash            |
| **Non-Volatile**   | HDD, SSD, Tape               | Persistent, slower, used for main DB storage   |
| **Database Files** | Data files, logs, temp files | Used by DBMS to manage transactions/data       |
| **Buffer Manager** | RAM pages, dirty bits        | Manages in-memory access to disk-resident data |
| **Page/Block**     | 4KB disk block               | Unit of storage and I/O                        |

---

### Introduction to Transaction Processing — Detailed Explanation

---

#### 1. **Definition**

* **Transaction Processing** is the technique used by **Database Management Systems (DBMS)** to **manage the execution** of database transactions in a way that ensures **correctness**, **consistency**, **isolation**, and **durability**.
* It allows **multiple users** to access and manipulate data **concurrently** while maintaining **data integrity**.

---

#### 2. **Objectives of Transaction Processing**

* Enforce **ACID properties** (Atomicity, Consistency, Isolation, Durability).
* Handle **multiple concurrent transactions** safely.
* Ensure **system recovery** after failure.
* Prevent **data corruption** due to errors or crashes.

---

#### 3. **Need for Transaction Processing**

| Scenario                         | Risk Without Transaction Processing                          |
| -------------------------------- | ------------------------------------------------------------ |
| **Concurrent Users**             | Conflicting data access, lost updates                        |
| **System Crash**                 | Incomplete transactions leave database in inconsistent state |
| **Hardware/Software Failures**   | Permanent data loss                                          |
| **User Errors or Interruptions** | Inconsistent data states due to partial execution            |

---

#### 4. **Key Concepts in Transaction Processing**

| Concept         | Description                                                              |
| --------------- | ------------------------------------------------------------------------ |
| **Transaction** | Logical unit of work consisting of DB operations                         |
| **Commit**      | Make all changes by a transaction permanent                              |
| **Abort**       | Cancel a transaction and undo all its changes                            |
| **Rollback**    | Undo operations of an uncommitted transaction                            |
| **Schedule**    | Sequence in which operations of multiple transactions are executed       |
| **Concurrency** | Ability of DBMS to allow multiple transactions to occur at the same time |
| **Recovery**    | Restore database to consistent state after a failure                     |

---

#### 5. **Types of Transaction Processing Systems**

| Type                   | Description                                                                       |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Single-user system** | Only one transaction runs at a time. No concurrency needed.                       |
| **Multi-user system**  | Multiple users can initiate transactions concurrently. Needs concurrency control. |
| **Real-time system**   | Immediate processing is required. Example: ATM withdrawal, flight booking         |
| **Batch system**       | Transactions processed in groups, not in real-time                                |

---

#### 6. **Single-User vs Multi-User Systems**

| Aspect          | Single-User System                   | Multi-User System                 |
| --------------- | ------------------------------------ | --------------------------------- |
| **Concurrency** | Not required                         | Required to avoid conflicts       |
| **Complexity**  | Low                                  | High due to simultaneous access   |
| **Example**     | Desktop personal accounting software | Online banking system, e-commerce |

---

#### 7. **Why Concurrency Control Is Needed**

* **Prevent anomalies** such as:

  * **Lost Update**: Two users update the same data item simultaneously.
  * **Temporary Inconsistency**: One transaction sees intermediate results of another.
  * **Uncommitted Data Read (Dirty Read)**: A transaction reads data written by another uncommitted transaction.
* Maintain **isolation** between transactions.

---

#### 8. **Why Recovery Is Needed**

* To restore database to **last consistent state** in case of:

  * **System crash** (e.g., power failure)
  * **Transaction abort**
  * **Disk failure**
* Involves techniques like:

  * **Write-ahead logging (WAL)**
  * **Checkpointing**
  * **Undo and Redo operations**

---

#### 9. **Transaction Life Cycle**

```plaintext
   Begin → Execute → Commit / Abort
         ↘ (Crash) ↘  (Rollback if needed)
```

---

#### 10. **Summary Table**

| Feature             | Description                                          |
| ------------------- | ---------------------------------------------------- |
| Transaction         | Unit of work that must follow ACID rules             |
| Concurrency Control | Ensures correct execution in multi-user systems      |
| Recovery Mechanism  | Handles failures and crashes using logs, checkpoints |
| Processing Types    | Single-user, Multi-user, Batch, Real-time            |
| Commit/Abort        | Finalize or cancel a transaction                     |

---
### Single-User System — Detailed Explanation

---

#### 1. **Definition**

* A **Single-User System** is a database environment where **only one user** can access and interact with the database at any given time.
* Only **one transaction is active** during execution; no other user or transaction can interfere.

---

#### 2. **Characteristics**

| Feature                   | Description                                                           |
| ------------------------- | --------------------------------------------------------------------- |
| **User Access**           | Only one user at a time.                                              |
| **Transaction Execution** | Transactions are executed **sequentially**.                           |
| **No Concurrency**        | No simultaneous transactions, so **no need for concurrency control**. |
| **Simple Design**         | Easier to implement and maintain due to lack of parallelism.          |
| **Lower Resource Usage**  | Requires less memory and processing power.                            |

---

#### 3. **Advantages**

| Advantage               | Explanation                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Simplicity**          | No need to handle conflicts, deadlocks, or isolation problems.             |
| **Speed (in low load)** | Fast execution for a single user, as no overhead from concurrency control. |
| **Cost-effective**      | Lower resource usage, ideal for small applications.                        |

---

#### 4. **Disadvantages**

| Disadvantage          | Explanation                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| **Not scalable**      | Cannot support multiple users simultaneously.                                 |
| **Idle resources**    | Hardware resources underutilized during idle periods.                         |
| **No parallelism**    | Can’t benefit from modern multicore CPUs or parallel I/O.                     |
| **Limited usability** | Not suitable for real-time or enterprise systems requiring multi-user access. |

---

#### 5. **Example Use Cases**

| Application                                  | Description                                                      |
| -------------------------------------------- | ---------------------------------------------------------------- |
| **Personal accounting software**             | User keeps records of income/expenses locally                    |
| **Standalone desktop databases**             | Small databases for personal inventory or notes                  |
| **Offline DB tools for development/testing** | Used by developers when building/testing without multi-user need |

---

#### 6. **Transaction Behavior in Single-User System**

* Transactions are **executed one after another**.
* No issues like:

  * Lost updates
  * Dirty reads
  * Non-repeatable reads
  * Deadlocks

> As only one transaction runs at a time, there is **no interference** or need for complex control mechanisms.

---

#### 7. **Architecture (Simplified)**

```plaintext
     [User/Application]
            ↓
     [DBMS Engine]
            ↓
     [Disk Storage / Files]
```

* No concurrency manager or lock manager is needed.

---

#### 8. **Comparison with Multi-User System**

| Feature             | Single-User System             | Multi-User System                      |
| ------------------- | ------------------------------ | -------------------------------------- |
| Concurrency Control | Not needed                     | Essential                              |
| Performance         | High (for one user)            | Shared resources among users           |
| Scalability         | Low                            | High                                   |
| Complexity          | Low                            | High (locking, scheduling, recovery)   |
| Suitability         | Personal or small applications | Large-scale, real-time, online systems |

---

#### 9. **When to Use**

* When **only one user** interacts with the database.
* In **embedded systems**, local DBs, or **testing environments**.
* Where **simplicity and minimal resource use** is more important than scalability.

---

#### 10. **Summary Table**

| Concept             | Details                                      |
| ------------------- | -------------------------------------------- |
| User Support        | One user at a time                           |
| Concurrency Control | Not required                                 |
| Ideal For           | Local apps, personal use, development        |
| Example             | Personal accounting, desktop DB tools        |
| Major Limitation    | Cannot handle concurrent users or scale well |

---

### Single-User vs Multi-User Systems — Detailed Comparison

---

#### 1. **Definition**

| Type                   | Description                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| **Single-User System** | A database environment where only **one user** can access and interact with the DB at a time. |
| **Multi-User System**  | A system that allows **multiple users** to access and execute transactions **concurrently**.  |

---

#### 2. **Key Differences**

| Aspect                       | **Single-User System**                             | **Multi-User System**                                        |
| ---------------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| **User Access**              | Only one user at a time                            | Multiple users simultaneously                                |
| **Concurrency**              | Not supported                                      | Supported and managed using concurrency control              |
| **Complexity**               | Simple architecture                                | Complex due to handling of concurrency, isolation, deadlocks |
| **Resource Utilization**     | Low (often underutilized hardware)                 | Efficient use of CPU, memory, and disk resources             |
| **Transaction Control**      | No risk of conflict, no locking needed             | Requires locking, timestamps, or MVCC to manage conflicts    |
| **Data Consistency Control** | Handled easily due to isolated access              | Needs concurrency control to maintain consistency            |
| **Deadlock Possibility**     | None                                               | Possible, must be detected and resolved                      |
| **Failure Recovery**         | Simple recovery mechanisms                         | Complex recovery using logging, checkpoints, and undo/redo   |
| **Performance**              | Fast for one user                                  | Scalable with increased users and optimized access           |
| **Scalability**              | Poor (not suitable for large or real-time systems) | High (supports growing user and transaction load)            |

---

#### 3. **Architecture**

**Single-User System:**

```plaintext
User/Application → DBMS → Disk Storage
```

**Multi-User System:**

```plaintext
Users → Transaction Manager → Scheduler + Lock Manager → Storage + Log Manager
```

---

#### 4. **Examples**

| Application Type         | Single-User System                  | Multi-User System                              |
| ------------------------ | ----------------------------------- | ---------------------------------------------- |
| **Accounting Software**  | Personal finance tracking tools     | Enterprise accounting system (e.g., Tally ERP) |
| **Educational Use**      | Student using local DB for practice | University database system with many users     |
| **Development/Testing**  | Developer testing SQL queries       | Web-based application used by many clients     |
| **Inventory Management** | Offline local shop management       | Real-time supply chain system                  |

---

#### 5. **Concurrency Problems in Multi-User Systems**

Multi-user systems must address:

* **Lost Update Problem**
* **Dirty Read Problem**
* **Non-repeatable Reads**
* **Phantom Reads**
* **Deadlocks**

Managed using:

* **Locks**
* **Timestamp ordering**
* **Multiversion concurrency control (MVCC)**

---

#### 6. **Recovery Complexity**

| System Type     | Recovery Requirement                                     |
| --------------- | -------------------------------------------------------- |
| **Single-User** | Simple undo/redo, limited failure scope                  |
| **Multi-User**  | Advanced logging, checkpointing, and recovery mechanisms |

---

#### 7. **Suitability**

| Type                   | Suitable For                                                |
| ---------------------- | ----------------------------------------------------------- |
| **Single-User System** | Personal, embedded, local or offline use                    |
| **Multi-User System**  | Online applications, real-time systems, enterprise software |

---

#### 8. **Summary Table**

| Feature                    | Single-User System | Multi-User System           |
| -------------------------- | ------------------ | --------------------------- |
| Number of Users            | One                | Many                        |
| Concurrency Control        | Not required       | Essential                   |
| Architecture               | Simple             | Complex                     |
| Resource Usage             | Low                | High                        |
| Data Consistency Challenge | Minimal            | Significant                 |
| Example Applications       | Personal DB tools  | Online banking, ERP systems |

---

### Why Concurrency Control is Needed — Detailed Explanation

---

#### 1. **Definition of Concurrency Control**

* **Concurrency control** is the **management of simultaneous operations** (transactions) on the database to **ensure consistency, correctness, and isolation**.
* It ensures that the **execution of concurrent transactions** does **not result in data anomalies or violations of database integrity**.

---

#### 2. **Purpose**

* Prevent **conflicting operations** from different transactions that **access or modify the same data items** simultaneously.
* Ensure that the **final database state is the same** as if the transactions were executed **serially (one after another)**.

---

#### 3. **Main Goals of Concurrency Control**

| Goal                | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **Consistency**     | Maintain integrity and constraints of the database                      |
| **Isolation**       | Transactions should not interfere with each other                       |
| **Serializability** | Ensure that concurrent execution is equivalent to some serial execution |
| **Recoverability**  | Ensure that committed transactions do not depend on aborted ones        |

---

#### 4. **Problems Without Concurrency Control**

| Problem                   | Description                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Lost Update**           | Two transactions read the same data and both update it, but only one update is saved.                         |
| **Dirty Read**            | A transaction reads data written by another transaction that has not yet committed.                           |
| **Non-repeatable Read**   | A transaction reads the same data item twice and gets different values due to an intervening update.          |
| **Phantom Read**          | A transaction re-executes a query and sees additional rows due to another committed transaction.              |
| **Inconsistent Analysis** | A transaction reads several data items that are being modified concurrently, leading to inconsistent results. |

---

#### 5. **Example Scenarios**

**a) Lost Update Problem**

* T1 reads balance = ₹1000
* T2 reads balance = ₹1000
* T1 subtracts ₹100 and writes ₹900
* T2 subtracts ₹200 and writes ₹800 → **T1's update is lost**

**b) Dirty Read Problem**

* T1 updates salary to ₹5000 but hasn't committed
* T2 reads salary = ₹5000
* T1 rolls back → T2 read invalid data

**c) Non-repeatable Read Problem**

* T1 reads balance of A = ₹1000
* T2 updates A to ₹800 and commits
* T1 reads balance of A again = ₹800 → different result

---

#### 6. **Concurrency Control Techniques**

| Technique                                   | Description                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------ |
| **Lock-based Protocols**                    | Transactions acquire locks on data items (shared/exclusive)                    |
| **Timestamp-based Protocols**               | Transactions ordered by timestamps; operations are validated against the order |
| **Optimistic Concurrency Control**          | Transactions proceed without locking and validate before committing            |
| **Multiversion Concurrency Control (MVCC)** | Maintains multiple versions of data to allow concurrent reads/writes           |

---

#### 7. **Isolation Levels (Defined in SQL)**

| Level                | Problem Allowed                     |
| -------------------- | ----------------------------------- |
| **Read Uncommitted** | Dirty Read, Non-repeatable, Phantom |
| **Read Committed**   | Non-repeatable, Phantom             |
| **Repeatable Read**  | Phantom                             |
| **Serializable**     | None (Fully isolated)               |

---

#### 8. **Consequences Without Concurrency Control**

| Consequence                 | Explanation                                                |
| --------------------------- | ---------------------------------------------------------- |
| **Data Inconsistency**      | Conflicting updates lead to incorrect or inconsistent data |
| **Unpredictable Results**   | Results of queries and updates vary due to interference    |
| **Violations of Integrity** | May violate business or relational constraints             |
| **Loss of Atomicity**       | Transactions may appear partially executed                 |
| **Cascading Rollbacks**     | Failure of one transaction forces others to roll back      |

---

#### 9. **Concurrency Control Ensures:**

| Guarantee           | Meaning                                                   |
| ------------------- | --------------------------------------------------------- |
| **Serializability** | Concurrent schedule is equivalent to some serial schedule |
| **Recoverability**  | No transaction commits based on uncommitted data          |
| **Isolation**       | Intermediate states are hidden from other transactions    |

---

#### 10. **Summary Table**

| Feature             | Description                                  |
| ------------------- | -------------------------------------------- |
| Concurrency Control | Manages simultaneous transaction execution   |
| Needed For          | Data integrity, isolation, serializability   |
| Prevents Problems   | Lost update, dirty read, non-repeatable read |
| Techniques          | Locks, timestamps, MVCC, optimistic methods  |
| Without It          | Inconsistent, incorrect, or lost data        |

---

### Why Recovery Is Needed — Detailed Explanation

---

#### 1. **Definition of Recovery**

* **Recovery** in a DBMS refers to the process of **restoring the database** to a **consistent state** after a **failure** (system crash, power loss, transaction error, etc.).
* It ensures that all **committed transactions persist**, and all **uncommitted or failed transactions are rolled back**.

---

#### 2. **Purpose of Recovery**

| Objective                     | Explanation                                                              |
| ----------------------------- | ------------------------------------------------------------------------ |
| **Data Consistency**          | Ensure database remains in a valid, consistent state after a failure.    |
| **Durability (ACID)**         | Guarantee that committed transactions survive crashes.                   |
| **Rollback Uncommitted Work** | Undo effects of incomplete or failed transactions.                       |
| **System Reliability**        | Provide trust in the database system’s ability to recover from failures. |

---

#### 3. **Types of Failures That Require Recovery**

| Failure Type            | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| **Transaction Failure** | Logical or input errors causing a transaction to abort.            |
| **System Crash**        | Operating system, DBMS, or power failure causing interruption.     |
| **Disk Failure**        | Hardware failure causing permanent data loss on disk.              |
| **Software Failure**    | Bugs in DBMS code or application programs.                         |
| **Media Failure**       | Entire storage media becomes unreadable (e.g., head crash in HDD). |

---

#### 4. **Common Failure Scenarios**

| Scenario                                    | Effect Without Recovery                   |
| ------------------------------------------- | ----------------------------------------- |
| System crashes after a transaction commits  | Committed changes may be lost.            |
| System crashes during transaction execution | Partial writes may corrupt data.          |
| Multiple transactions running during crash  | May leave inconsistent interleaved state. |

---

#### 5. **Recovery Goals**

| Goal                    | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| **Undo uncommitted**    | Ensure that changes by incomplete transactions are rolled back.              |
| **Redo committed**      | Ensure committed changes are re-applied if not written to disk before crash. |
| **Restore consistency** | Bring the DB back to the last known consistent state.                        |

---

#### 6. **Recovery Techniques in DBMS**

| Technique                     | Description                                                           |
| ----------------------------- | --------------------------------------------------------------------- |
| **Write-Ahead Logging (WAL)** | Log changes before applying them to the database (ensures atomicity). |
| **Checkpointing**             | Periodically save DB state to reduce recovery time.                   |
| **Undo/Redo Logs**            | Undo uncommitted changes, redo committed ones after recovery.         |
| **Shadow Paging**             | Maintain a shadow copy of pages to allow rollback on crash.           |

---

#### 7. **Write-Ahead Logging (WAL)**

* **Before** a data item is updated, the **log is written first**.
* Ensures that:

  * Changes can be **redone** if transaction was committed.
  * Changes can be **undone** if transaction was aborted or system crashed.

---

#### 8. **Transaction States and Recovery Actions**

| Transaction State                         | Recovery Action                                  |
| ----------------------------------------- | ------------------------------------------------ |
| **Committed**                             | **Redo** all operations to ensure durability.    |
| **Active / Partially committed / Failed** | **Undo** all operations to maintain consistency. |

---

#### 9. **Importance of Recovery in Multi-User Systems**

| Feature                 | Without Recovery                              | With Recovery                       |
| ----------------------- | --------------------------------------------- | ----------------------------------- |
| **Data Safety**         | Committed data may be lost                    | Preserves durability                |
| **System Trust**        | Users cannot trust DB after crash             | Users trust DB to recover correctly |
| **Concurrency Support** | Incomplete rollback causes cascading failures | Proper isolation maintained         |

---

#### 10. **Summary Table**

| Concept               | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| Recovery              | Process of restoring DB to consistent state after failure           |
| Needed Because        | Hardware/software failures, crashes, power loss, transaction errors |
| Main Goals            | Undo uncommitted changes, redo committed ones                       |
| Core Techniques       | WAL, checkpointing, undo/redo, shadow paging                        |
| Ensures ACID Property | Maintains **Atomicity** and **Durability** in case of failure       |

---

### Transaction — Detailed Explanation

---

#### 1. **Definition**

* A **transaction** is a **logical unit of work** in a database that comprises a sequence of operations (like read, write, update, delete) performed as a **single, indivisible unit**.
* A transaction must be **executed fully or not at all**, maintaining the **integrity and consistency** of the database.

---

#### 2. **Purpose**

* Maintain the **correctness of the database** even in the presence of failures.
* Support **concurrent access** while ensuring isolation and consistency.
* Allow for **recovery** by defining clear **commit** or **abort** points.

---

#### 3. **Examples of Transactions**

| Example             | Operations Involved                                |
| ------------------- | -------------------------------------------------- |
| Bank transfer       | Debit account A, credit account B                  |
| Online purchase     | Update inventory, generate invoice, record payment |
| Railway reservation | Reserve seat, update availability, generate ticket |

---

#### 4. **Operations in a Transaction**

| Operation    | Description                                                |
| ------------ | ---------------------------------------------------------- |
| **Read(X)**  | Reads the value of data item `X`.                          |
| **Write(X)** | Writes a new value to data item `X`.                       |
| **Begin**    | Starts a new transaction.                                  |
| **Commit**   | Saves all the changes made by the transaction permanently. |
| **Abort**    | Cancels the transaction and rolls back any changes made.   |

---

#### 5. **ACID Properties**

| Property        | Description                                                              |
| --------------- | ------------------------------------------------------------------------ |
| **Atomicity**   | All operations of a transaction either complete successfully or none do. |
| **Consistency** | A transaction takes the database from one valid state to another.        |
| **Isolation**   | Each transaction appears to execute independently of other transactions. |
| **Durability**  | Once committed, the changes are permanent, even if the system crashes.   |

---

#### 6. **Transaction Lifecycle**

| State                   | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| **Active**              | Transaction is executing its operations.                            |
| **Partially Committed** | Transaction has executed its final operation but not yet committed. |
| **Committed**           | Transaction has successfully completed, and all changes are saved.  |
| **Failed**              | Transaction cannot proceed due to an error or crash.                |
| **Aborted**             | Transaction is rolled back, and all effects are undone.             |

---

#### 7. **State Diagram of a Transaction**

```plaintext
    [Active]
        |
        v
[Partially Committed]
        |
  +-----+------+
  |            |
[v]         [Failed]
[Committed]     |
                v
            [Aborted]
```

---

#### 8. **Transaction Scheduling**

| Type of Schedule | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Serial**       | Transactions execute one after the other (no interleaving).  |
| **Concurrent**   | Operations of multiple transactions interleave.              |
| **Serializable** | Concurrent schedule that produces the same result as serial. |

---

#### 9. **Nested Transactions**

* A transaction may contain **sub-transactions**.
* Parent transaction commits only if all sub-transactions commit.

---

#### 10. **Summary Table**

| Concept         | Description                                             |
| --------------- | ------------------------------------------------------- |
| Transaction     | Logical unit of work on the database                    |
| Operations      | Begin, Read, Write, Commit, Abort                       |
| ACID Properties | Atomicity, Consistency, Isolation, Durability           |
| States          | Active, Partially Committed, Committed, Failed, Aborted |
| Role in DBMS    | Ensures correctness, isolation, and recovery of data    |

---

### System Concepts — Detailed Explanation

---

#### 1. **Definition**

* **System concepts** in database transaction processing refer to the **core principles and components** that govern how transactions are managed by the **DBMS (Database Management System)** to ensure correct, reliable, and concurrent execution.

---

#### 2. **Key System Concepts in Transaction Processing**

| Concept                 | Description                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| **Transaction**         | A logical unit of database work executed with ACID properties.                            |
| **Schedule**            | The order in which the operations of multiple transactions are executed.                  |
| **Serializability**     | A correctness criterion: schedule must be equivalent to some serial order.                |
| **Concurrency Control** | Mechanism to handle simultaneous transactions without conflicts.                          |
| **Recovery**            | Process of restoring database to a consistent state after failures.                       |
| **System State**        | The current configuration of the database including committed & in-progress transactions. |

---

#### 3. **Transaction States (Extended View)**

| State                   | Description                                                    |
| ----------------------- | -------------------------------------------------------------- |
| **Active**              | Transaction is executing its operations.                       |
| **Partially Committed** | Last operation is executed, ready to commit.                   |
| **Committed**           | Transaction has completed successfully; changes are permanent. |
| **Failed**              | Transaction encounters error or aborts due to failure.         |
| **Aborted**             | Changes made by the transaction are undone.                    |

---

#### 4. **State Transition Diagram**

```plaintext
[Active]
   ↓
[Partially Committed]
   ↓     ↘
[Committed] [Failed]
              ↓
          [Aborted]
```

---

#### 5. **System Log (Write-Ahead Logging - WAL)**

| Component      | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| **Log Record** | Records each database change before applying to actual data.                |
| **Undo/Redo**  | Used during recovery to roll back uncommitted or reapply committed changes. |
| **Checkpoint** | A snapshot of the database and log at a point in time to speed up recovery. |

---

#### 6. **Concurrency Control Mechanisms**

| Mechanism                                   | Description                                                             |
| ------------------------------------------- | ----------------------------------------------------------------------- |
| **Locks (Shared/Exclusive)**                | Prevent concurrent access to same data item in conflicting modes.       |
| **Timestamp Ordering**                      | Assigns timestamps to transactions to enforce serial order.             |
| **Multiversion Concurrency Control (MVCC)** | Maintains multiple versions of data to allow non-blocking reads/writes. |

---

#### 7. **Recovery Mechanisms**

| Method                  | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| **Undo (Rollback)**     | Reverses changes of failed/aborted transactions.                      |
| **Redo (Roll Forward)** | Reapplies changes of committed transactions during crash recovery.    |
| **Shadow Paging**       | Maintains a shadow copy of data pages; changes go to new page copies. |

---

#### 8. **Isolation and Schedules**

| Term                      | Description                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Schedule**              | A sequence of operation execution steps from multiple transactions.                        |
| **Serializable Schedule** | Schedule that yields same result as some serial (one-by-one) schedule.                     |
| **Recoverable Schedule**  | A schedule where transactions commit only after those whose data they read have committed. |

---

#### 9. **System Failures Handled**

| Type of Failure         | Example                                         |
| ----------------------- | ----------------------------------------------- |
| **Transaction Failure** | Syntax error, logical error in SQL transaction. |
| **System Crash**        | Power failure, OS crash.                        |
| **Disk Failure**        | Disk head crash, unreadable sector.             |

---

#### 10. **Summary Table**

| Feature                         | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| System Concepts in Transactions | Fundamental DBMS mechanisms ensuring transaction correctness          |
| Includes                        | Transactions, Schedules, Logs, Recovery, Concurrency, States          |
| Essential For                   | Reliable, concurrent, fault-tolerant DBMS operation                   |
| Core Mechanisms                 | Logging (WAL), Locking, Serializability, Undo/Redo, State transitions |

---

### Transaction vs System Concepts — Detailed Comparison

---

#### 1. **Basic Definition**

| Aspect         | **Transaction**                                                                    | **System Concepts**                                                                      |
| -------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Definition** | A **logical unit of database operations** performed together with ACID properties. | Fundamental **principles and mechanisms** for managing transactions in a DBMS.           |
| **Scope**      | Focuses on the execution and properties of a single unit of work.                  | Covers **multiple internal components** and processes that support transaction handling. |

---

#### 2. **Focus Area**

| Feature       | **Transaction**                                       | **System Concepts**                                                     |
| ------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- |
| **Execution** | Focuses on **how a unit of operations is performed**. | Focuses on **how transactions are managed and controlled** system-wide. |
| **Outcome**   | Ends with **commit or abort**.                        | Ensures **correct scheduling, recovery, and state handling**.           |
| **User View** | Appears as one consistent and isolated task.          | Encompasses **system internals like logs, concurrency, recovery, etc.** |

---

#### 3. **Core Components**

| Aspect              | **Transaction**                                         | **System Concepts**                                                                    |
| ------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Operations**      | Read, Write, Commit, Abort                              | Includes Logging, Scheduling, Locking, Recovery, Isolation Levels, State transitions   |
| **States**          | Active, Partially Committed, Committed, Failed, Aborted | Covers Transaction states + control flow, concurrency and fault-tolerance mechanisms   |
| **ACID Properties** | Defined and enforced at transaction level               | Ensured and **implemented by system-level concepts** like WAL, locks, isolation levels |

---

#### 4. **Relation Between Them**

| Feature            | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| **Dependency**     | A transaction relies on system concepts for correct execution.                    |
| **Implementation** | System concepts **implement, control, and protect** the behavior of transactions. |
| **Goal Alignment** | Both aim to **preserve data correctness, consistency, and fault tolerance**.      |

---

#### 5. **Comparison Table**

| Feature          | **Transaction**                                | **System Concepts**                                                |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| Definition       | Logical DB operation unit with ACID properties | Mechanisms for handling and managing transactions system-wide      |
| Focus            | What work is being done                        | How the system ensures that work is done correctly and safely      |
| Involves         | Read, Write, Commit, Abort                     | Schedules, Logs, Concurrency control, Recovery, Isolation          |
| State Management | Maintains transaction-specific states          | Manages transitions across all transactions and failure conditions |
| Error Handling   | Abort or rollback the current transaction      | Ensures proper system-wide recovery and rollback mechanisms        |
| Example          | Debit ₹1000 from A, credit to B                | Use logs to redo/undo the above transaction if system crashes      |

---

#### 6. **Conclusion**

| Viewpoint        | Transaction                        | System Concepts                                    |
| ---------------- | ---------------------------------- | -------------------------------------------------- |
| **User-Level**   | User-initiated logical action      | Mostly hidden from the user                        |
| **System-Level** | Relies on system to maintain rules | System ensures all transactions behave as expected |
| **Together**     | Work as a unit and a controller    | Together provide safe and reliable DB operations   |

---

### Transaction States — Detailed Explanation

---

#### 1. **Definition**

* **Transaction states** represent the **various phases** a transaction goes through during its execution in a database system.
* Helps the **DBMS track the status** of each transaction and decide the appropriate actions (e.g., commit, abort, rollback).

---

#### 2. **Main Transaction States**

| State                   | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| **Active**              | Transaction is executing its operations (read, write).           |
| **Partially Committed** | Final statement executed, but changes not yet permanently saved. |
| **Committed**           | All changes are permanently recorded in the database.            |
| **Failed**              | An error occurs; transaction cannot proceed.                     |
| **Aborted**             | Transaction is rolled back; changes are undone.                  |

---

#### 3. **State Transition Diagram**

```
[Active]
    ↓
[Partially Committed]
    ↓           ↘
[Committed]   [Failed]
                   ↓
               [Aborted]
```

---

#### 4. **Detailed Explanation of Each State**

---

**a) Active**

* Initial state when a transaction starts.
* It performs operations like:

  * **Read(X)**
  * **Write(X)**
* Stays active until:

  * All operations complete → move to **Partially Committed**
  * An error occurs → move to **Failed**

---

**b) Partially Committed**

* Transaction has completed its final statement.
* It has not yet confirmed all changes to the database.
* DBMS performs:

  * **Validation**
  * **Writing changes to log/disk**
* If successful → move to **Committed**
* If failure detected → move to **Failed**

---

**c) Committed**

* All changes made by the transaction are now **permanent**.
* Cannot be undone even after system failure.
* Logs are updated to reflect success.
* Durable as per the **Durability** property of ACID.

---

**d) Failed**

* Transaction cannot complete due to:

  * Logical error (e.g., divide by zero)
  * System crash or user interruption
* Changes may have been made but not yet committed.
* System must ensure:

  * **No changes are visible**
  * All effects are rolled back → move to **Aborted**

---

**e) Aborted**

* Transaction has been **rolled back**.
* Database is **restored to its previous consistent state**.
* DBMS may:

  * Log the failure
  * Restart the transaction if allowed
  * Discard the transaction completely

---

#### 5. **Additional Terms**

| Term             | Description                                                                  |
| ---------------- | ---------------------------------------------------------------------------- |
| **Rollback**     | Undo all changes made by a failed/aborted transaction.                       |
| **Restart**      | Some systems may attempt to re-execute an aborted transaction automatically. |
| **Commit Point** | The point at which the transaction is guaranteed to complete successfully.   |

---

#### 6. **Summary Table**

| State                   | Meaning                                         | Next State(s)                |
| ----------------------- | ----------------------------------------------- | ---------------------------- |
| **Active**              | Transaction is executing operations             | Partially Committed / Failed |
| **Partially Committed** | Final operation done, waiting for DB commit     | Committed / Failed           |
| **Committed**           | Changes made permanent, transaction successful  | Final                        |
| **Failed**              | Transaction cannot proceed                      | Aborted                      |
| **Aborted**             | Changes undone, DB restored to consistent state | Final / (Restart optionally) |

---

### Additional Operations in Transaction Processing — Detailed Explanation

---

#### 1. **Definition**

* **Additional operations** are supplementary control instructions used in transaction management to handle transaction **boundaries**, **error handling**, and **execution flow**.
* These operations provide **mechanisms to start, complete, abort, or undo/redo** actions in a transaction.

---

#### 2. **Main Additional Operations**

| Operation                 | Description                                                        |
| ------------------------- | ------------------------------------------------------------------ |
| **BEGIN / START**         | Marks the **start** of a new transaction.                          |
| **COMMIT**                | Makes **all changes permanent**; ends a successful transaction.    |
| **ROLLBACK / ABORT**      | Undoes all changes made by a transaction; used in case of failure. |
| **SAVEPOINT**             | Creates a **restore point** within a transaction.                  |
| **RELEASE SAVEPOINT**     | Deletes a previously defined savepoint.                            |
| **ROLLBACK TO SAVEPOINT** | Rolls back the transaction to a specific savepoint.                |
| **SET TRANSACTION**       | Specifies transaction properties (e.g., isolation level).          |

---

#### 3. **Detailed Explanation of Each Operation**

---

**a) BEGIN / START TRANSACTION**

* Initializes a new transaction context.
* All subsequent operations are considered part of this transaction.

```sql
BEGIN TRANSACTION;
-- or
START TRANSACTION;
```

---

**b) COMMIT**

* Finalizes a transaction.
* All changes are **saved to the database permanently**.
* Cannot be rolled back after this point.

```sql
COMMIT;
```

---

**c) ROLLBACK / ABORT**

* Terminates the transaction **unsuccessfully**.
* All changes made by the transaction are **undone**.
* Database is **restored to its state before the transaction began**.

```sql
ROLLBACK;
-- or
ABORT;
```

---

**d) SAVEPOINT**

* Creates a **named intermediate point** in the transaction.
* Useful for **partial rollback** without aborting the full transaction.

```sql
SAVEPOINT savepoint_name;
```

---

**e) ROLLBACK TO SAVEPOINT**

* Rolls back the transaction to the **specified savepoint**.
* Changes made **after** the savepoint are undone; changes **before** it are preserved.

```sql
ROLLBACK TO SAVEPOINT savepoint_name;
```

---

**f) RELEASE SAVEPOINT**

* **Deletes a savepoint**, making it unavailable for rollback.
* Does **not affect** transaction execution.

```sql
RELEASE SAVEPOINT savepoint_name;
```

---

**g) SET TRANSACTION**

* Defines **transaction behavior** such as:

  * **Isolation level** (READ COMMITTED, SERIALIZABLE, etc.)
  * **Read/write mode** (READ ONLY, READ WRITE)

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

#### 4. **Usage Example**

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT after_debit;

UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Error occurs here
ROLLBACK TO after_debit;

-- Retry or fix
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
```

---

#### 5. **Summary Table**

| Operation               | Function                                           |
| ----------------------- | -------------------------------------------------- |
| `BEGIN` / `START`       | Start a new transaction                            |
| `COMMIT`                | End transaction successfully and save changes      |
| `ROLLBACK`              | End transaction with failure and undo all changes  |
| `SAVEPOINT`             | Define intermediate rollback point                 |
| `ROLLBACK TO SAVEPOINT` | Undo to a specific savepoint, not full transaction |
| `RELEASE SAVEPOINT`     | Delete a defined savepoint                         |
| `SET TRANSACTION`       | Set properties like isolation level or access mode |

---

### Transaction States vs Additional Operations — Detailed Comparison

---

#### 1. **Basic Definition**

| Aspect         | **Transaction States**                                        | **Additional Operations**                                                                    |
| -------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Definition** | The **phases** a transaction goes through during execution.   | The **commands** or **instructions** used to control the behavior and flow of a transaction. |
| **Purpose**    | To **describe the status** of a transaction at a given point. | To **initiate, control, or terminate** a transaction.                                        |

---

#### 2. **Scope and Role**

| Feature                | **Transaction States**                             | **Additional Operations**                                           |
| ---------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| **Function**           | Track and manage **progression** of a transaction. | Perform **actions** on transactions (start, commit, abort, etc.).   |
| **System Perspective** | Internal state transitions managed by the DBMS.    | User/system-initiated commands that **trigger** or **alter** state. |
| **When Used**          | Happens **during execution** automatically.        | Issued **explicitly by user/application** or implicitly by system.  |

---

#### 3. **Key Components**

| Transaction States    | Additional Operations                                                        |
| --------------------- | ---------------------------------------------------------------------------- |
| `Active`              | `BEGIN` / `START TRANSACTION`                                                |
| `Partially Committed` | Internal phase before final `COMMIT`                                         |
| `Committed`           | `COMMIT` — completes the transaction successfully                            |
| `Failed`              | Triggered internally on error                                                |
| `Aborted`             | `ROLLBACK` / `ABORT` — undoes changes and ends the transaction               |
| *N/A*                 | `SAVEPOINT`, `ROLLBACK TO SAVEPOINT`, `RELEASE SAVEPOINT`, `SET TRANSACTION` |

---

#### 4. **State Control via Operations**

| Operation               | Affects Which State?                                                 |
| ----------------------- | -------------------------------------------------------------------- |
| `BEGIN` / `START`       | Moves transaction into the **Active** state                          |
| `COMMIT`                | Moves from **Partially Committed → Committed**                       |
| `ROLLBACK` / `ABORT`    | Moves from **Failed → Aborted**                                      |
| `SAVEPOINT`             | Defines a **sub-point** within the **Active** phase                  |
| `ROLLBACK TO SAVEPOINT` | Rolls back part of **Active** phase to an earlier stage              |
| `SET TRANSACTION`       | Sets parameters that may affect isolation behavior during **Active** |

---

#### 5. **Execution Flow with Both Concepts**

| Step                    | State                     | Operation Triggered      |
| ----------------------- | ------------------------- | ------------------------ |
| Transaction begins      | Active                    | `BEGIN`                  |
| Statements execute      | Active                    | -                        |
| Define savepoint        | Active                    | `SAVEPOINT`              |
| Execute more operations | Active                    | -                        |
| Error occurs            | Failed                    | - (System detects error) |
| User wants partial undo | Active (to earlier point) | `ROLLBACK TO SAVEPOINT`  |
| All operations succeed  | Partially Committed       | Final statement finished |
| Transaction completes   | Committed                 | `COMMIT`                 |

---

#### 6. **Analogy**

| Role                         | Transaction States                       | Additional Operations                                   |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------------- |
| Like in a **workflow**       | Represents the **status** of a task      | Represents the **buttons/actions** you press            |
| Similar to **traffic light** | Red, Yellow, Green lights showing states | Pedestrian button, timer reset = operations you trigger |

---

#### 7. **Summary Table**

| Feature      | **Transaction States**             | **Additional Operations**                           |
| ------------ | ---------------------------------- | --------------------------------------------------- |
| Concept Type | Descriptive (what is happening)    | Operational (what is being done)                    |
| Managed By   | DBMS (internally tracked)          | User or system (explicitly executed)                |
| Examples     | Active, Committed, Failed, Aborted | BEGIN, COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION |
| Used For     | Tracking progress                  | Controlling behavior and flow                       |
| Role         | Status indicator                   | Command executor                                    |

---

### Desirable Properties of Transactions — Detailed Explanation

---

#### 1. **Definition**

* Desirable properties of transactions are **essential guarantees** that ensure **correctness**, **reliability**, and **integrity** of the database even in the presence of **failures**, **concurrent executions**, and **system crashes**.
* These properties are formalized as the **ACID** properties.

---

#### 2. **ACID Properties of Transactions**

| Property        | Description                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **Atomicity**   | A transaction is **all-or-nothing**: either all its operations are executed or none.                          |
| **Consistency** | A transaction **brings the database from one valid state to another**, maintaining integrity constraints.     |
| **Isolation**   | Concurrent transactions **do not interfere** with each other; the result is the same as if executed serially. |
| **Durability**  | Once a transaction commits, its changes are **permanent**, even in the event of a system failure.             |

---

#### 3. **Atomicity (A)**

* Ensures that a **transaction's operations are treated as a single indivisible unit**.
* If any part of the transaction fails, **all changes are rolled back**.
* Achieved using:

  * **Undo logs**
  * **Transaction rollback mechanism**

**Example**:

```plaintext
Transfer ₹100 from Account A to B
Step 1: Debit ₹100 from A
Step 2: Credit ₹100 to B

If Step 2 fails → rollback Step 1 → A's balance is restored
```

---

#### 4. **Consistency (C)**

* Guarantees that a transaction transforms the database from one **consistent state to another**.
* Preserves **data integrity constraints**, such as:

  * Foreign key constraints
  * Domain constraints
  * Business rules

**Example**:

```plaintext
Total balance across all accounts must remain constant.
If ₹100 is transferred from A to B → Total remains the same.
```

---

#### 5. **Isolation (I)**

* Ensures that the **intermediate state of a transaction is not visible** to other concurrent transactions.
* Effect is **as if transactions execute serially**, even though they may run in parallel.
* Prevents problems like:

  * **Dirty reads**
  * **Non-repeatable reads**
  * **Phantom reads**

**Example**:

```plaintext
T1 reads balance from Account A
T2 updates A's balance and commits
T1 reads again → should see same value (no interference)
```

---

#### 6. **Durability (D)**

* Ensures that once a transaction **successfully commits**, its effects are **permanently recorded** in the database.
* Survives:

  * Power failure
  * System crash
* Achieved using:

  * **Write-Ahead Logging (WAL)**
  * **Checkpointing**
  * **Redo logs**

**Example**:

```plaintext
T1 updates a customer's balance and commits.
System crashes → balance is recovered from log after reboot.
```

---

#### 7. **Combined Importance of ACID**

| Property    | Prevents Issues Like                     | Ensures                                              |
| ----------- | ---------------------------------------- | ---------------------------------------------------- |
| Atomicity   | Partial updates, data corruption         | Transactions are all-or-nothing                      |
| Consistency | Integrity constraint violations          | Database remains valid before and after transactions |
| Isolation   | Concurrent interference, race conditions | Each transaction behaves independently               |
| Durability  | Loss of data after commit                | Data survives system failures                        |

---

#### 8. **Real-World Analogy**

| ACID Property   | Analogy Example                                                            |
| --------------- | -------------------------------------------------------------------------- |
| **Atomicity**   | Buying two items in a bundle — either you buy both or cancel the purchase. |
| **Consistency** | A balance sheet must always balance (Assets = Liabilities + Equity).       |
| **Isolation**   | Online orders placed simultaneously by two users must not conflict.        |
| **Durability**  | Saving a file ensures it’s on disk even after a power cut.                 |

---

#### 9. **Summary Table**

| Property    | Ensures...                              | Violations Can Lead To...                    |
| ----------- | --------------------------------------- | -------------------------------------------- |
| Atomicity   | All operations succeed or none do       | Partial changes, corrupt data                |
| Consistency | DB moves from valid to valid state      | Integrity constraints violated               |
| Isolation   | No interference from other transactions | Lost update, dirty read, non-repeatable read |
| Durability  | Data is safe after commit               | Data loss after crash                        |

---

### Concurrency Control Through Schedules — Detailed Explanation

---

#### 1. **Definition**

* **Concurrency control through schedules** refers to the **technique of organizing and managing the execution order** of operations from multiple transactions in such a way that **database consistency and isolation** are preserved.
* A **schedule** is a **sequence of operations** (read, write, commit, abort) from one or more transactions.

---

#### 2. **Purpose of Concurrency Control**

| Objective                | Explanation                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| **Correctness**          | Ensures that concurrent execution does not violate database integrity. |
| **Isolation**            | Prevents interference between transactions.                            |
| **Maximize parallelism** | Allows multiple transactions to proceed in parallel without conflict.  |
| **Avoid anomalies**      | Prevents issues like dirty reads, lost updates, etc.                   |

---

#### 3. **Schedule**

* A **schedule** is a sequence of operations from multiple transactions **interleaved** in some order.
* A **valid schedule** must:

  * Preserve the **order of operations** within each individual transaction.
  * Ensure **correct execution** as if the transactions had been executed serially.

---

#### 4. **Types of Schedules**

| Type                      | Description                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Serial Schedule**       | All operations of one transaction execute before any operation of the next.  |
| **Concurrent Schedule**   | Operations from different transactions are interleaved.                      |
| **Serializable Schedule** | Concurrent schedule that results in the same final state as some serial one. |

---

#### 5. **Need for Schedules in Concurrency Control**

* Without controlled schedules, concurrent transactions may cause:

  * **Dirty reads**: Reading uncommitted data.
  * **Lost updates**: Overwriting data written by another transaction.
  * **Inconsistent retrievals**: Reading partial results from multiple transactions.
* **Schedules define the order** in which operations execute and help prevent such problems.

---

#### 6. **Correctness of Schedules**

| Criteria                  | Description                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| **Conflict Serializable** | Schedule is equivalent to a serial schedule if **conflicting operations** are ordered the same way. |
| **View Serializable**     | Schedule is equivalent in terms of **read-from** and **final write**.                               |
| **Recoverable**           | Transactions commit only after the transactions whose data they used have committed.                |
| **Cascadeless**           | Transactions only read data written by **committed** transactions.                                  |
| **Strict**                | Transactions neither read nor write data modified by **uncommitted** transactions.                  |

---

#### 7. **Conflict in Schedules**

* Two operations **conflict** if:

  * They belong to **different transactions**, and
  * They operate on the **same data item**, and
  * At least one of them is a **write**.

| Operation 1 | Operation 2 | Conflict? |
| ----------- | ----------- | --------- |
| Read(X)     | Read(X)     | No        |
| Read(X)     | Write(X)    | Yes       |
| Write(X)    | Read(X)     | Yes       |
| Write(X)    | Write(X)    | Yes       |

---

#### 8. **Concurrency Control Methods (Through Scheduling)**

| Method                        | Description                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Two-Phase Locking (2PL)**   | Divides schedule into growing (acquire locks) and shrinking (release locks) phases to ensure serializability. |
| **Timestamp Ordering**        | Assigns a unique timestamp to each transaction and schedules operations accordingly.                          |
| **Validation-Based Protocol** | Transactions execute freely, validated at commit time for conflicts.                                          |

---

#### 9. **Example of Schedules**

**Schedule S1 (Serial):**

```plaintext
T1: Read(X), Write(X), Commit
T2: Read(Y), Write(Y), Commit
```

**Schedule S2 (Interleaved, but Serializable):**

```plaintext
T1: Read(X)
T2: Read(Y)
T1: Write(X), Commit
T2: Write(Y), Commit
```

**Schedule S3 (Not Serializable):**

```plaintext
T1: Read(X)
T2: Write(X)
T1: Write(X)
T2: Commit
T1: Commit
```

→ Final result may not match any serial execution of T1 and T2.

---

#### 10. **Summary Table**

| Concept                   | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| **Concurrency Control**   | Managing interleaved operations of multiple transactions    |
| **Schedule**              | Execution order of transaction operations                   |
| **Serial Schedule**       | Transactions execute one after another                      |
| **Serializable Schedule** | Interleaved schedule equivalent to a serial one             |
| **Recoverable Schedule**  | Ensures no transaction commits before the one it depends on |
| **Strict Schedule**       | Avoids dirty reads and cascading rollbacks                  |

---

### Taxonomy of Schedules — Detailed Explanation

---

#### 1. **Definition**

* **Taxonomy of Schedules** refers to the **classification of transaction schedules** based on properties like **serializability**, **recoverability**, and **isolation**.
* It helps in understanding **which schedules are correct and safe** for concurrent transaction execution in a DBMS.

---

#### 2. **Classification Criteria**

| Criteria                     | Types of Schedules Classified Based On It             |
| ---------------------------- | ----------------------------------------------------- |
| **Serializability**          | Conflict Serializable, View Serializable              |
| **Recoverability**           | Recoverable, Cascadeless, Strict                      |
| **Transaction Dependencies** | Based on read/write dependencies between transactions |

---

### A. Schedules Based on Serializability

---

#### 3. **1) Serial Schedule**

* All operations of one transaction execute completely before another starts.
* **No interleaving** of operations.
* Always **correct and consistent**.

**Example:**

```
T1: Read(X), Write(X), Commit
T2: Read(Y), Write(Y), Commit
```

---

#### 4. **2) Non-Serial Schedule**

* Operations of transactions are **interleaved**.
* May or may not be correct.
* Needs to be **tested for serializability**.

---

#### 5. **3) Conflict Serializable Schedule**

* A non-serial schedule that is **equivalent to a serial schedule** when **conflicting operations are ordered the same**.
* Conflicts arise when:

  * Two operations from different transactions
  * Operate on the same data item
  * At least one is a write

**Tested Using:**

* **Precedence Graph (Serialization Graph)**

  * If acyclic → Conflict Serializable

---

#### 6. **4) View Serializable Schedule**

* A schedule is **view equivalent** to a serial schedule if:

  * **Initial reads** are same
  * **Read-from relationships** are preserved
  * **Final writes** are same
* View serializability is **more general** than conflict serializability.
* Every conflict-serializable schedule is also view-serializable, but not vice versa.

---

### B. Schedules Based on Recoverability

---

#### 7. **1) Recoverable Schedule**

* A schedule is **recoverable** if **a transaction commits only after all transactions whose data it read have committed**.

**Prevents:**

* Committing a transaction that depended on an **uncommitted transaction**

**Example:**

```
T1: Write(X)
T2: Read(X)
T1: Commit
T2: Commit   ← Safe
```

---

#### 8. **2) Cascadeless Schedule**

* A schedule where a transaction **only reads data written by committed transactions**.

**Prevents:**

* Cascading rollbacks

**Stronger than recoverable schedules**

**Example:**

```
T1: Write(X)
T1: Commit
T2: Read(X)   ← Safe
```

---

#### 9. **3) Strict Schedule**

* A schedule where transactions **do not read or write** data **modified by uncommitted transactions**.
* Ensures **strict serializability**.
* Simplifies recovery by avoiding both cascading rollbacks and dirty reads.

---

### C. Summary of Recoverability-Based Schedules

| Type            | Read Uncommitted Data? | Commit Order Matters? | Cascading Rollbacks Possible? |
| --------------- | ---------------------- | --------------------- | ----------------------------- |
| Strict          | No                     | Yes                   | No                            |
| Cascadeless     | No                     | Yes                   | No                            |
| Recoverable     | Yes                    | Yes                   | Yes                           |
| Non-Recoverable | Yes                    | No                    | Yes                           |

---

### D. Summary Table — Taxonomy of Schedules

| Classification       | Types of Schedules                                   | Key Property Checked                          |
| -------------------- | ---------------------------------------------------- | --------------------------------------------- |
| **Serializability**  | Serial, Conflict Serializable, View Serializable     | Final state equivalence with serial execution |
| **Recoverability**   | Recoverable, Cascadeless, Strict                     | Commit ordering and read dependencies         |
| **Safety Guarantee** | Strict > Cascadeless > Recoverable > Non-Recoverable | Strict schedules offer strongest safety       |

---

### Characterizing Schedules Based on Recoverability — Detailed Explanation

---

#### 1. **Definition**

* Recoverability of a schedule refers to whether **committed transactions are dependent on only other committed transactions**.
* Ensures that the database can **recover to a consistent state** even if some transactions fail or abort.
* **Main focus**: **Read-after-write dependencies** and **commit order**.

---

#### 2. **Why Recoverability is Important**

| Purpose                     | Explanation                                                                   |
| --------------------------- | ----------------------------------------------------------------------------- |
| Prevent inconsistent states | Avoids situations where a committed transaction depends on an uncommitted one |
| Ensure safe recovery        | Ensures that system can roll back uncommitted transactions safely             |
| Avoid data corruption       | Prevents use of unconfirmed data during concurrent executions                 |

---

### 3. **Types of Schedules Based on Recoverability**

---

#### A) **Recoverable Schedule**

| Feature               | Description                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Definition**        | A schedule is **recoverable** if a transaction **Tj commits only after Ti**, which it **read data from**, has committed. |
| **Condition**         | If Tj reads X written by Ti → Tj should **commit after Ti**                                                              |
| **Problem Prevented** | Avoids **committing based on uncommitted/aborted data**                                                                  |

**Example (Recoverable):**

```plaintext
T1: Write(X)
T2: Read(X)  ← from T1
T1: Commit
T2: Commit  ← Safe
```

**Example (Not Recoverable):**

```plaintext
T1: Write(X)
T2: Read(X)
T2: Commit  ← Problem! T1 hasn’t committed yet
T1: Abort   ← Causes inconsistency in T2
```

---

#### B) **Cascadeless Schedule**

| Feature               | Description                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| **Definition**        | A schedule is **cascadeless** if **a transaction only reads data** written by **committed transactions**. |
| **Condition**         | Tj can read X only **after Ti (writer of X) has committed**                                               |
| **Problem Prevented** | Avoids **cascading rollbacks**                                                                            |

**Example (Cascadeless):**

```plaintext
T1: Write(X)
T1: Commit
T2: Read(X)  ← Safe
```

**Example (Not Cascadeless):**

```plaintext
T1: Write(X)
T2: Read(X)  ← Problem! T1 hasn't committed yet
T1: Abort    ← T2 must now rollback → Cascading rollback
```

---

#### C) **Strict Schedule**

| Feature               | Description                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**        | A schedule is **strict** if transactions can **neither read nor write** a data item **X modified by another uncommitted transaction**. |
| **Condition**         | No read/write on X until previous writer commits or aborts                                                                             |
| **Problem Prevented** | Avoids both **dirty reads and cascading rollbacks**                                                                                    |

**Example (Strict):**

```plaintext
T1: Write(X)
T1: Commit
T2: Read(X)  ← Safe
```

**Example (Not Strict):**

```plaintext
T1: Write(X)
T2: Read(X)  ← Problem! T1 hasn't committed yet → dirty read
```

---

#### D) **Non-Recoverable Schedule**

| Feature         | Description                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| **Definition**  | A schedule is **non-recoverable** if a transaction commits **before** the transaction whose data it read. |
| **Issue**       | **Tj commits based on data from Ti**, but Ti later aborts                                                 |
| **Consequence** | Data inconsistency and unrecoverable state                                                                |

---

### 4. **Comparison Table**

| Property            | **Recoverable** | **Cascadeless** | **Strict**  | **Non-Recoverable** |
| ------------------- | --------------- | --------------- | ----------- | ------------------- |
| Safe Commit Order   | Yes             | Yes             | Yes         | No                  |
| Dirty Reads         | Allowed         | Not Allowed     | Not Allowed | Allowed             |
| Cascading Rollbacks | Allowed         | Not Allowed     | Not Allowed | Allowed             |
| Simplifies Recovery | Partially       | Yes             | Yes         | No                  |
| Strongest Safety    | ✗               | ✗               | ✔           | ✗✗                  |

---

### 5. **Hierarchy of Schedules**

```
Strict ⊂ Cascadeless ⊂ Recoverable ⊂ All Schedules
```

* **Strict schedules** are a subset of **cascadeless**, which are a subset of **recoverable** schedules.

---

### 6. **Key Takeaways**

| Point                         | Explanation                                                             |
| ----------------------------- | ----------------------------------------------------------------------- |
| **Recoverable schedules**     | Ensure commit ordering is safe                                          |
| **Cascadeless schedules**     | Prevent cascading rollbacks by only reading committed data              |
| **Strict schedules**          | Provide maximum safety by preventing any read/write on uncommitted data |
| **Non-recoverable schedules** | Should be avoided due to unsafe and unrecoverable behavior              |

---

### Characterizing Schedules Based on Serializability (T1) — Detailed Explanation

---

#### 1. **Definition of Serializability**

* **Serializability** is the **strongest level of correctness** in concurrency control.
* A **schedule is serializable** if its outcome (final database state) is the **same as some serial schedule**, even if the operations are interleaved.
* Ensures that **concurrent execution** of transactions preserves **database consistency**.

---

#### 2. **Why Serializability is Needed**

| Reason                   | Explanation                                                |
| ------------------------ | ---------------------------------------------------------- |
| **Maintain consistency** | Parallel execution yields same result as some serial order |
| **Allow concurrency**    | Maximizes throughput while avoiding interference           |
| **Prevent anomalies**    | Avoids lost updates, dirty reads, inconsistent reads       |

---

#### 3. **Types of Serializability**

| Type                         | Description                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| **Conflict Serializability** | Based on ordering of **conflicting operations** (read/write on same data) |
| **View Serializability**     | Based on **read-from and write consistency** among transactions           |

---

### A. Conflict Serializability

---

#### 4. **Definition**

* A schedule is **conflict serializable** if it can be transformed into a **serial schedule** by **swapping non-conflicting operations**.

#### 5. **Conflicting Operations**

Operations **conflict** if:

* Belong to **different transactions**
* Operate on the **same data item**
* At least **one is a write**

| Operation 1 | Operation 2 | Conflict? |
| ----------- | ----------- | --------- |
| Read(X)     | Read(X)     | No        |
| Read(X)     | Write(X)    | Yes       |
| Write(X)    | Read(X)     | Yes       |
| Write(X)    | Write(X)    | Yes       |

---

#### 6. **Conflict Precedence Graph (Serialization Graph)**

* **Nodes**: Transactions (T1, T2, ...)

* **Edges**: Directed edge from Ti to Tj if:

  * Ti's operation **conflicts** with Tj's operation
  * Ti's operation **precedes** Tj's operation in the schedule

* **A schedule is conflict serializable if and only if the precedence graph is acyclic**

---

#### 7. **Example (Conflict Serializable)**

**Schedule S:**

```plaintext
T1: Read(X)
T2: Write(X)
T1: Write(X)
T2: Read(Y)
T2: Write(Y)
```

* Conflicts:

  * T1 Read(X) vs T2 Write(X): Edge T1 → T2
  * T1 Write(X) vs T2 Write(X): Edge T1 → T2

* Graph: T1 → T2

* Acyclic → **Conflict Serializable**

---

#### 8. **Example (Not Conflict Serializable)**

**Schedule S:**

```plaintext
T1: Read(X)
T2: Write(X)
T1: Write(X)
T2: Write(Y)
T1: Read(Y)
```

* Conflicts:

  * T1 Read(X) vs T2 Write(X): T2 → T1
  * T1 Write(X) vs T2 Write(X): T1 → T2 → **Cycle**
  * T1 Read(Y) vs T2 Write(Y): T2 → T1

* Graph has **cycle** → **Not conflict serializable**

---

### B. View Serializability

---

#### 9. **Definition**

* A schedule is **view serializable** if it is **view equivalent** to a serial schedule.

View equivalence conditions:

1. **Initial reads** (from the database) are the same
2. **Read-from relationships** are the same (which transaction writes the data read by another)
3. **Final writes** are the same (same transaction performs the last write on each data item)

* **View serializability ⊇ Conflict serializability**

  * All conflict-serializable schedules are view-serializable, but **not vice versa**

---

#### 10. **Comparison: Conflict vs View Serializability**

| Feature            | Conflict Serializability   | View Serializability                  |
| ------------------ | -------------------------- | ------------------------------------- |
| Basis              | Conflicting operations     | Read-from and final write consistency |
| Check method       | Precedence graph (acyclic) | Complex, exponential check            |
| Subset             | ⊆ View Serializability     | ⊇ Conflict Serializability            |
| Computational ease | Easy to check              | Hard to check                         |

---

### C. Summary Table

| Schedule Property         | Definition                                                   | Validity Check             |
| ------------------------- | ------------------------------------------------------------ | -------------------------- |
| **Serial**                | Transactions execute one after another                       | Directly ordered           |
| **Conflict Serializable** | Equivalent to a serial schedule based on conflict resolution | Precedence graph → Acyclic |
| **View Serializable**     | Same read-from and final write as a serial schedule          | Check for view equivalence |

---

### D. Key Takeaways

* **Conflict serializability** is the most **practical** and **commonly enforced** in databases.
* **View serializability** is more **permissive**, but harder to implement.
* **Serializability ensures correctness** by preserving the **effect of serial execution**.

---

### Transaction Isolation Levels (T2) — Detailed Explanation

---

#### 1. **Definition**

* **Isolation level** defines the **degree to which a transaction is isolated** from the effects (reads/writes) of other concurrent transactions.
* Controls how **and when changes made by one transaction become visible to others**.
* Defined in the **SQL standard (SQL92)** to handle **concurrency issues**.

---

#### 2. **Purpose of Isolation Levels**

| Purpose                               | Explanation                                                |
| ------------------------------------- | ---------------------------------------------------------- |
| **Prevent anomalies**                 | Avoid dirty reads, non-repeatable reads, and phantom reads |
| **Balance consistency & performance** | Higher isolation = more consistency but less concurrency   |
| **Control visibility**                | Defines when changes are visible to other transactions     |

---

#### 3. **Common Concurrency Anomalies**

| Anomaly                 | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| **Dirty Read**          | Reading **uncommitted data** from another transaction                 |
| **Non-Repeatable Read** | **Same read yields different results** within the same transaction    |
| **Phantom Read**        | A **new row appears** in a repeated query within the same transaction |

---

### 4. **Standard Isolation Levels (SQL)**

| Isolation Level      | Dirty Read | Non-Repeatable Read | Phantom Read | Performance | Consistency |
| -------------------- | ---------- | ------------------- | ------------ | ----------- | ----------- |
| **READ UNCOMMITTED** | ✔          | ✔                   | ✔            | High        | Low         |
| **READ COMMITTED**   | ✘          | ✔                   | ✔            | Moderate    | Moderate    |
| **REPEATABLE READ**  | ✘          | ✘                   | ✔            | Low         | High        |
| **SERIALIZABLE**     | ✘          | ✘                   | ✘            | Lowest      | Highest     |

---

### 5. **Detailed Description of Each Isolation Level**

---

#### A) **READ UNCOMMITTED**

| Feature              | Details                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| Allows dirty reads   | Yes — can read data written by uncommitted transactions                  |
| Non-repeatable reads | Yes                                                                      |
| Phantom reads        | Yes                                                                      |
| Use Case             | Rare; mostly used in analytics or logs where consistency is not critical |
| Locking              | No shared locks acquired                                                 |

**Example:**

```plaintext
T1: Write(X = 500)
T2: Read(X = 500) ← T1 has not committed
T1: Rollback
→ T2 read dirty data
```

---

#### B) **READ COMMITTED**

| Feature              | Details                                          |
| -------------------- | ------------------------------------------------ |
| Dirty reads          | Not allowed                                      |
| Non-repeatable reads | Allowed                                          |
| Phantom reads        | Allowed                                          |
| Use Case             | Default in many DBMS (e.g., Oracle, PostgreSQL)  |
| Locking              | Read locks acquired and released after each read |

**Example:**

```plaintext
T1: Read(X = 100)
T2: Update X = 200, Commit
T1: Read(X = 200) ← T1 sees different value for X in same transaction
```

---

#### C) **REPEATABLE READ**

| Feature              | Details                                                     |
| -------------------- | ----------------------------------------------------------- |
| Dirty reads          | Not allowed                                                 |
| Non-repeatable reads | Not allowed                                                 |
| Phantom reads        | Allowed                                                     |
| Use Case             | When consistent reads of rows are needed                    |
| Locking              | Shared locks on all rows read, held till end of transaction |

**Example:**

```plaintext
T1: SELECT * FROM orders WHERE amount > 100
T2: INSERT INTO orders (amount = 150)
T1: SELECT * FROM orders WHERE amount > 100 ← Now sees extra row (phantom)
```

---

#### D) **SERIALIZABLE**

| Feature                | Details                                             |
| ---------------------- | --------------------------------------------------- |
| Dirty reads            | Not allowed                                         |
| Non-repeatable reads   | Not allowed                                         |
| Phantom reads          | Not allowed                                         |
| Use Case               | Maximum consistency required (e.g., bank transfers) |
| Locking                | Locks on all accessed rows and ranges               |
| Internally Enforced As | Two-Phase Locking or Predicate Locking              |

**Behavior**:

* Prevents any new row that matches a previously executed query from being inserted/modified.

---

#### 6. **Anomaly Handling by Level**

| Isolation Level  | Dirty Read | Non-Repeatable Read | Phantom Read |
| ---------------- | ---------- | ------------------- | ------------ |
| Read Uncommitted | Possible   | Possible            | Possible     |
| Read Committed   | Prevented  | Possible            | Possible     |
| Repeatable Read  | Prevented  | Prevented           | Possible     |
| Serializable     | Prevented  | Prevented           | Prevented    |

---

#### 7. **Implementation Techniques**

| Technique                                   | Used By                                  |
| ------------------------------------------- | ---------------------------------------- |
| **Lock-Based Protocols**                    | Most traditional DBMS (e.g., SQL Server) |
| **Multiversion Concurrency Control (MVCC)** | PostgreSQL, Oracle                       |
| **Snapshot Isolation**                      | Variant of REPEATABLE READ in MVCC       |

---

#### 8. **Trade-Off Between Isolation and Performance**

| Isolation Level  | Consistency | Performance | Use Cases                                |
| ---------------- | ----------- | ----------- | ---------------------------------------- |
| Read Uncommitted | Lowest      | Fastest     | Logging, monitoring                      |
| Read Committed   | Medium      | Good        | Web apps, default in many DBMS           |
| Repeatable Read  | High        | Slower      | Reporting, financial queries             |
| Serializable     | Highest     | Slowest     | Bank transfers, mission-critical systems |

---

#### 9. **Summary Table**

| Level            | Prevents Dirty Reads | Prevents Non-Repeatable Reads | Prevents Phantom Reads |
| ---------------- | -------------------- | ----------------------------- | ---------------------- |
| Read Uncommitted | ✘                    | ✘                             | ✘                      |
| Read Committed   | ✔                    | ✘                             | ✘                      |
| Repeatable Read  | ✔                    | ✔                             | ✘                      |
| Serializable     | ✔                    | ✔                             | ✔                      |

---

