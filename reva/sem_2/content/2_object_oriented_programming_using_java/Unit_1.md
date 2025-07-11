# Unit - 1 -> Introduction to the Fundamentals of Java Programming
An overview of Java, Internal Details of JVM.
Difference between JDK, JRE and JVM, Features of Java.
Data types, Token, Type Conversion, Casting.
Arrays, Operators and Precedence, Branching and Looping statements.
Classes, objects, methods, Constructors, this, super and final keyword.

## Content -> 
### An Overview of Java

1. **Definition of Java**

   * Java is a high-level, object-oriented, class-based programming language.
   * It is designed to have as few implementation dependencies as possible.
   * It allows application developers to write once, run anywhere (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation.

2. **History and Development**

   * Developed by **James Gosling** at Sun Microsystems.
   * Initial release: **May 23, 1995**.
   * Later acquired by **Oracle Corporation** in 2010.
   * Originally designed for interactive television but later adapted for internet applications.

3. **Paradigm Support**

   * **Object-Oriented Programming** (OOP): Java supports principles like inheritance, encapsulation, polymorphism, and abstraction.
   * **Concurrent Programming**: Built-in support for multithreading.
   * **Generic Programming**: Supports generic classes and methods.
   * **Functional Programming**: Introduced lambda expressions in Java 8.

4. **Java Program Structure**

   * Every Java program must have a class.
   * Entry point is the `main()` method:

     ```java
     public static void main(String[] args)
     ```

5. **Compilation and Execution**

   * Java source code is written in `.java` files.
   * The Java compiler (`javac`) compiles source code into **bytecode** (`.class` files).
   * Bytecode is platform-independent and executed by the **Java Virtual Machine (JVM)**.
   * This makes Java both **compiled** and **interpreted**.

6. **Core Components of Java Platform**

   * **Java Language**: Syntax and semantics.
   * **Java Compiler**: Converts source code to bytecode.
   * **Java Virtual Machine (JVM)**: Executes bytecode on any device.
   * **Java API (Application Programming Interface)**: Predefined classes and interfaces for common tasks.

7. **Java Editions**

   * **Java SE (Standard Edition)**: Core language features and libraries.
   * **Java EE (Enterprise Edition)**: For large-scale applications (now Jakarta EE).
   * **Java ME (Micro Edition)**: For embedded systems and mobile devices.
   * **JavaFX**: For developing rich GUI applications.

8. **Platform Independence**

   * Achieved using bytecode and JVM.
   * Bytecode runs on any OS with the corresponding JVM implementation.
   * No need to recompile code for different platforms.

9. **Security**

   * Java includes a **security manager** and **bytecode verifier** to protect against malicious code.
   * Uses **sandboxing** for running untrusted code.
   * Provides APIs for encryption, authentication, and secure communication.

10. **Robustness**

* Strong memory management via **garbage collection**.
* Exception handling mechanism to manage run-time errors.
* Type checking at both compile-time and runtime.

11. **Portability**

* Java programs can run on any platform with JVM.
* Eliminates platform-specific dependencies.

12. **Built-in Libraries**

* Rich set of standard libraries:

  * **java.lang**: Fundamental classes (String, Math, Object).
  * **java.util**: Collections, Date, Random.
  * **java.io**: File and stream I/O.
  * **java.net**: Networking.
  * **java.sql**: Database connectivity.

13. **Use Cases and Applications**

* Desktop Applications
* Web Applications
* Mobile Applications (Android uses Java)
* Enterprise Applications
* Embedded Systems
* Scientific Applications
* Big Data and Analytics (with frameworks like Hadoop)

14. **Development Tools**

* **JDK (Java Development Kit)**: Includes compiler, debugger, and JVM.
* **IDEs**: Eclipse, IntelliJ IDEA, NetBeans.
* **Build Tools**: Maven, Gradle, Ant.

15. **Community and Ecosystem**

* One of the largest programming communities.
* Huge number of open-source libraries and frameworks.
* Regular updates and LTS (Long-Term Support) versions from Oracle and OpenJDK community.

### Internal Details of JVM (Java Virtual Machine)

---

1. **What is JVM?**

   * JVM (Java Virtual Machine) is an abstract computing machine that enables a computer to run Java bytecode.
   * It is a part of the Java Runtime Environment (JRE).
   * Responsible for interpreting or compiling bytecode and executing Java programs.

---

2. **Main Responsibilities of JVM**

   * Loads Java bytecode.
   * Verifies and interprets or compiles bytecode into machine code.
   * Manages memory (allocation and garbage collection).
   * Handles security checks.
   * Provides runtime environment and exception handling.

---

3. **Architecture of JVM**

   ```
   Java Source Code (.java)
          |
         javac (Compiler)
          |
      Bytecode (.class)
          |
         JVM
   ```

---

4. **Internal Components of JVM**

---

#### A. **Class Loader Subsystem**

* Loads `.class` files (bytecode) into JVM memory.
* Converts class files into runtime data structures.
* **Three phases:**

  1. **Loading**: Finds and loads class files.
  2. **Linking**:

     * **Verification**: Ensures bytecode is safe and valid.
     * **Preparation**: Allocates memory for class variables.
     * **Resolution**: Replaces symbolic references with direct references.
  3. **Initialization**: Assigns default values and runs static blocks.

---

#### B. **Method Area**

* Shared memory area for all threads.
* Stores:

  * Class structure (methods, fields).
  * Runtime constant pool.
  * Method and field data.
  * Code for static methods.

---

#### C. **Heap**

* Shared memory area.
* Stores:

  * All Java objects.
  * Arrays.
  * Class instances.
* Garbage Collector operates here to remove unused objects.

---

#### D. **Java Stack (Thread Stack)**

* Each thread has its own stack.
* Stores:

  * Frames for each method call.
  * Local variables, partial results.
  * Data for method invocation and return.
* Operates in LIFO (Last-In-First-Out) order.
* If stack exceeds limit → **StackOverflowError**.

---

#### E. **Program Counter (PC) Register**

* Each thread has its own PC register.
* Contains address of currently executing instruction (bytecode).
* Updated after each instruction is executed.

---

#### F. **Native Method Stack**

* Used for executing native (non-Java) methods written in C/C++.
* Interfaces with the OS using **JNI (Java Native Interface)**.
* Stores native method information and calls.

---

#### G. **Execution Engine**

* Core of JVM that executes the bytecode.
* Contains:

  1. **Interpreter**:

     * Reads and executes bytecode instructions one by one.
     * Slower, but used for startup and less-used code.

  2. **Just-In-Time (JIT) Compiler**:

     * Converts bytecode into native machine code for better performance.
     * Used for frequently executed code (hot spots).
     * Stored in memory to avoid recompilation.

  3. **Garbage Collector (GC)**:

     * Automatically frees memory by removing unreachable objects.
     * Uses algorithms like Mark-and-Sweep, Generational GC.

---

#### H. **Runtime Constant Pool**

* Part of the method area.
* Stores:

  * String literals.
  * Symbolic references to classes, methods, fields.
  * Constants used by bytecode.

---

#### I. **Native Interface (JNI - Java Native Interface)**

* Allows Java code to call and be called by native applications.
* Used to access OS-level resources, legacy libraries, hardware.

---

#### J. **Security Manager & Bytecode Verifier**

* **Bytecode Verifier**:

  * Checks bytecode for illegal code that can violate access rights.
  * Ensures type safety and memory integrity.

* **Security Manager**:

  * Defines security policy.
  * Restricts access to critical operations (file I/O, network, etc.).

---

5. **JVM Languages Support**

   * Not limited to Java. Supports multiple languages compiled to bytecode:

     * Kotlin
     * Scala
     * Groovy
     * JRuby
     * Jython

---

6. **JVM Implementations**

   * **HotSpot (Oracle/OpenJDK)** – Most widely used.
   * **GraalVM** – High-performance polyglot VM.
   * **OpenJ9 (IBM)** – Optimized for cloud-native apps.
   * **Zing (Azul Systems)** – Low-latency JVM.

---

7. **Performance Features**

   * **Garbage Collection Tuning**: G1, ZGC, Shenandoah.
   * **Adaptive Optimization**: Learns which code paths are hot.
   * **Tiered Compilation**: Combines interpreter + JIT for balance.

---

8. **JVM Life Cycle**

   * JVM starts when a Java program starts (`main` method).
   * Loads classes and initializes memory.
   * Executes program using interpreter and/or JIT.
   * Terminates when all non-daemon threads finish or System.exit is called.

### JDK (Java Development Kit)

---

1. **Definition**

   * JDK stands for **Java Development Kit**.
   * It is a **software development environment** used for developing Java applications.
   * It includes all necessary tools to write, compile, debug, and run Java programs.

---

2. **Main Purpose**

   * To provide the **developer tools** and **runtime environment** needed to create and run Java applications.

---

3. **Components of JDK**

#### A. **Development Tools**

* Located in the `bin/` directory.
* Used for compiling, packaging, debugging, and monitoring Java programs.

| Tool                    | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `javac`                 | Java compiler – converts `.java` files to `.class` bytecode. |
| `java`                  | Java launcher – runs Java applications by invoking JVM.      |
| `javadoc`               | Generates API documentation from Java source code comments.  |
| `jar`                   | Creates and manages `.jar` (Java Archive) files.             |
| `jdb`                   | Java debugger tool.                                          |
| `javap`                 | Disassembles `.class` files to view bytecode.                |
| `jconsole`, `jvisualvm` | Monitoring and profiling tools.                              |

---

#### B. **JRE (Java Runtime Environment)**

* JDK includes a complete **JRE** inside it.
* Contains JVM and class libraries required to run Java programs.
* Located in the `jre/` directory (older versions) or bundled under `/lib` and `/bin` in newer versions.

---

#### C. **Java Libraries (Class Libraries)**

* Predefined classes and APIs for common programming tasks.
* Examples:

  * `java.lang` (Object, Math, String, etc.)
  * `java.util` (Collections, Date, etc.)
  * `java.io`, `java.net`, `java.sql`, etc.

---

#### D. **Java Compiler API**

* Programmatic interface to access the compiler from applications.

---

#### E. **Java Native Interface (JNI)**

* Interface that allows Java code to interact with native applications and libraries written in C/C++.

---

#### F. **JavaFX SDK** (older JDKs)

* Used for developing GUI applications with rich media.
* Now distributed separately from JDK (since JDK 11).

---

4. **JDK Versions**

   * Released by **Oracle** and **OpenJDK community**.
   * Follows regular release cycle:

     * **LTS (Long-Term Support)**: e.g., JDK 8, JDK 11, JDK 17.
     * **Non-LTS**: Shorter support, released every 6 months.

---

5. **Platform Specific**

   * JDK is platform-dependent. Separate installers for:

     * Windows
     * Linux
     * macOS

---

6. **Directory Structure (Typical JDK Layout)**

   ```
   /jdk-XX/
   ├── bin/           → Executables like java, javac, javadoc
   ├── lib/           → Core Java libraries
   ├── include/       → Header files for JNI
   ├── jmods/         → Modular components (since Java 9)
   └── conf/          → Configuration files (e.g., security policy)
   ```

---

7. **JDK vs JRE vs JVM**

   | Component | Role                        | Contains                |
   | --------- | --------------------------- | ----------------------- |
   | JVM       | Runs Java bytecode          | Execution engine only   |
   | JRE       | Runs Java apps              | JVM + core libraries    |
   | JDK       | Develops and runs Java apps | JRE + development tools |

---

8. **Common Use Cases**

   * Writing Java applications.
   * Compiling source code.
   * Packaging apps into JAR files.
   * Generating documentation.
   * Debugging and monitoring apps.
   * Connecting to native libraries using JNI.

---

9. **Popular JDK Distributions**

   * **Oracle JDK** – Official, commercial license for production.
   * **OpenJDK** – Open-source reference implementation.
   * **Adoptium (Eclipse Temurin)** – Free, open-source builds.
   * **Amazon Corretto** – Free JDK by AWS.
   * **Zulu by Azul**, **Liberica by BellSoft**, etc.

---

10. **Modularization (from Java 9 onwards)**

* JDK is modularized using **Project Jigsaw**.
* Uses `jmod` and `module-info.java` to define and manage modules.
* Improves startup performance and footprint.

### JRE (Java Runtime Environment)

---

1. **Definition**

   * JRE stands for **Java Runtime Environment**.
   * It is a **software package** that provides the **necessary environment to run** Java applications.
   * It **does not include development tools** like a compiler or debugger.

---

2. **Main Purpose**

   * To **execute** Java programs that have already been compiled into bytecode (`.class` files).
   * Acts as a **layer between Java applications and the underlying operating system**.

---

3. **Components of JRE**

#### A. **Java Virtual Machine (JVM)**

* Executes Java bytecode.
* Provides memory management, garbage collection, security, and thread management.
* Converts bytecode to machine-specific instructions.

#### B. **Core Class Libraries**

* Collection of pre-written classes packaged in `.jar` files.
* Provides functionality such as file I/O, networking, data structures, GUI, etc.
* Examples:

  * `java.lang`: Basic language classes like `String`, `Math`, `Object`.
  * `java.util`: Collections, date, random.
  * `java.io`: File input/output.
  * `java.net`: Networking classes.
  * `java.sql`: Database interaction.

#### C. **Java Class Loader**

* Part of JVM that loads `.class` files into memory.
* Verifies and prepares classes for execution.

#### D. **Runtime Libraries**

* Set of dynamically loaded class files that are used during execution.
* Support for exception handling, type checking, etc.

---

4. **Directory Structure of JRE (Traditional Layout)**

   ```
   /jre/
   ├── bin/       → Java executable (java.exe, java)
   ├── lib/       → Core library files (.jar), property files
   └── lib/ext/   → Extension libraries (deprecated in Java 9+)
   ```

---

5. **Key Files in JRE**

   | File                                       | Purpose                                       |
   | ------------------------------------------ | --------------------------------------------- |
   | `java`                                     | Java application launcher.                    |
   | `rt.jar` (up to Java 8)                    | Runtime classes (deprecated in modular Java). |
   | `jvm.dll` (Windows) or `libjvm.so` (Linux) | JVM native implementation.                    |

---

6. **JRE vs JDK vs JVM**

   | Component | Contains                | Use Case                            |
   | --------- | ----------------------- | ----------------------------------- |
   | JVM       | Bytecode interpreter    | Executes bytecode                   |
   | JRE       | JVM + Class Libraries   | Runs Java applications              |
   | JDK       | JRE + Development Tools | Develops and runs Java applications |

---

7. **Usage of JRE**

   * Required to **run** Java applications on user machines.
   * Can be **separately installed** on machines where development tools are not needed.
   * Often embedded in software installers that require Java.

---

8. **JRE Availability**

   * **No separate JRE after Java 11** by Oracle.
   * JRE functionality is embedded inside the JDK distribution.
   * **Modular Java** (Java 9+) allows building custom runtime images using `jlink`.

---

9. **Platform Specific**

   * JRE is platform-dependent (different for Windows, Linux, macOS).
   * Provides a consistent runtime environment across platforms via JVM.

---

10. **Important Notes**

* JRE does **not include** the Java compiler (`javac`).
* Suitable for **end-users** who need to **run** Java applications but do not develop them.
* In modern Java, JDK is used even for runtime as JRE is no longer distributed separately.

### JVM (Java Virtual Machine)

---

1. **Definition**

   * JVM stands for **Java Virtual Machine**.
   * It is a **virtual (abstract) machine** that enables a computer to **run Java bytecode**.
   * It provides a **platform-independent execution environment** for Java programs.

---

2. **Role in Java Platform**

   * JVM is the **core component** of both **JDK** and **JRE**.
   * Converts **compiled Java bytecode** (`.class` files) into **machine-specific instructions**.
   * Handles runtime tasks such as **memory management**, **thread handling**, and **exception handling**.

---

3. **Execution Flow**

   ```
   Java Source (.java)
         ↓
   Java Compiler (javac)
         ↓
   Bytecode (.class)
         ↓
   Java Virtual Machine (JVM)
         ↓
   Machine Code Execution
   ```

---

4. **Main Responsibilities of JVM**

   * **Load** class files.
   * **Verify** bytecode.
   * **Execute** instructions.
   * **Allocate and manage memory**.
   * **Perform garbage collection**.
   * **Handle exceptions and security**.

---

5. **Key Features**

   * **Platform Independence** (via bytecode execution).
   * **Automatic Memory Management**.
   * **Security** via sandboxing and bytecode verification.
   * **Support for Multithreading**.
   * **Performance Optimization** (via JIT compiler).

---

6. **Architecture of JVM**

   ```
   ┌────────────────────────┐
   │   Class Loader Subsystem │
   └────────────────────────┘
             ↓
   ┌────────────────────────┐
   │     Runtime Data Areas   │
   └────────────────────────┘
   ↓     ↓       ↓      ↓      ↓
   PC  Method  Heap  Java  Native
   Reg  Area         Stack  Stack
             ↓
   ┌────────────────────────┐
   │     Execution Engine      │
   └────────────────────────┘
   ↓     ↓      ↓
   ```

Interpreter  JIT  GC
↓
┌────────────────────────┐
│    Native Interface (JNI) │
└────────────────────────┘

```

---

7. **Internal Components of JVM**

---

#### A. **Class Loader Subsystem**

- Loads `.class` files into JVM memory.  
- Three types of class loaders:  
  - **Bootstrap Loader** – Loads core Java classes.  
  - **Extension Loader** – Loads classes from extension directories.  
  - **Application Loader** – Loads classes from classpath.

---

#### B. **Runtime Data Areas**

- Divided into several memory regions:

1. **Method Area**
   - Shared across all threads.  
   - Stores class-level information like:
     - Class metadata  
     - Static variables  
     - Runtime constant pool  
     - Method code

2. **Heap**
   - Shared area for all threads.  
   - Stores **object instances** and arrays.  
   - Subject to **garbage collection**.

3. **Java Stack**
   - Thread-specific memory.  
   - Stores **frames** (one per method call).  
   - Each frame contains:
     - Local variables  
     - Operand stack  
     - Return values

4. **Program Counter (PC) Register**
   - Thread-specific.  
   - Holds the memory address of the **current instruction** being executed.

5. **Native Method Stack**
   - Thread-specific.  
   - Stores information about **native (non-Java) methods**.

---

#### C. **Execution Engine**

- Executes the bytecode loaded by the class loader.

Components:

1. **Interpreter**
   - Interprets bytecode line by line.  
   - Slower execution.

2. **Just-In-Time (JIT) Compiler**
   - Converts bytecode into **native machine code** at runtime.  
   - Speeds up execution of **frequently used code**.

3. **Garbage Collector**
   - Automatically removes **unreachable objects** from heap memory.  
   - Frees up memory and prevents memory leaks.

---

#### D. **Native Interface (JNI – Java Native Interface)**

- Provides interface to **interact with native applications/libraries** written in C/C++.  
- Enables use of OS-level features.

---

#### E. **Bytecode Verifier**

- Ensures the **correctness and safety** of bytecode before execution.  
- Prevents:
  - Stack overflows  
  - Invalid memory access  
  - Security breaches

---

8. **JVM Languages Support**

- JVM can run code compiled from multiple languages (not just Java), including:  
  - **Kotlin**  
  - **Scala**  
  - **Groovy**  
  - **JRuby**  
  - **Jython**

---

9. **JVM Implementations**

- **HotSpot JVM** – Default in Oracle JDK and OpenJDK.  
- **GraalVM** – High-performance, polyglot virtual machine.  
- **Eclipse OpenJ9** – Lightweight JVM by IBM.  
- **Zulu JVM**, **Azul Zing**, etc.

---

10. **JVM Errors and Exceptions**

- **StackOverflowError**: Java stack memory exceeded.  
- **OutOfMemoryError**: Heap memory exhausted.  
- **ClassNotFoundException**: Class not found during class loading.  
- **NoClassDefFoundError**: Class not available at runtime.  
- **ExceptionInInitializerError**: Static block failure.

---

11. **Advantages**

- Ensures **write once, run anywhere** (WORA).  
- Provides **security**, **memory management**, **portability**, and **performance optimization**.  
- **Multithreading support** built-in at the virtual machine level.
```

### Difference between JDK, JRE, and JVM

---

| **Aspect**              | **JDK (Java Development Kit)**                                       | **JRE (Java Runtime Environment)**                      | **JVM (Java Virtual Machine)**                              |
| ----------------------- | -------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| **Definition**          | A full-featured software development kit for Java programming.       | A runtime environment to run Java applications.         | An abstract machine that executes Java bytecode.            |
| **Primary Purpose**     | Used for **developing** Java applications.                           | Used for **executing** Java applications.               | Used to **interpret and run** compiled Java bytecode.       |
| **Contains**            | JRE + Development tools (compiler, debugger, etc.)                   | JVM + Core Java class libraries and supporting files.   | Only the virtual machine to run bytecode.                   |
| **Includes**            | - JRE<br>- `javac`, `java`, `jar`, `javadoc`, `jdb`, etc.            | - JVM<br>- Class libraries (`rt.jar` in older versions) | - Class loader<br>- Bytecode verifier<br>- Execution engine |
| **Required For**        | - Writing, compiling, debugging Java code<br>- Full Java development | - Running Java programs only (no development)           | - Low-level bytecode execution (used internally)            |
| **Development Tools**   | Yes                                                                  | No                                                      | No                                                          |
| **Class Libraries**     | Yes                                                                  | Yes                                                     | No                                                          |
| **Platform Dependence** | Platform-specific binaries                                           | Platform-specific binaries                              | Abstract, implemented per-platform                          |
| **Installation Size**   | Larger (contains everything)                                         | Smaller than JDK                                        | N/A (part of JRE/JDK)                                       |
| **Can Compile Code?**   | Yes (`javac`)                                                        | No                                                      | No                                                          |
| **Can Execute Code?**   | Yes (`java`)                                                         | Yes                                                     | Yes                                                         |
| **Typical User**        | Java developers                                                      | End users running Java apps                             | Internal component for both JRE and JDK                     |

---

### Visual Hierarchy:

```
JDK
├── JRE
│   ├── JVM
│   └── Class Libraries
└── Development Tools
    ├── javac (compiler)
    ├── javadoc, jar, jdb
    └── etc.
```

---

### Summary:

* **JVM** is the engine that runs Java bytecode.
* **JRE** is the environment that provides the JVM and necessary libraries to run Java programs.
* **JDK** includes the JRE and adds development tools needed to write and compile Java code.

### Features of Java

---

1. **Simple**

   * Easy to learn and use.
   * Syntax is clean and similar to C/C++.
   * Complex features like pointers and operator overloading are removed.

---

2. **Object-Oriented**

   * Everything in Java is treated as an object.
   * Supports OOP principles:

     * **Encapsulation**
     * **Abstraction**
     * **Inheritance**
     * **Polymorphism**

---

3. **Platform-Independent**

   * Java code is compiled into **bytecode**, which is platform-neutral.
   * Bytecode runs on any device that has a **Java Virtual Machine (JVM)**.
   * Achieves **WORA** (Write Once, Run Anywhere).

---

4. **Secure**

   * Java provides a **sandbox** environment to run programs.
   * Features:

     * No explicit pointer usage
     * Bytecode verification
     * Security Manager for access control
     * Exception handling to avoid system crashes

---

5. **Robust**

   * Strong memory management (automatic garbage collection).
   * Type checking at compile-time and runtime.
   * Exception handling to catch run-time errors.
   * Eliminates error-prone features (e.g., no direct memory access).

---

6. **Multithreaded**

   * Built-in support for **multithreading** (executing multiple threads simultaneously).
   * Includes synchronization primitives.
   * Improves performance of applications using threads.

---

7. **Architecture Neutral**

   * Bytecode is not dependent on processor architecture.
   * Ensures the same bytecode works on different hardware platforms.

---

8. **Portable**

   * Java programs are portable across platforms.
   * No need for platform-specific features in code.
   * Platform-independent libraries and standard data types ensure portability.

---

9. **High Performance**

   * Java is interpreted but also uses **JIT (Just-In-Time) compiler**.
   * Frequently used code is compiled into native machine code for faster execution.
   * Efficient garbage collection algorithms.

---

10. **Distributed**

* Supports distributed computing using **RMI (Remote Method Invocation)** and **CORBA**.
* Java programs can easily communicate over networks using:

  * **Sockets**
  * **URL/HTTP classes**
  * **Web services**

---

11. **Dynamic**

* Java supports dynamic loading of classes.
* Classes are linked at runtime, not compile-time.
* Supports reflection and runtime type information.

---

12. **Interpreted and Compiled**

* Java source code is **compiled** into bytecode.
* Bytecode is then **interpreted or compiled at runtime** by the JVM.
* Combination of compiled and interpreted execution provides flexibility and efficiency.

---

13. **Distributed Memory Management**

* Automatic **garbage collection** removes unused objects from heap memory.
* No manual memory deallocation needed, reducing memory leaks.

---

14. **Rich API**

* Java provides extensive **standard libraries** and **APIs**:

  * `java.lang`, `java.util`, `java.io`, `java.net`, `java.sql`, etc.
  * Supports GUI, networking, database connectivity, multithreading, etc.

---

15. **Open Source and Community Support**

* Java is maintained as **OpenJDK**, available freely.
* Large community and ecosystem for libraries, tools, frameworks.

---

16. **Scalable and Extensible**

* Suitable for building small to enterprise-level applications.
* Modular design allows easy expansion and integration with new modules.

### Data Types in Java

---

#### 1. **Definition**

* **Data types** in Java specify the type of data that a variable can hold.
* Java is **statically-typed**, meaning variable types must be declared before use.
* Two main categories:

  * **Primitive Data Types**
  * **Non-Primitive (Reference) Data Types**

---

## A. **Primitive Data Types**

* Java has **8 primitive data types**.
* These are predefined by the language and stored in stack memory.

---

| **Data Type** | **Size** | **Default Value** | **Range**         | **Description**                 |
| ------------- | -------- | ----------------- | ----------------- | ------------------------------- |
| `byte`        | 1 byte   | 0                 | –128 to 127       | Smallest integer data type      |
| `short`       | 2 bytes  | 0                 | –32,768 to 32,767 | Short integer                   |
| `int`         | 4 bytes  | 0                 | –2³¹ to 2³¹–1     | Default integer type            |
| `long`        | 8 bytes  | 0L                | –2⁶³ to 2⁶³–1     | Large integer                   |
| `float`       | 4 bytes  | 0.0f              | \~±3.4e38         | Single-precision decimal        |
| `double`      | 8 bytes  | 0.0d              | \~±1.7e308        | Double-precision decimal        |
| `char`        | 2 bytes  | '\u0000'          | 0 to 65,535       | Single 16-bit Unicode character |
| `boolean`     | 1 bit\*  | false             | true or false     | Logical values                  |

> \* Though the size of `boolean` is JVM-dependent, conceptually it is 1 bit.

---

### 1. `byte`

* Useful for saving memory in large arrays.
* Example:

  ```java
  byte a = 100;
  ```

### 2. `short`

* Larger than `byte` but smaller than `int`.
* Example:

  ```java
  short b = 10000;
  ```

### 3. `int`

* Default data type for integral values.
* Example:

  ```java
  int c = 123456;
  ```

### 4. `long`

* Used when a wider range is needed.
* Must append **L** at the end.
* Example:

  ```java
  long d = 123456789L;
  ```

### 5. `float`

* Used for single-precision floating-point values.
* Must append **f** at the end.
* Example:

  ```java
  float e = 5.75f;
  ```

### 6. `double`

* Default type for decimal values.
* Higher precision than float.
* Example:

  ```java
  double f = 19.99;
  ```

### 7. `char`

* Represents a single character.
* Stored as Unicode.
* Example:

  ```java
  char g = 'A';
  ```

### 8. `boolean`

* Represents true or false.
* Used in conditional statements.
* Example:

  ```java
  boolean isJavaFun = true;
  ```

---

## B. **Non-Primitive (Reference) Data Types**

* Store **references (addresses)** to objects, not the data itself.
* Created using classes, interfaces, arrays.
* Stored in **heap memory**.

### 1. **String**

* A sequence of characters.
* Internally an object of the `String` class.
* Example:

  ```java
  String name = "Java";
  ```

### 2. **Arrays**

* A collection of variables of the same type.
* Can be one-dimensional or multidimensional.
* Example:

  ```java
  int[] arr = {1, 2, 3};
  ```

### 3. **Classes**

* Used to define custom data types.
* Example:

  ```java
  class Student {
      int id;
      String name;
  }
  ```

### 4. **Interfaces**

* Similar to classes, but contain only abstract methods and constants.
* Used to define contracts for classes.

---

## C. **Differences Between Primitive and Non-Primitive**

| **Aspect**         | **Primitive Data Types**    | **Non-Primitive Data Types**        |
| ------------------ | --------------------------- | ----------------------------------- |
| Memory Location    | Stack                       | Heap                                |
| Contains           | Actual values               | References (addresses)              |
| Size               | Fixed                       | Can vary                            |
| Default Values     | Predefined (e.g., 0, false) | null                                |
| Creation           | Built-in                    | Created using class/interface/array |
| Null Value Support | No                          | Yes                                 |

---

## D. **Type Hierarchy (Simplified)**

```
Object
 ├─ String
 ├─ Array
 ├─ Custom Class
 ├─ Wrapper Classes (Integer, Double, etc.)
```

---

## E. **Type Compatibility**

* Implicit (widening) conversion possible between some primitive types.
* Non-primitive types require explicit casting or reference type compatibility.

### Tokens in Java

---

#### 1. **Definition**

* A **token** in Java is the **smallest meaningful unit** in a Java program.
* During compilation, the source code is broken into **tokens** by the **lexical analyzer** (scanner).
* Tokens are the **building blocks** of Java source code.

---

#### 2. **Types of Tokens in Java**

There are **six** main types of tokens in Java:

| Token Type      | Description                                         |
| --------------- | --------------------------------------------------- |
| **Keywords**    | Reserved words with predefined meaning in Java      |
| **Identifiers** | Names given to variables, methods, classes, etc.    |
| **Literals**    | Constant values assigned to variables               |
| **Operators**   | Symbols that perform operations on variables/values |
| **Separators**  | Symbols used to separate code elements              |
| **Comments**    | Notes ignored by the compiler                       |

---

### 1. **Keywords**

* Predefined, reserved words in Java.

* Cannot be used as identifiers (variable names, method names, etc.).

* All are in lowercase.

* Examples:
  `int`, `class`, `if`, `else`, `return`, `try`, `catch`, `static`, `final`, `new`, `this`, `super`, `import`, `package`

* Java has **50 keywords** (as of Java 17).

---

### 2. **Identifiers**

* User-defined names for **variables**, **methods**, **classes**, **interfaces**, **arrays**, etc.
* Rules:

  * Must begin with a **letter (A–Z or a–z)**, **underscore `_`**, or **dollar sign `$`**.
  * Cannot begin with a digit.
  * Can contain letters, digits, `_`, `$`.
  * Cannot be a **Java keyword**.
  * Case-sensitive.
* Examples:

  ```java
  int count;
  String name;
  class Student {}
  ```

---

### 3. **Literals**

* Represent **constant values** assigned to variables.
* Types of literals:

  | Literal Type   | Example             |
  | -------------- | ------------------- |
  | Integer        | `10`, `-25`, `0xFF` |
  | Floating-point | `3.14`, `2.7e3`     |
  | Character      | `'A'`, `'\n'`       |
  | String         | `"Hello"`, `""`     |
  | Boolean        | `true`, `false`     |
  | Null           | `null`              |

---

### 4. **Operators**

* Symbols that perform operations on variables and values.
* Java provides many operators:

  | Category   | Examples                         |                           |         |
  | ---------- | -------------------------------- | ------------------------- | ------- |
  | Arithmetic | `+`, `-`, `*`, `/`, `%`          |                           |         |
  | Relational | `==`, `!=`, `>`, `<`, `>=`, `<=` |                           |         |
  | Logical    | `&&`, \`                         |                           | `, `!\` |
  | Assignment | `=`, `+=`, `-=`, `*=`, `/=`      |                           |         |
  | Unary      | `++`, `--`, `+`, `-`             |                           |         |
  | Bitwise    | `&`, \`                          | `, `^`, `\~`, `<<`, `>>\` |         |
  | Ternary    | `?:`                             |                           |         |
  | instanceof | `instanceof`                     |                           |         |

---

### 5. **Separators (Delimiters)**

* Used to **structure code**.
* Types:

  | Separator | Description                        |
  | --------- | ---------------------------------- |
  | `;`       | Ends a statement                   |
  | `{` `}`   | Denotes block of code              |
  | `(` `)`   | Method/constructor/loop conditions |
  | `[` `]`   | Array declaration or access        |
  | `,`       | Separates variables/arguments      |
  | `.`       | Member access operator             |

---

### 6. **Comments**

* Used to explain code; **ignored by compiler**.
* Types:

  * **Single-line comment**:

    ```java
    // This is a comment
    ```

  * **Multi-line comment**:

    ```java
    /* This is a
       multi-line comment */
    ```

  * **Documentation comment** (used with `javadoc`):

    ```java
    /**
     * This is a documentation comment
     */
    ```

---

### 3. **Summary Table**

| **Token Type** | **Example**             | **Description**                      |
| -------------- | ----------------------- | ------------------------------------ |
| Keyword        | `class`, `if`, `return` | Reserved word                        |
| Identifier     | `main`, `Student`, `x`  | User-defined name                    |
| Literal        | `10`, `'A'`, `"Java"`   | Constant value                       |
| Operator       | `+`, `==`, `&&`, `++`   | Performs operation                   |
| Separator      | `;`, `{}`, `()`, `[]`   | Structures code                      |
| Comment        | `//`, `/* */`, `/** */` | Developer notes, ignored by compiler |

---

### 4. **Conclusion**

* Tokens are the **first stage of compilation** in Java.
* Every line of Java code is **composed of a sequence of tokens**.
* Understanding tokens is **essential for syntax and error-free code construction**.

### Type Conversion in Java

---

#### 1. **Definition**

* **Type Conversion** in Java refers to the process of **converting one data type into another**.
* It is used when values of one type need to be **assigned to a variable of a different type**.

---

#### 2. **Types of Type Conversion**

| **Type**                | **Also Called**                | **Performed By** | **Conversion Direction**   |
| ----------------------- | ------------------------------ | ---------------- | -------------------------- |
| **Implicit Conversion** | Widening Conversion            | Java Compiler    | Smaller type → Larger type |
| **Explicit Conversion** | Narrowing Conversion / Casting | Programmer       | Larger type → Smaller type |

---

## A. **Implicit Type Conversion (Widening)**

#### 1. **Definition**

* Java automatically converts a **smaller data type** to a **larger data type**.
* No data is lost.
* Happens automatically when assigning compatible types.

#### 2. **Valid Conversions (Hierarchy)**

```
byte → short → int → long → float → double
                ↑
              char
```

#### 3. **Example**

```java
int a = 10;
double b = a;  // int to double conversion (implicit)
System.out.println(b); // Output: 10.0
```

#### 4. **Key Points**

* No casting is required.
* Safe conversion.
* Converts only if target type can represent all values of source type.

---

## B. **Explicit Type Conversion (Narrowing / Type Casting)**

#### 1. **Definition**

* Java requires the programmer to **manually convert a larger type to a smaller type**.
* Done using **type casting** syntax.
* May cause **loss of data or precision**.

#### 2. **Syntax**

```java
target_type variable = (target_type) value;
```

#### 3. **Example**

```java
double a = 9.78;
int b = (int) a;  // double to int (explicit casting)
System.out.println(b); // Output: 9 (decimal part lost)
```

#### 4. **Key Points**

* Required when:

  * Converting from float/double to int/long.
  * Assigning long to int, int to byte, etc.
* Data might be **truncated or altered**.
* Must use casting operator `()`.

---

## C. **Type Conversion Between Primitive Types**

| From / To | byte | short | char | int | long | float | double |
| --------- | ---- | ----- | ---- | --- | ---- | ----- | ------ |
| byte      | —    | ✔     | ✘    | ✔   | ✔    | ✔     | ✔      |
| short     | ✘    | —     | ✘    | ✔   | ✔    | ✔     | ✔      |
| char      | ✘    | ✘     | —    | ✔   | ✔    | ✔     | ✔      |
| int       | ✘    | ✘     | ✘    | —   | ✔    | ✔     | ✔      |
| long      | ✘    | ✘     | ✘    | ✘   | —    | ✔     | ✔      |
| float     | ✘    | ✘     | ✘    | ✘   | ✘    | —     | ✔      |
| double    | ✘    | ✘     | ✘    | ✘   | ✘    | ✘     | —      |

✔ = Implicit conversion possible
✘ = Requires explicit casting

---

## D. **Type Conversion with Expressions**

* Mixed-type expressions are **automatically promoted**:

### Example:

```java
int a = 5;
float b = 6.2f;
float result = a + b;  // a is promoted to float
```

* In operations, Java promotes smaller types to the **largest type** involved in the expression.

---

## E. **Conversion with Wrapper Classes**

* Java provides **wrapper classes** (`Integer`, `Double`, `Float`, etc.) for each primitive.
* These provide utility methods for conversion:

### Example:

```java
String s = "100";
int num = Integer.parseInt(s); // String to int
```

---

## F. **Common Pitfalls**

1. **Loss of precision**

   ```java
   double d = 123.456;
   int i = (int) d;  // i = 123 (fractional part lost)
   ```

2. **Overflow**

   ```java
   int a = 130;
   byte b = (byte) a;  // b = -126 (overflow due to 8-bit limit)
   ```

3. **Incompatible types**

   ```java
   int i = 100;
   boolean b = (boolean) i;  // ❌ Error: incompatible types
   ```

---

## G. **Conclusion**

* **Use implicit conversion** when moving from smaller to larger types (safe).
* **Use explicit casting** carefully when narrowing types (risk of data loss).
* Java enforces strict type safety to avoid unexpected results.

### Casting in Java

---

#### 1. **Definition**

* **Casting** is the process of **converting one data type into another** explicitly.
* Java provides two types of casting:

  * **Primitive Type Casting** (between basic data types)
  * **Reference Type Casting** (between objects/classes in inheritance hierarchy)

---

## A. **Primitive Type Casting**

---

### 1. **Types**

| **Type**              | **Name**         | **Direction** | **Description**                       |
| --------------------- | ---------------- | ------------- | ------------------------------------- |
| **Widening Casting**  | Implicit Casting | Small → Large | Done automatically by Java            |
| **Narrowing Casting** | Explicit Casting | Large → Small | Must be done manually (may lose data) |

---

### 2. **Widening Casting** (Implicit)

* Automatically performed by Java
* No data loss
* Follows type promotion hierarchy:

  ```
  byte → short → int → long → float → double
                      ↑
                    char
  ```

#### Example:

```java
int a = 10;
double b = a;  // int to double (automatically)
System.out.println(b);  // 10.0
```

---

### 3. **Narrowing Casting** (Explicit)

* Programmer must manually specify conversion using `(type)`
* May result in data **loss**, **truncation**, or **overflow**

#### Syntax:

```java
target_type variable = (target_type) value;
```

#### Example:

```java
double x = 9.99;
int y = (int) x;  // fractional part is truncated
System.out.println(y);  // 9
```

---

### 4. **Common Cases of Primitive Casting**

| From     | To       | Casting Needed | Example                    |
| -------- | -------- | -------------- | -------------------------- |
| `int`    | `double` | No             | `double d = i;`            |
| `double` | `int`    | Yes            | `int i = (int) d;`         |
| `char`   | `int`    | No             | `int i = 'A'; // i = 65`   |
| `int`    | `char`   | Yes            | `char c = (char) 65; // A` |
| `long`   | `int`    | Yes            | `int i = (int) longValue;` |

---

### 5. **Problems with Narrowing**

#### a. **Loss of Precision**

```java
float f = 3.14f;
int i = (int) f;  // i = 3
```

#### b. **Overflow or Underflow**

```java
int a = 130;
byte b = (byte) a;  // b = -126 (due to overflow)
```

---

## B. **Reference Type Casting**

---

### 1. **Used with Class Hierarchies**

* Only applicable between objects of **related classes** (inheritance or interface implementation).

---

### 2. **Types of Reference Casting**

| Type            | Direction             | Description                      |
| --------------- | --------------------- | -------------------------------- |
| **Upcasting**   | Subclass → Superclass | Done automatically (implicit)    |
| **Downcasting** | Superclass → Subclass | Must be done manually (explicit) |

---

### 3. **Upcasting (Implicit)**

* Assigning a subclass object to a superclass reference.
* Safe and automatic.

#### Example:

```java
class Animal {}
class Dog extends Animal {}

Animal a = new Dog();  // Upcasting
```

---

### 4. **Downcasting (Explicit)**

* Assigning a superclass reference back to a subclass reference.
* Requires explicit casting.
* Risky: must use `instanceof` to avoid `ClassCastException`.

#### Example:

```java
Animal a = new Dog();      // Upcasted
Dog d = (Dog) a;           // Downcasting (explicit)
```

---

### 5. **Incorrect Downcasting (Throws Exception)**

```java
Animal a = new Animal();
Dog d = (Dog) a;  // ❌ Runtime error: ClassCastException
```

#### Safe Downcasting using `instanceof`:

```java
if (a instanceof Dog) {
    Dog d = (Dog) a;
}
```

---

## C. **Casting Between Wrapper Classes**

* Wrapper classes do **not** support direct casting between each other.
* Use utility methods for conversion:

#### Example:

```java
Integer i = 100;
Double d = i.doubleValue();  // Convert Integer to Double
```

---

## D. **Casting in Expressions**

* Java promotes smaller types to larger in expressions:

```java
byte a = 10;
byte b = 20;
int c = a + b;  // a and b promoted to int
```

* Use casting to assign back:

```java
byte c = (byte)(a + b);
```

---

## E. **Conclusion**

* Use **implicit casting** when going from smaller to larger types (safe).
* Use **explicit casting** when reducing type size (may lose data).
* For **object types**, casting is only valid between **related classes**.
* Always use `instanceof` for safe downcasting.

### Arrays in Java

---

#### 1. **Definition**

* An **array** is a **container object** that holds a **fixed number of elements** of the **same data type**.
* Each element is accessed by an **index**, starting from `0`.
* Arrays are **reference types** stored in **heap memory**.

---

#### 2. **Types of Arrays**

| Type                 | Description                                         |
| -------------------- | --------------------------------------------------- |
| **One-dimensional**  | Linear collection of elements                       |
| **Multidimensional** | Arrays of arrays (e.g., 2D, 3D arrays)              |
| **Jagged Arrays**    | Multidimensional arrays with different column sizes |

---

## A. **One-Dimensional Array**

---

### 1. **Declaration**

```java
int[] arr;      // preferred
int arr[];      // valid, C-style
```

### 2. **Creation**

```java
arr = new int[5];  // allocates memory for 5 integers (default values = 0)
```

### 3. **Initialization**

```java
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
```

### 4. **Combined Declaration and Initialization**

```java
int[] arr = {10, 20, 30, 40, 50};
```

---

### 5. **Accessing Elements**

```java
System.out.println(arr[2]);  // Output: 30
```

### 6. **Array Length**

```java
System.out.println(arr.length);  // Output: 5
```

---

### 7. **Traversal Using Loop**

```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

---

### 8. **Enhanced for Loop (for-each)**

```java
for (int num : arr) {
    System.out.println(num);
}
```

---

## B. **Multidimensional Arrays**

---

### 1. **2D Array Declaration**

```java
int[][] matrix = new int[2][3];  // 2 rows, 3 columns
```

### 2. **Initialization**

```java
matrix[0][0] = 1;
matrix[1][2] = 5;
```

### 3. **Inline Initialization**

```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6}
};
```

### 4. **Traversal**

```java
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}
```

---

## C. **Jagged Arrays (Ragged Arrays)**

* Rows can have **different lengths**.

```java
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[4];
jagged[2] = new int[1];
```

---

## D. **Array Characteristics**

| Feature             | Description                                   |
| ------------------- | --------------------------------------------- |
| Fixed Size          | Once declared, array size cannot be changed   |
| Homogeneous         | Only one data type per array                  |
| Zero-Based Indexing | Index starts at `0`                           |
| Stored in Heap      | Array objects reside in heap memory           |
| Length Property     | `array.length` gives number of elements       |
| Default Values      | int → 0, boolean → false, Object → null, etc. |

---

## E. **Default Values in Arrays**

| Data Type | Default Value |
| --------- | ------------- |
| int       | 0             |
| float     | 0.0f          |
| boolean   | false         |
| char      | '\u0000'      |
| Object    | null          |

---

## F. **Common Exceptions**

| Exception                        | Cause                                     |
| -------------------------------- | ----------------------------------------- |
| `ArrayIndexOutOfBoundsException` | Accessing invalid index (e.g., `arr[10]`) |
| `NullPointerException`           | Accessing elements of a null array        |

---

## G. **Arrays Class (java.util.Arrays)**

Useful utility methods for array operations:

| Method                      | Usage Example                           |
| --------------------------- | --------------------------------------- |
| `Arrays.sort(arr)`          | Sorts the array in ascending order      |
| `Arrays.fill(arr, val)`     | Fills all elements with specified value |
| `Arrays.toString(arr)`      | Converts array to String                |
| `Arrays.equals(arr1, arr2)` | Compares two arrays for equality        |

---

### Example:

```java
import java.util.Arrays;

int[] nums = {5, 2, 9, 1};
Arrays.sort(nums);
System.out.println(Arrays.toString(nums));  // [1, 2, 5, 9]
```

---

## H. **Conclusion**

* Arrays provide a simple and efficient way to store multiple values of the same type.
* Java arrays are **fixed in size** and support **indexed access**.
* For dynamic-sized collections, Java provides **ArrayList** and other **collections**.

### Operators in Java

---

#### 1. **Definition**

* **Operators** in Java are **symbols** that perform **operations** on variables and values.
* They are used to **manipulate data**, **perform calculations**, **compare values**, and more.

---

#### 2. **Types of Operators in Java**

| Category                | Operators                               |                                  |         |
| ----------------------- | --------------------------------------- | -------------------------------- | ------- |
| Arithmetic Operators    | `+`, `-`, `*`, `/`, `%`                 |                                  |         |
| Relational (Comparison) | `==`, `!=`, `>`, `<`, `>=`, `<=`        |                                  |         |
| Logical Operators       | `&&`, \`                                |                                  | `, `!\` |
| Assignment Operators    | `=`, `+=`, `-=`, `*=`, `/=`, `%=`       |                                  |         |
| Unary Operators         | `+`, `-`, `++`, `--`, `!`               |                                  |         |
| Bitwise Operators       | `&`, \`                                 | `, `^`, `\~`, `<<`, `>>`, `>>>\` |         |
| Ternary Operator        | `?:`                                    |                                  |         |
| Instanceof Operator     | `instanceof`                            |                                  |         |
| Shift Operators         | `<<`, `>>`, `>>>`                       |                                  |         |
| Special Operators       | `.`, `[]`, `()`, `new`, `super`, `this` |                                  |         |

---

## A. **Arithmetic Operators**

| Operator | Name           | Description       | Example |
| -------- | -------------- | ----------------- | ------- |
| `+`      | Addition       | Adds values       | `a + b` |
| `-`      | Subtraction    | Subtracts values  | `a - b` |
| `*`      | Multiplication | Multiplies values | `a * b` |
| `/`      | Division       | Divides values    | `a / b` |
| `%`      | Modulus        | Returns remainder | `a % b` |

---

## B. **Relational (Comparison) Operators**

| Operator | Description              | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |
| `>`      | Greater than             | `a > b`  |
| `<`      | Less than                | `a < b`  |
| `>=`     | Greater than or equal to | `a >= b` |
| `<=`     | Less than or equal to    | `a <= b` |

---

## C. **Logical Operators**

Used for **boolean logic**, usually in conditions.

| Operator | Description | Example          |            |         |   |         |
| -------- | ----------- | ---------------- | ---------- | ------- | - | ------- |
| `&&`     | Logical AND | `a > 0 && b > 0` |            |         |   |         |
| \`       |             | \`               | Logical OR | \`a > 0 |   | b > 0\` |
| `!`      | Logical NOT | `!(a > 0)`       |            |         |   |         |

---

## D. **Assignment Operators**

Used to assign or update variable values.

| Operator | Meaning             | Example  | Equivalent To |
| -------- | ------------------- | -------- | ------------- |
| `=`      | Assign              | `a = 5`  | —             |
| `+=`     | Add and assign      | `a += 2` | `a = a + 2`   |
| `-=`     | Subtract and assign | `a -= 3` | `a = a - 3`   |
| `*=`     | Multiply and assign | `a *= 4` | `a = a * 4`   |
| `/=`     | Divide and assign   | `a /= 2` | `a = a / 2`   |
| `%=`     | Modulo and assign   | `a %= 3` | `a = a % 3`   |

---

## E. **Unary Operators**

Work on a **single operand**.

| Operator | Description                 | Example      |
| -------- | --------------------------- | ------------ |
| `+`      | Unary plus (no effect)      | `+a`         |
| `-`      | Unary minus (negates value) | `-a`         |
| `++`     | Increment (pre/post)        | `++a`, `a++` |
| `--`     | Decrement (pre/post)        | `--a`, `a--` |
| `!`      | Logical NOT                 | `!true`      |

---

### **Increment / Decrement Explanation**

| Type           | Operation Order           | Example | Description             |
| -------------- | ------------------------- | ------- | ----------------------- |
| Pre-Increment  | First increment, then use | `++a`   | `a = 5; b = ++a;` → b=6 |
| Post-Increment | First use, then increment | `a++`   | `a = 5; b = a++;` → b=5 |

---

## F. **Bitwise Operators**

Used for **binary-level operations** on integer types.

| Operator | Name                 | Description                       |                     |
| -------- | -------------------- | --------------------------------- | ------------------- |
| `&`      | AND                  | Performs bitwise AND              |                     |
| \`       | \`                   | OR                                | Performs bitwise OR |
| `^`      | XOR                  | Performs bitwise exclusive OR     |                     |
| `~`      | Complement           | Inverts all bits                  |                     |
| `<<`     | Left shift           | Shifts bits to the left           |                     |
| `>>`     | Right shift          | Shifts bits to the right (signed) |                     |
| `>>>`    | Unsigned right shift | Fills zeros from the left         |                     |

---

## G. **Ternary Operator**

* Shorthand for `if-else` condition.

#### Syntax:

```java
condition ? value_if_true : value_if_false
```

#### Example:

```java
int a = 10, b = 20;
int max = (a > b) ? a : b;  // max = 20
```

---

## H. **instanceof Operator**

* Checks if an object is an instance of a specific class or subclass.

#### Example:

```java
String s = "Java";
System.out.println(s instanceof String);  // true
```

---

## I. **Special Operators**

| Operator | Purpose                        | Example               |
| -------- | ------------------------------ | --------------------- |
| `.`      | Access class or object members | `obj.method()`        |
| `[]`     | Access array elements          | `arr[0]`              |
| `()`     | Method calls or precedence     | `method()`, `(a + b)` |
| `new`    | Object or array creation       | `new Student()`       |
| `this`   | Current class reference        | `this.name`           |
| `super`  | Superclass reference           | `super.name`          |

---

## J. **Operator Precedence**

* Determines **which operator is evaluated first** in expressions.

| Precedence | Operators                 | Associativity |               |               |
| ---------- | ------------------------- | ------------- | ------------- | ------------- |
| Highest    | `[]`, `()`, `.`           | Left to Right |               |               |
|            | `++`, `--` (post)         |               |               |               |
|            | `++`, `--`, `+`, `-`, `!` | Right to Left |               |               |
|            | `*`, `/`, `%`             | Left to Right |               |               |
|            | `+`, `-`                  | Left to Right |               |               |
|            | `<<`, `>>`, `>>>`         | Left to Right |               |               |
|            | `<`, `>`, `<=`, `>=`      | Left to Right |               |               |
|            | `==`, `!=`                | Left to Right |               |               |
|            | `&`, `^`, \`              | \`            | Left to Right |               |
|            | `&&`, \`                  |               | \`            | Left to Right |
|            | `? :`                     | Right to Left |               |               |
| Lowest     | `=`, `+=`, `-=`, etc.     | Right to Left |               |               |

---

## K. **Conclusion**

* Operators are **core tools** in Java for manipulating data.
* Java supports **rich categories** of operators, covering arithmetic, logical, comparison, bitwise, and object-oriented needs.
* **Operator precedence** and **associativity** determine the order of evaluation.

### Operator Precedence in Java

---

#### 1. **Definition**

* **Operator precedence** defines the **order** in which different **operators are evaluated** in a complex expression.
* When multiple operators are used in a single expression, **precedence determines which operator is evaluated first**.

---

#### 2. **Associativity**

* If two operators have the same precedence, **associativity** decides the evaluation direction.
* Associativity can be:

  * **Left to Right**
  * **Right to Left**

---

## 3. **Java Operator Precedence Table**

| **Precedence Level** | **Operators**                                       | **Associativity**         | **Category**                    |               |            |
| -------------------- | --------------------------------------------------- | ------------------------- | ------------------------------- | ------------- | ---------- |
| 1 (Highest)          | `[]`, `()`, `.`                                     | Left to Right             | Array, method, member access    |               |            |
| 2                    | `++`, `--` (postfix)                                | Left to Right             | Post-increment/decrement        |               |            |
| 3                    | `++`, `--`, `+`, `-`, `~`, `!` (unary)              | Right to Left             | Unary, logical NOT, bitwise NOT |               |            |
| 4                    | `*`, `/`, `%`                                       | Left to Right             | Arithmetic                      |               |            |
| 5                    | `+`, `-`                                            | Left to Right             | Arithmetic                      |               |            |
| 6                    | `<<`, `>>`, `>>>`                                   | Left to Right             | Bitwise shift                   |               |            |
| 7                    | `<`, `<=`, `>`, `>=`, `instanceof`                  | Left to Right             | Relational/comparison           |               |            |
| 8                    | `==`, `!=`                                          | Left to Right             | Equality check                  |               |            |
| 9                    | `&`                                                 | Left to Right             | Bitwise AND                     |               |            |
| 10                   | `^`                                                 | Left to Right             | Bitwise XOR                     |               |            |
| 11                   | \`                                                  | \`                        | Left to Right                   | Bitwise OR    |            |
| 12                   | `&&`                                                | Left to Right             | Logical AND                     |               |            |
| 13                   | \`                                                  |                           | \`                              | Left to Right | Logical OR |
| 14                   | `?:`                                                | Right to Left             | Ternary conditional             |               |            |
| 15                   | `=`, `+=`, `-=`, `*=`, `/=`, `%=`<br>`&=`, `^=`, \` | =`, `<<=`, `>>=`, `>>>=\` | Right to Left                   | Assignment    |            |
| 16 (Lowest)          | `,` (comma operator)                                | Left to Right             | Sequential evaluation           |               |            |

---

## 4. **Examples**

---

### A. **Arithmetic Precedence**

```java
int result = 10 + 2 * 5;
// * has higher precedence than +
// result = 10 + (2 * 5) = 10 + 10 = 20
```

---

### B. **Parentheses**

```java
int result = (10 + 2) * 5;
// ( ) evaluated first
// result = 12 * 5 = 60
```

---

### C. **Post-Increment vs Pre-Increment**

```java
int a = 5;
int b = a++;  // b = 5, a = 6 (post-increment)
int c = ++a;  // a = 7, c = 7 (pre-increment)
```

---

### D. **Assignment Associativity**

```java
int x, y, z;
x = y = z = 10;
// Assignment is right to left
// z = 10 → y = z → x = y
```

---

### E. **Ternary with Logical**

```java
int a = 5, b = 10;
int max = (a > b) ? a : b;
// a > b = false → max = b = 10
```

---

## 5. **Best Practice**

* Use **parentheses** `()` to explicitly define the evaluation order and improve code readability.
* Avoid relying only on precedence in complex expressions.

---

## 6. **Conclusion**

* **Operator precedence** determines evaluation order.
* **Associativity** handles same-precedence conflicts.
* Parentheses should be used to control or override default precedence.

### Branching in Java

---

#### 1. **Definition**

* **Branching** is a control flow mechanism that allows **decision-making** in a program.
* Based on certain **conditions**, specific blocks of code are **executed or skipped**.
* It enables a program to **choose one path over another**.

---

## 2. **Types of Branching Statements in Java**

| Statement    | Description                                        |
| ------------ | -------------------------------------------------- |
| `if`         | Executes a block if condition is true              |
| `if-else`    | Executes one of two blocks based on condition      |
| `if-else-if` | Multiple conditions, one block executes            |
| `switch`     | Replaces multiple `if-else` using case values      |
| `return`     | Exits from a method and optionally returns a value |
| `break`      | Exits from `switch` or loop                        |
| `continue`   | Skips current iteration and continues loop         |

---

## A. **`if` Statement**

* Used to execute a block of code **only if** a specified condition is **true**.

### Syntax:

```java
if (condition) {
    // code block
}
```

### Example:

```java
int num = 10;
if (num > 0) {
    System.out.println("Positive number");
}
```

---

## B. **`if-else` Statement**

* Provides an **alternative block** when the condition is **false**.

### Syntax:

```java
if (condition) {
    // executes if true
} else {
    // executes if false
}
```

### Example:

```java
int num = -5;
if (num > 0) {
    System.out.println("Positive");
} else {
    System.out.println("Negative or Zero");
}
```

---

## C. **`if-else-if` Ladder**

* Used for checking **multiple conditions** sequentially.

### Syntax:

```java
if (condition1) {
    // block 1
} else if (condition2) {
    // block 2
} else if (condition3) {
    // block 3
} else {
    // default block
}
```

### Example:

```java
int marks = 85;
if (marks >= 90) {
    System.out.println("Grade A");
} else if (marks >= 80) {
    System.out.println("Grade B");
} else {
    System.out.println("Grade C or below");
}
```

---

## D. **`switch` Statement**

* Replaces multiple `if-else` for **discrete value checking**.
* Works with `byte`, `short`, `char`, `int`, `String`, `enum`, and wrapper classes.

### Syntax:

```java
switch (expression) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

### Example:

```java
int day = 3;
switch (day) {
    case 1: System.out.println("Monday"); break;
    case 2: System.out.println("Tuesday"); break;
    case 3: System.out.println("Wednesday"); break;
    default: System.out.println("Invalid day");
}
```

---

## E. **`return` Statement**

* Exits the current method.
* Optionally returns a value.

### Example:

```java
int sum(int a, int b) {
    return a + b;
}
```

---

## F. **`break` Statement**

* Exits the current **loop** or **`switch` block** immediately.

### Example in `switch`:

```java
switch (option) {
    case 1: System.out.println("Option 1"); break;
    case 2: System.out.println("Option 2"); break;
}
```

### Example in loop:

```java
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    System.out.println(i);
}
```

---

## G. **`continue` Statement**

* **Skips the current iteration** and proceeds to the next one in a loop.

### Example:

```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    System.out.println(i);  // Skips 3
}
```

---

## 3. **Summary Table**

| Statement    | Use Case                                |
| ------------ | --------------------------------------- |
| `if`         | Execute code if condition is true       |
| `if-else`    | Choose between two blocks               |
| `if-else-if` | Multiple conditions                     |
| `switch`     | Choose from multiple discrete values    |
| `break`      | Exit loop or switch                     |
| `continue`   | Skip iteration in loop                  |
| `return`     | Exit method and optionally return value |

---

## 4. **Conclusion**

* Branching provides the **ability to control program flow**.
* Use `if-else` for **range conditions** and `switch` for **specific values**.
* Use `break` and `continue` to control **loops and cases**.

### Looping Statements in Java

---

#### 1. **Definition**

* **Looping** is a control structure that allows **repeating a block of code** multiple times until a condition is met.
* It is used for **iteration**—executing code **repeatedly** with control over how many times and under what conditions.

---

## 2. **Types of Loops in Java**

| Loop Type       | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `for` loop      | Loop with initialization, condition, and update in one line |
| `while` loop    | Entry-controlled loop; checks condition before execution    |
| `do-while` loop | Exit-controlled loop; executes at least once                |
| `for-each` loop | Enhanced `for` loop used for arrays and collections         |

---

## A. **`for` Loop**

---

### 1. **Syntax**

```java
for (initialization; condition; update) {
    // body of the loop
}
```

### 2. **Explanation**

* **Initialization**: executed once at the start.
* **Condition**: checked before every iteration; loop runs if true.
* **Update**: executed at the end of each iteration.

### 3. **Example**

```java
for (int i = 1; i <= 5; i++) {
    System.out.println("Count: " + i);
}
```

---

## B. **`while` Loop**

---

### 1. **Syntax**

```java
while (condition) {
    // body of the loop
}
```

### 2. **Explanation**

* **Condition** is evaluated **before** each iteration.
* If false, the loop will **not execute at all**.

### 3. **Example**

```java
int i = 1;
while (i <= 5) {
    System.out.println("Value: " + i);
    i++;
}
```

---

## C. **`do-while` Loop**

---

### 1. **Syntax**

```java
do {
    // body of the loop
} while (condition);
```

### 2. **Explanation**

* **Loop body executes at least once**, even if the condition is false on the first check.
* Condition is evaluated **after** executing the loop body.

### 3. **Example**

```java
int i = 1;
do {
    System.out.println("Number: " + i);
    i++;
} while (i <= 5);
```

---

## D. **Enhanced `for-each` Loop**

---

### 1. **Syntax**

```java
for (datatype var : array) {
    // body of loop
}
```

### 2. **Usage**

* Used to iterate over arrays or collections (like `ArrayList`).
* Does **not use index**.

### 3. **Example**

```java
int[] numbers = {10, 20, 30, 40};

for (int num : numbers) {
    System.out.println(num);
}
```

---

## E. **Loop Control Statements**

---

### 1. **`break`**

* **Exits** the loop prematurely.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;
    System.out.println(i);
}
```

### 2. **`continue`**

* **Skips current iteration**, continues with next.

```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    System.out.println(i); // skips 3
}
```

---

## F. **Infinite Loops**

### 1. `for` Infinite Loop

```java
for (;;) {
    // runs forever
}
```

### 2. `while` Infinite Loop

```java
while (true) {
    // runs forever
}
```

---

## G. **Comparison of Loop Types**

| Feature                | `for` Loop            | `while` Loop            | `do-while` Loop        |
| ---------------------- | --------------------- | ----------------------- | ---------------------- |
| Condition Check        | Before each iteration | Before each iteration   | After each iteration   |
| Executes at least once | No                    | No                      | **Yes**                |
| Use Case               | Known iteration count | Unknown iteration count | Must run at least once |

---

## H. **Nested Loops**

* A loop inside another loop.

```java
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 2; j++) {
        System.out.println("i=" + i + ", j=" + j);
    }
}
```

---

## I. **Conclusion**

* Java provides **four loop types** for various control needs.
* `for`, `while`, and `do-while` cover **all general looping logic**.
* Use `break` and `continue` to fine-tune loop execution.
* Prefer `for-each` for **cleaner array/collection iteration**.

### Classes in Java

---

#### 1. **Definition**

* A **class** in Java is a **user-defined blueprint or prototype** from which **objects** are created.
* It defines **properties (fields)** and **behaviors (methods)** common to all objects of that type.
* A class is a **reference data type** in Java.

---

#### 2. **Syntax of Class Declaration**

```java
class ClassName {
    // Fields (data members)
    // Methods (member functions)
}
```

---

#### 3. **Example of a Simple Class**

```java
class Student {
    // Fields
    int id;
    String name;

    // Method
    void display() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}
```

---

## A. **Components of a Class**

---

### 1. **Fields (Instance Variables)**

* Represent the **state** or **attributes** of an object.
* Declared inside the class but outside methods.

```java
int age;
String name;
```

---

### 2. **Methods**

* Define the **behavior** or **functionality** of the class.
* Can operate on fields and perform operations.

```java
void greet() {
    System.out.println("Hello");
}
```

---

### 3. **Constructors**

* Special methods used to **initialize objects**.
* Called automatically when an object is created.

```java
Student() {
    id = 1;
    name = "Default";
}
```

---

### 4. **Blocks (Static & Instance)**

* **Instance block**: runs every time object is created.
* **Static block**: runs once when class is loaded.

```java
{
    // instance block
}

static {
    // static block
}
```

---

### 5. **Nested Classes**

* Classes can be declared inside another class.

```java
class Outer {
    class Inner {
        // inner class
    }
}
```

---

## B. **Creating an Object (Instance) of a Class**

```java
ClassName objectName = new ClassName();
```

### Example:

```java
Student s1 = new Student();  // Object creation
s1.id = 101;
s1.name = "Alice";
s1.display();                // Method call
```

---

## C. **Access Modifiers for Class Members**

| Modifier    | Accessible Within       | Accessible Outside Package |
| ----------- | ----------------------- | -------------------------- |
| `private`   | Same class only         | ❌                          |
| `default`   | Same package            | ❌                          |
| `protected` | Same package + subclass | ✔ in subclass              |
| `public`    | Everywhere              | ✔                          |

---

## D. **Types of Classes**

| Type                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| **Concrete class**      | Regular class with full implementation              |
| **Abstract class**      | Cannot be instantiated; contains abstract methods   |
| **Final class**         | Cannot be subclassed                                |
| **Static nested class** | Static class declared inside another class          |
| **Inner class**         | Non-static class declared inside another class      |
| **Anonymous class**     | Class without a name, defined at instantiation time |

---

## E. **Class vs Object**

| Class                  | Object                                 |
| ---------------------- | -------------------------------------- |
| Blueprint or template  | Instance of the class                  |
| Does not occupy memory | Occupies memory                        |
| Defined once           | Can create many objects from one class |

---

## F. **Memory Allocation for Class Members**

| Member Type        | When Memory Allocated  | Scope                     |
| ------------------ | ---------------------- | ------------------------- |
| Instance variables | When object is created | Specific to each object   |
| Static variables   | When class is loaded   | Shared by all objects     |
| Local variables    | When method/block runs | Exist within method/block |

---

## G. **Important Keywords**

| Keyword    | Use                                           |
| ---------- | --------------------------------------------- |
| `class`    | Declares a class                              |
| `new`      | Creates an object                             |
| `this`     | Refers to current object                      |
| `static`   | Belongs to class, not object                  |
| `final`    | Prevents modification (constant/class/method) |
| `abstract` | Declares an abstract class/method             |

---

## H. **Example Program**

```java
class Car {
    String brand;
    int speed;

    void start() {
        System.out.println(brand + " is starting at speed " + speed);
    }
}

public class Main {
    public static void main(String[] args) {
        Car c1 = new Car();
        c1.brand = "BMW";
        c1.speed = 100;
        c1.start();
    }
}
```

---

## I. **Conclusion**

* A **class** is the foundation of **object-oriented programming** in Java.
* It encapsulates **data** and **behavior** and supports features like **encapsulation**, **inheritance**, and **polymorphism**.

### Objects in Java

---

#### 1. **Definition**

* An **object** is a **runtime instance** of a class.
* It contains **fields (data/state)** and can perform **methods (behavior)** defined in its class.
* Objects are created using the `new` keyword.

---

#### 2. **Key Characteristics of Objects**

| Characteristic | Description                       |
| -------------- | --------------------------------- |
| **Identity**   | Unique reference in memory        |
| **State**      | Values of its fields (attributes) |
| **Behavior**   | Actions defined by its methods    |

---

#### 3. **Creating an Object**

```java
ClassName objectName = new ClassName();
```

#### Example:

```java
class Student {
    int id;
    String name;

    void display() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();  // object created
        s1.id = 101;
        s1.name = "Alice";
        s1.display();                // calling method on object
    }
}
```

---

#### 4. **Accessing Object Members**

* Use **dot (`.`) operator** to access fields and methods.

```java
s1.id = 100;        // accessing field
s1.display();       // invoking method
```

---

#### 5. **Multiple Objects of Same Class**

```java
Student s1 = new Student();
Student s2 = new Student();

s1.id = 1; s1.name = "John";
s2.id = 2; s2.name = "Jane";

s1.display();
s2.display();
```

Each object has its **own copy** of instance variables.

---

#### 6. **Object Memory Allocation**

* Objects are stored in **heap memory**.
* **Reference variables** store the address of the object in **stack memory**.

---

#### 7. **Reference vs Object**

| Term          | Description                                  |
| ------------- | -------------------------------------------- |
| **Object**    | The real entity created using `new`          |
| **Reference** | Variable that points to the object in memory |

```java
Student s = new Student();  // s is reference, object is on heap
```

---

#### 8. **Anonymous Object**

* Created without a reference.
* Useful for one-time use.

```java
new Student().display();  // No variable assigned
```

---

#### 9. **Array of Objects**

```java
Student[] students = new Student[3];
students[0] = new Student();
students[1] = new Student();
students[2] = new Student();
```

---

#### 10. **Passing Objects to Methods**

```java
void printStudent(Student s) {
    System.out.println(s.name);
}
```

---

#### 11. **Returning Object from Method**

```java
Student getStudent() {
    Student s = new Student();
    return s;
}
```

---

#### 12. **Object Lifecycle**

| Phase                  | Description                                    |
| ---------------------- | ---------------------------------------------- |
| **Creation**           | Using `new`                                    |
| **Usage**              | Accessing fields/methods                       |
| **Garbage Collection** | Unreferenced object is destroyed automatically |

---

#### 13. **Important Object Concepts**

| Concept            | Description                                         |
| ------------------ | --------------------------------------------------- |
| `this` keyword     | Refers to the current object                        |
| `null` reference   | A reference that points to no object                |
| Garbage Collection | JVM automatically reclaims memory of unused objects |

---

#### 14. **Example with `this` Keyword**

```java
class Student {
    int id;
    String name;

    Student(int id, String name) {
        this.id = id;          // 'this' refers to current object
        this.name = name;
    }
}
```

---

#### 15. **Conclusion**

* An **object** is an **instance of a class**, created using `new`.
* Objects store **individual data** and provide **access to class methods**.
* Java manages object memory automatically using **Garbage Collection**.

### Methods in Java

---

#### 1. **Definition**

* A **method** is a **block of code** that performs a **specific task**.
* It is also known as a **function** in other programming languages.
* Methods are used to **define behavior** in classes, to **reuse code**, and to **organize logic**.

---

## 2. **Syntax of a Method**

```java
return_type methodName(parameter_list) {
    // method body
}
```

### Example:

```java
int add(int a, int b) {
    return a + b;
}
```

---

## 3. **Types of Methods in Java**

| Type                        | Description                                      |
| --------------------------- | ------------------------------------------------ |
| **Instance Method**         | Operates on instance variables                   |
| **Static Method**           | Belongs to class, not objects (`static` keyword) |
| **Parameterized Method**    | Accepts parameters                               |
| **Method with Return Type** | Returns a value to the caller                    |
| **Void Method**             | Returns nothing (`void` return type)             |

---

## 4. **Example of Various Method Types**

```java
class MathUtil {
    int square(int x) {              // instance method
        return x * x;
    }

    static int cube(int x) {         // static method
        return x * x * x;
    }

    void show() {                    // void method
        System.out.println("This is MathUtil class");
    }
}
```

---

## 5. **Method Declaration Components**

| Component           | Description                                            |
| ------------------- | ------------------------------------------------------ |
| **Access Modifier** | `public`, `private`, `protected`, or default           |
| **Return Type**     | Type of value returned (`int`, `void`, `String`, etc.) |
| **Method Name**     | Valid Java identifier                                  |
| **Parameters**      | Inputs to the method                                   |
| **Method Body**     | Block of code that runs when method is called          |

---

## 6. **Calling a Method**

### A. **Instance Method (Using Object)**

```java
MathUtil m = new MathUtil();
int result = m.square(5);
```

### B. **Static Method (Using Class Name)**

```java
int result = MathUtil.cube(3);
```

---

## 7. **Method Overloading**

* Defining **multiple methods** with the **same name** but **different parameter lists**.
* Helps in **compile-time polymorphism**.

### Example:

```java
class Display {
    void show(int x) {
        System.out.println("Integer: " + x);
    }

    void show(String s) {
        System.out.println("String: " + s);
    }
}
```

---

## 8. **Return Statement**

* Used to **exit** from a method and **return a value**.

```java
int multiply(int a, int b) {
    return a * b;
}
```

---

## 9. **Parameter Passing in Java**

| Method            | Behavior                                       |
| ----------------- | ---------------------------------------------- |
| **Pass by Value** | Java **always** passes arguments **by value**. |

```java
void change(int x) {
    x = x + 10;  // doesn't change original value
}
```

---

## 10. **Access Modifiers with Methods**

| Modifier    | Scope                                         |
| ----------- | --------------------------------------------- |
| `public`    | Accessible from anywhere                      |
| `private`   | Accessible within the same class only         |
| `protected` | Accessible in the same package and subclasses |
| (default)   | Accessible within the same package only       |

---

## 11. **Recursive Method**

* A method that **calls itself**.

```java
int factorial(int n) {
    if (n == 1) return 1;
    else return n * factorial(n - 1);
}
```

---

## 12. **Varargs (Variable Arguments)**

* Allows passing **zero or more arguments** of the same type.

```java
void printNumbers(int... nums) {
    for (int n : nums) {
        System.out.println(n);
    }
}
```

---

## 13. **Method Signature**

* Combination of **method name** and **parameter list** (not return type).
* Used by compiler to **identify overloaded methods**.

```java
void sum(int a, int b);     // signature: sum(int, int)
```

---

## 14. **Main Method**

* Entry point of Java program.

```java
public static void main(String[] args) {
    // program starts here
}
```

---

## 15. **Difference: Instance vs Static Method**

| Feature    | Instance Method           | Static Method                |
| ---------- | ------------------------- | ---------------------------- |
| Belongs to | Object                    | Class                        |
| Access     | Using object              | Using class name or directly |
| Can access | Instance + static members | Only static members          |

---

## 16. **Conclusion**

* **Methods** are used for **encapsulation**, **code reuse**, and **logic abstraction**.
* They can be **static** or **instance**, and may **return values** or perform **actions** directly.
* Java supports **method overloading**, **recursion**, and **varargs** for flexible functionality.

### Constructors in Java

---

#### 1. **Definition**

* A **constructor** is a **special method** that is **automatically invoked** when an object of a class is **created**.
* Its purpose is to **initialize** objects (assign values to instance variables).
* Constructors **do not have a return type**, not even `void`.

---

## 2. **Syntax**

```java
class ClassName {
    ClassName() {
        // constructor body
    }
}
```

---

## 3. **Types of Constructors**

| Constructor Type              | Description                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| **Default Constructor**       | No parameters; provided by compiler if no constructor is defined                      |
| **No-arg Constructor**        | Defined explicitly with no arguments                                                  |
| **Parameterized Constructor** | Accepts parameters for customized initialization                                      |
| **Copy Constructor**          | Creates an object by copying data from another object (manual implementation in Java) |

---

## A. **Default Constructor**

* Provided **implicitly** by the compiler if no constructor is declared.
* Initializes instance variables to **default values**.

```java
class Demo {
    int x;

    // compiler provides: Demo() {}
}
```

---

## B. **No-argument Constructor**

* Constructor defined **explicitly** with no parameters.

```java
class Demo {
    int x;

    Demo() {
        x = 10;
        System.out.println("No-arg constructor called");
    }
}
```

---

## C. **Parameterized Constructor**

* Takes arguments to initialize fields during object creation.

```java
class Student {
    int id;
    String name;

    Student(int i, String n) {
        id = i;
        name = n;
    }
}
```

---

## D. **Copy Constructor (Manual Implementation)**

* Java does not provide built-in copy constructors like C++, but you can define your own.

```java
class Book {
    String title;

    Book(String t) {
        title = t;
    }

    Book(Book b) {
        title = b.title;
    }
}
```

---

## 4. **Constructor Overloading**

* Multiple constructors can be defined in the same class with **different parameter lists**.
* Enables **flexible initialization**.

```java
class Person {
    String name;
    int age;

    Person() {
        name = "Unknown";
        age = 0;
    }

    Person(String n, int a) {
        name = n;
        age = a;
    }
}
```

---

## 5. **Constructor vs Method**

| Feature     | Constructor                          | Method                              |
| ----------- | ------------------------------------ | ----------------------------------- |
| Name        | Same as class name                   | Any valid identifier                |
| Return type | None (not even void)                 | Must have return type (can be void) |
| Invocation  | Automatically during object creation | Manually using object               |
| Purpose     | Initializes object                   | Performs operations                 |

---

## 6. **Use of `this()` in Constructor**

* Used to call **another constructor** in the same class.

```java
class Employee {
    int id;
    String name;

    Employee() {
        this(0, "Unknown");
    }

    Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

---

## 7. **Use of `super()` in Constructor**

* Calls the **parent class constructor**.
* Must be the **first statement** in the subclass constructor.

```java
class Animal {
    Animal() {
        System.out.println("Animal constructor");
    }
}

class Dog extends Animal {
    Dog() {
        super();
        System.out.println("Dog constructor");
    }
}
```

---

## 8. **Private Constructor**

* Used to **restrict object creation** from outside the class.
* Common in **Singleton Design Pattern**.

```java
class Singleton {
    private Singleton() {}

    static Singleton obj = new Singleton();
}
```

---

## 9. **Constructor Chaining**

* Refers to **calling one constructor from another** using `this()` or `super()`.

```java
class Chain {
    Chain() {
        this(10);
    }

    Chain(int x) {
        System.out.println("Value: " + x);
    }
}
```

---

## 10. **Memory Allocation**

* Constructor does **not allocate memory**; the `new` keyword does.
* Constructor **initializes** memory after allocation.

---

## 11. **Rules of Constructor**

* Constructor name must be **identical** to the class name.
* Cannot have a return type.
* Can be **overloaded**, but not **overridden**.
* Can be declared **private, public, protected**, or **default**.

---

## 12. **Conclusion**

* **Constructors** are vital for **object initialization**.
* Java supports **multiple types** of constructors for flexibility.
* **Overloading**, `this()`, `super()`, and access modifiers give full control over how objects are initialized.

### `this` Keyword in Java

---

#### 1. **Definition**

* The **`this` keyword** is a **reference variable** in Java that refers to the **current object** of the class.
* It is used to **distinguish between instance variables and parameters** or to **invoke other members** of the current class.

---

## 2. **Key Uses of `this` Keyword**

| Use Case                                      | Description                                     |
| --------------------------------------------- | ----------------------------------------------- |
| Referring current class **instance variable** | When local and instance variable names are same |
| Calling **current class method**              | To invoke a method within the same class        |
| Calling **current class constructor**         | Used in constructor chaining with `this()`      |
| Passing current object as argument            | Can be passed to methods or constructors        |
| Returning current object                      | Useful for method chaining                      |

---

## 3. **Use Case 1: Referring Current Class Instance Variables**

* Used to **resolve naming conflict** between instance variables and parameters.

```java
class Student {
    int id;
    String name;

    Student(int id, String name) {
        this.id = id;         // refers to instance variable
        this.name = name;
    }
}
```

---

## 4. **Use Case 2: Calling Current Class Method**

```java
class Demo {
    void show() {
        System.out.println("Show method");
    }

    void display() {
        this.show();  // same as just show()
    }
}
```

---

## 5. **Use Case 3: Calling Current Class Constructor**

* Used for **constructor chaining** using `this()`.

```java
class Book {
    String title;
    double price;

    Book() {
        this("Unknown", 0.0);  // calls parameterized constructor
    }

    Book(String title, double price) {
        this.title = title;
        this.price = price;
    }
}
```

**Note:** `this()` must be the **first statement** in the constructor.

---

## 6. **Use Case 4: Passing `this` as Argument**

```java
class A {
    void display() {
        System.out.println("Display method");
    }

    void call(A obj) {
        obj.display();
    }

    void start() {
        call(this);  // passing current object as argument
    }
}
```

---

## 7. **Use Case 5: Returning Current Object**

* Enables **method chaining**.

```java
class Counter {
    int count = 0;

    Counter increment() {
        count++;
        return this;  // returns current object
    }

    void display() {
        System.out.println("Count: " + count);
    }
}

class Main {
    public static void main(String[] args) {
        new Counter().increment().increment().display();  // method chaining
    }
}
```

---

## 8. **Important Points**

* `this` can **only be used inside non-static methods or constructors**.
* `this` **cannot be used in static methods** because static methods do not belong to any object.
* `this` is **automatically available** in all instance methods and constructors.

---

## 9. **Internal Behavior of `this`**

* Java **implicitly** passes `this` to all non-static methods.
* It helps the JVM identify **which object’s fields/methods** are being referred to.

---

## 10. **Conclusion**

* `this` is a **powerful reference** to the **current object**.
* It ensures clarity and consistency when accessing members, helps in **constructor chaining**, **method chaining**, and **passing object references**.

### `super` Keyword in Java

---

#### 1. **Definition**

* The **`super`** keyword in Java is a reference variable used to **refer to the immediate parent class object**.
* It is mainly used in **inheritance** to access **parent class members** (variables, methods, and constructors) that are **overridden or hidden** in the child class.

---

## 2. **Key Uses of `super` Keyword**

| Use Case                             | Description                                                       |
| ------------------------------------ | ----------------------------------------------------------------- |
| Accessing **parent class variables** | When child and parent have same variable names                    |
| Invoking **parent class methods**    | When child class overrides parent method                          |
| Calling **parent class constructor** | To invoke parent’s constructor from child constructor (`super()`) |

---

## 3. **Use Case 1: Accessing Parent Class Variables**

```java
class Animal {
    String color = "White";
}

class Dog extends Animal {
    String color = "Black";

    void printColor() {
        System.out.println(super.color);  // accesses Animal's color
    }
}
```

**Output:**

```
White
```

---

## 4. **Use Case 2: Invoking Parent Class Method**

```java
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void sound() {
        super.sound();  // calls Animal's sound()
        System.out.println("Dog barks");
    }
}
```

**Output:**

```
Animal makes a sound  
Dog barks
```

---

## 5. **Use Case 3: Calling Parent Class Constructor**

* `super()` is used to call **parent class constructor** from the **subclass constructor**.
* Must be the **first statement** in the constructor.

```java
class Animal {
    Animal() {
        System.out.println("Animal constructor");
    }
}

class Dog extends Animal {
    Dog() {
        super();  // calls Animal()
        System.out.println("Dog constructor");
    }
}
```

**Output:**

```
Animal constructor  
Dog constructor
```

---

## 6. **Constructor Overloading with `super()`**

```java
class Animal {
    Animal(String type) {
        System.out.println("Animal type: " + type);
    }
}

class Dog extends Animal {
    Dog() {
        super("Dog");  // passes parameter to parent constructor
    }
}
```

**Output:**

```
Animal type: Dog
```

---

## 7. **Important Rules**

* `super()` must be **first statement** in the subclass constructor.
* If not explicitly called, **Java automatically calls the parent class’s default constructor**.
* Can only be used in **non-static context**.
* Can be used only in **subclasses**.

---

## 8. **`super` vs `this` Keyword**

| Feature   | `super`                        | `this`                               |
| --------- | ------------------------------ | ------------------------------------ |
| Refers to | Parent class object            | Current class object                 |
| Access    | Parent class methods/variables | Current class methods/variables      |
| Used in   | Subclass                       | Any class                            |
| Calls     | Parent constructor (`super()`) | Current class constructor (`this()`) |

---

## 9. **Example Program Using All Forms of `super`**

```java
class Vehicle {
    int speed = 60;

    Vehicle() {
        System.out.println("Vehicle constructor");
    }

    void display() {
        System.out.println("Speed: " + speed);
    }
}

class Car extends Vehicle {
    int speed = 120;

    Car() {
        super();              // calling parent constructor
    }

    void show() {
        super.display();      // calling parent method
        System.out.println("Speed: " + super.speed);  // accessing parent variable
    }
}
```

---

## 10. **Conclusion**

* The `super` keyword is essential for **inheritance handling** in Java.
* It enables **interaction with parent class members** that are overridden, and ensures **constructor chaining** for proper object initialization.

### `final` Keyword in Java

---

#### 1. **Definition**

* The **`final`** keyword in Java is used to **restrict** the user.
* It can be applied to:

  * **Variables** → to make constants (unchangeable values)
  * **Methods** → to prevent method overriding
  * **Classes** → to prevent inheritance

---

## 2. **Usage of `final` Keyword**

| Usage            | Purpose                                   |
| ---------------- | ----------------------------------------- |
| `final` variable | Value cannot be changed (constant)        |
| `final` method   | Cannot be overridden in a subclass        |
| `final` class    | Cannot be inherited (no subclass allowed) |

---

## 3. **`final` Variable**

### A. **Instance Variable**

```java
class Demo {
    final int MAX = 100;

    void show() {
        // MAX = 200;  // Error: cannot assign a value to final variable
    }
}
```

### B. **Local Variable**

```java
void display() {
    final int x = 10;
    // x = 20;  // Error
}
```

### C. **Blank Final Variable**

* Declared without initialization, but must be assigned **once** (e.g., in constructor).

```java
class Test {
    final int data;

    Test(int d) {
        data = d;  // initialized once here
    }
}
```

### D. **Static Final Variable (Constant)**

```java
class Constants {
    static final double PI = 3.14159;
}
```

---

## 4. **`final` Method**

* A method declared `final` **cannot be overridden** in any subclass.

```java
class A {
    final void display() {
        System.out.println("Final method");
    }
}

class B extends A {
    // void display() {}  // Error: cannot override final method
}
```

---

## 5. **`final` Class**

* A class declared `final` **cannot be extended/inherited**.

```java
final class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

// class Dog extends Animal {}  // Error: cannot subclass final class
```

---

## 6. **final with Reference Variables**

* The reference **cannot be changed**, but **the object’s state can be changed**.

```java
final int[] arr = {1, 2, 3};
arr[0] = 10;  // allowed
// arr = new int[5];  // Error: cannot reassign reference
```

---

## 7. **Characteristics and Rules**

| Feature                 | Description                      |
| ----------------------- | -------------------------------- |
| Value reassignment      | Not allowed for final variables  |
| Method overriding       | Not allowed for final methods    |
| Class inheritance       | Not allowed for final classes    |
| Variable initialization | Must be initialized exactly once |
| Compiler enforcement    | Enforced at **compile time**     |

---

## 8. **Difference between `final`, `finally`, and `finalize()`**

| Keyword      | Purpose                                                      |
| ------------ | ------------------------------------------------------------ |
| `final`      | Restriction modifier (class, method, var)                    |
| `finally`    | Block used with `try-catch` (executes always)                |
| `finalize()` | Method called by garbage collector before object destruction |

---

## 9. **Example Using All Three Uses**

```java
final class Base {
    final int x = 10;

    final void show() {
        System.out.println("Base show");
    }
}

class Main {
    public static void main(String[] args) {
        Base b = new Base();
        System.out.println(b.x);
        b.show();
    }
}
```

---

## 10. **Conclusion**

* The `final` keyword is used for **immutability**, **security**, and **optimization**.
* It ensures that **variables cannot change**, **methods are not overridden**, and **classes are not extended**, helping in writing **robust and predictable code**.


