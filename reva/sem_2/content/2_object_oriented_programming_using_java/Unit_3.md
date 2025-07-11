# Unit - 3 -> Packages, Interfaces, Multitherading and Exception Handling
Creation of User defined Packages, Importing Packages, Accessing Inbuilt Packages.
Introduction to Interfaces, Features of Interfaces, Creation of Interfaces.
Introduction to Multithreading, Life Cycle of A Thread, Creation of a Thread.
Exception Handling, Creation of User Defined Exceptions, Understanding the keywords in Java
- try, catch, throw, throws and finally, Examples on Exveption Handling.

## Content ->
### Creation of User Defined Packages in Java

---

#### 1. **Definition of Package**

* A **package** in Java is a **namespace** that organizes a set of related classes and interfaces.
* Helps avoid **name conflicts**, provides **modularity**, and supports **access protection**.

---

## 2. **Types of Packages**

| Type         | Description                               |
| ------------ | ----------------------------------------- |
| Built-in     | Provided by Java (`java.util`, `java.io`) |
| User-defined | Created by the programmer                 |

---

## 3. **Steps to Create a User Defined Package**

---

### **Step 1: Declare the Package**

* Use the `package` keyword at the **top of the Java file**.

```java
package mypack;
```

---

### **Step 2: Create Java Classes/Interfaces in the Package**

* Save the class in a `.java` file under a directory with the **same name as the package**.

```java
// File: mypack/Message.java
package mypack;

public class Message {
    public void show() {
        System.out.println("This is a message from user-defined package.");
    }
}
```

---

### **Step 3: Compile the Class with Package Structure**

* Use `javac` with `-d` option to place the class file in the correct folder.

```bash
javac -d . mypack/Message.java
```

> This creates a directory `mypack` with the compiled `Message.class` inside it.

---

### **Step 4: Use the Package in Another Class**

* Import the package using the `import` keyword.
* Or, use the fully qualified name.

```java
// File: Main.java
import mypack.Message;

public class Main {
    public static void main(String[] args) {
        Message m = new Message();
        m.show();
    }
}
```

---

### **Step 5: Compile and Run**

```bash
javac Main.java
java Main
```

---

## 4. **Directory Structure**

```
project/
│
├── mypack/
│   └── Message.java
│
└── Main.java
```

After compilation:

```
project/
│
├── mypack/
│   └── Message.class
│
├── Message.java
├── Main.java
└── Main.class
```

---

## 5. **Points to Remember**

| Rule / Note                               | Description                                         |
| ----------------------------------------- | --------------------------------------------------- |
| Package name = directory name             | Folder must match package name                      |
| `package` must be **first**               | No statements (except comments) before `package`    |
| Classes with `public` need same file name | Public class name must match file name              |
| Use `-d` flag in `javac`                  | To create proper directory structure during compile |

---

## 6. **Multiple Classes in a Package**

```java
// File: mypack/Hello.java
package mypack;
public class Hello {
    public void sayHello() {
        System.out.println("Hello from Hello class");
    }
}

// File: mypack/Greet.java
package mypack;
public class Greet {
    public void sayGreet() {
        System.out.println("Greetings from Greet class");
    }
}
```

---

## 7. **Using Fully Qualified Name (No `import`)**

```java
public class Test {
    public static void main(String[] args) {
        mypack.Message m = new mypack.Message();
        m.show();
    }
}
```

---

## 8. **Nested Packages**

```java
// File: com/example/tools/Tool.java
package com.example.tools;

public class Tool {
    public void run() {
        System.out.println("Tool from nested package.");
    }
}
```

Compile with:

```bash
javac -d . com/example/tools/Tool.java
```

---

## 9. **Advantages of Using Packages**

| Advantage            | Description                                          |
| -------------------- | ---------------------------------------------------- |
| Avoid name conflicts | Classes in different packages can have the same name |
| Controlled access    | Use access modifiers (private, protected, public)    |
| Easier maintenance   | Related classes grouped together                     |
| Reusability          | Packages can be imported and reused                  |

---

## 10. **Conclusion**

* Creating user-defined packages involves:

  * Declaring with `package`
  * Organizing directory structure
  * Using `javac -d` to compile
  * Importing and accessing from other classes
* Packages support **modular**, **reusable**, and **organized** Java programming.

### Importing Packages in Java

---

#### 1. **Definition**

* **Importing packages** means making the **classes or interfaces** from another package **accessible** in the current Java program.
* Achieved using the `import` keyword.
* Allows using **fully qualified names** or **simplified references** to access classes from packages.

---

## 2. **Syntax of `import` Statement**

```java
import package_name.ClassName;         // To import a specific class
import package_name.*;                 // To import all classes in a package
```

* `import` statements must appear **after the `package` statement (if any)** and **before any class definition**.

---

## 3. **Types of Importing**

| Type                     | Syntax Example                    | Description                                     |
| ------------------------ | --------------------------------- | ----------------------------------------------- |
| **Single Type Import**   | `import java.util.Scanner;`       | Imports only one class from a package           |
| **On-Demand Import**     | `import java.util.*;`             | Imports all classes and interfaces from package |
| **Static Import**        | `import static java.lang.Math.*;` | Imports static members like `PI`, `sqrt()` etc. |
| **Fully Qualified Name** | No `import` used                  | Directly use package + class in code            |

---

## 4. **Examples**

### A. **Single Type Import**

```java
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    }
}
```

---

### B. **On-Demand Import**

```java
import java.util.*;

public class Test {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
    }
}
```

---

### C. **Static Import**

```java
import static java.lang.Math.*;

public class Test {
    public static void main(String[] args) {
        double x = sqrt(16);     // No need to write Math.sqrt()
        System.out.println(PI);  // No need to write Math.PI
    }
}
```

---

### D. **Fully Qualified Name (No Import)**

```java
public class Test {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
    }
}
```

---

## 5. **Importing User-Defined Packages**

### Step-by-Step:

1. **Create the package**

```java
// File: mypack/Message.java
package mypack;

public class Message {
    public void display() {
        System.out.println("User-defined package class");
    }
}
```

2. **Import the package in another class**

```java
// File: Test.java
import mypack.Message;

public class Test {
    public static void main(String[] args) {
        Message m = new Message();
        m.display();
    }
}
```

3. **Compile and run**

```bash
javac -d . mypack/Message.java
javac Test.java
java Test
```

---

## 6. **Rules and Restrictions**

| Rule                                  | Explanation                                        |
| ------------------------------------- | -------------------------------------------------- |
| `import` must come after `package`    | Cannot be placed below class or method             |
| Class must be `public` to be imported | Or it won’t be accessible outside its package      |
| Cannot import sub-packages with `*`   | `import java.*;` does **not** import `java.util.*` |
| Redundant imports ignored             | Compiler avoids loading unused imports             |

---

## 7. **Packages Commonly Imported**

| Package     | Purpose                                                   |
| ----------- | --------------------------------------------------------- |
| `java.lang` | Core classes (`String`, `Math`, etc.) – **auto-imported** |
| `java.util` | Collections, Date, Scanner                                |
| `java.io`   | Input/output streams                                      |
| `java.net`  | Networking classes                                        |
| `java.sql`  | JDBC classes                                              |

---

## 8. **Static Import: Detailed**

* Allows access to **static fields and methods** directly.

### Example:

```java
import static java.lang.Math.max;

public class Test {
    public static void main(String[] args) {
        int a = max(5, 10);  // No need to write Math.max
        System.out.println(a);
    }
}
```

---

## 9. **Importing from Multiple Packages**

```java
import java.util.Scanner;
import java.io.*;

public class Test {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    }
}
```

---

## 10. **Conclusion**

* `import` provides a way to **reuse classes** from other packages without writing full names.
* Supports **modular** and **organized** programming by separating code into logical packages.
* Multiple ways exist: **single type, on-demand, static, or fully qualified**, depending on use case.

### Accessing Inbuilt Packages in Java

---

#### 1. **Definition**

* **Inbuilt packages** (also called **standard** or **predefined packages**) are packages provided by **Java’s API**.
* They contain classes and interfaces for **input/output**, **collections**, **networking**, **GUI**, **math**, **threading**, **database access**, etc.
* These are found in the **Java Development Kit (JDK)** and are located in the `java.*` and `javax.*` namespaces.

---

## 2. **Common Inbuilt Packages**

| Package Name    | Purpose / Contains Classes For            |
| --------------- | ----------------------------------------- |
| `java.lang`     | Core classes (String, Math, Object, etc.) |
| `java.util`     | Collections, Date, Scanner, etc.          |
| `java.io`       | Input/output streams                      |
| `java.net`      | Networking (Socket, URL, etc.)            |
| `java.sql`      | JDBC and database operations              |
| `java.awt`      | Abstract Window Toolkit (GUI programming) |
| `javax.swing`   | GUI components (buttons, frames, etc.)    |
| `java.time`     | Date and time API (Java 8+)               |
| `java.math`     | BigInteger, BigDecimal                    |
| `java.nio`      | Non-blocking I/O                          |
| `java.security` | Cryptography and security                 |

---

## 3. **How to Access Inbuilt Packages**

There are **3 ways** to access classes from inbuilt packages:

---

### A. **No Import Needed (java.lang)**

* The `java.lang` package is **automatically imported** in every Java program.
* Contains essential classes.

```java
public class Demo {
    public static void main(String[] args) {
        String name = "Java";      // from java.lang.String
        System.out.println(name);  // from java.lang.System
    }
}
```

---

### B. **Explicit Import (Single Class)**

* Use `import` to access one class from a package.

```java
import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    }
}
```

---

### C. **Wildcard Import (All Classes in Package)**

* Use `*` to import all classes/interfaces from a package.

```java
import java.util.*;

public class Demo {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
    }
}
```

---

## 4. **Examples of Accessing Inbuilt Packages**

---

### A. **Using `java.util` (Collection and Scanner)**

```java
import java.util.*;

public class Example {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<>();
        names.add("Java");
    }
}
```

---

### B. **Using `java.io` (File and Stream classes)**

```java
import java.io.*;

public class FileRead {
    public static void main(String[] args) throws IOException {
        FileReader fr = new FileReader("data.txt");
        int ch;
        while((ch = fr.read()) != -1) {
            System.out.print((char) ch);
        }
        fr.close();
    }
}
```

---

### C. **Using `java.net` (Networking)**

```java
import java.net.*;

public class NetworkExample {
    public static void main(String[] args) throws UnknownHostException {
        InetAddress ip = InetAddress.getLocalHost();
        System.out.println("IP Address: " + ip.getHostAddress());
    }
}
```

---

### D. **Using `javax.swing` (GUI)**

```java
import javax.swing.*;

public class SwingDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Demo");
        JButton btn = new JButton("Click");
        frame.add(btn);
        frame.setSize(200, 100);
        frame.setVisible(true);
    }
}
```

---

## 5. **Accessing Classes without `import` (Fully Qualified Name)**

```java
public class Test {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
    }
}
```

---

## 6. **Rules for Accessing Inbuilt Packages**

| Rule                              | Explanation                                                   |
| --------------------------------- | ------------------------------------------------------------- |
| `import` must be before class     | All imports must come before class definition                 |
| Only `java.lang` is auto-imported | All other packages must be imported manually                  |
| `*` does not include sub-packages | `import java.util.*;` doesn’t import `java.util.concurrent.*` |
| No duplicate imports required     | Compiler handles redundancy internally                        |

---

## 7. **Advantages of Using Inbuilt Packages**

| Benefit             | Description                                     |
| ------------------- | ----------------------------------------------- |
| Reusability         | Use pre-written, tested classes                 |
| Reduces Code Length | Avoid writing low-level implementations         |
| Standardization     | All Java developers use consistent APIs         |
| Saves Time          | Quickly add powerful features (GUI, networking) |

---

## 8. **Conclusion**

* Inbuilt packages provide **essential functionality** across all domains of Java.
* They are accessed using the `import` keyword, except for `java.lang`.
* Using them correctly allows for **faster, safer, and modular development**.

### Introduction to Interfaces in Java

---

#### 1. **Definition**

* An **interface** in Java is a **reference type**, similar to a class, that can **only contain constants, method signatures (abstract methods), default methods, static methods**, and **nested types**.
* Interfaces define a **contract** that classes must follow, **without providing implementation** (except for `default` and `static` methods).

---

#### 2. **Purpose of Interface**

* Achieve **abstraction**
* Support **multiple inheritance** (not possible with classes)
* Provide a way for **unrelated classes** to implement the same functionality

---

## 3. **Declaration Syntax**

```java
interface InterfaceName {
    // abstract method
    void methodName();
}
```

### Example:

```java
interface Animal {
    void eat();
    void sleep();
}
```

---

## 4. **Key Features of Interfaces**

| Feature                                            | Description                                 |
| -------------------------------------------------- | ------------------------------------------- |
| All methods are `public` and `abstract` by default | Except `default` and `static` methods       |
| All variables are `public static final`            | Treated as constants                        |
| Cannot have constructors                           | Cannot be instantiated directly             |
| Multiple interfaces can be implemented by a class  | Achieves multiple inheritance               |
| Can contain default and static methods             | From Java 8 onwards                         |
| Can be extended by other interfaces                | One interface can inherit another interface |

---

## 5. **Implementation of Interface**

* A class implements an interface using the `implements` keyword.

```java
interface Animal {
    void sound();
}

class Dog implements Animal {
    public void sound() {
        System.out.println("Bark");
    }
}
```

---

## 6. **Multiple Interfaces Implementation**

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Bird implements Flyable, Swimmable {
    public void fly() {
        System.out.println("Bird is flying");
    }
    public void swim() {
        System.out.println("Bird can swim too");
    }
}
```

---

## 7. **Interface vs Class**

| Aspect          | Interface                        | Class                       |
| --------------- | -------------------------------- | --------------------------- |
| Inheritance     | Supports multiple inheritance    | Single inheritance only     |
| Methods         | Abstract by default              | Can be concrete or abstract |
| Variables       | `public static final` by default | Can be any access modifier  |
| Constructors    | Not allowed                      | Allowed                     |
| Object Creation | Cannot be instantiated           | Can be instantiated         |

---

## 8. **Extending an Interface**

* One interface can extend another interface using `extends`.

```java
interface A {
    void methodA();
}

interface B extends A {
    void methodB();
}
```

---

## 9. **Default Methods (Java 8+)**

* Interfaces can provide default method implementations.

```java
interface Greeting {
    default void sayHello() {
        System.out.println("Hello!");
    }
}
```

---

## 10. **Static Methods in Interface**

* Can be called using the interface name directly.

```java
interface MathOperations {
    static int square(int x) {
        return x * x;
    }
}
```

Usage:

```java
int result = MathOperations.square(5);
```

---

## 11. **Functional Interfaces (Java 8+)**

* An interface with **only one abstract method**.
* Used with **lambda expressions**.
* Annotated with `@FunctionalInterface`.

```java
@FunctionalInterface
interface Calculator {
    int operation(int a, int b);
}
```

---

## 12. **Interface Inheritance Hierarchy**

```java
interface A {
    void methodA();
}

interface B extends A {
    void methodB();
}

class C implements B {
    public void methodA() { ... }
    public void methodB() { ... }
}
```

---

## 13. **Use Cases of Interfaces**

| Use Case             | Description                                          |
| -------------------- | ---------------------------------------------------- |
| Abstraction          | Hides implementation details                         |
| Multiple Inheritance | One class can implement many interfaces              |
| Loose Coupling       | Changes in implementation don’t affect the interface |
| Callback mechanisms  | Used in event-driven programming                     |
| API Design           | Most Java APIs are built using interfaces            |

---

## 14. **Real-Life Example (API)**

```java
import java.util.List;
List<String> myList = new ArrayList<>();
```

* `List` is an interface.
* `ArrayList` is a class implementing the `List` interface.
* We can switch to `LinkedList` or `Vector` easily by changing the implementation.

---

## 15. **Conclusion**

* Interfaces are a powerful mechanism in Java for **defining contracts** that must be fulfilled by implementing classes.
* They are **central to abstraction**, **polymorphism**, and **API design**, and are heavily used throughout the **Java Standard Library**.

### Features of Interfaces in Java

---

#### 1. **Pure Abstraction**

* Interfaces provide **100% abstraction** (before Java 8).
* They define **only method signatures**, not implementations (except `default` and `static` methods added later).

---

#### 2. **Method Characteristics**

* All methods in interfaces are by default:

  * `public`
  * `abstract` (except `default` and `static` methods)

```java
interface Sample {
    void show();  // implicitly public and abstract
}
```

---

#### 3. **Variable Characteristics**

* All variables in an interface are:

  * `public`
  * `static`
  * `final` (constants)

```java
interface Constants {
    int MAX = 100;  // equivalent to: public static final int MAX = 100;
}
```

---

#### 4. **No Constructors**

* Interfaces **cannot have constructors**.
* They **cannot be instantiated** directly.

---

#### 5. **Supports Multiple Inheritance**

* A class can implement **multiple interfaces**.
* Java avoids the **diamond problem** found in multiple class inheritance.

```java
interface A { void methodA(); }
interface B { void methodB(); }

class C implements A, B {
    public void methodA() { ... }
    public void methodB() { ... }
}
```

---

#### 6. **Interface Inheritance**

* An interface can **extend** another interface using `extends`.
* A single interface can extend **multiple interfaces**.

```java
interface A { void a(); }
interface B extends A { void b(); }
interface C extends A, B { void c(); }
```

---

#### 7. **`implements` Keyword Usage**

* A class uses the `implements` keyword to adopt an interface.

```java
class Demo implements Runnable {
    public void run() {
        System.out.println("Running thread...");
    }
}
```

---

#### 8. **Default Methods (Java 8+)**

* Interface methods can have **default implementation**.
* Useful for **backward compatibility**.

```java
interface Display {
    default void show() {
        System.out.println("Default implementation");
    }
}
```

---

#### 9. **Static Methods (Java 8+)**

* Can be defined inside an interface and called using the **interface name**.

```java
interface MathUtil {
    static int square(int x) {
        return x * x;
    }
}
```

---

#### 10. **Private Methods (Java 9+)**

* **Private methods** can be defined in interfaces to **reuse code** within `default` and `static` methods.

```java
interface Example {
    private void log(String msg) {
        System.out.println(msg);
    }
}
```

---

#### 11. **Functional Interfaces**

* An interface with **only one abstract method** is called a **functional interface**.
* Used with **lambda expressions**.

```java
@FunctionalInterface
interface Calculator {
    int compute(int a, int b);
}
```

---

#### 12. **Loose Coupling**

* Interfaces allow you to write **loosely coupled** code.
* Implementation details can change without affecting the interface contract.

---

#### 13. **Cannot Have Instance Fields**

* Only **constants** are allowed.
* No instance variables like in classes.

---

#### 14. **Used for Callbacks and Event Handling**

* Interfaces are commonly used in **event-driven programming** and **callback mechanisms**.

---

#### 15. **Interfaces in API Design**

* Java APIs heavily rely on interfaces (`List`, `Map`, `Runnable`, `Comparable`).
* Promotes **flexibility**, **interchangeability**, and **testability**.

---

## Summary Table

| Feature                        | Value                                        |
| ------------------------------ | -------------------------------------------- |
| Methods                        | `public abstract` (except default/static)    |
| Variables                      | `public static final` only                   |
| Instantiation                  | Not allowed                                  |
| Multiple Inheritance           | Supported via interfaces                     |
| Constructors                   | Not allowed                                  |
| Default/Static/Private Methods | Supported (Java 8+/9+)                       |
| Interface Inheritance          | One interface can extend others              |
| Implemented by Class           | Using `implements` keyword                   |
| Used in                        | Abstraction, Callbacks, APIs, Event Handling |


### Creation of Interfaces in Java

---

#### 1. **What is an Interface?**

* An **interface** in Java is a **blueprint of a class**.
* It contains:

  * **Abstract methods** (by default)
  * **Constants** (`public static final`)
  * **Default**, **Static**, and **Private methods** (Java 8/9+)

---

## 2. **Syntax to Declare an Interface**

```java
interface InterfaceName {
    // abstract method
    void method1();

    // constant
    int VALUE = 100;

    // default method (Java 8+)
    default void defaultMethod() {
        System.out.println("Default implementation");
    }

    // static method (Java 8+)
    static void staticMethod() {
        System.out.println("Static implementation");
    }

    // private method (Java 9+)
    private void helperMethod() {
        System.out.println("Helper for internal use");
    }
}
```

---

## 3. **Example: Simple Interface**

```java
interface Shape {
    void draw();  // abstract method
}
```

* The `draw()` method is implicitly `public` and `abstract`.

---

## 4. **Implementing an Interface in a Class**

```java
class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing a circle");
    }
}
```

* Class must **override all abstract methods** of the interface.

---

## 5. **Creating Interface with Constants**

```java
interface Constants {
    int MAX = 100;
    int MIN = 1;
}
```

* `MAX` and `MIN` are `public static final` by default.

---

## 6. **Multiple Interfaces**

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Duck implements Flyable, Swimmable {
    public void fly() {
        System.out.println("Duck can fly");
    }
    public void swim() {
        System.out.println("Duck can swim");
    }
}
```

* A class can **implement multiple interfaces**.

---

## 7. **Extending Interfaces**

* One interface can extend another (single or multiple).

```java
interface A {
    void a();
}

interface B extends A {
    void b();
}

interface C extends A, B {
    void c();
}
```

---

## 8. **Using Default Methods (Java 8+)**

```java
interface Printer {
    default void print() {
        System.out.println("Default Print");
    }
}
```

* Can be **inherited or overridden** in implementing classes.

---

## 9. **Using Static Methods in Interfaces (Java 8+)**

```java
interface MathOps {
    static int add(int a, int b) {
        return a + b;
    }
}
```

* Call using interface name: `MathOps.add(5, 3);`

---

## 10. **Functional Interface (Single Abstract Method)**

```java
@FunctionalInterface
interface Operation {
    int operate(int a, int b);
}
```

* Used with **Lambda Expressions**
* `@FunctionalInterface` is optional but helps with validation.

---

## 11. **Private Methods (Java 9+)**

* Used **internally** in default/static methods of interface.

```java
interface Logger {
    private void log(String msg) {
        System.out.println("Log: " + msg);
    }

    default void info(String msg) {
        log(msg);
    }
}
```

---

## 12. **Important Rules**

| Rule                                         | Description                               |
| -------------------------------------------- | ----------------------------------------- |
| Cannot instantiate an interface              | Must be implemented by a class            |
| All methods are `public abstract` by default | Except `default`, `static`, and `private` |
| All variables are `public static final`      | Treated as constants                      |
| Interface supports multiple inheritance      | Class can implement many interfaces       |

---

## 13. **Directory and Compilation (If separate files)**

```java
// File: MyInterface.java
interface MyInterface {
    void show();
}

// File: Test.java
class Test implements MyInterface {
    public void show() {
        System.out.println("Implemented show()");
    }

    public static void main(String[] args) {
        Test t = new Test();
        t.show();
    }
}
```

* Compile and run:

```bash
javac MyInterface.java Test.java
java Test
```

---

## 14. **Conclusion**

* Interface creation involves:

  * Declaring using `interface` keyword
  * Defining abstract methods or default/static methods
  * Implementing them using `implements` in classes
* Supports abstraction, multiple inheritance, and loose coupling.

### Introduction to Multithreading in Java

---

#### 1. **Definition of Multithreading**

* **Multithreading** is a programming concept that allows **multiple threads** to run **concurrently** within a single program (process).
* A **thread** is the **smallest unit of execution**.
* Multithreading helps in achieving **parallelism**, **better CPU utilization**, and **faster execution** for time-consuming tasks.

---

#### 2. **Why Use Multithreading?**

| Reason                        | Description                                          |
| ----------------------------- | ---------------------------------------------------- |
| Improved performance          | Multiple threads can perform tasks in parallel       |
| Better resource utilization   | Utilizes CPU cores efficiently                       |
| Responsiveness                | Keeps UI responsive (especially in GUI applications) |
| Simplifies asynchronous tasks | File I/O, network communication, animations, etc.    |

---

#### 3. **Thread vs Process**

| Feature       | Process                             | Thread                              |
| ------------- | ----------------------------------- | ----------------------------------- |
| Definition    | An independent program in execution | A lightweight sub-unit of a process |
| Memory        | Has its own memory space            | Shares memory with other threads    |
| Communication | Slow and complex                    | Fast and easy                       |
| Overhead      | High                                | Low                                 |

---

#### 4. **Thread in Java**

* Java provides **built-in support** for multithreading through the `java.lang.Thread` class and `java.lang.Runnable` interface.

---

## 5. **Ways to Create Threads in Java**

---

### A. **By Extending `Thread` Class**

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}

public class Test {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();  // starts the thread and calls run()
    }
}
```

---

### B. **By Implementing `Runnable` Interface**

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread is running");
    }
}

public class Test {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable());
        t.start();
    }
}
```

---

### C. **Using Lambda Expression (Java 8+)**

```java
public class Test {
    public static void main(String[] args) {
        Thread t = new Thread(() -> {
            System.out.println("Thread using lambda");
        });
        t.start();
    }
}
```

---

## 6. **Thread Lifecycle**

| State               | Description                                    |
| ------------------- | ---------------------------------------------- |
| **New**             | Thread is created but not started              |
| **Runnable**        | Thread is ready to run and waiting for CPU     |
| **Running**         | Thread is currently executing                  |
| **Blocked/Waiting** | Thread is waiting for a monitor lock or signal |
| **Terminated**      | Thread has finished execution or was aborted   |

---

## 7. **Thread Methods**

| Method             | Description                                |
| ------------------ | ------------------------------------------ |
| `start()`          | Starts the thread and invokes `run()`      |
| `run()`            | Entry point of the thread                  |
| `sleep(ms)`        | Pauses thread for given milliseconds       |
| `join()`           | Waits for a thread to finish execution     |
| `isAlive()`        | Checks if thread is still running          |
| `yield()`          | Gives control to another thread (optional) |
| `setPriority(int)` | Sets thread priority (1 to 10)             |
| `getPriority()`    | Gets current thread priority               |
| `currentThread()`  | Returns currently executing thread         |

---

## 8. **Thread Priority**

* Java threads have priority ranging from **1 (MIN\_PRIORITY)** to **10 (MAX\_PRIORITY)**.
* Default priority is **5 (NORM\_PRIORITY)**.
* Priority helps **suggest** the scheduler which thread to execute first.

---

## 9. **Multithreading in Real Applications**

| Use Case          | Example                                     |
| ----------------- | ------------------------------------------- |
| GUI Applications  | Swing apps with responsive UI               |
| Web Servers       | Handling multiple client requests           |
| Games             | Rendering, physics, sound processing        |
| File Downloading  | Downloading multiple files simultaneously   |
| Chat Applications | Listening and sending messages concurrently |

---

## 10. **Advantages of Multithreading**

| Advantage              | Description                                     |
| ---------------------- | ----------------------------------------------- |
| Efficient CPU usage    | No CPU idling when waiting for I/O              |
| Cost effective         | Threads share resources, saving memory          |
| Scalability            | Easier to write scalable, high-performance apps |
| Asynchronous execution | Time-consuming tasks run in background          |

---

## 11. **Challenges in Multithreading**

| Challenge              | Description                                        |
| ---------------------- | -------------------------------------------------- |
| Thread Synchronization | Managing access to shared resources                |
| Deadlock               | Two threads waiting on each other indefinitely     |
| Race Condition         | Multiple threads modifying shared data incorrectly |
| Complexity             | Debugging and testing multithreaded code is harder |

---

## 12. **Thread Class Hierarchy**

```
java.lang.Object
   ↳ java.lang.Thread
```

`Runnable` is an interface and not part of this inheritance chain.

---

## 13. **Best Practices**

* Use **Runnable** over **Thread** (supports better OOP and reuse)
* Avoid **shared mutable data**
* Use **synchronization** carefully to avoid deadlocks
* Prefer **Executors** for managing large numbers of threads (from `java.util.concurrent`)

---

## 14. **Conclusion**

* Multithreading in Java enables **parallel execution** of tasks to improve **performance**, **efficiency**, and **responsiveness**.
* Java provides multiple ways to create and manage threads through its rich API.
* It plays a vital role in **modern application development**, especially in **networking**, **concurrent processing**, and **interactive applications**.

### Life Cycle of a Thread in Java

---

#### 1. **Definition**

* The **thread life cycle** in Java describes the **various states** that a thread passes through from its **creation** to **termination**.
* These states are defined in the **`Thread.State`** enumeration.

---

### 2. **Thread Life Cycle States**

There are **six primary states** in the thread life cycle:

```
NEW → RUNNABLE → RUNNING → BLOCKED/WAITING/TIMED_WAITING → TERMINATED
```

---

### 3. **Detailed Explanation of Each State**

---

#### 1. **NEW**

* Thread is created but **not yet started**.
* Occurs after creating a Thread object using:

```java
Thread t = new Thread();
```

* The thread is in **NEW** state until `.start()` is called.

---

#### 2. **RUNNABLE**

* The thread is **ready to run** but **not necessarily running**.
* After calling `.start()`, the thread moves from NEW to RUNNABLE.
* The thread is in the **thread scheduler's queue**, waiting for CPU time.

```java
t.start();  // Moves from NEW → RUNNABLE
```

---

#### 3. **RUNNING**

* The thread is **currently executing** its code inside the `run()` method.
* Thread scheduler chooses one of the RUNNABLE threads to move to RUNNING state.
* Java does **not guarantee** the order in which threads are scheduled.

---

#### 4. **BLOCKED**

* The thread is **blocked waiting for a monitor lock**.
* Occurs when:

  * One thread tries to access a **synchronized block or method** that is locked by another thread.

Example:

```java
synchronized(obj) {
    // Only one thread can access this block at a time
}
```

---

#### 5. **WAITING**

* Thread is waiting **indefinitely** for another thread to perform a specific action.
* Entered when:

  * `join()`, `wait()` (without timeout), or similar methods are called.

```java
t.join();   // Current thread waits until thread `t` finishes
obj.wait(); // Current thread waits until notified
```

---

#### 6. **TIMED\_WAITING**

* Thread is waiting for a specified **time interval**.
* Automatically returns to RUNNABLE after the time expires.
* Entered using:

  * `sleep(time)`
  * `wait(time)`
  * `join(time)`
  * `Thread.sleep(time)`
  * `LockSupport.parkNanos(time)` (Advanced)

Example:

```java
Thread.sleep(1000);  // Waits 1 second
```

---

#### 7. **TERMINATED (or DEAD)**

* The thread has **completed execution** or has been **stopped due to an exception**.
* Once a thread reaches this state, it **cannot be restarted**.

---

### 4. **Thread Life Cycle Diagram**

```
NEW
 ↓  .start()
RUNNABLE
 ↔ (Scheduled by CPU)
RUNNING
 ↓  .sleep(), .wait(), .join()
TIMED_WAITING / WAITING / BLOCKED
 ↓ (time complete or notify)
RUNNABLE
 ↓
TERMINATED
```

---

### 5. **Java Code Demonstrating Life Cycle**

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running...");
        try {
            Thread.sleep(2000);  // TIMED_WAITING
        } catch (InterruptedException e) {
            System.out.println("Exception");
        }
    }
}

public class Test {
    public static void main(String[] args) {
        MyThread t = new MyThread();  // NEW
        System.out.println(t.getState()); // NEW
        t.start();  // RUNNABLE
        System.out.println(t.getState()); // RUNNABLE or RUNNING
        try {
            Thread.sleep(100);  // Main thread sleeps
            System.out.println(t.getState()); // TIMED_WAITING
            t.join();  // WAITING
        } catch (InterruptedException e) {}
        System.out.println(t.getState()); // TERMINATED
    }
}
```

---

### 6. **Thread State Enumeration (`Thread.State`)**

```java
Thread.State.NEW
Thread.State.RUNNABLE
Thread.State.BLOCKED
Thread.State.WAITING
Thread.State.TIMED_WAITING
Thread.State.TERMINATED
```

Use `getState()` method to check current state:

```java
Thread.State s = t.getState();
```

---

### 7. **Summary Table**

| State           | Trigger/Cause                          | Next Possible State                                 |
| --------------- | -------------------------------------- | --------------------------------------------------- |
| `NEW`           | Thread object created                  | `RUNNABLE` via `.start()`                           |
| `RUNNABLE`      | Thread ready, waiting for CPU          | `RUNNING`                                           |
| `RUNNING`       | Thread selected by scheduler           | `WAITING`, `TIMED_WAITING`, `BLOCKED`, `TERMINATED` |
| `BLOCKED`       | Waiting to acquire monitor lock        | `RUNNABLE` once lock is acquired                    |
| `WAITING`       | Waits for another thread indefinitely  | `RUNNABLE` after notify/join complete               |
| `TIMED_WAITING` | Waits for limited time                 | `RUNNABLE` after time expires                       |
| `TERMINATED`    | Execution complete or exception thrown | Final state (cannot restart)                        |

---

### 8. **Conclusion**

* Java threads move through **well-defined states** from creation to termination.
* Understanding thread life cycle is essential for **synchronization**, **resource sharing**, and **bug-free multithreading**.

### Creation of a Thread in Java

---

#### 1. **Definition**

* A **thread** is the smallest unit of a process that can execute independently.
* In Java, a thread can be created using:

  * **`Thread` class** (by extending it)
  * **`Runnable` interface** (by implementing it)
  * **`Callable` interface** with **`ExecutorService`** (advanced, supports return value)

---

### 2. **Method 1: By Extending `Thread` Class**

---

#### A. **Syntax**

```java
class MyThread extends Thread {
    public void run() {
        // code to be executed by thread
    }
}

public class Test {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();  // Thread created (NEW state)
        t1.start();                    // Thread started (RUNNABLE state)
    }
}
```

---

#### B. **Explanation**

* `MyThread` is a subclass of `Thread`.
* `run()` method defines the task of the thread.
* `start()` method creates a new thread and invokes `run()`.

---

### 3. **Method 2: By Implementing `Runnable` Interface**

---

#### A. **Syntax**

```java
class MyRunnable implements Runnable {
    public void run() {
        // code to execute in thread
    }
}

public class Test {
    public static void main(String[] args) {
        MyRunnable r = new MyRunnable();        // Create runnable object
        Thread t1 = new Thread(r);              // Wrap in a Thread
        t1.start();                             // Start the thread
    }
}
```

---

#### B. **Explanation**

* More flexible because Java supports only **single inheritance**.
* Recommended approach in most applications.

---

### 4. **Method 3: Using Anonymous Class**

```java
Thread t = new Thread(new Runnable() {
    public void run() {
        System.out.println("Thread using anonymous class");
    }
});
t.start();
```

---

### 5. **Method 4: Using Lambda Expression (Java 8+)**

```java
Thread t = new Thread(() -> {
    System.out.println("Thread using lambda");
});
t.start();
```

* Requires functional interface (`Runnable` has one method: `run()`).

---

### 6. **Example with Multiple Threads**

```java
class Task extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(i + " - " + Thread.currentThread().getName());
        }
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) {
        Task t1 = new Task();
        Task t2 = new Task();

        t1.start();
        t2.start();
    }
}
```

---

### 7. **Important Methods Used**

| Method            | Description                                 |
| ----------------- | ------------------------------------------- |
| `start()`         | Starts a new thread, invokes `run()`        |
| `run()`           | Contains the code to execute in thread      |
| `currentThread()` | Returns the currently running thread object |
| `isAlive()`       | Checks if the thread is still running       |

---

### 8. **Thread Naming**

```java
Thread t1 = new Thread(() -> System.out.println("Running"));
t1.setName("MyThread");
System.out.println(t1.getName());
```

---

### 9. **Checking Thread Status**

```java
Thread t1 = new Thread(() -> {
    System.out.println("Running...");
});

System.out.println(t1.getState()); // NEW
t1.start();
System.out.println(t1.isAlive());  // true or false
```

---

### 10. **Best Practice**

* Prefer using **`Runnable`** or **`ExecutorService`** (not `Thread` subclass) for better scalability and loose coupling.

---

### 11. **Conclusion**

* Threads in Java can be created by:

  * Extending `Thread` class
  * Implementing `Runnable` interface
  * Using anonymous classes or lambda expressions
* `start()` method must be called to **begin execution** of a new thread, which invokes the `run()` method internally.

### Exception Handling in Java

---

### 1. **Definition**

* **Exception Handling** in Java is a mechanism to **handle runtime errors** and maintain the normal flow of the program.
* An **exception** is an event that **disrupts** the normal flow of instructions.

---

### 2. **Hierarchy of Exception Classes**

```
java.lang.Throwable
   ├── java.lang.Error          → Serious issues (JVM errors)
   └── java.lang.Exception      → Recoverable problems
         ├── Checked Exceptions (IOException, SQLException)
         └── Unchecked Exceptions (RuntimeException, ArithmeticException, etc.)
```

---

### 3. **Types of Exceptions**

#### A. **Checked Exceptions**

* Caught or declared in method.
* Occur at **compile time**.
* Examples:

  * `IOException`
  * `SQLException`
  * `ClassNotFoundException`

#### B. **Unchecked Exceptions**

* Not required to handle explicitly.
* Occur at **runtime**.
* Examples:

  * `ArithmeticException`
  * `NullPointerException`
  * `ArrayIndexOutOfBoundsException`

#### C. **Errors**

* Irrecoverable conditions.
* Examples:

  * `StackOverflowError`
  * `OutOfMemoryError`

---

### 4. **Exception Handling Keywords**

| Keyword   | Description                                         |
| --------- | --------------------------------------------------- |
| `try`     | Defines a block of code to be tested for exceptions |
| `catch`   | Defines a block of code to handle the exception     |
| `finally` | Always executed after try-catch; used for cleanup   |
| `throw`   | Used to **explicitly throw** an exception           |
| `throws`  | Declares the exceptions a method can throw          |

---

### 5. **Syntax of Exception Handling**

```java
try {
    // risky code
} catch (ExceptionType e) {
    // handler
} finally {
    // cleanup code (optional)
}
```

---

### 6. **Example: Try-Catch**

```java
public class Example {
    public static void main(String[] args) {
        try {
            int x = 10 / 0; // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Division by zero not allowed.");
        }
    }
}
```

---

### 7. **Multiple Catch Blocks**

```java
try {
    int arr[] = new int[5];
    arr[10] = 20;
} catch (ArithmeticException e) {
    System.out.println("Arithmetic Error");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array Index Error");
} catch (Exception e) {
    System.out.println("General Error");
}
```

---

### 8. **Finally Block**

```java
try {
    int data = 50 / 5;
} catch (Exception e) {
    System.out.println("Handled");
} finally {
    System.out.println("Finally block always executes");
}
```

---

### 9. **Throw Keyword**

```java
public class ThrowExample {
    public static void main(String[] args) {
        throw new ArithmeticException("Manually thrown exception");
    }
}
```

---

### 10. **Throws Keyword**

```java
public class ThrowsExample {
    static void checkAge(int age) throws ArithmeticException {
        if (age < 18)
            throw new ArithmeticException("Not eligible");
        else
            System.out.println("Eligible");
    }

    public static void main(String[] args) {
        checkAge(15);
    }
}
```

---

### 11. **Custom (User-Defined) Exception**

```java
class MyException extends Exception {
    MyException(String msg) {
        super(msg);
    }
}

public class Test {
    public static void main(String[] args) {
        try {
            throw new MyException("Custom exception occurred");
        } catch (MyException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

---

### 12. **Built-in Common Exception Classes**

| Exception                        | Description                            |
| -------------------------------- | -------------------------------------- |
| `ArithmeticException`            | Divide by zero                         |
| `NullPointerException`           | Accessing null object reference        |
| `ArrayIndexOutOfBoundsException` | Accessing invalid array index          |
| `NumberFormatException`          | Converting string to number failed     |
| `ClassNotFoundException`         | Class not found during dynamic loading |
| `IOException`                    | Input/output failure                   |
| `FileNotFoundException`          | File not found                         |

---

### 13. **Best Practices in Exception Handling**

* Catch **specific exceptions** before general ones.
* Never use empty catch blocks.
* Use **finally** for closing resources.
* Avoid **throwing generic Exception**.
* Prefer **custom exceptions** for application-specific errors.

---

### 14. **Difference Between throw and throws**

| `throw`                                | `throws`                               |
| -------------------------------------- | -------------------------------------- |
| Used to **explicitly throw** exception | Used to **declare** exception          |
| Used **inside method** body            | Used **in method signature**           |
| Can throw **only one** exception       | Can declare **multiple** exceptions    |
| Example: `throw new Exception();`      | Example: `void m() throws IOException` |

---

### 15. **Conclusion**

* Exception handling in Java helps ensure **robustness** and **stability**.
* Java offers a complete set of mechanisms to handle, propagate, and recover from errors at runtime.

### Creation of User Defined Exceptions in Java

---

### 1. **What is a User-Defined Exception?**

* A **user-defined exception** (also called custom exception) is a class created by the programmer to handle **application-specific errors**.
* It is created by **extending the `Exception` class** (for checked exceptions) or `RuntimeException` (for unchecked exceptions).

---

### 2. **Steps to Create a User-Defined Exception**

---

#### Step 1: **Create a Class that Extends `Exception` or `RuntimeException`**

```java
class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}
```

---

#### Step 2: **Throw the Exception in Code Using `throw`**

```java
throw new MyException("This is a custom exception");
```

---

#### Step 3: **Handle the Exception Using `try-catch`**

```java
try {
    throw new MyException("Custom error occurred");
} catch (MyException e) {
    System.out.println("Caught custom exception: " + e.getMessage());
}
```

---

### 3. **Example: Custom Exception for Age Validation**

```java
class AgeException extends Exception {
    public AgeException(String message) {
        super(message);
    }
}

public class Test {
    public static void checkAge(int age) throws AgeException {
        if (age < 18) {
            throw new AgeException("Age must be 18 or above");
        } else {
            System.out.println("Valid age");
        }
    }

    public static void main(String[] args) {
        try {
            checkAge(16);
        } catch (AgeException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
```

---

### 4. **Checked vs Unchecked Custom Exceptions**

| Type                | Extend Class       | When Used                             |
| ------------------- | ------------------ | ------------------------------------- |
| Checked Exception   | `Exception`        | Must be declared or handled           |
| Unchecked Exception | `RuntimeException` | Handled optionally, thrown at runtime |

---

#### Example: Unchecked Custom Exception

```java
class InvalidInputException extends RuntimeException {
    public InvalidInputException(String msg) {
        super(msg);
    }
}

public class Test {
    public static void main(String[] args) {
        throw new InvalidInputException("Invalid input provided");
    }
}
```

---

### 5. **Constructor Types in Custom Exceptions**

You can define:

* Constructor with message only:

  ```java
  public MyException(String msg) { super(msg); }
  ```

* Constructor with no arguments:

  ```java
  public MyException() { super("Default error"); }
  ```

* Constructor with cause:

  ```java
  public MyException(Throwable cause) { super(cause); }
  ```

* Constructor with message and cause:

  ```java
  public MyException(String msg, Throwable cause) { super(msg, cause); }
  ```

---

### 6. **Advantages of User-Defined Exceptions**

| Benefit                       | Description                              |
| ----------------------------- | ---------------------------------------- |
| Application-specific handling | Customize errors based on business logic |
| Clean code                    | Better error management structure        |
| Reusability                   | Use across multiple classes/modules      |
| Meaningful error messages     | Easier to debug                          |

---

### 7. **Conclusion**

* User-defined exceptions are created by **extending `Exception` or `RuntimeException`**.
* They allow for **custom error handling**, improving the clarity and maintainability of Java applications.
* Use `throw` to raise and `try-catch` to handle them.

### Understanding the Exception Handling Keywords in Java

---

Java provides five key **keywords** for exception handling:

* `try`
* `catch`
* `throw`
* `throws`
* `finally`

Each plays a unique role in managing **runtime exceptions** and ensuring proper control flow and **resource management**.

---

### 1. **`try` Keyword**

#### → Purpose:

Used to define a **block of code** that may throw an exception.

#### → Syntax:

```java
try {
    // Code that might throw an exception
}
```

#### → Details:

* Must be followed by either **`catch`** or **`finally`** (or both).
* If an exception occurs, control is passed to the corresponding `catch`.

#### → Example:

```java
try {
    int result = 10 / 0;
}
```

---

### 2. **`catch` Keyword**

#### → Purpose:

Used to handle the **exception thrown** inside the `try` block.

#### → Syntax:

```java
catch (ExceptionType e) {
    // Handling code
}
```

#### → Details:

* You can have **multiple catch blocks** for different exception types.
* Order matters: **child exceptions** must be caught **before parent** ones.

#### → Example:

```java
try {
    int[] arr = new int[3];
    arr[5] = 10;
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array index error");
}
```

---

### 3. **`throw` Keyword**

#### → Purpose:

Used to **explicitly throw** an exception (either built-in or user-defined).

#### → Syntax:

```java
throw new ExceptionType("error message");
```

#### → Details:

* Only **one exception** can be thrown at a time.
* After `throw`, **no code executes** in that block.
* Must be an object of `Throwable` class or subclass.

#### → Example:

```java
throw new ArithmeticException("Cannot divide by zero");
```

---

### 4. **`throws` Keyword**

#### → Purpose:

Used in **method signature** to declare the exceptions that the method might throw.

#### → Syntax:

```java
returnType methodName() throws Exception1, Exception2 {
    // method body
}
```

#### → Details:

* Useful for **checked exceptions**.
* It passes the responsibility to the **caller method** to handle the exception.

#### → Example:

```java
void readFile() throws IOException {
    FileReader fr = new FileReader("file.txt");
}
```

---

### 5. **`finally` Keyword**

#### → Purpose:

Used to create a block of code that **always executes**, whether or not an exception occurred.

#### → Syntax:

```java
finally {
    // cleanup code
}
```

#### → Details:

* Used for **resource release**: files, sockets, database connections.
* Executes even if:

  * An exception is not caught
  * A `return` statement is used in try/catch

#### → Example:

```java
try {
    int x = 10 / 2;
} catch (Exception e) {
    System.out.println("Handled");
} finally {
    System.out.println("Finally block executed");
}
```

---

### 6. **All Keywords Together: Full Example**

```java
class MyException extends Exception {
    MyException(String msg) {
        super(msg);
    }
}

public class Demo {
    static void test(int age) throws MyException {
        if (age < 18)
            throw new MyException("Age below 18 not allowed");
        else
            System.out.println("Valid age");
    }

    public static void main(String[] args) {
        try {
            test(16);
        } catch (MyException e) {
            System.out.println("Caught: " + e.getMessage());
        } finally {
            System.out.println("Cleanup done");
        }
    }
}
```

---

### 7. **Summary Table**

| Keyword   | Purpose                                       | Location Used         |
| --------- | --------------------------------------------- | --------------------- |
| `try`     | Encloses risky code                           | Before catch/finally  |
| `catch`   | Handles specific exception                    | After try             |
| `throw`   | Throws an exception explicitly                | Inside a method block |
| `throws`  | Declares exceptions in method signature       | Method declaration    |
| `finally` | Executes code regardless of exception outcome | After try/catch       |

---

### 8. **Important Notes**

* `finally` always runs unless the JVM **terminates** (`System.exit()`).
* `throw` is followed by a **single exception object**.
* You **cannot catch** errors like `OutOfMemoryError` reliably.
* `throws` is mainly for **checked exceptions**.

---

### `try` Keyword in Java

---

### 1. **Definition**

* The `try` keyword is used to define a **block of code** where **exceptions may occur**.
* It allows the programmer to **catch and handle** those exceptions using associated `catch` or `finally` blocks.

---

### 2. **Syntax**

```java
try {
    // Code that might throw an exception
} catch (ExceptionType e) {
    // Code to handle the exception
}
```

OR

```java
try {
    // Code that might throw an exception
} finally {
    // Code that always executes
}
```

OR

```java
try {
    // Code that might throw an exception
} catch (ExceptionType1 e1) {
    // Handle exception type 1
} catch (ExceptionType2 e2) {
    // Handle exception type 2
} finally {
    // Always executes
}
```

---

### 3. **Purpose of `try` Block**

* Encapsulates **code that may generate exceptions** during execution.
* Prevents abnormal program termination.
* Ensures program continues running even after an exception is encountered.

---

### 4. **Rules for `try` Block**

| Rule                                                   | Explanation                               |
| ------------------------------------------------------ | ----------------------------------------- |
| Must be followed by `catch`, `finally`, or both        | Can't use `try` block alone               |
| Cannot have code directly after `try` without handlers | Results in compilation error              |
| Can be **nested** within another `try` block           | Called **nested try blocks**              |
| Can contain multiple **statements**                    | Any statement that might cause exceptions |

---

### 5. **Basic Example**

```java
public class TryExample {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;  // Will throw ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught: Division by zero.");
        }
    }
}
```

---

### 6. **Example with Multiple Statements**

```java
try {
    int a = Integer.parseInt("123");
    int b = 50 / 0;  // Exception occurs here
    System.out.println("This won't execute");
} catch (ArithmeticException e) {
    System.out.println("Division error");
}
```

---

### 7. **Nested `try` Block**

```java
try {
    try {
        int[] arr = new int[5];
        arr[7] = 10;  // Exception
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Inner catch block: " + e);
    }
} catch (Exception e) {
    System.out.println("Outer catch block: " + e);
}
```

---

### 8. **try with only finally**

```java
try {
    int result = 10 / 0;
} finally {
    System.out.println("This will always execute");
}
```

* Even though there is no `catch`, the `finally` block is executed.

---

### 9. **Invalid Usage**

```java
try
    System.out.println("Hello");
// Compilation Error – must have catch or finally
```

---

### 10. **Conclusion**

* The `try` block is essential for **detecting and isolating** exceptions.
* It must be paired with `catch` or `finally`.
* Helps write **robust and crash-resistant** code.

### `catch` Keyword in Java

---

### 1. **Definition**

* The `catch` keyword defines a **block of code** that is executed when a specific **exception** is thrown in the associated `try` block.
* It is used to **handle exceptions** and prevent **abnormal termination** of the program.

---

### 2. **Syntax**

```java
try {
    // code that may throw an exception
} catch (ExceptionType e) {
    // code to handle the exception
}
```

---

### 3. **Purpose**

* To **handle exceptions** of a specific type thrown inside a `try` block.
* Prevents program from crashing by providing **alternate logic** when an error occurs.

---

### 4. **Structure of a `catch` Block**

```java
catch (ExceptionType referenceName) {
    // Exception handling code
}
```

| Part            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `ExceptionType` | The type of exception to catch (e.g., `ArithmeticException`) |
| `referenceName` | A variable that holds the exception object                   |

---

### 5. **Example**

```java
public class CatchExample {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;  // Causes ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught: Division by zero");
        }
    }
}
```

---

### 6. **Multiple Catch Blocks**

* Used to handle **different types** of exceptions separately.

```java
try {
    int[] arr = new int[3];
    arr[5] = 100;  // ArrayIndexOutOfBoundsException
} catch (ArithmeticException e) {
    System.out.println("Arithmetic Exception");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array Index Out Of Bounds");
} catch (Exception e) {
    System.out.println("General Exception");
}
```

* **Important Rule:** Catch more **specific exceptions first**, and more **general exceptions last**.

---

### 7. **Unified Catch Block (Java 7+)**

* You can catch multiple exceptions in **one block** using `|` (pipe):

```java
try {
    // some risky code
} catch (IOException | SQLException e) {
    System.out.println("Handled IOException or SQLException");
}
```

---

### 8. **Accessing Exception Information**

* You can use methods from the exception object like:

```java
catch (Exception e) {
    System.out.println(e.getMessage());   // Returns error message
    e.printStackTrace();                  // Prints full stack trace
}
```

---

### 9. **Nested `catch` Not Allowed**

```java
// NOT allowed:
catch (Exception e) {
    catch (IOException ex) {
        // Invalid
    }
}
```

* Catch blocks **cannot be nested**. You must place them directly after `try`.

---

### 10. **Mandatory Pairing**

* Every `catch` must be **immediately after** a `try` block.
* You **cannot** use `catch` by itself, without a `try`.

---

### 11. **Conclusion**

* `catch` is used to **gracefully handle exceptions** thrown in the `try` block.
* Multiple `catch` blocks allow for **specific handling**.
* Using `catch` ensures the program **continues execution** even when errors occur.

### `throw` Keyword in Java

---

### 1. **Definition**

* The `throw` keyword in Java is used to **explicitly throw an exception** (either built-in or user-defined) **from a method or block** of code.
* Only one exception can be thrown at a time using `throw`.

---

### 2. **Syntax**

```java
throw new ExceptionType("Error message");
```

* `ExceptionType` must be a subclass of `Throwable` (e.g., `Exception`, `RuntimeException`, or custom exception class).
* The `new` keyword is used to create an instance of the exception object.

---

### 3. **Purpose**

* To signal that an **exceptional situation** has occurred.
* Allows **manual creation and propagation** of exceptions based on program logic.

---

### 4. **Basic Example**

```java
public class Example {
    public static void main(String[] args) {
        throw new ArithmeticException("Manually thrown");
    }
}
```

**Output:**

```
Exception in thread "main" java.lang.ArithmeticException: Manually thrown
```

---

### 5. **Throwing User-Defined Exception**

```java
class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

public class Test {
    public static void main(String[] args) {
        try {
            throw new MyException("This is a custom exception");
        } catch (MyException e) {
            System.out.println("Caught: " + e.getMessage());
        }
    }
}
```

---

### 6. **Use with Conditional Statements**

```java
public class Vote {
    static void checkAge(int age) {
        if (age < 18)
            throw new ArithmeticException("Not eligible to vote");
        else
            System.out.println("Eligible to vote");
    }

    public static void main(String[] args) {
        checkAge(16);
    }
}
```

---

### 7. **Difference Between `throw` and `throws`**

| Feature  | `throw`                                    | `throws`                                |
| -------- | ------------------------------------------ | --------------------------------------- |
| Usage    | Used to **actually throw** an exception    | Used to **declare** possible exceptions |
| Location | Inside method or block                     | In method signature                     |
| Quantity | Can throw only **one** exception at a time | Can declare **multiple** exceptions     |
| Syntax   | `throw new ExceptionType();`               | `void method() throws ExceptionType {}` |

---

### 8. **Points to Remember**

* After `throw`, **no code executes** in the same block.
* `throw` is used for **both checked and unchecked exceptions**.
* For checked exceptions, method must either:

  * Catch the exception using `try-catch`
  * OR declare it using `throws`

---

### 9. **Invalid Usage Example**

```java
// This is invalid: throws object that is not Throwable
throw "Some error";  // ❌ Compilation Error
```

---

### 10. **Conclusion**

* The `throw` keyword is used to **manually raise exceptions**.
* It plays a crucial role in **custom error signaling** and **validating logic** in real-time applications.

### `throws` Keyword in Java

---

### 1. **Definition**

* The `throws` keyword is used in a **method declaration** to specify **which checked exceptions** the method might throw.
* It tells the **caller** of the method to handle or declare the exception.

---

### 2. **Syntax**

```java
returnType methodName() throws ExceptionType1, ExceptionType2 {
    // method body
}
```

---

### 3. **Purpose**

* Used to **propagate checked exceptions** to the calling method.
* Avoids handling exceptions inside the method itself if desired.

---

### 4. **Applicable To**

* Only **checked exceptions** must be declared using `throws`.
* **Unchecked exceptions** (like `ArithmeticException`) need not be declared.

---

### 5. **Example: Single Exception**

```java
import java.io.*;

public class Example {
    static void readFile() throws IOException {
        FileReader fr = new FileReader("file.txt");
    }

    public static void main(String[] args) {
        try {
            readFile();
        } catch (IOException e) {
            System.out.println("File not found");
        }
    }
}
```

---

### 6. **Example: Multiple Exceptions**

```java
void process() throws IOException, SQLException {
    // code that may throw either exception
}
```

---

### 7. **Key Rules**

| Rule                                        | Explanation                               |
| ------------------------------------------- | ----------------------------------------- |
| Used only in **method signatures**          | Not inside method body                    |
| Used for **checked exceptions**             | Compiler forces handling                  |
| Can be used with **constructors**           | Like methods, constructors can also throw |
| Exception must be a subclass of `Throwable` | Only throwable types are allowed          |

---

### 8. **Invalid Example**

```java
void method() throws String {
    // ❌ Error: String is not throwable
}
```

---

### 9. **Conclusion**

* `throws` tells the caller **what exceptions may occur** and must be handled or re-declared.
* Useful when a method doesn’t want to handle exceptions **internally**.

---

---

### `finally` Keyword in Java

---

### 1. **Definition**

* The `finally` keyword is used to define a **block of code that always executes** after the `try-catch` block.
* It executes **regardless** of whether an exception was **handled or not**.

---

### 2. **Syntax**

```java
try {
    // code that may throw exception
} catch (Exception e) {
    // handle exception
} finally {
    // code that always executes
}
```

---

### 3. **Purpose**

* Used for **resource cleanup**:

  * Closing files
  * Releasing database connections
  * Freeing memory or sockets

---

### 4. **Example**

```java
public class FinallyExample {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Exception caught");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

---

### 5. **Output**

```
Exception caught  
Finally block executed
```

---

### 6. **When finally is executed**

| Situation                           | Is `finally` executed? |
| ----------------------------------- | ---------------------- |
| Exception thrown and **caught**     | ✅ Yes                  |
| Exception thrown and **not caught** | ✅ Yes                  |
| No exception thrown                 | ✅ Yes                  |
| Method returns from try/catch block | ✅ Yes                  |
| JVM terminated via `System.exit()`  | ❌ No                   |
| Fatal error or crash                | ❌ No                   |

---

### 7. **finally Without catch**

```java
try {
    int x = 5 / 1;
} finally {
    System.out.println("Always executes");
}
```

---

### 8. **Nested try-finally**

```java
try {
    try {
        int x = 5 / 0;
    } finally {
        System.out.println("Inner finally");
    }
} catch (Exception e) {
    System.out.println("Outer catch");
}
```

---

### 9. **Use Case: File Handling**

```java
FileReader fr = null;
try {
    fr = new FileReader("file.txt");
    // read from file
} catch (IOException e) {
    System.out.println("File error");
} finally {
    if (fr != null) {
        try { fr.close(); } catch (IOException e) {}
    }
}
```

---

### 10. **Conclusion**

* `finally` is used for **guaranteed cleanup**, and **executes under all circumstances**, unless the JVM is forcibly terminated.
* Helps ensure that resources are properly released.

### Examples on Exception Handling in Java

---

### **1. Basic Try-Catch Example**

```java
public class Example1 {
    public static void main(String[] args) {
        try {
            int a = 10, b = 0;
            int result = a / b; // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        }
    }
}
```

---

### **2. Multiple Catch Blocks**

```java
public class Example2 {
    public static void main(String[] args) {
        try {
            int[] arr = new int[3];
            arr[5] = 100; // ArrayIndexOutOfBoundsException
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index Out of Bounds Exception");
        } catch (Exception e) {
            System.out.println("General Exception");
        }
    }
}
```

---

### **3. Nested Try-Catch**

```java
public class Example3 {
    public static void main(String[] args) {
        try {
            try {
                int x = 5 / 0; // ArithmeticException
            } catch (ArithmeticException e) {
                System.out.println("Inner Catch: Division by zero");
            }
            int[] arr = new int[2];
            arr[3] = 10; // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Outer Catch: Invalid array index");
        }
    }
}
```

---

### **4. Try-Catch-Finally**

```java
public class Example4 {
    public static void main(String[] args) {
        try {
            int num = 100 / 2;
            System.out.println("Result: " + num);
        } catch (Exception e) {
            System.out.println("Error occurred");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

---

### **5. Throw Keyword Example**

```java
public class Example5 {
    static void validateAge(int age) {
        if (age < 18)
            throw new ArithmeticException("Age less than 18");
        else
            System.out.println("Eligible to vote");
    }

    public static void main(String[] args) {
        try {
            validateAge(16);
        } catch (ArithmeticException e) {
            System.out.println("Caught Exception: " + e.getMessage());
        }
    }
}
```

---

### **6. Throws Keyword Example**

```java
import java.io.*;

public class Example6 {
    static void readFile() throws IOException {
        FileReader fr = new FileReader("test.txt");
        fr.read();
        fr.close();
    }

    public static void main(String[] args) {
        try {
            readFile();
        } catch (IOException e) {
            System.out.println("File operation failed: " + e.getMessage());
        }
    }
}
```

---

### **7. User-Defined Exception**

```java
class InvalidMarkException extends Exception {
    InvalidMarkException(String msg) {
        super(msg);
    }
}

public class Example7 {
    static void checkMark(int mark) throws InvalidMarkException {
        if (mark < 0 || mark > 100)
            throw new InvalidMarkException("Mark should be between 0 and 100");
    }

    public static void main(String[] args) {
        try {
            checkMark(120);
        } catch (InvalidMarkException e) {
            System.out.println("Custom Exception: " + e.getMessage());
        }
    }
}
```

---

### **8. Finally without Catch**

```java
public class Example8 {
    public static void main(String[] args) {
        try {
            System.out.println("Try block running");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

---

### **9. Catching Multiple Exceptions in One Block (Java 7+)**

```java
import java.io.*;

public class Example9 {
    public static void main(String[] args) {
        try {
            String s = null;
            System.out.println(s.length()); // NullPointerException
        } catch (NullPointerException | ArithmeticException e) {
            System.out.println("Caught multiple possible exceptions");
        }
    }
}
```

---

### **10. Exception Propagation Example**

```java
public class Example10 {
    static void method1() {
        int x = 10 / 0;
    }

    static void method2() {
        method1();
    }

    public static void main(String[] args) {
        try {
            method2();
        } catch (ArithmeticException e) {
            System.out.println("Handled in main: " + e);
        }
    }
}
```

---
