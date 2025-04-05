# Python  
---

# Unit -I  
### INTRODUCTION TO PYTHON  
- Introduction to Python, Python History, Introduction to Object-oriented Programming, features of OOPs, Features of Python, “Hello world” program in Python, Keywords, Identifiers, Reading input  
- Data Types: Numeric data types - int, float, complex, Strings: Understanding string in build methods and Operations[slicing], Lists and its operations, Tuples and its operations, Dictionaries and Sets operations.  
- Operators in Python  -  Conditional blocks using if, else and elif, Simple for loops in python, For loop using ranges, Use of while and do while-loop in python, Loop manipulation using pass, continue, break and else.  

---

### 🔹 **Introduction to Python**

#### 📌 What is Python?
Python is a high-level, interpreted, general-purpose programming language. It was created by **Guido van Rossum** and released in **1991**. Python emphasizes **code readability** and has a **simple syntax** that allows programmers to express concepts in fewer lines of code compared to other programming languages like C++ or Java.

---

#### 📌 History of Python
- **1980s**: Guido van Rossum was working at Centrum Wiskunde & Informatica (CWI) in the Netherlands.
- **1989**: Started working on Python as a hobby project during Christmas.
- **1991**: Released Python 0.9.0. This version already included many features of today’s Python:
  - Functions
  - Exception handling
  - Modules
  - Core data types: str, list, dict, etc.
- **Python 2.x**: Released in 2000 (added features like list comprehensions).
- **Python 3.x**: Released in 2008 (not backward compatible; improved Unicode handling).

> The name "Python" was inspired by the British comedy series **"Monty Python's Flying Circus"**, not the snake 🐍.

---

#### 📌 Introduction to Object-Oriented Programming (OOP)

**OOP** is a programming paradigm based on the concept of **objects** which contain data (attributes) and methods (functions). It helps in organizing complex programs, promotes code reuse, and improves scalability.

##### Four Key Concepts of OOP:
1. **Encapsulation**: Wrapping data and methods into a single unit (class).
2. **Abstraction**: Hiding internal details and showing only necessary features.
3. **Inheritance**: Acquiring properties and behavior from another class.
4. **Polymorphism**: Using a unified interface for different data types (e.g., method overriding/overloading).

---

#### 📌 Features of OOPs
- Modularity: Code is divided into reusable parts (classes/objects).
- Reusability: Inherited classes can reuse code.
- Scalability: Easier to scale complex software.
- Maintainability: Modular code is easier to debug and maintain.
- Real-world modeling: Objects represent real-world entities.

---

#### 📌 Features of Python
- Easy to learn and use.
- Interpreted language (no need for compilation).
- Dynamically typed (no need to declare variables).
- Extensive standard library.
- Large community support.
- Platform-independent.
- Supports multiple programming paradigms (OOP, procedural, functional).
- Readable and clean syntax.
- Automatically manages memory (garbage collection).

---

#### 📌 Hello World Program in Python

```python
print("Hello, World!")
```

Explanation:
- `print()` is a built-in function used to display output.
- `"Hello, World!"` is a string passed to the print function.

---

#### 📌 Keywords in Python

**Keywords** are reserved words that cannot be used as variable names or identifiers.

Some examples:
```python
False, class, finally, is, return, None, continue, for, lambda, try, True,
def, from, nonlocal, while, and, del, global, not, with, as, elif, if, or, yield
```

Check all keywords using:
```python
import keyword
print(keyword.kwlist)
```

---

#### 📌 Identifiers in Python

- Identifiers are names used for variables, functions, classes, etc.
- Rules:
  - Can contain letters, digits, and underscores.
  - Cannot start with a digit.
  - Cannot use keywords.
  - Case-sensitive (`Age` ≠ `age`).

Valid examples: `name`, `student_id`, `_temp`, `isValid`
Invalid examples: `2name`, `class`, `@value`

---

#### 📌 Reading Input from the User

Use the `input()` function:
```python
name = input("Enter your name: ")
print("Hello", name)
```

- `input()` reads a string input from the user.
- To convert input to a specific type:
```python
age = int(input("Enter your age: "))  # Converts input to int
```

---

### 🔹 **Data Types in Python: Numeric Types**

Python supports multiple built-in **data types**. The first category is **Numeric types**, which are used to store numbers. These include:

---

## 1. **Integer (`int`)**
- Represents whole numbers (positive, negative, or zero) without any decimal point.

```python
a = 10
b = -25
c = 0
```

- **Type Checking**:
```python
print(type(a))  # <class 'int'>
```

- Python 3 has no fixed limit on the size of an integer. It automatically converts to long if needed.

---

## 2. **Floating-point (`float`)**
- Represents real numbers with a decimal point or in exponential (scientific) notation.

```python
x = 3.14
y = -0.5
z = 2.5e3  # 2.5 x 10^3 = 2500.0
```

- **Type Checking**:
```python
print(type(x))  # <class 'float'>
```

---

## 3. **Complex Numbers (`complex`)**
- Used for scientific and engineering purposes.
- Consist of a **real** part and an **imaginary** part.

```python
c1 = 2 + 3j
c2 = complex(4, -5)
```

- `j` or `J` represents the imaginary unit (√-1).
- **Type Checking**:
```python
print(type(c1))  # <class 'complex'>
```

- You can access real and imaginary parts:
```python
print(c1.real)  # 2.0
print(c1.imag)  # 3.0
```

---

### Numeric Type Functions and Type Conversion

- `int()`: Converts to integer.
- `float()`: Converts to float.
- `complex()`: Converts to complex.

```python
a = int(4.7)     # 4
b = float(3)     # 3.0
c = complex(2)   # (2+0j)
```

---

### Arithmetic with Numeric Types

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (modulus)
print(a ** b)   # 1000 (exponentiation)
```

---

### Summary

| Type     | Example     | Description                           |
|----------|-------------|---------------------------------------|
| `int`    | 5, -10       | Whole numbers                         |
| `float`  | 3.14, -0.1   | Numbers with decimal point            |
| `complex`| 2+3j, -1j    | Complex numbers (real + imaginary)    |

---

### 🔹 **Strings in Python**

A **string** is a sequence of characters enclosed within **single (`'`)**, **double (`"`)**, or **triple quotes (`'''` or `"""`)**. Strings in Python are **immutable**, meaning once created, they cannot be changed.

---

## 1. **Creating Strings**

```python
s1 = 'Hello'
s2 = "World"
s3 = '''This is 
a multi-line
string'''
```

---

## 2. **Accessing Characters and Indexing**

Python strings support **indexing**:

```python
s = "Python"
print(s[0])    # P
print(s[3])    # h
```

- **Negative indexing**:

```python
print(s[-1])   # n
print(s[-3])   # h
```

---

## 3. **Slicing Strings**

**Slicing** lets you extract parts of a string using `start:stop:step` syntax.

```python
s = "Programming"
print(s[0:5])    # Progr
print(s[3:8])    # gram
print(s[:])      # Programming
print(s[::2])    # Pormig
print(s[::-1])   # gnimmargorP (reversed string)
```

---

## 4. **Built-in String Methods**

| Method                | Description                             |
|------------------------|-----------------------------------------|
| `lower()`             | Converts to lowercase                   |
| `upper()`             | Converts to uppercase                   |
| `capitalize()`        | Capitalizes the first character         |
| `title()`             | Capitalizes each word                   |
| `strip()`             | Removes whitespace from both ends       |
| `lstrip()` / `rstrip()` | From left/right only                 |
| `replace(old, new)`   | Replaces substring                      |
| `find(sub)`           | Finds first index of `sub`              |
| `count(sub)`          | Counts how many times `sub` occurs      |
| `startswith()` / `endswith()` | Checks prefix/suffix         |
| `split()`             | Splits string into list                 |
| `join()`              | Joins list into string                  |

**Examples:**

```python
s = " Hello Python "
print(s.strip())         # "Hello Python"
print(s.upper())         # " HELLO PYTHON "
print(s.replace("Hello", "Hi"))  # " Hi Python "
print(s.find("Python"))  # 7
```

---

## 5. **String Operators**

```python
a = "Hello"
b = "World"

print(a + b)     # HelloWorld (Concatenation)
print(a * 3)     # HelloHelloHello
print("e" in a)  # True
```

---

## 6. **Escape Sequences**

| Sequence | Meaning              |
|----------|----------------------|
| `\n`     | New line             |
| `\t`     | Tab space            |
| `\\`     | Backslash            |
| `\'`     | Single quote         |
| `\"`     | Double quote         |

```python
print("Hello\nWorld")
```

---

### Summary

- Strings are immutable sequences of Unicode characters.
- Use slicing to extract substrings.
- Built-in methods provide powerful text manipulation tools.

---

### 🔹 **Lists and Their Operations in Python**

A **list** is a **mutable**, **ordered**, **indexable** collection of elements in Python. It can hold mixed data types (integers, strings, objects, etc.).

#### 1. **Creating a List**

```python
my_list = [1, 2, 3, 4]
mixed_list = [1, "hello", 3.14, True]
nested_list = [1, [2, 3], 4]
```

---

#### 2. **Accessing List Elements**

```python
print(my_list[0])     # 1
print(my_list[-1])    # 4
print(nested_list[1]) # [2, 3]
print(nested_list[1][1])  # 3
```

---

#### 3. **List Slicing**

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])    # [20, 30, 40]
print(my_list[:3])     # [10, 20, 30]
print(my_list[::-1])   # [50, 40, 30, 20, 10]
```

---

#### 4. **Modifying a List**

Lists are mutable, meaning we can change, add, or remove items:

```python
my_list[2] = 99        # Replace element
my_list.append(60)     # Add to end
my_list.insert(1, 15)  # Insert at index
```

---

#### 5. **Deleting Elements**

```python
del my_list[2]         # Delete element at index
my_list.remove(40)     # Remove by value
my_list.pop()          # Removes last item
my_list.pop(1)         # Removes item at index
my_list.clear()        # Removes all elements
```

---

#### 6. **List Methods**

| Method               | Description                          |
|----------------------|--------------------------------------|
| `append(x)`          | Adds `x` to end                      |
| `insert(i, x)`       | Inserts `x` at index `i`             |
| `extend([a, b])`     | Appends multiple values              |
| `remove(x)`          | Removes first occurrence of `x`      |
| `pop(i)`             | Removes element at index `i`         |
| `sort()`             | Sorts the list                       |
| `reverse()`          | Reverses the list                    |
| `index(x)`           | Returns index of first `x`           |
| `count(x)`           | Counts occurrences of `x`            |
| `copy()`             | Returns a copy of list               |

**Example:**

```python
nums = [5, 2, 9, 1]
nums.sort()
print(nums)     # [1, 2, 5, 9]
nums.reverse()
print(nums)     # [9, 5, 2, 1]
```

---

#### 7. **List Comprehension**

```python
squares = [x**2 for x in range(5)]    # [0, 1, 4, 9, 16]
even = [x for x in range(10) if x%2==0]  # [0, 2, 4, 6, 8]
```

---

### Summary

- Lists are mutable, ordered sequences.
- Powerful methods to add, remove, or search.
- Support slicing, iteration, and comprehension.

---

### 🔹 **Tuples and Their Operations in Python**

A **tuple** is similar to a list, but **immutable** — once defined, its elements cannot be changed.

#### 1. **Creating a Tuple**

```python
t1 = (1, 2, 3)
t2 = ("apple", 3.14, True)
t3 = (1,)          # single-element tuple (notice the comma)
t4 = tuple([4, 5]) # from a list
```

---

#### 2. **Accessing Tuple Elements**

```python
print(t1[0])     # 1
print(t2[-1])    # True
```

---

#### 3. **Tuple Slicing**

```python
t = (10, 20, 30, 40, 50)
print(t[1:4])     # (20, 30, 40)
print(t[::-1])    # (50, 40, 30, 20, 10)
```

---

#### 4. **Immutability of Tuples**

You **cannot** modify, delete or append to a tuple.

```python
t = (1, 2, 3)
# t[0] = 99       # Error: TypeError
# t.append(4)     # Error: AttributeError
```

But if a tuple contains **mutable objects**, those objects can be changed.

```python
t = ([1, 2], 3)
t[0].append(3)     # This is allowed
print(t)           # ([1, 2, 3], 3)
```

---

#### 5. **Tuple Methods**

Tuples have only **two built-in methods**:

| Method      | Description                           |
|-------------|---------------------------------------|
| `count(x)`  | Counts the number of occurrences of x |
| `index(x)`  | Returns the first index of x          |

```python
t = (1, 2, 2, 3)
print(t.count(2))     # 2
print(t.index(3))     # 3
```

---

#### 6. **Tuple Packing and Unpacking**

```python
# Packing
t = 1, "hello", 3.5

# Unpacking
a, b, c = t
print(a)  # 1
print(b)  # "hello"
print(c)  # 3.5
```

---

#### 7. **Why Use Tuples?**

- More **memory-efficient** than lists.
- Safer to use when data shouldn't change.
- Often used as **dictionary keys** (lists cannot be).

---

### Summary

- Tuples are **immutable** and **ordered**.
- Support indexing, slicing, unpacking.
- Fewer methods than lists, but more efficient in many cases.

---

### 🔷 **Dictionaries and Set Operations in Python**

---

## **1. Dictionaries in Python**

A **dictionary** is a collection of **key-value** pairs. It's **unordered**, **mutable**, and **indexed by keys** (not positions).

#### **Creating a Dictionary**

```python
student = {"name": "Alice", "age": 21, "course": "Python"}
```

You can also create dictionaries using the `dict()` constructor:

```python
student = dict(name="Alice", age=21)
```

---

#### **Accessing Values**

```python
print(student["name"])      # Alice
print(student.get("age"))   # 21
```

> `.get()` is safer — it returns `None` instead of throwing an error if key doesn’t exist.

---

#### **Modifying Dictionary**

```python
student["age"] = 22         # Update value
student["email"] = "a@mail.com"  # Add new key-value pair
```

---

#### **Removing Elements**

```python
del student["course"]
student.pop("email")        # Removes and returns value
student.clear()             # Empties the dictionary
```

---

#### **Dictionary Methods**

| Method            | Description                              |
|-------------------|------------------------------------------|
| `keys()`          | Returns a view of all keys               |
| `values()`        | Returns a view of all values             |
| `items()`         | Returns a view of all key-value pairs    |
| `get(key)`        | Gets the value for a key                 |
| `update(dict2)`   | Adds items from another dictionary       |
| `pop(key)`        | Removes key and returns value            |

```python
for k, v in student.items():
    print(k, v)
```

---

#### **Nested Dictionaries**

```python
students = {
    "s1": {"name": "A", "age": 20},
    "s2": {"name": "B", "age": 22}
}
```

---

## **2. Sets in Python**

A **set** is an **unordered**, **mutable**, and **unindexed** collection of **unique** elements.

#### **Creating a Set**

```python
s = {1, 2, 3}
s2 = set([3, 4, 5])
```

Duplicates are **automatically removed**:

```python
s = {1, 1, 2, 2, 3}
print(s)        # {1, 2, 3}
```

---

#### **Set Operations**

| Operation | Symbol | Example |
|----------|--------|---------|
| Union        | `|` or `.union()`       | `s1 | s2`        |
| Intersection | `&` or `.intersection()`| `s1 & s2`        |
| Difference   | `-` or `.difference()`  | `s1 - s2`        |
| Symmetric Difference | `^` | `s1 ^ s2`   |

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(a & b)  # {3}
```

---

#### **Set Methods**

| Method         | Description                        |
|----------------|------------------------------------|
| `add(x)`       | Adds an element                    |
| `update(iter)` | Adds multiple elements             |
| `remove(x)`    | Removes x, error if not present    |
| `discard(x)`   | Removes x, no error if missing     |
| `clear()`      | Empties the set                    |
| `pop()`        | Removes and returns random element |

---

#### **Frozen Set**

An **immutable** set:

```python
fs = frozenset([1, 2, 3])
# fs.add(4) → Error
```

---

### ✅ Summary

- **Dictionaries** store key-value pairs, support fast lookups.
- **Sets** store unique values and are great for mathematical operations.
- Both are **mutable** and powerful in data processing.

---

Next up:
**➡ Operators in Python**  
Shall we move on?

Great! Let’s now dive into:

---

### 🔶 **Operators in Python**

Operators are **symbols or words** used to perform **operations** on variables and values. Python supports several types of operators:

---

## **1. Arithmetic Operators**

Used for **basic math operations**.

| Operator | Description       | Example     | Result |
|----------|-------------------|-------------|--------|
| `+`      | Addition           | `3 + 2`     | `5`    |
| `-`      | Subtraction        | `5 - 1`     | `4`    |
| `*`      | Multiplication     | `4 * 3`     | `12`   |
| `/`      | Division           | `10 / 2`    | `5.0`  |
| `//`     | Floor Division     | `10 // 3`   | `3`    |
| `%`      | Modulus (Remainder)| `10 % 3`    | `1`    |
| `**`     | Exponentiation     | `2 ** 3`    | `8`    |

---

## **2. Assignment Operators**

Used to **assign values** to variables.

| Operator | Example      | Same as       |
|----------|--------------|---------------|
| `=`      | `x = 5`      | Assign 5 to x |
| `+=`     | `x += 3`     | `x = x + 3`   |
| `-=`     | `x -= 2`     | `x = x - 2`   |
| `*=`     | `x *= 4`     | `x = x * 4`   |
| `/=`     | `x /= 2`     | `x = x / 2`   |
| `//=`    | `x //= 3`    | `x = x // 3`  |
| `%=`     | `x %= 2`     | `x = x % 2`   |
| `**=`    | `x **= 2`    | `x = x ** 2`  |

---

## **3. Comparison Operators**

Used to **compare values** and return Boolean results (`True` or `False`).

| Operator | Description        | Example     | Result     |
|----------|--------------------|-------------|------------|
| `==`     | Equal to           | `2 == 2`    | `True`     |
| `!=`     | Not equal to       | `2 != 3`    | `True`     |
| `>`      | Greater than       | `5 > 3`     | `True`     |
| `<`      | Less than          | `3 < 5`     | `True`     |
| `>=`     | Greater or equal   | `4 >= 4`    | `True`     |
| `<=`     | Less or equal      | `2 <= 3`    | `True`     |

---

## **4. Logical Operators**

Used to combine conditional statements.

| Operator | Description          | Example             | Result      |
|----------|----------------------|---------------------|-------------|
| `and`    | True if both true    | `x > 2 and x < 5`   | `True`      |
| `or`     | True if one is true  | `x > 2 or x == 1`   | `True`      |
| `not`    | Inverts result       | `not(x > 2)`        | `False`     |

---

## **5. Identity Operators**

Used to compare object identities (memory locations).

| Operator | Description                      | Example        |
|----------|----------------------------------|----------------|
| `is`     | Returns True if same object      | `x is y`       |
| `is not` | Returns True if not same object  | `x is not y`   |

> Even if values are same, identity may differ for mutable objects.

---

## **6. Membership Operators**

Used to check if a value is in a sequence (list, string, etc.).

| Operator | Description           | Example         |
|----------|-----------------------|-----------------|
| `in`     | True if value exists  | `'a' in 'cat'`  |
| `not in` | True if not exists    | `5 not in [1,2]`|

---

## **7. Bitwise Operators**

Operate on bits (binary representations).

| Operator | Description     | Example     | Result   |
|----------|------------------|-------------|----------|
| `&`      | AND              | `5 & 3`     | `1`      |
| `|`      | OR               | `5 | 3`     | `7`      |
| `^`      | XOR              | `5 ^ 3`     | `6`      |
| `~`      | NOT              | `~5`        | `-6`     |
| `<<`     | Left Shift       | `5 << 1`    | `10`     |
| `>>`     | Right Shift      | `5 >> 1`    | `2`      |

---

### ✅ Summary

- Use **arithmetic** for math, **comparison** for conditions, **logical** for compound conditions.
- **Assignment**, **identity**, and **membership** operators are useful in data structures.
- **Bitwise** are more advanced — useful in low-level and performance-heavy tasks.

---

### 🔷 **Conditional Blocks in Python: `if`, `else`, `elif`**

Conditional blocks control the flow of your program based on **conditions**. Python uses `if`, `elif`, and `else` to implement conditional logic.

---

## **1. Basic `if` Statement**

Syntax:

```python
if condition:
    # code to execute if condition is true
```

Example:

```python
age = 20
if age >= 18:
    print("You are eligible to vote.")
```

---

## **2. `if...else` Statement**

Used when you want to run a block **if the condition is true**, and **another block if false**.

```python
if condition:
    # if block
else:
    # else block
```

Example:

```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## **3. `if...elif...else` Statement**

Use **`elif` (else if)** when checking **multiple conditions**.

```python
if condition1:
    # block1
elif condition2:
    # block2
else:
    # else block
```

Example:

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

---

## **4. Nested `if` Statements**

You can place one `if` block **inside another**.

```python
x = 10
y = 5

if x > 0:
    if y > 0:
        print("Both numbers are positive")
```

---

## **5. Ternary Operator (One-liner `if` Expression)**

```python
result = "Even" if num % 2 == 0 else "Odd"
```

---

### ✅ Summary

- Use `if` when there’s only one condition.
- Use `if...else` for binary decisions.
- Use `if...elif...else` to handle multiple options.
- Nested `if` is useful for multi-level conditions.
- Ternary (`x if condition else y`) is concise for simple assignments.

---

### 🔷 **Simple `for` Loops in Python**

A `for` loop is used to **iterate** over a **sequence** (like a list, tuple, string, or range). It executes a block of code **for each item** in the sequence.

---

## **1. Basic Syntax**

```python
for variable in sequence:
    # block of code
```

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

---

## **2. Iterating Over a String**

```python
for letter in "Python":
    print(letter)
```

Output:
```
P
y
t
h
o
n
```

---

## **3. Using `range()` Function**

`range(start, stop, step)` generates a sequence of numbers:

- `start` → optional (default is 0)
- `stop` → required
- `step` → optional (default is 1)

### Examples:

```python
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```

```python
for i in range(1, 6):
    print(i)
```
Output:
```
1
2
3
4
5
```

```python
for i in range(2, 11, 2):  # Even numbers from 2 to 10
    print(i)
```
Output:
```
2
4
6
8
10
```

---

## **4. Loop with List**

```python
numbers = [10, 20, 30]
for num in numbers:
    print("Value:", num)
```

---

## **5. Looping with Index using `range()` and `len()`**

```python
names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(i, names[i])
```

---

## **6. Nested `for` Loop**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

---

### ✅ Summary

- `for` loops are clean and readable.
- `range()` is often used to loop a specific number of times.
- You can loop over lists, strings, tuples, and dictionaries.

---

### 🔷 **For Loop Using `range()` in Python**

The `range()` function is one of the most commonly used tools in Python `for` loops. It generates a sequence of numbers, which are commonly used for iteration purposes.

---

## **1. Syntax of `range()`**

```python
range(start, stop, step)
```

- `start`: The beginning of the sequence (default is 0).
- `stop`: The end of the sequence (not inclusive).
- `step`: The difference between each number in the sequence (default is 1).

---

## **2. Examples of `range()` with `for` Loop**

### i. Basic `range(stop)` (from 0 to stop-1)

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

### ii. Using `range(start, stop)`

```python
for i in range(3, 8):
    print(i)
```

**Output:**
```
3
4
5
6
7
```

---

### iii. Using `range(start, stop, step)`

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:**
```
2
4
6
8
```

### iv. Reverse iteration using a negative step

```python
for i in range(10, 0, -1):
    print(i)
```

**Output:**
```
10
9
8
7
6
5
4
3
2
1
```

---

## **3. Looping Over Indexes of a List**

```python
colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(f"Index {i} = {colors[i]}")
```

---

## **4. Loop with Condition inside `for`**

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
```

---

### ✅ Summary

- `range()` is powerful for numeric iteration.
- You can use `range()` with 1, 2, or 3 arguments.
- Works great when looping by index or count.

---

### 🔷 **Use of `while` and `do while`-like Loop in Python**

Python does **not** have a built-in `do-while` loop like some other languages (C, C++, Java). However, we can **simulate** a `do-while` loop using a `while` loop.

---

## **1. `while` Loop in Python**

A `while` loop executes as long as the condition is `True`.

### **Syntax:**
```python
while condition:
    # block of code
```

---

### **Example 1: Basic `while` loop**

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**
```
1
2
3
4
5
```

---

### **Example 2: `while` loop with user input**

```python
name = ""
while name != "exit":
    name = input("Type 'exit' to quit: ")
```

---

## **2. Simulating a `do-while` Loop in Python**

A **`do-while` loop** is a loop that runs **at least once** before checking the condition.

### **Python Simulation:**

```python
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    print(f"You entered {num}")
```

**Explanation:**
- The loop runs **at least once**.
- The condition is checked **after** the input is taken.
- This mimics a `do-while` behavior.

---

## **3. Example: Sum of numbers until user enters 0**

```python
sum = 0
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    sum += num
print(f"Total sum is: {sum}")
```

---

### ✅ Summary:

- `while` loop is used when the number of iterations is **unknown**.
- Python doesn’t have `do-while` explicitly, but we simulate it using `while True` and `break`.

---

## **🔷 Loop Manipulation using `pass`, `continue`, `break`, and `else` in Python**

Python provides control statements to **manipulate the flow of loops**.

---

### **1. `break` Statement**

- Used to **exit the loop immediately**, even if the condition is still `True`.
- Useful when a terminating condition is met **inside** the loop.

#### **Example:**

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

**Output:**
```
1
2
3
4
```

---

### **2. `continue` Statement**

- Skips the **rest of the code inside the loop** for the current iteration.
- The loop does **not exit**; it continues to the next iteration.

#### **Example:**

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**
```
1
2
4
5
```

(`3` is skipped)

---

### **3. `pass` Statement**

- Does **nothing**; acts as a placeholder.
- Often used when the code is syntactically required but you don’t want to write anything (yet).

#### **Example:**

```python
for i in range(1, 4):
    if i == 2:
        pass  # Placeholder
    print(i)
```

**Output:**
```
1
2
3
```

---

### **4. `else` with Loops**

- The `else` block after a `for` or `while` loop executes **only if the loop completes normally** (i.e., not interrupted by `break`).

#### **Example with `for` loop:**

```python
for i in range(5):
    print(i)
else:
    print("Loop finished")
```

**Output:**
```
0
1
2
3
4
Loop finished
```

---

#### **Example with `break`:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished")
```

**Output:**
```
0
1
2
```

(No `"Loop finished"` because of `break`)

---

### ✅ Summary Table:

| Statement | Description |
|-----------|-------------|
| `break`   | Exits the loop immediately |
| `continue` | Skips current iteration and continues |
| `pass`    | Does nothing (placeholder) |
| `else`    | Executes if loop completes normally |

---

# Unit -III  
### FUNCTIONS, EXCEPTION, AND FILES  
- Functions: Types, parameters, arguments: positional arguments, keyword arguments, parameters with default values, functions with arbitrary arguments, Scope of variables: Local and global scope, Recursion and Lambda functions. Function Decorators, Generators  
- Structured Programming, Exceptions, Exception Handling, Types of Exceptions, The Except Block, the assert Statement, UserDefined Exceptions, Logging the Exceptions  
- Files: Files, Types of Files in Python, Opening a File, Closing a File, Working with Text Files Containing Strings, Knowing Whether a File Exists or Not, Working with Binary Files, The with Statement, Pickle in Python, The seek() and tell() Methods  

---

### **Basics of NumPy**

NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them.

#### **1. Why NumPy?**
- Native Python lists are slow for numerical operations.
- NumPy arrays are faster and more memory-efficient.
- Provides vectorized operations (element-wise calculations) without explicit loops.

#### **2. NumPy Arrays (ndarray)**
The core of NumPy is the `ndarray` object.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)
```

- `np.array()` is used to create an array.
- Arrays can be 1D, 2D, 3D, etc.

```python
# 2D array
arr_2d = np.array([[1, 2], [3, 4]])
```

#### **3. Array Properties**
- `arr.shape`: dimensions of the array
- `arr.ndim`: number of dimensions
- `arr.dtype`: data type
- `arr.size`: total number of elements
- `arr.itemsize`: size in bytes of each element

#### **4. Creating Arrays**
- `np.zeros((2,3))` – 2x3 array of zeros
- `np.ones((3,3))` – 3x3 array of ones
- `np.eye(4)` – 4x4 identity matrix
- `np.arange(0, 10, 2)` – array from 0 to 8 with step 2
- `np.linspace(0, 1, 5)` – 5 values from 0 to 1

#### **5. Reshaping Arrays**
```python
a = np.arange(12)
a.reshape(3, 4)  # reshape into 3 rows, 4 columns
```

#### **6. Indexing and Slicing**
```python
arr = np.array([10, 20, 30, 40])
print(arr[2])      # 30
print(arr[1:3])    # [20 30]
```

#### **7. Multi-dimensional Indexing**
```python
arr = np.array([[1,2,3], [4,5,6]])
print(arr[1,2])  # 6
```

---

### **Computation on NumPy Arrays**

One of the most powerful features of NumPy is the ability to perform vectorized operations. That means operations are applied element-wise, often eliminating the need for loops and making code much faster.

---

#### **1. Arithmetic Operations**

These operations are applied element-wise:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)   # [11 22 33]
print(a - b)   # [ 9 18 27]
print(a * b)   # [10 40 90]
print(a / b)   # [10. 10. 10.]
print(a ** 2)  # [100 400 900]
```

---

#### **2. Universal Functions (ufuncs)**

NumPy provides **ufuncs**—fast element-wise functions:

```python
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.power(a, 2)
np.mod(a, b)
```

**Mathematical functions:**
```python
np.sin(a)
np.log(a)
np.exp(a)
np.sqrt(a)
```

These work element-wise too.

---

#### **3. Broadcasting**

Broadcasting allows NumPy to perform operations between arrays of different shapes.

```python
a = np.array([1, 2, 3])
b = 5
print(a + b)  # [6 7 8]
```

Here, `b` is broadcast to `[5, 5, 5]`.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([1, 0, 1])
print(a + b)
# Output:
# [[2 2 4]
#  [5 5 7]]
```

---

#### **4. Aggregation Functions**

These functions summarize the contents of an array:

```python
a = np.array([1, 2, 3, 4, 5])

a.sum()      # 15
a.min()      # 1
a.max()      # 5
a.mean()     # 3.0
a.std()      # 1.414...
a.var()      # 2.0
```

**For multi-dimensional arrays:**
```python
m = np.array([[1, 2], [3, 4]])
m.sum(axis=0)  # [4 6] (sum of columns)
m.sum(axis=1)  # [3 7] (sum of rows)
```

---

## **Comparisons, Masks, and Boolean Arrays**

NumPy makes it easy to compare arrays and filter data using **boolean indexing** and **masks**. This is extremely useful for data analysis and filtering operations.

---

### **1. Element-wise Comparison Operators**

These return Boolean arrays:

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a < 3)     # [ True  True False False False ]
print(a >= 3)    # [False False  True  True  True ]
print(a == 3)    # [False False  True False False]
print(a != 3)    # [ True  True False  True  True ]
```

---

### **2. Boolean Arrays as Masks**

You can use these boolean arrays to filter elements:

```python
mask = a > 3
print(mask)         # [False False False  True  True]
print(a[mask])      # [4 5]
```

Shorter form:

```python
print(a[a > 3])     # [4 5]
```

---

### **3. Combining Conditions**

Use logical operators `&` (and), `|` (or), and `~` (not):

```python
print(a[(a > 2) & (a < 5)])   # [3 4]
print(a[(a < 2) | (a > 4)])   # [1 5]
print(a[~(a > 3)])            # [1 2 3]
```

**Note:** Parentheses are required due to operator precedence.

---

### **4. Boolean Indexing in 2D Arrays**

```python
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[b > 3])  # [4 5 6]
```

This flattens the result as it returns only matching elements.

---

### **5. `np.where()` Function**

`np.where()` returns indices or elements based on a condition:

```python
a = np.array([10, 20, 30, 40])

indices = np.where(a > 25)
print(indices)       # (array([2, 3]),)
print(a[indices])    # [30 40]
```

Use it to apply a conditional operation:

```python
np.where(a > 25, 1, 0)  # [0 0 1 1]
```
---

## **Fancy Indexing in NumPy**

**Fancy indexing** is a way to access multiple array elements at once using arrays (or lists) of indices, rather than slices.

It’s powerful when you want to pick specific elements in a non-contiguous way.

---

### **1. Indexing with Lists or Arrays**

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])
indexes = [1, 3, 4]

print(a[indexes])   # Output: [20 40 50]
```

You can use NumPy arrays as indexes too:

```python
i = np.array([0, 2, 4])
print(a[i])         # Output: [10 30 50]
```

---

### **2. Fancy Indexing in 2D Arrays**

For 2D arrays, you can access rows and columns specifically:

```python
b = np.array([[1, 2], [3, 4], [5, 6]])
print(b[[0, 2]])   # Output: rows 0 and 2 -> [[1 2], [5 6]]
```

You can even get specific elements using two index arrays:

```python
b = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

rows = [0, 1, 2]
cols = [2, 0, 1]

print(b[rows, cols])  # Output: [30 40 80]
```

Each pair (row[i], col[i]) gives the position of the desired element.

---

### **3. Using `np.ix_()` for Multi-Dimensional Fancy Indexing**

```python
x = np.array([[1, 2, 3],
              [4, 5, 6]])

rows = np.array([0, 1])
cols = np.array([0, 2])

print(x[np.ix_(rows, cols)])
# Output:
# [[1 3]
#  [4 6]]
```

`np.ix_()` helps in selecting submatrices by broadcasting the indices correctly.

---

### **4. Modifying Values Using Fancy Indexing**

```python
a = np.array([10, 20, 30, 40, 50])
a[[1, 3]] = -1
print(a)  # [10 -1 30 -1 50]
```

---

### **5. Duplicates Allowed in Fancy Indexing**

You can repeat indices:

```python
a = np.array([10, 20, 30])
print(a[[0, 0, 1]])  # [10 10 20]
```

---

**Fancy indexing** is often used in:

- Image processing (to select pixels),
- Machine learning (batch sampling),
- And data wrangling tasks.

---

## **Sorting Arrays in NumPy**

Sorting is an essential operation in data analysis and scientific computing. NumPy provides powerful tools to sort arrays efficiently.

---

### **1. `np.sort()` Function (Returns a Sorted Copy)**

This function returns a sorted **copy** of an array, without modifying the original.

```python
import numpy as np

a = np.array([3, 1, 4, 5, 2])
sorted_a = np.sort(a)

print(sorted_a)  # Output: [1 2 3 4 5]
print(a)         # Original remains unchanged: [3 1 4 5 2]
```

---

### **2. Sorting Multidimensional Arrays**

By default, it sorts along the last axis. You can change it using the `axis` parameter.

```python
b = np.array([[5, 2, 3],
              [7, 8, 1]])

# Sort each row (axis=1)
print(np.sort(b, axis=1))
# Output:
# [[2 3 5]
#  [1 7 8]]

# Sort each column (axis=0)
print(np.sort(b, axis=0))
# Output:
# [[5 2 1]
#  [7 8 3]]
```

---

### **3. `np.argsort()` (Returns the Indices of the Sorted Elements)**

Instead of the sorted values, this gives you the indices that would sort the array.

```python
a = np.array([4, 1, 3])
indices = np.argsort(a)

print(indices)      # Output: [1 2 0]
print(a[indices])   # Output: [1 3 4]
```

Very useful when sorting one array but applying the same changes to another (e.g., sorting labels with data).

---

### **4. Sorting with `kind` Parameter**

NumPy allows multiple sorting algorithms:

- `'quicksort'` (default)
- `'mergesort'` (stable)
- `'heapsort'`
- `'stable'` (new in recent versions, same as mergesort)

```python
a = np.array([3, 2, 1])
print(np.sort(a, kind='mergesort'))
```

Use `'mergesort'` when stability is important, such as sorting objects with identical keys.

---

### **5. Sorting Structured Arrays**

You can sort based on fields:

```python
data = np.array([(1, 'apple'), (3, 'banana'), (2, 'cherry')],
                dtype=[('id', 'i4'), ('fruit', 'U10')])

sorted_data = np.sort(data, order='id')
print(sorted_data)
```

You can also sort by multiple fields: `order=['fruit', 'id']`.

---

### Summary:

| Function         | Description                                      |
|------------------|--------------------------------------------------|
| `np.sort()`      | Returns a sorted **copy**                        |
| `np.argsort()`   | Returns the **indices** that would sort an array |
| `axis`           | Specifies row-wise or column-wise sorting        |
| `order`          | Used for structured arrays                       |

---

## **Structured Data: NumPy’s Structured Arrays**

Structured arrays allow you to store **heterogeneous data** (i.e., data with different data types) in a single NumPy array. This is useful when you want to mimic a database table or a spreadsheet-like structure.

---

### **1. What is a Structured Array?**

A structured array is like a record array where each element is a compound object with named fields (columns) of potentially different types.

---

### **2. Creating a Structured Array**

You define the structure using a list of `(name, type)` tuples:

```python
import numpy as np

data = np.array([(1, 'Alice', 9.5),
                 (2, 'Bob', 8.2)],
                dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')])

print(data)
```

**Output:**

```
[(1, 'Alice', 9.5) (2, 'Bob', 8.2)]
```

---

### **3. Accessing Fields**

You can access each column using its name:

```python
print(data['id'])      # Output: [1 2]
print(data['name'])    # Output: ['Alice' 'Bob']
```

---

### **4. Filtering Structured Arrays**

You can apply conditions using any field:

```python
high_scores = data[data['score'] > 9.0]
print(high_scores)
```

**Output:**

```
[(1, 'Alice', 9.5)]
```

---

### **5. Sorting Structured Arrays by Field**

Use `np.sort()` with the `order` parameter:

```python
sorted_by_score = np.sort(data, order='score')
print(sorted_by_score)
```

You can also sort by multiple fields:

```python
np.sort(data, order=['score', 'name'])
```

---

### **6. Adding a New Field (Requires Structured Tricks)**

NumPy arrays are fixed size. But you can create a new array with an additional field:

```python
from numpy.lib import recfunctions as rfn

new_data = rfn.append_fields(data, 'passed', [True, False], usemask=False)
print(new_data)
```

---

### **7. Use Cases of Structured Arrays**

- Reading structured CSV data without using Pandas.
- Efficient memory use for large datasets with mixed types.
- High-performance filtering and slicing on structured fields.

---

### **Summary Table**

| Feature                  | Example                                   |
|--------------------------|-------------------------------------------|
| Define structure         | `dtype=[('id', 'i4'), ('name', 'U10')]`   |
| Access field             | `data['name']`                            |
| Conditional filtering    | `data[data['score'] > 9]`                 |
| Sorting                  | `np.sort(data, order='score')`            |
| Add field                | `append_fields()` from `recfunctions`     |

---

## **Introduction to Pandas Objects**

Pandas provides two primary data structures:

### 1. **Series**
- A **one-dimensional** labeled array.
- Think of it like a column in Excel or a single column in a database.

**Creating a Series:**
```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

**Output:**
```
0    10
1    20
2    30
3    40
dtype: int64
```

You can also assign custom indices:
```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

---

### 2. **DataFrame**
- A **two-dimensional** labeled data structure (like an Excel sheet or SQL table).
- Columns can be of **different data types**.

**Creating a DataFrame from a dictionary:**
```python
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35
```

---

### 3. **Index**
- The Index object in pandas is used to label rows or columns.
- It helps in fast lookups, slicing, and data alignment.

```python
print(df.index)
print(df.columns)
```

---

### 4. **Other Ways to Create a DataFrame**

#### From a list of lists:
```python
data = [[1, 'Math'], [2, 'Science']]
df = pd.DataFrame(data, columns=['ID', 'Subject'])
```

#### From a NumPy array:
```python
import numpy as np
arr = np.array([[10, 20], [30, 40]])
df = pd.DataFrame(arr, columns=['A', 'B'])
```

---

### 5. **Viewing and Inspecting Data**

```python
df.head()       # First 5 rows
df.tail(2)      # Last 2 rows
df.shape        # Dimensions of the DataFrame
df.info()       # Summary of DataFrame
df.describe()   # Statistical summary for numerical columns
```

---

### 6. **Why Pandas?**
- High-performance, easy-to-use data structures.
- Integrated tools for reading/writing data from various formats (CSV, Excel, SQL, etc.).
- Powerful data cleaning, filtering, aggregation, reshaping, and visualization capabilities.

---

### Quick Recap

| Concept    | Description                                      |
|------------|--------------------------------------------------|
| Series     | One-dimensional labeled array                    |
| DataFrame  | Two-dimensional labeled tabular structure        |
| Index      | Labels for rows and columns                      |
| Creation   | From dicts, lists, arrays, CSV, etc.             |
| Methods    | `head()`, `tail()`, `shape()`, `describe()`, etc.|

---

## **Data Indexing and Selection in Pandas**

Data indexing is the process of selecting rows, columns, or subsets of data from a `Series` or `DataFrame`.

Pandas provides several ways to access and manipulate data:

---

### 1. **Accessing Columns**

You can access a column using:
```python
df['column_name']     # Returns a Series
df.column_name        # Works if the column name is a valid identifier
```

Example:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

print(df['name'])       # Access using brackets
print(df.name)          # Access using dot notation
```

---

### 2. **Accessing Rows**

#### a. Using `iloc` (integer-location based indexing):
```python
df.iloc[0]         # First row (position 0)
df.iloc[1:3]       # Rows from index 1 to 2 (exclusive of 3)
```

#### b. Using `loc` (label-based indexing):
```python
df.loc[0]          # Access row with label/index 0
df.loc[1:2]        # Includes both 1 and 2 (not exclusive)
```

---

### 3. **Accessing Specific Cell Values**

```python
df.loc[0, 'name']      # Value at row index 0 and column 'name'
df.iloc[1, 1]          # Value at second row and second column
```

---

### 4. **Boolean Indexing / Filtering Rows**

You can filter rows based on conditions:
```python
df[df['age'] > 25]       # Rows where age > 25
df[df['name'] == 'Bob']  # Rows where name is Bob
```

---

### 5. **Selecting Multiple Columns**

```python
df[['name', 'age']]     # Double brackets for multiple columns
```

---

### 6. **Using Conditions with Multiple Filters**

```python
df[(df['age'] > 25) & (df['name'] == 'Bob')]
```

Note: Use `&`, `|`, and parentheses `()` for multiple conditions.

---

### 7. **Setting a Column as Index**

```python
df.set_index('name', inplace=True)
```

This makes `'name'` the row label for easier access.

---

### 8. **Resetting Index**

```python
df.reset_index(inplace=True)
```

This reverts the DataFrame back to default integer indexing.

---

### 9. **Slicing Rows**

Just like Python lists:
```python
df[0:3]          # First three rows
```

---

### Summary Table

| Method        | Usage                                   |
|---------------|------------------------------------------|
| `df['col']`   | Access a column                          |
| `df.iloc[]`   | Access by integer index                  |
| `df.loc[]`    | Access by label/index name               |
| `df[cond]`    | Filter rows with a condition             |
| `df[['col1', 'col2']]` | Select multiple columns         |
| `set_index()` | Set a column as index                   |
| `reset_index()` | Reset to default integer index        |

---

## **Operating on Data in Pandas**

Pandas provides powerful operations for transforming, analyzing, and manipulating data efficiently. Here's an in-depth look:

---

### 1. **Arithmetic Operations**

Pandas allows you to perform vectorized operations on `Series` and `DataFrame` objects.

```python
import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

print(data + 1)           # Add 1 to every element
print(data * 2)           # Multiply each element by 2
```

Operations are **element-wise** and **broadcast-compatible**.

---

### 2. **Column-wise or Row-wise Operations**

Use `axis=0` for columns and `axis=1` for rows.

```python
print(data.sum(axis=0))   # Sum of each column
print(data.sum(axis=1))   # Sum of each row
```

---

### 3. **Aggregation Functions**

These include functions like:

- `sum()`, `mean()`, `median()`, `min()`, `max()`, `std()`, `var()`

Example:
```python
print(data.mean())        # Column-wise mean
print(data['A'].max())    # Maximum value in column A
```

---

### 4. **Applying Custom Functions with `apply()`**

```python
def square(x):
    return x * x

print(data['A'].apply(square))  # Apply to a column
```

You can also use lambda functions:
```python
data['A'].apply(lambda x: x ** 2)
```

For entire rows or columns:
```python
data.apply(np.sqrt)        # Applies sqrt to each value
```

---

### 5. **Descriptive Statistics**

```python
data.describe()  # Summary: count, mean, std, min, 25%, 50%, 75%, max
```

---

### 6. **Element-wise Comparisons**

```python
data > 15      # Boolean DataFrame
(data['B'] > 15).sum()  # Number of rows where column B > 15
```

---

### 7. **Using `map()` with Series**

Useful for transforming values in a Series.

```python
data['A'].map(lambda x: 'Even' if x % 2 == 0 else 'Odd')
```

---

### 8. **Using `applymap()` on DataFrame**

Used to apply a function to **every element** in the DataFrame:

```python
data.applymap(lambda x: x * 10)
```

---

### 9. **Using `agg()` for Multiple Aggregations**

```python
data.agg({
    'A': ['min', 'max', 'sum'],
    'B': ['mean', 'std']
})
```

---

### 10. **Chaining Operations**

You can chain operations for cleaner code:

```python
result = data[data['A'] > 1]['B'].mean()
```

---

### Summary

| Operation          | Function                             |
|--------------------|--------------------------------------|
| Arithmetic         | `+`, `-`, `*`, `/`, etc.             |
| Aggregation        | `sum()`, `mean()`, `max()`, etc.     |
| Descriptive stats  | `describe()`                         |
| Row/Column Ops     | `axis=0` (cols), `axis=1` (rows)     |
| Custom functions   | `apply()`, `map()`, `applymap()`     |

---

## **Handling Missing Data in Pandas**

Real-world data is often incomplete or contains missing values. Pandas provides several tools to detect, handle, and clean missing data.

---

### **1. What Represents Missing Data in Pandas?**

- **`NaN`**: Not a Number (used to represent missing numerical data)
- **`None`**: Used for missing object data (strings, lists, etc.)

---

### **2. Detecting Missing Data**

#### **a. `isnull()`**

Returns a DataFrame of the same shape indicating where values are null (`True`) or not (`False`):

```python
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, None]
})

print(data.isnull())
```

#### **b. `notnull()`**

Returns the opposite (non-missing values):

```python
print(data.notnull())
```

---

### **3. Counting Missing Values**

```python
print(data.isnull().sum())  # Count missing values column-wise
```

---

### **4. Dropping Missing Data**

#### **a. `dropna()`**

- Drops **rows** with any missing value by default:

```python
print(data.dropna())
```

- Drop columns with missing values:

```python
print(data.dropna(axis=1))
```

- Drop only if **all values** are missing:

```python
print(data.dropna(how='all'))
```

- Drop rows with less than a threshold of non-NA values:

```python
print(data.dropna(thresh=2))  # Keep rows with at least 2 non-null values
```

---

### **5. Filling Missing Data**

#### **a. `fillna()`**

- Fill with a constant value:

```python
print(data.fillna(0))
```

- Fill using forward fill (`ffill`) or backward fill (`bfill`):

```python
print(data.fillna(method='ffill'))  # Forward fill
print(data.fillna(method='bfill'))  # Backward fill
```

- Fill using column mean or median:

```python
print(data.fillna(data.mean()))
```

#### **b. Limit parameter**

Limit number of values to fill:

```python
data.fillna(method='ffill', limit=1)
```

---

### **6. Interpolation**

Fills missing values by interpolating between existing data points:

```python
data.interpolate()
```

---

### **7. Replacing Specific Values with NaN**

```python
data.replace("?", np.nan)
```

---

### **8. Checking if DataFrame has any missing values**

```python
print(data.isnull().values.any())  # True if any missing value exists
```

---

### Summary Table

| Task                          | Method                          |
|-------------------------------|----------------------------------|
| Detect missing values         | `isnull()`, `notnull()`         |
| Count missing values          | `isnull().sum()`                |
| Drop rows/columns             | `dropna()`                      |
| Fill missing values           | `fillna()`                      |
| Interpolation                 | `interpolate()`                 |
| Replace with NaN              | `replace()`                     |

---

## **Hierarchical Indexing in Pandas**

Hierarchical indexing (also known as **multi-level indexing**) allows you to have **multiple index levels** (rows and/or columns). This is very useful for working with higher-dimensional data in a 2D DataFrame.

---

### **1. Creating a MultiIndex Series**

```python
import pandas as pd

# Creating a multi-level index using tuples
index = [('A', 2020), ('A', 2021), ('B', 2020), ('B', 2021)]
multi_index = pd.MultiIndex.from_tuples(index)

data = pd.Series([100, 200, 150, 250], index=multi_index)
print(data)
```

#### Output:
```
A  2020    100
   2021    200
B  2020    150
   2021    250
dtype: int64
```

---

### **2. Accessing Data in MultiIndex Series**

```python
print(data['A'])        # All entries under label 'A'
print(data['A'][2021])  # Specific entry: 'A' in 2021
```

---

### **3. Creating MultiIndex DataFrame**

```python
import numpy as np

arrays = [
    ['A', 'A', 'B', 'B'],
    [2020, 2021, 2020, 2021]
]

multi_index = pd.MultiIndex.from_arrays(arrays, names=('Company', 'Year'))

df = pd.DataFrame(np.random.randn(4, 2), index=multi_index, columns=['Revenue', 'Profit'])
print(df)
```

---

### **4. Accessing Rows with `.loc[]` and `.xs()`**

#### a. Using `loc[]` for label-based access:

```python
print(df.loc['A'])            # All data for company 'A'
print(df.loc['A', 2021])      # Data for company 'A' in 2021
```

#### b. Using `xs()` (cross-section):

```python
# Get data for a specific year across all companies
print(df.xs(2020, level='Year'))
```

---

### **5. Swapping and Sorting Index Levels**

#### a. Swap index levels:

```python
df_swapped = df.swaplevel()
print(df_swapped)
```

#### b. Sort by index:

```python
print(df.sort_index())
print(df.sort_index(level='Year'))  # Sort by year
```

---

### **6. Stacking and Unstacking**

#### a. `stack()` converts columns into inner row indices:

```python
stacked = df.stack()
print(stacked)
```

#### b. `unstack()` does the reverse:

```python
unstacked = stacked.unstack()
print(unstacked)
```

---

### **7. Resetting and Setting Index**

#### a. Convert index to columns:

```python
print(df.reset_index())
```

#### b. Set new multi-level index:

```python
df2 = df.reset_index().set_index(['Year', 'Company'])
print(df2)
```

---

### **8. Aggregating with GroupBy on MultiIndex**

You can group and aggregate based on any index level:

```python
print(df.groupby(level='Company').mean())
```

---

### Summary

| Task                      | Function / Method     |
|---------------------------|------------------------|
| Create MultiIndex         | `pd.MultiIndex`        |
| Access elements           | `.loc[]`, `.xs()`      |
| Rearrange levels          | `swaplevel()`          |
| Sort index levels         | `sort_index()`         |
| Convert levels to columns | `reset_index()`        |
| Convert columns to levels | `set_index()`          |
| Transform structure       | `stack()`, `unstack()` |
| Aggregate by levels       | `groupby(level=...)`   |

---

## **Combining Data Sets in Pandas**

Combining data sets is essential when working with real-world data. Pandas provides several powerful functions to **merge**, **join**, **concatenate**, and **combine** data.

---

### **1. Concatenation with `pd.concat()`**

- Stacks DataFrames vertically or horizontally
- Think of it like adding new rows or columns

#### **a. Vertical (Row-wise)**

```python
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

result = pd.concat([df1, df2])
print(result)
```

#### **b. Horizontal (Column-wise)**

```python
result = pd.concat([df1, df2], axis=1)
print(result)
```

---

### **2. Merging with `pd.merge()`**

- Similar to SQL joins
- Matches rows based on key columns

```python
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [25, 30, 22]})

merged = pd.merge(left, right, on='ID')
print(merged)
```

#### Types of Joins:
| Merge Type | How to specify       | Behavior                          |
|------------|-----------------------|-----------------------------------|
| Inner      | `how='inner'`         | Only matching keys from both      |
| Outer      | `how='outer'`         | All keys from both tables         |
| Left       | `how='left'`          | All keys from left, match right   |
| Right      | `how='right'`         | All keys from right, match left   |

```python
merged_outer = pd.merge(left, right, on='ID', how='outer')
```

---

### **3. Joining with `.join()`**

- Simplified merge on index
- Good for combining columns by row index

```python
df1 = pd.DataFrame({'A': ['A0', 'A1']}, index=[0, 1])
df2 = pd.DataFrame({'B': ['B0', 'B1']}, index=[0, 1])

result = df1.join(df2)
print(result)
```

---

### **4. Appending Rows with `.append()`** *(Deprecated in newer versions)*

```python
df1 = pd.DataFrame({'A': ['A0', 'A1']})
df2 = pd.DataFrame({'A': ['A2', 'A3']})

result = df1.append(df2)
print(result)
```

Use `pd.concat()` instead of `append()` now.

---

### **5. Combining with `combine_first()`**

- Fill missing data from another DataFrame

```python
df1 = pd.DataFrame({'A': [1, None], 'B': [None, 4]})
df2 = pd.DataFrame({'A': [3, 4], 'B': [5, 6]})

result = df1.combine_first(df2)
print(result)
```

---

### Summary of Methods:

| Task                          | Function            |
|-------------------------------|---------------------|
| Stack data vertically/horizontally | `pd.concat()`      |
| Combine like SQL joins        | `pd.merge()`         |
| Combine on index              | `df.join()`          |
| Fill missing values           | `combine_first()`    |
| Append data (older method)    | `df.append()`        |

---

# Unit -III  
### FUNCTIONS, EXCEPTION, AND FILES  
- Functions: Types, parameters, arguments: positional arguments, keyword arguments, parameters with default values, functions with arbitrary arguments, Scope of variables: Local and global scope, Recursion and Lambda functions. Function Decorators, Generators  
- Structured Programming, Exceptions, Exception Handling, Types of Exceptions, The Except Block, the assert Statement, UserDefined Exceptions, Logging the Exceptions  
- Files: Files, Types of Files in Python, Opening a File, Closing a File, Working with Text Files Containing Strings, Knowing Whether a File Exists or Not, Working with Binary Files, The with Statement, Pickle in Python, The seek() and tell() Methods  

---

### **1. Functions in Python**

#### **What is a Function?**
A function is a block of organized, reusable code used to perform a single, related action. Functions help break our program into smaller and modular chunks, improving readability, reducing redundancy, and making testing easier.

---

### **Types of Functions**

1. **Built-in Functions**
   - Predefined in Python (e.g., `print()`, `len()`, `type()`, `sum()`, etc.)

2. **User-defined Functions**
   - Functions that you create using the `def` keyword.

---

### **Creating a User-Defined Function**

```python
def greet():
    print("Hello, world!")
```

**Calling the function:**

```python
greet()  # Output: Hello, world!
```

---

### **Parameters vs Arguments**

- **Parameter** is the variable listed inside the parentheses in the function definition.
- **Argument** is the value sent to the function when it is called.

```python
def greet(name):  # 'name' is a parameter
    print("Hello", name)

greet("Alice")  # 'Alice' is an argument
```

---

### **Types of Arguments**

1. **Positional Arguments**

   Arguments passed in the correct position order.

   ```python
   def add(a, b):
       return a + b

   print(add(2, 3))  # Output: 5
   ```

2. **Keyword Arguments**

   Arguments passed with parameter names.

   ```python
   def student(name, age):
       print(f"Name: {name}, Age: {age}")

   student(age=20, name="John")
   ```

3. **Default Arguments**

   Provide a default value if one is not given.

   ```python
   def greet(name="Guest"):
       print("Hello", name)

   greet()           # Output: Hello Guest
   greet("Alice")    # Output: Hello Alice
   ```

4. **Arbitrary Arguments (using `*args`)**

   Used when you don’t know how many arguments will be passed.

   ```python
   def add_all(*nums):
       total = sum(nums)
       print("Sum:", total)

   add_all(1, 2, 3, 4)  # Output: Sum: 10
   ```

5. **Arbitrary Keyword Arguments (using `**kwargs`)**

   Used when you want to accept any number of keyword arguments.

   ```python
   def student_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   student_info(name="Alice", age=21, course="Python")
   ```

---

### **2. Scope of Variables: Local and Global Scope**

In Python, **scope** refers to the region of a program where a variable is recognized and accessible. Python uses **LEGB Rule** to resolve names:

- **L**: Local — Inside the current function
- **E**: Enclosing — Inside enclosing functions (nested functions)
- **G**: Global — At the top-level of the script/module
- **B**: Built-in — Names preassigned in Python (e.g., `len`, `range`)

---

### **Local Variables**
- Declared inside a function.
- Only accessible within that function.

```python
def my_func():
    x = 10  # Local variable
    print(x)

my_func()
# print(x)  # Error: x is not defined outside the function
```

---

### **Global Variables**
- Declared outside any function.
- Accessible from anywhere in the file unless shadowed by a local variable.

```python
x = 5  # Global variable

def my_func():
    print(x)  # Accessing global variable

my_func()  # Output: 5
```

---

### **Modifying Global Variable Inside a Function**
To modify a global variable inside a function, use the `global` keyword:

```python
x = 5

def modify():
    global x
    x = 10

modify()
print(x)  # Output: 10
```

---

### **Enclosing Scope (Nonlocal Keyword)**
In nested functions, variables from the outer function can be accessed using `nonlocal`.

```python
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
# Output:
# Inner: inner
# Outer: inner
```

---

### Summary Table:

| Scope       | Declared In             | Accessible In                            |
|-------------|-------------------------|------------------------------------------|
| Local       | Inside a function       | That function only                       |
| Enclosing   | Inside outer function   | Inner functions (with `nonlocal`)        |
| Global      | Outside all functions   | Entire script/module (use `global`)      |
| Built-in    | Python pre-defined      | Everywhere                               |

---

### **3. Recursion and Lambda Functions**

---

## **Recursion in Python**

**Recursion** is a programming technique where a function calls itself to solve smaller instances of the same problem.

---

### **Structure of a Recursive Function:**
Every recursive function must have:
1. **Base Case** – the condition that stops recursion.
2. **Recursive Case** – the function calls itself.

---

### **Example: Factorial Using Recursion**

```python
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
```

---

### **How it works (factorial(5)):**
```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 5 * 4 * 3 * 2 * 1 * 1 => 120
```

---

### **Use Cases of Recursion:**
- Tree Traversals
- Factorial, Fibonacci, Tower of Hanoi
- Backtracking (e.g., maze solving)

---

## **Lambda Functions**

**Lambda functions** are anonymous, one-line functions using the `lambda` keyword.

### **Syntax:**

```python
lambda arguments: expression
```

---

### **Example:**

```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

---

### **Multiple Arguments:**

```python
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

---

### **Usage in Functions like `map()`, `filter()` and `sorted()`:**

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)  # Output: [1, 4, 9, 16]
```

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]
```

---

### **Key Differences: `def` vs `lambda`:**

| Feature      | `def` Function        | `lambda` Function       |
|--------------|------------------------|--------------------------|
| Name         | Requires a name        | Anonymous (no name)      |
| Body         | Can have multiple lines| Only one expression      |
| Usage        | General-purpose        | Simple operations        |

---

### **4. Function Decorators and Generators**

---

## **Function Decorators in Python**

A **decorator** is a function that **modifies the behavior** of another function without permanently changing it. Decorators are commonly used for logging, authentication, performance testing, and caching.

---

### **Basic Syntax:**

```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()
    return wrapper_function
```

---

### **Using the Decorator:**

```python
@decorator_function
def display():
    print("Display function called")

display()
```

**Output:**
```
Wrapper executed before display
Display function called
```

---

### **Decorators with Arguments:**

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

## **Chaining Decorators**

Multiple decorators can be applied:

```python
@decorator1
@decorator2
def my_func():
    pass
```

---

## **Built-in Decorators:**

- `@staticmethod` – defines a static method.
- `@classmethod` – defines a class method.
- `@property` – converts method into a read-only property.

---

## **Generators in Python**

Generators are **iterators** that yield items one at a time using the `yield` keyword. They are **memory efficient** and useful for large datasets.

---

### **Difference from Normal Functions:**

| Feature        | Function              | Generator Function         |
|----------------|------------------------|-----------------------------|
| Uses           | `return`               | `yield`                     |
| Execution      | Runs once              | Pauses and resumes          |
| Output         | Returns a value        | Returns a generator object  |

---

### **Basic Example:**

```python
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))  # Output: 1
print(next(g))  # Output: 2
```

---

### **Looping through Generators:**

```python
for value in my_gen():
    print(value)
```

---

### **Use Case: Fibonacci Sequence**

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
```

**Output:**
```
0
1
1
2
3
```

---

### **5. Structured Programming, Exceptions, and Exception Handling**

---

## **Structured Programming in Python**

Structured programming is a programming paradigm that emphasizes:
- **Modularity** (functions, procedures)
- **Sequence** (one step after another)
- **Decision-making** (if-else, loops)
- **Clarity and maintainability**

Python supports structured programming using:
- Functions (with local/global scope)
- Loops (`for`, `while`)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try`, `except`)

---

## **Exception Handling in Python**

Exceptions are **errors** that occur during program execution and disrupt the normal flow of the program. Exception handling allows you to catch these errors and take corrective action.

---

### **Why Handle Exceptions?**

- To **avoid crashing** the program
- To provide **informative error messages**
- To allow **clean exit or recovery**

---

## **Common Exceptions in Python**

| Exception          | Description                           |
|--------------------|---------------------------------------|
| `ZeroDivisionError` | Dividing by zero                     |
| `TypeError`        | Mismatched data types                 |
| `ValueError`       | Invalid value                         |
| `FileNotFoundError`| File does not exist                   |
| `IndexError`       | Accessing invalid list index          |
| `KeyError`         | Accessing invalid dictionary key      |

---

## **Basic Syntax of Exception Handling**

```python
try:
    # risky code
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print("Result:", result)
finally:
    print("This block always runs")
```

---

### **Blocks Used in Exception Handling:**

- `try`: Code that might throw an exception.
- `except`: Handles the exception.
- `else`: Runs if no exception occurs.
- `finally`: Always runs, used for cleanup.

---

## **The `assert` Statement**

Used to **check for conditions** that must be true. It’s mainly used for debugging.

```python
x = 10
assert x > 0   # Passes
assert x < 5   # Raises AssertionError
```

---

## **User-Defined Exceptions**

You can define your own exception by inheriting from the `Exception` class.

```python
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong!")
except MyError as e:
    print(e)
```

---

## **Logging Exceptions**

Instead of just printing errors, you can log them using Python’s built-in `logging` module.

```python
import logging

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)
```

Logging can be configured to write to a file, include timestamps, error levels, etc.

---

### **6. Files in Python**

---

File handling in Python allows us to store output to a file and read from a file when required. It is an essential feature for data persistence.

---

## **Types of Files in Python**

Python works with two types of files:

1. **Text Files**: Contains readable characters (like `.txt`, `.py`)
2. **Binary Files**: Contains binary data (like images, PDFs, compiled files)

---

## **Opening a File**

To work with a file, you must first open it using the `open()` function:

```python
file_object = open("filename", "mode")
```

### **Modes Available:**

| Mode | Description                          |
|------|--------------------------------------|
| `r`  | Read (default), file must exist      |
| `w`  | Write, creates a new file or overwrites |
| `a`  | Append, adds to existing file        |
| `rb` | Read binary                          |
| `wb` | Write binary                         |
| `r+` | Read and write                       |
| `w+` | Write and read (overwrites file)     |

---

## **Reading from a File**

```python
f = open("sample.txt", "r")
print(f.read())         # Read entire file
print(f.readline())     # Read one line
print(f.readlines())    # Read all lines into list
f.close()
```

---

## **Writing to a File**

```python
f = open("sample.txt", "w")
f.write("Hello, world!")
f.close()
```

Use `a` mode to append instead of overwriting.

---

## **Closing a File**

Always close files after use with `.close()`:

```python
f.close()
```

Or use a **`with` statement**, which automatically handles closing:

```python
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## **Check if a File Exists**

```python
import os

if os.path.exists("sample.txt"):
    print("File exists!")
else:
    print("File does not exist.")
```

---

## **Working with Binary Files**

```python
with open("image.png", "rb") as binary_file:
    data = binary_file.read()
```

---

## **The `with` Statement**

- Simplifies file handling
- Ensures files are properly closed even if an error occurs

```python
with open("data.txt", "w") as f:
    f.write("Using with statement")
```

---

## **Pickle in Python**

`pickle` is a module to **serialize and deserialize** Python objects (convert to/from byte stream):

```python
import pickle

# Saving an object
data = {'a': 1, 'b': 2}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Loading an object
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)
```

---

## **The `seek()` and `tell()` Methods**

- `tell()`: Returns current file position
- `seek(offset, from_what)`: Moves file pointer to desired location

```python
f = open("sample.txt", "r")
print(f.tell())     # Current position
f.seek(5)           # Move to 5th byte
print(f.read())     # Read from there
f.close()
```

---

# Unit -IV  
### OOPS and VISUALIZATION   
- Object-oriented Programming in Python: Classes, Objects, Instances, Abstract Data Types and classes, Inheritance, Encapsulation and Information hiding, Polymorphism  
- Basic functions of matplotlib-Simple Line Plot, Scatter Plot-Density and Contour Plots- Histograms, Binning and Density-Customizing Plot Legends, Colour Bars-Three- Dimensional Plotting in Matplotlib  
- Multithreaded Programming: Introduction, Threads and Processes, Python Threads, and the Global Interpreter Lock, Thread Module, Threading Module, Related Modules  

---

### **Object-Oriented Programming (OOP) in Python**

#### **1. Classes and Objects**

**What is OOP?**  
Object-Oriented Programming is a paradigm that uses “objects” and “classes” to design applications. Objects are instances of classes that bundle both data (attributes) and methods (functions).

##### **Class:**
A **class** is a blueprint for creating objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

- `__init__` is a special method (constructor) automatically called when a new object is created.
- `self` represents the instance itself (like `this` in other languages).

##### **Object:**
An **object** is an instance of a class.

```python
s1 = Student("John", 21)
s1.display()
```

#### **2. Instances**
Instances are specific realizations of a class. Each object can have different values for its attributes.

```python
s2 = Student("Alice", 22)
s2.display()
```

Here, `s2` is an instance of `Student`, and it holds its own copy of `name` and `age`.

---

### **Object-Oriented Programming (OOP) in Python**

#### **1. Classes and Objects**

**What is OOP?**  
Object-Oriented Programming is a paradigm that uses “objects” and “classes” to design applications. Objects are instances of classes that bundle both data (attributes) and methods (functions).

##### **Class:**
A **class** is a blueprint for creating objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

- `__init__` is a special method (constructor) automatically called when a new object is created.
- `self` represents the instance itself (like `this` in other languages).

##### **Object:**
An **object** is an instance of a class.

```python
s1 = Student("John", 21)
s1.display()
```

#### **2. Instances**
Instances are specific realizations of a class. Each object can have different values for its attributes.

```python
s2 = Student("Alice", 22)
s2.display()
```

Here, `s2` is an instance of `Student`, and it holds its own copy of `name` and `age`.

---

### **Inheritance in Python**

#### **1. What is Inheritance?**

Inheritance is an **Object-Oriented Programming (OOP)** feature that allows one class (child or subclass) to **inherit properties and behaviors (methods and attributes)** from another class (parent or superclass).

This promotes **code reusability** and supports the **"is-a" relationship** between classes.

---

#### **2. Syntax of Inheritance in Python**

```python
class Parent:
    def display(self):
        print("I am the Parent class.")

class Child(Parent):
    def show(self):
        print("I am the Child class.")
```

**Usage:**
```python
c = Child()
c.display()  # Inherited method
c.show()     # Child's own method
```

---

#### **3. Types of Inheritance in Python**

1. **Single Inheritance**  
   One child inherits from one parent class.

2. **Multiple Inheritance**  
   One child inherits from **more than one** parent.

   ```python
   class A:
       def method_a(self):
           print("A")

   class B:
       def method_b(self):
           print("B")

   class C(A, B):
       pass
   ```

3. **Multilevel Inheritance**  
   A class inherits from a child class which is already derived from another class.

   ```python
   class A:
       def a(self):
           print("A")

   class B(A):
       def b(self):
           print("B")

   class C(B):
       def c(self):
           print("C")
   ```

4. **Hierarchical Inheritance**  
   Multiple classes inherit from a single base class.

5. **Hybrid Inheritance**  
   Combination of more than one type of inheritance.

---

#### **4. The `super()` Function**

Used to call **parent class methods** from child class.

```python
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()   # Calls Parent __init__()
        print("Child init")
```

---

#### **5. Method Overriding**

A child class can **redefine** methods of the parent class.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
```

---

### **Encapsulation and Information Hiding in Python**

---

#### **1. What is Encapsulation?**

**Encapsulation** is the process of **binding data (attributes) and methods** that operate on that data into a **single unit** called a class. It helps to **restrict direct access** to some of an object's components, which is called **information hiding**.

---

#### **2. Why Encapsulation is Important?**

- Controls how the data is accessed or modified.
- Prevents accidental changes.
- Helps in securing sensitive data.
- Enables modularity and maintainability.

---

#### **3. Access Modifiers in Python**

Python doesn't have traditional access modifiers like `public`, `private`, and `protected`. Instead, it follows **naming conventions**:

| Access Level     | Syntax Example         | Meaning                                    |
|------------------|------------------------|--------------------------------------------|
| Public           | `self.name`            | Accessible from anywhere                   |
| Protected        | `self._name`           | Intended to be accessed only within class and subclasses |
| Private          | `self.__name`          | Name mangling occurs: `_ClassName__name`   |

---

#### **4. Example of Encapsulation and Information Hiding**

```python
class Student:
    def __init__(self, name, age):
        self.name = name          # Public
        self._age = age           # Protected
        self.__grade = "A"        # Private

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade in ["A", "B", "C", "D"]:
            self.__grade = grade
        else:
            print("Invalid grade")

s = Student("Alex", 20)
print(s.name)            # Works
print(s._age)            # Works, but discouraged
# print(s.__grade)       # Error
print(s.get_grade())     # Works
```

---

#### **5. Name Mangling for Private Variables**

Python internally changes the name of the private attribute to `_ClassName__attribute`.

```python
print(s._Student__grade)  # Works, but not recommended
```

---

#### **6. Summary of Encapsulation and Hiding**

- Public (`name`): accessible everywhere.
- Protected (`_name`): accessible in class and subclasses.
- Private (`__name`): not accessible directly from outside.
- Use **getter and setter** methods to access or modify private data.

---

### **Polymorphism in Python**

---

#### **1. What is Polymorphism?**

**Polymorphism** means **"many forms"**. It allows objects of **different classes** to be treated as **objects of a common super class**. It is primarily used with **inheritance**.

---

#### **2. Why Polymorphism is Useful?**

- Allows code reusability.
- Simplifies code structure.
- Enables functions to use objects of different types interchangeably.

---

#### **3. Types of Polymorphism**

1. **Compile-Time Polymorphism (Overloading)** – Not strictly supported in Python.
2. **Run-Time Polymorphism (Overriding)** – Fully supported via inheritance.

---

#### **4. Method Overriding (Runtime Polymorphism)**

A subclass provides a specific implementation of a method that is already defined in its superclass.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Using polymorphism
def make_animal_speak(animal):
    animal.speak()

a = Animal()
d = Dog()
c = Cat()

make_animal_speak(a)   # Animal speaks
make_animal_speak(d)   # Dog barks
make_animal_speak(c)   # Cat meows
```

---

#### **5. Duck Typing (Pythonic Polymorphism)**

“If it looks like a duck and quacks like a duck, it’s a duck.”

Python focuses on **behavior, not inheritance**.

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(flying_object):
    flying_object.fly()

b = Bird()
a = Airplane()

let_it_fly(b)
let_it_fly(a)
```

---

#### **6. Operator Overloading (Special Methods)**

Operators like `+`, `*`, etc., can behave differently depending on the operands.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)  # Output: 4 6
```

---

#### **7. Summary of Polymorphism in Python**

| Type                   | Description                              |
|------------------------|------------------------------------------|
| Method Overriding      | Subclass redefines a method              |
| Duck Typing            | Focuses on method availability           |
| Operator Overloading   | Redefining built-in operator behavior    |

---

### **Basic Functions of Matplotlib**

---

#### **1. What is Matplotlib?**

**Matplotlib** is a widely-used Python library for **creating static, animated, and interactive plots**. It provides a MATLAB-like interface for plotting and visualization.

---

#### **2. Installing Matplotlib**

```bash
pip install matplotlib
```

---

#### **3. Importing Matplotlib**

```python
import matplotlib.pyplot as plt
```

The `pyplot` module provides a collection of functions that make **Matplotlib work like MATLAB**.

---

#### **4. Basic Plotting**

Let’s create a **simple line plot**:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

---

#### **5. Common Functions in Matplotlib**

| Function                | Description                            |
|------------------------|----------------------------------------|
| `plt.plot()`           | Plot lines or markers                  |
| `plt.title()`          | Add title to the plot                  |
| `plt.xlabel()`         | Label for x-axis                       |
| `plt.ylabel()`         | Label for y-axis                       |
| `plt.legend()`         | Show legend                            |
| `plt.grid()`           | Display grid lines                     |
| `plt.savefig()`        | Save the figure to a file              |
| `plt.show()`           | Display the plot                       |

---

#### **6. Customizing a Line Plot**

```python
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, color='green', marker='o', linestyle='--')
plt.title('Customized Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
```

**Styling Options:**

- `color`: Line color (`'red'`, `'blue'`, `'green'`)
- `marker`: Data point symbol (`'o'`, `'^'`, `'s'`)
- `linestyle`: `'-'`, `'--'`, `':'`, `'-.'`

---

#### **7. Multiple Lines on Same Plot**

```python
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 5, 10, 17]

plt.plot(x, y1, label='y1', color='blue')
plt.plot(x, y2, label='y2', color='red')
plt.title('Multiple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Values')
plt.legend()
plt.show()
```

---

### **Scatter Plot in Matplotlib**

---

#### **1. What is a Scatter Plot?**

A **scatter plot** shows **individual data points** on a two-dimensional axis. It's useful to **visualize the relationship** (correlation) between two numerical variables.

---

#### **2. Creating a Simple Scatter Plot**

```python
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y)
plt.title('Simple Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
```

---

#### **3. Customizing Scatter Plots**

```python
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
colors = ['red', 'blue', 'green', 'purple', 'orange']
sizes = [20, 40, 60, 80, 100]

plt.scatter(x, y, color=colors, s=sizes, alpha=0.7, edgecolors='black')
plt.title('Customized Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
```

**Customization options:**

| Parameter     | Description                             |
|---------------|-----------------------------------------|
| `color`       | Set color of each point                 |
| `s`           | Size of each marker                     |
| `alpha`       | Transparency (0.0 to 1.0)               |
| `edgecolors`  | Color of marker border                  |

---

#### **4. Use Case Example: Height vs Weight**

```python
height = [150, 160, 170, 180, 190]
weight = [50, 60, 70, 80, 90]

plt.scatter(height, weight, color='teal')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```

---

### **Density and Contour Plots**

---

#### **1. What is a Density Plot?**

A **density plot** visualizes the distribution of data across a continuous interval. It’s typically a **smoothed version of a histogram**.

- In 2D, it shows the concentration of data points.
- Helps identify regions with higher or lower point density.

---

#### **2. What is a Contour Plot?**

A **contour plot** is used to represent **three-dimensional data** in two dimensions using **contour lines**.

- Contour lines connect points of equal value.
- Useful for visualizing functions of two variables.

---

### **Creating a Contour Plot in Matplotlib**

#### **Example: Contour plot of a mathematical function**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate grid of x and y values
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

# Define the function
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create contour plot
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.title('Contour Plot of f(x, y) = sin(sqrt(x^2 + y^2))')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.colorbar(label='Function Value')
plt.show()
```

---

### **Filled Contour Plot (contourf)**

```python
plt.contourf(X, Y, Z, levels=20, cmap='plasma')
plt.colorbar()
plt.title('Filled Contour Plot')
plt.show()
```

---

### **Why Use Contour Plots?**

- Visualize **topographical maps**
- Analyze **mathematical functions**
- Represent **heatmaps** with clear separation of regions

---

### **Real-Life Use Case**

Imagine you want to model **temperature** across a landscape. Each `(x, y)` represents a location, and `Z` is temperature. A contour plot lets you **see hot and cold regions clearly**.

---

### **Histograms, Binning, and Density in Matplotlib**

---

#### **1. What is a Histogram?**

A **histogram** is a graphical representation of the **distribution of numerical data**. It groups values into **bins** and shows how many values fall into each bin.

---

### **Creating a Histogram in Matplotlib**

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.randn(1000)  # 1000 random values from a normal distribution

# Create histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

---

#### **2. What is Binning?**

- **Binning** means grouping data into intervals (bins).
- The number of bins determines the resolution of the histogram:
  - **Fewer bins**: smoother, but less detailed.
  - **More bins**: more detailed, but possibly noisy.

Example:
```python
plt.hist(data, bins=10)  # wider bins
plt.hist(data, bins=50)  # narrower bins
```

---

#### **3. Density Plot (Smooth Histogram)**

A **density plot** estimates the **probability distribution** of a dataset.

- Instead of showing raw counts like a histogram, it shows **density**.
- In `plt.hist`, use `density=True`.

```python
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
```

---

#### **4. Adding a KDE (Kernel Density Estimate)**

Using `seaborn`:

```python
import seaborn as sns

sns.histplot(data, bins=30, kde=True, color='purple')
```

- `kde=True` overlays a smooth curve on the histogram.

---

### **Comparison: Histogram vs. Density Plot**

| Feature       | Histogram         | Density Plot         |
|---------------|-------------------|-----------------------|
| Shows         | Count per bin     | Probability density   |
| Appearance    | Stepped bars      | Smooth curve          |
| Binning       | Required           | Not required          |

---

### **When to Use What?**

- Use **histograms** to see **raw data distribution**.
- Use **density plots** for **smoothed trends**.
- Use **both together** for deeper insights.

---

### **Customizing Plot Legends and Colorbars in Matplotlib**

---

## **1. Plot Legends in Matplotlib**

Legends help identify different plots when you have multiple lines, points, or categories in one figure.

---

### **Adding a Basic Legend**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label='Squared')     # Label for legend
plt.plot(x, y2, label='Linear')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Basic Legend Example')
plt.legend()                         # Displays the legend
plt.show()
```

---

### **Legend Location**

```python
plt.legend(loc='upper left')
```

Common locations:
- `'upper left'`, `'upper right'`, `'lower left'`, `'lower right'`
- `'center'`, `'center left'`, `'center right'`, `'best'` (auto-position)

---

### **Customizing Legend Appearance**

```python
plt.legend(
    loc='best',
    fontsize='large',
    frameon=True,         # Show legend border
    shadow=True,          # Shadow under legend box
    title='Legend Title'  # Add title
)
```

---

## **2. Colorbars in Matplotlib**

**Colorbars** are used in plots where color indicates a value (like heatmaps, contour plots, or scatter plots with gradient color).

---

### **Example with Colorbar:**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar(label='Color Intensity')  # Adds colorbar
plt.title('Colorbar Example')
plt.show()
```

---

### **Customizing the Colorbar**

```python
cb = plt.colorbar()
cb.set_label('Density Level')
cb.ax.tick_params(labelsize=10)
```

---

### **Colormap Options**

You can change how colors are displayed using colormaps:
```python
plt.scatter(x, y, c=colors, cmap='plasma')  # Try: viridis, coolwarm, jet, magma, inferno
```

View all available colormaps:  
[https://matplotlib.org/stable/users/explain/colors/colormaps.html](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

---

## **Summary**

| Feature   | `plt.legend()`             | `plt.colorbar()`                     |
|-----------|----------------------------|--------------------------------------|
| Purpose   | Labels for plots           | Visual scale for color representation |
| Location  | Can be moved or styled     | Auto-added to color-based plots      |
| Custom    | Yes: font, border, title   | Yes: label, ticks, format            |

---

### **Three-Dimensional Plotting in Matplotlib**

---

Matplotlib supports 3D plotting through the `mpl_toolkits.mplot3d` module.

---

## **1. Setting Up a 3D Plot**

To create a 3D plot, you must:

```python
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 3D subplot
```

---

## **2. 3D Line Plot**

```python
z = np.linspace(0, 10, 100)
x = np.sin(z)
y = np.cos(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.title('3D Line Plot')
plt.show()
```

---

## **3. 3D Scatter Plot**

```python
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')

plt.title("3D Scatter Plot")
plt.show()
```

---

## **4. 3D Surface Plot**

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

plt.title("3D Surface Plot")
plt.show()
```

---

## **5. Customizing 3D Plots**

- **Color Maps:** `cmap='plasma'`, `cmap='coolwarm'`, etc.
- **Wireframes:**  
```python
ax.plot_wireframe(x, y, z, color='black')
```
- **Transparency:** `alpha=0.5`
- **Lines & Dots:** Customize markers, colors, and line styles.

---

## **6. Rotating the View**

```python
ax.view_init(elev=30, azim=45)  # elevation and azimuth angle
```

---

## **Use Cases of 3D Plotting**

- Scientific visualization
- Geospatial data representation
- Machine learning decision surfaces
- Mathematical functions

---

### **Multithreaded Programming in Python**

---

Multithreading is a way to **run multiple tasks (threads) concurrently** in a single process, improving performance in I/O-bound operations.

---

## **1. Threads vs Processes**

- **Thread**: Light-weight, shares memory space with the parent process.
- **Process**: Heavy-weight, has its own memory space.
- Threads are used when tasks share data and resources.

---

## **2. Python Threads and the GIL**

### **What is GIL?**

- **Global Interpreter Lock (GIL)** is a mutex that allows **only one thread to execute at a time** in CPython interpreter.
- It means true parallelism in CPU-bound threads is limited.
- However, **I/O-bound tasks** benefit greatly from multithreading.

---

## **3. Using the `thread` Module (deprecated)**

This is a low-level module and is **deprecated** in favor of `threading`.

```python
import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName}: {time.ctime(time.time())}")

# Start threads
_thread.start_new_thread(print_time, ("Thread-1", 2))
_thread.start_new_thread(print_time, ("Thread-2", 4))
```

---

## **4. Using the `threading` Module**

This is the **recommended** module for multithreading.

```python
import threading
import time

def worker(name):
    for i in range(3):
        print(f"{name} is working")
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed!")
```

---

## **5. Daemon Threads**

Daemon threads run in the background and **automatically terminate** when the main program exits.

```python
t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
```

---

## **6. Related Modules**

### **a. `queue` Module** (for thread-safe communication):

```python
from queue import Queue
import threading

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while not q.empty():
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

q = Queue()
threading.Thread(target=producer, args=(q,)).start()
threading.Thread(target=consumer, args=(q,)).start()
```

### **b. `concurrent.futures`** (High-level threading)

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4])
    for result in results:
        print(result)
```

---

## **Use Cases of Multithreading**

- Downloading multiple files
- Handling multiple socket connections
- Logging & background tasks
- Real-time data processing

---

