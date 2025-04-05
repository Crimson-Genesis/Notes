# Data Structer  
# Unit -I  
### Basics of Data Structures  
- Arrays -Insertion and deletion operations-Functions-Pointers- Declaring and Initializing Pointers-Pointer Arithmetic- Function and Pointer Parameters-Pointer and Arrays-Dynamic Memory Allocation  
- Structures- Defining and using a Structure-Passing Structures to Functions-Structure and Pointers  
- Basics of Data Structures-   Classifications (Primitive & Non-Primitive)- Data Structure Operations- Linear Data Structures- Stack: Definition- Array representation- Operations- Recursion, Towers of Hanoi- Applications of stack (Infix to postfix conversion, evaluation of expression).  
---

## **1. Arrays**

### **Definition:**
An array is a collection of elements of the same data type stored at contiguous memory locations. Each element in the array can be accessed using its index.

### **Declaration:**
```c
int arr[5]; // declares an integer array of size 5
```

### **Initialization:**
```c
int arr[5] = {1, 2, 3, 4, 5};
```

### **Accessing Elements:**
```c
printf("%d", arr[2]); // prints 3
```

---

### **Insertion Operation:**
To insert an element at a specific index, we may need to shift elements to the right.
```c
#include <stdio.h>
int main() {
    int arr[6] = {10, 20, 30, 40, 50};
    int i, pos = 2, val = 25;
    for (i = 5; i > pos; i--) {
        arr[i] = arr[i-1];
    }
    arr[pos] = val;

    for (i = 0; i < 6; i++)
        printf("%d ", arr[i]);
    return 0;
}
```

### **Output:**
```
10 20 25 30 40 50
```

---

### **Deletion Operation:**
To delete an element at a specific index, shift elements to the left.
```c
#include <stdio.h>
int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int i, pos = 2;

    for (i = pos; i < 4; i++) {
        arr[i] = arr[i+1];
    }

    for (i = 0; i < 4; i++)
        printf("%d ", arr[i]);
    return 0;
}
```

### **Output:**
```
10 20 40 50
```

---
## **2. Functions in C**

### **Definition:**
A function is a block of code that performs a specific task. It helps divide a program into smaller, manageable parts (modularity).

---

### **Types of Functions:**

| Type                                | Description                                     |
|-------------------------------------|-------------------------------------------------|
| **Library Function**                | Predefined (e.g., `printf()`, `scanf()`)        |
| **User-defined Function**           | Created by the programmer                       |

---

### **Function Syntax:**
```c
return_type function_name(parameters) {
    // body of the function
}
```

---

### **Example: Function to Add Two Numbers**
```c
#include <stdio.h>

// Function declaration
int add(int a, int b);

int main() {
    int sum;
    sum = add(5, 3); // Function call
    printf("Sum: %d", sum);
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
```

### **Output:**
```
Sum: 8
```

---

### **Function with No Arguments and No Return**
```c
void greet() {
    printf("Hello!\n");
}

int main() {
    greet();
    return 0;
}
```

---

### **Function with Arguments but No Return**
```c
void displaySum(int x, int y) {
    printf("Sum: %d\n", x + y);
}

int main() {
    displaySum(10, 20);
    return 0;
}
```

---

### **Function with Return but No Arguments**
```c
int getNumber() {
    return 42;
}

int main() {
    int num = getNumber();
    printf("Number: %d", num);
    return 0;
}
```

---
## **3. Pointers**

### **Definition:**
A **pointer** is a variable that stores the memory address of another variable.

---

### **Syntax:**
```c
data_type *pointer_name;
```

### **Example:**
```c
int a = 10;
int *p;
p = &a;  // p stores the address of variable a
```

---

### **Basic Concepts:**
| Concept                  | Explanation                                   |
|--------------------------|-----------------------------------------------|
| `&` (Address-of)         | Gets the address of a variable                |
| `*` (Dereference)        | Accesses the value stored at a pointer       |

---

### **Example Program:**
```c
#include <stdio.h>

int main() {
    int a = 5;
    int *p;
    p = &a;

    printf("Value of a: %d\n", a);        // 5
    printf("Address of a: %p\n", &a);     // Memory address
    printf("Value of p: %p\n", p);        // Same as &a
    printf("Value pointed by p: %d\n", *p); // 5

    return 0;
}
```

---

## **Pointer Arithmetic**

### **Operations:**
You can perform arithmetic operations on pointers:
- Increment (`p++`)
- Decrement (`p--`)
- Add or subtract an integer (`p + 2`, `p - 1`)

> These operations move the pointer by the size of the data type.

---

### **Example:**
```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};
    int *p = arr;

    printf("%d\n", *p);     // 10
    printf("%d\n", *(p+1)); // 20
    printf("%d\n", *(p+2)); // 30

    return 0;
}
```

---
## **4. Function and Pointer Parameters**

### **Passing Variables by Reference Using Pointers**

In C, **pointers** allow you to pass the address of a variable to a function, enabling the function to **modify the original variable** (i.e., pass-by-reference).

---

### **Syntax:**
```c
void function_name(int *param) {
    // *param refers to the original variable
}
```

---

### **Example: Swapping Two Numbers Using Pointers**
```c
#include <stdio.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main() {
    int a = 10, b = 20;
    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After swap: a = %d, b = %d\n", a, b);
    return 0;
}
```

### **Output:**
```
Before swap: a = 10, b = 20  
After swap: a = 20, b = 10
```

---

### **Why Use Pointers in Functions?**
- To modify actual variables.
- To reduce memory usage by avoiding large structure copies.
- Required for dynamic memory allocation and data structures.

---
## **5. Pointer and Arrays**

### **Relationship Between Pointers and Arrays**

In C, the name of an array acts like a pointer to its **first element**. You can use pointer arithmetic to access array elements.

---

### **Key Concepts:**
- `arr[i]` is equivalent to `*(arr + i)`
- An array name is a constant pointer.

---

### **Example: Accessing Array Elements with Pointers**
```c
#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = arr;

    printf("Using array indexing:\n");
    for(int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nUsing pointer arithmetic:\n");
    for(int i = 0; i < 5; i++) {
        printf("%d ", *(ptr + i));
    }

    return 0;
}
```

### **Output:**
```
Using array indexing:
10 20 30 40 50
Using pointer arithmetic:
10 20 30 40 50
```

---

### **Why It Matters:**
- Helps in implementing dynamic arrays.
- Used heavily in data structures like linked lists, stacks, etc.
- Pointers make functions work with arrays efficiently.

---
## **6. Dynamic Memory Allocation**

Dynamic Memory Allocation allows programs to request memory during runtime, unlike static allocation where memory is assigned during compile time.

---

### **Key Functions in C:**
| Function | Purpose |
|---------|---------|
| `malloc(size)` | Allocates a block of memory of `size` bytes. Returns a `void*` pointer. |
| `calloc(n, size)` | Allocates memory for `n` blocks of `size` bytes each and initializes them to 0. |
| `realloc(ptr, new_size)` | Reallocates the previously allocated memory to a new size. |
| `free(ptr)` | Frees the allocated memory. |

---

### **Example: Using `malloc` and `free`**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    arr = (int*) malloc(n * sizeof(int)); // Allocate memory for 5 integers

    if (arr == NULL) {
        printf("Memory allocation failed!");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }

    printf("Dynamic array contents:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    free(arr); // Deallocate memory
    return 0;
}
```

### **Output:**
```
Dynamic array contents:
0 10 20 30 40
```

---

### **Why It's Important:**
- Essential for data structures like **linked lists**, **stacks**, and **queues** where size isn't known in advance.
- Avoids memory wastage by allocating memory as needed.
- Enables resizing memory blocks during runtime.

---
## **7. Structures – Defining and Using a Structure**

A **structure** in C is a user-defined data type that allows grouping variables of different types under a single name.

---

### **Syntax: Defining a Structure**
```c
struct Student {
    int id;
    char name[50];
    float marks;
};
```

### **Declaring Structure Variables**
```c
struct Student s1;  // Using 'struct' keyword
```

You can also define and declare at once:
```c
struct Student {
    int id;
    char name[50];
    float marks;
} s1, s2;
```

---

### **Accessing Members**
Use the dot `.` operator:
```c
s1.id = 101;
strcpy(s1.name, "Alice");
s1.marks = 92.5;
```

---

### **Example: Structure to Store Student Information**
```c
#include <stdio.h>
#include <string.h>

struct Student {
    int id;
    char name[50];
    float marks;
};

int main() {
    struct Student s;

    s.id = 1;
    strcpy(s.name, "John Doe");
    s.marks = 87.5;

    printf("ID: %d\n", s.id);
    printf("Name: %s\n", s.name);
    printf("Marks: %.2f\n", s.marks);

    return 0;
}
```

### **Output:**
```
ID: 1
Name: John Doe
Marks: 87.50
```

---

### **Use Cases:**
- Useful in defining records (e.g., students, employees, products).
- Helps in managing grouped data more logically.

---
## **8. Passing Structures to Functions**

Structures in C can be passed to functions in **two ways**:
- **Pass by value**
- **Pass by reference (using pointers)**

---

### 🔹 **1. Pass by Value**

When a structure is passed by value, a **copy** of the entire structure is made. Changes made inside the function do **not affect** the original structure.

#### Example:
```c
#include <stdio.h>

struct Student {
    int id;
    float marks;
};

void display(struct Student s) {
    printf("ID: %d\n", s.id);
    printf("Marks: %.2f\n", s.marks);
}

int main() {
    struct Student s1 = {101, 85.5};
    display(s1);
    return 0;
}
```

#### Output:
```
ID: 101
Marks: 85.50
```

- ✅ Safe but uses more memory and time (copying large structures).

---

### 🔹 **2. Pass by Reference (Using Pointers)**

When a structure is passed by reference, only the **address** is passed. Changes made inside the function **reflect in the original structure**.

#### Example:
```c
#include <stdio.h>

struct Student {
    int id;
    float marks;
};

void update(struct Student *s) {
    s->marks += 5;  // Increase marks by 5
}

int main() {
    struct Student s1 = {101, 85.5};
    update(&s1);
    printf("Updated Marks: %.2f\n", s1.marks);
    return 0;
}
```

#### Output:
```
Updated Marks: 90.50
```

- ✅ Efficient and allows modifications
- ❌ Requires pointer handling (slightly more complex)

---

### 🔸 Summary Table:

| Method              | Memory Usage | Allows Modification | Syntax Complexity |
|---------------------|--------------|----------------------|--------------------|
| Pass by Value       | More         | ❌ No                | Easy               |
| Pass by Reference   | Less         | ✅ Yes               | Moderate           |

---

### 💡 Use Case Tips:

- Use **pass by value** when you only need to **read data**.
- Use **pass by reference** when you need to **modify** the original structure or save memory for large structures.

---
## **9. Structure and Pointers**

In C, we can use **pointers** with structures to access or modify structure members efficiently, especially when working with dynamic memory or passing structures to functions.

---

### 🔹 Declaring a Pointer to a Structure

To declare a pointer to a structure:
```c
struct Student {
    int id;
    float marks;
};

struct Student s1;
struct Student *ptr;

ptr = &s1;  // Pointer now points to s1
```

---

### 🔹 Accessing Members Using Pointers

Use the **arrow operator (`->`)** to access structure members via pointer:

```c
ptr->id = 101;
ptr->marks = 89.5;
```

This is equivalent to:
```c
(*ptr).id = 101;
(*ptr).marks = 89.5;
```

---

### 🔸 Example: Using Structure Pointer

```c
#include <stdio.h>

struct Student {
    int id;
    float marks;
};

int main() {
    struct Student s1 = {101, 90.0};
    struct Student *ptr = &s1;

    printf("ID: %d\n", ptr->id);
    printf("Marks: %.2f\n", ptr->marks);

    ptr->marks += 5;  // Update using pointer
    printf("Updated Marks: %.2f\n", ptr->marks);

    return 0;
}
```

#### Output:
```
ID: 101
Marks: 90.00
Updated Marks: 95.00
```

---

### 🔹 Structure with Dynamic Memory Allocation

Structure pointers are commonly used with dynamic memory using `malloc()` or `calloc()`:

```c
#include <stdio.h>
#include <stdlib.h>

struct Student {
    int id;
    float marks;
};

int main() {
    struct Student *ptr = (struct Student *)malloc(sizeof(struct Student));
    ptr->id = 111;
    ptr->marks = 88.5;

    printf("ID: %d\n", ptr->id);
    printf("Marks: %.2f\n", ptr->marks);

    free(ptr); // Don't forget to free the memory
    return 0;
}
```

---

### 🔸 Why Use Structure Pointers?

- Efficient memory usage
- Useful in dynamic memory allocation
- Required for passing structures by reference
- Used in linked lists, trees, and other data structures

---

### 💡 Key Notes:

| Concept                | Syntax                    |
|------------------------|---------------------------|
| Declare Pointer        | `struct A *ptr;`          |
| Assign Address         | `ptr = &var;`             |
| Access Member          | `ptr->member` or `(*ptr).member` |
| Dynamic Allocation     | `malloc(sizeof(struct A))` |

---
## **10. Basics of Data Structures – Classifications (Primitive & Non-Primitive)**

Understanding the classification of data structures is essential because it helps in choosing the appropriate structure for a given problem.

---

### 🔹 What is a Data Structure?

A **data structure** is a way to store and organize data in a computer so that it can be used efficiently.

---

### 🔸 Classification of Data Structures

Data structures are broadly classified into:

#### 1. **Primitive Data Structures**
These are basic data types supported by most programming languages.

| Type       | Example        |
|------------|----------------|
| Integer    | `int`          |
| Float      | `float`        |
| Character  | `char`         |
| Boolean    | `bool` (in C++)|

> 💡 Primitive types directly operate upon the machine instructions.

---

#### 2. **Non-Primitive Data Structures**

These are more complex data types built using primitive types. They are divided into:

##### a. **Linear Data Structures**
- Elements are arranged in a **sequential** order.
- Examples:
  - **Array**
  - **Linked List**
  - **Stack**
  - **Queue**

##### b. **Non-Linear Data Structures**
- Elements are **not arranged sequentially**.
- They may have hierarchical relationships.
- Examples:
  - **Tree**
  - **Graph**

##### c. **File Structures**
- Used to store data in secondary memory.
- Organized based on a specific format (sequential, indexed, etc.)

---

### 🔸 Diagram: Classification of Data Structures

```
Data Structures
├── Primitive
│   ├── int
│   ├── float
│   └── char
├── Non-Primitive
│   ├── Linear
│   │   ├── Array
│   │   ├── Linked List
│   │   ├── Stack
│   │   └── Queue
│   ├── Non-Linear
│   │   ├── Tree
│   │   └── Graph
│   └── File
```

---

### 🔹 Why This Classification Matters

- **Efficiency**: Choosing the right data structure optimizes performance.
- **Suitability**: Some structures are better suited for certain algorithms or data types.

---

### 🧠 Example Question:
**Q:** Classify the following: `int`, `queue`, `graph`, `char`

**A:**  
- `int` → Primitive  
- `queue` → Non-Primitive, Linear  
- `graph` → Non-Primitive, Non-Linear  
- `char` → Primitive  

---
## **11. Data Structure Operations**

Operations on data structures are the fundamental actions we can perform to modify, access, or manage data stored within them.

---

### 🔹 Common Operations on Data Structures

Regardless of the type of data structure, most support the following core operations:

| Operation        | Description |
|------------------|-------------|
| **Traversal**     | Accessing each element of the data structure exactly once to process it. |
| **Insertion**     | Adding a new element to the data structure. |
| **Deletion**      | Removing an element from the data structure. |
| **Searching**     | Finding a particular element in the data structure. |
| **Sorting**       | Arranging the elements in a specific order (ascending/descending). |
| **Updating**      | Changing the value of an element. |

---

### 🔸 Operation Examples

#### 🔹 1. **Traversal**
Example: Print all elements of an array  
```c
int arr[] = {10, 20, 30};
for (int i = 0; i < 3; i++)
    printf("%d ", arr[i]);
```

#### 🔹 2. **Insertion**
Example: Insert an element at end of an array
```c
arr[n] = 40;
n++;
```

#### 🔹 3. **Deletion**
Example: Delete an element by shifting elements
```c
for (int i = pos; i < n - 1; i++)
    arr[i] = arr[i + 1];
n--;
```

#### 🔹 4. **Searching**
Example: Linear search
```c
for (int i = 0; i < n; i++)
    if (arr[i] == key)
        return i;
```

#### 🔹 5. **Sorting**
Example: Bubble sort (ascending order)
```c
for (int i = 0; i < n - 1; i++)
    for (int j = 0; j < n - i - 1; j++)
        if (arr[j] > arr[j + 1])
            swap(arr[j], arr[j + 1]);
```

#### 🔹 6. **Updating**
Example: Updating the value at index 2
```c
arr[2] = 50;
```

---

### 📌 Key Points

- Efficient implementation of operations determines the **performance** of algorithms.
- Different structures offer different **time complexities** for operations. For example:
  - Searching in an **array** (unsorted) = O(n)
  - Searching in a **BST** (balanced) = O(log n)

---

### 🧠 Example Question:
**Q:** Which operation would you use to remove a value from a linked list?
**A:** Deletion operation.

---
## **12. Linear Data Structures**

### 🔹 What Are Linear Data Structures?

Linear data structures are data structures where elements are arranged sequentially, and each element is connected to the previous and the next one (except the first and last). They allow traversal in a single level from beginning to end.

---

### 🔸 Examples of Linear Data Structures

| Data Structure | Description |
|----------------|-------------|
| **Array**      | A collection of elements stored at contiguous memory locations. |
| **Linked List**| A linear collection of nodes where each node points to the next. |
| **Stack**      | A linear structure that follows **LIFO** (Last In First Out). |
| **Queue**      | A linear structure that follows **FIFO** (First In First Out). |

---

### 🔹 Key Characteristics

- **Single level** storage of elements.
- **Easy to implement** using arrays or linked lists.
- **Predictable traversal** order.
- **Memory usage is sequential** (especially in arrays).

---

### 🔸 Comparison of Linear Structures

| Structure | Insertion | Deletion | Access | Use Case |
|----------|-----------|----------|--------|----------|
| Array | Easy at end, costly at front | Costly if not at end | Fast (random access) | Static data |
| Linked List | Easy at head or tail | Easy if pointer is known | Slow (sequential) | Dynamic data |
| Stack | At top only | From top only | Top access only | Expression evaluation |
| Queue | At rear | From front | Sequential | Scheduling tasks |

---

### 📌 Example Use Case

- **Stacks**: Undo operations, expression conversion
- **Queues**: Task scheduling, printer queue
- **Arrays**: Lookup tables, static data
- **Linked Lists**: Dynamic memory usage, efficient insertion/deletion

---

### 🧠 Example Problem

**Q:** Which linear data structure would be best for implementing a browser's back button?

**A:** Stack — because it follows Last In First Out (LIFO), which suits the backtracking nature.

---
## **13. Stack: Definition**

### 🔹 What is a Stack?

A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element inserted into the stack is the first one to be removed.

---

### 🔸 Real-World Analogy

Think of a **stack of plates**:
- The plate you placed last on top is the first one you'll take off.
- You can only insert (push) or remove (pop) from the **top** of the stack.

---

### 🔹 Stack Terminologies

| Term       | Description |
|------------|-------------|
| **Push**   | Insert an element into the stack |
| **Pop**    | Remove the top element from the stack |
| **Peek/Top** | Retrieve the top element without removing it |
| **Underflow** | Attempt to pop from an empty stack |
| **Overflow** | Attempt to push into a full stack (in static stack) |

---

### 🔸 Stack Representation

- Can be represented using **arrays** or **linked lists**.
- Requires a **TOP** pointer to track the current top of the stack.

---

### 🔹 Stack Operations (using array)

```c
#define SIZE 100
int stack[SIZE];
int top = -1;

void push(int value) {
    if(top >= SIZE-1)
        printf("Stack Overflow");
    else
        stack[++top] = value;
}

int pop() {
    if(top == -1)
        printf("Stack Underflow");
    else
        return stack[top--];
}
```

---

### 🧠 Example Problem

**Q:** Show the status of the stack after the following operations:  
`PUSH(10), PUSH(20), POP(), PUSH(30), PUSH(40)`

**A:**

| Operation   | Stack Contents (Top → Bottom) |
|-------------|-------------------------------|
| PUSH(10)    | 10                            |
| PUSH(20)    | 20, 10                        |
| POP()       | 10                            |
| PUSH(30)    | 30, 10                        |
| PUSH(40)    | 40, 30, 10                    |

---
## **14. Stack: Array Representation**

### 🔹 Stack Using Arrays

A stack can be implemented using a **fixed-size array**, where a variable (usually named `top`) keeps track of the **index of the topmost element**.

---

### 🔸 Components of Array Representation

- **Array** to store the elements
- **Integer `top`** to keep track of the top position in the stack
- **MAX / SIZE** constant defining the maximum number of elements the stack can hold

---

### 🔹 Initial Conditions

- `top = -1` when the stack is **empty**
- Stack becomes **full** when `top == SIZE - 1`

---

### 🔸 Basic Operations

#### ➤ Push Operation

```c
void push(int stack[], int *top, int value, int SIZE) {
    if (*top == SIZE - 1)
        printf("Stack Overflow\n");
    else
        stack[++(*top)] = value;
}
```

#### ➤ Pop Operation

```c
int pop(int stack[], int *top) {
    if (*top == -1) {
        printf("Stack Underflow\n");
        return -1;
    } else {
        return stack[(*top)--];
    }
}
```

#### ➤ Peek (View Top Element)

```c
int peek(int stack[], int top) {
    if (top == -1)
        return -1;
    return stack[top];
}
```

---

### 🔸 Example

```c
#define SIZE 5
int stack[SIZE];
int top = -1;

push(stack, &top, 10);  // Stack: 10
push(stack, &top, 20);  // Stack: 20, 10
pop(stack, &top);       // Stack: 10
```

---

### 🧠 Example Problem

**Q:** Implement push and pop operations on a stack of size 3 and perform:  
`PUSH(5), PUSH(8), PUSH(2), PUSH(9), POP(), POP(), PUSH(7)`

**A:**

| Operation   | Output         | Stack Contents (Top → Bottom) |
|-------------|----------------|-------------------------------|
| PUSH(5)     | –              | 5                             |
| PUSH(8)     | –              | 8, 5                          |
| PUSH(2)     | –              | 2, 8, 5                       |
| PUSH(9)     | Overflow       | 2, 8, 5                       |
| POP()       | 2              | 8, 5                          |
| POP()       | 8              | 5                             |
| PUSH(7)     | –              | 7, 5                          |

---
## **15. Stack: Operations**

### 🔹 What is a Stack?

A **stack** is a **linear data structure** that follows the **Last In, First Out (LIFO)** principle. The most recent item added is the first one removed.

---

### 🔸 Primary Stack Operations

1. **Push(x)**  
   → Inserts element `x` on the top of the stack.  
   → Checks for **overflow**.

2. **Pop()**  
   → Removes and returns the top element of the stack.  
   → Checks for **underflow**.

3. **Peek() / Top()**  
   → Returns the topmost element without removing it.

4. **isEmpty()**  
   → Returns `true` if stack has no elements.

5. **isFull()**  
   → Returns `true` if stack has reached maximum capacity.

---

### 🔹 Stack Operation Flow (Visual)

Let’s assume an empty stack with `SIZE = 3`

```
Initial:        []
PUSH(10)        [10]
PUSH(20)        [20, 10]
PUSH(30)        [30, 20, 10]
PUSH(40)        Overflow
POP()           [20, 10] → returns 30
POP()           [10]     → returns 20
PEEK()          [10]     → returns 10
```

---

### 🔸 Full Example in C

```c
#include <stdio.h>
#define SIZE 3

int stack[SIZE];
int top = -1;

void push(int value) {
    if (top == SIZE - 1)
        printf("Stack Overflow\n");
    else
        stack[++top] = value;
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

int peek() {
    if (top == -1)
        return -1;
    return stack[top];
}
```

---

### 🧠 Example Problem

**Q:** Perform the following stack operations:  
`PUSH(1), PUSH(2), PUSH(3), POP(), PUSH(4), PEEK()`

**A:**

| Operation   | Stack (Top → Bottom) | Returned Value |
|-------------|-----------------------|----------------|
| PUSH(1)     | 1                     | –              |
| PUSH(2)     | 2, 1                  | –              |
| PUSH(3)     | 3, 2, 1               | –              |
| POP()       | 2, 1                  | 3              |
| PUSH(4)     | 4, 2, 1               | –              |
| PEEK()      | 4, 2, 1               | 4              |

---
## **16. Recursion**

### 🔹 What is Recursion?

**Recursion** is a programming technique where a function **calls itself** to solve a problem. Each recursive call solves a **smaller instance** of the original problem until a **base case** is reached.

---

### 🔸 Characteristics of Recursive Functions:

1. **Base Case**  
   - Terminates recursion to prevent infinite loops.
2. **Recursive Case**  
   - The part of the function that includes the recursive call.
3. **Stack Usage**  
   - Each function call is pushed onto the call stack.

---

### 🔸 Simple Example: Factorial

**Problem:** Find factorial of `n`  
**Definition:**  
$n! = n \times (n - 1)!$  
Base case: $0! = 1$

```c
int factorial(int n) {
    if (n == 0) 
        return 1;         // Base case
    else 
        return n * factorial(n - 1);  // Recursive call
}
```

---

### 🧠 Example Problem

**Q:** Find the factorial of 5

**A:**
```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 5 * 4 * 3 * 2 * 1 * 1 = 120
```

---

### 🔸 Recursive vs Iterative

| Feature        | Recursion                  | Iteration                 |
|----------------|----------------------------|---------------------------|
| Approach       | Function calls itself       | Looping structures (for/while) |
| Memory Usage   | More (stack frames)         | Less                      |
| Performance    | Sometimes slower            | Often faster              |
| Readability    | Often cleaner for complex logic | Verbose                  |

---

### 🔸 Real-Life Analogy

- **Matryoshka dolls**: Each doll contains a smaller doll → until you reach the smallest.
- **Directory Traversal**: Listing all files in nested folders.

---
## **17. Towers of Hanoi (Application of Recursion)**

### 🔹 Problem Statement

You are given **3 rods** and **n disks** of different sizes which can slide onto any rod. The puzzle starts with the disks **stacked in ascending order of size** on one rod (largest at the bottom).

**Goal**: Move all the disks to another rod following these rules:

1. Only one disk can be moved at a time.
2. Only the **top disk** of a rod can be moved.
3. A larger disk **cannot be placed** on top of a smaller disk.

---

### 🔸 Recursive Approach

Let’s name the rods as:
- **A**: Source rod  
- **B**: Auxiliary rod  
- **C**: Destination rod

#### Steps:
1. Move `n - 1` disks from A to B using C.
2. Move the largest disk from A to C.
3. Move `n - 1` disks from B to C using A.

---

### 🔸 Recursive Function in C

```c
#include <stdio.h>

void hanoi(int n, char from_rod, char to_rod, char aux_rod) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", from_rod, to_rod);
        return;
    }
    hanoi(n - 1, from_rod, aux_rod, to_rod);
    printf("Move disk %d from %c to %c\n", n, from_rod, to_rod);
    hanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main() {
    int n = 3;
    hanoi(n, 'A', 'C', 'B');
    return 0;
}
```

---

### 🔸 Example Output for 3 Disks

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

---

### 🔸 Time Complexity

The number of moves required = $2^n - 1$  
So, time complexity = **O($2^n$)**

---

### 🧠 Why Recursion Works Here

Each step of the puzzle is a **smaller instance** of the same problem. By solving smaller versions recursively, we solve the full puzzle elegantly.

---
## **18. Applications of Stack – Infix to Postfix Conversion**

---

### 🔹 What is Infix, Postfix?

- **Infix Expression**: Operators appear **between operands**  
  e.g. `A + B`
  
- **Postfix Expression (Reverse Polish Notation)**: Operators appear **after operands**  
  e.g. `AB+`

---

### 🔹 Why Convert Infix to Postfix?

- Postfix expressions do **not require parentheses**
- They are **easier to evaluate** using a stack

---

### 🔹 Precedence and Associativity Table

| Operator | Precedence | Associativity |
|----------|------------|---------------|
| `^`      | Highest    | Right         |
| `* / %`  | High       | Left          |
| `+ -`    | Low        | Left          |

---

### 🔹 Algorithm to Convert Infix to Postfix (Using Stack)

1. Initialize an empty **stack** for operators and an empty **output string**.
2. Scan the infix expression from **left to right**:
   - **Operand** → Add to output
   - **Left parenthesis** `(` → Push to stack
   - **Right parenthesis** `)` → Pop from stack to output until `(` is encountered (discard `(`)
   - **Operator** → Pop operators from stack to output **while precedence is higher or equal** (except `^`, which is right associative), then push current operator
3. After the scan, pop all remaining operators from the stack to output.

---

### 🔹 Example

**Input**: `(A+B)*C`  
**Output**: `AB+C*`

**Steps**:
- Read `(` → push  
- Read `A` → output: `A`  
- Read `+` → push  
- Read `B` → output: `AB`  
- Read `)` → pop `+` → output: `AB+`, discard `(`  
- Read `*` → push  
- Read `C` → output: `AB+C`  
- End → pop `*` → output: `AB+C*`

---

### 🔹 C Code

```c
#include <stdio.h>
#include <ctype.h>

#define SIZE 100
char stack[SIZE];
int top = -1;

int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/' || op == '%') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}

void push(char ch) {
    stack[++top] = ch;
}

char pop() {
    return stack[top--];
}

char peek() {
    return stack[top];
}

int isEmpty() {
    return top == -1;
}

void infixToPostfix(char* exp) {
    for (int i = 0; exp[i]; i++) {
        char ch = exp[i];

        if (isalnum(ch)) {
            printf("%c", ch);
        } else if (ch == '(') {
            push(ch);
        } else if (ch == ')') {
            while (!isEmpty() && peek() != '(')
                printf("%c", pop());
            pop(); // pop '('
        } else {
            while (!isEmpty() && precedence(ch) <= precedence(peek()))
                printf("%c", pop());
            push(ch);
        }
    }
    while (!isEmpty()) {
        printf("%c", pop());
    }
    printf("\n");
}

int main() {
    char expr[] = "(A+B)*C";
    printf("Postfix: ");
    infixToPostfix(expr);
    return 0;
}
```

---

### 🔹 Output

```
Postfix: AB+C*
```

---

### 🧠 Key Insight

Stacks help manage **operator precedence** and **parentheses** in infix expressions, enabling easy and correct postfix conversion.

---
## **19. Applications of Stack – Evaluation of Postfix Expression**

---

### 🔹 What is Postfix Expression?

In postfix (Reverse Polish) notation:
- **Operators come after operands**
- **No parentheses** needed
- e.g., Infix: `(3 + 4) * 5` → Postfix: `3 4 + 5 *`

---

### 🔹 Why Postfix is Easy to Evaluate?

Because the order of operations is already encoded, and there's **no need to check precedence or brackets**. We just **evaluate left to right** using a **stack**.

---

### 🔹 Algorithm to Evaluate Postfix Expression

1. Initialize an empty **stack**.
2. Scan the expression from **left to right**:
   - **Operand** → push to stack
   - **Operator** → pop top two elements, apply the operator, push result back
3. At the end, the stack will have **one element**, the result.

---

### 🔹 Example

**Postfix**: `3 4 + 5 *`  
**Steps**:

| Step | Stack |
|------|-------|
| Read 3 → push | 3 |
| Read 4 → push | 3 4 |
| Read + → pop 3, 4 → 3+4=7 → push | 7 |
| Read 5 → push | 7 5 |
| Read * → pop 7, 5 → 7*5=35 → push | 35 |

✅ Final Result: `35`

---

### 🔹 C Code

```c
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define SIZE 100
int stack[SIZE];
int top = -1;

void push(int val) {
    stack[++top] = val;
}

int pop() {
    return stack[top--];
}

int evaluatePostfix(char* exp) {
    for (int i = 0; exp[i]; i++) {
        char ch = exp[i];

        if (isdigit(ch)) {
            push(ch - '0');
        } else {
            int b = pop();
            int a = pop();
            switch (ch) {
                case '+': push(a + b); break;
                case '-': push(a - b); break;
                case '*': push(a * b); break;
                case '/': push(a / b); break;
            }
        }
    }
    return pop();
}

int main() {
    char expr[] = "34+5*";  // equivalent to (3 + 4) * 5
    printf("Result = %d\n", evaluatePostfix(expr));
    return 0;
}
```

---

### 🔹 Output

```
Result = 35
```

---

### 🧠 Key Insight

Using a stack simplifies expression evaluation by maintaining operand order and managing operations without worrying about precedence or brackets.

---
# Unit -II  
### Queue and Linked List  
- Queue: Definition- Array representation   Operations- Applications. Types of queues- Simple queue- Circular queue- Double-ended queue-Priority queue.  
- Linked List: Definition- Singly linked list: Representation in memory- Traversing - Insertion- Deletion and Searching.   
- Doubly linked list- Header linked list- Circular linked list.  
---

### Queue: Definition

A **Queue** is a linear data structure that follows the **FIFO** (First In First Out) principle. The element that is inserted first is the one that is removed first. It's analogous to a line of people waiting—first come, first served.

#### Basic Terminology
- **Front**: The index from where the element is removed.
- **Rear**: The index where a new element is inserted.

---

### Array Representation of Queue

In array representation, the queue is maintained using an array and two indices: `front` and `rear`.

#### Initialization:
```c
int queue[SIZE];
int front = -1, rear = -1;
```

#### Enqueue Operation (Insert):
```c
if(rear == SIZE - 1)
    printf("Queue Overflow\n");
else {
    if(front == -1)
        front = 0;
    rear++;
    queue[rear] = element;
}
```

#### Dequeue Operation (Remove):
```c
if(front == -1 || front > rear)
    printf("Queue Underflow\n");
else {
    printf("Element deleted: %d", queue[front]);
    front++;
}
```

---

### Example Problem: Enqueue and Dequeue in Array Queue

**Input**: Enqueue 10, 20, 30 → Dequeue → Enqueue 40  
**Process**:
- Enqueue 10 → Queue: [10]
- Enqueue 20 → Queue: [10, 20]
- Enqueue 30 → Queue: [10, 20, 30]
- Dequeue → Removed 10 → Queue: [20, 30]
- Enqueue 40 → Queue: [20, 30, 40]

**Output**:
```
Deleted element: 10
Final queue: 20, 30, 40
```

---

### Types of Queues

Queues can be implemented in several variations to handle different use-cases more efficiently. Below are the commonly used types of queues:

---

### 1. Simple Queue (Linear Queue)

- **FIFO structure**.
- Insert at `rear` and delete from `front`.
- Inefficient memory usage due to unused spaces at the beginning after deletions.

#### Example:
```text
Enqueue: 10, 20, 30
Dequeue: 10
Queue: [__, 20, 30] → can't insert more when rear = SIZE-1
```

---

### 2. Circular Queue

- Overcomes the limitation of the simple queue by connecting the rear to the front.
- Efficient use of memory.
- Insert and delete operations are done using modulo arithmetic.

#### Formula:
```c
rear = (rear + 1) % SIZE;
front = (front + 1) % SIZE;
```

#### Example:
```text
Initial Queue: [__, __, __, __, __]
Enqueue 10, 20, 30 → [10, 20, 30, __, __]
Dequeue twice → [__, __, 30, __, __]
Enqueue 40, 50 → [10, 20, 30, 40, 50] (wraps around)
```

---

### 3. Double-Ended Queue (Deque)

- Insertion and deletion allowed at **both ends**.
- Two types:
  - **Input-restricted deque**: Insertion at one end only.
  - **Output-restricted deque**: Deletion at one end only.

#### Example:
```text
Deque: [20, 30]
InsertLeft(10) → [10, 20, 30]
InsertRight(40) → [10, 20, 30, 40]
DeleteLeft() → [20, 30, 40]
DeleteRight() → [20, 30]
```

---

### 4. Priority Queue

- Elements are inserted based on **priority**.
- Higher priority elements are removed before lower priority ones, regardless of insertion order.
- Implemented using:
  - Array of queues for different priorities
  - Heap (binary heap for efficiency)

#### Example:
```text
Insert(30, p=1), Insert(20, p=3), Insert(40, p=2)
→ Order of Deletion: 20 (p=3), 40 (p=2), 30 (p=1)
```

---
### Linked List: Definition

A **Linked List** is a linear data structure where elements (called *nodes*) are stored in **non-contiguous memory locations**. Each node contains two parts:
1. **Data**: The actual value stored.
2. **Pointer (Link)**: A reference to the next node in the list.

---

### Advantages of Linked List over Arrays:
- **Dynamic size**: Grows and shrinks during runtime.
- **Efficient insertion/deletion**: Especially in the middle or beginning.
- No memory wastage due to unused indices like in arrays.

---

### Types of Linked Lists:
1. **Singly Linked List**
2. **Doubly Linked List**
3. **Circular Linked List**
4. **Header Linked List** (variation)

---

### Basic Node Structure (in C):
```c
struct Node {
    int data;
    struct Node* next;
};
```

---

### Visual Example:
```text
Head → [10|*] → [20|*] → [30|NULL]
```
Each box is a node with data and a pointer to the next.

---

### Real-World Analogy:
Imagine train compartments connected using couplers. Each coach knows only about the next coach.

---
### Singly Linked List: Representation in Memory

A **Singly Linked List (SLL)** is a collection of nodes where **each node points to the next node** in the sequence. It is the simplest type of linked list, and it ends with a node that points to `NULL`, marking the end of the list.

---

### Node Structure in C:
```c
struct Node {
    int data;
    struct Node* next;
};
```

### Memory Representation:

Suppose we have a list with values: 5 → 10 → 15

Each node is created in a different memory location and linked using pointers:
```
Address     Node
1000       [5 | 1040]
1040       [10 | 1070]
1070       [15 | NULL]
```

The head pointer holds the address of the first node (1000). Each node’s `next` pointer holds the address of the next node. The last node points to `NULL`.

---

### Creating and Linking Nodes (Example in C):
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    struct Node* head = malloc(sizeof(struct Node));
    struct Node* second = malloc(sizeof(struct Node));
    struct Node* third = malloc(sizeof(struct Node));

    head->data = 5;
    head->next = second;

    second->data = 10;
    second->next = third;

    third->data = 15;
    third->next = NULL;

    return 0;
}
```

---

This way, the singly linked list is dynamically built in memory with nodes pointing to the next node, and memory is not wasted like in arrays.

---
### Traversing a Singly Linked List

**Traversing** means visiting each node in the list exactly once, from the head to the last node. This is commonly used to display data, search for elements, or perform calculations like sum or count.

---

### Logic:

Start from the `head` node and follow the `next` pointers until `NULL` is reached.

---

### Algorithm:
1. Initialize a pointer `ptr` to the head.
2. While `ptr` is not `NULL`:
   - Access `ptr->data`
   - Move to the next node: `ptr = ptr->next`

---

### Example in C:
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void traverse(struct Node* head) {
    struct Node* ptr = head;
    while (ptr != NULL) {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}
```

### Sample Output:
```
5 -> 10 -> 15 -> NULL
```

---

### Example Problem:

**Problem:** Write a function to count the number of nodes in a singly linked list.

**Solution:**
```c
int countNodes(struct Node* head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}
```

---

**Time Complexity:** $O(n)$  
**Space Complexity:** $O(1)$

### Insertion in a Singly Linked List

**Insertion** in a singly linked list means adding a new node at a specified position in the list. The common cases include:

1. Insertion at the beginning  
2. Insertion at the end  
3. Insertion after a given node  

---

## 1. Insertion at the Beginning

**Logic:**
- Create a new node.
- Point its `next` to the current `head`.
- Update `head` to this new node.

**Code:**
```c
void insertAtBeginning(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = *head;
    *head = newNode;
}
```

---

## 2. Insertion at the End

**Logic:**
- Create a new node.
- Traverse to the last node.
- Make `last->next` point to the new node.

**Code:**
```c
void insertAtEnd(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head;
    newNode->data = newData;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = newNode;
}
```

---

## 3. Insertion After a Given Node

**Logic:**
- Ensure the given node exists.
- Allocate the new node.
- Point new node’s `next` to given node’s `next`.
- Update given node’s `next` to the new node.

**Code:**
```c
void insertAfter(struct Node* prevNode, int newData) {
    if (prevNode == NULL) return;

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}
```

---

## Example Problem:

**Problem:** Start with an empty list. Insert 10 at the beginning, 20 at the end, and 15 after the first node. Display the list.

**Solution Output:**
```
10 -> 15 -> 20 -> NULL
```

---

**Time Complexity:**
- Beginning: $O(1)$  
- End: $O(n)$  
- After node: $O(1)$ (if pointer to previous node is known)

---
### Deletion in a Singly Linked List

Deletion refers to removing a node from the linked list. The three common cases are:

1. Deletion at the beginning  
2. Deletion at the end  
3. Deletion of a node with a specific value  

---

## 1. Deletion at the Beginning

**Logic:**
- Store the current head in a temporary pointer.
- Move `head` to the next node.
- Free the old head node.

**Code:**
```c
void deleteAtBeginning(struct Node** head) {
    if (*head == NULL) return;

    struct Node* temp = *head;
    *head = (*head)->next;
    free(temp);
}
```

---

## 2. Deletion at the End

**Logic:**
- Traverse to the second last node.
- Free the last node.
- Set second last node’s `next` to NULL.

**Code:**
```c
void deleteAtEnd(struct Node** head) {
    if (*head == NULL) return;

    struct Node *temp = *head;
    
    // Only one node
    if (temp->next == NULL) {
        free(temp);
        *head = NULL;
        return;
    }

    // Traverse to second last
    while (temp->next->next != NULL)
        temp = temp->next;

    free(temp->next);
    temp->next = NULL;
}
```

---

## 3. Deletion of a Node with Specific Value

**Logic:**
- Search for the node with the given key.
- If found, bypass it and free the memory.

**Code:**
```c
void deleteNode(struct Node** head, int key) {
    struct Node *temp = *head, *prev = NULL;

    // Head node holds the key
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }

    // Search for the key
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // Key not found
    if (temp == NULL) return;

    prev->next = temp->next;
    free(temp);
}
```

---

## Example Problem

**Problem:** Given list: `10 -> 15 -> 20`, delete the node with value 15.

**Result:**
```
10 -> 20 -> NULL
```

---

**Time Complexity:**
- Deletion at beginning: $O(1)$  
- Deletion at end or by key: $O(n)$

---
### Searching in a Singly Linked List

**Goal:** Find whether a given element exists in the list and, if so, return its position (index).

---

## Logic

- Start from the head node.
- Traverse each node one by one.
- Compare each node’s data with the search key.
- If found, return the index (starting from 0).
- If end is reached without finding, return -1 (not found).

---

## Code

```c
int search(struct Node* head, int key) {
    int index = 0;
    while (head != NULL) {
        if (head->data == key)
            return index;
        head = head->next;
        index++;
    }
    return -1;  // Not found
}
```

---

## Example Problem

**Given List:**  
`5 -> 10 -> 15 -> 20 -> NULL`

**Search Key:**  
`15`

**Output:**  
`2` (Because it is at the 2nd index if indexing starts from 0)

**Search Key:**  
`25`

**Output:**  
`-1` (Because it is not in the list)

---

## Time Complexity

- Best case (found early): $O(1)$  
- Worst case (not found or at end): $O(n)$

---
### Doubly Linked List

A **Doubly Linked List (DLL)** is a linear data structure where each node contains three parts:
- **Data**: The value stored.
- **Pointer to the previous node**.
- **Pointer to the next node**.

This allows traversal in both **forward and backward** directions.

---

## Structure of a Node in DLL

```c
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};
```

---

## Memory Representation

Each node has:
```
[prev | data | next] --> [prev | data | next] --> NULL
```

Example:
```
NULL <- [10] <-> [20] <-> [30] -> NULL
```

---

## Basic Operations

### 1. Insertion at the Beginning

```c
void insertAtFront(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->prev = NULL;
    newNode->next = *head;

    if (*head != NULL)
        (*head)->prev = newNode;

    *head = newNode;
}
```

### 2. Insertion at the End

```c
void insertAtEnd(struct Node** head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* last = *head;
    newNode->data = newData;
    newNode->next = NULL;

    if (*head == NULL) {
        newNode->prev = NULL;
        *head = newNode;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = newNode;
    newNode->prev = last;
}
```

---

### 3. Deletion of a Node

```c
void deleteNode(struct Node** head, struct Node* del) {
    if (*head == NULL || del == NULL) return;

    if (*head == del) *head = del->next;
    if (del->next != NULL) del->next->prev = del->prev;
    if (del->prev != NULL) del->prev->next = del->next;

    free(del);
}
```

---

## Example Problem

**Task:**  
Insert 10, 20, 30 at end.  
Insert 5 at front.  
Then delete 20.

### Output DLL:
```
5 <-> 10 <-> 30
```

---

## Time Complexities

| Operation         | Time Complexity |
|------------------|------------------|
| Insertion         | O(1) at beginning, O(n) at end |
| Deletion          | O(1) (if pointer to node given) |
| Traversal         | O(n) |

---
### Header Linked List

A **Header Linked List** is a variation of linked lists (singly or doubly) that contains a special **header node** at the beginning of the list.  
This header node **does not store user data** — it often stores metadata like the number of elements in the list or simply serves as a dummy node to simplify list operations.

---

### Structure of a Header Node

```c
struct Node {
    int data;
    struct Node* next;
};

// With header node:
struct HeaderList {
    int count;              // stores number of nodes in the list
    struct Node* head;      // points to the actual first node
};
```

---

### Advantages of Header Linked List
- Simplifies insertion and deletion operations by removing special cases for the head.
- Can store useful metadata (e.g., total node count) in the header node.
- Reduces edge case logic in linked list algorithms.

---

### Example: Inserting a node at the front

```c
void insertFront(struct HeaderList* list, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = list->head;
    list->head = newNode;
    list->count++;
}
```

---

### Example Use Case

- Suppose we want to store a list of 3 elements: 10 → 20 → 30  
- Initially, header node points to `NULL`, count is 0  
- After insertions:

```
Header Node → [10] → [20] → [30] → NULL
Count = 3
```

---

### Example Problem

**Task:** Use a header linked list to insert 3 values: 10, 20, 30. Print count.

**Solution Output:**
```
List: 10 -> 20 -> 30
Count: 3
```

---

### Time Complexities

| Operation     | Time Complexity |
|----------------|------------------|
| Insertion (Front) | O(1) |
| Insertion (End)   | O(n) |
| Deletion (Known node) | O(1) |
| Count Access      | O(1) (if maintained in header) |

---
### Circular Linked List

A **Circular Linked List (CLL)** is a variation of a linked list where the **last node points back to the first node**, forming a **circular structure**. This can be implemented as a **Singly Circular Linked List** or **Doubly Circular Linked List**.

---

### 1. Singly Circular Linked List

- Each node has two fields: `data` and `next`.
- The `next` of the last node points to the first node.

**Structure:**
```c
struct Node {
    int data;
    struct Node* next;
};
```

---

### Example Creation

```c
void createCircular(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    
    if (*head == NULL) {
        *head = newNode;
        newNode->next = *head;
    } else {
        struct Node* temp = *head;
        while (temp->next != *head)
            temp = temp->next;
        temp->next = newNode;
        newNode->next = *head;
    }
}
```

---

### 2. Doubly Circular Linked List

- Each node has three fields: `prev`, `data`, and `next`.
- The `next` of the last node points to the first node.
- The `prev` of the first node points to the last node.

---

### Advantages of Circular Linked List

- **Traversal is continuous** – can start from any node.
- No need to check for `NULL` during traversal.
- Suitable for applications like round-robin scheduling, music playlists, etc.

---

### Traversal Example (Singly)

```c
void display(struct Node* head) {
    if (head == NULL) return;
    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(back to head)\n");
}
```

---

### Example Problem

**Task:** Create a circular singly linked list with values 1, 2, 3, and display the list.

**Expected Output:**
```
1 -> 2 -> 3 -> (back to head)
```

---

### Time Complexities

| Operation     | Time Complexity |
|----------------|------------------|
| Insertion (Front/End) | O(n) |
| Deletion (Known node) | O(n) |
| Traversal              | O(n) |

---

# Unit -III  
### Searching, Sorting and Introduction to Non-Linear Data Structures-Graphs  
- Searching: Linear Search- Binary Search- Comparison of Linear and Binary Search.  
- Sorting:  Insertion Sort- Selection Sort- Bubble sort - Quick Sort- Merge Sort.  
- Non-linear structures: Introduction- Graphs: Introduction- Graph representations- Graph traversals: DFS-BFS- Graph applications.  

---
### 🔍 Searching: Linear Search

**Linear Search** is the simplest search algorithm. It checks each element of the list sequentially until the desired element is found or the list ends.

---

### **Algorithm:**

```c
int linearSearch(int arr[], int n, int key) {
    for(int i = 0; i < n; i++) {
        if(arr[i] == key)
            return i; // Key found at index i
    }
    return -1; // Key not found
}
```

---

### **Example:**

**Input:**
```
arr = [5, 3, 7, 2, 8], key = 2
```

**Output:**
```
Element found at index 3
```

---

### **Time Complexity:**

- **Best Case:** O(1) → if the element is at the beginning
- **Average Case:** O(n)
- **Worst Case:** O(n)

---

### **Space Complexity:**

- O(1) → No extra space required

---

### **Use Cases:**

- Useful for small or unsorted lists.
- No assumptions about order.

---
### 🔍 Searching: Binary Search

**Binary Search** is an efficient algorithm for finding an item from a **sorted** list by repeatedly dividing the search interval in half.

---

### **Algorithm (Iterative):**

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;

    while(low <= high) {
        int mid = (low + high) / 2;

        if(arr[mid] == key)
            return mid;
        else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1; // Key not found
}
```

---

### **Example:**

**Input:**
```
arr = [2, 4, 6, 8, 10, 12], key = 8
```

**Steps:**
- mid = (0 + 5) / 2 = 2 → arr[2] = 6 < 8 → search right
- mid = (3 + 5) / 2 = 4 → arr[4] = 10 > 8 → search left
- mid = (3 + 3) / 2 = 3 → arr[3] = 8 → match found!

**Output:**
```
Element found at index 3
```

---

### **Time Complexity:**

- **Best Case:** O(1) → middle element is the key
- **Average/Worst Case:** O(log n)

---

### **Space Complexity:**

- O(1) for iterative version
- O(log n) for recursive version (due to call stack)

---

### **Key Points:**

- Array must be **sorted**.
- Much faster than linear search on large datasets.

---
### 🔍 Comparison of Linear and Binary Search

| **Criteria**             | **Linear Search**                              | **Binary Search**                             |
|--------------------------|------------------------------------------------|-----------------------------------------------|
| **Pre-requisite**        | Works on **unsorted** or sorted data           | Works only on **sorted** data                 |
| **Time Complexity**      | O(n) in worst case                             | O(log n) in worst case                        |
| **Best Case**            | O(1) – if element is at the beginning          | O(1) – if element is at the middle            |
| **Space Complexity**     | O(1)                                           | O(1) iterative, O(log n) recursive            |
| **Implementation**       | Easier to implement                            | Slightly more complex                         |
| **Efficiency**           | Less efficient for large datasets              | Very efficient for large sorted datasets      |
| **Performance**          | Slower as n increases                          | Faster as n increases                         |

---

### 🔢 Example Comparison

Suppose we want to search for the number `30` in the array:

**Array (Unsorted):**  
`[15, 3, 10, 30, 22, 45, 8]`  
- Linear Search: Can find `30` directly, as sorting is not needed.  
- Binary Search: **Cannot be used** unless array is sorted.

**Array (Sorted):**  
`[3, 8, 10, 15, 22, 30, 45]`  
- Linear Search: May still take many steps.
- Binary Search: Quickly finds `30` by halving search space.

---

### 💡 Summary

- Use **Linear Search** for small or unsorted datasets.
- Use **Binary Search** for large sorted datasets.

---
### 🧹 Sorting Algorithms

---

### 1. **Insertion Sort**

**Idea:**  
Build the sorted array one item at a time by picking elements and placing them at the correct position.

**Steps:**  
1. Assume first element is already sorted.  
2. Take next element and compare with all elements in the sorted part.  
3. Shift all greater elements one position to the right.  
4. Insert the current element in correct position.

**Example:**

Unsorted Array: `[5, 2, 4, 6, 1, 3]`

- Pass 1: `[2, 5, 4, 6, 1, 3]`  
- Pass 2: `[2, 4, 5, 6, 1, 3]`  
- Pass 3: `[2, 4, 5, 6, 1, 3]`  
- Pass 4: `[1, 2, 4, 5, 6, 3]`  
- Pass 5: `[1, 2, 3, 4, 5, 6]`

**Time Complexity:**  
- Best: O(n)  
- Worst: O(n²)  
- Space: O(1)

---

### 2. **Selection Sort**

**Idea:**  
Repeatedly pick the smallest (or largest) element and place it at the beginning.

**Steps:**  
1. Find the minimum element in the unsorted part.  
2. Swap it with the first unsorted element.  
3. Move the boundary of sorted/unsorted part.

**Example:**

Unsorted Array: `[64, 25, 12, 22, 11]`

- Pass 1: `[11, 25, 12, 22, 64]`  
- Pass 2: `[11, 12, 25, 22, 64]`  
- Pass 3: `[11, 12, 22, 25, 64]`  
- Pass 4: `[11, 12, 22, 25, 64]`

**Time Complexity:**  
- Best, Average, Worst: O(n²)  
- Space: O(1)

---

### 3. **Bubble Sort**

**Idea:**  
Repeatedly swap adjacent elements if they are in wrong order.

**Steps:**  
1. Compare adjacent elements.  
2. Swap if needed.  
3. Largest bubble to the end in each pass.

**Example:**

Unsorted Array: `[5, 1, 4, 2, 8]`

- Pass 1: `[1, 4, 2, 5, 8]`  
- Pass 2: `[1, 2, 4, 5, 8]`  
- Pass 3: `[1, 2, 4, 5, 8]`

**Time Complexity:**  
- Best: O(n) (if optimized)  
- Worst: O(n²)  
- Space: O(1)

---
### ⚡ Quick Sort

---

**Idea:**  
Quick Sort is a **divide-and-conquer** algorithm. It picks a "pivot" element and partitions the array into two halves:  
- Elements less than the pivot  
- Elements greater than the pivot  
Then, it recursively sorts the sub-arrays.

---

### **Steps:**

1. Pick a pivot (e.g., last element).
2. Partition the array:
   - All elements smaller than pivot go to left.
   - All greater go to right.
3. Recursively apply to left and right subarrays.

---

### **Example:**

Unsorted: `[10, 80, 30, 90, 40, 50, 70]`  
Pivot = 70 → Partition → `[10, 30, 40, 50] 70 [90, 80]`  
Recursively sort both sides.

---

### **Time Complexity:**

- Best & Avg Case: O(n log n)  
- Worst Case (sorted/reverse): O(n²)  
- Space: O(log n) due to recursion

---

### ✅ **C Code for Quick Sort (Turbo C Compatible)**

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // last element as pivot
    int i = (low - 1); // index of smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high); // partition index
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");
    printArray(arr, n);
}
```

---
### 🧩 Merge Sort

---

**Concept:**  
Merge Sort is a **stable**, comparison-based, **divide-and-conquer** sorting algorithm.  
It divides the array into two halves, sorts them, and **merges** the sorted halves.

---

### **Steps:**

1. Divide array into two halves recursively until each sub-array has one element.
2. Merge the sub-arrays in a sorted manner.

---

### **Example:**

Unsorted: `[38, 27, 43, 3, 9, 82, 10]`  
Divide: `[38, 27, 43]` and `[3, 9, 82, 10]`  
Keep dividing → Merge back sorted.

---

### **Time Complexity:**

- Best, Average, Worst: **O(n log n)**  
- Space: **O(n)** (uses auxiliary array)

---

### ✅ **C Code for Merge Sort (Turbo C Compatible)**

```c
#include <stdio.h>

void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // create temp arrays
    int L[50], R[50]; // assume max size 50

    // copy data to temp arrays
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // merge temp arrays back into arr[l..r]
    i = 0; j = 0; k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    // copy remaining elements
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;

        mergeSort(arr, l, m);    // sort first half
        mergeSort(arr, m + 1, r); // sort second half

        merge(arr, l, m, r);
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\n");
}

void main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("Sorted array: ");
    printArray(arr, arr_size);
}
```

---

### 🌐 Introduction to Graphs

---

**Definition:**  
A **graph** is a **non-linear** data structure consisting of **nodes (vertices)** and **edges (connections)** between them.

---

### 🧱 Basic Terminology:

| Term           | Description                                           |
|----------------|-------------------------------------------------------|
| **Vertex (Node)** | Fundamental unit of a graph                           |
| **Edge**         | Connection between two vertices                        |
| **Undirected Graph** | Edges have no direction                            |
| **Directed Graph (Digraph)** | Edges have direction (A → B)                |
| **Weighted Graph** | Edges have weights or costs (e.g., distances)        |
| **Adjacency**    | Two nodes are adjacent if they share an edge          |
| **Degree**       | Number of edges incident to a vertex                  |
| **Path**         | Sequence of edges connecting a sequence of vertices   |
| **Cycle**        | A path that starts and ends at the same vertex        |

---

### 📊 Types of Graphs:

- **Simple Graph** – No loops or multiple edges
- **Multi Graph** – May have multiple edges between vertices
- **Complete Graph** – Every vertex connected to every other
- **Connected Graph** – There’s a path between every pair of vertices
- **Cyclic / Acyclic Graphs** – Graphs with or without cycles
- **Directed Acyclic Graph (DAG)** – No cycles & edges have direction

---

### 🏗 Graph Representation:

1. **Adjacency Matrix**
   - 2D array `G[V][V]`
   - `G[i][j] = 1` if edge from vertex i to j
   - Space: O(V²)
2. **Adjacency List**
   - Array of linked lists or arrays
   - Space efficient: O(V + E)

---

### ✅ Example – Undirected Graph

```
A ----- B
|     / |
|   /   |
C ----- D
```

- Vertices: A, B, C, D
- Edges: (A-B), (A-C), (B-D), (B-C), (C-D)

---

### 🔢 Adjacency Matrix (Undirected)

|     | A | B | C | D |
|-----|---|---|---|---|
| **A** | 0 | 1 | 1 | 0 |
| **B** | 1 | 0 | 1 | 1 |
| **C** | 1 | 1 | 0 | 1 |
| **D** | 0 | 1 | 1 | 0 |

---

### 🧠 Use-Cases:

- Maps and Navigation Systems
- Social Networks
- Networking and Routing
- Scheduling (DAGs)

---
### 🔍 Graph Traversals: DFS and BFS

---

Graph traversal means **visiting all the vertices** of a graph in a systematic manner.

Two popular methods:
- **DFS (Depth First Search)**
- **BFS (Breadth First Search)**

---

## 🔁 Depth First Search (DFS)

### 🧠 Idea:
Explore as far as possible along each branch before backtracking.

### 🧾 Algorithm (Recursive):
1. Mark the current node as visited.
2. Visit all the unvisited adjacent nodes recursively.

### ✅ Code (C – Using Adjacency Matrix):
```c
#include <stdio.h>

int graph[10][10], visited[10], n;

void DFS(int v) {
    printf("%d ", v);
    visited[v] = 1;
    for(int i = 0; i < n; i++) {
        if(graph[v][i] && !visited[i])
            DFS(i);
    }
}

int main() {
    int i, j;
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);

    for(i = 0; i < n; i++) visited[i] = 0;

    printf("DFS Traversal: ");
    DFS(0);
    return 0;
}
```

---

## 🔁 Breadth First Search (BFS)

### 🧠 Idea:
Explore all the neighbors at the current depth before moving to the next depth.

### ✅ Code (C – Using Queue and Adjacency Matrix):
```c
#include <stdio.h>

int graph[10][10], visited[10], queue[10], front = -1, rear = -1, n;

void enqueue(int v) {
    if(rear == 9) return;
    if(front == -1) front = 0;
    queue[++rear] = v;
}

int dequeue() {
    if(front == -1 || front > rear) return -1;
    return queue[front++];
}

void BFS(int v) {
    int i;
    enqueue(v);
    visited[v] = 1;

    while(front <= rear) {
        v = dequeue();
        printf("%d ", v);

        for(i = 0; i < n; i++) {
            if(graph[v][i] && !visited[i]) {
                enqueue(i);
                visited[i] = 1;
            }
        }
    }
}

int main() {
    int i, j;
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);

    for(i = 0; i < n; i++) visited[i] = 0;

    printf("BFS Traversal: ");
    BFS(0);
    return 0;
}
```

---

### 🔄 DFS vs BFS Comparison:

| Feature       | DFS                      | BFS                      |
|---------------|---------------------------|---------------------------|
| Strategy      | Depth (go deep first)     | Breadth (level-by-level) |
| Uses          | Stack or Recursion        | Queue                    |
| Memory        | Less                      | More                     |
| Use Case      | Topological Sort, Cycle Detection | Shortest Path in unweighted graph |

---
### 📌 Graph Applications

Graphs are incredibly versatile structures used in many real-world and theoretical applications.

---

### 1. **Shortest Path Finding**

- **Dijkstra’s Algorithm** (for weighted graphs with non-negative edges)
- **BFS** (for unweighted graphs)

**Example:**
- Finding the shortest route in Google Maps.

---

### 2. **Cycle Detection**

- **DFS** helps detect cycles in directed and undirected graphs.

**Applications:**
- Deadlock detection in OS
- Verifying dependency graphs (e.g., software build tools)

---

### 3. **Topological Sorting**

- Applies to **Directed Acyclic Graphs (DAGs)**.
- Used in **task scheduling**, **build systems**, etc.

---

### 4. **Minimum Spanning Tree (MST)**

- Algorithms: **Prim’s**, **Kruskal’s**
- Connect all nodes with minimum total edge weight.

**Use Case:**
- Network design (LAN, electrical wiring)

---

### 5. **Network Flow (Max Flow Problem)**

- **Ford-Fulkerson algorithm**
- Used in resource allocation problems, traffic routing, etc.

---

### 6. **Social Network Analysis**

- Nodes = Users, Edges = Connections
- Used in friend suggestions, influencer analysis

---

### 7. **Web Crawling**

- Uses **BFS** to crawl websites starting from a seed URL.

---

### 8. **Maps and Navigation Systems**

- Graphs represent cities and roads
- Algorithms like **A\*** and **Dijkstra** power route finding

---

### 9. **Electrical Circuits & Chip Design**

- Components and connections are modeled using graphs.

---

### 10. **Recommendation Systems**

- Collaborative filtering using graph structures

---

### Example Problem: Shortest Path in Unweighted Graph

#### Problem:
Find the shortest path from node 0 to all other nodes in an unweighted graph.

#### Code (Using BFS):
```c
#include <stdio.h>

#define INF 9999

int graph[10][10], distance[10], visited[10], n;

void BFS(int start) {
    int queue[10], front = 0, rear = 0;
    queue[rear++] = start;
    visited[start] = 1;
    distance[start] = 0;

    while (front < rear) {
        int node = queue[front++];
        for (int i = 0; i < n; i++) {
            if (graph[node][i] && !visited[i]) {
                distance[i] = distance[node] + 1;
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    printf("Enter number of nodes: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &graph[i][j]);

    for (int i = 0; i < n; i++) {
        visited[i] = 0;
        distance[i] = INF;
    }

    BFS(0);

    printf("Shortest distance from node 0:\n");
    for (int i = 0; i < n; i++)
        printf("To %d = %d\n", i, distance[i]);

    return 0;
}
```

---

# Unit -IV  
### Trees and Heaps  
- Trees:  Trees and its representation-Binary Tree- Types of Binary Trees.  
- Binary tree traversals- Binary Search Tree- B Tree- AVL tree - Threaded Binary tree- Red-Black trees - Properties of Red Black trees- Applications of trees.  
- Heaps: Introduction about heap structure - max and min heap-Applications of Heap data structure.  

---
### **Trees and Its Representation**

---

#### **What is a Tree?**
A **tree** is a non-linear, hierarchical data structure consisting of **nodes** connected by **edges**. It has the following properties:
- One node is designated as the **root**.
- Every other node is connected by a **single path** from the root.
- Each node can have **zero or more children**.
- A node with no children is called a **leaf**.

---

#### **Terminology**
- **Root**: The topmost node.
- **Parent/Child**: A node connected directly above/below another.
- **Siblings**: Nodes sharing the same parent.
- **Leaf**: Node with no children.
- **Level**: Depth from root (root is level 0).
- **Height**: Longest path from root to any leaf.
- **Degree**: Number of children a node has.

---

### **Tree Representation**

There are mainly two ways to represent a tree in memory:

---

#### **1. Using Linked Representation (Node-based)**

Each node contains:
- Data
- Pointer to left child
- Pointer to right child

```c
struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};
```

---

#### **2. Using Array Representation**

Only efficient for complete binary trees.

- Root is stored at index 0.
- Left child of node at index `i` is at `2i + 1`
- Right child is at `2i + 2`
- Parent is at `(i - 1) / 2`

---

### **Example Problem: Create a Binary Tree (Linked Representation)**

```c
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode *left, *right;
};

struct TreeNode* createNode(int value) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

int main() {
    struct TreeNode* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    printf("Root Node: %d\n", root->data);
    printf("Left Child of Root: %d\n", root->left->data);
    printf("Right Child of Root: %d\n", root->right->data);

    return 0;
}
```

---
### **Binary Tree and Types of Binary Trees**

---

#### **What is a Binary Tree?**

A **Binary Tree** is a special type of tree in which each node has at most **two children**, referred to as the **left child** and **right child**.

---

### **Types of Binary Trees**

---

#### **1. Full Binary Tree**
- Every node has either 0 or 2 children.
- No node has only one child.

**Example:**
```
      1
     / \
    2   3
```

---

#### **2. Complete Binary Tree**
- All levels are completely filled except possibly the last level.
- Nodes in the last level are as far left as possible.

**Example:**
```
      1
     / \
    2   3
   / \
  4   5
```

---

#### **3. Perfect Binary Tree**
- All internal nodes have 2 children.
- All leaf nodes are at the same level.

**Example:**
```
      1
     / \
    2   3
   / \ / \
  4  5 6  7
```

---

#### **4. Degenerate (or Skewed) Binary Tree**
- Each node has only one child.
- Can be **left-skewed** or **right-skewed**.

**Left Skewed:**
```
    1
   /
  2
 /
3
```

**Right Skewed:**
```
1
 \
  2
   \
    3
```

---

#### **5. Balanced Binary Tree**
- Height of the tree is minimal.
- Left and right subtrees differ in height by at most one.

---

### **Example Problem: Check if a Tree is Full Binary Tree**

```c
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* createNode(int data) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

int isFullBinaryTree(struct TreeNode* root) {
    if (root == NULL)
        return 1;

    if (root->left == NULL && root->right == NULL)
        return 1;

    if (root->left && root->right)
        return isFullBinaryTree(root->left) && isFullBinaryTree(root->right);

    return 0;
}

int main() {
    struct TreeNode* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    if (isFullBinaryTree(root))
        printf("The tree is a full binary tree.\n");
    else
        printf("The tree is NOT a full binary tree.\n");

    return 0;
}
```

---
### **Binary Tree Traversals**

Tree traversal means visiting every node in a tree exactly once in a systematic way. There are two main types of binary tree traversals:

---

### **1. Depth-First Traversal (DFS)**  
- **Inorder (Left, Root, Right)**  
- **Preorder (Root, Left, Right)**  
- **Postorder (Left, Right, Root)**  

---

#### **Example Tree**
```
        1
       / \
      2   3
     / \
    4   5
```

**Inorder Traversal:** 4 2 5 1 3  
**Preorder Traversal:** 1 2 4 5 3  
**Postorder Traversal:** 4 5 2 3 1  

---

### **2. Breadth-First Traversal (Level Order)**  
- Visit nodes level by level using a queue.

---

### **C Program for Tree Traversals**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

// Inorder traversal
void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Preorder traversal
void preorder(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Postorder traversal
void postorder(struct Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

int main() {
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);

    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");

    printf("Preorder traversal: ");
    preorder(root);
    printf("\n");

    printf("Postorder traversal: ");
    postorder(root);
    printf("\n");

    return 0;
}
```

---
### **Binary Search Tree (BST)**

A **Binary Search Tree** is a binary tree where each node has a key, and:

- The **left subtree** of a node contains only nodes with keys **less than** the node’s key.
- The **right subtree** contains only nodes with keys **greater than** the node’s key.
- Both subtrees must also be binary search trees.

---

### **Basic Operations**

1. **Insertion**
2. **Searching**
3. **Deletion**

---

### **Example Tree**

Let's insert the following numbers in this order: `50, 30, 70, 20, 40, 60, 80`

Resulting BST:
```
        50
       /  \
     30    70
    / \    / \
  20  40  60  80
```

---

### **C Program for Insertion and Inorder Traversal**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

// Insertion in BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) return newNode(data);

    if (data < root->data)
        root->left = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data);

    return root;
}

// Inorder Traversal
void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

int main() {
    struct Node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    printf("Inorder traversal of BST: ");
    inorder(root);
    printf("\n");

    return 0;
}
```

---
### **B-Trees**

A **B-Tree** is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in **logarithmic time**.

It is commonly used in databases and file systems due to its ability to minimize disk access.

---

### **Properties of B-Trees**

Let **t** be the minimum degree (order) of the B-Tree.

1. Every node has at most **2t - 1** keys and **2t** children.
2. Every node (except root) has at least **t - 1** keys.
3. The root has at least **1** key.
4. All leaves appear on the same level.
5. Keys in a node are sorted in increasing order.

---

### **Why Use B-Trees?**

- Binary search trees can become skewed and degenerate to linked lists.
- B-Trees keep height small even for large amounts of data.
- Efficient for **disk-based** and **database systems** where data access cost is high.

---

### **Simple Diagram of B-Tree (t = 2)**

```
Insert: 10, 20, 5, 6, 12, 30, 7, 17

Resulting B-tree:
         [10, 20]
        /   |   \
    [5,6,7] [12,17] [30]
```

Each internal node has 1 to 3 keys and 2 to 4 children.

---

### **Basic Operations**

1. **Search** – similar to binary search.
2. **Insert** – insert in a node; if full, split.
3. **Delete** – delete key; may cause merging or borrowing.

---

### **Applications of B-Trees**

- File systems (e.g., NTFS, ext4)
- Database indexing (MySQL, Oracle)
- Multilevel indexing in search engines

---
### **AVL Tree (Adelson-Velsky and Landis Tree)**

An **AVL Tree** is a self-balancing binary search tree where the difference in heights of left and right subtrees (balance factor) is maintained to be **–1, 0, or +1** for every node.

---

### **Key Properties**

- Each node stores an extra **balance factor**:
  - `balance = height(left subtree) - height(right subtree)`
- If the balance factor becomes less than –1 or more than +1, **rebalancing** is done using rotations.

---

### **Rotations in AVL Tree**

There are **4 types of rotations** used to rebalance:

1. **Right Rotation (RR Rotation)** – for Left-Left imbalance
2. **Left Rotation (LL Rotation)** – for Right-Right imbalance
3. **Left-Right Rotation (LR Rotation)** – for Left-Right imbalance
4. **Right-Left Rotation (RL Rotation)** – for Right-Left imbalance

---

### **Example of RR Rotation**

Inserting nodes: 30 → 20 → 10

Before rotation:
```
      30
     /
   20
  /
10
```

After RR Rotation:
```
    20
   /  \
 10   30
```

---

### **Time Complexities**

| Operation | Time Complexity |
|-----------|------------------|
| Search    | O(log n)         |
| Insert    | O(log n)         |
| Delete    | O(log n)         |

---

### **Example Problem**

**Insert the elements 10, 20, 30 into an AVL Tree**

**Step-by-step**:
1. Insert 10 → no imbalance.
2. Insert 20 → no imbalance.
3. Insert 30 → Right-Right case → Left Rotation needed at 10.

Final tree:
```
    20
   /  \
 10   30
```

---

### **Advantages of AVL Trees**

- Guarantees **logarithmic height**.
- Faster lookup than unbalanced BST.
- Useful in memory-constrained and performance-critical applications.

---
### **Threaded Binary Tree**

A **Threaded Binary Tree** is a binary tree variant that makes **inorder traversal faster and avoids recursion or stack usage** by using otherwise NULL pointers to point to inorder predecessor or successor.

---

### **Why Use Threaded Binary Trees?**

In a standard binary tree, many left and right pointers are `NULL`. Threaded binary trees use these null pointers to form **threads**, which link to **inorder predecessor or successor**.

---

### **Types of Threaded Binary Trees**

1. **Single Threaded**
   - Each node is threaded towards either:
     - **Inorder predecessor** (left thread), or
     - **Inorder successor** (right thread)

2. **Double Threaded**
   - Each node has threads for both **inorder predecessor and successor**

---

### **Structure of a Threaded Node**

```c
struct Node {
    int data;
    Node *left, *right;
    bool lthread; // true if left pointer is a thread
    bool rthread; // true if right pointer is a thread
};
```

---

### **Advantages of Threaded Binary Tree**

- Inorder traversal without stack or recursion
- Saves memory and increases traversal speed
- Efficient for applications with frequent traversals

---

### **Inorder Traversal (Threaded Tree)**

```c
void inorder(Node* root) {
    Node* current = leftmost(root);
    while (current != NULL) {
        printf("%d ", current->data);
        if (current->rthread)
            current = current->right;
        else
            current = leftmost(current->right);
    }
}

Node* leftmost(Node* node) {
    if (!node) return NULL;
    while (!node->lthread)
        node = node->left;
    return node;
}
```

---

### **Use Case**

- Efficient memory usage in constrained systems
- Ideal for interpreters, expression trees, and compilers

---
### **Red-Black Trees**

A **Red-Black Tree** is a type of **self-balancing binary search tree** where each node stores an extra bit representing “color” (either **Red** or **Black**) to ensure the tree remains balanced during insertions and deletions.

---

### **Properties of Red-Black Trees**

1. Each node is either **Red** or **Black**
2. The **root** is always **Black**
3. All **leaves** (NULLs) are **Black**
4. If a node is **Red**, then **both children must be Black** (no two reds in a row)
5. **Every path from a node to its descendant leaves** must have the **same number of Black nodes**

These rules ensure the tree height remains logarithmic, guaranteeing **O(log n)** time for search, insert, and delete.

---

### **Structure of a Red-Black Tree Node (C code)**

```c
typedef enum { RED, BLACK } Color;

typedef struct Node {
    int data;
    Color color;
    struct Node *left, *right, *parent;
} Node;
```

---

### **Operations in Red-Black Tree**

#### 1. **Insertion**
- New node is always inserted as **Red**
- Violations (like two reds in a row) are fixed using **rotations** and **recoloring**

#### 2. **Deletion**
- More complex than insertion
- Re-balancing is done to maintain Red-Black properties

#### 3. **Rotations**
Used to maintain balance:
- **Left Rotation**
- **Right Rotation**

---

### **Left Rotation Example (C)**

```c
void leftRotate(Node **root, Node *x) {
    Node *y = x->right;
    x->right = y->left;

    if (y->left != NULL)
        y->left->parent = x;

    y->parent = x->parent;

    if (x->parent == NULL)
        *root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    y->left = x;
    x->parent = y;
}
```

---

### **Advantages of Red-Black Tree**

- **Balanced BST** with guaranteed `O(log n)` time for search, insert, and delete
- Widely used in STL (`map`, `set`), Java's `TreeMap`, and Linux kernel memory management

---

### **Use Case Example:**
Suppose you insert: 10, 20, 30, 15  
- After every insert, Red-Black properties are rechecked  
- Rotations/recoloring are applied to maintain balance  

---
### **Applications of Trees**

Trees, especially binary and specialized trees like AVL and Red-Black trees, have a wide range of practical applications in computer science and real-world systems:

---

#### 1. **Hierarchical Data Representation**
- Trees naturally represent data with a hierarchy.
- **Examples**:
  - File systems (directories and files)
  - XML and JSON data parsing
  - Organizational charts
  - DOM in web browsers

---

#### 2. **Searching and Sorting**
- Binary Search Trees (BSTs), AVL Trees, and Red-Black Trees provide efficient **search, insert, and delete** operations in **O(log n)** time.
- Used in:
  - Symbol tables in compilers
  - Indexing in databases

---

#### 3. **Routing and Network Algorithms**
- Tree-based structures are used in:
  - Routing algorithms (like spanning trees)
  - Broadcast networks
  - IP routing (tries, prefix trees)

---

#### 4. **Heaps in Priority Queues**
- Used in:
  - Task scheduling (OS schedulers)
  - Dijkstra’s algorithm for shortest path
  - Heap Sort

---

#### 5. **Expression Parsing**
- Expression trees are used to evaluate mathematical expressions.
- **Applications**:
  - Calculators
  - Compilers (syntax trees)

---

#### 6. **Decision Trees**
- Machine learning uses decision trees for classification and regression.
- Nodes represent tests, branches represent outcomes, leaves represent labels or results.

---

#### 7. **Tries (Prefix Trees)**
- Special kind of tree used for fast retrieval of strings.
- Applications:
  - Auto-completion
  - Spell checkers
  - IP routing

---

#### 8. **Games and AI**
- Game trees (like minimax trees) are used in decision-making systems for AI.
- Helps evaluate all possible moves and choose the optimal one.

---

#### 9. **Memory Allocation**
- Trees are used in dynamic memory allocation systems to track free/used memory blocks.

---

#### 10. **Databases**
- B-Trees and B+ Trees are widely used in database indexing due to their efficiency in disk-based storage systems.

---
### **Heaps: Introduction and Structure**

---

#### **What is a Heap?**

A **heap** is a specialized tree-based data structure that satisfies the **heap property**:
- **Max-Heap**: Parent node is **greater than or equal** to its children.
- **Min-Heap**: Parent node is **less than or equal** to its children.

---

#### **Characteristics of a Heap**
- It is a **complete binary tree** (every level is filled except possibly the last, and nodes are as far left as possible).
- Stored efficiently using **arrays**.
- No ordering between siblings is required—only the parent-child relationship matters.

---

#### **Array Representation of a Heap**
Given a node at index `i`:
- **Left child** = `2*i`
- **Right child** = `2*i + 1`
- **Parent** = `i/2` (floor)

*Note*: Indexing usually starts at **1** for heap implementation.

---

#### **Example: Max-Heap**
```
        50
       /  \
     30    40
    /  \   /
  10   5  20
```
Array Representation: `[50, 30, 40, 10, 5, 20]`

---

#### **Operations on Heap**
1. **Insert**: Add the new element at the end and "heapify up".
2. **Delete Max/Min**: Replace root with last element, delete it, and "heapify down".
3. **Peek**: Return root without removing it.

---

#### **Code: Insert into a Max Heap**

```c
#include <stdio.h>

void heapifyUp(int heap[], int index) {
    int parent = (index - 1) / 2;
    if (index > 0 && heap[index] > heap[parent]) {
        int temp = heap[index];
        heap[index] = heap[parent];
        heap[parent] = temp;
        heapifyUp(heap, parent);
    }
}

void insert(int heap[], int *size, int value) {
    heap[*size] = value;
    (*size)++;
    heapifyUp(heap, *size - 1);
}

void printHeap(int heap[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {
    int heap[100];
    int size = 0;
    
    insert(heap, &size, 50);
    insert(heap, &size, 30);
    insert(heap, &size, 40);
    insert(heap, &size, 10);
    insert(heap, &size, 5);
    insert(heap, &size, 20);
    
    printHeap(heap, size);
    return 0;
}
```

**Output**:
```
50 30 40 10 5 20
```

---
### **Max Heap and Min Heap**

---

#### **Max Heap**

- In a **Max Heap**, the value of the **parent node is greater than or equal to** the value of its children.
- The **maximum value** is always stored at the **root**.
- Used in **priority queues**, **heap sort**, etc.

**Example:**

```
         90
        /  \
      80    70
     / \   /
    50 60 65
```

Array: `[90, 80, 70, 50, 60, 65]`

---

#### **Min Heap**

- In a **Min Heap**, the value of the **parent node is less than or equal to** the value of its children.
- The **minimum value** is always at the **root**.
- Used in **Dijkstra's algorithm**, **Huffman encoding**, etc.

**Example:**

```
         10
        /  \
      20    15
     / \   /
   40  25 30
```

Array: `[10, 20, 15, 40, 25, 30]`

---

#### **Comparison Table**

| Feature        | Max Heap              | Min Heap              |
|----------------|------------------------|------------------------|
| Root Node      | Maximum element         | Minimum element         |
| Usage          | Heap Sort, Priority Queue | Dijkstra, Prim, etc.    |
| Structure      | Complete Binary Tree     | Complete Binary Tree     |
| Insertion      | Bubble up                | Bubble up                |
| Deletion       | Bubble down              | Bubble down              |

---

#### **C Code: Convert an Array into a Min-Heap**

```c
#include <stdio.h>

void heapifyDown(int heap[], int n, int i) {
    int smallest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < n && heap[left] < heap[smallest])
        smallest = left;

    if (right < n && heap[right] < heap[smallest])
        smallest = right;

    if (smallest != i) {
        int temp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = temp;
        heapifyDown(heap, n, smallest);
    }
}

void buildMinHeap(int heap[], int n) {
    for (int i = n/2 - 1; i >= 0; i--)
        heapifyDown(heap, n, i);
}

void printHeap(int heap[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {
    int heap[] = {40, 10, 30, 50, 20, 60};
    int n = sizeof(heap)/sizeof(heap[0]);

    buildMinHeap(heap, n);
    printHeap(heap, n);
    return 0;
}
```

**Output:**
```
10 20 30 50 40 60
```

---
### **Applications of Heap Data Structure**

---

Heaps, particularly Min-Heaps and Max-Heaps, are widely used in various computing problems due to their efficient performance characteristics. Below are the major applications:

---

#### **1. Priority Queues**

- **Heaps** are the most efficient structure to implement **priority queues**.
- In a priority queue, each element is associated with a priority, and elements are served based on their priority.
- **Max-Heap** is used when higher priority means higher value.
- **Min-Heap** is used when lower value has higher priority.

---

#### **2. Heap Sort**

- An efficient **comparison-based sorting algorithm**.
- Process:
  - Build a Max-Heap.
  - Repeatedly remove the root (maximum element) and rebuild the heap.
- Time Complexity: **O(n log n)**

---

#### **3. Dijkstra's Shortest Path Algorithm**

- **Min-Heap** is used to find the node with the **minimum tentative distance** efficiently.
- Allows fast extraction of the minimum and updating key values.

---

#### **4. Prim’s Minimum Spanning Tree**

- Similar to Dijkstra, **Min-Heap** helps in selecting the minimum weight edge efficiently.

---

#### **5. Job Scheduling Algorithms**

- Jobs with **higher priority** can be scheduled using a **Max-Heap**.
- Useful in **Operating Systems** for **process management**.

---

#### **6. Median Maintenance**

- You can use **two heaps** (Min-Heap & Max-Heap) to dynamically calculate the **median** of a stream of numbers.
- Max-Heap stores the smaller half, and Min-Heap stores the larger half.

---

#### **7. K'th Largest or Smallest Element in an Array**

- Use a **heap of size k** to find the k-th largest or smallest element in **O(n log k)** time.

---

#### **8. Heap-based Data Structures**

- **Binomial Heap**, **Fibonacci Heap**, **Pairing Heap**, etc. are advanced heap structures used in more optimized algorithms.

---

#### **9. Event Simulation Systems**

- Simulations use heaps to efficiently **process events** in chronological order (based on timestamps).

---

#### **10. Huffman Encoding**

- **Min-Heap** is used to build **Huffman Trees** for **lossless data compression**.

---

