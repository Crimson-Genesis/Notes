## 🗺️ Roadmap of the topics.

1. **Address-of and dereference operators**
2. **Array ↔ pointer relationship**
3. **Double pointers**
4. **Function pointers**
5. **`typedef` usage**
6. **File I/O (text + binary)**
7. **Unions and shared memory**
8. **Preprocessor directives**
9. **Header guards**
10. **Storage-class specifiers** (`const`, `volatile`, `static`, `extern`)
11. **Segmentation faults, stack vs. heap**
12. **Memory leaks and `valgrind`**
13. **String manipulation (manual & `<string.h>`)**
14. **Hash tables (concept + C implementation)**
15. **Build systems, linking multiple objects**
16. **How C maps to assembly, stack frames, calling conventions**
17. **Undefined behavior & C standard model**
18. **Memory alignment & struct padding**
19. **Inline assembly**
20. **Low-level I/O and POSIX system calls**
21. **Signals, fork/exec, and processes**
22. **Threads, concurrency, race conditions**
23. **Networking (sockets)**
24. **Dynamic libraries (`dlopen`, `dlsym`)**
25. **Makefiles & compiler optimization flags**
26. **Profiling tools** (`gprof`, `perf`, `valgrind --tool=cachegrind`)
27. **Custom allocators & manual optimizations**
28. **Inline functions, macros for performance**
29. **Portability & standards (C89 → C23)**
30. **Writing libraries & defensive programming**
31. **Unit testing frameworks**

---
---

# 🧠 Compact C Mastery Reference

*(For someone who’s already comfortable coding in C)*

---

### 1️⃣ Address-of (`&`) and Dereference (`*`)

* **What:** `&` gives you the memory address of a variable; `*` gives you the value stored at an address.
* **Why:** Pointers are just variables holding addresses — these two operators are the key to manipulating them.
* **Example:**

  ```c
  int x = 5; 
  int *p = &x;   // address-of
  printf("%d", *p); // dereference → 5
  ```

---

### 2️⃣ Array ↔ Pointer Relationship

* **What:** In most contexts, an array name “decays” to a pointer to its first element.
* **Why:** Explains why `arr[i] == *(arr + i)`.
* **Example:**

  ```c
  int a[3] = {1,2,3};
  int *p = a;  // same as &a[0]
  ```

---

### 3️⃣ Double Pointers

* **What:** A pointer to another pointer (`int **pp`).
* **Why:** Used for dynamic 2D arrays, modifying a pointer in a function, or holding lists of strings.
* **Example:**

  ```c
  int *p, **pp = &p;
  ```

---

### 4️⃣ Function Pointers

* **What:** Variable storing the address of a function.
* **Why:** Enables callbacks, plugin systems, and dynamic dispatch.
* **Example:**

  ```c
  int add(int a,int b){return a+b;}
  int (*fptr)(int,int)=add;
  printf("%d", fptr(2,3));
  ```

---

### 5️⃣ `typedef`

* **What:** Creates an alias for a type.
* **Why:** Simplifies complex declarations and improves readability.
* **Example:**

  ```c
  typedef unsigned long ulong;
  typedef int (*cmp_fn)(int,int);
  ```

---

### 6️⃣ File I/O (Text & Binary)

* **What:** Reading/writing files with the C standard I/O library (`FILE *`).
* **Why:** Essential for persistent data.
* **Example:**

  ```c
  FILE *f = fopen("data.txt","r");
  fscanf(f,"%d",&x);
  fclose(f);
  ```

---

### 7️⃣ Unions

* **What:** Share the same memory for different data types.
* **Why:** Memory-efficient data representation (e.g., variant types).
* **Example:**

  ```c
  union num { int i; float f; };
  ```

---

### 8️⃣ Preprocessor Directives

* **What:** Instructions run *before* compilation (`#define`, `#if`, etc.).
* **Why:** For constants, macros, and conditional compilation.
* **Example:**

  ```c
  #define PI 3.14
  #ifdef DEBUG
  printf("Debug mode");
  #endif
  ```

---

### 9️⃣ Header Guards

* **What:** Prevent multiple inclusion of the same header file.
* **Why:** Avoids redefinition errors.
* **Example:**

  ```c
  #ifndef MY_HEADER_H
  #define MY_HEADER_H
  ...
  #endif
  ```

---

### 🔟 Storage-class Specifiers

* **What:** Control variable linkage, lifetime, and mutability.
* **Why:** Defines visibility and optimization hints.
* **Examples:**

  * `const` → cannot modify.
  * `volatile` → prevent compiler optimization on changing hardware vars.
  * `static` → internal linkage or persistent function vars.
  * `extern` → variable defined in another file.

---

### 11️⃣ Segmentation Faults, Stack vs Heap

* **What:** Crash when program accesses invalid memory.
* **Why:** Understanding memory layout prevents bugs.
* **Example:**

  * Stack → function variables.
  * Heap → `malloc()` allocations.
  * Segfault → dereferencing `NULL` or freed pointers.

---

### 12️⃣ Memory Leaks & Tools

* **What:** Memory allocated but never freed.
* **Why:** Wastes RAM; in long-running processes, fatal.
* **Tool:** `valgrind --leak-check=full ./a.out`

---

### 13️⃣ String Manipulation

* **What:** Working with null-terminated char arrays.
* **Why:** C has no string type; understanding `'\0'` is key.
* **Example:**

  ```c
  char s[10]="Hi";
  strcat(s,"!"); // from <string.h>
  ```

---

### 14️⃣ Hash Tables

* **What:** Map keys → values using a hash function.
* **Why:** O(1) lookups.
* **Example:** Implement via array + linked list buckets.

---

### 15️⃣ Build Systems & Linking

* **What:** Combine multiple `.c` → `.o` → executable.
* **Why:** Enables modular programs.
* **Example:**

  ```bash
  gcc main.o util.o -o app
  ```

  Make automates this.

---

### 16️⃣ C ↔ Assembly Mapping

* **What:** How C statements become assembly instructions.
* **Why:** Crucial for optimization and debugging.
* **Example:**

  ```bash
  gcc -S main.c  # emits .s assembly
  ```

---

### 17️⃣ Undefined Behavior (UB)

* **What:** Operations where C standard says result is unpredictable.
* **Why:** Causes compiler-dependent bugs.
* **Example:**

  ```c
  int x = 1; x = x++; // UB
  ```

---

### 18️⃣ Memory Alignment & Struct Padding

* **What:** CPUs require data on certain byte boundaries.
* **Why:** Explains why structs have extra padding.
* **Example:**

  ```c
  struct s { char c; int x; }; // likely 8 bytes total
  ```

---

### 19️⃣ Inline Assembly

* **What:** Embed assembly inside C.
* **Why:** For fine control or hardware access.
* **Example (GCC):**

  ```c
  asm("movl $1, %eax");
  ```

---

### 20️⃣ Low-level I/O

* **What:** Direct system calls (`read`, `write`) instead of stdio.
* **Why:** Faster and required in kernel-like code.
* **Example:**

  ```c
  write(1, "Hello\n", 6);
  ```

---

### 21️⃣ Processes: `fork()`, `exec()`, Signals

* **What:** Core of UNIX process control.
* **Why:** Spawning, replacing, communicating processes.
* **Example:**

  ```c
  pid_t pid = fork();
  if(pid==0) execlp("ls","ls",NULL);
  ```

---

### 22️⃣ Threads, Concurrency, Race Conditions

* **What:** Parallel tasks sharing memory.
* **Why:** Speed and multitasking; needs synchronization.
* **Example:**

  ```c
  pthread_create(&t,NULL,fn,NULL);
  pthread_join(t,NULL);
  ```

---

### 23️⃣ Networking (Sockets)

* **What:** Communicating via TCP/UDP sockets.
* **Why:** Foundation of all network servers/clients.
* **Example:**

  ```c
  socket(AF_INET, SOCK_STREAM, 0);
  ```

---

### 24️⃣ Dynamic Libraries (`dlopen`, `dlsym`)

* **What:** Load `.so` files at runtime.
* **Why:** Plugin systems, modular apps.
* **Example:**

  ```c
  void* h = dlopen("libm.so",RTLD_LAZY);
  double (*cos_f)(double)=dlsym(h,"cos");
  ```

---

### 25️⃣ Makefiles & Optimization Flags

* **What:** Automate builds, manage dependencies.
* **Why:** Efficient rebuilding, control compiler behavior.
* **Example:**

  ```make
  all: app
  app: main.o util.o
      gcc $^ -o $@
  ```

  Optimization flags: `-O0`, `-O2`, `-O3`, `-march=native`.

---

### 26️⃣ Profiling Tools

* **What:** Measure where your code spends time.
* **Why:** Optimize hotspots.
* **Tools:**

  * `gprof app gmon.out`
  * `perf record ./app`
  * `valgrind --tool=callgrind ./app`

---

### 27️⃣ Custom Memory Allocators

* **What:** Implement your own malloc/free pools.
* **Why:** Performance tuning or debugging.
* **Example:** manage blocks in a pre-allocated buffer.

---

### 28️⃣ Inline Functions & Macros

* **What:** Small functions expanded inline to avoid call overhead.
* **Why:** Faster but increases code size.
* **Example:**

  ```c
  inline int sq(int x){return x*x;}
  #define SQR(x) ((x)*(x))
  ```

---

### 29️⃣ Portability & Standards

* **What:** C89/C99/C11/C23 differences.
* **Why:** Ensures code works across compilers and platforms.
* **Example:** restrict, inline, `_Generic`, threads, and modules (C23).

---

### 30️⃣ Writing Libraries & Defensive Programming

* **What:** Clean APIs, error checking, documentation.
* **Why:** Safe reusable code.
* **Example:** Use consistent naming, return error codes, validate all inputs.

---

### 31️⃣ Unit Testing Frameworks

* **What:** Automate testing of small units of code.
* **Why:** Prevent regressions.
* **Examples:** `Check`, `cmocka`, or your own `assert()`-based test harness.

---
---

### 🧠 Address-of (`&`) and Dereference (`*`) Operators

These two symbols look tiny, but they control *the entire power of pointers, memory, and low-level C programming.*
We’ll go step-by-step, from what’s happening conceptually to how it looks in memory.

---

## 🧩 1️⃣ What these operators mean

| Operator | Name            | Meaning                                                       |
| -------- | --------------- | ------------------------------------------------------------- |
| `&`      | **Address-of**  | "Give me the address (memory location) of this variable."     |
| `*`      | **Dereference** | "Go to this address and get (or set) the value stored there." |

They are **opposites** of each other — like encode ↔ decode.

---

## 🧠 2️⃣ Visual model

Think of memory as a row of boxes, each with:

* An **address** (like house number)
* A **value** (what’s inside the house)

```
Address: 1000   1004   1008   1012
Value:     10     20     30     40
```

When you declare:

```c
int x = 42;
```

Let’s say `x` lives at address `0x1000`.

```
x --> [ 42 ]   (stored at 0x1000)
```

* `x` → means “the value” → 42
* `&x` → means “the address” → 0x1000

If you store that address somewhere:

```c
int *p = &x;
```

Now:

```
p --> [ 0x1000 ]    (the pointer holds x’s address)
x --> [ 42 ]        (the actual value)
```

Then:

* `p` = 0x1000 (address of x)
* `*p` = 42 (value at that address)
* `&x` = 0x1000

So:

```c
*p == x  // always true
```

---

## 🧮 3️⃣ Example program

```c
#include <stdio.h>

int main() {
    int x = 10;
    int *p = &x;        // p stores address of x

    printf("x = %d\n", x);
    printf("&x = %p\n", &x);   // print address of x
    printf("p = %p\n", p);     // same as &x
    printf("*p = %d\n", *p);   // value at address in p

    *p = 99;                  // modify x through pointer
    printf("After *p=99, x = %d\n", x);

    return 0;
}
```

### Output example:

```
x = 10
&x = 0x7ffeefbff4ac
p = 0x7ffeefbff4ac
*p = 10
After *p=99, x = 99
```

✅ So when you change `*p`, you’re directly changing `x`, because `p` points to the memory where `x` lives.

---

## ⚙️ 4️⃣ What really happens in memory

| Name | Address | Value  | Explanation              |
| ---- | ------- | ------ | ------------------------ |
| `x`  | 0x1000  | 99     | Holds an integer         |
| `p`  | 0x1008  | 0x1000 | Holds the address of `x` |

So:

* `p` (0x1008) → points to `x` (0x1000)
* `*p` → “go to address 0x1000 and read its value”

---

## 🧠 5️⃣ Pointer declaration vs dereference usage

### Declaring:

```c
int *p;     // declares a pointer to int
```

The `*` here means “this variable is a pointer type.”

### Using:

```c
*p = 42;    // dereferences pointer p to set the int value
```

The `*` here means “go to that address.”

💡 Context decides whether `*` is part of a type declaration or an operation.

---

## 🧪 6️⃣ Experiment: see addresses yourself

Try this code:

```c
#include <stdio.h>

int main() {
    int a = 5, b = 10;
    int *p = &a;
    printf("p = %p, *p = %d\n", p, *p);
    p = &b;
    printf("p = %p, *p = %d\n", p, *p);
}
```

You’ll see that when `p` changes to `&b`, the value `*p` also changes — because now the pointer looks at a different memory address.

---

## 🧩 7️⃣ A common pitfall

```c
int *p;
*p = 10;  // ❌ WRONG! p is uninitialized
```

This will cause a **segmentation fault**, because `p` doesn’t point anywhere valid yet — you’re dereferencing garbage.

✅ Always initialize:

```c
int x;
int *p = &x; // valid
*p = 10;
```

---

## 🧱 8️⃣ Combining & and *

They cancel out:

```c
int x = 7;
int *p = &x;

printf("%d\n", *(&x));   // 7
printf("%p\n", &(*p));   // same as &x
```

`*(&x)` = “take the address of x, then go there” → gives x.
`&(*p)` = “dereference p, then take its address” → gives &x.

---

## 🧰 9️⃣ Quick analogy

Think of:

* `x` → a **house**
* `&x` → the **house address**
* `p` → a **notebook where you write addresses**
* `*p` → you **go to the address written in the notebook and open that house**

---

## 🔬 10️⃣ Summary Table

| Expression | Meaning                              | Type   |
| ---------- | ------------------------------------ | ------ |
| `x`        | Value of variable                    | int    |
| `&x`       | Address of variable                  | int *  |
| `p`        | Value stored in pointer (an address) | int *  |
| `*p`       | Value pointed to by pointer          | int    |
| `&p`       | Address of pointer itself            | int ** |

---

## 💡 11️⃣ Practical uses

* Accessing/modifying values indirectly (parameter passing)
* Dynamic memory (`malloc`) returns pointers
* Data structures (linked lists, trees)
* System programming (memory-mapped I/O)
* Function parameters (simulate pass-by-reference)

---

## 🚀 12️⃣ Exercises for mastery

1. Print the address of every variable in a function.
2. Create an `int x`, a pointer `p`, and a pointer-to-pointer `pp`, and print all values.
3. Write a function:

   ```c
   void increment(int *n) { (*n)++; }
   ```

   and call it with `increment(&x);`
4. Try dereferencing an uninitialized pointer — observe the segmentation fault.
5. Observe pointer arithmetic:

   ```c
   int a[3] = {1,2,3};
   printf("%d", *(a+1)); // 2
   ```

---
---

# 🧩 2️⃣ Array ↔ Pointer Relationship in C

---

## 🧠 1️⃣ What’s the big idea?

In C, **arrays and pointers are deeply related — but not the same.**
When you use an array’s name in most expressions, it **“decays” into a pointer** to its first element.

That means:

```c
int arr[3] = {10, 20, 30};
int *p = arr;   // same as int *p = &arr[0];
```

Here `arr` acts as a pointer to the first element — but the array *itself* is still a fixed block of memory that knows its own size at compile time.

---

## 🧩 2️⃣ Memory visualization

Assume:

```c
int arr[3] = {10, 20, 30};
```

Memory layout:

| Address | Name   | Value |
| ------- | ------ | ----- |
| 0x1000  | arr[0] | 10    |
| 0x1004  | arr[1] | 20    |
| 0x1008  | arr[2] | 30    |

Now:

* `arr` → address of the first element → `0x1000`
* `&arr[0]` → also `0x1000`
* `arr + 1` → `0x1004`
* `*(arr + 1)` → value `20`

✅ So:

```c
arr[i] == *(arr + i)
```

is *always true*.

---

## ⚙️ 3️⃣ Example program

```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};
    int *p = arr; // same as &arr[0]

    for (int i = 0; i < 3; i++) {
        printf("arr[%d] = %d, *(p+%d) = %d\n", i, arr[i], i, *(p+i));
    }
}
```

### Output:

```
arr[0] = 10, *(p+0) = 10
arr[1] = 20, *(p+1) = 20
arr[2] = 30, *(p+2) = 30
```

---

## 🧮 4️⃣ Pointer arithmetic explained

When you do:

```c
p + 1
```

C automatically adds **sizeof(*p)** bytes to the address.
So for an `int*`, if each `int` is 4 bytes:

```
p + 1  →  address + 4
p + 2  →  address + 8
```

That’s why you can iterate over arrays using pointers:

```c
for (int *ptr = arr; ptr < arr + 3; ptr++) {
    printf("%d ", *ptr);
}
```

---

## 🧠 5️⃣ When arrays are *not* pointers

Even though arrays can “act” like pointers, they’re not fully the same.

| Expression | Type                    | Meaning                      |
| ---------- | ----------------------- | ---------------------------- |
| `arr`      | array of int            | Fixed-size block             |
| `&arr[0]`  | pointer to int          | Address of first element     |
| `&arr`     | pointer to entire array | Different type: `int (*)[3]` |

Let’s see an example:

```c
int arr[3] = {1,2,3};
printf("%p %p %p\n", arr, &arr[0], &arr);
```

**Output (same numeric value, different types):**

```
0x7ffeefbff580 0x7ffeefbff580 0x7ffeefbff580
```

They look the same when printed, but note:

* `arr` has type `int *`
* `&arr` has type `int (*)[3]`

So `&arr + 1` jumps the whole array (adds 12 bytes), not one element (4 bytes).

---

## 💡 6️⃣ Why this matters

Understanding this is key to:

* Implementing string functions (`char *s`)
* Using dynamic memory (`malloc`)
* Passing arrays to functions

---

## 📦 7️⃣ Passing arrays to functions

```c
void print_arr(int *a, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
}

int main() {
    int arr[3] = {10, 20, 30};
    print_arr(arr, 3);
}
```

Here `arr` “decays” to `int *` when passed to the function.

Inside `print_arr`, there’s no way to know the original array size (because it became just a pointer), which is why we pass `n` separately.

---

## ⚙️ 8️⃣ Multi-dimensional arrays & pointer relationships

```c
int arr[2][3] = {{1,2,3},{4,5,6}};
```

* `arr` → pointer to first row → type `int (*)[3]`
* `arr[0]` → pointer to first element of row → type `int *`
* `*arr` → same as `arr[0]`
* `arr[i][j]` → same as `*(*(arr+i)+j)`

So:

```c
arr[1][2] == *(*(arr+1)+2)
```

✅ evaluates to 6.

---

## 🚫 9️⃣ Common mistakes

❌ Assigning to array name:

```c
int a[3];
int *b;
b = a;   // OK
a = b;   // ❌ error: array is not assignable
```

Arrays are not assignable — they’re fixed memory blocks.

❌ Going out of bounds:

```c
printf("%d", arr[3]); // undefined behavior
```

No bounds check in C. You’re on your own.

---

## ⚗️ 10️⃣ Small pointer lab

Try this to really *see* it:

```c
#include <stdio.h>
int main() {
    int arr[3] = {10,20,30};
    printf("arr=%p, arr+1=%p\n", arr, arr+1);
    printf("&arr=%p, &arr+1=%p\n", &arr, &arr+1);
}
```

You’ll notice:

* `arr+1` increments by `sizeof(int)` (4 bytes)
* `&arr+1` increments by `sizeof(arr)` (12 bytes)

---

## 🧬 11️⃣ Quick mental model

```
arr[i]  ==  *(arr + i)
&arr[i] ==  arr + i
```

👉 Arrays are **contiguous memory blocks**,
and pointers are **variables that store memory addresses**.

The language lets you use one like the other for flexibility — but never forget arrays are static while pointers are dynamic.

---

## ⚡ 12️⃣ Summary table

| Concept                   | Example   | Type            | Meaning                  |
| ------------------------- | --------- | --------------- | ------------------------ |
| Array name                | `arr`     | `int*` (decays) | address of first element |
| Address of first element  | `&arr[0]` | `int*`          | same as `arr`            |
| Address of whole array    | `&arr`    | `int (*)[N]`    | pointer to array         |
| Dereference array pointer | `*arr`    | `int`           | first element            |
| Access element            | `arr[i]`  | `int`           | value at offset `i`      |
| Pointer arithmetic        | `arr + i` | `int*`          | pointer to i-th element  |

---

## 🧠 13️⃣ Real-world use cases

* Strings (`char *`) are just arrays of chars.
* Dynamic arrays (`malloc`) use pointers, not static arrays.
* Multi-dimensional arrays and matrices.
* Function parameters for arrays.
* Pointer arithmetic in low-level systems code.

---
---

# 🧩 3️⃣ Double Pointers (`**`)

---

## 🧠 1️⃣ What is a double pointer?

A **double pointer** (also called a *pointer to pointer*) is a variable that **stores the address of another pointer**.

👉 It’s a **level of indirection** —
you don’t point to data directly, you point to the pointer *that points* to the data.

---

## 🧩 2️⃣ Analogy

Imagine you have:

* A **value**: a locker containing a number.
* A **pointer**: a sticky note with the locker’s number.
* A **double pointer**: a slip of paper that has the location of the sticky note.

So:

```
Value →  [42]
Pointer → [address of Value]
Double Pointer → [address of Pointer]
```

---

## ⚙️ 3️⃣ Basic example

```c
#include <stdio.h>

int main() {
    int x = 10;
    int *p = &x;   // p points to x
    int **pp = &p; // pp points to p

    printf("x = %d\n", x);
    printf("&x = %p\n", &x);
    printf("p = %p (address of x)\n", p);
    printf("&p = %p\n", &p);
    printf("pp = %p (address of p)\n", pp);
    printf("*pp = %p (value of p)\n", *pp);
    printf("**pp = %d (value of x)\n", **pp);
}
```

### Output (addresses differ):

```
x = 10
&x = 0x7ffca08...
p = 0x7ffca08...
&p = 0x7ffca08...
pp = 0x7ffca08...
*pp = 0x7ffca08...
**pp = 10
```

You can see:

* `p` stores `&x`
* `pp` stores `&p`
* `*pp` gives `p`
* `**pp` gives the value at `x`

---

## 🧮 4️⃣ Memory layout

Let’s visualize:

| Name | Address  | Value    | Meaning            |
| ---- | -------- | -------- | ------------------ |
| `x`  | `0x1000` | 10       | actual integer     |
| `p`  | `0x2000` | `0x1000` | pointer to x       |
| `pp` | `0x3000` | `0x2000` | pointer to pointer |

So:

| Expression | Evaluates to                         | Result |
| ---------- | ------------------------------------ | ------ |
| `x`        | value                                | 10     |
| `p`        | address of x                         | 0x1000 |
| `*p`       | value at that address                | 10     |
| `pp`       | address of p                         | 0x2000 |
| `*pp`      | value at that address (which is `p`) | 0x1000 |
| `**pp`     | value at that address (`x`)          | 10     |

---

## 🧠 5️⃣ Why use double pointers?

1. **To modify a pointer inside a function**
   (Since arguments are passed by value, you need a pointer to pointer to change the original pointer.)
2. **To dynamically allocate 2D arrays**
   (Arrays of pointers to arrays.)
3. **For linked structures** (like lists of lists)
4. **For handling command-line arguments** (`char **argv`)
5. **For implementing double indirection (array of strings)**

---

## 🧩 6️⃣ Example 1 — modifying a pointer inside a function

```c
#include <stdio.h>
#include <stdlib.h>

void allocate(int **p) {
    *p = malloc(sizeof(int));
    **p = 42;
}

int main() {
    int *ptr = NULL;
    allocate(&ptr);
    printf("*ptr = %d\n", *ptr);
    free(ptr);
}
```

✅ Output:

```
*ptr = 42
```

### Explanation:

* `allocate()` receives address of `ptr` (so `p` points to `ptr`)
* Inside, `*p` is `ptr`
* `*p = malloc(...)` sets the pointer itself (in main)
* `**p = 42` writes value to allocated memory

Without `int **`, you couldn’t modify the caller’s pointer.

---

## 🧩 7️⃣ Example 2 — double pointer and arrays of pointers (2D arrays)

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int **arr;
    int rows = 2, cols = 3;

    arr = malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++)
        arr[i] = malloc(cols * sizeof(int));

    // Fill array
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            arr[i][j] = i * cols + j + 1;

    // Print array
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++)
            printf("%d ", arr[i][j]);
        printf("\n");
    }

    // Free
    for (int i = 0; i < rows; i++) free(arr[i]);
    free(arr);
}
```

### Output:

```
1 2 3
4 5 6
```

✅ Here:

* `arr` points to a block of row pointers
* Each `arr[i]` points to a row of ints
* So `arr[i][j]` = `*(*(arr+i)+j)`

---

## ⚠️ 8️⃣ Common mistakes

❌ Forgetting to allocate for both levels:

```c
int **p;
p = malloc(sizeof(int)); // WRONG — should be sizeof(int *)
```

✅ Correct:

```c
p = malloc(n * sizeof(int *)); // allocate array of pointers
```

❌ Forgetting to free all levels:

```c
free(arr); // ❌ memory leak (rows still allocated)
```

✅ Must free each row first.

---

## 🧬 9️⃣ Type breakdown

| Declaration  | Type                      | Meaning                                 |
| ------------ | ------------------------- | --------------------------------------- |
| `int *p`     | pointer to int            | points to value                         |
| `int **pp`   | pointer to pointer to int | points to another pointer               |
| `int ***ppp` | triple pointer            | rarely used (pointer to double pointer) |

---

## 🧠 10️⃣ Real examples in C

* **`main(int argc, char **argv)`**

  * `argv` is a pointer to array of strings (`char*`).
  * So `argv[i]` is a string, `argv[i][j]` is a character.

* **`execv()`**, **`envp`**, and other POSIX calls use `char **`.

---

## 🧱 11️⃣ Quick experiment

```c
#include <stdio.h>
int main() {
    char *names[] = {"Yuvraj", "Alice", "Bob"};
    char **pp = names;

    for (int i = 0; i < 3; i++)
        printf("%s\n", *(pp + i));  // same as names[i]
}
```

✅ Output:

```
Yuvraj
Alice
Bob
```

Here:

* `names` is an array of `char *`
* `names` itself decays to `char **` (pointer to first string)

---

## ⚡ 12️⃣ Summary Table

| Expression | Type               | Meaning                  |
| ---------- | ------------------ | ------------------------ |
| `int x`    | int                | normal value             |
| `int *p`   | pointer to int     | holds address of int     |
| `int **pp` | pointer to pointer | holds address of pointer |
| `*p`       | int                | dereference once         |
| `**pp`     | int                | dereference twice        |
| `&x`       | int *              | address of x             |
| `&p`       | int **             | address of p             |

---

## 🧩 13️⃣ Mental Model

```
**pp → *(*pp)
```

Break it from right to left:

1. `pp` → address of `p`
2. `*pp` → contents of `p` (address of x)
3. `**pp` → value at address in `p` (the actual x)

---

## 🧠 14️⃣ Where double pointers shine

| Use case                         | Why needed                     |
| -------------------------------- | ------------------------------ |
| Modify pointer inside a function | Function parameters are copies |
| 2D dynamic arrays                | Pointers to pointers           |
| CLI arguments (`argv`)           | Array of strings               |
| Linked lists of lists            | Nested references              |
| Memory management routines       | Manage blocks indirectly       |

---

## ✅ Key takeaway

> A **double pointer** lets you manipulate *what another pointer points to.*

If a pointer is “an address to data,”
then a double pointer is “an address to a pointer.”

---
---

# 🧩 4️⃣ Function Pointers

---

## 🧠 1️⃣ What is a function pointer?

A **function pointer** is just like a normal pointer —
but instead of pointing to a variable or memory address of data,
it points to a **function’s entry address in memory**.

In C, every function has a fixed location in memory where its instructions start.
A function pointer can store that address and call it later.

---

## 🧮 2️⃣ Syntax basics

You declare a function pointer like this:

```c
<return_type> (*<name>)(<parameter_types>);
```

Example:

```c
int (*fp)(int, int);
```

➡️ “fp is a pointer to a function that takes two ints and returns an int.”

---

## ⚙️ 3️⃣ Minimal working example

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int (*fptr)(int, int);  // declare function pointer
    fptr = add;             // assign address of function
    // OR fptr = &add; — both are valid

    int result = fptr(2, 3);  // call via pointer
    printf("Result = %d\n", result);
}
```

### Output:

```
Result = 5
```

✅ `fptr(2,3)` means → “call the function whose address is stored in `fptr`”.

You could also write:

```c
(*fptr)(2,3);
```

Both mean the same — function call through pointer.

---

## 🧠 4️⃣ What’s happening in memory

Let’s visualize:

| Symbol         | Meaning                   | Example Address |
| -------------- | ------------------------- | --------------- |
| `add`          | Function in memory        | 0x400500        |
| `fptr`         | Pointer to function       | holds 0x400500  |
| `(*fptr)(2,3)` | Executes code at 0x400500 | runs `add`      |

So `fptr` just holds the memory location of the function, exactly like a data pointer holds an address of a variable.

---

## ⚙️ 5️⃣ Another example — multiple functions, one pointer

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int main() {
    int (*op)(int, int);

    op = add;
    printf("add: %d\n", op(5, 3));

    op = sub;
    printf("sub: %d\n", op(5, 3));
}
```

✅ Output:

```
add: 8
sub: 2
```

---

## 🧩 6️⃣ Using function pointers as function arguments (callbacks)

This is where they become powerful 🔥

```c
#include <stdio.h>

void compute(int a, int b, int (*operation)(int, int)) {
    printf("Result = %d\n", operation(a, b));
}

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

int main() {
    compute(3, 4, add);
    compute(3, 4, mul);
}
```

✅ Output:

```
Result = 7
Result = 12
```

Now `compute()` can apply *any* function that matches `(int,int) -> int`.
This pattern is called a **callback function** — common in GUI toolkits, event systems, sorting (`qsort`), and signal handlers.

---

## 🧱 7️⃣ Real-world example: `qsort()` from `<stdlib.h>`

`qsort()` uses a function pointer for comparison:

```c
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int arr[] = {5, 2, 9, 1};
qsort(arr, 4, sizeof(int), compare);
```

* `compare` is a function pointer passed to `qsort`.
* `qsort` calls `compare()` internally to decide ordering.

Prototype:

```c
void qsort(void *base, size_t nitems, size_t size,
           int (*compar)(const void*, const void*));
```

See that? That `(*compar)` part = a **function pointer**.

---

## 🧠 8️⃣ Arrays of function pointers

You can store multiple function pointers in an array to implement **menus**, **dispatch tables**, or **virtual tables** (like C++ vtables but manual).

```c
#include <stdio.h>

int add(int a,int b){return a+b;}
int sub(int a,int b){return a-b;}
int mul(int a,int b){return a*b;}

int main() {
    int (*ops[])(int,int) = {add, sub, mul};
    int choice;
    printf("0:add 1:sub 2:mul\n");
    scanf("%d", &choice);
    printf("Result = %d\n", ops[choice](5,3));
}
```

✅ Run and choose operation interactively — each menu choice calls a different function via pointer.

---

## ⚙️ 9️⃣ Function pointers to `void` return

Yes — you can have pointers to any type of function, including `void`:

```c
void greet() { printf("Hi!\n"); }
void (*fp)() = greet;
fp();  // prints Hi!
```

---

## 🧠 10️⃣ Function pointer typedefs (make it clean!)

Long pointer declarations get messy fast, so use `typedef`:

```c
typedef int (*operation_fn)(int, int);

int add(int a,int b){return a+b;}
int sub(int a,int b){return a-b;}

int main() {
    operation_fn op = add;
    printf("%d\n", op(3,4));
}
```

✅ This makes code much clearer — especially for APIs.

---

## 🧩 11️⃣ Function pointer to pointer (meta level)

Yes, you can even have **pointer to function pointer**:

```c
int add(int a,int b){return a+b;}
int (*fp)(int,int)=add;
int (**fpp)(int,int)=&fp;

printf("%d\n", (**fpp)(2,3)); // → 5
```

Used rarely, mostly for dynamic structures or APIs that modify callbacks.

---

## ⚙️ 12️⃣ Function pointer arrays and tables in real systems

Common in:

* OS kernels (syscall tables)
* Interpreters (opcode handlers)
* Event systems (callback registry)
* GUI event dispatching
* Plugin or driver systems

Example: syscall table style

```c
int sys_open(){...}
int sys_read(){...}
int sys_write(){...}

int (*syscalls[])(void) = {sys_open, sys_read, sys_write};
```

Then call dynamically by index.

---

## ⚠️ 13️⃣ Common mistakes

❌ Wrong signature:

```c
int (*fptr)(int); // wrong: expects 1 arg
fptr = add;       // compiler warning
```

✅ Must match prototype exactly.

❌ Dereferencing NULL pointer:

```c
int (*fptr)(int,int) = NULL;
fptr(2,3);  // segmentation fault
```

✅ Always check before calling:

```c
if (fptr) fptr(2,3);
```

---

## 🧬 14️⃣ Summary Table

| Concept     | Syntax                        | Description                       |
| ----------- | ----------------------------- | --------------------------------- |
| Declare     | `int (*f)(int,int);`          | f points to func taking (int,int) |
| Assign      | `f = add;`                    | assign function address           |
| Call        | `f(2,3)` or `(*f)(2,3)`       | call through pointer              |
| Pass as arg | `foo(add)`                    | callback                          |
| Typedef     | `typedef int (*op)(int,int);` | alias for cleaner syntax          |

---

## 🧠 15️⃣ Mental model

```
add → [ machine code starting address ]
fptr → holds address of that code
fptr(args...) → jumps to that address and executes
```

The same CPU `CALL` instruction is used — the only difference is that the target address comes from memory instead of being hardcoded.

---

## 🧠 16️⃣ Advanced: Function pointers and `void *`

Sometimes, you see `void *` cast to store arbitrary function addresses (in plugin systems or syscall tables), but C forbids calling a function through a mismatched pointer type.
In POSIX and Linux kernel code, this is handled carefully with explicit casts and matching types.

---

## 🧩 17️⃣ Real-world examples

| Function pointer used in | Purpose                            |
| ------------------------ | ---------------------------------- |
| `signal()`               | Signal handling callback           |
| `qsort()`                | Sorting comparator                 |
| `pthread_create()`       | Thread start routine               |
| Linux syscalls           | System call dispatch table         |
| GUI libraries            | Button click callbacks             |
| Game engines             | Event loops, AI behavior switching |

---

## ⚡ 18️⃣ Quick experiments to try

1. Make a calculator that uses a function pointer array for `+ - * /`.
2. Implement your own `map()` function:

   ```c
   void map(int *arr, int n, int (*fn)(int));
   ```
3. Write a program where a function takes another function to filter array elements.
4. Pass a function pointer to a thread or timer routine.

---

## 🚀 19️⃣ Takeaway

> A **function pointer** stores a **function’s address** and lets you call it dynamically.

They’re essential for:

* Callbacks
* Event-driven programming
* Generic algorithms (`qsort`, `bsearch`)
* Dynamic linking & plugins
* Emulating polymorphism in plain C

---
---

# 🧩 5️⃣ `typedef` — Type Definition Alias in C

---

## 🧠 1️⃣ What is `typedef`?

`typedef` **creates an alias (nickname)** for an existing type.
It does **not create a new type** — it just gives a *type name* another name.

### Basic form:

```c
typedef <existing_type> <new_name>;
```

So this:

```c
typedef unsigned long ulong;
```

means that now you can use:

```c
ulong x = 1000;   // same as unsigned long x = 1000;
```

---

## 🧩 2️⃣ Why use `typedef`?

### 🔹 Simplify long or complex declarations

```c
typedef unsigned long int u64;
```

### 🔹 Improve readability & maintainability

```c
typedef struct student Student;
```

### 🔹 Abstract data structures in headers

```c
typedef struct Node* NodePtr;
```

So users don’t need to know the internals — just that it’s a pointer type.

### 🔹 Cleaner function pointers

```c
typedef int (*Operation)(int,int);
Operation add, sub;
```

---

## ⚙️ 3️⃣ Basic examples

```c
typedef int INTEGER;
INTEGER a = 10;
printf("%d", a); // same as int a = 10
```

✅ Nothing fancy — compiler treats it as `int`, but `INTEGER` makes intent clearer.

---

## 🧱 4️⃣ `typedef` with structs (the most common use)

Without typedef:

```c
struct student {
    int id;
    char name[20];
};

struct student s1;  // need 'struct' keyword every time
```

With typedef:

```c
typedef struct student {
    int id;
    char name[20];
} Student;

Student s1;  // clean!
```

You can even skip the tag name entirely:

```c
typedef struct {
    int id;
    char name[20];
} Student;
```

---

## 🧠 5️⃣ `typedef` with pointers

```c
typedef int* IntPtr;

IntPtr a, b;
```

✅ Both `a` and `b` are `int*`.

⚠️ But **be careful**:

```c
int* a, b;
```

Only `a` is a pointer — `b` is an `int`.
So `typedef` helps make pointer intent clearer.

---

## ⚙️ 6️⃣ `typedef` with function pointers

This is one of its most powerful uses.

Without typedef:

```c
int (*op)(int, int);
```

With typedef:

```c
typedef int (*Operation)(int, int);
Operation add, sub;
```

Now:

```c
int add_fn(int a, int b) { return a + b; }
Operation f = add_fn;
printf("%d", f(2, 3));
```

✅ Way more readable.

---

## 🧩 7️⃣ `typedef` for array types

You can alias array types too:

```c
typedef int Matrix3x3[3][3];
Matrix3x3 mat = { {1,2,3}, {4,5,6}, {7,8,9} };
```

✅ Now `mat` is declared in one clean line.

---

## 🧠 8️⃣ `typedef` with `struct` pointers

Common in data structures like linked lists:

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

Then you can write:

```c
Node *head = NULL;
```

Instead of:

```c
struct Node *head = NULL;
```

✅ This pattern is *everywhere* in C libraries (e.g., GTK, libcurl, POSIX APIs).

---

## ⚙️ 9️⃣ `typedef` with `enum`

```c
typedef enum {
    RED, GREEN, BLUE
} Color;

Color c = RED;
```

✅ You don’t have to repeat `enum` every time.

---

## 🧩 10️⃣ `typedef` for hiding implementation details

Header (`list.h`):

```c
typedef struct List List;

List* list_create(void);
void list_add(List*, int);
```

Source (`list.c`):

```c
struct List {
    int data[100];
    int count;
};
```

✅ This “opaque pointer” hides internal structure, enabling information hiding / encapsulation (like OOP in C).

---

## ⚙️ 11️⃣ `typedef` + `const` rules

Placement of `const` matters:

```c
typedef int* IntPtr;
const IntPtr p = &x;
```

Here `p` is a **constant pointer to int**,
not a pointer to a constant int.

Because:

```c
typedef int* IntPtr;
const IntPtr p;  // == int *const p;
```

If you want `const int*`, you must declare typedef differently:

```c
typedef const int* ConstIntPtr;
```

---

## 🧠 12️⃣ Combining with `struct`, `union`, and `enum`

You can typedef any complex type cleanly:

```c
typedef union {
    int i;
    float f;
    char c;
} Value;

typedef struct {
    char key[20];
    Value val;
} KeyValue;
```

✅ Makes nested types readable and maintainable.

---

## 🧩 13️⃣ Real-world usage examples

| Use case           | Example                                            |
| ------------------ | -------------------------------------------------- |
| **Platform types** | `typedef unsigned long uint64_t;`                  |
| **Custom handles** | `typedef struct Window* WindowHandle;`             |
| **Callback types** | `typedef void (*EventHandler)(int code);`          |
| **Portable code**  | `typedef int bool; #define true 1 #define false 0` |
| **Opaque structs** | Hiding implementation from users                   |

---

## ⚠️ 14️⃣ Common mistakes / misconceptions

❌ Thinking `typedef` creates a new type — it doesn’t.
✅ It’s just an alias; `typedef int myint;` and `int` are the same type to the compiler.

❌ Misusing `typedef` on function signatures that don’t match.
✅ Always match parameter and return types exactly.

❌ Forgetting that `typedef` applies to the full declaration:

```c
typedef int* Ptr;
Ptr a, b; // both are pointers ✅
```

…but `int* a, b;` makes only `a` a pointer ❌

---

## 🧬 15️⃣ Advanced: typedef and function prototypes

You can typedef a function type itself (not just pointer):

```c
typedef int MathOp(int, int);
```

Then:

```c
MathOp *fn = add;   // pointer to such function
```

✅ Equivalent to:

```c
typedef int (*MathOpPtr)(int, int);
MathOpPtr fn = add;
```

---

## 💡 16️⃣ Why professionals use `typedef` everywhere

| Without typedef          | With typedef    |
| ------------------------ | --------------- |
| `int (*f)(void*, void*)` | `CompareFunc f` |
| `struct Node *head`      | `NodePtr head`  |
| `unsigned long long`     | `u64`           |
| `int (*)(int,int)`       | `OperationFn`   |

Cleaner, safer, and easier to refactor later.

---

## 🧱 17️⃣ Summary Table

| Syntax                          | Meaning                       |
| ------------------------------- | ----------------------------- |
| `typedef int INT;`              | INT is alias for int          |
| `typedef struct {...} Student;` | Student alias for struct      |
| `typedef int* IntPtr;`          | IntPtr alias for int pointer  |
| `typedef int (*Func)(int,int);` | Func is function pointer type |
| `typedef enum {...} Color;`     | Color alias for enum          |

---

## 🧠 18️⃣ Quick exercises to master it

1. Create a typedef for a function pointer `void (*callback)(int, float)`.
2. Use typedef to simplify a linked list struct.
3. Create a typedef for `char[256]` → call it `String256`.
4. Use typedef to define an opaque struct type in a header file and implement it in a `.c`.
5. Create a typedef for a comparator function and use it with `qsort`.

---

✅ **Summary thought:**

> `typedef` doesn’t change the compiler — it changes your *clarity*.
> It’s how professional C code stays readable even when dealing with complex pointers, structs, and function signatures.

---
---

# 🧩 6️⃣ File I/O in C (Text + Binary)

---

## 🧠 1️⃣ Files in C — the big picture

C provides **high-level file handling** via the `FILE *` type defined in `<stdio.h>`.

When you open a file:

* The system associates a **file descriptor (low-level number)** with a `FILE*` (a buffered stream).
* You can then read/write using the library functions.

---

## ⚙️ 2️⃣ The basic workflow

| Step | Function                                                             | Purpose                       |
| ---- | -------------------------------------------------------------------- | ----------------------------- |
| 1    | `fopen()`                                                            | Open a file (returns `FILE*`) |
| 2    | `fprintf()`, `fscanf()`, `fgets()`, `fputs()`, `fread()`, `fwrite()` | Perform I/O                   |
| 3    | `fclose()`                                                           | Close the file                |
| 4    | `feof()`, `ferror()`                                                 | Check for end or error        |

---

## 🧩 3️⃣ Opening a file

```c
FILE *fp;
fp = fopen("data.txt", "r");
```

### Modes

| Mode                     | Meaning         | Notes                  |
| ------------------------ | --------------- | ---------------------- |
| `"r"`                    | Read (text)     | File must exist        |
| `"w"`                    | Write (text)    | Overwrites or creates  |
| `"a"`                    | Append (text)   | Add to end or create   |
| `"r+"`                   | Read + Write    | File must exist        |
| `"w+"`                   | Read + Write    | Overwrites or creates  |
| `"a+"`                   | Read + Append   | Create if missing      |
| `"rb"` / `"wb"` / `"ab"` | Binary versions | No newline conversions |

✅ Always check for success:

```c
if (fp == NULL) {
    perror("Error opening file");
    return 1;
}
```

---

## 🧠 4️⃣ Writing to text files

### Using `fprintf()`

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("output.txt", "w");
    if (!fp) return 1;

    fprintf(fp, "Name: %s\nAge: %d\n", "Yuvraj", 21);
    fclose(fp);
}
```

✅ Writes formatted text, just like `printf()` but to a file.

---

### Using `fputs()` or `putc()`

```c
fputs("Hello File\n", fp);
putc('A', fp);
```

---

## ⚙️ 5️⃣ Reading from text files

### Using `fscanf()`

```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("output.txt", "r");
    char name[20];
    int age;

    fscanf(fp, "Name: %s\nAge: %d\n", name, &age);
    printf("%s is %d years old\n", name, age);
    fclose(fp);
}
```

---

### Using `fgets()` for lines

```c
char buffer[100];
while (fgets(buffer, sizeof(buffer), fp))
    printf("%s", buffer);
```

* `fgets()` reads **until newline or EOF**.
* Always safe for strings (avoids overflow).

---

## 🧩 6️⃣ Handling EOF and errors

C uses special macros:

* **`EOF`** → End of File constant (-1)
* **`feof(FILE*)`** → true if end reached
* **`ferror(FILE*)`** → true if error occurred

Example:

```c
int c;
while ((c = fgetc(fp)) != EOF) {
    putchar(c);
}
if (feof(fp)) printf("End of file\n");
```

---

## 🧱 7️⃣ File positioning — `fseek`, `ftell`, `rewind`

Used to move around in a file.

```c
fseek(fp, 0, SEEK_END);   // move to end
long size = ftell(fp);    // get position (file size)
rewind(fp);               // back to start
```

| Constant   | Meaning               |
| ---------- | --------------------- |
| `SEEK_SET` | From beginning        |
| `SEEK_CUR` | From current position |
| `SEEK_END` | From end              |

---

## 💾 8️⃣ Binary File I/O

Unlike text files, **binary mode** writes/reads bytes *exactly* as they are in memory — no newline conversions, no formatting.

### Writing binary data

```c
#include <stdio.h>

struct Student {
    int id;
    float marks;
};

int main() {
    struct Student s = {1, 87.5};
    FILE *fp = fopen("student.dat", "wb");
    fwrite(&s, sizeof(struct Student), 1, fp);
    fclose(fp);
}
```

✅ `fwrite(ptr, size, count, file)`
→ Writes `count` elements of size `size` from memory `ptr`.

---

### Reading binary data

```c
#include <stdio.h>

struct Student {
    int id;
    float marks;
};

int main() {
    struct Student s;
    FILE *fp = fopen("student.dat", "rb");
    fread(&s, sizeof(struct Student), 1, fp);
    printf("ID=%d Marks=%.2f\n", s.id, s.marks);
    fclose(fp);
}
```

✅ `fread(ptr, size, count, file)`
→ Reads `count` elements into memory at `ptr`.

---

## 🧠 9️⃣ Binary vs Text mode — key differences

| Feature             | Text                                    | Binary                       |
| ------------------- | --------------------------------------- | ---------------------------- |
| Data interpretation | Human-readable                          | Raw bytes                    |
| End of line         | `\n` may translate to `\r\n` on Windows | No translation               |
| Used for            | Configs, logs, scripts                  | Structs, images, executables |
| Functions used      | `fprintf`, `fscanf`, `fgets`            | `fread`, `fwrite`            |
| Example             | `"Name 21"`                             | `0x01 0x42 0x8F ...`         |

---

## ⚠️ 10️⃣ Common mistakes

❌ Forgetting to `fclose(fp)`
➡️ Causes data not to flush to disk.

❌ Mixing text and binary writes
➡️ Always open with correct mode (`"wb"` or `"w"`).

❌ Using wrong `fread()`/`fwrite()` size
➡️ Always use `sizeof(type)`.

❌ Not checking `fopen()` result
➡️ Can lead to segmentation fault on `NULL` pointer.

---

## 🧩 11️⃣ Combining both — read/write multiple records

```c
#include <stdio.h>

typedef struct {
    int id;
    char name[20];
    float score;
} Student;

int main() {
    Student students[3] = {
        {1, "Yuvraj", 95.5},
        {2, "Alice", 89.0},
        {3, "Bob", 76.5}
    };

    FILE *fp = fopen("data.bin", "wb");
    fwrite(students, sizeof(Student), 3, fp);
    fclose(fp);

    // read back
    fp = fopen("data.bin", "rb");
    Student temp;
    while (fread(&temp, sizeof(Student), 1, fp))
        printf("%d %s %.2f\n", temp.id, temp.name, temp.score);
    fclose(fp);
}
```

✅ Output:

```
1 Yuvraj 95.50
2 Alice 89.00
3 Bob 76.50
```

---

## 🧠 12️⃣ File streams and buffers

* Each `FILE*` has an internal **I/O buffer**.
* `fclose()` or `fflush(fp)` flushes (writes) the buffer to disk.
* For immediate write:

  ```c
  fflush(fp);
  ```
* stdin, stdout, stderr are **predefined**:

  ```c
  fprintf(stdout, "Hello\n");
  fprintf(stderr, "Error occurred\n");
  ```

---

## 🧬 13️⃣ `remove()` and `rename()`

```c
rename("old.txt", "new.txt");
remove("temp.txt");
```

Simple file operations built into C standard library.

---

## 🧱 14️⃣ File I/O error handling

```c
if (ferror(fp))
    perror("File error");

clearerr(fp);  // reset file status flags
```

---

## ⚡ 15️⃣ Quick example summary

| Action        | Function    | Example                         |
| ------------- | ----------- | ------------------------------- |
| Open file     | `fopen()`   | `FILE *f = fopen("a.txt","r");` |
| Write text    | `fprintf()` | `fprintf(f,"Hello");`           |
| Read text     | `fscanf()`  | `fscanf(f,"%d",&n);`            |
| Read line     | `fgets()`   | `fgets(buf,100,f);`             |
| Write binary  | `fwrite()`  | `fwrite(&x,sizeof x,1,f);`      |
| Read binary   | `fread()`   | `fread(&x,sizeof x,1,f);`       |
| Move position | `fseek()`   | `fseek(f,0,SEEK_END);`          |
| Get position  | `ftell()`   | `long pos = ftell(f);`          |
| Close file    | `fclose()`  | `fclose(f);`                    |

---

## 🧠 16️⃣ Advanced: random access to records

Example: modify 2nd student record directly in binary file.

```c
fseek(fp, sizeof(Student) * 1, SEEK_SET);
fread(&s, sizeof(Student), 1, fp);
s.score = 99.9;
fseek(fp, -sizeof(Student), SEEK_CUR);
fwrite(&s, sizeof(Student), 1, fp);
```

✅ This edits just that one record — no need to reload everything.

---

## 🧩 17️⃣ Real-world use cases

| Type          | Example                             |
| ------------- | ----------------------------------- |
| Text          | Logs, configs, CSV files            |
| Binary        | Databases, images, executables      |
| Mixed         | Game save files, serialized structs |
| Random Access | File-based databases                |

---

## 🚀 18️⃣ Summary

| Concept   | Text I/O                    | Binary I/O               |
| --------- | --------------------------- | ------------------------ |
| Read      | `fscanf`, `fgets`, `fgetc`  | `fread`                  |
| Write     | `fprintf`, `fputs`, `fputc` | `fwrite`                 |
| Mode      | `"r"`, `"w"`, `"a"`         | `"rb"`, `"wb"`, `"ab"`   |
| Data      | Human-readable              | Raw memory               |
| Use cases | Logs, text files            | Structs, serialized data |

---

✅ **Takeaway:**

> File I/O in C revolves around `FILE*`.
> You open → operate → close.
> Use text mode for human-readable files, binary for performance and structured data.

---
---

# 🧩 7️⃣ **Unions and Shared Memory**

---

## 🧠 1️⃣ What is a `union`?

A **union** is like a `struct`, but instead of each member having **its own memory**,
**all members share the same memory space.**

That means:

* All union members **start at the same address**.
* The size of a union = size of its **largest member**.
* Writing to one member overwrites the others.

### Syntax:

```c
union Name {
    type1 member1;
    type2 member2;
    ...
};
```

---

## 🧩 2️⃣ Example: How unions share memory

```c
#include <stdio.h>

union Data {
    int i;
    float f;
    char c;
};

int main() {
    union Data d;
    d.i = 65;

    printf("i = %d\n", d.i);
    printf("f = %.2f\n", d.f);
    printf("c = %c\n", d.c);
}
```

### Output (example):

```
i = 65
f = 9.11e-44
c = A
```

Here:

* All three members (`i`, `f`, `c`) **occupy the same memory**.
* When you write `d.i = 65`, those bytes represent the number 65.
* Reading as a `char` → `'A'` (ASCII code 65).
* Reading as a `float` → nonsense (`9.11e-44`) because it’s interpreting the same bits differently.

---

## ⚙️ 3️⃣ Memory layout visualization

Let’s assume a 4-byte `union Data`:

```
Address →   0x1000  0x1001  0x1002  0x1003
             -----------------------------
Bytes  →   [  65    0x00    0x00    0x00  ]  ← when i=65
             \______\______\______\______/
               i, f, and c share this space
```

All members start at `0x1000`.
`sizeof(union Data)` = 4 (largest member = `int` or `float`).

---

## 🧠 4️⃣ Size of a union

```c
union Test {
    char c;
    int i;
    double d;
};

printf("%zu\n", sizeof(union Test));
```

✅ Output (on 64-bit system):

```
8
```

Because `double` (8 bytes) is the largest member.

---

## 🧩 5️⃣ Accessing union members

You can only access *one member at a time* (the one you last wrote).
C doesn’t keep track of which member is “active”; you must manage that yourself.

```c
union Data d;
d.f = 3.14;
printf("%f\n", d.f);  // ✅ ok
printf("%d\n", d.i);  // ⚠️ undefined behavior
```

---

## ⚙️ 6️⃣ Common use case — type punning

Sometimes, we intentionally reinterpret the same bytes as different types.

```c
#include <stdio.h>

union Converter {
    float f;
    unsigned int i;
};

int main() {
    union Converter c;
    c.f = 1.0;
    printf("Float 1.0 as hex = 0x%X\n", c.i);
}
```

✅ Output (IEEE-754 32-bit float representation):

```
Float 1.0 as hex = 0x3F800000
```

**Type punning** like this is often used in:

* Compilers/interpreters
* Graphics drivers
* Networking protocols
* Embedded systems (interpreting hardware registers)

⚠️ **Note:** In strict ISO C, type punning through unions is *technically* implementation-defined — but it’s widely supported (especially in GCC/Clang).

---

## 🧱 7️⃣ Unions inside structs (tagged unions)

Used to make *variant types* — same memory used for multiple interpretations.

Example:

```c
#include <stdio.h>

typedef struct {
    enum { INT, FLOAT } type;
    union {
        int i;
        float f;
    } value;
} Variant;

int main() {
    Variant v;
    v.type = INT;
    v.value.i = 42;
    printf("Stored int: %d\n", v.value.i);

    v.type = FLOAT;
    v.value.f = 3.14;
    printf("Stored float: %.2f\n", v.value.f);
}
```

✅ Output:

```
Stored int: 42
Stored float: 3.14
```

Here, the `enum` keeps track of **which field is valid** — this is called a **tagged union** (very common in interpreters, compilers, and message parsers).

---

## 🧠 8️⃣ Unions vs Structs

| Feature       | `struct`                             | `union`                          |
| ------------- | ------------------------------------ | -------------------------------- |
| Memory layout | Each member has its own space        | All members share the same space |
| Size          | Sum of member sizes (plus padding)   | Size of largest member           |
| Access        | All members can exist simultaneously | Only one valid at a time         |
| Use case      | Multiple related fields              | Multiple *alternative* fields    |

Example:

```c
struct Example {
    int i;
    float f;
};  // size ≈ 8

union Example {
    int i;
    float f;
};  // size ≈ 4
```

---

## 🧩 9️⃣ Practical use cases

| Use Case                     | Description                                               |
| ---------------------------- | --------------------------------------------------------- |
| **Type punning**             | Interpret data in multiple formats (e.g., bits to float). |
| **Tagged unions (variants)** | Represent values that can have different types.           |
| **Protocol parsers**         | Interpret network packets as multiple layouts.            |
| **Embedded systems**         | Read/write to same hardware register differently.         |
| **Memory optimization**      | Save space when only one field is used at a time.         |

---

## 🧠 10️⃣ Example — Packet interpretation (network-style)

```c
#include <stdio.h>

typedef union {
    struct { unsigned short x, y; } pos;
    unsigned int packed;
} Packet;

int main() {
    Packet p;
    p.pos.x = 10;
    p.pos.y = 20;
    printf("x=%u, y=%u, packed=0x%X\n", p.pos.x, p.pos.y, p.packed);
}
```

✅ Output (endianness-dependent):

```
x=10, y=20, packed=0x0014000A
```

This is **common in low-level networking**, where you pack coordinates, IDs, flags, etc., into one machine word.

---

## ⚠️ 11️⃣ Common pitfalls

❌ Accessing a field that wasn’t last written → **undefined behavior**.
❌ Assuming endianness (byte order) is the same across systems.
❌ Using unions in portable data formats (binary files) without defining structure explicitly.

---

## 🧩 12️⃣ Nested unions

You can have unions inside unions, or unions inside structs:

```c
struct Mixed {
    char label;
    union {
        int i;
        float f;
        char s[4];
    } data;
};
```

✅ Used to hold “either integer, float, or short string”.

---

## 🧱 13️⃣ Real-world examples

| Context                    | Usage                                       |
| -------------------------- | ------------------------------------------- |
| **Compilers/interpreters** | Storing constant types (int, float, string) |
| **Graphics engines**       | Reinterpreting float↔int bits               |
| **Embedded systems**       | Accessing register bits individually        |
| **File formats**           | Shared fields for text and binary types     |
| **Networking**             | Packing multiple fields into one integer    |

---

## 🧮 14️⃣ Advanced example: bitfields + union

```c
#include <stdio.h>

typedef union {
    unsigned int value;
    struct {
        unsigned int r:8;
        unsigned int g:8;
        unsigned int b:8;
        unsigned int a:8;
    } rgba;
} Color;

int main() {
    Color c;
    c.value = 0xFF112233;
    printf("R=%X G=%X B=%X A=%X\n", c.rgba.r, c.rgba.g, c.rgba.b, c.rgba.a);
}
```

✅ Output:

```
R=33 G=22 B=11 A=FF
```

💡 That’s how graphics code often extracts RGBA channels from a 32-bit color!

---

## 🧠 15️⃣ Size and alignment summary

| Rule            | Meaning                              |
| --------------- | ------------------------------------ |
| `sizeof(union)` | Size of largest member               |
| Alignment       | Equal to alignment of largest member |
| Shared memory   | All members start at offset 0        |

---

## ⚡ 16️⃣ Summary Table

| Concept        | Struct         | Union                  |
| -------------- | -------------- | ---------------------- |
| Memory sharing | No             | Yes                    |
| Active members | All            | One                    |
| Size           | Sum            | Max                    |
| Used for       | Grouped data   | Variant data           |
| Example        | Student record | Token type in compiler |

---

## 🚀 17️⃣ Key takeaway

> A **union** is a way to overlay different data types on the same memory region.

You decide how to interpret those bytes — that’s the **power and danger** of C.

Unions make C extremely efficient and flexible, but also let you shoot yourself in the foot if you forget which member is active.

---

✅ **Summary thought:**

> Use `union` when you want one piece of memory to hold *one of several possible data types at a time.*

---
---

# 🧩 8️⃣ **Preprocessor Directives in C**

---

## 🧠 1️⃣ What is the C Preprocessor?

Before your code is compiled, it goes through a **text substitution engine** called the **preprocessor** (`cpp`).

The preprocessor:

* Runs **before** the compiler.
* Handles **macros, includes, and conditional compilation**.
* Produces a “pure C” file that the compiler then compiles.

You can see the preprocessed code by running:

```bash
gcc -E main.c
```

This shows what the compiler actually sees after preprocessing.

---

## 🧩 2️⃣ Types of Preprocessor Directives

| Category           | Directive                                              | Purpose                     |
| ------------------ | ------------------------------------------------------ | --------------------------- |
| **File inclusion** | `#include`                                             | Add code from another file  |
| **Macros**         | `#define`, `#undef`                                    | Text substitution           |
| **Conditionals**   | `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#endif` | Compile parts conditionally |
| **Miscellaneous**  | `#error`, `#pragma`, `#line`                           | Control compiler behavior   |

---

## ⚙️ 3️⃣ File inclusion — `#include`

Tells the preprocessor to copy another file’s content here.

### Syntax:

```c
#include <stdio.h>   // system header
#include "myheader.h" // local header
```

* `<...>` → search system include directories.
* `"..."` → search current directory first, then system dirs.

✅ Used for:

* Linking library headers.
* Splitting code into `.c` and `.h` files.

---

## 🧩 4️⃣ Macros — `#define`

### Simple macro (constant)

```c
#define PI 3.14159
#define SIZE 100
```

Replaces every occurrence of `PI` and `SIZE` **before compilation**.

```c
float area = PI * r * r;
```

becomes:

```c
float area = 3.14159 * r * r;
```

---

### Macro with arguments

```c
#define SQUARE(x) ((x) * (x))
```

✅ Usage:

```c
printf("%d\n", SQUARE(5));  // 25
```

💡 Always use parentheses — otherwise:

```c
#define BAD_SQ(x) x*x
printf("%d\n", BAD_SQ(1+2)); // expands to 1+2*1+2 → 5 ❌
```

---

### Multi-line macros

Use backslash `\` to continue on the next line:

```c
#define DEBUG_PRINT(x) \
    printf("DEBUG: %s = %d\n", #x, x)
```

✅ `#x` converts the argument name to a string literal (stringizing operator).

Example:

```c
int a = 42;
DEBUG_PRINT(a);
```

Output:

```
DEBUG: a = 42
```

---

## 🧠 5️⃣ `#undef`

Undefines a macro:

```c
#define MAX 100
#undef MAX
```

Now `MAX` is no longer recognized.

---

## ⚙️ 6️⃣ Conditional compilation

Control *which parts* of the code are included based on conditions.

---

### `#ifdef` / `#ifndef`

```c
#ifdef DEBUG
printf("Debug info\n");
#endif
```

* `#ifdef` → executes if macro is defined.
* `#ifndef` → executes if macro is **not** defined.

---

### `#if` / `#elif` / `#else` / `#endif`

```c
#define VERSION 2

#if VERSION == 1
    printf("Old version\n");
#elif VERSION == 2
    printf("New version\n");
#else
    printf("Unknown version\n");
#endif
```

✅ This code compiles differently based on the macro value.

---

### Combining conditions

```c
#if defined(WINDOWS) || defined(LINUX)
    printf("Running on PC\n");
#endif
```

---

### Use in header guards (preview for next topic)

```c
#ifndef MY_HEADER_H
#define MY_HEADER_H

// contents

#endif
```

✅ Ensures the file is included only once.

---

## 🧩 7️⃣ Special macro operators

| Operator | Meaning     | Example                                         |
| -------- | ----------- | ----------------------------------------------- |
| `#`      | Stringize   | `#define STR(x) #x` → `STR(hi)` → `"hi"`        |
| `##`     | Token-paste | `#define CAT(a,b) a##b` → `CAT(var,1)` → `var1` |

Example:

```c
#define MAKE_FN(name) void name##_handler() { printf(#name " called\n"); }

MAKE_FN(keyboard)
MAKE_FN(mouse)

int main() {
    keyboard_handler();
    mouse_handler();
}
```

✅ Output:

```
keyboard called
mouse called
```

---

## ⚙️ 8️⃣ Predefined macros

C provides several predefined macros (auto-defined by compiler):

| Macro      | Meaning                           |
| ---------- | --------------------------------- |
| `__FILE__` | Current filename                  |
| `__LINE__` | Current line number               |
| `__DATE__` | Compilation date                  |
| `__TIME__` | Compilation time                  |
| `__func__` | Current function name (C99+)      |
| `__STDC__` | Defined if compiler follows ISO C |

Example:

```c
printf("File: %s, Line: %d\n", __FILE__, __LINE__);
```

Output:

```
File: main.c, Line: 10
```

---

## 🧠 9️⃣ `#error` and `#pragma`

### `#error`

Force a compile-time error (good for enforcing requirements):

```c
#ifndef LINUX
#error "This code only builds on Linux"
#endif
```

### `#pragma`

Gives special instructions to the compiler.

Examples:

```c
#pragma once       // modern alternative to include guards
#pragma pack(1)    // no padding in structs
```

Compiler-specific pragmas exist (e.g., GCC, MSVC).

---

## ⚙️ 10️⃣ `#line`

Changes the compiler’s reported line number or file name.

Used mainly in code generators or debugging:

```c
#line 100 "generated_code.c"
```

Now the compiler thinks the next line is line 100 in “generated_code.c”.

---

## 🧩 11️⃣ How preprocessing actually works

Given:

```c
#define X 5
#define Y (X+1)
int a = Y;
```

After preprocessing (run `gcc -E file.c`):

```c
int a = (5+1);
```

✅ The preprocessor works **purely by text substitution**, no type-checking or evaluation yet.

---

## ⚠️ 12️⃣ Common pitfalls

❌ Using macros instead of `const` when possible
→ Macros don’t respect scope or type safety.

```c
#define LIMIT 10
const int limit = 10; // ✅ better
```

❌ Forgetting parentheses in macro parameters
→ Operator precedence bugs.

❌ Using complex macros instead of inline functions
→ Use `inline` functions when possible — they’re safer and debuggable.

---

## 🧩 13️⃣ Real-world uses of preprocessor directives

| Use Case                | Directive                               |
| ----------------------- | --------------------------------------- |
| **Cross-platform code** | `#ifdef WINDOWS` / `#ifdef LINUX`       |
| **Debug vs release**    | `#ifdef DEBUG`                          |
| **Versioning**          | `#if VERSION >= 2`                      |
| **Compile-time checks** | `#error` for unsupported configs        |
| **Logging**             | `#define LOG(...)` macro wrappers       |
| **Performance toggles** | Enable/disable features at compile time |

---

## 🧠 14️⃣ Example: compile-time debug logging

```c
#include <stdio.h>

#define DEBUG 1

#if DEBUG
    #define LOG(msg) printf("DEBUG: %s:%d: %s\n", __FILE__, __LINE__, msg)
#else
    #define LOG(msg)
#endif

int main() {
    LOG("Program started");
}
```

✅ Output:

```
DEBUG: main.c:10: Program started
```

If you `#undef DEBUG`, all logs disappear without changing code logic — pure compile-time control.

---

## 🧬 15️⃣ Order of preprocessor execution

1. Remove comments
2. Process `#define` and macros
3. Process includes (`#include`)
4. Evaluate conditionals (`#if`, `#ifdef`)
5. Produce final expanded C source

---

## ⚡ 16️⃣ Summary Table

| Directive          | Purpose             | Example               |
| ------------------ | ------------------- | --------------------- |
| `#include`         | Include files       | `#include <stdio.h>`  |
| `#define`          | Define macros       | `#define PI 3.14`     |
| `#undef`           | Remove macro        | `#undef PI`           |
| `#if/#else/#endif` | Conditional compile | `#if DEBUG`           |
| `#ifdef/#ifndef`   | Check if defined    | `#ifdef DEBUG`        |
| `#error`           | Force error         | `#error "Bad config"` |
| `#pragma`          | Compiler control    | `#pragma once`        |
| `#line`            | Change line info    | `#line 100 "fake.c"`  |

---

✅ **Key takeaway:**

> The **preprocessor** runs before compilation, performing text substitution, conditional compilation, and file inclusion — giving you dynamic control over what gets compiled and how.

It’s the backbone of **cross-platform C**, **configurable builds**, and **macro-based frameworks**.

---
---

# 🧩 9️⃣ **Header Guards**

---

## 🧠 1️⃣ What is a header file?

A **header file** (`.h`) contains:

* Function declarations
* Struct and type definitions
* Macros and constants
* External variable declarations

It’s meant to be shared among multiple `.c` files.

Example:

```c
// mathutils.h
int add(int a, int b);
```

```c
// main.c
#include "mathutils.h"
#include "mathutils.h"  // accidentally included twice
```

Without protection, this causes **duplicate definition or redefinition errors**.

---

## ⚠️ 2️⃣ The multiple inclusion problem

When you include the same header file in more than one place (directly or indirectly),
the compiler might see the same code **twice**.

Example:

```c
// file1.h
int a;

// file2.h
#include "file1.h"
#include "file1.h"
```

Compiler sees:

```c
int a;
int a; // ❌ redefinition error
```

This becomes worse when one header includes another that also includes the same file.

---

## 🧩 3️⃣ The solution — Header Guards

A **header guard** ensures the file’s content is included only once per compilation unit.

### Basic pattern:

```c
#ifndef HEADER_NAME_H
#define HEADER_NAME_H

// header contents go here

#endif
```

---

## 🧠 4️⃣ How it works

Let’s break it down:

1. `#ifndef HEADER_NAME_H`
   → “If `HEADER_NAME_H` is *not* defined...”
2. `#define HEADER_NAME_H`
   → “Define it, so next time this header is included, skip it.”
3. `#endif`
   → Closes the block.

So, when the preprocessor processes the same file again:

* It sees that `HEADER_NAME_H` **is already defined**,
* So it **skips the entire content** inside the guard.

---

### Example:

#### `mathutils.h`

```c
#ifndef MATHUTILS_H
#define MATHUTILS_H

int add(int, int);
int sub(int, int);

#endif
```

#### `main.c`

```c
#include "mathutils.h"
#include "mathutils.h" // second inclusion ignored
```

✅ Output: no error — header included only once.

---

## ⚙️ 5️⃣ Naming conventions for header guards

By convention:

* All uppercase.
* Use underscores.
* End with `_H` or `_H_`.
* Include project/module name to avoid clashes.

Examples:

```c
#ifndef PROJECT_MATHUTILS_H
#define PROJECT_MATHUTILS_H
...
#endif
```

```c
#ifndef _LIST_NODE_H_
#define _LIST_NODE_H_
...
#endif
```

---

## 🧱 6️⃣ Visual explanation

| Step | Action                                                              |
| ---- | ------------------------------------------------------------------- |
| ①    | File is first included → macro not defined → file contents included |
| ②    | Macro defined inside                                                |
| ③    | Second inclusion → macro already defined → contents skipped         |

```
#include "file.h"    ← included
#include "file.h"    ← skipped
```

---

## 🧩 7️⃣ Example of indirect inclusion

#### `a.h`

```c
#ifndef A_H
#define A_H
int funcA();
#endif
```

#### `b.h`

```c
#ifndef B_H
#define B_H
#include "a.h"
#endif
```

#### `main.c`

```c
#include "a.h"
#include "b.h"
```

Even though `a.h` is included twice (once directly, once via `b.h`),
the header guard ensures it’s only compiled once. ✅

---

## 🧠 8️⃣ Alternative: `#pragma once`

Modern compilers (GCC, Clang, MSVC) support a simpler version:

```c
#pragma once

// header contents
```

✅ Automatically ensures file is included only once.
✅ No need for macros.
⚠️ Non-standard (not in ISO C, but universally supported today).

---

## 🧩 9️⃣ Header guards vs `#pragma once`

| Feature     | Header Guard                   | `#pragma once`                                   |
| ----------- | ------------------------------ | ------------------------------------------------ |
| Standard?   | ✅ Yes (pure C)                 | ⚠️ Non-standard, but supported by most compilers |
| Portability | Works everywhere               | Works in 99% of compilers                        |
| Flexibility | You choose macro name          | Compiler-managed                                 |
| Speed       | Slightly slower (macro lookup) | Slightly faster (compiler caches file)           |

In practice:

* Use `#pragma once` for modern code.
* Use traditional guards for maximum portability (especially embedded or old compilers).

---

## ⚙️ 10️⃣ Typical header file structure

```c
#ifndef PROJECT_MYHEADER_H
#define PROJECT_MYHEADER_H

#include <stdio.h>  // system includes

#define PI 3.14159

typedef struct {
    int x, y;
} Point;

int add(int a, int b);
void print_point(Point p);

#endif // PROJECT_MYHEADER_H
```

✅ Clean, readable, safe.

---

## 🧠 11️⃣ Why header guards matter

In larger projects:

```c
main.c
 ↳ engine.h
     ↳ utils.h
         ↳ config.h
 ↳ config.h   ← included again
```

Without guards → compiler sees `config.h` twice → duplicate definitions.
With guards → second inclusion skipped automatically.

---

## 🧩 12️⃣ Common mistakes

❌ Forgetting to close with `#endif` → compilation error.
❌ Using different macro name in `#ifndef` and `#define`.
❌ Using very generic macro name like `#ifndef DATA_H` (risk of collision).
✅ Use unique prefix like `PROJECT_MODULE_FILE_H`.

---

## 🧬 13️⃣ Header guards in real projects

| Project      | Style                    |
| ------------ | ------------------------ |
| Linux kernel | `#ifndef _LINUX_SCHED_H` |
| OpenSSL      | `#ifndef HEADER_AES_H`   |
| SDL          | `#ifndef SDL_video_h_`   |
| GCC          | `#ifndef GCC_TREE_H`     |

✅ Every serious C project uses guards or `#pragma once`.

---

## ⚡ 14️⃣ Summary Table

| Directive      | Purpose                   | Example               |
| -------------- | ------------------------- | --------------------- |
| `#ifndef`      | If not defined            | `#ifndef MATHUTILS_H` |
| `#define`      | Define a macro            | `#define MATHUTILS_H` |
| `#endif`       | End condition             | Closes guard          |
| `#pragma once` | Single inclusion (modern) | No macros needed      |

---

## ✅ 15️⃣ Key takeaway

> Header guards are **compile-time safety nets**.
> They prevent duplicate inclusions, redefinitions, and linkage errors,
> ensuring that every `.h` file is compiled only once per translation unit.

---

### 🧠 Rule of thumb:

* Always wrap your headers in guards or use `#pragma once`.
* Name guards uniquely: `PROJECT_MODULENAME_H`.
* Never define actual variables in headers (only declarations).

---
---

# 🧩 10️⃣ **Storage-Class Specifiers in C**

---

## 🧠 1️⃣ What are storage-class specifiers?

Storage-class specifiers in C control **how and where** variables and functions are stored, and **how long** they exist in memory.

They determine:

1. **Lifetime** → How long the variable exists.
2. **Scope** → Where it is visible.
3. **Linkage** → Whether it can be shared across files.

---

## 🧩 2️⃣ The four main storage-class specifiers

| Specifier  | Purpose                                                 | Typical Usage          |
| ---------- | ------------------------------------------------------- | ---------------------- |
| `auto`     | Default for local variables                             | Rarely used explicitly |
| `static`   | Persist between function calls or hide from other files | Functions, globals     |
| `extern`   | Declare a global variable defined elsewhere             | Cross-file sharing     |
| `register` | Suggest CPU register storage (obsolete hint)            | Performance hint       |

C also uses **type qualifiers** like:

* `const` — read-only protection
* `volatile` — disable compiler optimizations for unpredictable values

We’ll include those here, since they often come together.

---

## ⚙️ 3️⃣ Understanding scope, lifetime, and linkage

| Storage class     | Scope          | Lifetime                | Linkage  |
| ----------------- | -------------- | ----------------------- | -------- |
| Local (`auto`)    | Function/block | Temporary (stack)       | None     |
| `static` (local)  | Function/block | Permanent (global data) | None     |
| `static` (global) | File           | Permanent               | Internal |
| `extern`          | Global         | Permanent               | External |
| `register`        | Function/block | Temporary               | None     |

---

## 🧩 4️⃣ `auto` (default local variable)

`auto` is the **default** storage class for local (function) variables.

```c
void foo() {
    auto int x = 5; // same as int x = 5;
}
```

* Exists only while the function executes.
* Stored on the **stack**.
* Re-created every time the function runs.

✅ Rarely written explicitly — redundant.

---

## ⚙️ 5️⃣ `static` — the most powerful and misunderstood one

`static` changes **lifetime** and/or **linkage**, depending on where it’s used.

---

### a) `static` inside a function (local static)

```c
void counter() {
    static int count = 0;
    count++;
    printf("count = %d\n", count);
}
```

Each time you call `counter()`,
the variable `count` **retains its value** between calls.

✅ Output:

```
count = 1
count = 2
count = 3
```

* Stored in **data segment**, not stack.
* **Lifetime:** whole program.
* **Scope:** function only (not visible outside).

---

### b) `static` for global variables or functions (file scope)

```c
static int global = 10;  // visible only in this .c file
static void helper() { printf("internal\n"); }
```

* Variable/function is **visible only inside this file**.
* Other `.c` files can’t access it (even with `extern`).
* Prevents *name collisions* across modules.

✅ Used for encapsulation (like “private” in C).

---

### c) Summary of `static`

| Context         | Scope    | Lifetime | Linkage  |
| --------------- | -------- | -------- | -------- |
| Inside function | Function | Program  | None     |
| At global level | File     | Program  | Internal |

---

## 🧠 6️⃣ `extern` — “I exist in another file”

Used to **declare** a global variable or function defined elsewhere.

```c
// file1.c
int counter = 0;
```

```c
// file2.c
extern int counter;
void increment() { counter++; }
```

✅ `extern` tells the compiler:

> “This variable is defined in another file — don’t allocate it again, just link to it.”

Without `extern`, if you re-declare it, you’d create a duplicate variable → *linker error*.

---

### Function declarations are `extern` by default

```c
int printf(const char *, ...); // implicitly extern
```

No need to write `extern` manually.

---

### Global scope summary

| Specifier | Visible in other files? | Description      |
| --------- | ----------------------- | ---------------- |
| `static`  | ❌ No                    | Internal linkage |
| `extern`  | ✅ Yes                   | External linkage |

---

## ⚙️ 7️⃣ `register` — a hint to store in CPU registers

```c
void sum() {
    register int i;
    for (i = 0; i < 10; i++) printf("%d ", i);
}
```

* Tells compiler “store this in a CPU register (if possible).”
* No guarantees — compiler decides.
* You **can’t take the address** of a register variable:

  ```c
  register int x;
  printf("%p", &x); // ❌ error
  ```

💡 Modern compilers ignore this — optimization is automatic.

---

## 🧩 8️⃣ `const` — read-only protection

Declares a variable **whose value cannot be modified** after initialization.

```c
const int max = 10;
max = 20; // ❌ error
```

But note: `const` affects **modifiability**, not **storage**.

### With pointers:

```c
int x = 5;
const int *p = &x;   // pointer to const int (value cannot change via *p)
int *const q = &x;   // const pointer (address cannot change)
```

| Declaration          | Meaning                                       |
| -------------------- | --------------------------------------------- |
| `const int *p`       | “pointer to const int” — can’t change value   |
| `int *const p`       | “const pointer to int” — can’t change pointer |
| `const int *const p` | both const                                    |

---

## 🧠 9️⃣ `volatile` — tells the compiler “don’t optimize me!”

Used for variables whose value can change **outside program control** (like hardware registers, interrupts, or threads).

Example:

```c
volatile int status;
while (status == 0);  // wait for hardware flag
```

✅ Without `volatile`, compiler might optimize the loop to:

```c
while (1); // assumes status never changes (wrong!)
```

So `volatile` prevents such optimizations — the variable is always **re-read from memory**.

---

## ⚙️ 10️⃣ Combining `const` and `volatile`

Sometimes you need **both**:

```c
const volatile int input_reg = 0x4000;
```

* `const` → program doesn’t change it.
* `volatile` → hardware *can* change it (e.g., sensors, timers).

---

## 🧩 11️⃣ Putting it all together

Example combining everything:

```c
#include <stdio.h>

int global = 5;         // external linkage
static int hidden = 10; // internal linkage

void foo(void) {
    static int call_count = 0; // retains value
    register int i;            // maybe optimized
    const int limit = 3;       // read-only
    volatile int flag = 1;     // unpredictable value

    call_count++;
    for (i = 0; i < limit; i++)
        printf("Run %d\n", call_count);

    if (flag) printf("Flag set!\n");
}
```

---

## 🧠 12️⃣ Summary Table

| Specifier         | Scope   | Lifetime      | Linkage  | Meaning                 |
| ----------------- | ------- | ------------- | -------- | ----------------------- |
| `auto`            | Local   | Function      | None     | Default for locals      |
| `static` (local)  | Local   | Whole program | None     | Retains value           |
| `static` (global) | File    | Whole program | Internal | Hidden from other files |
| `extern`          | Global  | Whole program | External | Declared elsewhere      |
| `register`        | Local   | Function      | None     | Hint for CPU register   |
| `const`           | Depends | Depends       | —        | Read-only               |
| `volatile`        | Depends | Depends       | —        | No optimization         |

---

## ⚙️ 13️⃣ Memory segment overview

| Segment   | Contains                          | Example                  |
| --------- | --------------------------------- | ------------------------ |
| **Text**  | Code                              | Function bodies          |
| **Data**  | Initialized globals/static vars   | `int x = 10;`            |
| **BSS**   | Uninitialized globals/static vars | `static int y;`          |
| **Stack** | Local vars                        | `int a;` inside function |
| **Heap**  | Dynamic memory                    | `malloc()`               |

`static`, `extern`, and `const` usually go in the **data/BSS** segments,
`auto` and `register` go in the **stack**.

---

## ⚡ 14️⃣ Real-world usage patterns

| Use case                   | Keyword          | Example                                  |
| -------------------------- | ---------------- | ---------------------------------------- |
| Persistent local state     | `static`         | Counter inside a function                |
| Hide internal globals      | `static`         | Helper variable or function in a .c file |
| Share globals across files | `extern`         | Shared config or flag                    |
| Read-only constants        | `const`          | `const double PI = 3.14159;`             |
| Hardware register          | `volatile`       | `volatile int *UART = (int*)0x4000;`     |
| Combined hardware register | `const volatile` | read-only hardware input port            |

---

## 🧠 15️⃣ Best practices

✅ Use `static` for all internal globals — avoid polluting global namespace.
✅ Use `const` for constants instead of `#define`.
✅ Use `volatile` for hardware or multithreading.
✅ Use `extern` only in headers (not in `.c` definitions).
✅ Don’t use `register` — modern compilers do it automatically.

---

## 🚀 16️⃣ Key takeaway

> Storage-class specifiers control **visibility, lifetime, and linkage** —
> essentially, *who can see a variable, how long it lives, and where it resides in memory.*

They bridge the gap between **compiler theory** and **runtime behavior** — essential knowledge for systems, embedded, and OS-level C programming.

---
---

# 🧩 11️⃣ **Segmentation Faults, Stack vs Heap**

---

## 🧠 1️⃣ What is a segmentation fault?

A **segmentation fault** (or **segfault**) occurs when your program tries to **access memory it doesn’t own**.

It’s the OS’s way of saying:

> “You just touched memory outside your permitted segment.”

When this happens, the CPU triggers a hardware **memory protection fault**, and the OS **kills the process**.

---

## 💀 2️⃣ Common causes of segmentation faults

| Cause                                               | Example                                      |
| --------------------------------------------------- | -------------------------------------------- |
| ❌ Dereferencing a NULL pointer                      | `int *p = NULL; *p = 10;`                    |
| ❌ Dereferencing an uninitialized pointer            | `int *p; *p = 10;`                           |
| ❌ Accessing freed memory                            | `free(p); *p = 5;`                           |
| ❌ Writing past array bounds                         | `int a[3]; a[5] = 10;`                       |
| ❌ Stack overflow (too deep recursion or big arrays) | Recursive calls or `int a[10000000];`        |
| ❌ Incorrect pointer arithmetic                      | `*(p + 100)` when array has only 10 elements |

---

## 🧱 3️⃣ Memory layout of a typical C program

Here’s how a process’s memory is structured:

```
   High addresses
   ┌───────────────────────────┐
   │ Stack (grows down)        │ ← local variables, function calls
   ├───────────────────────────┤
   │ Unused                    │
   ├───────────────────────────┤
   │ Heap (grows up)           │ ← malloc(), calloc(), realloc()
   ├───────────────────────────┤
   │ BSS segment               │ ← uninitialized static/global vars
   ├───────────────────────────┤
   │ Data segment              │ ← initialized static/global vars
   ├───────────────────────────┤
   │ Text segment (code)       │ ← compiled machine instructions
   └───────────────────────────┘
   Low addresses
```

📍 Note:

* **Stack** grows *downward* (toward lower addresses).
* **Heap** grows *upward* (toward higher addresses).

When these regions collide (stack ↔ heap), you get *stack overflow* or *out-of-memory* errors.

---

## 🧩 4️⃣ Stack vs Heap: quick comparison

| Feature       | Stack                    | Heap                                   |
| ------------- | ------------------------ | -------------------------------------- |
| Managed by    | Compiler                 | Programmer                             |
| Allocation    | Automatic                | Manual (`malloc`, `calloc`, `realloc`) |
| Lifetime      | Ends when function exits | Persists until `free()`                |
| Speed         | Very fast                | Slower                                 |
| Size          | Limited (MBs)            | Large (GBs, OS-dependent)              |
| Common errors | Stack overflow           | Memory leaks, use-after-free           |

---

## ⚙️ 5️⃣ Stack memory — automatic allocation

When you declare a variable inside a function:

```c
void foo() {
    int x = 10;   // stored on stack
}
```

* Allocated when `foo()` is called.
* Freed when `foo()` returns.
* You **must not** return its address!

Example ❌:

```c
int* bad() {
    int x = 10;
    return &x; // returns address of destroyed variable
}
```

The returned pointer now points to *invalid stack memory* → segfault if dereferenced.

✅ Correct version:

```c
int* good() {
    int *p = malloc(sizeof(int));
    *p = 10;
    return p; // valid heap memory
}
```

---

## 🧠 6️⃣ Heap memory — manual allocation

When you need memory that **outlives a function**, you use `malloc()` or friends.

```c
int *p = malloc(sizeof(int));
*p = 42;
free(p);
```

* Heap memory stays valid until you `free()` it.
* Forgetting to `free()` causes **memory leaks**.
* Using after `free()` causes **use-after-free** (undefined behavior → segfault).

---

## 🧩 7️⃣ Example: Segfault from use-after-free

```c
int *p = malloc(sizeof(int));
*p = 10;
free(p);
printf("%d\n", *p); // ❌ undefined behavior (segfault)
```

✅ Fix:

```c
free(p);
p = NULL;  // safe guard
```

Now dereferencing `p` will cause a **clear NULL segfault**, not random memory corruption.

---

## ⚙️ 8️⃣ Example: Stack overflow (too deep recursion)

```c
void recurse() {
    int x[1000]; // each call allocates 4KB
    recurse();   // infinite recursion → crash
}
int main() {
    recurse();
}
```

💥 Eventually, the stack pointer exceeds allowed memory (e.g., 8 MB on Linux),
and the OS kills the process with `Segmentation fault (core dumped)`.

---

## 🧠 9️⃣ Example: Writing beyond array bounds

```c
int a[3];
a[5] = 10;  // ❌ writing past end
```

This corrupts **neighboring memory** on stack, often overwriting:

* Return addresses
* Saved registers
* Local variables

This can cause unpredictable behavior or immediate crash.

✅ Always ensure valid indices:

```c
if (i >= 0 && i < 3)
    a[i] = 10;
```

---

## 🧩 10️⃣ Stack vs Heap visual comparison

```
STACK                HEAP
-----                -----
int x = 10;          int *p = malloc(4);
(pushed automatically)  (allocated manually)

Scope: function only   Scope: until free()
Lifetime: auto         Lifetime: manual
```

---

## ⚙️ 11️⃣ Real-world debugging: `gdb`

Run your program with:

```bash
gdb ./a.out
(gdb) run
(gdb) backtrace
```

Example output:

```
Program received signal SIGSEGV, Segmentation fault.
0x000055555555515a in main () at main.c:5
5       *p = 10;
```

This shows **where** the segfault occurred.

---

## 🧠 12️⃣ Example: Heap buffer overflow

```c
int *p = malloc(3 * sizeof(int));
for (int i = 0; i < 10; i++) // ❌ too many writes
    p[i] = i;
```

Writes beyond allocated heap block — may:

* Corrupt the allocator’s metadata
* Crash immediately
* Or cause strange crashes later

✅ Fix:

```c
for (int i = 0; i < 3; i++) p[i] = i;
```

---

## 🧩 13️⃣ Detecting memory errors with Valgrind

Valgrind is a tool that detects:

* Invalid reads/writes
* Leaks
* Use-after-free

```bash
valgrind --leak-check=full ./a.out
```

Output example:

```
Invalid write of size 4
    at main.c:8
    Address 0x51f1044 is 0 bytes after a block of size 12
```

💡 It literally tells you where you messed up memory.

---

## ⚙️ 14️⃣ Stack and Heap collisions (rare but real)

If you allocate too much stack (deep recursion or huge local arrays),
and also allocate large heap chunks,
they may **collide** in the virtual address space.

```c
int big[100000000];  // 400 MB → crash immediately
```

✅ Fix: use `malloc()` for large data structures.

---

## 🧠 15️⃣ Memory corruption symptoms

| Symptom                                | Possible cause                       |
| -------------------------------------- | ------------------------------------ |
| Random segfaults                       | Writing outside array bounds         |
| Program runs fine, then crashes later  | Use-after-free                       |
| Variables mysteriously change values   | Stack overwrite                      |
| Different behavior on debug vs release | Undefined behavior due to memory bug |

---

## 🧩 16️⃣ Stack vs Heap summary table

| Feature     | Stack               | Heap                      |
| ----------- | ------------------- | ------------------------- |
| Managed by  | Compiler            | Programmer                |
| Created via | Local variables     | `malloc()`, `calloc()`    |
| Freed by    | Automatically       | `free()`                  |
| Size        | Limited (a few MBs) | Large (depends on RAM/OS) |
| Speed       | Very fast           | Slower                    |
| Lifetime    | Function scope      | Until manually freed      |
| Errors      | Stack overflow      | Leaks, use-after-free     |

---

## ⚠️ 17️⃣ Preventing segmentation faults

✅ Initialize all pointers:

```c
int *p = NULL;
```

✅ Always allocate before dereferencing:

```c
p = malloc(sizeof(int));
```

✅ Free properly and nullify:

```c
free(p);
p = NULL;
```

✅ Use safe array access:

```c
if (i < N) arr[i] = val;
```

✅ Don’t return addresses of local variables.
✅ Prefer dynamic allocation for large data.
✅ Use Valgrind to detect hidden memory issues.

---

## 🧬 18️⃣ Example: full demo

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = malloc(3 * sizeof(int));
    for (int i = 0; i < 3; i++)
        p[i] = i * 10;

    for (int i = 0; i < 3; i++)
        printf("%d ", p[i]);

    free(p);
    p = NULL;

    // Uncomment to trigger segfault:
    // printf("%d", *p);  // deref after free
}
```

✅ Output:

```
0 10 20
```

❌ Uncommenting the last line gives:

```
Segmentation fault (core dumped)
```

---

## 🧠 19️⃣ Key mental model

```
Stack = automatic, temporary, fast
Heap  = manual, persistent, flexible
Segfault = trying to touch memory you don't own
```

---

## 🚀 20️⃣ Summary

| Concept                | Description                                |
| ---------------------- | ------------------------------------------ |
| **Segmentation fault** | Accessing memory not owned by your process |
| **Stack**              | Local variables; grows down; auto-managed  |
| **Heap**               | Dynamically allocated memory; grows up     |
| **Stack overflow**     | Too much recursion or large locals         |
| **Use-after-free**     | Accessing freed heap memory                |
| **Buffer overflow**    | Writing past allocated bounds              |

---

✅ **Key takeaway:**

> A segmentation fault isn’t a random error — it’s your OS protecting memory boundaries.
> If you understand the stack and heap layout, you can always find *why* it happened.

---
---

# 🧩 12️⃣ **Memory Leaks and `valgrind`**

---

## 🧠 1️⃣ What is a memory leak?

A **memory leak** occurs when:

> You allocate memory on the heap but never `free()` it.

That memory remains “reserved” by your process,
even though your program no longer has a pointer to access it.

Since only the OS can reclaim it after your program ends,
if this happens in a long-running process (like a server or daemon),
it gradually **consumes all RAM**.

---

## ⚙️ 2️⃣ Simple example

```c
#include <stdlib.h>

void leak() {
    int *p = malloc(sizeof(int) * 5);
    p[0] = 42;
} // ❌ no free()
```

✅ The memory allocated is never freed.
When `leak()` returns, `p` goes out of scope — you **lose the only reference** to that memory.
It’s still allocated in the heap, but you can’t access or release it anymore.

💡 After a few thousand iterations, your memory usage skyrockets.

---

## 🧱 3️⃣ Correct version

```c
#include <stdlib.h>

void no_leak() {
    int *p = malloc(sizeof(int) * 5);
    p[0] = 42;
    free(p);  // ✅ memory freed
}
```

Always **pair every `malloc()` with a `free()`**.

---

## 🧩 4️⃣ Common causes of memory leaks

| Cause                         | Example                                     |
| ----------------------------- | ------------------------------------------- |
| ❌ Forgetting to `free()`      | `p = malloc(...); // but never free(p)`     |
| ❌ Losing pointer reference    | `p = malloc(...); p = NULL;`                |
| ❌ Early return or error path  | Forgetting to free before `return`          |
| ❌ Allocating in loops         | Memory allocated repeatedly without freeing |
| ❌ Not freeing nested pointers | In structs that contain dynamic arrays      |

---

### Example: Losing the reference

```c
int *p = malloc(100);
p = malloc(200); // ❌ leak: old 100 bytes lost
free(p);         // only frees new one
```

✅ Correct way:

```c
free(p);
p = malloc(200);
```

---

## ⚙️ 5️⃣ Example: multiple leaks in one program

```c
#include <stdlib.h>
#include <string.h>

int main() {
    char *name = malloc(50);
    strcpy(name, "Yuvraj");

    int *arr = malloc(10 * sizeof(int));

    // Oops, forgot to free name and arr
    return 0;
}
```

✅ Fix:

```c
free(name);
free(arr);
```

---

## 🧠 6️⃣ Why memory leaks are dangerous

* In short-lived programs → mostly harmless.
* In long-running programs (servers, daemons, simulations):

  * Memory usage keeps increasing.
  * System starts swapping.
  * Eventually → **Out of Memory (OOM)** → process killed.

💡 Think of it like “forgetting to put dishes away after eating” —
one meal is fine, a year later your kitchen’s a mess.

---

## ⚙️ 7️⃣ Detecting leaks manually (bad idea)

You could manually track allocations:

```c
static int allocated = 0;
void *track_malloc(size_t size) {
    allocated += size;
    return malloc(size);
}
void track_free(void *ptr, size_t size) {
    allocated -= size;
    free(ptr);
}
```

But that’s tedious, error-prone, and doesn’t handle nested structures.

Instead: use **Valgrind** 🔍

---

# 🧰 8️⃣ `valgrind` — The Memory Detective

Valgrind is a **dynamic analysis tool** that runs your program inside a virtual machine to track:

* Memory leaks
* Invalid reads/writes
* Use-after-free
* Double frees
* Uninitialized memory access

---

## ⚙️ 9️⃣ Installing Valgrind (Linux)

On Arch:

```bash
sudo pacman -S valgrind
```

On Ubuntu/Debian:

```bash
sudo apt install valgrind
```

---

## 🧠 10️⃣ Basic usage

Compile your program with debug symbols:

```bash
gcc -g main.c -o main
```

Then run:

```bash
valgrind --leak-check=full ./main
```

---

### Example output (with leak):

```bash
==30281== HEAP SUMMARY:
==30281==     in use at exit: 200 bytes in 2 blocks
==30281==   total heap usage: 2 allocs, 0 frees, 200 bytes allocated
==30281==
==30281== 200 bytes in 2 blocks are definitely lost in loss record 1 of 1
==30281==    at 0x4C2EFD8: malloc (vg_replace_malloc.c:309)
==30281==    by 0x400566: main (main.c:5)
==30281==
==30281== LEAK SUMMARY:
==30281==    definitely lost: 200 bytes in 2 blocks
==30281==    indirectly lost: 0 bytes in 0 blocks
==30281==      possibly lost: 0 bytes in 0 blocks
==30281==    still reachable: 0 bytes in 0 blocks
==30281==         suppressed: 0 bytes in 0 blocks
==30281== ERROR SUMMARY: 0 errors from 0 contexts
```

---

✅ **Key sections:**

* `definitely lost` → real memory leaks (no pointer to block remains)
* `indirectly lost` → leaked through another leaked pointer
* `still reachable` → memory still has references (not freed but not lost)
* `suppressed` → ignored by config

---

## 🧩 11️⃣ Example program with Valgrind output

### Code:

```c
#include <stdlib.h>
int main() {
    int *p = malloc(10 * sizeof(int));
    p[0] = 42;
    return 0;  // forgot to free
}
```

### Run:

```bash
valgrind --leak-check=full ./a.out
```

### Output:

```
==5551== HEAP SUMMARY:
==5551==    definitely lost: 40 bytes in 1 blocks
==5551== LEAK SUMMARY:
==5551==    definitely lost: 40 bytes in 1 blocks
```

✅ “Definitely lost” = memory leak confirmed.

---

## ⚙️ 12️⃣ Fixing the leak

```c
#include <stdlib.h>
int main() {
    int *p = malloc(10 * sizeof(int));
    p[0] = 42;
    free(p);
    return 0;
}
```

✅ Output after rerunning:

```
All heap blocks were freed -- no leaks are possible
```

---

## 🧠 13️⃣ Detecting other issues with Valgrind

### 🔸 Use-after-free:

```c
int *p = malloc(4);
free(p);
*p = 10;  // ❌
```

Valgrind:

```
Invalid write of size 4
```

### 🔸 Uninitialized variable:

```c
int *p = malloc(sizeof(int));
printf("%d", *p); // ❌
```

Valgrind:

```
Use of uninitialized value
```

---

## 🧩 14️⃣ Memory leak categories (Valgrind terms)

| Category            | Meaning                                                             |
| ------------------- | ------------------------------------------------------------------- |
| **Definitely lost** | You lost all pointers → true leak                                   |
| **Indirectly lost** | Leaked object is referenced only by another leaked object           |
| **Still reachable** | Not freed but still accessible (not harmful in short-lived program) |
| **Suppressed**      | Ignored via suppression rules                                       |

---

## ⚙️ 15️⃣ Typical memory leak patterns

| Pattern                                   | Example                        |
| ----------------------------------------- | ------------------------------ |
| Forgetting `free()`                       | Common in loops                |
| Overwriting pointer                       | `p = malloc(); p = malloc();`  |
| Missing `free()` in error paths           | Early returns or failed checks |
| Leaks in structs                          | Forget to free inner fields    |
| Not freeing dynamically allocated strings | `strdup()` results not freed   |

---

## 🧠 16️⃣ Detecting leaks in complex programs

For large projects, use:

```bash
valgrind --track-origins=yes --leak-check=full --show-leak-kinds=all ./program
```

* `--track-origins=yes` → tells you *where* uninitialized memory came from.
* `--show-leak-kinds=all` → show all leak categories.

---

## 🧩 17️⃣ Preventing memory leaks

✅ **Always pair malloc/free.**

```c
void *ptr = malloc(...);
if (!ptr) exit(1);
free(ptr);
```

✅ **Set freed pointers to NULL.**

```c
free(ptr);
ptr = NULL;
```

✅ **Check allocations.**

```c
int *p = malloc(10 * sizeof(int));
if (p == NULL) { perror("malloc failed"); exit(1); }
```

✅ **Free in reverse order of allocation.**

✅ **Use tools regularly** (Valgrind, AddressSanitizer, etc.)

---

## 🧠 18️⃣ Memory safety tools (besides Valgrind)

| Tool                        | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| **AddressSanitizer (ASan)** | Built into GCC/Clang: detects buffer overflows and leaks. |
| **Valgrind**                | Detects leaks and invalid accesses.                       |
| **ElectricFence**           | Detects buffer overruns (old but simple).                 |
| **Dr. Memory**              | Windows equivalent of Valgrind.                           |

Example (ASan):

```bash
gcc -fsanitize=address -g main.c -o main
./main
```

---

## ⚡ 19️⃣ Memory lifecycle visualization

```
malloc() → allocates memory on heap
↓
used normally
↓
free() → returns it to heap
↓
(reusing after free) → undefined behavior
↓
never freeing → leak
```

---

## 🚀 20️⃣ Summary Table

| Concept             | Description                                   |
| ------------------- | --------------------------------------------- |
| Memory leak         | Allocated heap memory not freed               |
| Causes              | Forgetting `free()`, losing pointers          |
| Detection           | `valgrind --leak-check=full ./prog`           |
| Valgrind categories | definitely, indirectly, still reachable       |
| Fix                 | Always free, nullify, match malloc/free pairs |
| Prevention          | Careful design + automated checks             |
| Tools               | Valgrind, AddressSanitizer                    |

---

✅ **Key takeaway:**

> A segmentation fault kills your program instantly.
> A memory leak kills your system *slowly*.
> Tools like **Valgrind** and careful design keep your C programs stable and professional.

---
---

# 🧩 13️⃣ **String Manipulation (Manual & `<string.h>`)**

---

## 🧠 1️⃣ What is a string in C?

In C, a **string is just an array of characters terminated by a special null character**:

```
'\0'  (ASCII 0)
```

### Example:

```c
char name[] = "Yuvraj";
```

Internally stored as:

```
['Y', 'u', 'v', 'r', 'a', 'j', '\0']
```

✅ `"Yuvraj"` occupies **7 bytes** (6 letters + 1 for `'\0'`).

---

## ⚙️ 2️⃣ Two common ways to declare strings

### (a) As a character array:

```c
char name[] = "Yuvraj";
```

* Stored in writable memory.
* You can modify it:

  ```c
  name[0] = 'A';
  ```

### (b) As a string literal:

```c
char *name = "Yuvraj";
```

* Stored in **read-only** memory.
* ❌ Cannot modify it:

  ```c
  name[0] = 'A';  // segmentation fault
  ```

---

## 🧩 3️⃣ Manual string manipulation (no `<string.h>`)

You can manipulate strings manually using pointers and loops — this gives you a deep understanding of how memory works.

---

### 🧮 a) Finding string length manually

```c
int my_strlen(const char *str) {
    int len = 0;
    while (str[len] != '\0')
        len++;
    return len;
}
```

✅ Equivalent to `strlen(str)`.

---

### 🧱 b) Copying one string to another

```c
void my_strcpy(char *dest, const char *src) {
    int i = 0;
    while ((dest[i] = src[i]) != '\0')
        i++;
}
```

✅ Equivalent to `strcpy(dest, src)`.

⚠️ Make sure `dest` is large enough to hold `src`.

---

### 🧩 c) Concatenating two strings

```c
void my_strcat(char *dest, const char *src) {
    int i = 0, j = 0;
    while (dest[i] != '\0') i++; // move to end of dest
    while ((dest[i++] = src[j++]) != '\0');
}
```

✅ Equivalent to `strcat(dest, src)`.

---

### 🧠 d) Comparing two strings

```c
int my_strcmp(const char *a, const char *b) {
    int i = 0;
    while (a[i] && (a[i] == b[i])) i++;
    return (unsigned char)a[i] - (unsigned char)b[i];
}
```

✅ Equivalent to `strcmp(a, b)`
Returns:

* `0` → equal
* `<0` → first < second
* `>0` → first > second

---

### ⚙️ e) Reversing a string

```c
void my_strrev(char *s) {
    int len = 0;
    while (s[len]) len++;
    for (int i = 0; i < len / 2; i++) {
        char temp = s[i];
        s[i] = s[len - i - 1];
        s[len - i - 1] = temp;
    }
}
```

✅ Equivalent to `strrev()` (non-standard, but common in some compilers).

---

### 🧠 f) Counting vowels, digits, spaces

```c
int count_vowels(const char *s) {
    int count = 0;
    for (int i = 0; s[i]; i++)
        if (strchr("aeiouAEIOU", s[i])) count++;
    return count;
}
```

---

## ⚙️ 4️⃣ String manipulation using `<string.h>`

The C Standard Library provides many built-in functions for string operations, declared in:

```c
#include <string.h>
```

Let’s go through the most commonly used ones 👇

---

### 🧩 a) `strlen()` — length of string

```c
size_t strlen(const char *str);
```

Example:

```c
char s[] = "Hello";
printf("Length = %zu\n", strlen(s));
```

Output:

```
Length = 5
```

---

### 🧱 b) `strcpy()` — copy string

```c
char *strcpy(char *dest, const char *src);
```

Example:

```c
char src[] = "Reva";
char dest[10];
strcpy(dest, src);
printf("%s\n", dest);
```

⚠️ No bounds checking — can overflow if `dest` too small.
✅ Safer version (POSIX): `strncpy(dest, src, n)`.

---

### ⚙️ c) `strcat()` — concatenate strings

```c
char *strcat(char *dest, const char *src);
```

Example:

```c
char s1[20] = "Hello ";
char s2[] = "World";
strcat(s1, s2);
printf("%s\n", s1);
```

Output:

```
Hello World
```

✅ Safer version: `strncat(dest, src, n)`

---

### 🧠 d) `strcmp()` — compare strings

```c
int strcmp(const char *s1, const char *s2);
```

Returns:

* `0` if equal
* `<0` if `s1 < s2`
* `>0` if `s1 > s2`

Example:

```c
printf("%d\n", strcmp("abc", "abd")); // -1
```

---

### 🧩 e) `strchr()` and `strrchr()` — find character

```c
char *strchr(const char *s, int c);   // first occurrence
char *strrchr(const char *s, int c);  // last occurrence
```

Example:

```c
char s[] = "Hello World";
char *p = strchr(s, 'o');   // points to 1st 'o'
printf("%s\n", p);          // Output: o World
```

---

### ⚙️ f) `strstr()` — find substring

```c
char *strstr(const char *haystack, const char *needle);
```

Example:

```c
char s[] = "Reva University";
char *p = strstr(s, "Uni");
printf("%s\n", p);  // Output: University
```

---

### 🧠 g) `strtok()` — split string (tokenize)

```c
char *strtok(char *str, const char *delim);
```

Example:

```c
char s[] = "one,two,three";
char *token = strtok(s, ",");
while (token) {
    printf("%s\n", token);
    token = strtok(NULL, ",");
}
```

✅ Output:

```
one
two
three
```

⚠️ Modifies the original string!
✅ Use `strtok_r()` for thread-safe version.

---

### 🧩 h) `memcpy()` and `memmove()`

Used for raw memory copying.

```c
void *memcpy(void *dest, const void *src, size_t n);
```

Example:

```c
char src[] = "Hello";
char dest[10];
memcpy(dest, src, strlen(src) + 1);
printf("%s\n", dest);
```

✅ `memmove()` handles overlapping regions safely.

---

### ⚙️ i) `memset()` — fill memory with a value

```c
void *memset(void *ptr, int value, size_t num);
```

Example:

```c
char s[10];
memset(s, '-', 9);
s[9] = '\0';
printf("%s\n", s);  // ---------
```

---

## 🧠 5️⃣ String pointer basics

Strings and pointers are deeply related in C:

```c
char s[] = "Hello";
char *p = s;

printf("%c\n", *p);    // 'H'
printf("%c\n", *(p+1)); // 'e'
```

You can traverse a string using a pointer:

```c
for (char *p = s; *p; p++)
    putchar(*p);
```

---

## ⚙️ 6️⃣ Example: Manual + Library Combo

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    strcpy(name, "Yuvraj");
    printf("Name: %s\n", name);
    printf("Length: %zu\n", strlen(name));

    strcat(name, " Singh");
    printf("Full name: %s\n", name);

    if (strstr(name, "Singh"))
        printf("Surname found!\n");

    strrev(name); // non-standard, use manual reverse if needed
    printf("Reversed: %s\n", name);
}
```

✅ Output:

```
Name: Yuvraj
Length: 6
Full name: Yuvraj Singh
Surname found!
Reversed: hgniS jarvuY
```

---

## 🧩 7️⃣ Common pitfalls

❌ Forgetting the null terminator:

```c
char name[5] = {'Y', 'u', 'v', 'r', 'a'}; // ❌ no '\0'
printf("%s", name); // undefined behavior
```

✅ Fix:

```c
char name[6] = {'Y', 'u', 'v', 'r', 'a', '\0'};
```

---

❌ Buffer overflow:

```c
char dest[5];
strcpy(dest, "Yuvraj"); // ❌ writes beyond buffer
```

✅ Fix:

```c
strncpy(dest, "Yuvraj", sizeof(dest)-1);
dest[sizeof(dest)-1] = '\0';
```

---

❌ Modifying string literals:

```c
char *s = "Hello";
s[0] = 'h'; // ❌ segmentation fault
```

✅ Fix:

```c
char s[] = "Hello";
s[0] = 'h';
```

---

## ⚙️ 8️⃣ Advanced tip: dynamic string building

```c
char *msg = malloc(100);
strcpy(msg, "Hello");
strcat(msg, " World");
printf("%s\n", msg);
free(msg);
```

Or reallocate as needed:

```c
msg = realloc(msg, 200);
```

---

## 🧠 9️⃣ Summary Table

| Function    | Purpose        | Manual Equivalent |
| ----------- | -------------- | ----------------- |
| `strlen()`  | Get length     | loop until `'\0'` |
| `strcpy()`  | Copy           | custom loop       |
| `strcat()`  | Concatenate    | nested loop       |
| `strcmp()`  | Compare        | char-by-char      |
| `strchr()`  | Find character | loop search       |
| `strstr()`  | Find substring | nested search     |
| `strtok()`  | Tokenize       | manual split      |
| `memcpy()`  | Copy bytes     | `for` loop        |
| `memset()`  | Fill bytes     | `for` loop        |
| `strncpy()` | Safe copy      | checked copy      |

---

## 🚀 10️⃣ Key takeaway

> In C, strings are just **character arrays with a `'\0'` terminator**.
> `<string.h>` provides convenient, battle-tested utilities —
> but understanding the **manual logic** helps you handle low-level memory operations safely and confidently.

---
---

# Hash Table

A **hash table** maps keys → values using a *hash function* `h(key)` that produces an integer, then reduces it modulo the number of buckets:

```
index = h(key) % capacity
```

If multiple keys map to the same bucket (collision), common strategies:

* **Separate chaining**: each bucket is a linked list of entries (used here).
* **Open addressing**: probe for another slot (linear/quadratic/double hashing).

Pros: average **O(1)** insert/search/delete.
Cons: worst-case **O(n)** (bad hash or load factor), requires careful memory management in C.

---

# Complexity (average / worst)

* Insert: O(1) average, O(n) worst
* Search: O(1) average, O(n) worst
* Delete: O(1) average, O(n) worst
* Space: O(n + capacity)

Keep load factor (n / capacity) ~ 0.5–0.75 to preserve performance — resize (rehash) when exceeded.

---

# Implementation (separate chaining, string keys & values)

Copy this into `hashtable.c`:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

/* Simple portable strdup in case it's not available */
static char *xstrdup(const char *s) {
    if (!s) return NULL;
    size_t n = strlen(s) + 1;
    char *d = malloc(n);
    if (!d) return NULL;
    memcpy(d, s, n);
    return d;
}

/* Node stored in each bucket's linked list */
typedef struct ht_node {
    char *key;
    char *value;
    struct ht_node *next;
} ht_node;

/* Hash table */
typedef struct {
    ht_node **buckets; /* array of pointers to ht_node */
    size_t capacity;   /* number of buckets */
    size_t size;       /* number of entries stored */
} hashtable;

/* djb2 string hash (good, simple) */
static size_t hash_djb2(const char *str) {
    uint64_t hash = 5381;
    int c;
    while ((c = (unsigned char)*str++))
        hash = ((hash << 5) + hash) + (uint64_t)c; /* hash * 33 + c */
    return (size_t)hash;
}

/* Create table with given capacity */
hashtable *ht_create(size_t capacity) {
    hashtable *ht = malloc(sizeof(hashtable));
    if (!ht) return NULL;
    ht->capacity = (capacity < 8) ? 8 : capacity;
    ht->size = 0;
    ht->buckets = calloc(ht->capacity, sizeof(ht_node*));
    if (!ht->buckets) { free(ht); return NULL; }
    return ht;
}

/* Free a linked list of nodes */
static void free_bucket(ht_node *node) {
    while (node) {
        ht_node *next = node->next;
        free(node->key);
        free(node->value);
        free(node);
        node = next;
    }
}

/* Destroy hashtable and free memory */
void ht_free(hashtable *ht) {
    if (!ht) return;
    for (size_t i = 0; i < ht->capacity; ++i)
        free_bucket(ht->buckets[i]);
    free(ht->buckets);
    free(ht);
}

/* Internal: rehash into larger bucket array (double capacity) */
static int ht_resize(hashtable *ht, size_t new_capacity) {
    ht_node **new_buckets = calloc(new_capacity, sizeof(ht_node*));
    if (!new_buckets) return 0;
    /* move entries */
    for (size_t i = 0; i < ht->capacity; ++i) {
        ht_node *node = ht->buckets[i];
        while (node) {
            ht_node *next = node->next;
            size_t idx = hash_djb2(node->key) % new_capacity;
            node->next = new_buckets[idx];
            new_buckets[idx] = node;
            node = next;
        }
    }
    free(ht->buckets);
    ht->buckets = new_buckets;
    ht->capacity = new_capacity;
    return 1;
}

/* Insert or update (ownership: ht makes copies of key & value) */
int ht_put(hashtable *ht, const char *key, const char *value) {
    if (!ht || !key) return 0;
    /* Resize if load factor > 0.75 */
    if ((double)ht->size / (double)ht->capacity > 0.75) {
        if (!ht_resize(ht, ht->capacity * 2)) return 0;
    }
    size_t idx = hash_djb2(key) % ht->capacity;
    ht_node *node = ht->buckets[idx];
    while (node) {
        if (strcmp(node->key, key) == 0) {
            /* update existing value */
            char *newval = xstrdup(value);
            if (!newval) return 0;
            free(node->value);
            node->value = newval;
            return 1;
        }
        node = node->next;
    }
    /* create new node and push front */
    ht_node *newnode = malloc(sizeof(ht_node));
    if (!newnode) return 0;
    newnode->key = xstrdup(key);
    newnode->value = xstrdup(value);
    if (!newnode->key || !newnode->value) {
        free(newnode->key); free(newnode->value); free(newnode);
        return 0;
    }
    newnode->next = ht->buckets[idx];
    ht->buckets[idx] = newnode;
    ht->size++;
    return 1;
}

/* Get value by key (returns pointer to value owned by table — do not free) */
char *ht_get(hashtable *ht, const char *key) {
    if (!ht || !key) return NULL;
    size_t idx = hash_djb2(key) % ht->capacity;
    ht_node *node = ht->buckets[idx];
    while (node) {
        if (strcmp(node->key, key) == 0) return node->value;
        node = node->next;
    }
    return NULL; /* not found */
}

/* Remove entry by key; returns 1 if removed, 0 if not found */
int ht_remove(hashtable *ht, const char *key) {
    if (!ht || !key) return 0;
    size_t idx = hash_djb2(key) % ht->capacity;
    ht_node **pp = &ht->buckets[idx];
    ht_node *node = *pp;
    while (node) {
        if (strcmp(node->key, key) == 0) {
            *pp = node->next;
            free(node->key);
            free(node->value);
            free(node);
            ht->size--;
            return 1;
        }
        pp = &node->next;
        node = node->next;
    }
    return 0;
}

/* Simple debug print of the table */
void ht_print(hashtable *ht) {
    if (!ht) return;
    printf("Hashtable: size=%zu capacity=%zu\n", ht->size, ht->capacity);
    for (size_t i = 0; i < ht->capacity; ++i) {
        printf("[%zu]:", i);
        ht_node *node = ht->buckets[i];
        while (node) {
            printf(" (%s => %s)", node->key, node->value);
            node = node->next;
        }
        printf("\n");
    }
}

/* Example usage */
#ifdef HT_TEST
int main(void) {
    hashtable *ht = ht_create(8);
    ht_put(ht, "apple", "red");
    ht_put(ht, "banana", "yellow");
    ht_put(ht, "grape", "purple");
    ht_put(ht, "pear", "green");
    ht_put(ht, "lemon", "yellow");
    ht_print(ht);

    printf("get grape = %s\n", ht_get(ht, "grape"));
    ht_put(ht, "grape", "green-ish"); // update
    printf("get grape = %s\n", ht_get(ht, "grape"));

    ht_remove(ht, "banana");
    printf("after removing banana:\n");
    ht_print(ht);

    ht_free(ht);
    return 0;
}
#endif
```

---

# How to compile & run

Save above to `hashtable.c`. Compile and run test:

```bash
gcc -std=c11 -Wall -Wextra -DHT_TEST hashtable.c -o hashtable
./hashtable
```

`-DHT_TEST` enables the `main()` in the file for quick testing.

---

# Memory ownership & safety notes

* This implementation makes **copies** of keys & values (`xstrdup`) so caller can free their originals safely. The hash table owns its copies and frees them on delete / `ht_free`.
* If you want to store arbitrary `void*` values (not strings), change `char *value` to `void *value` and decide who manages lifetime.
* Always call `ht_free()` to avoid leaks.
* `strdup` is POSIX; we used `xstrdup` to stay portable.

---

# Resizing & tuning

* We resize (double) when load factor > 0.75. You can shrink when load factor < 0.2.
* Choose capacity as prime numbers can help distribution but modulo with power-of-two capacities + good hash also works.
* Hash function: `djb2` is simple and decent for strings; for cryptographic or adversarial inputs consider stronger functions or randomized seeds.

---

# Pitfalls & gotchas

* **Bad hash** → many collisions → degrade to linked lists (O(n)).
* **Non-unique keys** — you must decide whether to allow duplicates or overwrite (this implementation overwrites).
* **Thread-safety** — not thread-safe; add locks for concurrent access.
* **Memory leaks** — if you store pointers you don’t own, be careful to free only what belongs to the table.
* **Integer keys** — convert to string or design hash for integers.

---

# Alternatives

* **Open addressing (linear/quadratic/Robin Hood)**: fewer mallocs, better cache locality, but more complex deletion/resize logic.
* **Sorted vector + binary search**: simpler, good for small sets. Insert O(n), search O(log n).
* **Use existing libraries**: khash, uthash (single-header), glib’s GHashTable if you want production-tested code quickly.

---
---

# Build systems & linking multiple object files (compact but practical)

## 1 — Concepts & workflow (high level)

1. **Compilation unit**: each `.c` file is compiled into an object file `.o`.
2. **Linking**: the linker combines `.o` files (and libraries) into an executable (or shared object).
3. **Why separate compile?** Faster incremental builds and modular code (only recompile changed files).
4. **Headers (`.h`)** hold declarations; `.c` hold definitions. Include headers so the compiler knows function/types signatures.

---

## 2 — Basic gcc commands

* **Compile-only** (C → object):

```bash
gcc -c foo.c -o foo.o   # produces foo.o, no linking
```

* **Link** (objects → executable):

```bash
gcc foo.o bar.o -o myapp
```

* **Compile + link in one step**:

```bash
gcc foo.c bar.c -o myapp
```

* **Add include paths** (for headers not in system dirs):

```bash
gcc -I/path/to/includes -c foo.c
```

* **Add libraries** (linker options):

```bash
gcc foo.o -L/path/to/libs -lmylib -o myapp
# -L adds library search path, -l<name> links lib<name>.so or lib<name>.a
```

* **Common flags**:

  * `-g` add debug symbols
  * `-O2` optimize (or `-O0` for debug)
  * `-Wall -Wextra` enable warnings
  * `-fPIC` for position-independent code (needed for building shared libs)
  * `-shared` build shared library (`.so`)
  * `-static` link statically (linker option; creates static binary if libs available)

---

## 3 — Example: small multi-file program

Files:

```
src/ main.c      // calls greet()
src/ greet.c     // defines greet()
include/greet.h  // declaration
```

Commands:

```bash
gcc -Iinclude -c src/greet.c -o build/greet.o
gcc -Iinclude -c src/main.c  -o build/main.o
gcc build/main.o build/greet.o -o bin/myapp
```

---

## 4 — Makefile (practical, with dependency generation)

Save as `Makefile`:

```make
CC := gcc
CFLAGS := -std=c11 -Wall -Wextra -g -O0 -Iinclude
LDFLAGS :=
LDLIBS :=

SRCDIR := src
BUILDDIR := build
BINDIR := bin

SOURCES := $(wildcard $(SRCDIR)/*.c)
OBJECTS := $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SOURCES))
DEPS := $(OBJECTS:.o=.d)

TARGET := $(BINDIR)/myapp

.PHONY: all clean dirs

all: dirs $(TARGET)

dirs:
	mkdir -p $(BUILDDIR) $(BINDIR)

# Link
$(TARGET): $(OBJECTS)
	$(CC) $(LDFLAGS) $^ -o $@ $(LDLIBS)

# Compile with automatic dependency generation (-MMD -MP)
$(BUILDDIR)/%.o: $(SRCDIR)/%.c
	$(CC) $(CFLAGS) -MMD -MP -c $< -o $@

# Include auto-generated dependency files
-include $(DEPS)

clean:
	rm -rf $(BUILDDIR) $(BINDIR)
```

Notes:

* `-MMD -MP` creates `.d` files containing dependency lists so `make` will recompile when headers change.
* `$^` = all prerequisites, `$@` = target, `$<` = first prerequisite.

---

## 5 — Static vs Shared libraries

### Static library (`.a`)

* Create object files then archive:

```bash
gcc -c lib/foo.c -o lib/foo.o
ar rcs lib/libmylib.a lib/foo.o lib/bar.o
# Link statically:
gcc main.o -Llib -lmylib -o myapp   # by default picks libmylib.a if no .so found (or use -static)
```

* Pros: single stand-alone binary, no runtime dependency on .so.
* Cons: bigger binary; harder to update library without relinking.

### Shared library (`.so`)

* Build position-independent objects:

```bash
gcc -fPIC -c lib/foo.c -o lib/foo.o
gcc -shared -o lib/libmylib.so lib/foo.o lib/bar.o
# Link:
gcc main.o -Llib -lmylib -o myapp
# At runtime, the dynamic loader finds libmylib.so
```

* Use `LD_LIBRARY_PATH` or `-Wl,-rpath,/path/to/lib` (or install to system dirs) so the loader finds `.so`.

---

## 6 — Linker order & common pitfalls

* **Order matters** for static linking: object files should come before libraries that depend on them:

  ```bash
  gcc a.o -lfoo    # if a.o uses foo
  ```

  For multiple libraries, if A depends on B you may need `-lA -lB` or repeat `-lA` in old linkers.

* **Undefined reference** at link time means: you declared a function but never provided a definition to the linker (missing .o or lib).

* **Multiple definition** means you provided two symbols with same name (e.g., defining a global var in a header without `extern`).

* **Header-only mistakes**: don't put non-`inline` function or variable definitions in headers without `static` or `extern`; that causes duplicate symbols.

---

## 7 — Useful tools for diagnosing linking problems

* `gcc -v` show linker invocation.
* `nm file.o` shows symbols in object files / libs (`T` = text/defined, `U` = undefined).
* `ldd ./myapp` lists dynamic dependencies (.so files).
* `objdump -t` or `readelf -s` for symbol tables.
* `strace` can show runtime loader activity if .so missing.

Example: if `undefined reference to 'foo'` → check `nm libmylib.a | grep foo` or `nm libmylib.so | grep foo`.

---

## 8 — Dependency management & best practices

* **Use header guards** or `#pragma once`.
* Put `extern` declarations for globals in headers; define the variable in exactly one `.c`.
* Keep headers minimal (forward declare structs when possible).
* Use `pkg-config` for third-party libs:

```bash
gcc `pkg-config --cflags gtk+-3.0` -c main.c
gcc main.o `pkg-config --libs gtk+-3.0` -o gui
```

* For large projects prefer CMake, Meson, or autotools (they handle platform quirks).

---

## 9 — Advanced linking topics (short)

* **LTO (Link-Time Optimization)**: `-flto` enables cross-translation-unit optimizations; both compile and link with `-flto`.
* **Static linking**: `-static` produces fully static binary (beware glibc static complexity on Linux).
* **RPATH** (`-Wl,-rpath,/path`) embeds runtime library path.
* **Linker scripts** control symbol layout (advanced).
* **Position Independent Executable (PIE)**: `-fPIE -pie` for ASLR-friendly executables.

---

## 10 — Quick checklist when link fails

* Did you compile all `.c` files? (`-c` step)
* Are you linking the required libraries? (`-l` and `-L`)
* Are function signatures mismatched (C++ name mangling vs `extern "C"`)?
* Do headers accidentally define variables? (use `extern` in headers)
* Are object files/libraries in the correct order?
* For runtime `.so` errors use `ldd` and check `LD_LIBRARY_PATH` or `rpath`.

---

## 11 — Minimal workflow example

1. Edit code in `src/` and headers in `include/`.
2. Build object files: `gcc -Iinclude -c src/*.c -O2 -g -Wall`.
3. Link: `gcc build/*.o -o bin/app`.
4. Run `./bin/app`. If undefined symbol, run `nm` on the .o files and libs to find which file provides it.

---
---

# 🧩 16️⃣ How C Maps to Assembly, Stack Frames & Calling Conventions

---

## 🧠 1️⃣ The “mental bridge” between C and Assembly

When you write:

```c
int add(int a, int b) {
    return a + b;
}
```

The compiler (GCC/Clang) transforms it into **assembly** instructions that your CPU executes.
Each instruction works on **registers**, **memory**, and **the stack**.

---

## ⚙️ 2️⃣ The memory layout of a running C program

```
  +---------------------------+  ← High addresses
  | Stack (local vars)        |  grows ↓
  +---------------------------+
  | Heap (malloc/new)         |  grows ↑
  +---------------------------+
  | BSS segment               |  uninitialized globals
  +---------------------------+
  | Data segment              |  initialized globals
  +---------------------------+
  | Text segment (code)       |  compiled instructions
  +---------------------------+  ← Low addresses
```

---

## 🧩 3️⃣ Function calls: what really happens

When you call a function in C, e.g.:

```c
int main() {
    int x = add(2, 3);
}
```

These steps happen:

1. **Arguments** are placed in registers or pushed on the stack.
2. **Return address** (the point to continue after the function) is pushed onto the stack.
3. **Stack frame** is created for local variables.
4. Function executes.
5. Function returns a value (in register).
6. Stack frame is destroyed and control returns to caller.

---

## ⚙️ 4️⃣ Example: a simple C function

```c
int add(int a, int b) {
    int sum = a + b;
    return sum;
}
```

Compile and disassemble (`gcc -S add.c -o add.s`)
Example output (x86-64, System V ABI):

```asm
add:
    push    rbp            ; save caller's base pointer
    mov     rbp, rsp       ; set new base pointer
    mov     DWORD PTR [rbp-4], edi   ; a → [rbp-4]
    mov     DWORD PTR [rbp-8], esi   ; b → [rbp-8]
    mov     eax, DWORD PTR [rbp-4]
    add     eax, DWORD PTR [rbp-8]
    mov     DWORD PTR [rbp-12], eax  ; sum = a+b
    mov     eax, DWORD PTR [rbp-12]  ; return sum
    pop     rbp
    ret
```

Let’s decode this:

| Assembly                    | Meaning                           |
| --------------------------- | --------------------------------- |
| `push rbp` / `mov rbp, rsp` | Create a new **stack frame**      |
| `[rbp-4]`, `[rbp-8]`        | Local variables or saved params   |
| `edi`, `esi`, `eax`         | Registers holding `int` values    |
| `pop rbp` / `ret`           | Restore caller’s frame and return |

---

## 🧠 5️⃣ Stack frame visualization

When `add(2, 3)` runs:

```
Stack top ↓
+------------------+
| return address   | ← pushed by CALL
+------------------+
| old rbp          | ← push rbp
+------------------+
| a = 2 (rbp-4)    |
+------------------+
| b = 3 (rbp-8)    |
+------------------+
| sum (rbp-12)     |
+------------------+
```

---

## 🧩 6️⃣ Calling conventions — how parameters & return values are passed

A **calling convention** defines:

* Where function parameters go
* Who cleans the stack
* Which registers are preserved

### a) x86-64 (System V — Linux / macOS)

| Parameter order | Register |
| --------------- | -------- |
| 1st             | RDI      |
| 2nd             | RSI      |
| 3rd             | RDX      |
| 4th             | RCX      |
| 5th             | R8       |
| 6th             | R9       |
| Return value    | RAX      |

Additional arguments → pushed on stack.
Caller saves volatile registers (rdi, rsi, rdx, rcx, r8, r9, r10, r11).
Callee saves non-volatile (rbx, rbp, r12–r15).

---

### b) x86 (32-bit) — cdecl (classic C convention)

* Arguments pushed **right to left** on stack
* Return value in **EAX**
* Caller cleans stack (after call)

Example:

```asm
push 3
push 2
call add
add  esp, 8   ; caller removes args
```

---

### c) Windows x64

* 1st–4th args → RCX, RDX, R8, R9
* Shadow space (32 bytes) reserved on stack for all calls
* Return in RAX

---

## ⚙️ 7️⃣ Example with local variables & function calls

```c
int square(int x) { return x * x; }

int main() {
    int a = 5;
    int b = square(a);
    return b;
}
```

Simplified assembly (x86-64):

```asm
square:
    mov     eax, edi    ; param in edi
    imul    eax, eax    ; eax = x*x
    ret                 ; return eax

main:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp-4], 5
    mov     edi, DWORD PTR [rbp-4]  ; arg in edi
    call    square
    mov     DWORD PTR [rbp-8], eax  ; b = return value
    mov     eax, DWORD PTR [rbp-8]
    pop     rbp
    ret
```

✅ Observe:

* Argument `a` is copied into register `edi` before `call square`.
* `eax` carries the return value back.

---

## 🧱 8️⃣ Inlining & optimization

When you compile with `-O2`, the compiler may **inline** small functions:

```c
int square(int x) { return x * x; }
```

becomes part of `main()`; no call at all — just:

```asm
imul eax, eax
```

✅ This is why small functions may not appear as separate stack frames in optimized builds.

---

## 🧩 9️⃣ The prologue & epilogue pattern

Almost every compiled function follows this template (unless optimized):

```asm
push rbp        ; prologue
mov  rbp, rsp
sub  rsp, N     ; reserve local space

...             ; function body

leave           ; same as mov rsp, rbp + pop rbp
ret             ; epilogue
```

The **stack frame** is always aligned to 16 bytes on x86-64 for SIMD instructions.

---

## ⚙️ 10️⃣ Variadic functions (e.g., `printf`)

Variadic functions follow the same convention, but arguments are also tracked in registers & stack.
Extra metadata (number of vector registers used) is passed in `al`.
At runtime, macros like `va_start` use pointer arithmetic to iterate over the stack arguments.

---

## 🧠 11️⃣ Recursion and the stack

Each function call creates a new frame on the stack.
Recursive calls create multiple frames until:

* Base case returns
* Or stack overflows (no base case or too deep recursion)

Example:

```c
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
```

Each call stores its own copy of `n` and return address.

---

## 🧩 12️⃣ Example of stack growth

For `fact(3)`:

```
fact(3) frame → n=3, waiting for fact(2)
fact(2) frame → n=2, waiting for fact(1)
fact(1) frame → n=1, returns 1
Stack unwinds ← each multiply returns
```

Each `ret` pops its frame (via restoring `rbp` and `rsp`).

---

## ⚙️ 13️⃣ The `call` and `ret` instructions

| Instruction | Effect                                          |
| ----------- | ----------------------------------------------- |
| `call func` | Pushes return address on stack, jumps to `func` |
| `ret`       | Pops return address, jumps back to caller       |

Example:

```asm
call add   ; pushes next-instruction address
ret        ; pops and jumps back
```

---

## 🧠 14️⃣ How return values are passed

| Type                             | Register(s)                                               |
| -------------------------------- | --------------------------------------------------------- |
| `int`, `char`, `short`, pointers | `RAX`                                                     |
| `float`                          | `XMM0`                                                    |
| `double`                         | `XMM0`                                                    |
| Structs (small)                  | `RAX`/`RDX` combo                                         |
| Large structs                    | Caller allocates space; pointer passed in hidden register |

---

## 🧩 15️⃣ Stack frame alignment example

If locals need 12 bytes, compiler aligns stack to 16:

```asm
sub rsp, 16
```

Not 12 — ensures correct alignment for vector ops (e.g., `movaps`).

---

## ⚙️ 16️⃣ Example: inspecting with `objdump`

Compile:

```bash
gcc -O0 -fno-omit-frame-pointer -g demo.c -o demo
objdump -d demo | less
```

You’ll see assembly annotated with function names.
Or use:

```bash
gdb ./demo
(gdb) disassemble add
```

---

## 🧠 17️⃣ Why calling conventions matter

* They ensure **binary compatibility** between separately compiled modules and libraries.
* If you mix conventions (e.g., `__cdecl` vs `__stdcall` on Windows), you corrupt the stack.
* Important when writing:

  * Inline assembly
  * System calls
  * Foreign function interfaces (e.g., Python C API)
  * Handwritten assembly

---

## 🧩 18️⃣ Summary Table

| Concept                     | Meaning                                                        |
| --------------------------- | -------------------------------------------------------------- |
| Stack frame                 | Memory region per function call containing locals, return addr |
| Base pointer (`rbp`)        | Anchor for frame-local variables                               |
| Stack pointer (`rsp`)       | Points to top of current stack                                 |
| Calling convention          | Defines parameter passing / cleanup rules                      |
| Prologue / Epilogue         | Setup & teardown of stack frame                                |
| Registers (x86-64 System V) | RDI, RSI, RDX, RCX, R8, R9 (args), RAX (return)                |
| Function call               | `call` pushes return addr, `ret` pops it                       |
| Recursion                   | Multiple stack frames, one per call                            |

---

## ⚡ 19️⃣ Practical experiment

Compile with `-S`:

```bash
gcc -O0 -S -fno-omit-frame-pointer demo.c
```

Edit the `.s` file; observe how C constructs (loops, if, return) become assembly:

* `for` → compare/jump
* `if` → `cmp` + `je`/`jne`
* `return` → `mov eax,...` + `ret`

---

## 🚀 20️⃣ Key takeaway

> Every C function call maps to **stack frame creation**, **register argument passing**, and **assembly instructions** that manipulate those stack frames.
> Understanding this mapping is the foundation for:
>
> * Debugging segmentation faults
> * Reading compiler output
> * Writing inline assembly
> * Understanding ABI-level interoperability

---
---

# 🧩 17️⃣ Undefined Behavior & The C Standard Model

---

## 🧠 1️⃣ The “C Model” — what the compiler *thinks* happens

C is a **high-level abstraction over machine code**, but the C standard does **not** define exact CPU behavior.
Instead, it defines a **model** — how objects, types, and side effects behave *in theory*,
and leaves many machine-dependent things *unspecified* for speed and portability.

The compiler assumes your code **always follows the rules of the standard**.
If you break them — you enter **undefined behavior** land, and **anything** can happen.

---

## ⚙️ 2️⃣ The three behavior categories in C

| Type                           | Defined by Standard?   | Example                                             | Compiler’s Obligation                                          |
| ------------------------------ | ---------------------- | --------------------------------------------------- | -------------------------------------------------------------- |
| ✅ **Defined behavior**         | Yes                    | `a = b + c;`                                        | Must behave exactly as defined                                 |
| ⚠️ **Unspecified behavior**    | Several valid outcomes | Function args may evaluate left→right or right→left | Any valid result allowed                                       |
| 💀 **Undefined behavior (UB)** | No meaning assigned    | `i = i++;`                                          | Compiler can do *anything* — crash, optimize, reformat reality |

---

## 🧩 3️⃣ Why undefined behavior exists

The C standard **allows UB intentionally** for:

* **Performance:** compiler can assume “no UB” → better optimizations.
* **Hardware flexibility:** works across architectures (x86, ARM, embedded).
* **Simplicity:** avoids defining absurd edge cases.

Example:
Dereferencing `NULL` is UB → no runtime check, faster code.
If C required defining what happens, every pointer access would need a runtime check — slowing everything down.

---

## ⚙️ 4️⃣ Examples of undefined behavior (UB)

Let’s go through the common categories:

---

### 🧨 1. Out-of-bounds array access

```c
int arr[3] = {1,2,3};
int x = arr[5]; // UB
```

* May read garbage, segfault, or silently corrupt data.
* Compiler assumes you never do this → may optimize aggressively.

---

### 🧨 2. Modifying and reading a variable in one expression

```c
i = i++;
```

❌ UB — both modify and read `i` without a sequence point.
Compilers can emit totally different results.

✅ Defined:

```c
i++;
i = i + 1;
```

---

### 🧨 3. Dereferencing invalid or freed pointers

```c
int *p = malloc(sizeof(int));
free(p);
*p = 10;  // UB (use-after-free)
```

Even if the memory “still looks okay,” the behavior is undefined —
it might corrupt the heap metadata or crash later.

---

### 🧨 4. Using uninitialized variables

```c
int x;
printf("%d\n", x); // UB
```

C standard: “value of uninitialized variable is indeterminate.”
Can cause segmentation fault or print random numbers.

---

### 🧨 5. Integer overflow (for signed ints)

```c
int x = 2147483647 + 1; // UB
```

Unsigned overflow is *well-defined* (wraps modulo 2ⁿ).
Signed overflow is UB because C treats signed ints as *mathematical integers*.

---

### 🧨 6. Violating strict aliasing rules

```c
float f = 3.14;
int *ip = (int*)&f;   // UB
printf("%d", *ip);
```

Strict aliasing: different pointer types may not alias the same memory,
except `char*`. Compiler assumes each type lives in isolation for optimization.

✅ Allowed:

```c
unsigned char *bytes = (unsigned char*)&f;
```

---

### 🧨 7. Misaligned pointer access

```c
int *p = (int*)((char*)&x + 1); // not aligned to 4 bytes
int y = *p;                     // UB on architectures needing alignment
```

---

### 🧨 8. Buffer overflow (classic)

```c
char s[5] = "Hello"; // ❌ missing '\0' → overflow
```

Writes past end of buffer → UB (may corrupt stack or return address).

---

### 🧨 9. Modifying string literals

```c
char *s = "abc";
s[0] = 'x'; // UB (string literals are read-only)
```

---

### 🧨 10. Data races in multi-threaded programs

```c
// two threads writing same variable without mutex
global++; // UB
```

Even if it “seems fine,” results can differ per run or per optimization.

---

## ⚙️ 5️⃣ Unspecified vs Undefined vs Implementation-defined

| Term                       | Meaning                            | Example                                 |
| -------------------------- | ---------------------------------- | --------------------------------------- |
| **Undefined**              | Behavior not defined at all        | `i = i++;`                              |
| **Unspecified**            | Multiple valid results allowed     | Function argument order                 |
| **Implementation-defined** | Compiler defines it, must document | Size of `int`, representation of `char` |

---

## 🧠 6️⃣ The “as-if” rule

The compiler can do *anything* to optimize your code **as long as** it behaves “as if” it followed the standard.

So if UB occurs, the compiler’s guarantees collapse — it can:

* Remove seemingly valid code,
* Reorder operations,
* Assume impossible conditions.

Example:

```c
if (p != NULL) *p = 10;
```

Compiler may **assume** `p != NULL` always, since dereferencing NULL is UB → may reorder code or skip checks entirely.

---

## 🧩 7️⃣ Example: UB changing optimization results

```c
int a = 5;
int b = (++a) + (a++); // UB
printf("%d %d\n", a, b);
```

Different outputs:

```
gcc -O0 → 12 12
gcc -O2 → 13 11
```

Why? The compiler is free to reorder or eliminate code after UB.

---

## ⚙️ 8️⃣ Example: signed integer overflow

```c
int x = INT_MAX;
x = x + 1; // UB
```

At `-O2`, compiler assumes overflow cannot happen, so it may remove comparisons like:

```c
if (x + 1 < x) ...
```

Since UB "can’t happen", it treats condition as false — optimizing it out entirely!

---

## 🧠 9️⃣ “The compiler as a liar”

Once UB happens anywhere, **the compiler can make any assumption**:

* Skip code paths.
* Optimize entire functions away.
* Hoist code above loops.
* Even remove runtime checks.

Example:

```c
int *p = NULL;
if (p) *p = 10;   // compiler might remove the condition!
```

Since dereferencing `p` is UB, compiler may assume `p` is never NULL.

---

## 🧩 🔥 10️⃣ Real-world examples of UB causing chaos

### Heartbleed (2014)

* Caused by buffer over-read — UB by reading beyond allocated memory.

### Linux Kernel bugs

* Sometimes triggered by violating alignment or race conditions.

### Security exploits

* Attackers deliberately induce UB (e.g., buffer overflow) → inject code, hijack control flow.

---

## ⚙️ 11️⃣ Detecting UB

### Use **Sanitizers**

```bash
gcc -fsanitize=undefined -g prog.c -o prog
./prog
```

Detects:

* Integer overflow
* Null dereference
* Invalid shifts
* Out-of-bounds
* Misaligned access

Example output:

```
runtime error: signed integer overflow: 2147483647 + 1 cannot be represented in type 'int'
```

### Use **Valgrind** for memory-related UB

```bash
valgrind ./prog
```

### Use **Static analyzers**

* `clang --analyze file.c`
* `cppcheck`
* `scan-build gcc ...`

---

## 🧠 12️⃣ Example: Undefined but looks harmless

```c
int x = 1;
int y = x << 31; // UB (shifting sign bit)
```

Result is not guaranteed — different CPUs interpret differently.

---

## 🧩 13️⃣ Avoiding UB — golden rules

✅ Initialize all variables.
✅ Stay within array bounds.
✅ Don’t modify variables twice between sequence points.
✅ Don’t access freed memory.
✅ Use correct pointer types.
✅ Don’t overflow signed integers.
✅ Protect shared data in threads with locks.
✅ Don’t modify string literals.
✅ Use tools to catch UB early.

---

## ⚙️ 14️⃣ The C abstract machine model

The **C standard defines an “abstract machine”**:

* Has objects with well-defined lifetimes.
* Execution proceeds as a sequence of operations with side effects.
* Accessing objects outside lifetime or violating type rules = UB.

The compiler must generate code that behaves **as if** executed by this abstract machine — unless UB occurs, then all bets are off.

---

## 🧠 15️⃣ Why compilers exploit UB

Optimization example:

```c
int foo(int *p) {
    if (p == NULL) return 0;
    *p = 5;
    return *p;
}
```

Because dereferencing NULL is UB, compiler can assume `p != NULL`.
So it may optimize to:

```asm
mov eax, 5
ret
```

→ It **removes the null check** entirely.

---

## 🧩 16️⃣ Why UB differs from “just wrong output”

UB ≠ “buggy output.”
UB = **“no rules apply”**.
Even printing, jumping, or causing segmentation fault are *all valid outcomes*.

C Standard literally says:

> “If a program’s behavior is undefined, the implementation may do anything it chooses.”

---

## ⚙️ 17️⃣ Examples of “unspecified behavior” (not UB)

```c
printf("%d %d\n", f1(), f2());
```

The order of evaluation (f1 or f2 first) is **unspecified**,
but each is valid — it’s just not guaranteed to be consistent.

---

## 🧠 18️⃣ Implementation-defined examples

| Behavior             | Examples                         |
| -------------------- | -------------------------------- |
| Size of data types   | `sizeof(int)` may be 2, 4, or 8  |
| Endianness           | Little vs Big endian             |
| Signed right shift   | `-4 >> 1` may round up or down   |
| Character signedness | `char` may be signed or unsigned |

---

## 🧩 19️⃣ UB in optimization — practical tip

You can tell the compiler not to exploit UB:

```bash
-fwrapv
```

Treats signed overflow as wrapping instead of UB (useful in math-heavy code).

Or:

```bash
-fno-strict-aliasing
```

Disables aliasing optimizations that assume type purity.

---

## 🚀 20️⃣ Summary Table

| Type             | Example       | Defined?                    | Notes                    |
| ---------------- | ------------- | --------------------------- | ------------------------ |
| ✅ Defined        | `x = a + b;`  | Yes                         | Standard defines exactly |
| ⚠️ Unspecified   | Order of args | Yes, multiple valid results |                          |
| 💀 Undefined     | `i = i++;`    | No                          | Anything can happen      |
| ⚙️ Impl.-defined | Size of `int` | Defined per compiler        |                          |

---

## ⚡ Key takeaway

> The C compiler assumes **you never trigger undefined behavior**.
> If you do, it stops following your code and starts optimizing **based on lies**.
>
> **UB is the invisible line** between predictable machine code and chaos.

---
---

# 🧩 18️⃣ **Memory Alignment & Struct Padding**

---

## 🧠 1️⃣ What is memory alignment?

**Memory alignment** means that data is stored at addresses that are multiples of their size (or their alignment requirement).

For example:

* A 4-byte `int` is typically stored at an address divisible by 4.
* An 8-byte `double` → address divisible by 8.

✅ This allows the CPU to access data in **fewer cycles**
❌ Misaligned data may cause:

* Slow access (on x86)
* Or even **crashes** (on ARM, SPARC, RISC-V)

---

## ⚙️ 2️⃣ Why alignment matters to CPUs

Imagine your CPU fetching memory in *words* (e.g., 8 bytes at a time).
If a variable starts halfway through one word, the CPU needs **two reads** to get the data.

Example:

```
Address:  0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07
Data:     [ intA ][ intB ]
```

If `intB` starts at 0x02 instead of 0x04, it overlaps → slower and misaligned.

---

## 🧩 3️⃣ Alignment requirements by data type (typical x86-64)

| Type        | Size    | Alignment | Example aligned address |
| ----------- | ------- | --------- | ----------------------- |
| `char`      | 1 byte  | 1         | 0x1000                  |
| `short`     | 2 bytes | 2         | 0x1002                  |
| `int`       | 4 bytes | 4         | 0x1004                  |
| `float`     | 4 bytes | 4         | 0x1008                  |
| `double`    | 8 bytes | 8         | 0x1010                  |
| `long long` | 8 bytes | 8         | 0x1020                  |
| pointer     | 8 bytes | 8         | 0x1030                  |

---

## ⚙️ 4️⃣ The problem: Structs mix types of different alignments

Example:

```c
struct A {
    char c;
    int i;
};
```

Intuitively, you might think:

```
sizeof(char) + sizeof(int) = 1 + 4 = 5 bytes
```

But check:

```c
printf("%zu\n", sizeof(struct A));
```

✅ Output:

```
8
```

Why? → **padding**

---

## 🧩 5️⃣ Visualizing the padding

```
struct A {
    char c;   // 1 byte
    // 3 bytes of padding to align 'i'
    int i;    // 4 bytes
}
```

| Member    | Offset | Size | Notes                             |
| --------- | ------ | ---- | --------------------------------- |
| `c`       | 0      | 1    | char                              |
| padding   | 1–3    | 3    | added by compiler                 |
| `i`       | 4      | 4    | aligned to 4 bytes                |
| **Total** | **8**  | —    | multiple of largest alignment (4) |

✅ So `sizeof(struct A)` = 8 bytes, not 5.

---

## 🧠 6️⃣ Rule of alignment in structs

For every structure:

1. Each member starts at an address **multiple of its alignment**.
2. Total struct size is **padded to a multiple of the largest alignment** (so arrays of the struct are aligned properly).

---

## ⚙️ 7️⃣ Example with mixed members

```c
struct B {
    char  a;    // 1 byte
    double b;   // 8 bytes
    int   c;    // 4 bytes
};
```

Let’s layout:

| Member    | Offset       | Size | Padding                                       |
| --------- | ------------ | ---- | --------------------------------------------- |
| `a`       | 0            | 1    | padding 7 bytes (to align double)             |
| `b`       | 8            | 8    | aligned                                       |
| `c`       | 16           | 4    | padding 4 bytes (to make total multiple of 8) |
| **Total** | **24 bytes** | —    | ✅ aligned to 8                                |

✅ `sizeof(struct B)` = 24.

---

## 🧩 8️⃣ How to optimize structure layout (reduce padding)

You can reorder fields to minimize padding.

```c
// Bad layout
struct bad {
    char c;
    double d;
    int i;
};

// Good layout
struct good {
    double d;  // largest first
    int i;
    char c;
};
```

| Struct | Size       |
| ------ | ---------- |
| bad    | 24 bytes   |
| good   | 16 bytes ✅ |

---

## ⚙️ 9️⃣ Nested structures

If a struct contains another struct, the alignment of the inner struct also affects the outer struct.

```c
struct inner {
    char a;
    int b;
};

struct outer {
    char x;
    struct inner y;
    double z;
};
```

Visualization:

```
outer:
  0   : x
  1-3 : padding
  4   : y.a
  5-7 : padding
  8-11: y.b
 12-15: padding (to align z)
 16-23: z
total = 24
```

✅ `sizeof(struct outer)` = 24 bytes (aligned to 8).

---

## 🧠 10️⃣ Struct alignment rules summary

| Rule | Explanation                                                     |
| ---- | --------------------------------------------------------------- |
| 1    | Each member’s offset must be a multiple of its alignment        |
| 2    | Struct’s total size must be a multiple of its largest alignment |
| 3    | Compiler inserts invisible padding bytes to enforce these rules |
| 4    | Order members from largest → smallest to minimize padding       |

---

## ⚙️ 11️⃣ Controlling alignment manually

### a) GCC/Clang `__attribute__((packed))`

```c
struct __attribute__((packed)) P {
    char c;
    int i;
};
```

✅ Removes all padding → tightly packed (size = 5).
⚠️ But on some architectures, **unaligned access may crash** or slow down.

### b) Align to larger boundary

```c
struct __attribute__((aligned(16))) X {
    int a;
};
```

Forces alignment to 16 bytes.

---

## 🧩 12️⃣ Practical example: reading binary files

Suppose you read from a binary file written by another program:

```c
struct Record {
    char tag;
    int value;
};
```

If the file is packed (no padding), but your compiler inserts padding (size=8),
reading it directly → misaligned data.

✅ Use:

```c
#pragma pack(push, 1)
struct Record { char tag; int value; };
#pragma pack(pop)
```

or

```c
struct __attribute__((packed)) Record { ... };
```

---

## ⚙️ 13️⃣ Arrays of structs

When you have:

```c
struct A {
    char c;
    int i;
};
struct A arr[3];
```

Each element starts at a **multiple of 8 bytes** (since `sizeof(A)` = 8).
This ensures `arr[i].i` stays aligned.

---

## 🧠 14️⃣ Alignment of dynamically allocated data

When you use `malloc()`, memory is aligned to the strictest requirement on your system (typically 16 bytes on x86-64).

✅ So:

```c
struct A *p = malloc(sizeof(struct A));
```

`p` is properly aligned for any type.

If you need custom alignment (e.g., 64 bytes for SIMD):

```c
void *ptr;
posix_memalign(&ptr, 64, 1024);
```

---

## ⚙️ 15️⃣ Inspecting structure layout

### Using `offsetof` macro

```c
#include <stdio.h>
#include <stddef.h>

struct Demo {
    char a;
    int b;
    double c;
};

int main() {
    printf("a: %zu, b: %zu, c: %zu, size: %zu\n",
           offsetof(struct Demo, a),
           offsetof(struct Demo, b),
           offsetof(struct Demo, c),
           sizeof(struct Demo));
}
```

Output:

```
a: 0, b: 4, c: 8, size: 16
```

---

## 🧩 16️⃣ Alignment vs portability

Different compilers or CPUs may pad structs differently!
So binary layouts aren’t portable between:

* 32-bit vs 64-bit
* GCC vs MSVC
* ARM vs x86

✅ If you need exact binary layout (e.g., file I/O, networking):

* Use `#pragma pack` or `__attribute__((packed))`
* Or serialize manually (byte-by-byte)

---

## 🧠 17️⃣ Alignment and performance

On most modern CPUs:

* Aligned memory accesses = 1 cycle
* Unaligned accesses = 2–4 cycles (x86) or crash (ARM)

So even though packing saves space, it can **slow down memory-heavy code**.

Tradeoff:

| Case                              | Recommendation             |
| --------------------------------- | -------------------------- |
| Structs in tight loops            | Keep aligned               |
| Structs sent over network or disk | Pack them                  |
| Embedded (low RAM)                | Pack, but handle carefully |

---

## ⚙️ 18️⃣ Example: alignment mismatch crash (on ARM)

```c
struct P {
    char c;
    int x;
} __attribute__((packed));

int main() {
    struct P p = {'A', 42};
    int *ptr = &p.x;   // misaligned (offset 1)
    printf("%d\n", *ptr); // ❌ crash on ARM
}
```

✅ Works on x86 (CPU handles misaligned access).
💀 Crashes on ARM (hardware alignment enforcement).

---

## 🧩 19️⃣ How compilers ensure alignment in malloc’d memory

The C standard guarantees:

> "The pointer returned by `malloc()` is suitably aligned for any object type."

So:

```c
int *p = malloc(sizeof(int));
double *d = malloc(sizeof(double));
```

Both are always properly aligned.

---

## 🚀 20️⃣ Summary Table

| Concept                   | Meaning                                          |
| ------------------------- | ------------------------------------------------ |
| **Alignment**             | Data stored at address multiple of its alignment |
| **Padding**               | Extra unused bytes inserted for alignment        |
| **Struct size**           | Multiple of largest member’s alignment           |
| **Packed struct**         | No padding — risk of misalignment                |
| **Optimization**          | Order members from largest → smallest            |
| **Alignment-safe malloc** | Always returns sufficiently aligned memory       |
| **Performance**           | Misalignment = slower or crash-prone             |

---

## ⚡ Key takeaway

> In C, **the compiler automatically aligns and pads structures** for performance and CPU safety.
>
> If you care about memory size or binary compatibility, you must **understand and control** this layout — but be careful not to break alignment on strict architectures.

---
---

# 🧩 19️⃣ **Inline Assembly in C**

---

## 🧠 1️⃣ What is inline assembly?

**Inline assembly** means embedding assembly code *directly inside C*.
It gives you **direct access to registers**, **flags**, and **hardware instructions** without leaving your C program.

Example:

```c
int a = 10, b = 20, result;
asm("addl %%ebx, %%eax"
    : "=a"(result)
    : "a"(a), "b"(b));
```

✅ Adds `b` to `a` using CPU registers directly.

---

## ⚙️ 2️⃣ Why use inline assembly?

| Use Case                              | Example                            |
| ------------------------------------- | ---------------------------------- |
| Access CPU registers                  | Read timestamp counter             |
| Hardware I/O                          | Port in/out in embedded/OS         |
| Critical performance                  | Optimized cryptography, pixel math |
| System-level control                  | Syscalls, interrupt enabling       |
| Interfacing with special instructions | SIMD, FPU, or coprocessor          |

---

## 🧩 3️⃣ Inline assembly types

| Type                  | Description                                 |
| --------------------- | ------------------------------------------- |
| **Basic (old-style)** | `asm("instructions");`                      |
| **Extended (GCC)**    | `asm("..." : outputs : inputs : clobbers);` |
| **MSVC style**        | `__asm { ... }` (not in GCC/Clang)          |

We’ll focus on **GCC/Clang Extended Inline Assembly**, which is the standard in Linux/Unix systems.

---

## 🧠 4️⃣ Syntax (GCC extended form)

```c
asm volatile (
    "assembly_template"
    : output_operands
    : input_operands
    : clobbered_registers
);
```

Example:

```c
int a = 10, b = 20, result;
asm volatile (
    "addl %[b], %[a]"
    : [a] "+r" (a)      // output (a gets updated)
    : [b] "r" (b)       // input
);
result = a;
```

---

## ⚙️ 5️⃣ Understanding the components

| Section               | Meaning                                           |
| --------------------- | ------------------------------------------------- |
| `"assembly_template"` | The actual assembly code                          |
| `output_operands`     | Variables modified by assembly                    |
| `input_operands`      | Variables read by assembly                        |
| `clobbers`            | Registers or memory modified indirectly           |
| `volatile`            | Prevent compiler from optimizing or removing code |

---

### Example template placeholders

| Placeholder      | Description                               |
| ---------------- | ----------------------------------------- |
| `%0`, `%1`, `%2` | Positional operands                       |
| `%%eax`, `%%rbx` | Literal register (escaped with `%%`)      |
| `[name]`         | Named operand label                       |
| `"r"`            | “any general-purpose register” constraint |
| `"m"`            | “memory operand” constraint               |

---

## 🧩 6️⃣ Simple example: addition

```c
int a = 3, b = 4, c;
asm("addl %%ebx, %%eax"
    : "=a"(c)
    : "a"(a), "b"(b));
printf("Sum = %d\n", c);
```

Explanation:

* `"a"` binds variable to **EAX**
* `"b"` binds variable to **EBX**
* `"=a"` → output written into EAX

---

## ⚙️ 7️⃣ Using named operands

Named operands make it easier to read:

```c
int a = 5, b = 10, result;
asm("add %[b], %[a]"
    : [a] "+r" (a)
    : [b] "r" (b));
result = a;
```

Equivalent assembly (x86):

```
mov a_reg, a
add a_reg, b_reg
mov a, a_reg
```

✅ `"+r"(a)` → both input & output (read-modify-write).

---

## 🧠 8️⃣ `volatile` keyword in assembly

Without `volatile`, the compiler may **optimize away** your assembly if it thinks the result isn’t used.

✅ Example (read timestamp counter):

```c
unsigned long long tsc;
asm volatile ("rdtsc" : "=A"(tsc));
```

Reads CPU clock cycle counter directly into variable.

---

## ⚙️ 9️⃣ Clobbered registers

Tell the compiler which registers your assembly *destroys* so it doesn’t store useful data there.

Example:

```c
asm volatile ("addl %%ebx, %%eax"
              :
              :
              : "eax", "ebx");
```

Compiler then avoids using `eax` or `ebx` for other C variables around that code.

---

## 🧩 10️⃣ Reading CPU flags (example: carry flag)

```c
unsigned int a = 0xFFFFFFFF, b = 1, carry;
asm(
    "addl %[b], %[a];"
    "setc %[carry];"
    : [a] "+r"(a), [carry] "=r"(carry)
    : [b] "r"(b)
);
printf("Sum = %u, Carry = %u\n", a, carry);
```

✅ Adds two 32-bit numbers and stores carry flag result.

---

## 🧠 11️⃣ Reading special registers (like RSP, RBP)

```c
unsigned long sp;
asm volatile ("mov %%rsp, %0" : "=r"(sp));
printf("Stack pointer: 0x%lx\n", sp);
```

You just accessed the CPU’s **stack pointer** directly!

---

## ⚙️ 12️⃣ Inline assembly for system calls (Linux example)

In Linux, system calls are made via `syscall` instruction on x86-64.

Example: write `"Hello\n"` using syscall:

```c
#include <unistd.h>

int main() {
    const char msg[] = "Hello\n";
    asm volatile (
        "mov $1, %%rax\n\t"   // syscall: write
        "mov $1, %%rdi\n\t"   // fd = stdout
        "mov %[msg], %%rsi\n\t"
        "mov $6, %%rdx\n\t"   // length
        "syscall"
        :
        : [msg] "r"(msg)
        : "rax", "rdi", "rsi", "rdx"
    );
    return 0;
}
```

✅ Works exactly like `write(1, msg, 6)` in libc.

---

## 🧠 13️⃣ Inline assembly for performance tuning (micro-optimizations)

Example: multiply and add in one instruction (`LEA`):

```c
int a = 5, b = 3, c;
asm("lea (%1,%1,4), %0" : "=r"(c) : "r"(a));  // c = a*5
printf("%d\n", c); // Output: 25
```

`LEA` = Load Effective Address → computes arithmetic quickly without affecting flags.

---

## ⚙️ 14️⃣ Output constraints and modifiers

| Constraint | Meaning                                         |
| ---------- | ----------------------------------------------- |
| `"=r"(x)`  | Output in register                              |
| `"+r"(x)`  | Read + write (updated in place)                 |
| `"m"(x)`   | Access memory directly                          |
| `"g"(x)`   | Register or memory                              |
| `"A"(x)`   | EDX:EAX pair (for 64-bit values in 32-bit mode) |

---

## 🧩 15️⃣ Accessing memory operands

```c
int x = 10;
asm("incl %0" : "+m"(x));
printf("%d\n", x); // 11
```

✅ Increments variable `x` directly in memory using the `inc` instruction.

---

## 🧠 16️⃣ Multiple assembly statements

Use `\n\t` for line breaks and tab spacing:

```c
asm volatile (
    "movl $1, %%eax\n\t"
    "movl $2, %%ebx\n\t"
    "addl %%ebx, %%eax"
    : /* no outputs */
    : /* no inputs */
    : "eax", "ebx"
);
```

---

## ⚙️ 17️⃣ Using inline assembly for custom CPU instructions (SIMD / SSE)

Example: sum 4 floats using SSE registers:

```c
#include <xmmintrin.h> // SSE intrinsics header

float sum4(float *a) {
    float result;
    asm volatile (
        "movups (%1), %%xmm0\n\t"
        "haddps %%xmm0, %%xmm0\n\t"
        "haddps %%xmm0, %%xmm0\n\t"
        "movss %%xmm0, %0\n\t"
        : "=m"(result)
        : "r"(a)
        : "xmm0"
    );
    return result;
}
```

✅ Adds 4 floats in a SIMD register.

---

## 🧠 18️⃣ Inline assembly pitfalls

| Mistake                                      | Result                                                       |
| -------------------------------------------- | ------------------------------------------------------------ |
| Forgetting `volatile`                        | Compiler may remove or reorder code                          |
| Missing clobbers                             | Compiler reuses registers you overwrite                      |
| Wrong constraints                            | Variables go in wrong registers or cause crashes             |
| Mixing 32/64-bit registers                   | Partial updates, undefined results                           |
| Using inline asm in optimized builds (`-O2`) | Compiler may reorder around it — always declare side effects |

---

## ⚙️ 19️⃣ Safer alternatives: Intrinsics

Modern compilers provide **intrinsics** — C functions that map to specific CPU instructions but keep type safety.

Example:

```c
#include <immintrin.h>
__m128 a = _mm_set_ps1(1.0f); // moveps xmm
```

✅ Compiles to real SIMD instructions, but is portable and easier to debug.

---

## 🚀 20️⃣ Summary Table

| Concept                       | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `asm("...")`                  | Embed raw assembly                          |
| `asm volatile("...")`         | Prevent optimization                        |
| Output operands               | Tell compiler where results go              |
| Input operands                | Variables used in assembly                  |
| Clobbers                      | Registers/memory modified implicitly        |
| `"r"`, `"m"`, `"g"`           | Operand constraints                         |
| `"+r"`                        | Read/Write operand                          |
| `__attribute__((aligned(N)))` | Alignment control                           |
| Intrinsics                    | High-level, safer alternative to inline asm |

---

## ⚡ Key takeaway

> Inline assembly gives you **ultimate control** over what your CPU does —
> but with great power comes great responsibility.
>
> If you misdeclare registers, forget clobbers, or omit `volatile`,
> your program can miscompile even without visible bugs.

---
---

# 🧩 20️⃣ **Low-level I/O and POSIX System Calls**

---

## 🧠 1️⃣ What are system calls?

Every user-space program (like yours) runs in **user mode**,
and cannot directly access hardware or kernel memory.

When you need the kernel to do something — like read a file, allocate memory, or send data over a network —
you make a **system call** (syscall).

A system call is a controlled jump from **user space → kernel space**.

---

## ⚙️ 2️⃣ System call vs C library function

| Layer                          | Example               | Description                     |
| ------------------------------ | --------------------- | ------------------------------- |
| **Your C code**                | `printf("Hi");`       | Calls a C library function      |
| **C standard library (glibc)** | `write(fd, buf, len)` | Calls a **system call wrapper** |
| **Kernel syscall**             | `sys_write()`         | Actual kernel implementation    |

So:

```
printf() → write() → sys_write() → hardware
```

---

## 🧩 3️⃣ Standard POSIX system calls

| Category        | Common syscalls                                            |
| --------------- | ---------------------------------------------------------- |
| File I/O        | `open`, `read`, `write`, `close`, `lseek`                  |
| File management | `unlink`, `rename`, `stat`, `chmod`                        |
| Process control | `fork`, `exec`, `exit`, `wait`                             |
| Memory          | `brk`, `mmap`, `munmap`                                    |
| Signals         | `kill`, `signal`, `sigaction`                              |
| IPC             | `pipe`, `dup`, `socket`, `bind`, `connect`, `send`, `recv` |

These come from **POSIX (Portable Operating System Interface)** —
a standard API supported by UNIX-like systems (Linux, macOS, BSD).

---

## ⚙️ 4️⃣ The POSIX I/O model — file descriptors

In Linux, **everything is a file**:

* Regular files
* Devices (`/dev/sda`)
* Pipes, sockets
* Even terminals

Every open file is represented by an integer **file descriptor (fd)**:

| FD | Description |
| -- | ----------- |
| 0  | stdin       |
| 1  | stdout      |
| 2  | stderr      |

---

## 🧩 5️⃣ Basic system calls for file I/O

### `open()`

```c
#include <fcntl.h>
int fd = open("file.txt", O_RDONLY);
```

Flags:

* `O_RDONLY` – read only
* `O_WRONLY` – write only
* `O_RDWR` – read/write
* `O_CREAT` – create if not exists
* `O_TRUNC` – truncate existing file
* `O_APPEND` – append to end

Example:

```c
int fd = open("log.txt", O_WRONLY | O_CREAT | O_APPEND, 0644);
```

Permissions `0644` → owner: rw-, group: r--, others: r--.

---

### `read()`

```c
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);
```

Reads up to `count` bytes from `fd` into `buf`.

```c
char buf[100];
ssize_t n = read(fd, buf, sizeof(buf));
```

Returns:

* number of bytes read
* `0` → EOF
* `-1` → error

---

### `write()`

```c
ssize_t write(int fd, const void *buf, size_t count);
```

Example:

```c
write(1, "Hello\n", 6);  // write to stdout
```

✅ This is **faster** and **lower-level** than `printf()`,
but you need to manage formatting and buffers yourself.

---

### `close()`

```c
int close(int fd);
```

Releases the file descriptor and frees kernel resources.

---

## 🧠 6️⃣ Example: copy file using only system calls

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    int src = open("input.txt", O_RDONLY);
    int dest = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    char buf[1024];
    ssize_t n;

    while ((n = read(src, buf, sizeof(buf))) > 0)
        write(dest, buf, n);

    close(src);
    close(dest);
    return 0;
}
```

✅ Works like `cp input.txt output.txt`, but implemented manually.

---

## ⚙️ 7️⃣ `lseek()` — move file pointer

```c
off_t lseek(int fd, off_t offset, int whence);
```

Moves the current position in an open file:

* `SEEK_SET` → from start
* `SEEK_CUR` → from current
* `SEEK_END` → from end

Example:

```c
lseek(fd, 0, SEEK_SET); // rewind to start
```

---

## 🧩 8️⃣ Direct system calls without libc (`syscall()`)

Normally you call `read()` via glibc,
but you can call the kernel directly with `syscall()`:

```c
#include <sys/syscall.h>
#include <unistd.h>

long bytes = syscall(SYS_write, 1, "Hello syscall\n", 14);
```

✅ Equivalent to `write(1, "Hello syscall\n", 14)`

---

## ⚙️ 9️⃣ How syscalls work internally

1. Arguments placed in registers:

   * x86_64 Linux uses:
     RAX = syscall number
     RDI, RSI, RDX, R10, R8, R9 = arguments

2. `syscall` instruction traps to kernel mode.

3. Kernel executes handler (e.g., `sys_write`).

4. Return value goes back in RAX.

---

### Example in pure assembly:

```asm
mov $1, %rax       # syscall: write
mov $1, %rdi       # fd = stdout
mov $msg, %rsi     # buf pointer
mov $13, %rdx      # length
syscall
```

---

## 🧠 10️⃣ Example: read from stdin & echo to stdout

```c
#include <unistd.h>

int main() {
    char buf[100];
    ssize_t n;
    while ((n = read(0, buf, sizeof(buf))) > 0)
        write(1, buf, n);
}
```

✅ This works like the Unix `cat` command.

---

## ⚙️ 11️⃣ Difference between stdio and system calls

| Feature     | `stdio.h` (`fopen`, `fprintf`) | `unistd.h` (`open`, `write`) |
| ----------- | ------------------------------ | ---------------------------- |
| Layer       | Buffered (C library)           | Direct kernel interface      |
| Efficiency  | Buffered, slower per call      | Unbuffered, faster           |
| Ease of use | Formatted I/O                  | Raw bytes                    |
| Portability | High                           | POSIX only                   |
| Use for     | High-level programs            | System/embedded code         |

---

## 🧩 12️⃣ `dup()` and `dup2()` — duplicate file descriptors

Used to redirect streams.

Example:

```c
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd = open("out.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    dup2(fd, 1);       // redirect stdout → file
    write(1, "Hello\n", 6);  // goes into out.txt
    close(fd);
}
```

✅ This is how shells implement redirection (`> out.txt`).

---

## ⚙️ 13️⃣ `pipe()` — interprocess communication

```c
int fds[2];
pipe(fds);
write(fds[1], "Hello", 5);
char buf[6];
read(fds[0], buf, 5);
buf[5] = '\0';
printf("%s\n", buf);  // Output: Hello
```

✅ Used in UNIX pipelines:
`ls | grep txt`

---

## 🧠 14️⃣ Non-blocking I/O

Use `O_NONBLOCK` flag in `open()` or `fcntl()` to make file descriptors non-blocking.

```c
int fd = open("fifo", O_RDONLY | O_NONBLOCK);
```

✅ Useful for event-driven I/O or polling.

---

## 🧩 15️⃣ Checking errors properly

Every syscall returns:

* `>= 0` → success
* `-1` → failure (`errno` set)

Example:

```c
#include <errno.h>
#include <stdio.h>

if (read(fd, buf, 10) == -1)
    perror("read failed");
```

✅ `errno` tells you what went wrong (`EACCES`, `EBADF`, `ENOENT`, etc.)

---

## ⚙️ 16️⃣ High-performance I/O

System calls are expensive (~100ns+).
For large data:

* Use fewer, larger `read()`/`write()` calls.
* Use `mmap()` for memory-mapped I/O (read/write files directly in memory).
* Use `sendfile()` to transfer data kernel-to-kernel without copying to user space.

---

## 🧠 17️⃣ Example: `mmap()` — map file into memory

```c
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    int fd = open("data.txt", O_RDONLY);
    struct stat st;
    fstat(fd, &st);

    char *addr = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    write(1, addr, st.st_size);

    munmap(addr, st.st_size);
    close(fd);
}
```

✅ Maps file into memory — avoids explicit read loops.

---

## ⚙️ 18️⃣ Example: raw system call (no libc) — write via `syscall()`

```c
#include <sys/syscall.h>
#include <unistd.h>

int main() {
    const char msg[] = "Raw syscall write\n";
    syscall(SYS_write, 1, msg, sizeof(msg) - 1);
}
```

✅ Works even without `#include <stdio.h>` — pure Linux kernel interface.

---

## 🧠 19️⃣ Why low-level I/O matters

| Reason              | Explanation                                     |
| ------------------- | ----------------------------------------------- |
| Performance         | No buffering overhead                           |
| Control             | Full access to file descriptors, blocking modes |
| Portability         | POSIX-compliant across all UNIX-like systems    |
| Foundation          | Used internally by libc, shells, and daemons    |
| Systems programming | Required in OS, device drivers, servers         |

---

## 🚀 20️⃣ Summary Table

| Function         | Purpose               |
| ---------------- | --------------------- |
| `open()`         | Open/create file      |
| `read()`         | Read bytes            |
| `write()`        | Write bytes           |
| `close()`        | Close file descriptor |
| `lseek()`        | Move file offset      |
| `dup()`/`dup2()` | Duplicate FD          |
| `pipe()`         | Create IPC pipe       |
| `syscall()`      | Direct system call    |
| `mmap()`         | Map file to memory    |
| `errno`          | Error reporting       |

---

## ⚡ Key takeaway

> Low-level POSIX I/O gives you **direct control over the kernel**.
> It’s faster, unbuffered, and forms the **foundation of all higher-level I/O** in Unix.
>
> Once you understand this layer, you can write your own file utilities, shells, servers, and even parts of an OS.

---
---

# 🧩 21️⃣ **Signals, fork/exec, and Processes**

---

## 🧠 1️⃣ What is a process?

A **process** is a running instance of a program.
Each process has:

* Its own memory (stack, heap, code, globals)
* File descriptors (stdin, stdout, etc.)
* Environment variables
* Process ID (**PID**)

Linux isolates processes but allows controlled communication via **signals**, **pipes**, and **shared memory**.

---

## ⚙️ 2️⃣ The process hierarchy

When Linux starts:

```
init (PID 1)
 ├── getty
 │   ├── bash
 │   │   ├── vim
 │   │   └── gcc
 │   └── login
 └── systemd services...
```

Each process can create child processes → forming a **tree**.
Every child inherits some state (environment, file descriptors, etc.) from its parent.

---

## 🧩 3️⃣ Process creation: `fork()`

`fork()` duplicates the current process.

```c
#include <unistd.h>
pid_t pid = fork();
```

Returns:

* `> 0` → child’s PID (in parent process)
* `0` → in child process
* `-1` → error (no resources)

---

### Example:

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid == 0)
        printf("Child: PID=%d, PPID=%d\n", getpid(), getppid());
    else
        printf("Parent: PID=%d, child PID=%d\n", getpid(), pid);
}
```

**Output (unordered due to scheduling):**

```
Parent: PID=1234, child PID=1235
Child: PID=1235, PPID=1234
```

✅ `fork()` clones the calling process — both keep executing *after* the fork.

---

## 🧠 4️⃣ Memory layout after `fork()`

After `fork()`:

* Both parent and child have identical memory (copy-on-write).
* File descriptors are shared (until closed).
* Variables have same values, but separate copies.

If you modify a variable in one — it doesn’t affect the other (after copy-on-write happens).

---

### Example:

```c
int x = 10;
if (fork() == 0)
    x++;
else
    x--;
printf("%d\n", x);
```

Output (unordered):

```
9
11
```

✅ Two separate processes, two different `x` values.

---

## ⚙️ 5️⃣ Running a new program: `exec()`

`exec()` replaces the current process image with a **new program**.

```c
#include <unistd.h>
execl("/bin/ls", "ls", "-l", NULL);
```

This call **never returns** — the current program is replaced.

### Variants:

| Function                             | Description                  |
| ------------------------------------ | ---------------------------- |
| `execl(path, arg0, arg1, ..., NULL)` | List of args                 |
| `execv(path, argv[])`                | Vector of args               |
| `execle(path, ..., envp[])`          | Custom environment           |
| `execvp(file, argv[])`               | Uses `$PATH` search (common) |

---

### Example:

```c
#include <unistd.h>

int main() {
    char *args[] = {"ls", "-l", "/usr", NULL};
    execvp("ls", args);
}
```

✅ Executes `/bin/ls -l /usr`
If successful, your current process *becomes* `ls`.

---

## 🧩 6️⃣ The `fork()` + `exec()` pattern

Used by **shells**, **init systems**, and **job controllers**.

```c
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child
        execlp("ls", "ls", "-l", NULL);
        perror("exec failed");
    } else {
        // Parent
        wait(NULL);
        printf("Child finished.\n");
    }
}
```

✅ The parent creates a child → child runs `ls` → parent waits → continues.

This is literally how your **shell executes commands**.

---

## 🧠 7️⃣ `wait()` and `waitpid()`

Parent waits for child process termination.

```c
#include <sys/wait.h>
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
```

* Blocks until child exits.
* Returns child PID.
* Stores exit code in `*status`.

Example:

```c
int status;
pid_t cpid = wait(&status);
printf("Child %d exited with %d\n", cpid, WEXITSTATUS(status));
```

---

## ⚙️ 8️⃣ Exit status

Child process ends by:

* Returning from `main()` → exit code of return value
* Calling `exit(status)`
* Being terminated by a signal

Parent sees exit code via `wait()`:

```c
if (WIFEXITED(status))
    printf("Exited normally: %d\n", WEXITSTATUS(status));
```

---

## 🧩 9️⃣ Zombie and orphan processes

### 🧟 Zombie:

* Child has exited, but parent hasn’t called `wait()`.
* Remains in process table with status “Z”.

Solution:

* Always call `wait()` (or `waitpid()`).

### 👶 Orphan:

* Parent exits before child.
* Child gets adopted by `init` (PID 1).

---

## 🧠 10️⃣ The `getpid()` and `getppid()` system calls

```c
printf("PID: %d, Parent PID: %d\n", getpid(), getppid());
```

Every process knows:

* Its own PID (`getpid()`)
* Its parent’s PID (`getppid()`)

---

## ⚙️ 11️⃣ Spawning multiple processes

Example:

```c
for (int i = 0; i < 3; i++) {
    if (fork() == 0) {
        printf("Child %d PID=%d\n", i, getpid());
        _exit(0);
    }
}
for (int i = 0; i < 3; i++)
    wait(NULL);
```

✅ Spawns 3 children, waits for all to finish.

---

## 🧩 12️⃣ Signals — asynchronous process communication

A **signal** is an asynchronous notification sent to a process.

Examples:

* `SIGINT` (Ctrl+C)
* `SIGTERM` (kill request)
* `SIGKILL` (forced kill, cannot be caught)
* `SIGCHLD` (child terminated)
* `SIGALRM` (timer)
* `SIGSEGV` (segmentation fault)

---

## ⚙️ 13️⃣ Sending signals

Use `kill()`:

```c
#include <signal.h>
kill(pid, SIGTERM);
```

Or from shell:

```
kill -9 <pid>
```

---

## 🧠 14️⃣ Handling signals — `signal()` and `sigaction()`

Example:

```c
#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void handler(int sig) {
    printf("Caught signal %d\n", sig);
}

int main() {
    signal(SIGINT, handler); // handle Ctrl+C
    while (1)
        sleep(1);
}
```

✅ Run → press Ctrl+C → prints "Caught signal 2" instead of exiting.

---

### Modern version — `sigaction()`

```c
#include <signal.h>

void handler(int sig) { write(1, "Signal!\n", 8); }

int main() {
    struct sigaction sa = {0};
    sa.sa_handler = handler;
    sigaction(SIGINT, &sa, NULL);
    while (1) pause();
}
```

✅ More portable & thread-safe than `signal()`.

---

## ⚙️ 15️⃣ Ignoring or resetting signals

```c
signal(SIGINT, SIG_IGN);  // ignore Ctrl+C
signal(SIGINT, SIG_DFL);  // restore default behavior
```

---

## 🧩 16️⃣ Signal masks (blocking signals)

Sometimes you need to **block** signals temporarily (e.g., during critical section).

```c
sigset_t set;
sigemptyset(&set);
sigaddset(&set, SIGINT);
sigprocmask(SIG_BLOCK, &set, NULL); // block Ctrl+C
```

---

## 🧠 17️⃣ Signal-safe functions

Inside a signal handler, you can only safely call **async-signal-safe** functions —
like `_exit()`, `write()`, `signal()`, etc.
❌ Never call `printf()` or `malloc()` — may cause reentrancy bugs.

---

## ⚙️ 18️⃣ Process groups and sessions

Used by shells to manage foreground/background jobs.

| Concept                      | Meaning                                          |
| ---------------------------- | ------------------------------------------------ |
| **Process group**            | Set of related processes (e.g., pipeline)        |
| **Session**                  | Group of process groups (e.g., terminal session) |
| **Foreground process group** | One that gets keyboard input                     |

System calls: `setpgid()`, `setsid()`, `tcsetpgrp()`

---

## 🧩 19️⃣ Daemons (background processes)

A **daemon** is a process detached from terminal, usually started at boot.

To daemonize a process:

```c
if (fork() > 0) exit(0);     // parent exits
setsid();                    // new session
chdir("/");                  // change working directory
umask(0);                    // clear file mode mask
close(0); close(1); close(2);
```

✅ Now it runs independently in the background (like `sshd`, `cron`).

---

## 🚀 20️⃣ Summary Table

| Concept           | System Call                | Purpose                     |
| ----------------- | -------------------------- | --------------------------- |
| Process creation  | `fork()`                   | Clone current process       |
| Execute program   | `exec()`                   | Replace process image       |
| Wait for child    | `wait()` / `waitpid()`     | Synchronize parent-child    |
| Terminate process | `exit()` / `_exit()`       | End process                 |
| Get PID           | `getpid()` / `getppid()`   | Get process IDs             |
| Send signal       | `kill()`                   | Notify or terminate process |
| Handle signal     | `signal()` / `sigaction()` | Custom behavior             |
| Block signals     | `sigprocmask()`            | Critical section control    |
| Process group     | `setpgid()`                | Job control                 |
| Daemonize         | `setsid()` + `fork()`      | Run in background           |

---

## ⚡ Key takeaway

> Processes are **independent units of execution**, and **signals** are how they communicate asynchronously.
>
> `fork()` + `exec()` is the foundation of **every Unix shell**,
> and `signal()` + `wait()` are how the kernel and user processes stay in sync.

Once you master this, you can build:

* Your own shell (`fork` + `exec` + `wait`)
* Daemons (`setsid`, `fork`)
* Job control systems (`kill`, `SIGCHLD`)
* Servers that spawn worker processes

---
---

# 🧩 22️⃣ **Threads, Concurrency, and Race Conditions**

---

## 🧠 1️⃣ What is a thread?

A **thread** is a **lightweight process** —
it runs independently but **shares**:

* Memory (heap, globals, static variables)
* File descriptors
* Code and data segments

Each thread has its own:

* **Stack**
* **Program counter**
* **Registers**

So threads are faster to create, destroy, and communicate with than full processes.

---

## ⚙️ 2️⃣ Threads vs Processes

| Feature       | Process                    | Thread                        |
| ------------- | -------------------------- | ----------------------------- |
| Memory        | Separate address space     | Shared memory                 |
| Communication | IPC (pipes, sockets, etc.) | Direct variable sharing       |
| Creation cost | High (`fork()`)            | Low (`pthread_create()`)      |
| Isolation     | Strong                     | Weak (can corrupt each other) |
| Typical use   | Independent programs       | Parallel work in same program |

---

## 🧩 3️⃣ POSIX threads (pthreads)

Linux follows the **POSIX threads (pthreads)** API.
All thread functions are in **`<pthread.h>`** and linked using `-lpthread`.

---

### Example: simplest multithreaded program

```c
#include <stdio.h>
#include <pthread.h>

void* task(void* arg) {
    printf("Hello from thread! arg=%d\n", *(int*)arg);
    return NULL;
}

int main() {
    pthread_t t;
    int value = 42;

    pthread_create(&t, NULL, task, &value);
    pthread_join(t, NULL);

    printf("Thread finished.\n");
}
```

Compile with:

```bash
gcc -pthread main.c -o threads
```

✅ Output:

```
Hello from thread! arg=42
Thread finished.
```

---

## ⚙️ 4️⃣ The core pthread functions

| Function           | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `pthread_create()` | Create a new thread                        |
| `pthread_exit()`   | Exit the current thread                    |
| `pthread_join()`   | Wait for a thread to finish                |
| `pthread_self()`   | Get current thread ID                      |
| `pthread_detach()` | Mark thread as non-joinable (auto cleanup) |

---

### Example:

```c
pthread_t tid;
pthread_create(&tid, NULL, worker, NULL);
pthread_join(tid, NULL);
```

`pthread_join()` blocks until the thread completes, just like `wait()` for processes.

---

## 🧩 5️⃣ Multiple threads example

```c
#include <pthread.h>
#include <stdio.h>

void* work(void* arg) {
    int id = *(int*)arg;
    printf("Thread %d running (PID=%d)\n", id, getpid());
    return NULL;
}

int main() {
    pthread_t threads[3];
    int ids[3] = {1, 2, 3};

    for (int i = 0; i < 3; i++)
        pthread_create(&threads[i], NULL, work, &ids[i]);

    for (int i = 0; i < 3; i++)
        pthread_join(threads[i], NULL);
}
```

✅ Output:

```
Thread 1 running (PID=2341)
Thread 3 running (PID=2341)
Thread 2 running (PID=2341)
```

➡️ Notice: all have the *same PID* but different internal thread IDs.

---

## 🧠 6️⃣ Concurrency vs Parallelism

| Term            | Meaning                                              |
| --------------- | ---------------------------------------------------- |
| **Concurrency** | Multiple tasks *appear* to run at once (interleaved) |
| **Parallelism** | Tasks run *truly simultaneously* (multi-core)        |

Example:

* On a single-core CPU → threads are concurrent.
* On a multi-core CPU → they can be parallel.

---

## ⚙️ 7️⃣ Shared data and race conditions

Threads share memory → great for communication,
but dangerous if two threads modify the same variable at the same time.

### Example of a race condition:

```c
#include <stdio.h>
#include <pthread.h>

int counter = 0;

void* increment(void* arg) {
    for (int i = 0; i < 1000000; i++)
        counter++;
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Final counter = %d\n", counter);
}
```

Expected: `2,000,000`
Actual: Random (e.g., `1,345,892`, `1,980,002`)

✅ That’s a **race condition**.

---

## 🧩 8️⃣ Why race conditions happen

### The statement:

```c
counter++;
```

is *not atomic*.

It’s really:

```asm
mov eax, counter
add eax, 1
mov counter, eax
```

So if two threads run this sequence simultaneously, they can overwrite each other’s results.

---

## ⚙️ 9️⃣ Mutex (Mutual Exclusion Lock)

A **mutex** ensures that only **one thread** executes a critical section at a time.

### Example:

```c
#include <pthread.h>
#include <stdio.h>

int counter = 0;
pthread_mutex_t lock;

void* increment(void* arg) {
    for (int i = 0; i < 1000000; i++) {
        pthread_mutex_lock(&lock);
        counter++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&lock, NULL);

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&lock);
    printf("Final counter = %d\n", counter);
}
```

✅ Output: always `2000000`

---

## 🧠 10️⃣ What happens inside `pthread_mutex_lock()`

Internally:

* If mutex is free → thread acquires it immediately.
* If taken → thread **blocks** (sleeps) until it’s free.
* Prevents data races but can cause **deadlocks** if misused.

---

## ⚙️ 11️⃣ Deadlocks

A **deadlock** occurs when threads wait on each other forever.

Example:

```c
pthread_mutex_t A, B;

void* thread1(void* arg) {
    pthread_mutex_lock(&A);
    pthread_mutex_lock(&B);  // waits here
}
void* thread2(void* arg) {
    pthread_mutex_lock(&B);
    pthread_mutex_lock(&A);  // waits here
}
```

✅ Both threads now wait for each other → **deadlock**.

Fix: always lock in the same order.

---

## 🧩 12️⃣ Other synchronization tools

| Tool                     | Purpose                              |
| ------------------------ | ------------------------------------ |
| **`pthread_mutex_t`**    | Mutual exclusion                     |
| **`pthread_rwlock_t`**   | Reader/writer locks                  |
| **`pthread_spinlock_t`** | Fast, CPU-bound lock                 |
| **`pthread_cond_t`**     | Condition variable for signaling     |
| **`sem_t`**              | Counting semaphore                   |
| **`pthread_barrier_t`**  | Wait until all threads reach a point |

---

## ⚙️ 13️⃣ Condition variables — for signaling between threads

Used for "wait until something happens."

Example:

```c
#include <pthread.h>
#include <stdio.h>

int ready = 0;
pthread_mutex_t lock;
pthread_cond_t cond;

void* waiter(void* arg) {
    pthread_mutex_lock(&lock);
    while (!ready)
        pthread_cond_wait(&cond, &lock);
    printf("Condition met!\n");
    pthread_mutex_unlock(&lock);
    return NULL;
}

void* setter(void* arg) {
    sleep(1);
    pthread_mutex_lock(&lock);
    ready = 1;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&lock, NULL);
    pthread_cond_init(&cond, NULL);

    pthread_create(&t1, NULL, waiter, NULL);
    pthread_create(&t2, NULL, setter, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
}
```

✅ Output:

```
Condition met!
```

---

## 🧠 14️⃣ Thread attributes

You can customize a thread’s:

* Stack size
* Scheduling policy
* Detached state

Example:

```c
pthread_attr_t attr;
pthread_attr_init(&attr);
pthread_attr_setstacksize(&attr, 1024*1024);
pthread_create(&t, &attr, task, NULL);
```

---

## ⚙️ 15️⃣ Detached threads

Detached threads clean themselves up automatically — no `pthread_join()` needed.

```c
pthread_t t;
pthread_create(&t, NULL, task, NULL);
pthread_detach(t);
```

✅ Use when you don’t need to wait for the thread’s result (like background tasks).

---

## 🧩 16️⃣ Race conditions beyond data

Race conditions can also happen in:

* File access (multiple threads writing to same file)
* Resource cleanup
* Signal handling
* Thread cancellation

Always synchronize access to *shared resources*.

---

## 🧠 17️⃣ Thread-safe vs non-thread-safe functions

| Thread-safe           | Non-thread-safe             |
| --------------------- | --------------------------- |
| `write()`, `read()`   | `strtok()`, `asctime()`     |
| `fwrite_unlocked()`   | `localtime()`               |
| `pthread_*` functions | `rand()`, `gethostbyname()` |

Use the `_r` (reentrant) versions if available, e.g. `strtok_r()`.

---

## ⚙️ 18️⃣ Debugging concurrency bugs

🧩 Common tools:

* **Valgrind/Helgrind** → detects race conditions and deadlocks:

  ```bash
  valgrind --tool=helgrind ./threads
  ```
* **ThreadSanitizer**:

  ```bash
  gcc -fsanitize=thread main.c -pthread
  ```

---

## 🧠 19️⃣ Modern alternatives (for C11 and beyond)

C11 introduced **native threads** (in `<threads.h>`):

```c
#include <threads.h>

int work(void* arg) {
    printf("Hello from thread!\n");
    return 0;
}

int main() {
    thrd_t t;
    thrd_create(&t, work, NULL);
    thrd_join(t, NULL);
}
```

Still not as widely supported as pthreads, but cleaner syntax.

---

## 🚀 20️⃣ Summary Table

| Concept            | Description                                      |
| ------------------ | ------------------------------------------------ |
| Thread             | Lightweight unit of execution sharing memory     |
| Concurrency        | Interleaved execution (one CPU)                  |
| Parallelism        | True simultaneous execution (multi-core)         |
| Race condition     | Multiple threads modify shared data without sync |
| Mutex              | Protects critical section                        |
| Condition variable | Signals between threads                          |
| Deadlock           | Threads waiting on each other forever            |
| Detached thread    | No join required                                 |
| Thread sanitizer   | Detects data races automatically                 |

---

## ⚡ Key takeaway

> Threads let your program **do multiple things at once**,
> but shared memory makes them dangerous.
>
> **Concurrency bugs** are the hardest to find — use mutexes, condition variables, and proper design.
> Think of threads as knives: powerful, but cut easily if you’re careless 🔪

---
---

# 🧩 23️⃣ **Networking (Sockets)**

---

## 🧠 1️⃣ What is a socket?

A **socket** is a **communication endpoint**.
It allows two processes — possibly on different machines — to send and receive data.

Think of it like a **file descriptor** that connects two computers.

In Unix, “everything is a file” — so sockets behave just like file descriptors for I/O.

---

## ⚙️ 2️⃣ Basic concept — the 5-tuple connection

A network connection is defined by:

```
(Source IP, Source Port, Destination IP, Destination Port, Protocol)
```

Example:

```
(192.168.1.10, 54321, 93.184.216.34, 80, TCP)
```

---

## 🧩 3️⃣ Types of sockets

| Type                   | Protocol  | Use                                       |
| ---------------------- | --------- | ----------------------------------------- |
| **Stream socket**      | TCP       | Reliable, ordered, connection-oriented    |
| **Datagram socket**    | UDP       | Unreliable, fast, connectionless          |
| **Raw socket**         | IP        | For low-level packet control (root only)  |
| **UNIX domain socket** | Local IPC | For communication between local processes |

---

## ⚙️ 4️⃣ Socket programming model

All socket-based programs follow this flow:

### 🖥️ Server

1. `socket()` – create socket
2. `bind()` – assign IP + port
3. `listen()` – wait for clients
4. `accept()` – accept connection
5. `read()` / `write()` – communicate
6. `close()` – end connection

### 💻 Client

1. `socket()` – create socket
2. `connect()` – connect to server
3. `read()` / `write()` – communicate
4. `close()` – end connection

---

## 🧠 5️⃣ Creating a socket

```c
#include <sys/socket.h>
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
```

| Parameter     | Meaning          |
| ------------- | ---------------- |
| `AF_INET`     | IPv4             |
| `SOCK_STREAM` | TCP              |
| `0`           | default protocol |

✅ Returns a file descriptor like any other file.

---

## ⚙️ 6️⃣ Binding a socket (server)

```c
#include <netinet/in.h>
#include <string.h>

struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);       // host to network short
addr.sin_addr.s_addr = INADDR_ANY; // listen on all interfaces

bind(sockfd, (struct sockaddr*)&addr, sizeof(addr));
```

✅ `htons()` converts 8080 → network byte order (big-endian).

---

## 🧩 7️⃣ Listening and accepting connections

```c
listen(sockfd, 5); // max 5 pending connections

struct sockaddr_in client;
socklen_t len = sizeof(client);
int client_fd = accept(sockfd, (struct sockaddr*)&client, &len);
```

✅ `accept()` blocks until a client connects — returns a new socket descriptor for that client.

---

## ⚙️ 8️⃣ Connecting to a server (client side)

```c
#include <arpa/inet.h>
#include <string.h>

struct sockaddr_in serv;
serv.sin_family = AF_INET;
serv.sin_port = htons(8080);
inet_pton(AF_INET, "127.0.0.1", &serv.sin_addr);

connect(sockfd, (struct sockaddr*)&serv, sizeof(serv));
```

✅ `inet_pton()` converts a string IP (“127.0.0.1”) into a binary address.

---

## 🧠 9️⃣ Sending and receiving data

Use `send()` and `recv()`, or simply `read()` and `write()`.

```c
char buf[1024];
send(sockfd, "Hello", 5, 0);
recv(sockfd, buf, sizeof(buf), 0);
```

✅ `send()` and `recv()` give more control (flags), but `read()`/`write()` work too.

---

## ⚙️ 10️⃣ Closing sockets

```c
close(sockfd);
```

Just like files — closes the connection gracefully (sends TCP FIN packet).

---

## 🧩 11️⃣ Full example — TCP Echo Server

### `server.c`

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;

    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(server_fd, 5);
    printf("Server listening on port 8080...\n");

    struct sockaddr_in client;
    socklen_t len = sizeof(client);
    int client_fd = accept(server_fd, (struct sockaddr*)&client, &len);
    printf("Client connected!\n");

    char buf[1024];
    ssize_t n;
    while ((n = read(client_fd, buf, sizeof(buf))) > 0) {
        write(client_fd, buf, n); // echo back
    }

    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### `client.c`

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv;

    serv.sin_family = AF_INET;
    serv.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &serv.sin_addr);

    connect(sockfd, (struct sockaddr*)&serv, sizeof(serv));
    printf("Connected to server!\n");

    char msg[] = "Hello Server!";
    write(sockfd, msg, strlen(msg));

    char buf[1024];
    int n = read(sockfd, buf, sizeof(buf));
    buf[n] = '\0';
    printf("Received: %s\n", buf);

    close(sockfd);
}
```

✅ Run the server first, then the client.

Output:

```
Server listening on port 8080...
Client connected!

Client: Connected to server!
Received: Hello Server!
```

---

## ⚙️ 12️⃣ UDP (Datagram) Sockets

UDP is **connectionless** — you don’t call `connect()` or `accept()`.

### Server:

```c
int s = socket(AF_INET, SOCK_DGRAM, 0);
bind(s, (struct sockaddr*)&addr, sizeof(addr));
recvfrom(s, buf, sizeof(buf), 0, (struct sockaddr*)&client, &len);
```

### Client:

```c
sendto(s, "Hi", 2, 0, (struct sockaddr*)&server, sizeof(server));
```

✅ Faster than TCP, but no delivery guarantee.

---

## 🧠 13️⃣ Blocking vs non-blocking sockets

Default = **blocking** (`read()` waits for data).
To make **non-blocking**:

```c
#include <fcntl.h>
fcntl(sockfd, F_SETFL, O_NONBLOCK);
```

✅ Useful for event-driven servers (e.g., `select()`, `poll()`, `epoll()`).

---

## ⚙️ 14️⃣ Multiplexing connections — `select()`

Handle multiple clients without threads.

```c
fd_set fds;
FD_ZERO(&fds);
FD_SET(server_fd, &fds);
select(server_fd + 1, &fds, NULL, NULL, NULL);
```

✅ Waits for sockets ready to read/write → efficient single-threaded concurrency.

---

## 🧩 15️⃣ Network byte order

Network protocols use **big-endian** byte order.

Conversion functions:

| Function  | Description            |
| --------- | ---------------------- |
| `htons()` | host → network (short) |
| `htonl()` | host → network (long)  |
| `ntohs()` | network → host (short) |
| `ntohl()` | network → host (long)  |

---

## 🧠 16️⃣ Common sockaddr structures

| Struct                | Purpose             |
| --------------------- | ------------------- |
| `struct sockaddr`     | Generic version     |
| `struct sockaddr_in`  | IPv4                |
| `struct sockaddr_in6` | IPv6                |
| `struct sockaddr_un`  | UNIX domain sockets |

---

## ⚙️ 17️⃣ Useful socket options (`setsockopt`)

| Option         | Description                 |
| -------------- | --------------------------- |
| `SO_REUSEADDR` | Reuse address without delay |
| `SO_KEEPALIVE` | Detect dead TCP connections |
| `SO_RCVTIMEO`  | Timeout for recv()          |
| `SO_SNDTIMEO`  | Timeout for send()          |

Example:

```c
int opt = 1;
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
```

---

## 🧩 18️⃣ UNIX domain sockets (local IPC)

Faster than TCP, no networking — same API but with `AF_UNIX`.

```c
struct sockaddr_un addr;
addr.sun_family = AF_UNIX;
strcpy(addr.sun_path, "/tmp/mysock");
bind(fd, (struct sockaddr*)&addr, sizeof(addr));
```

✅ Used by system daemons, Docker, X11, etc.

---

## 🧠 19️⃣ Debugging network programs

| Tool                       | Use                            |
| -------------------------- | ------------------------------ |
| `netstat -tuln`            | Show listening sockets         |
| `ss -ltn`                  | Modern replacement for netstat |
| `lsof -i`                  | Show which process uses a port |
| `tcpdump -i any port 8080` | Capture packets                |
| `nc` (netcat)              | Test sockets manually          |

---

## 🚀 20️⃣ Summary Table

| Function                        | Purpose                 |
| ------------------------------- | ----------------------- |
| `socket()`                      | Create a socket         |
| `bind()`                        | Assign IP/port          |
| `listen()`                      | Wait for connections    |
| `accept()`                      | Accept incoming client  |
| `connect()`                     | Connect to server       |
| `send()` / `recv()`             | Exchange data           |
| `close()`                       | Close socket            |
| `htons()`, `ntohl()`            | Convert byte order      |
| `setsockopt()`                  | Set socket options      |
| `select()`, `poll()`, `epoll()` | Handle multiple sockets |

---

## ⚡ Key takeaway

> Sockets are the **universal interface** for communication — local or networked.
>
> They form the foundation of HTTP, SSH, DNS, SMTP, and every modern Internet service.
>
> Once you master sockets, you can build **servers, clients, chat apps, and even distributed systems**.

---
---

# 🧩 24️⃣ **Dynamic Libraries (`dlopen`, `dlsym`, `dlclose`)**

---

## 🧠 1️⃣ What are dynamic libraries?

A **dynamic library** (aka **shared library**, `.so` in Linux, `.dll` in Windows)
is a compiled object file **loaded at runtime** rather than at program startup.

It contains **compiled code** that can be shared between multiple programs.

Examples:

* `/lib/x86_64-linux-gnu/libc.so.6` — C standard library
* `/usr/lib/libm.so` — math library
* `/usr/lib/libpthread.so` — threading

---

## ⚙️ 2️⃣ Static vs Shared vs Dynamic Loading

| Type                           | Linked at    | Loaded when      | Function calls resolved when | Example            |
| ------------------------------ | ------------ | ---------------- | ---------------------------- | ------------------ |
| **Static library (.a)**        | Compile time | At build         | At compile                   | `ar rcs libfoo.a`  |
| **Shared library (.so)**       | Link time    | Program start    | At load                      | `gcc main.c -lfoo` |
| **Dynamic loading (`dlopen`)** | Runtime      | Only when needed | At runtime                   | Plugin systems     |

---

## 🧩 3️⃣ Shared library creation example

Let’s start by building a shared library.

### `mathlib.c`

```c
#include <stdio.h>

void hello() {
    printf("Hello from shared library!\n");
}

int add(int a, int b) {
    return a + b;
}
```

Compile to shared object:

```bash
gcc -fPIC -shared -o libmathlib.so mathlib.c
```

✅ `-fPIC` → Position Independent Code (needed for shared libs)
✅ `-shared` → produce `.so` file

Now you have a `libmathlib.so` that any program can use.

---

## ⚙️ 4️⃣ Linking normally (static dynamic linking)

You can link it directly like:

```bash
gcc main.c -L. -lmathlib -o main
```

But now we’ll go one step deeper: **load it manually at runtime**.

---

## 🧩 5️⃣ The `<dlfcn.h>` interface

POSIX defines the **Dynamic Loader API**:

```c
#include <dlfcn.h>

void *dlopen(const char *filename, int flags);
void *dlsym(void *handle, const char *symbol);
int dlclose(void *handle);
char *dlerror(void);
```

All are declared in `<dlfcn.h>` and require linking with `-ldl`.

---

## ⚙️ 6️⃣ Example: loading a shared library at runtime

### `main.c`

```c
#include <stdio.h>
#include <dlfcn.h>

int main() {
    void *handle;
    void (*hello_func)();
    int (*add_func)(int, int);
    char *error;

    // 1. Load library
    handle = dlopen("./libmathlib.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "Error: %s\n", dlerror());
        return 1;
    }

    // 2. Load symbols (function pointers)
    hello_func = dlsym(handle, "hello");
    add_func   = dlsym(handle, "add");

    if ((error = dlerror()) != NULL) {
        fprintf(stderr, "Symbol error: %s\n", error);
        dlclose(handle);
        return 1;
    }

    // 3. Call dynamically loaded functions
    hello_func();
    printf("Result = %d\n", add_func(3, 4));

    // 4. Close library
    dlclose(handle);
    return 0;
}
```

Compile:

```bash
gcc main.c -ldl -o dynload
```

Run:

```
./dynload
```

Output:

```
Hello from shared library!
Result = 7
```

✅ You just dynamically loaded and executed functions from a shared library at runtime!

---

## 🧠 7️⃣ Understanding `dlopen()` flags

| Flag          | Meaning                             |
| ------------- | ----------------------------------- |
| `RTLD_LAZY`   | Resolve symbols as needed (faster)  |
| `RTLD_NOW`    | Resolve all symbols immediately     |
| `RTLD_GLOBAL` | Export symbols for future libraries |
| `RTLD_LOCAL`  | (default) Keep symbols private      |

Example:

```c
dlopen("libmathlib.so", RTLD_NOW | RTLD_GLOBAL);
```

---

## ⚙️ 8️⃣ How `dlsym()` works

* `dlsym(handle, "symbol")` looks for the given function or variable in the library.
* Returns a **`void*` pointer**.
* You cast it to the right function type before calling.

Example:

```c
int (*sum)(int,int) = (int (*)(int,int)) dlsym(handle, "add");
```

---

## 🧩 9️⃣ Handling errors with `dlerror()`

Always clear and check errors:

```c
dlerror(); // clear any old error
sum = dlsym(handle, "add");
char *err = dlerror();
if (err) {
    fprintf(stderr, "Error: %s\n", err);
}
```

✅ `dlerror()` returns a human-readable string describing what went wrong.

---

## ⚙️ 10️⃣ Closing the library (`dlclose`)

```c
dlclose(handle);
```

* Decrements reference count.
* When count reaches 0 → library is unloaded from memory.
* All pointers to its functions become invalid.

---

## 🧠 11️⃣ Dynamic loading of variables

You can also load **global variables**.

Example (`libvar.c`):

```c
int value = 42;
```

Build:

```bash
gcc -fPIC -shared -o libvar.so libvar.c
```

Load in C:

```c
int *ptr = dlsym(handle, "value");
printf("Value = %d\n", *ptr);
```

✅ Works exactly like function loading.

---

## ⚙️ 12️⃣ Using `dlopen()` for plugins (real-world example)

Many applications (like **VLC**, **GIMP**, **Python**, and **VSCode**)
load **plugin modules** at runtime using this technique.

Example pseudo-flow:

```c
// Discover plugin
char plugin_path[256] = "./plugins/plugin1.so";
void *handle = dlopen(plugin_path, RTLD_NOW);

// Each plugin must define an init function
void (*init_plugin)() = dlsym(handle, "plugin_init");
init_plugin();
```

---

## 🧩 13️⃣ Environment variables controlling dynamic loading

| Variable          | Purpose                                                            |
| ----------------- | ------------------------------------------------------------------ |
| `LD_LIBRARY_PATH` | Search path for `.so` files                                        |
| `LD_PRELOAD`      | Force-load a library before others (used for debugging or hooking) |
| `LD_DEBUG`        | Print loader debug info                                            |

Example:

```bash
LD_LIBRARY_PATH=./libs ./myapp
```

---

## ⚙️ 14️⃣ Checking linked libraries

```bash
ldd ./dynload
```

Example output:

```
linux-vdso.so.1 =>  (0x00007ffd5b5fd000)
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f5f0b2b0000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f5f0aef0000)
```

✅ Shows which `.so` files are linked at runtime.

---

## 🧠 15️⃣ Example — calling unknown plugin functions dynamically

Imagine a plugin defines this:

```c
void register_plugin(const char *name);
```

You don’t know it at compile time.
But at runtime:

```c
void (*register_plugin)(const char*);
register_plugin = dlsym(handle, "register_plugin");
register_plugin("Audio Enhancer");
```

✅ This is exactly how **plugin systems** like OBS, GIMP, and Audacity work.

---

## ⚙️ 16️⃣ Symbol versioning and dependencies

Dynamic libraries can depend on other `.so` files.
When loading `libfoo.so`, the loader automatically loads its dependencies (from ELF headers).

You can inspect with:

```bash
readelf -d libfoo.so
```

Look for:

```
NEEDED libbar.so
```

---

## 🧩 17️⃣ Thread safety

`dlopen`, `dlsym`, `dlclose`, and `dlerror` are thread-safe.
But if your library has **global state**, you must synchronize access manually.

---

## ⚙️ 18️⃣ Advanced: `RTLD_NEXT` and function interposition

You can override symbols at runtime:

Example: wrap `malloc()`:

```c
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

void *malloc(size_t size) {
    static void* (*real_malloc)(size_t) = NULL;
    if (!real_malloc)
        real_malloc = dlsym(RTLD_NEXT, "malloc");

    printf("Allocating %zu bytes\n", size);
    return real_malloc(size);
}
```

Compile:

```bash
gcc -fPIC -shared -o malloc_hook.so malloc_hook.c -ldl
```

Run:

```bash
LD_PRELOAD=./malloc_hook.so ./your_program
```

✅ This technique is used by **profilers**, **sanitizers**, and **LD_PRELOAD-based hooks**.

---

## 🧠 19️⃣ Common pitfalls

| Mistake                          | Consequence                                   |
| -------------------------------- | --------------------------------------------- |
| Forget `-ldl`                    | Linker error: `undefined reference to dlopen` |
| Forget `RTLD_LAZY` or `RTLD_NOW` | `dlopen()` fails                              |
| Wrong function cast              | Segfault when calling                         |
| Forget `dlclose()`               | Memory leak                                   |
| Missing `LD_LIBRARY_PATH`        | Loader can’t find `.so`                       |

---

## 🚀 20️⃣ Summary Table

| Function                 | Purpose                                      |
| ------------------------ | -------------------------------------------- |
| `dlopen()`               | Load shared library at runtime               |
| `dlsym()`                | Look up a function or variable               |
| `dlerror()`              | Get error message                            |
| `dlclose()`              | Unload library                               |
| `RTLD_LAZY` / `RTLD_NOW` | Lazy vs eager symbol resolution              |
| `LD_LIBRARY_PATH`        | Library search path                          |
| `LD_PRELOAD`             | Preload libraries for interposition          |
| `-fPIC`                  | Generate position-independent code for `.so` |

---

## ⚡ Key takeaway

> `dlopen()` and `dlsym()` give C programs **runtime modularity** —
> load code dynamically like Python imports, extend programs without recompiling,
> and implement plugin-based architectures.

You’ve now learned the **entire lifecycle of dynamic linking**, from compilation to runtime loading 🔥

---
---

# 🧩 25️⃣ **Makefiles & Compiler Optimization Flags**

---

## 🧠 1️⃣ What is a Makefile?

A **Makefile** is an automation script for compiling and linking multi-file C programs.

Instead of typing long `gcc` commands every time,
you just type `make` and it figures out what needs to be rebuilt.

---

### Basic idea:

```bash
gcc -c main.c
gcc -c utils.c
gcc main.o utils.o -o app
```

becomes 👇

```make
app: main.o utils.o
	gcc main.o utils.o -o app

main.o: main.c
	gcc -c main.c

utils.o: utils.c
	gcc -c utils.c
```

Then:

```bash
make
```

✅ Automatically builds only what changed.

---

## ⚙️ 2️⃣ Makefile syntax

### General form:

```
target: dependencies
<TAB> command
```

* **target** → file or goal to build
* **dependencies** → files needed to build target
* **command** → executed if dependencies are newer than target

Tabs **must** be used before commands (not spaces!).

---

## 🧩 3️⃣ Variables in Makefiles

Variables make rules reusable:

```make
CC = gcc
CFLAGS = -Wall -Wextra -O2
OBJ = main.o utils.o

app: $(OBJ)
	$(CC) $(OBJ) -o app $(CFLAGS)
```

✅ `$(CC)` → compiler
✅ `$(CFLAGS)` → compiler flags
✅ `$(OBJ)` → object files

Run:

```bash
make
```

---

## ⚙️ 4️⃣ Phony targets

Some targets (like “clean”) don’t produce files.

```make
.PHONY: clean
clean:
	rm -f *.o app
```

✅ Use `.PHONY` to avoid confusion with files of same name.

---

## 🧠 5️⃣ Automatic variables

Make provides automatic variables for convenience:

| Variable | Meaning          |
| -------- | ---------------- |
| `$@`     | Target name      |
| `$<`     | First dependency |
| `$^`     | All dependencies |

Example:

```make
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
```

✅ Compiles any `.c` file into `.o`.

---

## ⚙️ 6️⃣ Example: full Makefile for a small project

```
# Makefile for myapp
CC = gcc
CFLAGS = -Wall -O2
OBJ = main.o math.o io.o
TARGET = myapp

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(CFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)
```

✅ Usage:

```bash
make        # build
make clean  # remove binaries
```

---

## 🧩 7️⃣ Include dependencies automatically

Generate `.d` dependency files (headers):

```make
%.d: %.c
	@$(CC) -M $< > $@
-include $(SRC:.c=.d)
```

✅ Ensures recompilation if headers change.

---

## ⚙️ 8️⃣ Parallel builds

Use multiple CPU cores:

```bash
make -j$(nproc)
```

✅ Builds independent files concurrently (great for big projects).

---

## 🧠 9️⃣ Common Makefile macros

| Variable  | Description                    |
| --------- | ------------------------------ |
| `CC`      | Compiler (gcc, clang)          |
| `CFLAGS`  | Compiler flags                 |
| `LDFLAGS` | Linker flags                   |
| `LDLIBS`  | Libraries (`-lm`, `-lpthread`) |
| `SRC`     | Source files                   |
| `OBJ`     | Object files                   |
| `TARGET`  | Output binary                  |

---

## ⚙️ 10️⃣ Example: linking libraries

```make
CC = gcc
CFLAGS = -Wall -O2
LDFLAGS = -L. -lmylib
LDLIBS = -ldl -lpthread

app: main.o
	$(CC) $^ $(LDFLAGS) $(LDLIBS) -o $@
```

✅ Automatically links your custom `.so` libraries.

---

## 🧠 11️⃣ Makefile best practices

✅ Always include `-Wall -Wextra`
✅ Use variables for compiler flags
✅ Separate source, build, and output dirs
✅ Use `.PHONY` for non-file targets
✅ Add a `clean` rule

---

---

# ⚙️ Compiler Optimization Flags 🧠

---

Now let’s cover the *second half* of the topic —
how to make your binaries **faster, smaller, or debuggable**.

---

## 🧩 12️⃣ Optimization levels

| Flag     | Description                                             |
| -------- | ------------------------------------------------------- |
| `-O0`    | No optimization (default, fastest compile)              |
| `-O1`    | Basic optimization                                      |
| `-O2`    | Recommended for most production builds (safe, fast)     |
| `-O3`    | Aggressive optimization (loop unrolling, vectorization) |
| `-Ofast` | Breaks strict IEEE rules for more speed                 |
| `-Os`    | Optimize for **size**                                   |
| `-Oz`    | (Clang) even smaller binary                             |
| `-Og`    | Optimized for debugging (GCC)                           |

Example:

```bash
gcc main.c -O2 -o app
```

---

## ⚙️ 13️⃣ Architecture-specific tuning

| Flag                | Description                                    |
| ------------------- | ---------------------------------------------- |
| `-march=native`     | Optimize for your CPU                          |
| `-mtune=generic`    | Tune for broad compatibility                   |
| `-mavx`, `-msse4.2` | Enable vector instructions                     |
| `-mfma`             | Use Fused Multiply-Add instructions            |
| `-pipe`             | Use pipes instead of temp files when compiling |

Example:

```bash
gcc -O3 -march=native -flto main.c -o app
```

✅ Enables all CPU instructions available on your machine.

---

## 🧠 14️⃣ Link-time optimization (LTO)

`-flto` allows GCC to optimize **across multiple files** during linking.

```bash
gcc -O3 -flto main.c utils.c -o app
```

✅ Produces faster and smaller binaries.

---

## ⚙️ 15️⃣ Profile-guided optimization (PGO)

PGO compiles your code based on **real execution profiles**.

### Steps:

1. Compile with profiling:

   ```bash
   gcc -fprofile-generate -O2 *.c -o app
   ```
2. Run your program with typical inputs:

   ```bash
   ./app
   ```
3. Recompile using profile data:

   ```bash
   gcc -fprofile-use -O2 *.c -o app
   ```

✅ Compiler optimizes hot code paths based on actual usage.

---

## 🧩 16️⃣ Debugging flags

| Flag                      | Purpose                                  |
| ------------------------- | ---------------------------------------- |
| `-g`                      | Include debugging info                   |
| `-ggdb`                   | Detailed debug info for GDB              |
| `-O0`                     | Disable optimization for clear debugging |
| `-fno-omit-frame-pointer` | Easier stack traces                      |

Example:

```bash
gcc -g -O0 main.c -o debug_app
```

---

## ⚙️ 17️⃣ Warning and safety flags

| Flag                   | Purpose                    |
| ---------------------- | -------------------------- |
| `-Wall`                | Enable all common warnings |
| `-Wextra`              | More warnings              |
| `-Werror`              | Treat warnings as errors   |
| `-pedantic`            | Enforce strict ISO C       |
| `-fsanitize=address`   | Detect memory errors       |
| `-fsanitize=undefined` | Detect undefined behavior  |

Example:

```bash
gcc -Wall -Wextra -fsanitize=address main.c -o safe_app
```

✅ AddressSanitizer finds buffer overflows and use-after-free bugs.

---

## 🧠 18️⃣ Reducing binary size

| Flag                                                    | Description           |
| ------------------------------------------------------- | --------------------- |
| `-Os`                                                   | Optimize for size     |
| `-s`                                                    | Strip symbol table    |
| `strip app`                                             | Remove all debug info |
| `-fdata-sections -ffunction-sections -Wl,--gc-sections` | Remove unused code    |

Example:

```bash
gcc -Os -s -ffunction-sections -fdata-sections -Wl,--gc-sections main.c -o tiny
```

✅ Great for embedded or distro packaging.

---

## ⚙️ 19️⃣ Profiling and performance measurement

### `gprof`

```bash
gcc -pg main.c -o prof_app
./prof_app
gprof prof_app gmon.out > report.txt
```

### `perf`

Linux kernel tool for CPU analysis:

```bash
perf record ./app
perf report
```

---

## 🧩 20️⃣ Example: Professional-grade Makefile

```make
CC = gcc
CFLAGS = -Wall -Wextra -O2 -march=native -flto
LDFLAGS = -lm -lpthread
OBJ = main.o math.o io.o
TARGET = app

$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $@ $(CFLAGS) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)
```

✅ Add `make -j$(nproc)` → parallel build.
✅ Add `CFLAGS=-g -O0` → debug build.

---

# 🚀 Summary Table

| Flag/Concept              | Purpose                           |
| ------------------------- | --------------------------------- |
| `make`                    | Automate builds                   |
| `$@`, `$<`, `$^`          | Auto variables                    |
| `CC`, `CFLAGS`, `LDFLAGS` | Build config                      |
| `-O0` → `-O3`             | Optimization levels               |
| `-Ofast`                  | Maximum optimization, unsafe math |
| `-Os`, `-Oz`              | Optimize for size                 |
| `-march=native`           | Use CPU’s full capabilities       |
| `-flto`                   | Link-time optimization            |
| `-fprofile-use`           | Profile-guided optimization       |
| `-Wall -Wextra`           | Enable all warnings               |
| `-fsanitize`              | Runtime checks for memory bugs    |
| `make -j`                 | Parallel builds                   |

---

## ⚡ Key takeaway

> **Makefiles** let you manage large projects efficiently,
> while **compiler flags** give you fine control over performance, size, and safety.
>
> Real pros know how to switch between:
> 🧩 `-O0 -g` → debugging
> ⚙️ `-O2 -flto` → production
> 🧠 `-Ofast -march=native` → performance-critical builds

---
---

# 🧩 26️⃣ **Profiling Tools (`gprof`, `perf`, `valgrind --tool=cachegrind`)**

---

## 🧠 1️⃣ Why profiling?

> “Premature optimization is the root of all evil.” — Donald Knuth

Profiling helps you **find the slow parts** of your program before you optimize.
Without it, you’re guessing.

Profilers measure:

* CPU usage per function
* Function call frequency
* Cache misses
* Branch mispredictions
* I/O time
* System call overhead

---

## ⚙️ 2️⃣ Categories of profilers

| Type                  | Examples            | Description                      |
| --------------------- | ------------------- | -------------------------------- |
| **Sampling**          | `perf`, `gprof`     | Record stack traces at intervals |
| **Instrumentation**   | `gprof`, `valgrind` | Modify binary to collect data    |
| **Hardware-assisted** | `perf`, `OProfile`  | Use CPU counters                 |
| **Cache simulators**  | `cachegrind`        | Emulate L1/L2 cache performance  |

---

## 🧩 3️⃣ Setup for profiling (general rule)

To get accurate profiling:

1. **Compile with debug symbols**

   ```bash
   gcc -g -O2 main.c -o app
   ```
2. **Run with typical input**
3. **Analyze results**
4. **Optimize only where it matters**

---

# ⚙️ Part 1 — `gprof`

---

## 🧠 4️⃣ What is `gprof`?

`gprof` is the **GNU profiler** that analyzes:

* Time spent in each function
* Function call counts
* Call relationships (caller/callee tree)

---

## 🧩 5️⃣ How `gprof` works

1. Compiler inserts profiling hooks using `-pg`
2. When program runs, timing and call info are saved to `gmon.out`
3. You analyze that file with `gprof`

---

## ⚙️ 6️⃣ Example

### `profile_test.c`

```c
#include <stdio.h>

void work1() {
    for (volatile int i = 0; i < 10000000; i++);
}

void work2() {
    for (volatile int i = 0; i < 20000000; i++);
}

int main() {
    work1();
    work2();
    return 0;
}
```

Compile with profiling enabled:

```bash
gcc -pg -O2 profile_test.c -o profile_test
```

Run:

```bash
./profile_test
```

✅ This creates a file named `gmon.out`

---

## 🧠 7️⃣ Analyze results

Run:

```bash
gprof ./profile_test gmon.out > report.txt
```

Sample output:

```
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total
 time   seconds   seconds    calls  ms/call  ms/call  name
 33.3      0.10     0.10         1   100.00   100.00  work1
 66.7      0.30     0.20         1   200.00   200.00  work2
```

✅ You can clearly see `work2()` took twice as long as `work1()`.

---

## ⚙️ 8️⃣ Call graph output

`gprof` also shows how functions call each other:

```
index %time    self  children    called     name
[1]    66.7    0.2    0.0       1         main [1]
                1/1                 work1 [2]
                1/1                 work2 [3]
```

---

## 🧩 9️⃣ Pros and cons of `gprof`

✅ **Advantages**

* Easy to use
* No external dependencies
* Works on any GCC program

❌ **Disadvantages**

* Doesn’t handle multi-threaded code well
* Doesn’t measure I/O wait time
* Slower due to instrumentation

---

# ⚙️ Part 2 — `perf` (Linux kernel profiler)

---

## 🧠 10️⃣ What is `perf`?

`perf` is a **powerful Linux profiling framework** built into the kernel.
It measures **hardware events** like:

* CPU cycles
* Cache misses
* Branch mispredictions
* Context switches
* Function call frequency

It’s much more detailed than `gprof`.

---

## 🧩 11️⃣ Using `perf` for basic profiling

Compile normally (no `-pg` required):

```bash
gcc -g -O2 main.c -o app
```

Run:

```bash
perf record ./app
```

✅ Collects performance data during execution.

Then:

```bash
perf report
```

Shows interactive interface with:

* CPU usage per function
* Time percentage
* Assembly with hotspots highlighted

---

## ⚙️ 12️⃣ Example output (simplified)

```
Samples: 3K of event 'cycles', Event count (approx.): 3,000,000
  Overhead  Command  Shared Object       Symbol
  40.01%    app      app                 [.] work2
  20.34%    app      app                 [.] work1
  10.12%    app      libc-2.33.so        [.] printf
```

✅ You can see which functions consume CPU cycles.

---

## 🧠 13️⃣ Inspecting assembly view

In `perf report`, press **`a`** to see annotated disassembly:
shows exactly which assembly instruction eats the most time.

Example:

```
  │     mov    eax,DWORD PTR [rbp-0x4]
  │     inc    eax
  │     mov    DWORD PTR [rbp-0x4],eax  # <--- Hot line
```

---

## ⚙️ 14️⃣ Advanced perf commands

| Command             | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `perf stat ./app`   | Basic performance summary                            |
| `perf record ./app` | Record detailed profile                              |
| `perf report`       | Interactive analysis                                 |
| `perf annotate`     | View annotated assembly                              |
| `perf top`          | Real-time CPU profiler (like `top` but per function) |

Example:

```bash
perf stat ./app
```

Output:

```
 Performance counter stats for './app':
    1,000,000,000 cycles
      200,000,000 instructions
     20,000,000 cache-misses
```

---

## 🧩 15️⃣ Perf hardware counters

| Event              | Meaning                     |
| ------------------ | --------------------------- |
| `cycles`           | CPU cycles used             |
| `instructions`     | Total executed instructions |
| `cache-misses`     | Missed cache lookups        |
| `branch-misses`    | Wrong branch predictions    |
| `context-switches` | OS switched between threads |
| `page-faults`      | Memory page misses          |

---

## ⚙️ 16️⃣ Example: compare two builds

```bash
perf stat ./app_O2
perf stat ./app_O3
```

✅ Quickly see how optimization flags change performance.

---

## 🧠 17️⃣ Combining perf with flamegraphs (optional pro tip)

You can generate **flamegraphs** to visualize CPU usage:

```bash
perf record -F 99 -a -g ./app
perf script > out.perf
./flamegraph.pl out.perf > flamegraph.svg
```

✅ Shows time spent per call stack — extremely powerful for performance debugging.

---

# ⚙️ Part 3 — `valgrind --tool=cachegrind`

---

## 🧠 18️⃣ What is Cachegrind?

`cachegrind` is part of **Valgrind**.
It simulates the CPU’s **L1/L2 caches** and instruction pipelines to measure:

* Cache misses (L1/L2)
* Branch prediction accuracy
* Instruction-level efficiency

It’s like running your program inside a **virtual CPU performance analyzer**.

---

## 🧩 19️⃣ Using Cachegrind

Compile with debugging info:

```bash
gcc -g -O2 app.c -o app
```

Run under cachegrind:

```bash
valgrind --tool=cachegrind ./app
```

Output:

```
==12345== I   refs:      1,000,000
==12345== I1  misses:         200
==12345== LLi misses:          50
==12345== D   refs:        500,000
==12345== D1  misses:       1,000
==12345== LLd misses:         200
==12345== Branch mispred:      30
```

✅ `I` → instruction cache
✅ `D` → data cache
✅ `LL` → last-level cache
✅ Shows where CPU stalls happen.

---

## ⚙️ 20️⃣ Viewing detailed function breakdown

After running, Cachegrind creates:

```
cachegrind.out.<pid>
```

View with:

```bash
cg_annotate cachegrind.out.<pid> | less
```

Example:

```
--------------------------------------------------------------------------------
Ir   I1mr  ILmr  Dr  D1mr  DLmr  Dw  D1mw  DLmw   Function
--------------------------------------------------------------------------------
3,000  100    10  1,500   200    40  750   150     work2
1,500   20     5    800   100    20  400    80     work1
```

✅ Ir = Instruction reads
✅ Dr = Data reads
✅ D1mr/D1mw = L1 misses
✅ DLmr/DLmw = L2 misses

---

## 🧠 21️⃣ How to interpret results

| Metric                   | Meaning                   | Fix                    |
| ------------------------ | ------------------------- | ---------------------- |
| High **I1 misses**       | Poor instruction locality | Inline small functions |
| High **D1 misses**       | Poor data locality        | Improve array layout   |
| High **LL misses**       | Cache too small           | Change data structures |
| High **branch mispreds** | Unpredictable branches    | Simplify conditions    |

---

## ⚙️ 22️⃣ Compare cache performance across versions

Run cachegrind twice:

```bash
valgrind --tool=cachegrind ./v1
valgrind --tool=cachegrind ./v2
cg_diff cachegrind.out.v1 cachegrind.out.v2 > diff.out
cg_annotate diff.out
```

✅ Shows exactly how your optimization affected cache efficiency.

---

## 🧩 23️⃣ Combining all three tools

| Tool         | Measures                             | Use Case                 |
| ------------ | ------------------------------------ | ------------------------ |
| `gprof`      | Function call times                  | Basic CPU profiling      |
| `perf`       | Hardware counters, syscalls, threads | Advanced Linux profiling |
| `cachegrind` | Cache and instruction efficiency     | Micro-level optimization |

---

## 🧠 24️⃣ Bonus: Valgrind vs Perf

| Feature                   | `valgrind` | `perf`        |
| ------------------------- | ---------- | ------------- |
| Works on any system       | ✅          | ✅             |
| Requires root             | ❌          | Sometimes     |
| Affects timing            | Yes (slow) | No            |
| Measures cache simulation | ✅          | Real hardware |
| Measures kernel time      | ❌          | ✅             |

✅ Use Valgrind for precision & education.
✅ Use Perf for real-world performance.

---

## 🚀 25️⃣ Summary Table

| Tool            | Command                              | What it shows                        |
| --------------- | ------------------------------------ | ------------------------------------ |
| **gprof**       | `gcc -pg prog.c` → `gprof ./prog`    | Function-level timing                |
| **perf**        | `perf record ./prog` → `perf report` | CPU usage, syscalls, cache, branches |
| **cachegrind**  | `valgrind --tool=cachegrind ./prog`  | Simulated cache efficiency           |
| **cg_annotate** | Analyze `cachegrind.out.*`           | Function-level cache data            |
| **cg_diff**     | Compare two runs                     | Optimization effect                  |

---

## ⚡ Key takeaway

> Profiling turns *guessing* into *measuring*.
>
> * Use **`gprof`** for function-level timing
> * Use **`perf`** for CPU, kernel, and real hardware stats
> * Use **`valgrind --tool=cachegrind`** for micro-architecture tuning

These tools let you see *inside your CPU* — instruction by instruction, cache by cache line —
and give you the insight to turn your code from **working** → **blazingly efficient** ⚙️🔥

---
---

# 🧩 27️⃣ **Custom Allocators & Manual Optimizations**

---

## 🧠 1️⃣ Why build custom allocators?

The default `malloc()` is **general-purpose** — great for most cases,
but sometimes it’s too **slow**, **fragmented**, or **wasteful** for performance-critical systems.

Real-world cases:

* Game engines: need *fast, temporary memory* (pools, frames)
* OS kernels: use *slab allocators*
* High-frequency trading systems: avoid dynamic allocation overhead
* Embedded systems: fixed-size preallocated memory

---

## ⚙️ 2️⃣ How `malloc()` and `free()` work (simplified)

The typical flow:

```
+------------------+
| malloc(size)     |
|  ↓               |
| request memory → kernel (via brk/mmap) |
|  ↓               |
| manage free list / heap blocks |
|  ↓               |
| return pointer    |
+------------------+
```

Internally, `malloc`:

* Splits and merges blocks
* Adds metadata headers
* Calls `sbrk()` or `mmap()` if more memory is needed

You can see this in action:

```bash
man brk
man mmap
```

---

## 🧩 3️⃣ The problem with default malloc

| Problem                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| **Overhead**              | Each malloc/free involves bookkeeping and possible system calls |
| **Fragmentation**         | Small allocations leave “holes” in memory                       |
| **Thread contention**     | `malloc()` locks internally for thread safety                   |
| **Unpredictable latency** | Large allocations may trigger kernel page allocation            |

---

## ⚙️ 4️⃣ When to use a custom allocator

| Situation                          | Recommended allocator |
| ---------------------------------- | --------------------- |
| Many small fixed-size objects      | Pool / slab allocator |
| Temporary objects (freed together) | Arena allocator       |
| Stack-like allocation pattern      | Stack allocator       |
| Variable lifetime objects          | Buddy allocator       |
| Tight memory limits (embedded)     | Static arena          |

---

## 🧠 5️⃣ Arena Allocator (linear / bump allocator)

Simplest custom allocator —
you allocate a big chunk once and then “bump” a pointer forward as you allocate.

No `free()`, just reset everything at once.

---

### Example:

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    char *base;
    size_t size;
    size_t offset;
} Arena;

Arena* arena_create(size_t size) {
    Arena *a = malloc(sizeof(Arena));
    a->base = malloc(size);
    a->size = size;
    a->offset = 0;
    return a;
}

void* arena_alloc(Arena *a, size_t bytes) {
    if (a->offset + bytes > a->size) return NULL;
    void *ptr = a->base + a->offset;
    a->offset += bytes;
    return ptr;
}

void arena_reset(Arena *a) {
    a->offset = 0;
}

void arena_free(Arena *a) {
    free(a->base);
    free(a);
}
```

---

### Usage:

```c
int main() {
    Arena *arena = arena_create(1024 * 1024); // 1 MB arena

    int *arr = arena_alloc(arena, 100 * sizeof(int));
    strcpy(arena_alloc(arena, 20), "Hello Arena!");

    printf("%s\n", (char*)(arena->base + sizeof(int) * 100));
    arena_reset(arena);  // reuse whole block instantly
    arena_free(arena);
}
```

✅ Super fast (just pointer arithmetic)
✅ No fragmentation
❌ No individual `free()` calls

---

## ⚙️ 6️⃣ Stack Allocator

Like arena, but supports **LIFO free order** (like a call stack).

```c
typedef struct {
    char *base;
    size_t offset;
    size_t size;
} StackAlloc;

void* stack_alloc(StackAlloc *s, size_t bytes) {
    void *ptr = s->base + s->offset;
    s->offset += bytes;
    return ptr;
}

void stack_free(StackAlloc *s, size_t mark) {
    s->offset = mark;
}
```

You take a “mark” before allocation:

```c
size_t mark = stack.offset;
Foo *f = stack_alloc(&stack, sizeof(Foo));
stack_free(&stack, mark);
```

✅ Perfect for nested temporary allocations (like recursive parsing or physics updates).

---

## 🧩 7️⃣ Pool Allocator (object pools)

Allocates fixed-size chunks from a preallocated block.
Each free slot is linked to the next free one.

---

### Example:

```c
typedef struct Block {
    struct Block *next;
} Block;

typedef struct {
    Block *free_list;
    void *memory;
    size_t block_size;
    size_t capacity;
} Pool;

Pool* pool_create(size_t block_size, size_t capacity) {
    Pool *p = malloc(sizeof(Pool));
    p->block_size = block_size;
    p->capacity = capacity;
    p->memory = malloc(block_size * capacity);

    p->free_list = p->memory;
    Block *curr = p->free_list;
    for (size_t i = 1; i < capacity; i++) {
        curr->next = (Block*)((char*)p->memory + i * block_size);
        curr = curr->next;
    }
    curr->next = NULL;
    return p;
}

void* pool_alloc(Pool *p) {
    if (!p->free_list) return NULL;
    Block *block = p->free_list;
    p->free_list = block->next;
    return block;
}

void pool_free(Pool *p, void *ptr) {
    Block *block = ptr;
    block->next = p->free_list;
    p->free_list = block;
}

void pool_destroy(Pool *p) {
    free(p->memory);
    free(p);
}
```

✅ Constant-time alloc/free
✅ No fragmentation
❌ Fixed-size only

Used in: **kernels, games, and real-time systems**.

---

## ⚙️ 8️⃣ Buddy Allocator

The **buddy allocator** is used in Linux kernel memory management.
It recursively divides memory blocks into halves (“buddies”).

Example:

```
1MB block → two 512KB → four 256KB → ...
```

When you free memory, it merges with its buddy if adjacent and same size.

✅ Balanced between flexibility and fragmentation.
❌ More complex to implement.

---

## 🧠 9️⃣ Slab Allocator (used in Linux kernel)

* Combination of **pools** and **caches**.
* Keeps pre-initialized objects (like file descriptors, inodes).
* Uses **object reuse** to minimize cache misses.

Functions like:

```c
kmem_cache_create()
kmem_cache_alloc()
kmem_cache_free()
```

You can mimic this in userspace for high-performance systems (databases, servers).

---

## ⚙️ 10️⃣ Region-based allocation (common in compilers)

Compilers and interpreters (like GCC or Python) use **region allocation**:

* Allocate nodes from a region (arena)
* Free the whole region when done (e.g., end of function or compilation unit)

✅ Perfect for structured, short-lived data.
❌ Memory persists until region reset.

---

## 🧩 11️⃣ Manual optimization techniques

Even with good allocators, **manual memory management and code tuning** matter:

| Technique                    | Description                                                   |
| ---------------------------- | ------------------------------------------------------------- |
| **Object reuse**             | Recycle objects instead of freeing/reallocating               |
| **Memory alignment**         | Use `posix_memalign()` or `aligned_alloc()` for SIMD or cache |
| **Cache-friendly data**      | Prefer arrays of structs (AoS) → structs of arrays (SoA)      |
| **Avoid heap fragmentation** | Group same-sized allocations                                  |
| **Batch allocations**        | Allocate arrays instead of many small objects                 |
| **Avoid false sharing**      | Don’t let threads share cache lines                           |

---

## ⚙️ 12️⃣ Alignment and cache optimization example

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
    int *data;
    posix_memalign((void**)&data, 64, 1024 * sizeof(int)); // 64-byte aligned
    for (int i = 0; i < 1024; i++) data[i] = i;
    printf("Aligned data at %p\n", (void*)data);
    free(data);
}
```

✅ Helps vectorized (SIMD) operations run faster due to cache alignment.

---

## 🧠 13️⃣ Measuring allocator performance

Use `time`, `perf`, or `valgrind --tool=massif`:

```bash
valgrind --tool=massif ./app
ms_print massif.out.*
```

Shows memory usage graph (heap growth, fragmentation, peaks).

---

## ⚙️ 14️⃣ Replace `malloc` globally (advanced)

You can define your own `malloc`/`free` in a shared object and preload it:

```c
#include <stdlib.h>
#include <stdio.h>

void* malloc(size_t size) {
    printf("Allocating %zu bytes\n", size);
    return __libc_malloc(size); // call real malloc
}
```

Compile:

```bash
gcc -fPIC -shared -o mymalloc.so malloc_hook.c -ldl
LD_PRELOAD=./mymalloc.so ./app
```

✅ Used by profilers and memory debuggers (like `jemalloc`, `tcmalloc`).

---

## 🧩 15️⃣ jemalloc, tcmalloc, and custom allocators in the wild

| Allocator           | Used by              | Features                         |
| ------------------- | -------------------- | -------------------------------- |
| **jemalloc**        | FreeBSD, Redis, Rust | Multithreaded, low fragmentation |
| **tcmalloc**        | Google Chrome        | Thread-caching fast paths        |
| **Hoard**           | Scientific computing | Scalable, NUMA-aware             |
| **Slab allocators** | Linux kernel         | Reusable, cache-efficient        |

✅ All provide better performance for specific workloads than glibc’s malloc.

---

## ⚙️ 16️⃣ Example: custom allocator for structs

```c
typedef struct {
    int id;
    float pos[3];
} Particle;

#define MAX_PARTICLES 100000

Particle pool[MAX_PARTICLES];
int free_index = 0;

Particle* alloc_particle() {
    if (free_index >= MAX_PARTICLES) return NULL;
    return &pool[free_index++];
}

void reset_particles() { free_index = 0; }
```

✅ O(1) allocation
✅ No `malloc`/`free` overhead
✅ Excellent for game loops or physics simulations

---

## 🧠 17️⃣ Manual optimization tips summary

| Goal                      | Technique                  |
| ------------------------- | -------------------------- |
| Reduce CPU stalls         | Align data to cache lines  |
| Improve locality          | Access memory sequentially |
| Reduce malloc overhead    | Use pools or arenas        |
| Speed up hot code         | Inline small functions     |
| Improve branch prediction | Simplify conditions        |
| Reduce cache misses       | Use SoA layout             |
| Avoid synchronization     | Use per-thread allocators  |

---

## ⚙️ 18️⃣ Example: Struct of Arrays (SoA) optimization

Instead of:

```c
typedef struct {
    float x, y, z;
} Vec3;
Vec3 points[1000];
```

Use:

```c
typedef struct {
    float x[1000];
    float y[1000];
    float z[1000];
} Vec3_SoA;
```

✅ Enables vectorized SIMD instructions.
✅ Improves cache hits.

Used heavily in:

* Game engines
* Physics simulations
* ML tensor libraries

---

## 🧩 19️⃣ When not to use custom allocators

❌ Small apps with low memory pressure
❌ Multi-threaded apps unless thread-safe
❌ When OS memory manager already performs well

✅ Use them only for *measured* bottlenecks.

---

## 🚀 20️⃣ Summary Table

| Allocator Type      | Use Case           | Free Strategy | Example            |
| ------------------- | ------------------ | ------------- | ------------------ |
| **Arena / Bump**    | Temporary memory   | All at once   | Compilers          |
| **Stack allocator** | LIFO allocations   | Mark/rollback | Recursive parsers  |
| **Pool allocator**  | Fixed-size objects | Individual    | Game engines       |
| **Buddy allocator** | Flexible memory    | Merge buddies | OS kernels         |
| **Slab allocator**  | Object reuse       | Cache reclaim | Linux kernel       |
| **Custom**          | Performance tuning | Custom        | jemalloc, tcmalloc |

---

## ⚡ Key takeaway

> The standard allocator (`malloc`) is *good*, but **you can do better** for specific workloads.
>
> Custom allocators are about **control** — over performance, fragmentation, and cache behavior.
>
> Combine this with profiling (`perf`, `cachegrind`) → you can push your program to *hardware-level efficiency*. ⚙️🚀

---
---

# 🧩 28️⃣ **Inline Functions & Macros for Performance**

---

## 🧠 1️⃣ Why we inline functions

Normally, when you call a function:

```c
int square(int x) { return x * x; }
int main() { return square(5); }
```

the compiler generates:

```
main:
    push 5
    call square
    add esp, 4
```

Function calls have overhead:

* Push arguments onto stack
* Jump to function
* Save/restore registers
* Return to caller

Inlining replaces the call **with the function body itself**.

```c
main:
    mov eax, 5
    imul eax, eax
    ret
```

✅ No call overhead, better instruction locality
❌ Larger binary (code bloat)

---

## ⚙️ 2️⃣ Inline functions — the modern, type-safe way

Defined using the `inline` keyword:

```c
inline int square(int x) { return x * x; }
```

Or in headers (for small utilities):

```c
static inline float lerp(float a, float b, float t) {
    return a + t * (b - a);
}
```

✅ Replaces function call with code
✅ Type-safe
✅ Obeys normal scoping and debugging rules

---

## 🧩 3️⃣ Inline function syntax rules

* Must be defined **in the same translation unit** (unless `extern inline`)
* Usually put in headers with `static inline`
* Don’t put large functions inline — compiler may inline automatically anyway

---

## ⚙️ 4️⃣ Example: manual inline vs function call

```c
#include <stdio.h>

inline int square_inline(int x) { return x * x; }
int square_normal(int x) { return x * x; }

int main() {
    int n = 1000000;
    volatile int sum = 0;
    for (int i = 0; i < n; i++)
        sum += square_inline(i);  // inlined
}
```

Compile with:

```bash
gcc -O3 -S -o - main.c | grep -A3 imul
```

✅ You’ll see **no `call` instruction**, only `imul` — it’s fully inlined.

---

## 🧠 5️⃣ When to use inline functions

| Use case                           | Good idea?        |
| ---------------------------------- | ----------------- |
| Small, frequently called functions | ✅ Yes             |
| Large, complex functions           | ❌ No (code bloat) |
| Simple math or accessor functions  | ✅ Excellent       |
| Recursive functions                | ❌ Impossible      |
| Performance-critical loops         | ✅ Often helps     |

---

## ⚙️ 6️⃣ When the compiler ignores `inline`

`inline` is a **hint**, not a command.
The compiler may ignore it if:

* The function is too large
* Optimizations are disabled (`-O0`)
* The function’s address is taken (`&func`)

Use `__attribute__((always_inline))` for forced inlining:

```c
inline __attribute__((always_inline)) int fastadd(int a, int b) {
    return a + b;
}
```

Or with MSVC:

```c
__forceinline int fastadd(int a, int b) { return a + b; }
```

---

## 🧩 7️⃣ Static inline in headers (the correct way)

To avoid multiple definition errors:

```c
// mathutils.h
#ifndef MATHUTILS_H
#define MATHUTILS_H

static inline float clamp(float x, float min, float max) {
    return x < min ? min : (x > max ? max : x);
}

#endif
```

✅ Each source file gets its own copy.
✅ Avoids linker conflicts.
✅ Standard way to inline small helpers in C libraries.

---

## ⚙️ 8️⃣ Inline with optimization flags

Inlining is automatically handled at higher optimization levels:

| Flag    | Behavior                       |
| ------- | ------------------------------ |
| `-O0`   | No inlining                    |
| `-O1`   | Basic inlining                 |
| `-O2`   | Aggressive heuristics          |
| `-O3`   | Loop unrolling + auto-inlining |
| `-flto` | Link-time cross-file inlining  |

You can force maximum inline expansion:

```bash
gcc -O3 -finline-functions -finline-limit=1000
```

---

## 🧠 9️⃣ Function-like macros

Before `inline` existed, C programmers used **macros** for “manual inlining”.

```c
#define SQUARE(x) ((x) * (x))
```

✅ Expands textually → no call overhead
❌ No type checking
❌ Multiple evaluation of arguments

---

### Example of macro hazard:

```c
#define SQUARE(x) ((x) * (x))
int a = 5;
int b = SQUARE(a++);  // expands to ((a++) * (a++))
```

✅ Result: undefined behavior (a incremented twice).

---

## ⚙️ 10️⃣ Macro best practices

Use parentheses around parameters and body:

```c
#define MAX(a,b) ((a) > (b) ? (a) : (b))
```

Use `do { ... } while (0)` for multi-statement macros:

```c
#define LOG(x) do { printf("DEBUG: %s\n", x); } while (0)
```

✅ Makes macro act like a single statement syntactically.

---

## 🧩 11️⃣ Example: inline vs macro comparison

```c
#define add_macro(a,b) ((a)+(b))
inline int add_func(int a, int b) { return a+b; }

int main() {
    int x = add_macro(1,2);
    int y = add_func(1,2);
}
```

Both expand to the same assembly at `-O2`.
✅ But `add_func()` has type checking and debugger visibility.
So:

> Always prefer `inline` functions unless you *need* macro tricks.

---

## ⚙️ 12️⃣ Macro advantages (when still useful)

✅ Compile-time conditional compilation:

```c
#ifdef DEBUG
#define LOG(x) printf("DEBUG: %s\n", x)
#else
#define LOG(x)
#endif
```

✅ Compile-time constants:

```c
#define KB(x) ((x) * 1024)
#define ALIGN16(x) (((x) + 15) & ~15)
```

✅ Branchless bit manipulations:

```c
#define IS_POW2(x) (!((x) & ((x)-1)))
```

---

## 🧠 13️⃣ Inline functions vs macros (summary)

| Feature            | Inline function  | Macro        |
| ------------------ | ---------------- | ------------ |
| Type-safe          | ✅                | ❌            |
| Evaluated once     | ✅                | ❌ (multiple) |
| Debuggable         | ✅                | ❌            |
| Compile-time logic | ❌                | ✅            |
| Constant folding   | ✅ (with `const`) | ✅            |
| Text substitution  | ❌                | ✅            |
| Risky              | No               | Yes 😬       |

✅ Use inline for performance.
✅ Use macros for compile-time logic or constants.

---

## ⚙️ 14️⃣ Constant folding & compiler optimization

Even without `inline`, compilers can eliminate function calls for simple functions with `-O2`:

```c
int square(int x) { return x*x; }
int main() { return square(5); }
```

Compiler replaces it with:

```
return 25;
```

✅ Known as **constant folding**.
✅ Happens automatically with optimization.

---

## 🧩 15️⃣ Inline assembly inside inline functions

You can mix inline assembly for ultimate control:

```c
inline int add_fast(int a, int b) {
    int res;
    __asm__("addl %2, %1"
            : "=r"(res)
            : "0"(a), "r"(b));
    return res;
}
```

✅ Inlined directly → no function call
✅ Hardware-optimized

Used in cryptography, compilers, and drivers.

---

## ⚙️ 16️⃣ Inline and branch prediction hints

Modern compilers let you guide prediction:

```c
#define likely(x)   __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)
```

Usage:

```c
if (likely(ptr != NULL))
    do_something();
else
    handle_error();
```

✅ Helps CPU’s branch predictor and instruction prefetcher.

---

## 🧠 17️⃣ Manual inlining trade-offs

| Advantage                      | Cost                          |
| ------------------------------ | ----------------------------- |
| Removes function call overhead | Increases code size           |
| Improves instruction locality  | May reduce cache efficiency   |
| Enables constant folding       | Longer compile times          |
| Useful for hot code paths      | Bad for rarely used functions |

Rule of thumb:

> Inline *small*, *pure*, *frequently called* functions.

---

## ⚙️ 18️⃣ Inline + LTO = cross-file optimization

With `-flto`, compiler can inline even across source files.

```bash
gcc -O3 -flto main.c utils.c -o app
```

✅ Functions in `utils.c` can be inlined into `main.c` automatically.
✅ The compiler effectively sees the *whole program*.

---

## 🧩 19️⃣ Advanced inline attributes (GCC/Clang)

| Attribute                        | Effect                                         |
| -------------------------------- | ---------------------------------------------- |
| `__attribute__((always_inline))` | Force inlining                                 |
| `__attribute__((noinline))`      | Prevent inlining                               |
| `__attribute__((hot))`           | Mark function as performance-critical          |
| `__attribute__((cold))`          | Mark as unlikely to run                        |
| `__attribute__((flatten))`       | Inline all function calls inside this function |

Example:

```c
__attribute__((hot, always_inline))
inline int fastmul(int a, int b) { return a * b; }
```

---

## ⚙️ 20️⃣ Summary Table

| Feature                     | Keyword                          | Effect                             |
| --------------------------- | -------------------------------- | ---------------------------------- |
| **Inline function**         | `inline`                         | Replace function calls with body   |
| **Forced inline**           | `__attribute__((always_inline))` | Guarantee inlining                 |
| **Macro**                   | `#define`                        | Text replacement, no type checking |
| **Branch prediction hint**  | `__builtin_expect`               | Optimize CPU branch predictor      |
| **Prevent inlining**        | `__attribute__((noinline))`      | Keep call                          |
| **Cross-file optimization** | `-flto`                          | Whole-program inlining             |
| **Safe inline in headers**  | `static inline`                  | Avoid duplicate symbols            |

---

## ⚡ Key takeaway

> Use **`inline` functions** for small, hot code paths that are called often.
> Use **macros** only for constants, compile-time logic, or low-level tricks.
> Let the **compiler’s optimizer (`-O2`, `-O3`, `-flto`)** handle the rest —
> it knows better than you most of the time 😉

With inlining, macros, and compiler guidance,
you’re now working at the **machine-instruction level** — making your C code *as fast as hand-written assembly* ⚙️🔥

---
---

# 🧩 29️⃣ **Portability & Standards (C89 → C23)**

---

## 🧠 1️⃣ What “portability” means in C

> Portability = your program compiles and runs the same way
> on **different compilers, operating systems, or hardware architectures**.

Examples:

* From GCC → Clang → MSVC
* From Linux → macOS → Windows → Embedded ARM
* From x86 → ARM → RISC-V

C’s power is **close-to-hardware** — but that also means it’s full of *platform-dependent traps*.

---

## ⚙️ 2️⃣ What are “C standards”?

C was standardized by **ANSI (American National Standards Institute)** and later **ISO**.

Each standard defines:

* Syntax and semantics
* Standard library behavior
* Undefined / implementation-defined areas

Versions:

| Standard         | Year        | Common name   | Compiler flag |
| ---------------- | ----------- | ------------- | ------------- |
| ANSI C / ISO C90 | 1989 / 1990 | **C89 / C90** | `-std=c90`    |
| C99              | 1999        | **C99**       | `-std=c99`    |
| C11              | 2011        | **C11**       | `-std=c11`    |
| C17              | 2018        | **C17**       | `-std=c17`    |
| C23              | 2023        | **C23**       | `-std=c23`    |

---

## 🧩 3️⃣ C89 / C90 — “Classic C”

📅 **Released:** 1989 (ANSI), ratified as ISO C90
🔹 First official C standard.

### Key features:

* Function prototypes (`int f(int x)`)
* `void` keyword
* `const`, `volatile`
* Standard headers (`<stdio.h>`, `<stdlib.h>`, etc.)
* Single-line comments **not allowed** (`//`)
* Variable declarations **must be at start of block**

### Example:

```c
int main(void) {
    int i;           // must declare before use
    for (i = 0; i < 10; i++)
        printf("%d\n", i);
    return 0;
}
```

✅ Supported everywhere — still used for **embedded systems**.
❌ No flexible arrays, `inline`, or `stdint.h`.

---

## ⚙️ 4️⃣ C99 — the modernization wave 🌊

📅 **Released:** 1999
Goal: bring C closer to what real programmers were already doing.

### ✅ Major new features:

* **Single-line comments:** `// like C++`
* **Mixed declarations and code:**

  ```c
  for (int i = 0; i < 10; i++) ...
  ```
* **`long long int`** (64-bit integers)
* **`_Bool`**, `bool` (`<stdbool.h>`)
* **`inline` functions**
* **Variable-length arrays (VLA)**

  ```c
  int n = 5;
  int arr[n];
  ```
* **`restrict`** keyword (pointer alias optimization)
* **`snprintf()`**, `vsnprintf()` (safe string functions)
* **`stdint.h`** → fixed-width integers (`int32_t`, `uint64_t`)
* **Designated initializers:**

  ```c
  struct point p = {.x = 1, .y = 2};
  ```
* **Compound literals:**

  ```c
  int *p = (int[]){1, 2, 3};
  ```

✅ Big leap in expressiveness and safety.
❌ Some features (like VLAs) were controversial in embedded systems.

---

## 🧠 5️⃣ C11 — safety, concurrency, and atomics ⚙️

📅 **Released:** 2011
Focus: **multithreading**, **atomic ops**, and **runtime safety**.

### ✅ New features:

* `_Thread_local` storage class
* `<threads.h>` → portable threading API

  ```c
  thrd_t t;
  thrd_create(&t, func, arg);
  ```
* `<stdatomic.h>` → lock-free atomics

  ```c
  atomic_int x = 0;
  atomic_fetch_add(&x, 1);
  ```
* `<stdnoreturn.h>`, `_Noreturn`
* `_Static_assert`
* Optional **bounds-checking library** (`<stdbit.h>`, `<uchar.h>`)
* Improved Unicode support: `char16_t`, `char32_t`

✅ Brought C into the multithreaded era.
❌ `<threads.h>` rarely implemented fully until GCC 12+.

---

## ⚙️ 6️⃣ C17 — “bugfix release”

📅 **Released:** 2018
👉 No new features — just clarifications and defect fixes from C11.

Think of it like:

```
C11 + errata = C17
```

✅ Safe baseline for modern C projects.
✅ All modern compilers support it.

---

## 🧠 7️⃣ C23 — the new generation ⚡

📅 **Released:** December 2023
Goal: Modernize C syntax & usability while keeping compatibility.

### ✅ Major new features:

#### 🔹 1. Type inference (`auto`)

```c
auto x = 42;     // int
auto y = 3.14;   // double
```

#### 🔹 2. `nullptr`

```c
int *p = nullptr;   // safer than NULL
```

#### 🔹 3. `typeof` & `decltype`

```c
typeof(x) y = 123;      // type of x
decltype(3.14) z = 0.0; // double
```

#### 🔹 4. Improved function declarations

```c
[[nodiscard]] int foo(void);
[[deprecated]] void old_func();
```

#### 🔹 5. UTF-8 character type

```c
char8_t *s = u8"Hello";
```

#### 🔹 6. `constexpr`-like constants

```c
constexpr int N = 100;
```

#### 🔹 7. Standardized attributes (`[[nodiscard]]`, `[[maybe_unused]]`, `[[deprecated]]`)

#### 🔹 8. Safer syntax improvements

* Implicit `int` is banned
* Implicit function declarations banned
* Boolean literals: `true`/`false` standardized

---

✅ C23 is **modern, expressive, and safer**
❌ Still fresh — not all compilers fully support it yet (as of GCC 14/Clang 17).

---

## ⚙️ 8️⃣ Compiler flags for standard versions

| Standard       | GCC/Clang flag     |
| -------------- | ------------------ |
| C89 / C90      | `-std=c90`         |
| C99            | `-std=c99`         |
| C11            | `-std=c11`         |
| C17            | `-std=c17`         |
| C23            | `-std=c23`         |
| GNU extensions | `-std=gnu99`, etc. |

Example:

```bash
gcc -std=c99 -Wall -Wextra -pedantic main.c -o app
```

✅ Use `-pedantic` to enforce standard compliance.

---

## 🧠 9️⃣ Portability categories

| Category                 | Description                          | Example issue                               |
| ------------------------ | ------------------------------------ | ------------------------------------------- |
| **Source portability**   | Code compiles on any compiler        | Use standard headers only                   |
| **Binary portability**   | Compiled binary runs on any platform | Rare in C (depends on ABI)                  |
| **Behavior portability** | Code behaves identically everywhere  | Avoid UB, rely on standard-defined behavior |

---

## ⚙️ 10️⃣ Common portability pitfalls

| Issue                  | Explanation                            | Fix                                             |
| ---------------------- | -------------------------------------- | ----------------------------------------------- |
| **Endianness**         | Byte order differs (x86=LE, ARM=BE/LE) | Use `<endian.h>` or convert manually            |
| **Word size**          | `long` = 4 bytes on Win64, 8 on Linux  | Use `int32_t`, `int64_t`                        |
| **Struct padding**     | Different compilers align differently  | Use `#pragma pack` or `__attribute__((packed))` |
| **File paths**         | `\` vs `/`                             | Use `/` or abstraction                          |
| **Text encoding**      | ASCII vs UTF-8 vs UTF-16               | Use `char8_t`, locale APIs                      |
| **Undefined behavior** | Compilers optimize differently         | Avoid UB!                                       |
| **Threading model**    | POSIX vs Win32                         | Use `<threads.h>` or abstraction layer          |

---

## 🧩 11️⃣ Endianness check example

```c
#include <stdint.h>
#include <stdio.h>

int main() {
    uint16_t x = 0x1;
    char *c = (char*)&x;
    printf("%s-endian\n", *c ? "Little" : "Big");
}
```

✅ Prints `"Little-endian"` on x86.

---

## ⚙️ 12️⃣ Integer size differences

| Type        | 32-bit Linux | 64-bit Linux | Windows x64 |
| ----------- | ------------ | ------------ | ----------- |
| `int`       | 4            | 4            | 4           |
| `long`      | 4            | 8            | 4           |
| `long long` | 8            | 8            | 8           |
| `void*`     | 4            | 8            | 8           |

✅ Always use `<stdint.h>` types for precise sizes.

---

## 🧠 13️⃣ Avoiding undefined behavior (UB)

Common portability killers:

| UB                                | Example                         |
| --------------------------------- | ------------------------------- |
| Signed integer overflow           | `int x = INT_MAX + 1;`          |
| Shifting by width or more         | `x << 32`                       |
| Modifying & reading same variable | `i = i++;`                      |
| Using uninitialized memory        | `int x; printf("%d", x);`       |
| Accessing out-of-bounds           | `arr[10] = 0;`                  |
| Violating aliasing rules          | Type-punning structs improperly |

✅ Compilers assume UB “never happens”, so they *optimize it away*.

---

## ⚙️ 14️⃣ Platform abstraction macros

```c
#ifdef _WIN32
    #define PATH_SEP '\\'
#else
    #define PATH_SEP '/'
#endif
```

✅ Write once, compile anywhere.

---

## 🧩 15️⃣ Portability helpers (standard headers)

| Header            | Purpose                   |
| ----------------- | ------------------------- |
| `<stdint.h>`      | Fixed-width integer types |
| `<inttypes.h>`    | Format macros (`PRId64`)  |
| `<stdbool.h>`     | `bool`, `true`, `false`   |
| `<stdalign.h>`    | Alignment control         |
| `<threads.h>`     | Portable threads          |
| `<uchar.h>`       | Unicode characters        |
| `<stdnoreturn.h>` | Non-returning functions   |

---

## ⚙️ 16️⃣ Locale and encoding portability

Different platforms use different default encodings:

* Linux → UTF-8
* Windows → UTF-16 (wide chars)

Use:

```c
setlocale(LC_ALL, "");
```

Or explicit Unicode APIs (`char16_t`, `char32_t`, `wchar_t`).

---

## 🧠 17️⃣ Compiler feature detection

Check supported features:

```c
#if __STDC_VERSION__ >= 201112L
    // C11 or newer
#endif
```

### `__STDC_VERSION__` values:

| Version | Macro     |
| ------- | --------- |
| C90     | undefined |
| C99     | `199901L` |
| C11     | `201112L` |
| C17     | `201710L` |
| C23     | `202311L` |

---

## ⚙️ 18️⃣ Modern best practices for portability

✅ Use `-std=c17` or `-std=c23` for new projects
✅ Avoid compiler extensions unless guarded by macros
✅ Always include `<stdint.h>`
✅ Use feature macros for conditional compilation
✅ Avoid undefined or implementation-defined behavior
✅ Build with multiple compilers (GCC, Clang, MSVC)

---

## 🧩 19️⃣ Real-world portable code example

```c
#include <stdio.h>
#include <stdint.h>
#include <threads.h>

int main(void) {
#if __STDC_VERSION__ >= 201112L
    printf("C standard: %ld\n", __STDC_VERSION__);
#endif
    printf("int32_t size = %zu\n", sizeof(int32_t));
    return 0;
}
```

✅ Compiles under GCC, Clang, and MSVC with identical output.

---

## 🚀 20️⃣ Summary Table

| Standard      | Year | Highlights                         | Notes                                  |
| ------------- | ---- | ---------------------------------- | -------------------------------------- |
| **C89 / C90** | 1989 | Prototypes, `void`, standard libs  | Baseline for embedded                  |
| **C99**       | 1999 | `//`, `bool`, `inline`, `stdint.h` | Big modernization                      |
| **C11**       | 2011 | Threads, atomics, Unicode          | Concurrency support                    |
| **C17**       | 2018 | C11 + bugfixes                     | Stable, mainstream                     |
| **C23**       | 2023 | `auto`, `nullptr`, attributes      | Modern, safer, not fully supported yet |

---

## ⚡ Key takeaway

> C’s greatest strength is *portability across decades and devices.*
>
> Follow the standards, avoid undefined behavior, use fixed-width types,
> and your code will compile on **everything from a Raspberry Pi to a supercomputer** —
> even 30 years from now 🧠⚙️

---
---

# 🧩 30️⃣ **Writing Libraries & Defensive Programming**

---

## 🧠 1️⃣ What is a library?

A **C library** is a **collection of reusable functions and types** that can be linked into other programs.

It can be:

* **Static Library** (`.a`) → copied into the program binary at link time
* **Shared Library** (`.so`) → loaded at runtime (via `dlopen()` or the loader)

---

### Example project layout:

```
mathlib/
├── include/
│   └── mathlib.h
├── src/
│   └── mathlib.c
├── build/
│   └── libmathlib.a  (or libmathlib.so)
└── tests/
    └── test_math.c
```

---

## ⚙️ 2️⃣ Header file design (API surface)

Your header (`.h`) defines:

* What the **user sees** (public API)
* Data types, constants, macros
* Function prototypes
* Documentation comments

Example — `mathlib.h`

```c
#ifndef MATHLIB_H
#define MATHLIB_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>

/* Adds two numbers. Returns their sum. */
int add(int a, int b);

/* Calculates factorial of n (n >= 0). 
 * Returns -1 on overflow.
 */
int factorial(int n);

#ifdef __cplusplus
}
#endif

#endif // MATHLIB_H
```

✅ Includes guards
✅ Works in both C and C++
✅ Provides documentation comments
✅ No internal implementation details

---

## 🧩 3️⃣ Implementation file (private logic)

Your `.c` file implements the API — and may have private helper functions.

`mathlib.c`

```c
#include "mathlib.h"
#include <limits.h>

int add(int a, int b) {
    return a + b;
}

int factorial(int n) {
    if (n < 0) return -1;
    int res = 1;
    for (int i = 2; i <= n; i++) {
        if (res > INT_MAX / i)
            return -1;  // overflow check
        res *= i;
    }
    return res;
}
```

✅ No global variables
✅ Checks for errors
✅ Does not depend on `main()`

---

## ⚙️ 4️⃣ Compiling into a library

### Static:

```bash
gcc -c src/mathlib.c -Iinclude -o build/mathlib.o
ar rcs build/libmathlib.a build/mathlib.o
```

### Shared:

```bash
gcc -fPIC -shared src/mathlib.c -Iinclude -o build/libmathlib.so
```

---

## 🧠 5️⃣ Using your library

### Link it to another program:

`main.c`

```c
#include "mathlib.h"
#include <stdio.h>

int main() {
    printf("5! = %d\n", factorial(5));
}
```

### Compile:

```bash
gcc main.c -Lbuild -lmathlib -Iinclude -o app
export LD_LIBRARY_PATH=build:$LD_LIBRARY_PATH
./app
```

✅ Clean separation between *API* and *implementation*.

---

# ⚙️ 6️⃣ Defensive programming — mindset shift

> “Code not for the happy path — code for the idiot path.” 😅

Defensive programming means writing C code that:

* Checks every input
* Handles every error
* Fails safely instead of silently corrupting memory

---

## 🧩 7️⃣ The 4 principles of defensive programming

| Principle              | Description                          |
| ---------------------- | ------------------------------------ |
| **Validate input**     | Never trust user or caller           |
| **Handle all errors**  | Every function must report failure   |
| **Limit side effects** | Avoid hidden global state            |
| **Fail gracefully**    | Never crash, corrupt, or leak memory |

---

## ⚙️ 8️⃣ Input validation examples

```c
int divide(int a, int b, int *result) {
    if (!result) return -1;     // invalid pointer
    if (b == 0) return -2;      // divide by zero
    *result = a / b;
    return 0;                   // success
}
```

✅ Prevents null dereference, division by zero, and provides error codes.

---

## 🧠 9️⃣ Error handling strategies

### 1. **Return codes (traditional C)**

```c
#define SUCCESS 0
#define ERR_INVALID -1
#define ERR_OVERFLOW -2
```

Simple and portable.

---

### 2. **Global error state**

```c
errno = EINVAL;
```

Used by POSIX APIs — but **not thread-safe** unless handled carefully.

---

### 3. **Out parameters**

```c
int read_file(const char *path, char **out_data);
```

✅ Keeps function return code reserved for success/failure.

---

## ⚙️ 10️⃣ Asserting invariants

Assertions verify assumptions during development:

```c
#include <assert.h>

int factorial(int n) {
    assert(n >= 0);   // development check
    ...
}
```

✅ Catches programmer errors during testing
❌ Don’t rely on asserts for production checks

Compile with:

* `-DNDEBUG` → disables assertions in release builds.

---

## 🧠 11️⃣ Resource safety — avoid leaks & dangling pointers

Always follow:

```c
resource = acquire();
if (!resource) return ERR_NO_MEM;

... use resource ...

release(resource);
```

And never “free twice”:

```c
free(ptr);
ptr = NULL;
```

✅ Set pointer to `NULL` after freeing to prevent double free.

---

## ⚙️ 12️⃣ Encapsulation — hide internal details

Never expose internal structures in headers.

Bad:

```c
typedef struct {
    int count;
    char *data;
} List;
```

Good:

```c
typedef struct List List;   // opaque type

List* list_create(void);
void list_add(List *l, const char *item);
void list_destroy(List *l);
```

✅ Allows internal redesign without breaking API.
✅ Protects users from accessing internal data.

---

## 🧩 13️⃣ Versioned and defensive APIs

Version your library and expose it clearly:

```c
#define MATHLIB_VERSION_MAJOR 1
#define MATHLIB_VERSION_MINOR 2
#define MATHLIB_VERSION_PATCH 0
```

Expose:

```c
const char* mathlib_version(void);
```

✅ Prevents linking mismatches
✅ Helps backward compatibility

---

## ⚙️ 14️⃣ Error resilience with fallback mechanisms

Example:

```c
FILE *fp = fopen("config.txt", "r");
if (!fp) {
    fprintf(stderr, "Warning: using defaults\n");
    use_default_config();
}
```

✅ Don’t crash on missing files — fail safely.

---

## 🧠 15️⃣ Thread safety

* Avoid **global mutable state**
* Use **mutexes** or **thread-local storage** when necessary
* Mark shared data `volatile` or `atomic`
* Reentrant APIs return state via parameters, not statics

✅ Example of reentrancy:

```c
int random_next(unsigned *state) {
    *state = (*state * 1103515245 + 12345) % (1u << 31);
    return *state;
}
```

---

## ⚙️ 16️⃣ Defensive memory allocation pattern

Always check `malloc()` return:

```c
char *buf = malloc(size);
if (!buf) {
    fprintf(stderr, "Out of memory\n");
    return ERR_NOMEM;
}
```

Prefer wrapper functions:

```c
void* xmalloc(size_t size) {
    void *p = malloc(size);
    if (!p) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    return p;
}
```

✅ Ensures consistent failure handling across project.

---

## 🧩 17️⃣ Function contracts (documented expectations)

Clearly define:

* What inputs are valid
* What outputs are guaranteed
* When errors are returned

Example in header:

```c
/* 
 * Computes average of array.
 * 
 * @param arr: pointer to array of length n (must not be NULL)
 * @param n: number of elements (must be > 0)
 * @return average value, or 0.0 if input invalid
 */
double average(const double *arr, size_t n);
```

---

## ⚙️ 18️⃣ Library testing — “defense by verification”

Write a dedicated test suite:

```c
#include "mathlib.h"
#include <assert.h>

int main() {
    assert(add(2, 3) == 5);
    assert(factorial(0) == 1);
    assert(factorial(-1) == -1);
    return 0;
}
```

Automate with `make test`, `CTest`, or `Check` (C unit test framework).

✅ Catches regressions before users do.

---

## 🧠 19️⃣ Compile defensively

Use strict compiler flags:

```bash
gcc -Wall -Wextra -Wpedantic -Werror -O2 -std=c17
```

Optionally:

```bash
-fstack-protector-strong -D_FORTIFY_SOURCE=2 -fsanitize=address,undefined
```

✅ Detects buffer overflows, memory leaks, and undefined behavior early.

---

## ⚙️ 20️⃣ Checklist for writing professional-grade C libraries

| Category           | Checklist                                        |
| ------------------ | ------------------------------------------------ |
| **API Design**     | Clear naming, consistent style, opaque types     |
| **Safety**         | Validate all inputs, handle NULLs, bounds check  |
| **Memory**         | No leaks, no double frees, predictable ownership |
| **Error Handling** | Uniform return codes, no silent failures         |
| **Thread Safety**  | Avoid globals, reentrant functions               |
| **Portability**    | Use standard C, test across compilers            |
| **Documentation**  | Comments, README, header docstrings              |
| **Testing**        | Automated unit tests, assertions                 |
| **Build**          | Makefile or CMake, static/shared builds          |
| **Versioning**     | Semantic version macros                          |

---

## 🚀 Example: Minimal Portable Library Template

```
myutils/
├── include/
│   └── myutils.h
├── src/
│   └── myutils.c
├── tests/
│   └── test_myutils.c
├── Makefile
└── README.md
```

**Makefile**

```make
CC = gcc
CFLAGS = -Wall -Wextra -std=c17 -Iinclude
OBJ = src/myutils.o
TARGET = libmyutils.a

$(TARGET): $(OBJ)
	ar rcs $@ $^

test: $(TARGET)
	gcc tests/test_myutils.c -L. -lmyutils -Iinclude -o test && ./test

clean:
	rm -f $(OBJ) $(TARGET) test
```

✅ Fully portable
✅ Supports unit tests
✅ Ready for static or shared linking

---

## ⚡ Key takeaway

> Great C libraries are not just *fast* — they are **safe, predictable, portable, and self-defensive**.
>
> Your code should handle misuse, memory failure, and bad inputs **gracefully**,
> because your library will outlive you — and it deserves to. 🧠

---
---

# 🧩 31️⃣ **Unit Testing Frameworks in C**

---

## 🧠 1️⃣ What is unit testing?

> Unit testing = testing small, isolated pieces (“units”) of your code
> — usually **one function** or **module** — automatically.

Each test checks one behavior or condition.
If all tests pass, your library still behaves as intended.
If any test fails, you know *exactly what broke* and *where*.

---

## ⚙️ 2️⃣ Why testing is vital in C

Unlike high-level languages (Python, Rust), C gives you:

* **Manual memory control**
* **No exceptions**
* **Undefined behavior**
* **No type safety beyond compiler**

So testing is your *first and last line of defense*.

Unit tests catch:

* Memory leaks
* Logic errors
* Regression bugs after refactors
* API misuse
* Undefined behavior due to edge cases

---

## 🧩 3️⃣ The anatomy of a unit test

A unit test typically has:

| Step             | Example                           |
| ---------------- | --------------------------------- |
| **1. Setup**     | Initialize test data or state     |
| **2. Action**    | Call function under test          |
| **3. Assertion** | Compare actual vs expected result |
| **4. Teardown**  | Free memory, cleanup              |

Example (manual style):

```c
#include "mathlib.h"
#include <assert.h>

int main(void) {
    assert(add(2, 3) == 5);
    assert(factorial(0) == 1);
    assert(factorial(-1) == -1);
    return 0;
}
```

✅ Simple but no reporting or grouping.
❌ No summary, no skipping, no setup/teardown automation.

That’s where **testing frameworks** come in.

---

# ⚙️ 4️⃣ Popular Unit Testing Frameworks for C

| Framework     | Highlights                          | Suitable for                  |
| ------------- | ----------------------------------- | ----------------------------- |
| **Check**     | POSIX-friendly, mature, XML reports | Linux / CI systems            |
| **Unity**     | Lightweight, embedded-friendly      | Microcontrollers              |
| **cmocka**    | Mocking + assertions, simple setup  | Modern C projects             |
| **Criterion** | Auto-discovery, multithreaded tests | Desktop / performance testing |

---

# 🧩 5️⃣ Framework 1: **Check**

📦 Install:

```bash
sudo apt install check
```

### Example — `test_math.c`

```c
#include <check.h>
#include "mathlib.h"

START_TEST(test_addition)
{
    ck_assert_int_eq(add(2, 3), 5);
    ck_assert_int_ne(add(2, 2), 5);
}
END_TEST

START_TEST(test_factorial)
{
    ck_assert_int_eq(factorial(0), 1);
    ck_assert_int_eq(factorial(5), 120);
    ck_assert_int_eq(factorial(-3), -1);
}
END_TEST

Suite* math_suite(void)
{
    Suite *s = suite_create("MathLib");
    TCase *tc = tcase_create("Core");

    tcase_add_test(tc, test_addition);
    tcase_add_test(tc, test_factorial);
    suite_add_tcase(s, tc);
    return s;
}

int main(void)
{
    int number_failed;
    Suite *s = math_suite();
    SRunner *sr = srunner_create(s);
    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? 0 : 1;
}
```

Compile:

```bash
gcc test_math.c src/mathlib.c -Iinclude -lcheck -o test_math
./test_math
```

Output:

```
Running suite(s): MathLib
100%: Checks: 2, Failures: 0
```

✅ Clear results
✅ Easy to add more test cases
✅ Can output XML for CI tools

---

# ⚙️ 6️⃣ Framework 2: **Unity**

💡 Extremely small and self-contained — perfect for embedded, IoT, or C-only builds.

📦 Get it:
[https://github.com/ThrowTheSwitch/Unity](https://github.com/ThrowTheSwitch/Unity)

---

### Example — `test_math_unity.c`

```c
#include "unity.h"
#include "mathlib.h"

void setUp(void) {}
void tearDown(void) {}

void test_addition(void) {
    TEST_ASSERT_EQUAL_INT(5, add(2, 3));
}

void test_factorial(void) {
    TEST_ASSERT_EQUAL_INT(1, factorial(0));
    TEST_ASSERT_EQUAL_INT(-1, factorial(-1));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_addition);
    RUN_TEST(test_factorial);
    return UNITY_END();
}
```

Compile:

```bash
gcc test_math_unity.c src/mathlib.c unity.c -Iinclude -o test_math_unity
./test_math_unity
```

Output:

```
test_math_unity.c: test_addition: PASS
test_math_unity.c: test_factorial: PASS
-----------------------
2 Tests 0 Failures
OK
```

✅ Minimal dependencies
✅ Portable (works even on microcontrollers)

---

# 🧩 7️⃣ Framework 3: **cmocka**

🧩 Lightweight, modern, supports **mocking** and **assertions**.

📦 Install:

```bash
sudo apt install cmocka
```

---

### Example — `test_math_cmocka.c`

```c
#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>
#include "mathlib.h"

static void test_add(void **state) {
    (void)state;
    assert_int_equal(add(2, 3), 5);
}

static void test_factorial(void **state) {
    (void)state;
    assert_int_equal(factorial(5), 120);
    assert_int_equal(factorial(-1), -1);
}

int main(void) {
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_add),
        cmocka_unit_test(test_factorial),
    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
```

Compile:

```bash
gcc test_math_cmocka.c src/mathlib.c -Iinclude -lcmocka -o test_math_cmocka
./test_math_cmocka
```

Output:

```
[==========] Running 2 test(s).
[ RUN      ] test_add
[       OK ] test_add
[ RUN      ] test_factorial
[       OK ] test_factorial
[==========] 2 test(s) run.
[  PASSED  ] 2 test(s).
```

✅ Very readable
✅ Good for CI and mocking system calls
✅ Has per-group setup/teardown

---

# ⚙️ 8️⃣ Framework 4: **Criterion**

💎 Modern C testing framework with **auto test discovery**, **parallel execution**, and **color output**.
Perfect for larger desktop projects.

📦 Install:

```bash
sudo apt install libcriterion-dev
```

---

### Example — `test_math_criterion.c`

```c
#include <criterion/criterion.h>
#include "mathlib.h"

Test(math, addition) {
    cr_assert_eq(add(2, 3), 5);
}

Test(math, factorial) {
    cr_assert_eq(factorial(5), 120);
    cr_assert_eq(factorial(-1), -1);
}
```

Compile:

```bash
gcc test_math_criterion.c src/mathlib.c -Iinclude -lcriterion -o test_math_criterion
./test_math_criterion
```

Output:

```
[====] Running 2 tests
[PASS] math::addition
[PASS] math::factorial
[====] Summary: All tests passed
```

✅ Auto-detects tests
✅ Thread-safe
✅ Works great with CI (GitHub Actions, GitLab CI)

---

# 🧠 9️⃣ Assertions (common across frameworks)

| Assertion                           | Meaning                   |
| ----------------------------------- | ------------------------- |
| `assert_true(expr)`                 | Expression should be true |
| `assert_false(expr)`                | Should be false           |
| `assert_int_equal(a, b)`            | Integers equal            |
| `assert_float_equal(a, b, epsilon)` | Floats within tolerance   |
| `assert_non_null(ptr)`              | Pointer not NULL          |
| `assert_string_equal(a, b)`         | Strings equal             |
| `assert_memory_equal(a, b, len)`    | Compare byte arrays       |

✅ Assertions crash the test *only for that case* — rest continue.

---

# ⚙️ 10️⃣ Organizing tests

Recommended structure:

```
project/
├── include/
├── src/
├── tests/
│   ├── test_math.c
│   ├── test_io.c
│   └── Makefile
```

Makefile:

```make
CC=gcc
CFLAGS=-Wall -Wextra -std=c17 -I../include
LIBS=-lcheck

tests: test_math

test_math: test_math.c ../src/mathlib.c
	$(CC) $(CFLAGS) $^ -o $@ $(LIBS)

run:
	./test_math
```

✅ One test file per module.
✅ Build + run with `make run`.

---

# 🧩 11️⃣ Integrating with CI/CD (automation)

You can run tests automatically using:

* **GitHub Actions**
* **GitLab CI**
* **Make + Jenkins**
* **CTest (CMake)**

Example GitHub Action snippet:

```yaml
- name: Run Unit Tests
  run: |
    make
    make test
```

✅ Ensures every commit passes all tests.

---

# ⚙️ 12️⃣ Memory testing in tests

Combine with Valgrind:

```bash
valgrind --leak-check=full ./test_math
```

✅ Ensures no leaks, invalid reads/writes, or double frees.

---

# 🧠 13️⃣ Mocking dependencies

Some frameworks (like `cmocka`) allow mocking:

```c
will_return(__wrap_fopen, NULL);
expect_function_call(__wrap_fprintf);
```

✅ Lets you test error paths like “file open failed” without real files.

---

# ⚙️ 14️⃣ Code coverage integration

To measure how much code your tests execute:

```bash
gcc -fprofile-arcs -ftest-coverage main.c -o app
./app
gcov main.c
```

Or use:

```bash
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory out
```

✅ Produces HTML coverage reports.

---

# 🧩 15️⃣ Testing philosophy

> “If you can’t test it, you don’t understand it.”

Guidelines:

* One test per behavior
* Name tests clearly (`test_factorial_negative`)
* Don’t mix many checks in one test
* Write tests *before* refactoring
* Run tests *after every commit*

---

# 🚀 16️⃣ Summary Table

| Framework     | Pros                              | Ideal for              |
| ------------- | --------------------------------- | ---------------------- |
| **Check**     | Mature, POSIX, CI-friendly        | Linux development      |
| **Unity**     | Tiny, header-only                 | Embedded / bare-metal  |
| **cmocka**    | Mocking, clean syntax             | Modern portable libs   |
| **Criterion** | Auto-discovery, colored, parallel | Desktop / CI pipelines |

---

# 🧠 17️⃣ Defensive Testing Checklist

| Category          | Best Practice                             |
| ----------------- | ----------------------------------------- |
| **Isolation**     | Test one function at a time               |
| **Repeatability** | No external dependencies                  |
| **Error paths**   | Test invalid inputs, not just happy cases |
| **Resources**     | Run under Valgrind                        |
| **Performance**   | Add benchmarks if needed                  |
| **Automation**    | Run in CI/CD on every push                |

---

# ⚡ Key takeaway

> Testing in C is not optional — it’s *how you prove your code is correct, safe, and maintainable.*
>
> Once you integrate unit tests into your build system, your C codebase becomes self-verifying:
> every future change either **proves** correctness or **exposes** regressions instantly. 🧠✅

---
---
