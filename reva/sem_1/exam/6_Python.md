# Python
# **Unit 3: Functions, Exceptions, and Files**
# **Functions in Python**  

Functions in Python allow code reuse, modularity, and better organization. They help break down complex tasks into manageable parts.

---

## **📌 1. Defining and Calling Functions**  
A function is defined using the `def` keyword.  

### **🔹 Example: Simple Function**
```python
def greet():
    print("Hello, World!")

greet()  # Calling the function
```

---

## **📌 2. Types of Function Arguments**  

Python functions support four types of arguments:

### **🔹 (A) Positional Arguments**
Arguments are assigned based on position.
```python
def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15
```

### **🔹 (B) Keyword Arguments**
Arguments are passed with parameter names.
```python
def greet(name, msg):
    print(f"{msg}, {name}!")

greet(name="Alice", msg="Good Morning")  # Output: Good Morning, Alice!
```

### **🔹 (C) Default Arguments**
If no value is given, the default is used.
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9 (3^2)
print(power(3, 3))   # Output: 27 (3^3)
```

### **🔹 (D) Variable-Length Arguments**  
- `*args` – Accepts multiple positional arguments as a tuple.
- `**kwargs` – Accepts multiple keyword arguments as a dictionary.

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # Output: 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# Output:
# name: Alice
# age: 25
```

---

## **📌 3. Lambda Functions (Anonymous Functions)**  
Lambda functions are single-line functions without a `def` keyword.

### **🔹 Example:**
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

---

## **📌 4. `map()`, `filter()`, and `reduce()`**
These are higher-order functions that operate on iterables.

### **🔹 `map()`: Apply a function to each element**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

### **🔹 `filter()`: Filter elements based on a condition**
```python
numbers = [10, 15, 20, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [10, 20]
```

### **🔹 `reduce()`: Reduce a sequence into a single value**  
Requires `functools` module.
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1*2*3*4)
```

---

## **📌 5. Recursion in Python**  
A function calling itself.

### **🔹 Example: Factorial using Recursion**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### **🔥 Summary**
✔ **Positional, Keyword, Default & Variable-Length Arguments**  
✔ **Lambda Functions for One-Liners**  
✔ **Higher-Order Functions (`map`, `filter`, `reduce`)**  
✔ **Recursion for Solving Problems**  

---
# **Exception Handling in Python**  

Exception handling is a way to handle runtime errors to prevent program crashes.

---

## **📌 1. What are Exceptions?**  
Exceptions are errors that occur during execution. Common examples include:  

| Exception | Description |
|-----------|------------|
| `ZeroDivisionError` | Dividing by zero |
| `TypeError` | Invalid operation on data types |
| `ValueError` | Invalid input for a function |
| `IndexError` | Accessing an index out of range |
| `KeyError` | Accessing a missing dictionary key |

Example:  
```python
print(5 / 0)  # ZeroDivisionError
```

---

## **📌 2. Using `try` and `except`**  
To prevent program crashes, we use `try-except` blocks.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Enter a number.")
```

---

## **📌 3. Handling Multiple Exceptions**  
```python
try:
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
except (IndexError, KeyError) as e:
    print(f"Error: {e}")
```

---

## **📌 4. Using `else` and `finally`**  
- `else`: Runs if no exception occurs.  
- `finally`: Always executes, whether an exception occurs or not.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
```

---

## **📌 5. Raising Custom Exceptions (`raise`)**  
Use `raise` to trigger custom errors.

```python
def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older.")
    print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print(e)
```

---

## **📌 6. Exception Hierarchy in Python**  
All exceptions inherit from `BaseException` → `Exception`.  

| Exception Type | Description |
|---------------|------------|
| `Exception` | Base class for most exceptions |
| `ArithmeticError` | Errors in arithmetic operations |
| `LookupError` | Errors in index/key lookup |
| `OSError` | Operating system-related errors |

Example:
```python
try:
    raise ArithmeticError("Custom arithmetic error.")
except ArithmeticError as e:
    print(e)
```

---

## **📌 7. Logging & Debugging Exceptions**  
Instead of `print()`, use logging for better debugging.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    print(5 / 0)
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)
```

---

### **🔥 Summary**
✔ Use `try-except` for handling errors.  
✔ Use `else` when no errors occur.  
✔ Use `finally` for cleanup.  
✔ `raise` helps define custom exceptions.  
✔ Use `logging` for debugging.  

---
# **File Handling in Python**  

File handling allows reading, writing, and managing files efficiently.

---

## **📌 1. Types of Files in Python**
1. **Text Files**: Store human-readable data (`.txt`, `.csv`, `.log`).
2. **Binary Files**: Store data in binary format (`.jpg`, `.pdf`, `.dat`).

---

## **📌 2. Opening a File (`open()` function)**  
Syntax:  
```python
file = open("filename.txt", mode)
```
| Mode | Description |
|------|------------|
| `"r"` | Read mode (default) |
| `"w"` | Write mode (overwrites existing content) |
| `"a"` | Append mode (adds data at the end) |
| `"x"` | Create a new file (fails if file exists) |
| `"b"` | Binary mode (use with other modes, e.g., `"rb"`) |

Example:
```python
file = open("example.txt", "r")  # Opens file in read mode
file.close()  # Always close the file
```

---

## **📌 3. Reading from a File (`read()`, `readline()`, `readlines()`)**
```python
file = open("example.txt", "r")

print(file.read())      # Reads the entire file
print(file.readline())  # Reads one line
print(file.readlines()) # Reads all lines into a list

file.close()
```

---

## **📌 4. Writing to a File (`write()`)**
```python
file = open("example.txt", "w")  # Overwrites existing content
file.write("Hello, Python!\n")
file.write("File handling is easy.\n")
file.close()
```

To append data instead:
```python
file = open("example.txt", "a")  # Adds data at the end
file.write("Appending this line.\n")
file.close()
```

---

## **📌 5. Using `with` Statement (Best Practice)**
The `with` statement ensures files close automatically.
```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)  # File closes automatically
```

---

## **📌 6. Working with Binary Files**
Writing binary data:
```python
with open("image.jpg", "rb") as file:
    content = file.read()
```
Writing binary data:
```python
with open("output.jpg", "wb") as file:
    file.write(content)
```

---

## **📌 7. `seek()` and `tell()`**
- `tell()`: Gets the current position in the file.
- `seek(offset, whence)`: Moves the cursor.

```python
with open("example.txt", "r") as file:
    print(file.tell())   # Shows the current position
    file.seek(10)        # Moves cursor to the 10th byte
    print(file.read())   # Reads from the new position
```

---

## **📌 8. Pickle Module (Storing Objects)**
Python’s `pickle` module saves objects in a file.

```python
import pickle

data = {"name": "Alice", "age": 25}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  # Serializing

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)  # Deserializing
    print(loaded_data)
```

---

### **🔥 Summary**
✔ `open()` opens a file, `close()` closes it.  
✔ `read()`, `readline()`, `readlines()` for reading.  
✔ `write()`, `append()` for writing.  
✔ `with open()` ensures auto-closing.  
✔ `seek()`, `tell()` manage file positions.  
✔ `pickle` saves Python objects.  

---

# **Unit 4: OOP & Visualization**
# **Object-Oriented Programming (OOP) in Python**  

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.

---

## **📌 1. Classes and Objects**  

A **class** is a blueprint for creating objects, and an **object** is an instance of a class.  

### **Defining a Class and Creating an Object**  
```python
class Car:
    def __init__(self, brand, model):  # Constructor
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
my_car = Car("Toyota", "Corolla")
my_car.display_info()
```
🔹 `__init__()` is a constructor that initializes object attributes.  
🔹 `self` represents the instance of the class.  

---

## **📌 2. Encapsulation**  
Encapsulation restricts access to data by defining public, protected, and private attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Accessor method

# Creating an object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✅ Output: 1500
```
🔹 `__balance` is private (`__` before the variable makes it inaccessible from outside).  
🔹 Use getter (`get_balance()`) and setter methods to access and modify private attributes.  

---

## **📌 3. Inheritance**  
Inheritance allows one class to inherit attributes and methods from another class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent constructor
        self.model = model

    def display(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
my_car = Car("Tesla", "Model S")
my_car.start()      # ✅ Output: Tesla is starting...
my_car.display()    # ✅ Output: Car: Tesla Model S
```
🔹 `super().__init__()` calls the parent class’s constructor.  
🔹 The `Car` class inherits the `start()` method from `Vehicle`.  

---

## **📌 4. Polymorphism**  
Polymorphism allows methods to have different implementations in derived classes.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Function demonstrating polymorphism
def make_sound(animal):
    animal.speak()

# Creating objects
dog = Dog()
cat = Cat()

make_sound(dog)  # ✅ Output: Bark
make_sound(cat)  # ✅ Output: Meow
```
🔹 The `speak()` method is overridden in `Dog` and `Cat`.  
🔹 `make_sound(animal)` can accept any subclass object.  

---

## **📌 5. Abstraction**  
Abstraction hides implementation details and only shows essential features.  

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (no implementation)

class Dog(Animal):
    def make_sound(self):
        print("Bark")

# animal = Animal() ❌ Error (cannot instantiate abstract class)
dog = Dog()
dog.make_sound()  # ✅ Output: Bark
```
🔹 `ABC` is the base class for abstraction.  
🔹 `@abstractmethod` forces child classes to implement `make_sound()`.  

---

## **📌 6. Method Resolution Order (MRO)**  
MRO defines the order in which Python looks for methods in a class hierarchy.  

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.show()  # ✅ Output: B (Method Resolution Order: D → B → C → A)
print(D.mro())  # Shows MRO order
```

🔹 Python follows **C3 Linearization (MRO)** to determine method calling order.  

---

### **🔥 Summary**
✔ **Encapsulation**: Restricts direct access to data.  
✔ **Inheritance**: Allows code reusability by extending classes.  
✔ **Polymorphism**: Enables method overriding.  
✔ **Abstraction**: Hides implementation details.  
✔ **MRO**: Defines method lookup order in multiple inheritance.  

---
# **Multithreading & Concurrency in Python**  

Multithreading and concurrency allow a program to execute multiple tasks simultaneously, improving efficiency and responsiveness.

---

## **📌 1. What is Multithreading?**  
Multithreading enables the execution of multiple threads in a single process.  
- **Thread**: A lightweight, independent execution unit within a process.  
- **Concurrency**: Multiple tasks appearing to run simultaneously.  
- **Parallelism**: Multiple tasks running **simultaneously** on multi-core processors.

---

## **📌 2. Creating a Thread using `threading` Module**  

```python
import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

# Creating a thread
t = threading.Thread(target=print_numbers)
t.start()
t.join()  # Wait for thread to finish before proceeding
```
🔹 `threading.Thread(target=function_name)` creates a new thread.  
🔹 `start()` begins execution.  
🔹 `join()` ensures the main program waits for the thread to complete.  

---

## **📌 3. Running Multiple Threads**  

```python
import threading

def task(name):
    print(f"Task {name} is running...")

# Creating multiple threads
t1 = threading.Thread(target=task, args=("One",))
t2 = threading.Thread(target=task, args=("Two",))

t1.start()
t2.start()

t1.join()
t2.join()
```
🔹 Multiple threads can be started using `start()`.  
🔹 `args=("value",)` passes arguments to the function.  

---

## **📌 4. Global Interpreter Lock (GIL)**
Python's **Global Interpreter Lock (GIL)** allows only one thread to execute Python bytecode at a time, preventing true parallel execution in CPU-bound tasks.

**🛠 How to bypass GIL?**
- Use **multiprocessing** for CPU-intensive tasks.
- Use **threading** only for I/O-bound tasks.

---

## **📌 5. Thread Synchronization (Locks, Semaphores)**  

### **Using a Lock**
A lock ensures that only one thread accesses a shared resource at a time.

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:  # Locking the critical section
        counter += 1

# Creating multiple threads
threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print("Final Counter:", counter)
```
🔹 `lock.acquire()` and `lock.release()` ensure only one thread modifies `counter`.  
🔹 `with lock:` automatically acquires and releases the lock.  

---

## **📌 6. Semaphores**
Semaphores control access to a resource with a limited number of slots.

```python
import threading
import time

semaphore = threading.Semaphore(2)  # Max 2 threads allowed at a time

def worker(name):
    with semaphore:
        print(f"{name} is working...")
        time.sleep(2)  # Simulating work

# Creating multiple threads
threads = [threading.Thread(target=worker, args=(f"Thread-{i}",)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
```
🔹 At most **2** threads can run the `worker` function simultaneously.  

---

## **📌 7. Thread Pooling with `ThreadPoolExecutor`**
A thread pool allows efficient execution of multiple tasks.

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return f"Processed {n}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

print(list(results))
```
🔹 `ThreadPoolExecutor(max_workers=3)` limits execution to 3 threads at a time.  
🔹 `executor.map()` applies the function to multiple inputs.  

---

### **🔥 Summary**
✔ **Multithreading** improves performance for I/O-bound tasks.  
✔ **GIL** prevents true parallel execution for CPU-bound tasks.  
✔ **Locks** and **Semaphores** help synchronize shared resources.  
✔ **Thread pooling** manages multiple threads efficiently.  

---
# **Data Visualization using Matplotlib**  

Matplotlib is a powerful Python library for creating a variety of plots and charts. It is widely used for data visualization in scientific computing and machine learning.

---

## **📌 1. Introduction to Matplotlib**
Matplotlib provides an interface similar to MATLAB for creating static, animated, and interactive plots. The primary module used is `pyplot`.

```python
import matplotlib.pyplot as plt
```

---

## **📌 2. Creating a Simple Line Plot**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-', color='b', label="Data Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()
```
🔹 `plot(x, y)` creates a line plot.  
🔹 `marker='o'` adds data points.  
🔹 `linestyle='-'` defines the line style.  
🔹 `color='b'` sets the color.  
🔹 `show()` displays the plot.  

---

## **📌 3. Scatter Plot**
Used to display the relationship between two variables.

```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='x', alpha=0.7)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot Example")
plt.show()
```
🔹 `scatter(x, y)` creates a scatter plot.  
🔹 `color='red'` changes point color.  
🔹 `marker='x'` sets point style.  
🔹 `alpha=0.7` controls transparency.  

---

## **📌 4. Bar Chart**
```python
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()
```
🔹 `bar(x, y)` creates a bar chart.  
🔹 Colors can be customized for each bar.  

---

## **📌 5. Histogram**
Used to show frequency distributions.

```python
data = np.random.randn(1000)  # 1000 random values

plt.hist(data, bins=30, color='c', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()
```
🔹 `hist(data, bins=30)` creates a histogram with 30 bins.  

---

## **📌 6. Subplots (Multiple Plots in One Figure)**
```python
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot(x, y, 'r')  # Line plot
axes[0, 1].scatter(x, y, color='b')  # Scatter plot
axes[1, 0].bar(categories, values, color='g')  # Bar chart
axes[1, 1].hist(data, bins=20, color='y')  # Histogram

plt.tight_layout()
plt.show()
```
🔹 `subplots(2, 2)` creates a 2×2 grid of plots.  
🔹 Each plot type is placed in a different section.  

---

## **📌 7. 3D Plotting**
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

ax.scatter(x, y, z, color='m')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("3D Scatter Plot")
plt.show()
```
🔹 `projection='3d'` enables 3D plotting.  

---

### **🔥 Summary**
✔ **Matplotlib** is a powerful visualization tool in Python.  
✔ **Line, Scatter, Bar, and Histogram** are basic plots.  
✔ **Subplots** allow multiple charts in one figure.  
✔ **3D plots** enhance data visualization for higher dimensions.  

---
# **Legends, Labels, and Annotations in Matplotlib**  

Matplotlib provides various features to enhance the readability and presentation of plots, including **legends, labels, and annotations**. These elements help explain what different parts of the graph represent.

---

## **📌 1. Adding Labels to Axes**
Labels describe the X and Y axes, making it clear what data the plot represents.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel("X-axis Label")  # Label for X-axis
plt.ylabel("Y-axis Label")  # Label for Y-axis
plt.title("Plot with Labels")  # Title of the plot
plt.show()
```
🔹 **`xlabel()`** → Adds label to the X-axis.  
🔹 **`ylabel()`** → Adds label to the Y-axis.  
🔹 **`title()`** → Adds a title to the plot.  

---

## **📌 2. Adding Legends to a Plot**
A **legend** helps distinguish different data series in a plot.

```python
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 20, 25, 35]

plt.plot(x, y1, marker='o', linestyle='-', color='b', label="Series 1")
plt.plot(x, y2, marker='s', linestyle='--', color='r', label="Series 2")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot with Legend")
plt.legend()  # Adding legend
plt.show()
```
🔹 **`label="Series Name"`** → Defines the legend label for each line.  
🔹 **`legend()`** → Displays the legend on the plot.  

### **👉 Customizing the Legend**
```python
plt.legend(loc="upper left", fontsize=12, shadow=True, title="Legend Title")
```
🔹 `loc="upper left"` → Specifies the legend's position.  
🔹 `fontsize=12` → Sets font size.  
🔹 `shadow=True` → Adds a shadow effect.  
🔹 `title="Legend Title"` → Adds a title inside the legend box.  

---

## **📌 3. Adding Annotations to a Plot**
Annotations highlight specific points in the plot.

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-', color='b')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot with Annotation")

# Annotating a point
plt.annotate(
    "Highest Point", 
    xy=(5, 40),  # Point to annotate
    xytext=(3, 35),  # Text position
    arrowprops=dict(facecolor='red', shrink=0.05)  # Arrow style
)

plt.show()
```
🔹 **`annotate(text, xy, xytext, arrowprops)`** → Adds annotation.  
🔹 `xy=(5,40)` → Specifies the point to annotate.  
🔹 `xytext=(3,35)` → Defines the text's location.  
🔹 `arrowprops=dict(facecolor='red')` → Draws an arrow pointing to the point.  

---

## **🔥 Summary**
✔ **Labels (`xlabel`, `ylabel`, `title`)** → Describe axes and plot title.  
✔ **Legends (`legend()`)** → Help distinguish multiple series.  
✔ **Annotations (`annotate()`)** → Highlight specific points.  

---
Since we've covered **Legends, Labels, and Annotations**, let's move on to the next topic in **Matplotlib**:  

# **📌 3D Plots using Matplotlib**  

Matplotlib provides **`mpl_toolkits.mplot3d`** to create **3D plots**. These plots help visualize data with three axes: **X, Y, and Z**.

---

## **1️⃣ Creating a Simple 3D Plot**  

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample Data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Example function

# Creating 3D Figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting Surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Surface Plot")

plt.show()
```

🔹 **`projection='3d'`** → Enables 3D plotting.  
🔹 **`plot_surface(X, Y, Z, cmap='viridis')`** → Creates a 3D surface plot with color mapping.  

---

## **2️⃣ 3D Scatter Plot**
A **scatter plot in 3D** can be useful for visualizing clusters or distributions.

```python
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Random 3D Data
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

ax.scatter(x, y, z, color='r', marker='o')  # Scatter points

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Scatter Plot")

plt.show()
```

🔹 **`scatter(x, y, z, color='r', marker='o')`** → Creates a 3D scatter plot.  

---

## **3️⃣ 3D Line Plot**
A **3D line plot** can show trends in three dimensions.

```python
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Line Data
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t

ax.plot(x, y, z, color='b', linewidth=2)

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Line Plot")

plt.show()
```

🔹 **`plot(x, y, z, color='b')`** → Draws a 3D line.

---

## **🔥 Summary**
✔ **3D Surface Plot** → `plot_surface()`  
✔ **3D Scatter Plot** → `scatter()`  
✔ **3D Line Plot** → `plot()`  

---

