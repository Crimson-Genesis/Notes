# Unit - 2 -> Introduction to Polymorphism, Iheritance, String, Handling, Collections
Method Overloading, Inheritance, Methos Overriding.
String Handling, Wrapper Class, Input/Output java Streams.
Collections: Collections Overview, The Collection Interfaces, The Colleaction Classes, Lambda Expressions, Java Memory Management.

## Content ->
### Method Overloading in Java

---

#### 1. **Definition**

* **Method Overloading** means defining **multiple methods with the same name** but with **different parameter lists** (type, number, or order).
* It enables **compile-time polymorphism**, also called **static binding**.

---

#### 2. **Purpose**

* Allows performing **similar operations** with **different inputs**.
* Improves **code readability** and **maintainability**.

---

## 3. **Key Rules of Method Overloading**

| Rule                                             | Explanation                                              |
| ------------------------------------------------ | -------------------------------------------------------- |
| **Same method name**                             | All overloaded methods must have the same name           |
| **Different parameter list**                     | Must differ in number, type, or order of parameters      |
| **Return type may differ but is not sufficient** | Compiler only uses parameter list to distinguish methods |
| **Access modifier can differ**                   | Overloaded methods can have different access levels      |
| **Throws clause can differ**                     | It does not affect overloading                           |

---

## 4. **Types of Overloading**

| Type                       | Description                                     |
| -------------------------- | ----------------------------------------------- |
| **By number of arguments** | Same data types, different number of parameters |
| **By data types**          | Same number, different data types               |
| **By sequence/order**      | Same types and count, but different order       |

---

## 5. **Examples of Method Overloading**

### A. **By Number of Arguments**

```java
class MathUtils {
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

---

### B. **By Data Type**

```java
class Printer {
    void print(int a) {
        System.out.println("Integer: " + a);
    }

    void print(String s) {
        System.out.println("String: " + s);
    }
}
```

---

### C. **By Order of Parameters**

```java
class Display {
    void show(String name, int age) {
        System.out.println(name + " - " + age);
    }

    void show(int age, String name) {
        System.out.println(age + " - " + name);
    }
}
```

---

## 6. **Invalid Overloading (Only by Return Type)**

```java
// This will cause a compile-time error

class Sample {
    int compute() {
        return 5;
    }

    // double compute() { return 5.5; } // ❌ Error: same name & parameters
}
```

---

## 7. **Overloading with Type Promotion**

* If exact match not found, Java uses **type promotion**.

```java
void display(long x) {
    System.out.println("Long: " + x);
}

display(10);  // int promoted to long
```

---

## 8. **Constructor Overloading**

* Constructor can also be overloaded with different parameter lists.

```java
class Student {
    Student() {
        System.out.println("Default");
    }

    Student(String name) {
        System.out.println("Name: " + name);
    }
}
```

---

## 9. **Method Overloading vs Method Overriding**

| Feature            | Method Overloading            | Method Overriding          |
| ------------------ | ----------------------------- | -------------------------- |
| Class relationship | Same class                    | Parent-child (inheritance) |
| Parameters         | Must be different             | Must be same               |
| Return type        | Can be same or different      | Must be same or covariant  |
| Binding            | Compile-time (static binding) | Runtime (dynamic binding)  |
| Polymorphism Type  | Compile-time polymorphism     | Runtime polymorphism       |

---

## 10. **Conclusion**

* **Method Overloading** is a way to **reuse the same method name** with **different input configurations**.
* It enables **flexibility**, **code clarity**, and supports **compile-time polymorphism** in Java.

### Inheritance in Java

---

#### 1. **Definition**

* **Inheritance** is an **object-oriented programming** concept where **one class acquires the properties and behaviors of another class**.
* In Java, it is implemented using the `extends` keyword.
* It enables **code reuse**, **method overriding**, and **polymorphism**.

---

#### 2. **Terminology**

| Term           | Meaning                                     |
| -------------- | ------------------------------------------- |
| **Superclass** | The class whose properties are inherited    |
| **Subclass**   | The class that inherits from the superclass |
| **`extends`**  | Keyword used to inherit a class             |
| **IS-A**       | Relationship model that defines inheritance |

---

#### 3. **Syntax**

```java
class Parent {
    // fields and methods
}

class Child extends Parent {
    // additional fields and methods
}
```

---

#### 4. **Types of Inheritance in Java**

| Type                                  | Description                                         | Supported in Java        |
| ------------------------------------- | --------------------------------------------------- | ------------------------ |
| **Single Inheritance**                | One subclass inherits one superclass                | ✔️ Yes                   |
| **Multilevel Inheritance**            | Class inherits a class which inherits another class | ✔️ Yes                   |
| **Hierarchical Inheritance**          | Multiple subclasses inherit a single superclass     | ✔️ Yes                   |
| **Multiple Inheritance (classes)**    | One class inherits more than one class              | ❌ Not supported          |
| **Multiple Inheritance (interfaces)** | One class implements multiple interfaces            | ✔️ Yes (via `interface`) |

---

### A. **Single Inheritance Example**

```java
class Animal {
    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }
}
```

---

### B. **Multilevel Inheritance Example**

```java
class Animal {
    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }
}

class Puppy extends Dog {
    void weep() {
        System.out.println("Weeping");
    }
}
```

---

### C. **Hierarchical Inheritance Example**

```java
class Animal {
    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("Meowing");
    }
}
```

---

## 5. **Use of `super` Keyword in Inheritance**

* **`super`** is used to:

  * Access superclass variables/methods
  * Invoke superclass constructor

```java
class Animal {
    Animal() {
        System.out.println("Animal Constructor");
    }

    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    Dog() {
        super();  // calls Animal constructor
        System.out.println("Dog Constructor");
    }

    void display() {
        super.eat();  // calls Animal's eat method
    }
}
```

---

## 6. **Method Overriding in Inheritance**

* Subclass provides its **own implementation** of a method defined in superclass.
* Enables **runtime polymorphism**.

```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Bark");
    }
}
```

---

## 7. **Protected Access Modifier**

* Allows superclass members to be accessible in subclass even in **different packages**.

```java
class A {
    protected int data = 100;
}

class B extends A {
    void show() {
        System.out.println(data);  // accessible due to protected
    }
}
```

---

## 8. **Benefits of Inheritance**

| Benefit                  | Explanation                                       |
| ------------------------ | ------------------------------------------------- |
| **Code Reusability**     | Avoid rewriting the same code in multiple classes |
| **Method Overriding**    | Enables custom behavior in subclass               |
| **Runtime Polymorphism** | Achieved through upcasting and method overriding  |
| **Organized Code**       | Logical hierarchy of class relationships          |

---

## 9. **Restrictions in Java Inheritance**

* Java **does not support multiple inheritance** with classes due to ambiguity (diamond problem).
* Java solves this by using **interfaces** for multiple inheritance.

---

## 10. **Inheritance and Object Creation**

```java
class A {
    A() {
        System.out.println("A Constructor");
    }
}

class B extends A {
    B() {
        System.out.println("B Constructor");
    }
}

class Main {
    public static void main(String[] args) {
        B obj = new B();  // both A and B constructors are called
    }
}
```

**Output:**

```
A Constructor  
B Constructor
```

---

## 11. **Conclusion**

* Inheritance is used to **build relationships** between classes.
* It facilitates **code reuse**, **polymorphism**, and **hierarchical organization** of classes.
* Java supports **single, multilevel, and hierarchical inheritance**, while **multiple inheritance** is only supported through **interfaces**.

### Method Overriding in Java

---

#### 1. **Definition**

* **Method Overriding** occurs when a **subclass provides a specific implementation** of a method that is already defined in its **superclass**.
* The **method signature must be identical** (name, return type, parameters).
* It enables **runtime polymorphism** (dynamic method dispatch).

---

## 2. **Purpose**

* To provide **specific behavior** of a method in a subclass.
* Allows one to **customize functionality** inherited from a superclass.

---

## 3. **Requirements for Overriding**

| Rule                                          | Description                                                       |
| --------------------------------------------- | ----------------------------------------------------------------- |
| Same method name                              | Must match exactly                                                |
| Same return type                              | Must be the same or a **covariant** type                          |
| Same parameter list                           | Must match exactly                                                |
| Inheritance                                   | Must be between parent and child class                            |
| Access modifier                               | Subclass method must be **same or more accessible**               |
| Not `final`, `static`, or `private`           | These cannot be overridden                                        |
| Use of `@Override` (optional but recommended) | Indicates to compiler that method is intended to override another |

---

## 4. **Basic Example**

```java
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
```

---

## 5. **Invocation of Overridden Methods**

```java
class Main {
    public static void main(String[] args) {
        Animal obj = new Dog();  // Upcasting
        obj.sound();             // Calls Dog's sound() at runtime
    }
}
```

**Output:**

```
Dog barks
```

---

## 6. **Use of `super` in Overriding**

* Used to call the **superclass version** of the overridden method.

```java
class Dog extends Animal {
    @Override
    void sound() {
        super.sound();         // Calls Animal's sound()
        System.out.println("Dog barks");
    }
}
```

---

## 7. **Covariant Return Type**

* Java allows **returning a subclass** type when overriding.

```java
class Animal {
    Animal getAnimal() {
        return this;
    }
}

class Dog extends Animal {
    @Override
    Dog getAnimal() {
        return this;
    }
}
```

---

## 8. **Access Modifiers and Overriding**

| Superclass Modifier       | Allowed in Subclass Overriding               |
| ------------------------- | -------------------------------------------- |
| `public`                  | `public`                                     |
| `protected`               | `protected` or `public`                      |
| default (package-private) | default, protected, or public (same package) |
| `private`                 | ❌ Cannot be overridden                       |

---

## 9. **Final, Static, and Private Methods**

| Method Type | Overridable?                | Reason                           |
| ----------- | --------------------------- | -------------------------------- |
| `final`     | ❌ No                        | Cannot be modified in subclass   |
| `static`    | ❌ No (hides, not overrides) | Belongs to class, not object     |
| `private`   | ❌ No                        | Not accessible outside its class |

---

## 10. **Polymorphism through Overriding**

* Enables **runtime polymorphism** by using a **superclass reference** to a **subclass object**.

```java
Animal a = new Dog();
a.sound();  // Dog's version is called
```

---

## 11. **Difference Between Overriding and Overloading**

| Feature              | Method Overriding         | Method Overloading        |
| -------------------- | ------------------------- | ------------------------- |
| Inheritance required | Yes                       | No                        |
| Parameters           | Must be same              | Must be different         |
| Return type          | Must be same or covariant | Can be different          |
| Polymorphism type    | Runtime polymorphism      | Compile-time polymorphism |
| Binding              | Dynamic binding           | Static binding            |

---

## 12. **Example: Runtime Polymorphism**

```java
class Shape {
    void draw() {
        System.out.println("Drawing shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing circle");
    }
}

class Main {
    public static void main(String[] args) {
        Shape s = new Circle();
        s.draw();  // Output: Drawing circle
    }
}
```

---

## 13. **Conclusion**

* **Method Overriding** allows **subclasses to define their own behavior** for methods defined in a **superclass**.
* It supports **runtime polymorphism**, enabling Java to select the appropriate method **dynamically at execution time**.

### String Handling in Java

---

#### 1. **Definition**

* A **String** in Java is a **sequence of characters**.
* Strings are **objects** of the `String` class in `java.lang` package.
* They are **immutable**: once created, their content **cannot be changed**.

---

## 2. **Ways to Create a String**

### A. **Using String Literals**

```java
String s1 = "Hello";
```

* Stored in **String Constant Pool**
* If another string with the same content is created, **no new object** is created.

### B. **Using `new` Keyword**

```java
String s2 = new String("Hello");
```

* Creates a **new object** in the heap memory, even if the same content exists.

---

## 3. **String Immutability**

* Once a `String` is created, **it cannot be modified**.
* Any modification results in the creation of a **new object**.

```java
String s = "Java";
s.concat(" Language");  // "Java Language" is a new object
System.out.println(s);  // Output: Java
```

---

## 4. **Common String Methods**

| Method                          | Description                                  |
| ------------------------------- | -------------------------------------------- |
| `length()`                      | Returns the length of the string             |
| `charAt(int index)`             | Returns character at given index             |
| `substring(int begin, int end)` | Returns substring from begin to end-1        |
| `contains(CharSequence s)`      | Checks if string contains specified sequence |
| `equals(Object obj)`            | Compares content (case-sensitive)            |
| `equalsIgnoreCase(String)`      | Compares content (ignores case)              |
| `compareTo(String another)`     | Lexicographically compares two strings       |
| `toLowerCase()`                 | Converts string to lowercase                 |
| `toUpperCase()`                 | Converts string to uppercase                 |
| `trim()`                        | Removes leading and trailing spaces          |
| `replace(char old, char new)`   | Replaces all occurrences of a character      |
| `split(String regex)`           | Splits string using regular expression       |

---

## 5. **String Comparison Methods**

| Comparison Type        | Method               | Description                             |
| ---------------------- | -------------------- | --------------------------------------- |
| Content-based          | `equals()`           | True if contents are the same           |
| Reference-based        | `==`                 | True if references point to same object |
| Ignore case comparison | `equalsIgnoreCase()` | True if contents match ignoring case    |
| Lexicographic compare  | `compareTo()`        | Returns int (0 if equal, <0 or >0)      |

---

## 6. **String Concatenation**

### A. **Using `+` Operator**

```java
String s1 = "Hello";
String s2 = "World";
String s3 = s1 + " " + s2;  // Hello World
```

### B. **Using `concat()` Method**

```java
String s = "Java".concat(" Language");  // Java Language
```

---

## 7. **StringBuffer vs StringBuilder vs String**

| Feature     | `String`       | `StringBuffer`       | `StringBuilder`        |
| ----------- | -------------- | -------------------- | ---------------------- |
| Mutability  | Immutable      | Mutable              | Mutable                |
| Thread-safe | No             | Yes (synchronized)   | No (not synchronized)  |
| Performance | Slow           | Slower (thread-safe) | Faster (single thread) |
| Use-case    | Read-only data | Multi-threaded env   | Single-threaded env    |

---

## 8. **StringBuffer Example**

```java
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");
System.out.println(sb);  // Hello World
```

---

## 9. **StringBuilder Example**

```java
StringBuilder sb = new StringBuilder("Data");
sb.append("Base");
System.out.println(sb);  // DataBase
```

---

## 10. **String Formatting**

```java
String name = "Alice";
int age = 25;
String result = String.format("Name: %s, Age: %d", name, age);
```

**Output:**

```
Name: Alice, Age: 25
```

---

## 11. **String Interning**

* The `intern()` method puts the string in the **string pool**.
* Ensures that **identical strings share the same memory reference**.

```java
String s1 = new String("Java");
String s2 = s1.intern();  // adds to string pool
```

---

## 12. **Converting Between String and Other Types**

| Conversion       | Example                   |
| ---------------- | ------------------------- |
| String → int     | `Integer.parseInt("123")` |
| int → String     | `String.valueOf(123)`     |
| char\[] → String | `new String(charArray)`   |
| String → char\[] | `"hello".toCharArray()`   |

---

## 13. **Looping through Characters**

```java
String s = "Hello";
for (int i = 0; i < s.length(); i++) {
    System.out.println(s.charAt(i));
}
```

---

## 14. **Regular Expressions with String**

```java
String data = "Java123";
boolean b = data.matches("[A-Za-z0-9]+");  // true
```

---

## 15. **Conclusion**

* Java provides powerful **string handling** using the **`String` class and its methods**.
* For **mutable strings**, `StringBuilder` and `StringBuffer` are used.
* Proper handling of strings is essential for **text processing**, **data formatting**, and **I/O operations**.

### Wrapper Classes in Java

---

#### 1. **Definition**

* **Wrapper classes** in Java provide a way to **use primitive data types as objects**.
* Each primitive type (like `int`, `float`, etc.) has a corresponding **wrapper class** in the `java.lang` package.

---

## 2. **Primitive Types and Their Wrapper Classes**

| Primitive Type | Wrapper Class |
| -------------- | ------------- |
| `byte`         | `Byte`        |
| `short`        | `Short`       |
| `int`          | `Integer`     |
| `long`         | `Long`        |
| `float`        | `Float`       |
| `double`       | `Double`      |
| `char`         | `Character`   |
| `boolean`      | `Boolean`     |

---

## 3. **Purpose of Wrapper Classes**

| Use Case                      | Description                                                |
| ----------------------------- | ---------------------------------------------------------- |
| **Collections**               | Collections like `ArrayList` cannot store primitives       |
| **Object Conversion**         | Convert primitives to objects and vice versa               |
| **Utility Methods**           | Wrapper classes have useful static methods (e.g., parsing) |
| **Type Conversion**           | Convert strings to numbers, vice versa                     |
| **Default values in classes** | Use objects in generics or as null-initialized members     |

---

## 4. **Creating Wrapper Objects**

### A. **Using Constructor (Deprecated in newer Java)**

```java
Integer i = new Integer(10);     // discouraged
Double d = new Double(3.14);
```

### B. **Using `valueOf()` (Preferred Method)**

```java
Integer i = Integer.valueOf(10);
Double d = Double.valueOf("3.14");
```

---

## 5. **Auto-boxing and Unboxing (Since Java 5)**

| Term           | Meaning                                                    |
| -------------- | ---------------------------------------------------------- |
| **Autoboxing** | Automatic conversion from primitive to wrapper object      |
| **Unboxing**   | Automatic conversion from wrapper object to primitive type |

### A. **Example of Autoboxing**

```java
int a = 5;
Integer obj = a;  // autoboxing
```

### B. **Example of Unboxing**

```java
Integer obj = 10;
int a = obj;  // unboxing
```

---

## 6. **Important Methods in Wrapper Classes**

| Class       | Method                             | Description                  |
| ----------- | ---------------------------------- | ---------------------------- |
| `Integer`   | `parseInt(String)`                 | Converts String to `int`     |
| `Integer`   | `toString()`                       | Converts Integer to String   |
| `Double`    | `parseDouble(String)`              | Converts String to `double`  |
| `Boolean`   | `parseBoolean(String)`             | Converts String to `boolean` |
| `Character` | `isDigit(char)` / `isLetter(char)` | Character property checks    |

---

## 7. **Example: Using Wrapper in Collections**

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);      // autoboxing
        list.add(20);
        int x = list.get(0); // unboxing
        System.out.println(x);
    }
}
```

---

## 8. **Comparison Between Primitives and Wrappers**

| Feature            | Primitive Type (`int`) | Wrapper Class (`Integer`) |
| ------------------ | ---------------------- | ------------------------- |
| Memory efficient   | Yes                    | Slightly more memory used |
| Can be null        | No                     | Yes                       |
| Use in Collections | No                     | Yes                       |
| Object methods     | No                     | Yes (e.g., `toString()`)  |

---

## 9. **Parsing Strings to Primitive Types**

```java
int num = Integer.parseInt("123");       // String to int
double d = Double.parseDouble("3.14");   // String to double
```

---

## 10. **Default Values**

| Data Type | Default (primitive) | Default (wrapper) |
| --------- | ------------------- | ----------------- |
| `int`     | `0`                 | `null`            |
| `boolean` | `false`             | `null`            |

---

## 11. **Boxing and Unboxing in Arithmetic**

```java
Integer a = 10;
Integer b = 20;
int sum = a + b;  // auto-unboxing occurs
```

---

## 12. **Conclusion**

* Wrapper classes are essential when **working with objects**, especially in **collections** and **generic types**.
* They provide useful **conversion and utility methods**, and enable **auto-boxing** to simplify coding.

### Input/Output (I/O) Streams in Java

---

#### 1. **Definition**

* **I/O Streams** in Java are used to **read data from sources** (like files, keyboard, etc.) and **write data to destinations** (like files, console, etc.).
* Streams are **sequences of data**: a **stream represents a flow of data** (input or output).

---

## 2. **Types of Streams**

| Type              | Description                             |
| ----------------- | --------------------------------------- |
| **Input Stream**  | Used to read data **from** a source     |
| **Output Stream** | Used to write data **to** a destination |

---

## 3. **Java I/O Stream Classification**

### A. **Based on Data Type**

| Category      | Classes for Byte Data             | Classes for Character Data  |
| ------------- | --------------------------------- | --------------------------- |
| Input Stream  | `InputStream` and its subclasses  | `Reader` and its subclasses |
| Output Stream | `OutputStream` and its subclasses | `Writer` and its subclasses |

---

## 4. **Byte Streams**

* Handles **raw binary data** (images, audio, etc.)
* **Base classes**:

  * `InputStream`
  * `OutputStream`

### Common Byte Stream Classes

| Purpose        | Input Classes          | Output Classes          |
| -------------- | ---------------------- | ----------------------- |
| File Access    | `FileInputStream`      | `FileOutputStream`      |
| Array Handling | `ByteArrayInputStream` | `ByteArrayOutputStream` |
| Buffering      | `BufferedInputStream`  | `BufferedOutputStream`  |
| Filter Streams | `DataInputStream`      | `DataOutputStream`      |

---

## 5. **Character Streams**

* Handles **textual data** (characters and strings)
* **Base classes**:

  * `Reader`
  * `Writer`

### Common Character Stream Classes

| Purpose        | Reader Classes    | Writer Classes    |
| -------------- | ----------------- | ----------------- |
| File Access    | `FileReader`      | `FileWriter`      |
| Buffering      | `BufferedReader`  | `BufferedWriter`  |
| Array Handling | `CharArrayReader` | `CharArrayWriter` |
| Formatting     | —                 | `PrintWriter`     |

---

## 6. **Basic Byte Stream Example**

### Reading from a File:

```java
import java.io.*;

class ReadFile {
    public static void main(String[] args) throws IOException {
        FileInputStream fin = new FileInputStream("data.txt");
        int i;
        while ((i = fin.read()) != -1) {
            System.out.print((char) i);
        }
        fin.close();
    }
}
```

### Writing to a File:

```java
FileOutputStream fout = new FileOutputStream("data.txt");
String s = "Hello Java Stream";
byte[] b = s.getBytes();
fout.write(b);
fout.close();
```

---

## 7. **Basic Character Stream Example**

### Reading Using `BufferedReader`:

```java
BufferedReader br = new BufferedReader(new FileReader("data.txt"));
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
br.close();
```

### Writing Using `BufferedWriter`:

```java
BufferedWriter bw = new BufferedWriter(new FileWriter("data.txt"));
bw.write("Welcome to Java I/O");
bw.newLine();
bw.write("Second line");
bw.close();
```

---

## 8. **System I/O Streams**

| Stream       | Class         | Purpose                   |
| ------------ | ------------- | ------------------------- |
| `System.in`  | `InputStream` | Read input from keyboard  |
| `System.out` | `PrintStream` | Display output to console |
| `System.err` | `PrintStream` | Display error messages    |

```java
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
System.out.print("Enter name: ");
String name = reader.readLine();
System.out.println("Hello, " + name);
```

---

## 9. **DataInputStream and DataOutputStream**

* Used to read/write **primitive data types** as binary data.

```java
DataOutputStream dos = new DataOutputStream(new FileOutputStream("info.dat"));
dos.writeInt(100);
dos.writeUTF("Java");
dos.close();

DataInputStream dis = new DataInputStream(new FileInputStream("info.dat"));
int x = dis.readInt();
String s = dis.readUTF();
dis.close();
```

---

## 10. **ObjectInputStream and ObjectOutputStream**

* Used to read/write **objects** (serialization).

```java
ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("obj.dat"));
out.writeObject(new Student("Amit", 101));
out.close();

ObjectInputStream in = new ObjectInputStream(new FileInputStream("obj.dat"));
Student s = (Student) in.readObject();
in.close();
```

---

## 11. **Closing Streams**

* Always **close streams** using `.close()` method to release resources.
* Recommended to use **`try-with-resources`** in Java 7+:

```java
try (FileReader fr = new FileReader("data.txt")) {
    // reading code
}
```

---

## 12. **Exception Handling in I/O**

* Common exceptions:

  * `IOException`
  * `FileNotFoundException`
  * `EOFException`

Use `try-catch` to handle:

```java
try {
    FileReader fr = new FileReader("abc.txt");
} catch (FileNotFoundException e) {
    System.out.println("File not found.");
}
```

---

## 13. **Conclusion**

* Java I/O streams enable **efficient reading and writing** of data from/to various sources.
* **Byte streams** handle raw data; **character streams** handle text.
* Supports **buffering**, **serialization**, **filtering**, and **data-type-specific** operations via specialized classes.

### Collections in Java: Overview

---

#### 1. **Definition**

* **Collections** in Java are **frameworks** that provide **architecture** to store, retrieve, and manipulate **groups of objects**.
* Located in the package: `java.util`.
* The **Java Collections Framework (JCF)** provides **interfaces**, **implementations (classes)**, and **algorithms** for working with data structures.

---

## 2. **Need for Collections**

| Problem with Arrays          | How Collections Solve It                            |
| ---------------------------- | --------------------------------------------------- |
| Fixed size                   | Collections are **dynamic** in size                 |
| Not type-safe (no generics)  | Collections use **generics**                        |
| No built-in algorithms       | Collections provide built-in **sorting, searching** |
| Manual resizing & complexity | Collection classes handle resizing and operations   |

---

## 3. **Hierarchy of Java Collection Framework**

```
            Iterable
                |
            Collection
        --------------------
        |        |         |
      List     Set      Queue
        |        |         |
   ArrayList   HashSet   PriorityQueue
   LinkedList  LinkedHashSet  Deque
   Vector      TreeSet     ArrayDeque
```

### A. **Root Interface: `Iterable`**

* Interface with `forEach()` and `iterator()` methods.
* Superinterface of `Collection`.

---

## 4. **Major Interfaces in Collections**

| Interface    | Description                                               |
| ------------ | --------------------------------------------------------- |
| `Collection` | Root of the collection hierarchy                          |
| `List`       | Ordered, index-based, allows duplicates                   |
| `Set`        | Unordered, no duplicates                                  |
| `Queue`      | Ordered for processing (FIFO), supports insertion/removal |
| `Deque`      | Double-ended queue (insertion/removal at both ends)       |
| `Map`        | Stores key-value pairs (**not part of Collection**)       |

---

## 5. **Key Classes Implementing Interfaces**

| Interface | Classes Implementing It                            |
| --------- | -------------------------------------------------- |
| `List`    | `ArrayList`, `LinkedList`, `Vector`, `Stack`       |
| `Set`     | `HashSet`, `LinkedHashSet`, `TreeSet`              |
| `Queue`   | `PriorityQueue`, `ArrayDeque`                      |
| `Map`     | `HashMap`, `TreeMap`, `LinkedHashMap`, `Hashtable` |

---

## 6. **Generic Syntax**

```java
List<String> list = new ArrayList<String>();
```

* Allows **type safety**, avoids `ClassCastException`.

---

## 7. **Collection vs Collections**

| Term          | Meaning                                  |
| ------------- | ---------------------------------------- |
| `Collection`  | **Interface** (base of collection types) |
| `Collections` | **Utility class** with static methods    |

```java
Collections.sort(list);
Collections.reverse(list);
```

---

## 8. **Common Operations Provided**

| Operation        | Method Name               |
| ---------------- | ------------------------- |
| Add element      | `add(E e)`                |
| Remove element   | `remove(Object o)`        |
| Search element   | `contains(Object o)`      |
| Size             | `size()`                  |
| Clear collection | `clear()`                 |
| Check empty      | `isEmpty()`               |
| Iterate          | `iterator()`, `forEach()` |

---

## 9. **Iterating Collections**

### A. **Using for-each loop**

```java
for (String s : list) {
    System.out.println(s);
}
```

### B. **Using Iterator**

```java
Iterator<String> itr = list.iterator();
while (itr.hasNext()) {
    System.out.println(itr.next());
}
```

---

## 10. **Advantages of Java Collections Framework**

| Advantage                | Description                              |
| ------------------------ | ---------------------------------------- |
| **Reusable**             | Predefined data structures               |
| **Type Safe (Generics)** | Compile-time checks                      |
| **Standardization**      | Common interfaces & behaviors            |
| **Performance**          | Optimized implementations                |
| **Extensibility**        | Custom implementations possible          |
| **Interoperability**     | Easily works with arrays, legacy systems |

---

## 11. **Conclusion**

* The **Java Collections Framework** provides a **unified architecture** for manipulating and storing groups of objects.
* It includes **interfaces**, **classes**, and **algorithms** that offer **flexibility, scalability**, and **ease of use** for data management.

### The Collection Interfaces in Java

---

#### 1. **Overview**

* **Collection Interfaces** are a part of the **Java Collections Framework (JCF)**.
* They define the **standard operations** (add, remove, search, iterate, etc.) that all collection types must support.
* Located in `java.util` package.
* Provide the **blueprint** for various collection classes like `ArrayList`, `HashSet`, `TreeSet`, etc.

---

## 2. **Hierarchy Diagram**

```
java.lang.Iterable
      |
  java.util.Collection
      |------------------|
   List      Set       Queue
                       |
                    Deque

java.util.Map (separate hierarchy)
```

---

## 3. **Core Collection Interfaces**

| Interface    | Type               | Description                                                     |
| ------------ | ------------------ | --------------------------------------------------------------- |
| `Collection` | Root Interface     | Base of all collection types (except `Map`)                     |
| `List`       | Linear List        | Ordered, allows duplicates, indexed                             |
| `Set`        | Unordered Set      | No duplicates, unordered                                        |
| `Queue`      | FIFO Queue         | Ordered for processing, supports insertion/removal              |
| `Deque`      | Double-Ended Queue | Allows insertion/removal from both ends                         |
| `Map`        | Key-Value Pair     | Stores pairs, no duplicate keys (not a subtype of `Collection`) |

---

## 4. **`Collection<E>` Interface**

* **Root interface** of the collection hierarchy.
* Contains general-purpose methods common to all collections.

### Common Methods:

```java
boolean add(E e)
boolean remove(Object o)
boolean contains(Object o)
int size()
boolean isEmpty()
void clear()
Iterator<E> iterator()
```

---

## 5. **`List<E>` Interface**

* An **ordered** collection (also called **sequence**).
* Elements can be **accessed by index**.
* Allows **duplicate elements**.

### Implementing Classes:

* `ArrayList`
* `LinkedList`
* `Vector`
* `Stack`

### Key Methods:

```java
void add(int index, E element)
E get(int index)
E remove(int index)
int indexOf(Object o)
ListIterator<E> listIterator()
```

---

## 6. **`Set<E>` Interface**

* A collection that **does not allow duplicate elements**.
* **Unordered** (except for `LinkedHashSet`).

### Implementing Classes:

* `HashSet`
* `LinkedHashSet`
* `TreeSet` (SortedSet)

### Key Characteristics:

| Implementation  | Order Maintained?       | Sorted? |
| --------------- | ----------------------- | ------- |
| `HashSet`       | ❌ No                    | ❌ No    |
| `LinkedHashSet` | ✅ Yes (insertion order) | ❌ No    |
| `TreeSet`       | ✅ Yes (sorted order)    | ✅ Yes   |

---

## 7. **`SortedSet<E>` and `NavigableSet<E>`**

* **Subinterfaces of `Set`** for **sorted elements**.
* Implemented by `TreeSet`.

### Methods:

```java
E first()
E last()
SortedSet<E> subSet(E from, E to)
NavigableSet<E> descendingSet()
```

---

## 8. **`Queue<E>` Interface**

* Used to hold elements before **processing**.
* Typically used in **FIFO** (First-In-First-Out) order.
* Some queues (like `PriorityQueue`) use **priority-based** ordering.

### Implementing Classes:

* `LinkedList`
* `PriorityQueue`
* `ArrayDeque`

### Key Methods:

```java
boolean offer(E e)
E poll()       // removes head
E peek()       // views head
```

---

## 9. **`Deque<E>` Interface** (Double-Ended Queue)

* Extends `Queue`
* Allows insertion/removal from **both ends**

### Implementing Class:

* `ArrayDeque`

### Key Methods:

```java
void addFirst(E e)
void addLast(E e)
E removeFirst()
E removeLast()
```

---

## 10. **`Map<K, V>` Interface** (Separate Hierarchy)

* Stores **key-value pairs**
* Keys must be **unique**, values can be **duplicate**

### Implementing Classes:

* `HashMap`
* `TreeMap`
* `LinkedHashMap`
* `Hashtable`

### Key Methods:

```java
V put(K key, V value)
V get(Object key)
boolean containsKey(Object key)
Set<K> keySet()
Collection<V> values()
Set<Map.Entry<K,V>> entrySet()
```

---

## 11. **Important Subinterfaces and Views**

| Interface           | Description                       |
| ------------------- | --------------------------------- |
| `Iterable<E>`       | Root for iteration (`for-each`)   |
| `SortedSet<E>`      | Set with sorted elements          |
| `NavigableSet<E>`   | SortedSet with navigation methods |
| `SortedMap<K,V>`    | Map with keys sorted              |
| `NavigableMap<K,V>` | SortedMap with navigation methods |

---

## 12. **Generics with Collections**

* Enforces **type safety** at compile time.
* Example:

```java
List<String> names = new ArrayList<>();
names.add("Alice");
```

---

## 13. **Comparison of Interfaces**

| Interface | Allows Duplicates | Ordered | Indexed   | Sorted         | Use Case                    |
| --------- | ----------------- | ------- | --------- | -------------- | --------------------------- |
| `List`    | Yes               | Yes     | Yes       | No             | Linear data                 |
| `Set`     | No                | No      | No        | Only `TreeSet` | Unique data                 |
| `Queue`   | Yes               | Yes     | No        | Depends        | Task processing             |
| `Deque`   | Yes               | Yes     | No        | No             | Double-end processing queue |
| `Map`     | No (keys)         | No      | Key-based | Only `TreeMap` | Key-value pairs             |

---

## 14. **Conclusion**

* **Collection interfaces** define the **structure and behavior** of all data collections in Java.
* Each interface has multiple **implementations** with different performance characteristics.
* Proper selection of the interface and implementation ensures **efficient and optimized data handling**.

### The Collection Classes in Java

---

#### 1. **Definition**

* **Collection classes** are **concrete implementations** of collection interfaces (like `List`, `Set`, `Queue`) provided by the **Java Collections Framework (JCF)** in the `java.util` package.
* These classes offer ready-to-use **data structures** such as **dynamic arrays**, **hash tables**, **linked lists**, **stacks**, **queues**, and **sets**.

---

## 2. **List Implementation Classes**

### A. `ArrayList`

* **Resizable array implementation**
* Maintains **insertion order**
* Allows **duplicates**
* Allows **null** values

```java
List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
```

### Key Features:

| Feature            | Value                         |
| ------------------ | ----------------------------- |
| Ordered            | Yes                           |
| Indexed            | Yes                           |
| Duplicate elements | Allowed                       |
| Performance        | Fast for random access (O(1)) |

---

### B. `LinkedList`

* **Doubly-linked list** implementation
* Implements both `List` and `Deque`
* Efficient for **insertion/deletion** operations

```java
List<String> list = new LinkedList<>();
list.add("X");
list.add("Y");
```

### Key Features:

| Feature           | Value              |
| ----------------- | ------------------ |
| Ordered           | Yes                |
| Fast insertion    | Yes (O(1) at ends) |
| Random access     | Slow (O(n))        |
| Implements Queue? | Yes (`Deque`)      |

---

### C. `Vector` (Legacy)

* **Thread-safe** dynamic array
* Synchronized methods (slower)
* Rarely used in new code; replaced by `ArrayList`

```java
Vector<Integer> v = new Vector<>();
v.add(100);
```

---

### D. `Stack` (Legacy)

* Subclass of `Vector`
* Implements **LIFO (Last In First Out)**

```java
Stack<String> stack = new Stack<>();
stack.push("A");
stack.pop();
```

---

## 3. **Set Implementation Classes**

### A. `HashSet`

* **Hash table** based implementation of `Set`
* **Unordered**
* Does **not allow duplicates**
* Allows **one null** element

```java
Set<String> set = new HashSet<>();
set.add("Apple");
set.add("Banana");
```

---

### B. `LinkedHashSet`

* Maintains **insertion order**
* Internally uses **LinkedList + HashTable**
* No duplicates allowed

```java
Set<Integer> set = new LinkedHashSet<>();
set.add(10);
set.add(20);
```

---

### C. `TreeSet`

* **Sorted set** using **Red-Black Tree**
* Maintains elements in **ascending order**
* Does **not allow null**
* Implements `NavigableSet`

```java
Set<String> set = new TreeSet<>();
set.add("C");
set.add("A");
set.add("B");
```

**Output Order**: A, B, C

---

## 4. **Queue and Deque Classes**

### A. `PriorityQueue`

* Implements **Queue**
* Elements are **ordered by priority**
* Uses **min-heap** by default

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(30);
pq.add(10);
pq.add(20);
```

---

### B. `ArrayDeque`

* Implements **Deque** (double-ended queue)
* Faster than `Stack` and `LinkedList`
* Does **not allow nulls**

```java
ArrayDeque<String> dq = new ArrayDeque<>();
dq.addFirst("X");
dq.addLast("Y");
```

---

## 5. **Map Implementation Classes** (Not part of Collection interface)

### A. `HashMap`

* **Key-value** pair storage
* **Unordered**
* Allows **one null key** and **multiple null values**
* Not synchronized

```java
Map<Integer, String> map = new HashMap<>();
map.put(1, "Java");
map.put(2, "Python");
```

---

### B. `LinkedHashMap`

* Maintains **insertion order**
* Good for predictable iteration
* Allows one null key

```java
Map<Integer, String> map = new LinkedHashMap<>();
map.put(1, "One");
map.put(2, "Two");
```

---

### C. `TreeMap`

* Keys are **sorted in natural order**
* Does **not allow null key**
* Implements `NavigableMap`

```java
Map<Integer, String> map = new TreeMap<>();
map.put(3, "C");
map.put(1, "A");
map.put(2, "B");
```

**Output Order**: 1, 2, 3

---

### D. `Hashtable` (Legacy)

* Thread-safe map
* **Does not allow null keys or values**
* Slower than `HashMap`

```java
Hashtable<String, Integer> ht = new Hashtable<>();
ht.put("A", 100);
```

---

## 6. **Comparison Table**

| Class           | Type  | Ordered?   | Duplicate Allowed?    | Null Allowed? | Thread Safe? |
| --------------- | ----- | ---------- | --------------------- | ------------- | ------------ |
| `ArrayList`     | List  | Yes        | Yes                   | Yes           | No           |
| `LinkedList`    | List  | Yes        | Yes                   | Yes           | No           |
| `Vector`        | List  | Yes        | Yes                   | Yes           | Yes          |
| `Stack`         | List  | Yes (LIFO) | Yes                   | Yes           | Yes          |
| `HashSet`       | Set   | No         | No                    | One null      | No           |
| `LinkedHashSet` | Set   | Yes        | No                    | One null      | No           |
| `TreeSet`       | Set   | Sorted     | No                    | No            | No           |
| `PriorityQueue` | Queue | Sorted     | Yes                   | No            | No           |
| `ArrayDeque`    | Deque | Yes        | Yes                   | No            | No           |
| `HashMap`       | Map   | No         | Keys: No, Values: Yes | 1 null key    | No           |
| `LinkedHashMap` | Map   | Yes        | Keys: No, Values: Yes | 1 null key    | No           |
| `TreeMap`       | Map   | Sorted     | Keys: No, Values: Yes | No            | No           |
| `Hashtable`     | Map   | No         | Keys: No, Values: No  | No            | Yes          |

---

## 7. **Conclusion**

* Java provides a **rich set of collection classes** that offer efficient ways to handle data.
* Choice of class depends on:

  * **Order** requirement
  * **Thread safety**
  * **Sorting**
  * **Duplication**
  * **Null handling**
* Use the appropriate class based on the **specific use case** and **performance need**.

### Lambda Expressions in Java

---

#### 1. **Definition**

* A **lambda expression** is a **concise way to represent an anonymous function** (i.e., a method without a name).
* Introduced in **Java 8**, lambda expressions enable writing **functional-style code** in Java.
* Mainly used to implement **functional interfaces** (interfaces with a single abstract method).

---

## 2. **Syntax**

```java
(parameters) -> { body }
```

### Examples:

```java
() -> System.out.println("Hello");
x -> x * x;
(x, y) -> x + y;
```

---

## 3. **Functional Interface Requirement**

* Lambda expressions **must be assigned to a functional interface**.
* A **functional interface** is an interface with only **one abstract method**.
* Annotated using `@FunctionalInterface` (optional but recommended).

### Example:

```java
@FunctionalInterface
interface MyInterface {
    void show();
}
```

---

## 4. **Examples of Built-in Functional Interfaces (in `java.util.function`)**

| Interface           | Abstract Method     | Description                      |
| ------------------- | ------------------- | -------------------------------- |
| `Predicate<T>`      | `boolean test(T t)` | Takes one input, returns boolean |
| `Function<T,R>`     | `R apply(T t)`      | Takes input, returns output      |
| `Consumer<T>`       | `void accept(T t)`  | Takes input, returns nothing     |
| `Supplier<T>`       | `T get()`           | Takes no input, returns value    |
| `BiFunction<T,U,R>` | `R apply(T t, U u)` | Takes two inputs, returns output |

---

## 5. **Example with Custom Functional Interface**

```java
@FunctionalInterface
interface Operation {
    int operate(int a, int b);
}

public class Main {
    public static void main(String[] args) {
        Operation add = (a, b) -> a + b;
        Operation mul = (a, b) -> a * b;
        System.out.println(add.operate(5, 3)); // 8
        System.out.println(mul.operate(5, 3)); // 15
    }
}
```

---

## 6. **Using Lambda with Collections**

### A. **Using `forEach()`**

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.forEach(name -> System.out.println(name));
```

---

### B. **Using `sort()`**

```java
List<Integer> numbers = Arrays.asList(5, 2, 9, 1);
numbers.sort((a, b) -> a - b);
```

---

## 7. **Block Lambda Expression**

* If the lambda body has multiple statements, use **block `{}`** and `return` if needed.

```java
Operation sub = (a, b) -> {
    int result = a - b;
    return result;
};
```

---

## 8. **Type Inference**

* Java automatically infers the type of parameters from the context.

```java
Predicate<String> checkLength = s -> s.length() > 5;
```

---

## 9. **Use Cases of Lambda Expressions**

| Use Case                   | Description                                  |
| -------------------------- | -------------------------------------------- |
| Simplify anonymous classes | Replace them with shorter lambda syntax      |
| Event handling in GUI      | Used in Swing and JavaFX event handling      |
| Stream API                 | Filtering, mapping, reducing data            |
| Collections manipulation   | Sorting, iterating, applying transformations |
| Functional programming     | Encourages a more declarative coding style   |

---

## 10. **Lambda vs Anonymous Class**

### A. **Anonymous Class**

```java
Runnable r = new Runnable() {
    public void run() {
        System.out.println("Running");
    }
};
```

### B. **Lambda Expression**

```java
Runnable r = () -> System.out.println("Running");
```

---

## 11. **Limitations of Lambda Expressions**

| Limitation                              | Description                                         |
| --------------------------------------- | --------------------------------------------------- |
| Can use only functional interfaces      | Cannot be used for interfaces with multiple methods |
| Cannot access non-final local variables | Captured variables must be **effectively final**    |
| No checked exception handling inside    | Must handle exceptions manually                     |

---

## 12. **Conclusion**

* Lambda expressions in Java **reduce boilerplate code**, make code **more readable**, and promote **functional programming**.
* They are essential for working with **streams**, **collections**, and **functional interfaces** efficiently.

### Java Memory Management

---

#### 1. **Definition**

* **Java Memory Management** is the process of **allocating**, **managing**, and **reclaiming** memory in the Java runtime environment.
* It ensures **efficient use of memory** and avoids memory leaks.
* Memory is managed through **automatic garbage collection**, eliminating the need for manual memory deallocation.

---

## 2. **Memory Areas in JVM**

Java divides memory into the following **runtime data areas**:

### A. **Heap Memory**

* Stores **objects** and **class instances**
* Shared among all threads
* **Managed by Garbage Collector**

### B. **Stack Memory**

* Stores **method calls**, **local variables**, and **references**
* One **stack per thread**
* Automatically created/destroyed with method invocation

### C. **Method Area (or Metaspace in Java 8+)**

* Stores **class metadata**, **static variables**, **constants**
* Shared across threads

### D. **Program Counter (PC) Register**

* Each thread has its own PC
* Stores the **address of the current executing instruction**

### E. **Native Method Stack**

* Used for executing **native (non-Java) methods**

---

## 3. **Structure of Java Heap (After Java 8)**

```
Heap
├── Young Generation
│   ├── Eden Space
│   ├── Survivor Space (S0)
│   └── Survivor Space (S1)
└── Old Generation (Tenured)
```

### A. **Young Generation**

* New objects are created here
* Frequent **Minor Garbage Collections**

### B. **Old Generation**

* Stores long-lived objects
* Cleaned using **Major Garbage Collections**

---

## 4. **Garbage Collection (GC)**

* Java automatically **removes unused objects** (i.e., those with no references)
* Prevents **memory leaks**
* Involves two types:

  * **Minor GC** – Clears Young Generation
  * **Major GC** – Clears Old Generation

---

## 5. **Garbage Collector Algorithms**

| Algorithm                       | Description                                        |
| ------------------------------- | -------------------------------------------------- |
| **Serial GC**                   | Single-threaded, suitable for small apps           |
| **Parallel GC**                 | Multi-threaded for young gen, for throughput       |
| **CMS (Concurrent Mark Sweep)** | Concurrent collection with low pause time          |
| **G1 (Garbage First)**          | Region-based GC for large heap, default in Java 9+ |
| **ZGC**                         | Ultra-low pause time GC, Java 11+                  |

---

## 6. **Object Allocation Process**

1. Object created using `new` keyword.
2. Memory allocated in **Eden space**.
3. If Eden is full → **Minor GC** occurs.
4. Surviving objects moved to **Survivor spaces**.
5. After multiple cycles, long-lived objects moved to **Old Generation**.

---

## 7. **Memory Leak in Java**

* Occurs when objects are no longer needed but **still referenced**.
* Common causes:

  * Static fields
  * Improper listener registrations
  * Caching without proper eviction
  * Unclosed resources

---

## 8. **Finalization and `finalize()` Method**

* Java calls `finalize()` before GC collects an object.
* **Deprecated in Java 9**, not reliable for resource cleanup.

---

## 9. **Best Practices for Memory Management**

| Practice                             | Description                             |
| ------------------------------------ | --------------------------------------- |
| Use local variables                  | Automatically cleared after method call |
| Use try-with-resources               | Auto-close I/O, DB connections, etc.    |
| Avoid unnecessary object references  | Set large objects to `null` after use   |
| Use weak references where applicable | Prevent strong hold on memory           |
| Monitor memory usage using tools     | Use profilers like VisualVM, JConsole   |

---

## 10. **Types of References**

| Reference Type        | Description                             |
| --------------------- | --------------------------------------- |
| **Strong Reference**  | Default; prevents GC                    |
| **Weak Reference**    | Collected if no strong reference exists |
| **Soft Reference**    | Cleared only when memory is low         |
| **Phantom Reference** | Used to track object finalization       |

---

## 11. **JVM Parameters for Memory Control**

| Parameter             | Purpose                  |
| --------------------- | ------------------------ |
| `-Xms`                | Initial heap size        |
| `-Xmx`                | Maximum heap size        |
| `-Xss`                | Stack size per thread    |
| `-XX:+UseG1GC`        | Use G1 Garbage Collector |
| `-XX:+PrintGCDetails` | Print GC logs            |

---

## 12. **Tools for Memory Monitoring**

| Tool        | Description                            |
| ----------- | -------------------------------------- |
| `jconsole`  | GUI for JVM monitoring                 |
| `jvisualvm` | Visual profiler for memory/thread/GC   |
| `jstat`     | Monitors GC statistics                 |
| `MAT`       | Eclipse Memory Analyzer for heap dumps |

---

## 13. **Example: Garbage Collection in Action**

```java
public class GCExample {
    public static void main(String[] args) {
        GCExample obj = new GCExample();
        obj = null;
        System.gc();  // Suggests JVM to run GC
    }

    @Override
    protected void finalize() {
        System.out.println("Object collected");
    }
}
```

---

## 14. **Conclusion**

* Java handles memory automatically using **garbage collection**, which improves safety and productivity.
* Understanding JVM memory areas and GC behavior is essential for **writing efficient, leak-free applications**.


