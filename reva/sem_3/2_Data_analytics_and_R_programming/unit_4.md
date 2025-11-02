# Unit - 4

## Basic of R and Statistics using R
- Basic Math
- Variables
- Data Types
- Vectors
- Calling Functions
- Function Documentation
- Missing Data
- Advanced Data Structures:- DataFrame, Lists, matrices, Arrays
- Reading Data into R: Reading CSVs, Excel Data
- Reading from Databases
- Statistical Graphics - Visulization

- Basic Statistics: Summary Statistics
- Correlation and Covariance
- T-Tests
- ANOVA
- Linear Models: Simple Linear Regression
- Multiple Linear Regression
- Logistic Regression

---
---

# 🧮 **Basic Math in R**

R is primarily designed for **statistical and numerical computing**, so it can easily perform **basic arithmetic**, **mathematical functions**, and **vectorized operations**.

---

### 🔹 **1. Arithmetic Operations**

R supports all basic arithmetic operators:

| Operator    | Description         | Example    | Output |
| ----------- | ------------------- | ---------- | ------ |
| `+`         | Addition            | `3 + 5`    | `8`    |
| `-`         | Subtraction         | `10 - 4`   | `6`    |
| `*`         | Multiplication      | `6 * 7`    | `42`   |
| `/`         | Division            | `15 / 3`   | `5`    |
| `^` or `**` | Exponentiation      | `2 ^ 4`    | `16`   |
| `%%`        | Modulus (remainder) | `10 %% 3`  | `1`    |
| `%/%`       | Integer division    | `10 %/% 3` | `3`    |

✅ **Example in R Console:**

```R
> 4 + 3 * 2
[1] 10
> (4 + 3) * 2
[1] 14
> 17 %% 5
[1] 2
```

---

### 🔹 **2. Mathematical Functions**

R provides built-in functions for common mathematical operations:

| Function      | Description               | Example             | Output     |
| ------------- | ------------------------- | ------------------- | ---------- |
| `sqrt(x)`     | Square root               | `sqrt(16)`          | `4`        |
| `abs(x)`      | Absolute value            | `abs(-9)`           | `9`        |
| `log(x)`      | Natural log (base e)      | `log(10)`           | `2.302585` |
| `log10(x)`    | Log base 10               | `log10(100)`        | `2`        |
| `exp(x)`      | Exponential (e^x)         | `exp(1)`            | `2.718282` |
| `sin(x)`      | Sine (in radians)         | `sin(pi/2)`         | `1`        |
| `cos(x)`      | Cosine                    | `cos(pi)`           | `-1`       |
| `tan(x)`      | Tangent                   | `tan(pi/4)`         | `1`        |
| `round(x, n)` | Round to n decimal places | `round(3.14159, 2)` | `3.14`     |
| `ceiling(x)`  | Round up                  | `ceiling(3.2)`      | `4`        |
| `floor(x)`    | Round down                | `floor(3.9)`        | `3`        |

---

### 🔹 **3. Vectorized Math**

In R, math operations apply **element-wise** over vectors and arrays.

✅ **Example:**

```R
x <- c(2, 4, 6)
y <- c(1, 2, 3)

x + y
# [1] 3 6 9

x * y
# [1] 2 8 18
```

➡️ Each element of `x` and `y` is operated on in parallel.

If the lengths differ, R **recycles** the shorter one:

```R
> x <- c(1, 2, 3, 4)
> y <- c(10, 20)
> x + y
[1] 11 22 13 24
```

---

### 🔹 **4. Mathematical Constants**

R provides some built-in constants:

| Constant        | Meaning           | Example                  |
| --------------- | ----------------- | ------------------------ |
| `pi`            | π (3.141593...)   | `pi * 2` → `6.283185`    |
| `Inf`           | Infinity          | `1/0` → `Inf`            |
| `NaN`           | Not a Number      | `0/0` → `NaN`            |
| `TRUE`, `FALSE` | Boolean constants | `as.numeric(TRUE)` → `1` |

---

### 🔹 **5. Random Numbers & Sequences**

| Function             | Description                          | Example                          |
| -------------------- | ------------------------------------ | -------------------------------- |
| `seq(from, to, by)`  | Create sequence                      | `seq(1, 10, by=2)` → `1 3 5 7 9` |
| `rep(x, times)`      | Repeat elements                      | `rep(5, 3)` → `5 5 5`            |
| `runif(n)`           | Random numbers (uniform)             | `runif(5)`                       |
| `rnorm(n, mean, sd)` | Random numbers (normal distribution) | `rnorm(3, mean=0, sd=1)`         |

---

### 🔹 **6. Example: Simple Statistics**

```R
x <- c(2, 4, 6, 8, 10)
mean(x)   # 6
median(x) # 6
sd(x)     # 3.162278
sum(x)    # 30
```

---

### ✅ **Summary**

| Concept        | Example          | Result               |
| -------------- | ---------------- | -------------------- |
| Arithmetic     | `5 * (2 + 3)`    | `25`                 |
| Math functions | `sqrt(49)`       | `7`                  |
| Vectorized     | `c(1,2,3)^2`     | `1 4 9`              |
| Constants      | `pi * 2`         | `6.283185`           |
| Random numbers | `rnorm(5)`       | Normal random values |
| Basic stats    | `mean(c(1,2,3))` | `2`                  |

---

# 🧩 **Variables in R**

A **variable** in R is simply a **name that stores a value** — such as a number, string, vector, or data frame.
You can think of it as a *container* holding data in memory.

---

### 🔹 **1. Creating Variables**

You can create (or assign) variables using the **assignment operators**:

| Operator | Example   | Description                        |
| -------- | --------- | ---------------------------------- |
| `<-`     | `x <- 10` | Most commonly used in R            |
| `->`     | `10 -> x` | Assigns value to the left variable |
| `=`      | `x = 10`  | Works the same, but less preferred |

✅ **Examples:**

```R
x <- 5
y = 3
z <- x + y
z
# [1] 8
```

➡️ The arrow `<-` is preferred in R because it shows the direction of data flow.

---

### 🔹 **2. Variable Naming Rules**

Variable names in R must follow certain conventions:

✅ **Allowed:**

* Letters (`a-z`, `A-Z`)
* Numbers (but **not at the start**)
* Dot (`.`) and underscore (`_`)

❌ **Not Allowed:**

* Names starting with a number (e.g., `2x`)
* Special characters (`@`, `$`, `#`, `-`, etc.)
* Reserved words (like `if`, `for`, `TRUE`, `NULL`, etc.)

✅ **Examples:**

```R
age <- 21
.student_name <- "Yuvraj"
total_marks <- 480
```

❌ **Invalid examples:**

```R
2var <- 10   # starts with a number
my-var <- 20 # invalid character '-'
```

---

### 🔹 **3. Checking and Removing Variables**

* **List all variables:**

  ```R
  ls()
  ```
* **Remove a variable:**

  ```R
  rm(x)
  ```
* **Remove all variables:**

  ```R
  rm(list = ls())
  ```

---

### 🔹 **4. Assigning Multiple Variables**

R supports **vectorized assignment**:

```R
a <- b <- c <- 100
```

All three variables will store the value `100`.

Or assign using vectors:

```R
x <- c(10, 20, 30)
y <- c("A", "B", "C")
```

---

### 🔹 **5. Checking Variable Type**

Use `class()` or `typeof()` to check what kind of data a variable holds.

✅ **Example:**

```R
x <- 42
class(x)
# [1] "numeric"

y <- "Hello"
class(y)
# [1] "character"
```

---

### 🔹 **6. Variable Scope**

R has **two types of scopes**:

| Scope Type       | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| **Global Scope** | Variables declared outside functions are accessible everywhere.     |
| **Local Scope**  | Variables created inside functions exist only within that function. |

✅ **Example:**

```R
x <- 10       # Global variable

myFunc <- function() {
  y <- 5      # Local variable
  print(x + y)
}

myFunc()  # Output: 15
print(y)  # Error: object 'y' not found
```

---

### 🔹 **7. Constants in R**

R doesn’t have built-in *constant variables*, but by convention, constants are written in **all uppercase letters**:

```R
PI <- 3.14159
MAX_LIMIT <- 100
```

They can still be changed, but developers agree not to modify them.

---

### 🔹 **8. Example Program**

```R
# Assign variables
name <- "Alice"
age <- 25
height <- 5.6

# Display output
cat("Name:", name, "\nAge:", age, "\nHeight:", height)
```

**Output:**

```
Name: Alice 
Age: 25 
Height: 5.6
```

---

### ✅ **Summary Table**

| Concept         | Description            | Example                    |
| --------------- | ---------------------- | -------------------------- |
| Create variable | Assign a value         | `x <- 10`                  |
| View variables  | List all               | `ls()`                     |
| Remove variable | Delete one or all      | `rm(x)` / `rm(list=ls())`  |
| Check type      | Data type of variable  | `class(x)`                 |
| Global scope    | Exists everywhere      | Defined outside a function |
| Local scope     | Inside a function only | Defined inside a function  |

---

# 🧩 **Data Types in R**

Everything in R is an **object**, and each object has a **data type** that defines the **kind of values it can store** and **how operations are performed** on it.

---

## 🧠 **1. What is a Data Type?**

A **data type** determines what kind of value a variable can hold — for example, numbers, text, or logical (TRUE/FALSE).

Think of it as the *nature* or *category* of the data.

---

## 🔹 **2. Basic (Atomic) Data Types in R**

R has **6 main atomic data types**, which are the smallest unit of data in R.

| Type          | Description                       | Example           | Check Function   |
| ------------- | --------------------------------- | ----------------- | ---------------- |
| **Numeric**   | Real numbers (decimal or integer) | `3.14`, `42`      | `is.numeric()`   |
| **Integer**   | Whole numbers only                | `10L`, `-5L`      | `is.integer()`   |
| **Complex**   | Complex numbers                   | `2 + 3i`          | `is.complex()`   |
| **Character** | Text/string values                | `"R Programming"` | `is.character()` |
| **Logical**   | Boolean values                    | `TRUE`, `FALSE`   | `is.logical()`   |
| **Raw**       | Binary data                       | `charToRaw("A")`  | `is.raw()`       |

---

### 🧮 Example Code

```R
num <- 10.5
int <- 10L
char <- "Hello"
logi <- TRUE
comp <- 2 + 3i
rawdata <- charToRaw("R")

# Checking data types
class(num)      # "numeric"
class(int)      # "integer"
class(char)     # "character"
class(logi)     # "logical"
class(comp)     # "complex"
class(rawdata)  # "raw"
```

---

## 🔹 **3. Type Conversion (Coercion)**

R automatically converts data types when you mix them in operations — this is called **type coercion**.

### Example:

```R
x <- c(1, "2", TRUE)
x
# [1] "1" "2" "TRUE"
```

👉 Here, R converts everything to **character**, since it’s the most general type that can hold all values.

### Manual Conversion Functions:

| Function          | Converts To |
| ----------------- | ----------- |
| `as.numeric(x)`   | Numeric     |
| `as.integer(x)`   | Integer     |
| `as.character(x)` | Character   |
| `as.logical(x)`   | Logical     |
| `as.complex(x)`   | Complex     |

✅ Example:

```R
x <- "10"
as.numeric(x)
# [1] 10
```

---

## 🔹 **4. Special Values**

| Symbol         | Meaning       | Example       |
| -------------- | ------------- | ------------- |
| `NA`           | Missing value | `x <- NA`     |
| `NaN`          | Not a Number  | `0/0`         |
| `Inf` / `-Inf` | Infinity      | `1/0`, `-1/0` |
| `NULL`         | Empty object  | `x <- NULL`   |

✅ Example:

```R
x <- c(1, 2, NA, 4)
mean(x)            # NA (because missing value)
mean(x, na.rm=TRUE) # 2.333 (ignores NA)
```

---

## 🔹 **5. Checking Type and Structure**

| Function        | Purpose                | Example      |
| --------------- | ---------------------- | ------------ |
| `class(x)`      | Returns object’s class | `class(x)`   |
| `typeof(x)`     | Returns internal type  | `typeof(x)`  |
| `is.numeric(x)` | Checks if numeric      | `TRUE/FALSE` |
| `str(x)`        | Structure of object    | `str(x)`     |

✅ Example:

```R
y <- 10L
class(y)   # "integer"
typeof(y)  # "integer"
```

---

## 🔹 **6. Example Program**

```R
# Creating variables of different data types
a <- 10.5
b <- 20L
c <- "R Programming"
d <- TRUE
e <- 2 + 3i

# Display values and their types
cat("a =", a, "- Type:", class(a), "\n")
cat("b =", b, "- Type:", class(b), "\n")
cat("c =", c, "- Type:", class(c), "\n")
cat("d =", d, "- Type:", class(d), "\n")
cat("e =", e, "- Type:", class(e), "\n")
```

**Output:**

```
a = 10.5 - Type: numeric
b = 20 - Type: integer
c = R Programming - Type: character
d = TRUE - Type: logical
e = 2+3i - Type: complex
```

---

## 🔹 **7. Diagram — Data Types Hierarchy**

```
R Data Types
│
├── Atomic (Single Values)
│   ├── Numeric
│   ├── Integer
│   ├── Complex
│   ├── Character
│   ├── Logical
│   └── Raw
│
└── Data Structures (Collections)
    ├── Vector
    ├── List
    ├── Matrix
    ├── Array
    └── Data Frame
```

---

## ✅ **Summary Table**

| Category  | Type        | Example          | Conversion Function |
| --------- | ----------- | ---------------- | ------------------- |
| Numeric   | `numeric`   | `3.14`, `2`      | `as.numeric()`      |
| Integer   | `integer`   | `10L`, `-5L`     | `as.integer()`      |
| Character | `character` | `"R"`, `"Data"`  | `as.character()`    |
| Logical   | `logical`   | `TRUE`, `FALSE`  | `as.logical()`      |
| Complex   | `complex`   | `2 + 3i`         | `as.complex()`      |
| Raw       | `raw`       | `charToRaw("A")` | —                   |

---

# 🧩 **Vectors in R**

---

## 🔹 1. What is a Vector?

A **vector** in R is a **sequence of elements** that are **of the same data type**.

Think of it like a **one-dimensional array** —
it can hold numbers, characters, or logical values, but **not a mix** of different types.

📘 Example:

```R
x <- c(10, 20, 30, 40)
```

Here, `x` is a numeric vector of 4 elements.

---

## 🔹 2. Creating Vectors

Vectors are created using the **`c()` (combine)** function.

| Type      | Example                           | Description       |
| --------- | --------------------------------- | ----------------- |
| Numeric   | `v1 <- c(1, 2, 3, 4)`             | Contains numbers  |
| Character | `v2 <- c("R", "Data", "Science")` | Contains text     |
| Logical   | `v3 <- c(TRUE, FALSE, TRUE)`      | Contains booleans |
| Integer   | `v4 <- c(1L, 2L, 3L)`             | Explicit integers |
| Complex   | `v5 <- c(1+2i, 3+4i)`             | Complex numbers   |

---

### 🔸 Using Sequences

R provides special functions to generate numeric sequences.

| Function | Description       | Example            | Output    |
| -------- | ----------------- | ------------------ | --------- |
| `:`      | Sequence operator | `1:5`              | 1 2 3 4 5 |
| `seq()`  | Custom step size  | `seq(1, 10, by=2)` | 1 3 5 7 9 |
| `rep()`  | Repeat values     | `rep(5, times=4)`  | 5 5 5 5   |

✅ Example:

```R
nums <- seq(2, 10, by = 2)
nums
# [1] 2 4 6 8 10
```

---

## 🔹 3. Accessing Vector Elements

You can access vector elements using **square brackets [ ]**.

```R
x <- c(10, 20, 30, 40, 50)

x[1]     # First element
x[3]     # Third element
x[c(2,4)]# Multiple elements
x[-1]    # Exclude first element
```

✅ **Output:**

```
[1] 10
[1] 30
[1] 20 40
[1] 20 30 40 50
```

---

## 🔹 4. Modifying Elements

You can directly change values using indices.

```R
x[2] <- 25
x
# [1] 10 25 30 40 50
```

Add new elements:

```R
x <- c(x, 60)
# [1] 10 25 30 40 50 60
```

---

## 🔹 5. Vector Operations

Vectors in R are **vectorized**, meaning operations are applied to each element automatically.

✅ **Arithmetic operations:**

```R
x <- c(10, 20, 30)
y <- c(1, 2, 3)

x + y  # [1] 11 22 33
x - y  # [1] 9 18 27
x * y  # [1] 10 40 90
x / y  # [1] 10 10 10
```

✅ **Scalar operations:**

```R
x * 2  # [1] 20 40 60
```

---

## 🔹 6. Vector Recycling

When vectors are of **unequal length**, R repeats (recycles) the shorter vector.

```R
x <- c(10, 20, 30, 40)
y <- c(1, 2)

x + y
# [1] 11 22 31 42
```

🧠 Note: R gives a *warning* if the longer vector length is not a multiple of the shorter one.

---

## 🔹 7. Vector Functions

| Function    | Description        | Example                    |
| ----------- | ------------------ | -------------------------- |
| `length(x)` | Number of elements | `length(c(1,2,3))` → `3`   |
| `sum(x)`    | Sum of all values  | `sum(c(1,2,3))` → `6`      |
| `mean(x)`   | Average value      | `mean(c(2,4,6))` → `4`     |
| `max(x)`    | Largest value      | `max(c(1,5,3))` → `5`      |
| `min(x)`    | Smallest value     | `min(c(1,5,3))` → `1`      |
| `sort(x)`   | Sort ascending     | `sort(c(4,1,3))` → `1 3 4` |

✅ Example:

```R
x <- c(10, 20, 30, 40, 50)
cat("Sum =", sum(x), "\nMean =", mean(x))
```

---

## 🔹 8. Logical Indexing

You can use logical conditions to **filter** data.

```R
x <- c(5, 10, 15, 20, 25)
x[x > 15]
# [1] 20 25
```

---

## 🔹 9. Combining Vectors

```R
a <- c(1, 2, 3)
b <- c(4, 5, 6)
c <- c(a, b)
c
# [1] 1 2 3 4 5 6
```

---

## 🔹 10. Diagram — Vector Representation

```
Vector (x)
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
 Index: 1    2    3    4
```

---

## ✅ **Summary Table**

| Operation  | Description     | Example         | Output        |
| ---------- | --------------- | --------------- | ------------- |
| Create     | Combine values  | `x <- c(1,2,3)` | 1 2 3         |
| Sequence   | Generate series | `seq(1,5,by=2)` | 1 3 5         |
| Repeat     | Repeat value    | `rep(5,3)`      | 5 5 5         |
| Access     | Get elements    | `x[2]`          | 2             |
| Filter     | Conditional     | `x[x>2]`        | 3             |
| Length     | Count elements  | `length(x)`     | 3             |
| Arithmetic | Element-wise    | `x+y`           | vector result |

---

## 🧠 **Example Program**

```R
# Create a numeric vector
marks <- c(75, 82, 90, 68, 95)

# Perform basic operations
total <- sum(marks)
average <- mean(marks)
highest <- max(marks)
lowest <- min(marks)

cat("Total =", total, "\nAverage =", average,
    "\nHighest =", highest, "\nLowest =", lowest)
```

**Output:**

```
Total = 410 
Average = 82 
Highest = 95 
Lowest = 68
```

---

# 🧩 **Calling Functions in R**

## 🔹 1. What is a Function?

A **function** is a **set of instructions** that performs a specific task.
In R, almost everything you do — from adding numbers to reading data — involves calling a function.

📘 Example:

```R
sum(c(10, 20, 30))
# Output: 60
```

Here:

* `sum` → is the **function name**
* `c(10, 20, 30)` → is the **argument** passed to it

---

## 🔹 2. Basic Function Syntax

```R
function_name(argument1, argument2, ...)
```

Each function can take **zero or more arguments**.

✅ **Examples:**

```R
sqrt(16)        # Square root
abs(-8)         # Absolute value
round(3.14159)  # Round to nearest integer
```

---

## 🔹 3. Functions with Multiple Arguments

Many functions accept **named arguments**, which makes them more readable.

✅ Example:

```R
round(3.14159, digits = 2)
# Output: 3.14
```

Here:

* `3.14159` is the number
* `digits = 2` specifies rounding precision

---

## 🔹 4. Default Arguments

Some functions have **default values** for arguments —
if you don’t pass them, R uses the default automatically.

✅ Example:

```R
seq(from = 1, to = 10)
# Default step size is 1
```

Equivalent to:

```R
seq(1, 10, by = 1)
```

---

## 🔹 5. Argument Order and Naming

R allows calling functions **with or without naming** arguments.

✅ Example:

```R
seq(1, 10, by = 2)          # Positional
seq(from = 1, to = 10, by = 2)  # Named
seq(to = 10, from = 1, by = 2)  # Order doesn’t matter if named
```

---

## 🔹 6. Nested Function Calls

You can **nest functions** — i.e., call one function inside another.

✅ Example:

```R
result <- sqrt(sum(c(4, 9, 16)))
print(result)
# Output: 5
```

🧠 Explanation:

* `sum(c(4,9,16))` → 29
* `sqrt(29)` → ≈ 5.385

---

## 🔹 7. Getting Help on Functions

R has built-in documentation for every function.

| Command                  | Purpose             |
| ------------------------ | ------------------- |
| `?function_name`         | Open help page      |
| `help(function_name)`    | Same as above       |
| `example(function_name)` | Shows example usage |

✅ Example:

```R
?mean
example(mean)
```

---

## 🔹 8. User-Defined Function Calls

You can also define your own functions and call them like built-ins.

✅ Example:

```R
# Define a function
add <- function(a, b) {
  return(a + b)
}

# Call the function
add(10, 20)
# Output: 30
```

---

## 🔹 9. Functions Returning Multiple Values

A function can return multiple results as a **list**.

✅ Example:

```R
stats <- function(x) {
  result <- list(
    mean = mean(x),
    median = median(x),
    sd = sd(x)
  )
  return(result)
}

values <- c(10, 20, 30, 40)
output <- stats(values)
print(output)
```

**Output:**

```
$mean
[1] 25
$median
[1] 25
$sd
[1] 12.90994
```

---

## 🔹 10. Commonly Used Built-in Functions

| Category   | Function         | Example                   | Output          |
| ---------- | ---------------- | ------------------------- | --------------- |
| Math       | `sum()`          | `sum(1:5)`                | `15`            |
| Math       | `sqrt()`         | `sqrt(16)`                | `4`             |
| Statistics | `mean()`         | `mean(c(1,2,3))`          | `2`             |
| Statistics | `sd()`           | `sd(c(1,2,3))`            | `1`             |
| Character  | `toupper()`      | `toupper("r")`            | `"R"`           |
| Character  | `paste()`        | `paste("Hello", "World")` | `"Hello World"` |
| Sequence   | `seq()`          | `seq(1,5)`                | `1 2 3 4 5`     |
| Repeat     | `rep()`          | `rep(2,4)`                | `2 2 2 2`       |
| Logical    | `any()`, `all()` | `any(c(TRUE,FALSE))`      | `TRUE`          |

---

## 🔹 11. Diagram — Function Calling Structure

```
┌─────────────────────────────────┐
│        Function Call            │
│  function_name(arg1, arg2, …)   │
├─────────────────────────────────┤
│ function_name → Built-in/User   │
│ arg1, arg2 → Passed arguments   │
│ Returns → Result or object      │
└─────────────────────────────────┘
```

---

## ✅ **Example Program**

```R
# Define function
circle_area <- function(radius) {
  area <- pi * radius^2
  return(area)
}

# Call function
r <- 5
result <- circle_area(r)
cat("Area of circle with radius", r, "=", result)
```

**Output:**

```
Area of circle with radius 5 = 78.53982
```

---

## ✅ **Summary Table**

| Concept         | Description                   | Example                       |
| --------------- | ----------------------------- | ----------------------------- |
| Call function   | Execute a predefined function | `sum(1:5)`                    |
| Named arguments | Specify argument by name      | `seq(from=1,to=5)`            |
| Nested call     | Use a function inside another | `sqrt(sum(x))`                |
| User-defined    | Custom-made function          | `myfunc <- function(x) {x^2}` |
| Help            | Documentation for function    | `?mean`                       |

---

# 🧠 **Function Documentation in R**

Function documentation in **R** helps users understand **what a function does, its syntax, arguments, return values, and examples** of how to use it.
R provides **built-in help systems** to access documentation directly from the console.

---

## 📘 **1. Accessing Documentation**

### 🔹 **Using `help()` function**

You can use the `help()` function to display documentation for any R function.

```R
help(mean)
```

or equivalently:

```R
?mean
```

✅ **Example Output:**

* Description: Explains what the function does (e.g., computes the arithmetic mean).
* Usage: Shows syntax (`mean(x, trim = 0, na.rm = FALSE)`).
* Arguments: Explains parameters.
* Details: Provides detailed notes.
* Value: What the function returns.
* Examples: Shows sample code.

---

## 📘 **2. Searching for Help**

### 🔹 **Use `help.search()` or `??` to search topics**

If you don’t remember the exact function name:

```R
help.search("regression")
```

or

```R
??regression
```

🔹 This searches all installed packages’ documentation for the keyword “regression”.

---

## 📘 **3. Getting Argument Details**

### 🔹 **Use `args()`**

Lists a function’s arguments and their defaults.

```R
args(lm)
```

🔹 Output:

```
function (formula, data, subset, weights, ...)
```

---

## 📘 **4. Viewing Example Code**

### 🔹 **Use `example()`**

Runs examples provided in the function’s documentation.

```R
example(mean)
```

---

## 📘 **5. Viewing Function Code**

### 🔹 **Use `print()` or simply type the function name**

To see the actual R code for functions (if not internal C code):

```R
mean
```

or

```R
print(mean)
```

---

## 📘 **6. Getting Help on Packages**

### 🔹 **Use `help(package = "packageName")`**

Shows all functions available in a package.

```R
help(package = "stats")
```

---

## 📘 **7. Getting Vignette (Detailed Tutorial)**

Vignettes are detailed documents provided by packages explaining functionality with examples.

```R
vignette()
```

List all available vignettes.

To open a specific one:

```R
vignette("dplyr")
```

---

## 📘 **8. Getting Function Examples in Code**

If you want to **try examples interactively**:

```R
example(plot)
```

---

## 📘 **9. Getting Quick Help Summary**

If you only want a short description of the function:

```R
help.start()
```

Opens R’s full HTML help browser (GUI mode).

---

## 🧩 **Summary Table**

| Command                          | Description                        |
| -------------------------------- | ---------------------------------- |
| `help(fun)` / `?fun`             | Get documentation for a function   |
| `help.search("term")` / `??term` | Search documentation for a keyword |
| `args(fun)`                      | Show function arguments            |
| `example(fun)`                   | Run function examples              |
| `vignette()`                     | List available vignettes           |
| `help(package = "pkg")`          | Show all functions in a package    |
| `help.start()`                   | Opens HTML help browser            |

---

## 🧠 **Example**

```R
# Find documentation for the sum() function
?sum

# List arguments of the function
args(sum)

# View examples of the function
example(sum)
```

---

# 📊 **Missing Data in R**

In real-world datasets, it’s very common to have **missing or incomplete values** — for example, a column of ages might have some empty cells or a survey might have skipped responses.
In R, **missing data** are handled using a special value called `NA`.

---

## 🧠 **1. What is Missing Data?**

**Missing data** refers to data points that are not recorded or unavailable for some reason.

In R, a missing value is represented by:

```R
NA   # Not Available
```

Examples:

```R
x <- c(1, 2, NA, 4, 5)
```

Here, the 3rd element is missing.

---

## 📘 **2. Identifying Missing Data**

### 🔹 **Check for Missing Values**

You can use `is.na()` to detect missing values in a vector or dataset.

```R
x <- c(10, 20, NA, 40)
is.na(x)
```

**Output:**

```
[1] FALSE FALSE TRUE FALSE
```

✅ TRUE indicates the missing value.

---

## 📘 **3. Counting Missing Values**

To count how many values are missing:

```R
sum(is.na(x))
```

**Output:** `1` (since there’s one missing value)

---

## 📘 **4. Removing Missing Data**

If you want to remove missing values:

### 🔹 **Using `na.omit()`**

```R
x_clean <- na.omit(x)
x_clean
```

**Output:**

```
[1] 10 20 40
```

### 🔹 **Using `complete.cases()`**

This returns only the rows where *no* values are missing.

```R
data <- data.frame(a = c(1, 2, NA), b = c(4, NA, 6))
data[complete.cases(data), ]
```

**Output:**

```
  a b
1 1 4
```

---

## 📘 **5. Replacing Missing Data**

Sometimes instead of removing, you can **replace (impute)** missing values.

### 🔹 Replace with a specific value

```R
x[is.na(x)] <- 0
```

### 🔹 Replace with the mean

```R
x[is.na(x)] <- mean(x, na.rm = TRUE)
```

`na.rm = TRUE` removes missing values while computing the mean.

---

## 📘 **6. Ignoring Missing Data in Calculations**

When performing operations like `mean()` or `sum()`, R returns `NA` if there are missing values unless you specify `na.rm = TRUE`.

### Example:

```R
x <- c(10, 20, NA, 30)

mean(x)
# Output: NA

mean(x, na.rm = TRUE)
# Output: 20
```

---

## 📘 **7. Detecting Missing Data in Data Frames**

You can apply `is.na()` to a data frame to find all missing values:

```R
data <- data.frame(
  Name = c("A", "B", "C"),
  Age  = c(25, NA, 30),
  Salary = c(50000, 60000, NA)
)

is.na(data)
```

**Output:**

```
     Name   Age Salary
[1,] FALSE FALSE  FALSE
[2,] FALSE  TRUE  FALSE
[3,] FALSE FALSE   TRUE
```

---

## 📘 **8. Visualizing Missing Data**

To understand missing data patterns, you can use packages like:

```R
install.packages("naniar")
library(naniar)

vis_miss(data)
```

This visually shows which columns and rows contain missing values.

---

## 🧩 **Summary Table**

| Function / Option      | Purpose                                |
| ---------------------- | -------------------------------------- |
| `NA`                   | Represents missing value               |
| `is.na(x)`             | Detects missing values                 |
| `sum(is.na(x))`        | Counts missing values                  |
| `na.omit(x)`           | Removes missing values                 |
| `complete.cases(data)` | Returns rows without missing values    |
| `na.rm = TRUE`         | Ignores missing values in calculations |
| `x[is.na(x)] <- value` | Replaces missing values                |

---

## 🧠 **Example Summary**

```R
# Example dataset
x <- c(1, 2, NA, 4, 5, NA)

# Detect missing
is.na(x)

# Count missing
sum(is.na(x))

# Remove missing
clean_x <- na.omit(x)

# Replace missing with mean
x[is.na(x)] <- mean(x, na.rm = TRUE)
```

---

# 🧩 **Advanced Data Structures in R**

R supports several **data structures** to store and manipulate data efficiently.
Let’s first recall the **basic hierarchy** of R objects:

| Data Structure | Type of Elements               | Dimensions         | Example                        |
| -------------- | ------------------------------ | ------------------ | ------------------------------ |
| **Vector**     | Same type                      | 1D                 | `c(1,2,3)`                     |
| **Matrix**     | Same type                      | 2D                 | `matrix(1:6, nrow=2)`          |
| **Array**      | Same type                      | Multi-dimensional  | `array(1:8, dim=c(2,2,2))`     |
| **List**       | Different types                | 1D (heterogeneous) | `list(name="A", age=20)`       |
| **Data Frame** | Columns can be different types | 2D (tabular)       | `data.frame(name="A", age=20)` |

---

## 🧱 **1. DataFrame**

A **DataFrame** is a **2D table-like structure** — similar to an Excel sheet or SQL table.
Each **column** can contain a different type of data (numeric, character, factor, etc.).

### 🧠 **Structure:**

```
+-------+-------+-------+
| Name  | Age   | Marks |
+-------+-------+-------+
| Ram   | 20    | 85    |
| Sam   | 21    | 90    |
| John  | 19    | 78    |
+-------+-------+-------+
```

---

### 🧮 **Creating a DataFrame:**

```R
students <- data.frame(
  Name = c("Ram", "Sam", "John"),
  Age = c(20, 21, 19),
  Marks = c(85, 90, 78)
)

print(students)
```

**Output:**

```
   Name Age Marks
1   Ram  20    85
2   Sam  21    90
3  John  19    78
```

---

### 🧰 **Accessing Elements:**

```R
students$Name      # Access column by name
students[1, ]      # First row
students[, 2]      # Second column
students[2, 3]     # Row 2, Column 3
```

---

### 🧪 **Adding New Column:**

```R
students$Grade <- c("A", "A+", "B")
```

### 🧹 **Removing Column:**

```R
students$Age <- NULL
```

---

✅ **Useful Functions:**

| Function      | Purpose             |
| ------------- | ------------------- |
| `nrow(df)`    | Number of rows      |
| `ncol(df)`    | Number of columns   |
| `names(df)`   | Column names        |
| `str(df)`     | Structure of data   |
| `summary(df)` | Statistical summary |

---

## 🧮 **2. Lists**

A **list** in R is a **collection of elements of different types** — numeric, character, vector, matrix, dataframe, even other lists!

### 📘 **Example:**

```R
my_list <- list(
  Name = "Ravi",
  Age = 25,
  Scores = c(85, 90, 88),
  Details = data.frame(ID=1, Dept="CSE")
)

print(my_list)
```

**Output (simplified):**

```
$Name
[1] "Ravi"

$Age
[1] 25

$Scores
[1] 85 90 88

$Details
  ID Dept
1  1  CSE
```

---

### 🧭 **Accessing List Elements:**

```R
my_list$Name
my_list[[3]]
my_list[["Scores"]][2]   # second score
```

---

✅ **Key Features:**

* Can store **heterogeneous data**.
* Each element is indexed by name or number.
* Useful for **returning multiple outputs** from a function.

---

### 📦 **Nested List Example:**

```R
nested_list <- list(
  person = list(name="Anu", age=22),
  marks = list(math=90, sci=85)
)
nested_list$person$name
```

---

## 🧮 **3. Matrices**

A **matrix** is a **two-dimensional** data structure with **homogeneous elements** (all elements must be of the same data type).

### 📘 **Structure:**

```
     [,1] [,2] [,3]
[1,]   1    3    5
[2,]   2    4    6
```

---

### 🧮 **Creating a Matrix:**

```R
m <- matrix(1:6, nrow = 2, ncol = 3)
print(m)
```

**Output:**

```
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
```

(Default filling is column-wise)

---

### ⚙️ **Matrix Operations:**

```R
m1 <- matrix(1:4, 2)
m2 <- matrix(5:8, 2)
m1 + m2      # Element-wise addition
m1 %*% m2    # Matrix multiplication
t(m1)        # Transpose
```

---

✅ **Functions:**

| Function    | Purpose               |
| ----------- | --------------------- |
| `nrow(m)`   | Number of rows        |
| `ncol(m)`   | Number of columns     |
| `dim(m)`    | Dimensions            |
| `t(m)`      | Transpose             |
| `m1 %*% m2` | Matrix multiplication |

---

## 🧮 **4. Arrays**

An **array** is like a **multi-dimensional matrix**.
You can think of it as **a stack of matrices**.

---

### 📘 **Creating an Array:**

```R
arr <- array(1:12, dim = c(2, 3, 2))
print(arr)
```

**Output:**

```
, , 1
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

, , 2
     [,1] [,2] [,3]
[1,]    7    9   11
[2,]    8   10   12
```

Here we have **2 matrices (layers)** of **2x3** each.

---

### 🧭 **Accessing Elements:**

```R
arr[1, 2, 1]  # Row 1, Column 2, Layer 1
```

---

✅ **Features:**

| Feature           | Description                       |
| ----------------- | --------------------------------- |
| Multi-dimensional | Can have 2, 3, or more dimensions |
| Homogeneous       | All elements must be same type    |
| Useful in         | Scientific & spatial computations |

---

## 🧩 **Summary Table**

| Structure     | Dimensions | Data Type         | Access Method | Example Use            |
| ------------- | ---------- | ----------------- | ------------- | ---------------------- |
| **Vector**    | 1D         | Same              | `x[1]`        | Simple lists of values |
| **Matrix**    | 2D         | Same              | `m[1,2]`      | Linear algebra         |
| **Array**     | 3D+        | Same              | `a[1,2,3]`    | Image / spatial data   |
| **List**      | 1D         | Mixed             | `l$Name`      | Complex, nested data   |
| **DataFrame** | 2D         | Mixed (by column) | `df$Age`      | Tabular data           |

---

## 📊 **Visual Summary Diagram**

```
Vector → Matrix → Array
   ↓
  List → DataFrame
```

* **Vector, Matrix, Array** → homogeneous
* **List, DataFrame** → heterogeneous

---

# 📥 **Reading Data into R**

R provides many built-in and package-based functions to **import external data** into **data frames**, which can then be processed and analyzed.

---

## 🧩 **1. Common Data Import Formats**

| File Type      | Example Extension | Function to Read             | Function to Write       |
| -------------- | ----------------- | ---------------------------- | ----------------------- |
| **CSV**        | `.csv`            | `read.csv()` / `read.csv2()` | `write.csv()`           |
| **Text (TSV)** | `.txt`, `.tsv`    | `read.table()`               | `write.table()`         |
| **Excel**      | `.xls`, `.xlsx`   | `readxl::read_excel()`       | `writexl::write_xlsx()` |
| **JSON**       | `.json`           | `jsonlite::fromJSON()`       | `jsonlite::toJSON()`    |
| **Database**   | `.db`, `.sql`     | `DBI::dbReadTable()`         | `DBI::dbWriteTable()`   |

---

## 📘 **2. Reading CSV Files**

A **CSV (Comma-Separated Values)** file stores tabular data separated by commas.

### 🧠 Example File: `students.csv`

```
Name,Age,Marks
Ravi,21,85
Anu,22,90
Kiran,20,78
```

---

### 📥 **Read CSV into R**

```R
students <- read.csv("students.csv")
print(students)
```

**Output:**

```
   Name Age Marks
1  Ravi  21    85
2   Anu  22    90
3 Kiran  20    78
```

---

### ⚙️ **Optional Parameters**

| Parameter          | Description                          | Example                                        |
| ------------------ | ------------------------------------ | ---------------------------------------------- |
| `header`           | Whether first row has column names   | `read.csv("file.csv", header=TRUE)`            |
| `sep`              | Field separator                      | `read.csv("file.csv", sep=",")`                |
| `stringsAsFactors` | Prevents automatic factor conversion | `read.csv("file.csv", stringsAsFactors=FALSE)` |
| `na.strings`       | What represents missing data         | `read.csv("file.csv", na.strings="NA")`        |

---

### 📤 **Write CSV**

```R
write.csv(students, "output_students.csv", row.names = FALSE)
```

---

### 📊 **Diagram: CSV Reading Process**

```
[students.csv] → read.csv() → DataFrame(students)
```

---

## 📘 **3. Reading Excel Files (.xls / .xlsx)**

To read Excel files, you must install and load the **readxl** or **openxlsx** package.

---

### 🧩 **Install and Load Package**

```R
install.packages("readxl")
library(readxl)
```

---

### 📥 **Read Excel File**

Example: `data.xlsx`

| Name  | Age | Marks |
| ----- | --- | ----- |
| Ravi  | 21  | 85    |
| Anu   | 22  | 90    |
| Kiran | 20  | 78    |

```R
students_excel <- read_excel("data.xlsx")
print(students_excel)
```

**Output:**

```
# A tibble: 3 × 3
  Name   Age Marks
  <chr> <dbl> <dbl>
1 Ravi     21    85
2 Anu      22    90
3 Kiran    20    78
```

> `tibble` is a modern form of `data.frame` (from the `tidyverse`).

---

### ⚙️ **Optional Parameters (read_excel)**

| Parameter   | Description                    | Example                                   |
| ----------- | ------------------------------ | ----------------------------------------- |
| `sheet`     | Specify sheet name or index    | `read_excel("data.xlsx", sheet=2)`        |
| `range`     | Specify cell range             | `read_excel("data.xlsx", range="A1:C4")`  |
| `col_names` | TRUE/FALSE for header row      | `read_excel("data.xlsx", col_names=TRUE)` |
| `na`        | Define missing value indicator | `read_excel("data.xlsx", na="NA")`        |

---

### 📤 **Write to Excel**

Install `writexl` or `openxlsx`:

```R
install.packages("writexl")
library(writexl)

write_xlsx(students_excel, "students_output.xlsx")
```

---

## 📘 **4. Reading Text / TSV Files**

If the file uses a **tab** or **space** as separator:

### Example File: `students.txt`

```
Name Age Marks
Ravi 21 85
Anu 22 90
Kiran 20 78
```

```R
students_txt <- read.table("students.txt", header=TRUE)
```

Or for **tab-separated**:

```R
students_tsv <- read.delim("students.tsv")
```

---

## 📘 **5. Viewing the Imported Data**

```R
head(students)     # View first 6 rows
tail(students)     # View last 6 rows
summary(students)  # Get statistical summary
str(students)      # Structure of data frame
```

---

## 📊 **6. Example Workflow**

```R
# Step 1: Import Data
data <- read.csv("sales.csv", header = TRUE, stringsAsFactors = FALSE)

# Step 2: Inspect Data
head(data)
summary(data)
str(data)

# Step 3: Clean Missing Data
data <- na.omit(data)

# Step 4: Export Processed Data
write.csv(data, "clean_sales.csv", row.names = FALSE)
```

---

## 🧠 **7. Common Errors & Fixes**

| Error                       | Cause           | Solution                                                |
| --------------------------- | --------------- | ------------------------------------------------------- |
| `file not found`            | Wrong file path | Use full path `"C:/Users/.../file.csv"`                 |
| `NA introduced by coercion` | Type mismatch   | Convert column using `as.numeric()` or `as.character()` |
| `unexpected symbol`         | Wrong separator | Use `sep="\t"` or `sep=";"` as needed                   |

---

## 📘 **8. Tip: Set Working Directory**

You can set or get the working directory to simplify file paths.

```R
getwd()                     # Show current working directory
setwd("C:/Users/Yuvraj/Documents/R")   # Change working directory
```

---

## 🧩 **Summary Table**

| File Type     | Function       | Package | Output Object    |
| ------------- | -------------- | ------- | ---------------- |
| CSV           | `read.csv()`   | Base R  | DataFrame        |
| Excel         | `read_excel()` | readxl  | Tibble/DataFrame |
| Text          | `read.table()` | Base R  | DataFrame        |
| TSV           | `read.delim()` | Base R  | DataFrame        |
| Excel (Write) | `write_xlsx()` | writexl | File (.xlsx)     |

---

## 🧠 **Visualization of the Process**

```
+----------------+
|   Data Files   |
|  (.csv, .xlsx) |
+----------------+
        ↓
  Import Functions
 (read.csv, read_excel)
        ↓
+----------------+
|   Data Frame   |
|   in R Memory  |
+----------------+
```

---

# 📘 **Reading from Databases in R**

R allows you to connect to and interact with **databases** (like MySQL, PostgreSQL, SQLite, Oracle, etc.) to directly read and write data without manual export/import steps.

---

## 🧩 **1. Why Read from Databases?**

* Databases store large, structured datasets efficiently.
* Instead of exporting CSVs, R can directly connect, query, and import only the required data.
* Enables automation, reproducibility, and integration with real-world systems.

---

## 🧠 **2. Common R Packages for Database Connectivity**

| Package                         | Use Case                                                      |
| ------------------------------- | ------------------------------------------------------------- |
| **DBI**                         | Standard interface for database operations.                   |
| **RMySQL**                      | Connect to **MySQL** or **MariaDB** databases.                |
| **RPostgreSQL** / **RPostgres** | Connect to **PostgreSQL** databases.                          |
| **RODBC**                       | Generic ODBC interface (works for many DBs via ODBC drivers). |
| **RSQLite**                     | Work with **SQLite** databases (lightweight, file-based).     |
| **odbc**                        | Modern and high-performance ODBC package.                     |

---

## ⚙️ **3. Basic Workflow**

1. **Load the required package**
2. **Establish a connection**
3. **List tables**
4. **Run SQL queries**
5. **Fetch data**
6. **Close the connection**

---

## 🧩 **4. Example — Connecting to a MySQL Database**

```r
# Install packages if not already installed
install.packages("DBI")
install.packages("RMySQL")

# Load libraries
library(DBI)

# Create connection
con <- dbConnect(
  RMySQL::MySQL(),
  dbname = "company_db",
  host = "localhost",
  port = 3306,
  user = "root",
  password = "your_password"
)

# List tables in the database
dbListTables(con)

# Run a SQL query
employee_data <- dbGetQuery(con, "SELECT * FROM employees LIMIT 10")

# Display the data
print(employee_data)

# Disconnect
dbDisconnect(con)
```

---

## 💾 **5. Example — Using SQLite Database**

SQLite databases are stored in a single file, making them ideal for local projects.

```r
# Load package
library(DBI)
library(RSQLite)

# Connect to SQLite database (creates if not exists)
con <- dbConnect(RSQLite::SQLite(), dbname = "students.db")

# Create a table
dbWriteTable(con, "students", data.frame(
  id = 1:3,
  name = c("Alice", "Bob", "Charlie"),
  marks = c(85, 90, 78)
))

# Read from the table
data <- dbReadTable(con, "students")
print(data)

# Run a query
result <- dbGetQuery(con, "SELECT * FROM students WHERE marks > 80")
print(result)

# Disconnect
dbDisconnect(con)
```

---

## 🔍 **6. Using ODBC for Universal Database Access**

If your system has an **ODBC driver**, use the `odbc` package.

```r
library(DBI)
library(odbc)

con <- dbConnect(odbc(),
                 Driver   = "PostgreSQL Driver",
                 Server   = "localhost",
                 Database = "sales_db",
                 UID      = "user",
                 PWD      = "password",
                 Port     = 5432)

data <- dbGetQuery(con, "SELECT * FROM transactions LIMIT 5")
print(data)

dbDisconnect(con)
```

---

## 📊 **7. Writing Data Back to Database**

```r
# Assume you already have a connection
dbWriteTable(con, "new_table", my_dataframe, overwrite = TRUE)
```

* `overwrite = TRUE` → replaces the table if it exists.
* `append = TRUE` → adds new rows to existing table.

---

## ✅ **8. Advantages**

* Fast, secure, and scalable data access.
* Handles large datasets efficiently.
* Seamless integration with SQL and R functions.
* Enables data automation pipelines.

---

## ⚠️ **9. Common Issues**

| Issue               | Cause / Fix                               |
| ------------------- | ----------------------------------------- |
| Connection Error    | Incorrect credentials or port             |
| SSL Handshake Error | Database requires SSL setup               |
| Missing Driver      | Install proper R package or system driver |
| Permissions Denied  | Ensure read/write privileges in DB        |

---

# 📊 **Statistical Graphics and Visualization in R**

R is one of the most powerful languages for **data visualization** — it provides both **basic plotting functions** and **advanced graphical systems** like **ggplot2** for statistical and customized graphics.

---

## 🎯 **1. What is Statistical Visualization?**

**Statistical Graphics** are visual representations of data that help:

* Summarize complex datasets
* Identify patterns, trends, and outliers
* Compare groups or relationships
* Support statistical reasoning

---

## 🧩 **2. R’s Visualization Systems**

| System                            | Description                                                    | Example Package    |
| --------------------------------- | -------------------------------------------------------------- | ------------------ |
| **Base Graphics**                 | Built into R; uses simple plotting functions                   | `plot()`, `hist()` |
| **Lattice Graphics**              | Designed for conditioning plots (multi-variable relationships) | `lattice`          |
| **ggplot2 (Grammar of Graphics)** | Most flexible and modern system                                | `ggplot2`          |

---

## 🧮 **3. Base Graphics in R**

### 🟢 Example: Basic Plotting

```r
# Simple scatter plot
x <- 1:10
y <- x^2
plot(x, y, main="Base R Plot", xlab="X Values", ylab="Y Values", col="blue", pch=19)
```

**Common Base R Plot Functions:**

| Function    | Description                  |
| ----------- | ---------------------------- |
| `plot()`    | Generic plotting function    |
| `hist()`    | Histogram                    |
| `boxplot()` | Box plot                     |
| `barplot()` | Bar chart                    |
| `pie()`     | Pie chart                    |
| `lines()`   | Add lines to plots           |
| `points()`  | Add points to existing plots |
| `abline()`  | Add straight line            |
| `legend()`  | Add legend                   |

---

## 📈 **4. Lattice Graphics**

Lattice allows **multi-panel plots** to visualize relationships across variables.

```r
install.packages("lattice")
library(lattice)

# Example: Sepal Length vs Sepal Width for each Species
xyplot(Sepal.Length ~ Sepal.Width | Species, data = iris,
       main = "Lattice Plot Example", layout = c(3, 1))
```

---

## 🎨 **5. ggplot2 — Grammar of Graphics**

`ggplot2` is the most widely used R package for elegant and complex graphics.

### ⚙️ **Basic Structure**

```r
ggplot(data, aes(x, y)) + geom_<type>() + theme_<style>()
```

### 🟢 Example: Scatter Plot

```r
install.packages("ggplot2")
library(ggplot2)

ggplot(data = iris, aes(x = Sepal.Length, y = Petal.Length, color = Species)) +
  geom_point(size = 3) +
  ggtitle("Sepal vs Petal Length by Species") +
  theme_minimal()
```

### 🟣 Example: Histogram

```r
ggplot(mtcars, aes(x = mpg)) +
  geom_histogram(binwidth = 2, fill = "skyblue", color = "black") +
  ggtitle("Distribution of Miles per Gallon")
```

### 🟠 Example: Boxplot

```r
ggplot(iris, aes(x = Species, y = Sepal.Length, fill = Species)) +
  geom_boxplot() +
  ggtitle("Sepal Length by Species")
```

---

## 🧠 **6. Common Geometries (Geoms) in ggplot2**

| Geometry           | Function     | Purpose                          |
| ------------------ | ------------ | -------------------------------- |
| `geom_point()`     | Scatter plot | Relationship between 2 variables |
| `geom_line()`      | Line chart   | Time series or trends            |
| `geom_bar()`       | Bar chart    | Category comparisons             |
| `geom_histogram()` | Histogram    | Frequency distribution           |
| `geom_boxplot()`   | Box plot     | Spread and outliers              |
| `geom_density()`   | Density plot | Smooth distribution curve        |

---

## 🔧 **7. Customizing Visuals**

You can enhance visual clarity with themes and labels:

```r
ggplot(mtcars, aes(x = factor(cyl), y = mpg, fill = factor(cyl))) +
  geom_boxplot() +
  labs(title = "Mileage by Cylinder Count", x = "Cylinders", y = "MPG") +
  theme_classic()
```

---

## 📊 **8. Combining Statistics with Plots**

ggplot2 can overlay **statistical summaries**:

```r
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", col = "red") +
  ggtitle("Regression Line: MPG vs Weight")
```

This adds a **linear regression line** showing the trend between variables.

---

## 🧮 **9. Visualizing Categorical Data**

```r
# Bar plot of gear counts
ggplot(mtcars, aes(x = factor(gear))) +
  geom_bar(fill = "orange") +
  ggtitle("Count of Cars by Gear Type")
```

---

## 🌐 **10. Advanced: Faceting**

Faceting allows multiple small plots based on a categorical variable.

```r
ggplot(iris, aes(x = Petal.Length, y = Petal.Width)) +
  geom_point() +
  facet_wrap(~ Species) +
  ggtitle("Faceted Plot by Species")
```

---

## ✅ **11. Advantages of R Visualization**

* Handles **large datasets** easily.
* Integrates with **statistical modeling** results.
* Fully **customizable** aesthetics.
* Wide range of **themes, extensions**, and **interactive libraries** (like `plotly`).

---

# 📊 **Basic Statistics in R: Summary Statistics**

Summary Statistics are **quantitative descriptions** that summarize and provide insight into the main features of a dataset.
They help you **understand data distribution, central tendency, and variability** before applying advanced analytics or visualization.

---

## 🎯 **1. What are Summary Statistics?**

Summary statistics give an **overview** of your dataset by describing:

* **Central tendency** (mean, median, mode)
* **Dispersion** (range, variance, standard deviation)
* **Shape of distribution** (skewness, kurtosis)
* **Count and missing values**

In short, they answer:

> “What does my data look like overall?”

---

## 🧩 **2. Key Summary Measures**

| Type                 | Statistic          | Meaning                  | R Function                                    |
| -------------------- | ------------------ | ------------------------ | --------------------------------------------- |
| **Central Tendency** | Mean               | Average value            | `mean()`                                      |
|                      | Median             | Middle value             | `median()`                                    |
|                      | Mode               | Most frequent value      | Custom function                               |
| **Dispersion**       | Range              | Max - Min                | `range()`                                     |
|                      | Variance           | Spread around mean       | `var()`                                       |
|                      | Standard Deviation | Average deviation        | `sd()`                                        |
| **Position**         | Min, Max           | Smallest & Largest value | `min()`, `max()`                              |
| **Distribution**     | Quantiles          | Divide data into parts   | `quantile()`                                  |
| **Shape**            | Skewness, Kurtosis | Asymmetry and peakedness | `library(e1071)` → `skewness()`, `kurtosis()` |

---

## 🧮 **3. Example Dataset**

```r
data <- c(12, 15, 13, 17, 19, 20, 18, 15, 14)
```

---

## 🧠 **4. Central Tendency**

### ➤ Mean

```r
mean(data)
# Output: 15.9
```

**Interpretation:** The average value of the dataset.

### ➤ Median

```r
median(data)
# Output: 15
```

**Interpretation:** Middle value when data is sorted.

### ➤ Mode

R does not have a built-in mode function, but you can define one:

```r
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
getmode(data)
# Output: 15
```

---

## 📏 **5. Dispersion (Variability)**

### ➤ Range

```r
range(data)
# Output: 12 20
```

### ➤ Variance

```r
var(data)
# Output: 7.3625
```

### ➤ Standard Deviation

```r
sd(data)
# Output: 2.7134
```

**Interpretation:** The data points deviate from the mean by ~2.7 units on average.

---

## 🔢 **6. Quantiles and Percentiles**

```r
quantile(data)
# Output:
# 0%  25%  50%  75% 100%
# 12   14   15   18   20
```

**Interpretation:**

* 25% of data ≤ 14
* 75% of data ≤ 18

To find specific percentile:

```r
quantile(data, probs = 0.9)
# Output: 19.8
```

---

## 🧮 **7. Shape of Distribution**

```r
install.packages("e1071")
library(e1071)

skewness(data)   # Measure of asymmetry
kurtosis(data)   # Measure of peak/flatness
```

* **Skewness > 0:** Right-skewed (tail on right)
* **Skewness < 0:** Left-skewed (tail on left)
* **Kurtosis > 3:** Leptokurtic (sharp peak)
* **Kurtosis < 3:** Platykurtic (flat peak)

---

## 📋 **8. Summary Function**

You can get all important statistics at once:

```r
summary(data)
# Output:
# Min. 1st Qu. Median Mean 3rd Qu. Max.
# 12.0  14.0   15.0   15.9  18.0  20.0
```

---

## 🧩 **9. Summary of a DataFrame**

Example using built-in dataset:

```r
summary(iris)
```

**Output:**
Shows mean, median, min, max, and quartiles for each numeric column.

---

## 🔍 **10. Visualizing Summary Statistics**

Combine summary stats with visualization to understand data better:

### ➤ Histogram

```r
hist(data, main="Histogram of Data", xlab="Values", col="lightblue")
```

### ➤ Boxplot

```r
boxplot(data, main="Boxplot of Data", col="orange")
```

Shows **median**, **quartiles**, and **outliers** visually.

---

## ✅ **11. Key Takeaways**

| Concept               | Description                              |
| --------------------- | ---------------------------------------- |
| **Mean**              | Represents the average                   |
| **Median**            | Middle value (less affected by outliers) |
| **Mode**              | Most frequent value                      |
| **Variance/SD**       | Spread of data                           |
| **Range**             | Difference between extremes              |
| **Skewness/Kurtosis** | Describe shape                           |
| **Summary()**         | Quick overview in one command            |

---

# 📈 **Correlation and Covariance in R**

Both **correlation** and **covariance** describe **relationships between two variables** —
but they differ in **scale** and **interpretation**.

Let’s understand both deeply with math, intuition, and R examples 👇

---

## 🧠 **1. Covariance — Measure of Relationship Direction**

### 🔹 **Definition**

Covariance measures **how two variables change together**.

* If one variable increases when the other increases → **Positive covariance**
* If one increases while the other decreases → **Negative covariance**

### 🔹 **Mathematical Formula**

For variables ( X ) and ( Y ):

[
\text{Cov}(X, Y) = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{n-1}
]

### 🔹 **Interpretation**

| Covariance Value | Meaning                                                         |
| ---------------: | --------------------------------------------------------------- |
|            `> 0` | Both variables increase together (Positive relationship)        |
|            `< 0` | One increases while the other decreases (Negative relationship) |
|            `= 0` | No relationship between the variables                           |

---

### 🔹 **Example in R**

```r
x <- c(10, 20, 30, 40, 50)
y <- c(15, 25, 35, 45, 55)

cov(x, y)
```

**Output:**

```
250
```

✅ **Interpretation:** Positive covariance → both variables move in the same direction.

---

### 🔹 **Example 2: Negative Covariance**

```r
a <- c(10, 20, 30, 40, 50)
b <- c(50, 40, 30, 20, 10)

cov(a, b)
```

**Output:**

```
-250
```

✅ **Interpretation:** Negative covariance → one increases while the other decreases.

---

## ⚖️ **2. Correlation — Measure of Relationship Strength**

### 🔹 **Definition**

Correlation shows **how strongly two variables are related**, and **is normalized** between **-1 and +1**.

It’s derived from covariance:

[
r_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
]

Where:

* ( \sigma_X ), ( \sigma_Y ) are standard deviations of ( X ) and ( Y ).

---

### 🔹 **Interpretation Table**

| Correlation (r) | Relationship                  |
| --------------- | ----------------------------- |
| +1              | Perfect positive relationship |
| +0.7 to +0.9    | Strong positive               |
| +0.3 to +0.6    | Moderate positive             |
| 0               | No correlation                |
| -0.3 to -0.6    | Moderate negative             |
| -0.7 to -0.9    | Strong negative               |
| -1              | Perfect negative relationship |

---

### 🔹 **Example in R**

```r
x <- c(10, 20, 30, 40, 50)
y <- c(15, 25, 35, 45, 55)

cor(x, y)
```

**Output:**

```
1
```

✅ **Perfect positive correlation**

---

### 🔹 **Example 2: Negative Correlation**

```r
a <- c(10, 20, 30, 40, 50)
b <- c(50, 40, 30, 20, 10)

cor(a, b)
```

**Output:**

```
-1
```

✅ **Perfect negative correlation**

---

## 📊 **3. Visualizing Correlation**

### ➤ **Scatter Plot**

A scatter plot helps to visualize correlation.

```r
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)
plot(x, y, main="Positive Correlation", col="blue", pch=19)
```

---

### ➤ **Correlation Matrix**

For a **data frame** with multiple variables:

```r
data <- data.frame(
  height = c(150, 160, 170, 180, 190),
  weight = c(50, 60, 70, 80, 90),
  age = c(20, 25, 30, 35, 40)
)

cor(data)
```

**Output:**

```
          height    weight       age
height  1.0000000  1.0000000  1.0000000
weight  1.0000000  1.0000000  1.0000000
age     1.0000000  1.0000000  1.0000000
```

✅ **All are perfectly correlated** (since data is linear).

---

## 📈 **4. Covariance vs Correlation — Comparison**

| Feature            | Covariance                               | Correlation                                     |
| ------------------ | ---------------------------------------- | ----------------------------------------------- |
| **Definition**     | Measures how two variables vary together | Measures strength and direction of relationship |
| **Formula**        | Σ((X−μₓ)(Y−μᵧ)) / (n−1)                  | Cov(X,Y) / (σₓσᵧ)                               |
| **Range**          | (−∞, +∞)                                 | −1 to +1                                        |
| **Unit**           | Product of variables’ units              | Unitless                                        |
| **Interpretation** | Difficult due to scale                   | Easy and comparable                             |
| **Normalization**  | No                                       | Yes                                             |
| **Use Case**       | Intermediate step                        | Final relationship metric                       |

---

## 📘 **5. Real-Life Example**

**Scenario:**
You have students’ **study hours** and their **exam scores**.

```r
hours <- c(2, 4, 6, 8, 10)
marks <- c(30, 50, 65, 80, 95)

# Covariance
cov(hours, marks)

# Correlation
cor(hours, marks)
```

**Output:**

```
Covariance = 81.25
Correlation = 0.993
```

✅ The high correlation (close to 1) means that **more study hours strongly lead to higher marks**.

---

## 🧩 **6. Visualization: Correlation Matrix Heatmap**

You can visualize correlations easily using `corrplot` package:

```r
install.packages("corrplot")
library(corrplot)

M <- cor(mtcars)
corrplot(M, method="color")
```

This shows a **color-coded heatmap** of correlations between variables in the dataset.

---

## 🧠 **7. Summary Table**

| Aspect         | Covariance                   | Correlation              |
| -------------- | ---------------------------- | ------------------------ |
| Meaning        | Direction of relationship    | Strength & direction     |
| Range          | Unbounded                    | -1 ≤ r ≤ +1              |
| Scale          | Dependent on data units      | Independent of units     |
| Output         | Can be large or small number | Always between -1 and +1 |
| Interpretation | Hard to compare              | Easy to compare          |

---

# 🧮 **T-Test in R (Student’s t-test)**

A **t-test** is a statistical method used to **compare the means of two groups** and determine whether they are **significantly different** from each other.
It is one of the most fundamental hypothesis tests in statistics.

---

## 🎯 **1. Purpose of a T-Test**

We use a **t-test** when:

* The population **standard deviation is unknown**.
* The **sample size is small (n < 30)**.
* We want to test **mean differences** between groups.

---

## 🧠 **2. Basic Idea**

It tests the **null hypothesis (H₀)**:

> “There is **no significant difference** between the means of two groups.”

Versus the **alternative hypothesis (H₁)**:

> “There **is a significant difference** between the means.”

---

## 📘 **3. Formula**

[
t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
]

Where:

* ( \bar{X}_1, \bar{X}_2 ) = sample means
* ( s_p ) = pooled standard deviation
* ( n_1, n_2 ) = sample sizes

---

## ⚖️ **4. Types of T-Tests**

| Type                              | Use Case                                               | Example                         |
| --------------------------------- | ------------------------------------------------------ | ------------------------------- |
| **One-Sample T-Test**             | Compare sample mean vs known value                     | Is the average height > 170 cm? |
| **Independent Two-Sample T-Test** | Compare means of two independent groups                | Male vs Female scores           |
| **Paired T-Test**                 | Compare means of same group before and after treatment | Weight before vs after diet     |

---

## 🧩 **5. One-Sample T-Test**

Used when comparing **one sample mean** with a **known population mean**.

### 🔹 **Example**

Suppose the average IQ in the population is 100.
You want to test if students from a school have a **different average IQ**.

```r
iq <- c(98, 102, 101, 105, 99, 100, 103, 97, 104)
t.test(iq, mu = 100)
```

### 🔹 **Output**

```
One Sample t-test
t = 0.861, df = 8, p-value = 0.414
alternative hypothesis: true mean is not equal to 100
95 percent confidence interval:  98.38 103.06
sample estimates: mean = 100.72
```

✅ **Interpretation:**

* **p-value = 0.414 > 0.05** → Fail to reject H₀
  ⇒ No significant difference from 100.

---

## 🧩 **6. Independent Two-Sample T-Test**

Used to compare **two independent groups**.

### 🔹 **Example**

```r
group1 <- c(85, 90, 88, 92, 91, 87, 89)
group2 <- c(78, 82, 79, 80, 81, 83, 77)

t.test(group1, group2, var.equal = TRUE)
```

### 🔹 **Output**

```
Two Sample t-test
t = 5.021, df = 12, p-value = 0.0002
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:  6.23 13.49
sample estimates: mean of x = 88.86, mean of y = 80.00
```

✅ **Interpretation:**

* **p-value = 0.0002 < 0.05**
  ⇒ Reject H₀ → significant difference between groups.

---

## 🧩 **7. Paired T-Test**

Used when data comes from **same group** measured **twice** (before & after).

### 🔹 **Example**

```r
before <- c(200, 195, 188, 202, 190)
after  <- c(180, 185, 172, 190, 175)

t.test(before, after, paired = TRUE)
```

### 🔹 **Output**

```
Paired t-test
t = 6.23, df = 4, p-value = 0.003
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:  8.73 24.27
sample estimates: mean difference = 16.5
```

✅ **Interpretation:**

* **p-value = 0.003 < 0.05**
  ⇒ Reject H₀ → significant difference before and after.

---

## 🧮 **8. Interpreting T-Test Results**

| Component               | Meaning                                   |
| ----------------------- | ----------------------------------------- |
| **t**                   | Test statistic (measures difference size) |
| **df**                  | Degrees of freedom (n₁ + n₂ - 2)          |
| **p-value**             | Probability of observing result under H₀  |
| **Confidence Interval** | Range where true difference lies          |
| **Mean of x/y**         | Sample means being compared               |

---

## 📊 **9. Visualization**

You can visualize differences using boxplots:

```r
boxplot(group1, group2,
        names = c("Group 1", "Group 2"),
        col = c("lightblue", "lightgreen"),
        main = "Comparison of Two Groups")
```

---

## 📘 **10. Summary Table**

| Type of T-Test         | Description                          | Function                    |
| ---------------------- | ------------------------------------ | --------------------------- |
| One Sample             | Compare sample mean with known value | `t.test(x, mu=value)`       |
| Independent Two-Sample | Compare two independent groups       | `t.test(x, y)`              |
| Paired                 | Compare same group before/after      | `t.test(x, y, paired=TRUE)` |

---

## 🧠 **11. Key Notes**

* Always check **assumptions**:

  * Data is **normally distributed**
  * Variances are **equal** for independent t-tests
* Use `var.equal=FALSE` if variances are unequal.
* If data is **not normal**, use **Wilcoxon test** instead.

---

## ✅ **Summary**

| Aspect      | Explanation                                                 |
| ----------- | ----------------------------------------------------------- |
| Purpose     | Compare means                                               |
| Statistic   | t-value                                                     |
| p-value     | Determines significance                                     |
| Main types  | One-sample, Independent, Paired                             |
| Example use | Comparing two treatments, two groups, before-after analysis |

---

# **ANOVA (Analysis of Variance) in R**

---

#### **1. Introduction**

* **ANOVA (Analysis of Variance)** is a statistical technique used to compare **means of three or more groups**.
* It determines whether at least one group mean is **significantly different** from others.
* It extends the **t-test**, which compares only two means.

---

#### **2. Basic Idea**

ANOVA analyzes the **variability** of data:

* **Between-group variance:** Variability due to the difference between group means.
* **Within-group variance:** Variability due to random differences within each group.

If between-group variance is much larger than within-group variance → significant difference between group means.

---

#### **3. Hypotheses**

* **Null Hypothesis (H₀):** All group means are equal.
  $$ H_0: \mu_1 = \mu_2 = \mu_3 = \dots = \mu_k $$

* **Alternative Hypothesis (H₁):** At least one group mean is different.
  $$ H_1: \text{At least one } \mu_i \neq \mu_j $$

---

#### **4. Types of ANOVA**

| Type              | Description                                                                 | Example                                                              |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **One-Way ANOVA** | One categorical independent variable and one continuous dependent variable. | Compare test scores of students from 3 different schools.            |
| **Two-Way ANOVA** | Two categorical independent variables.                                      | Compare effect of **gender** and **teaching method** on test scores. |
| **MANOVA**        | Multiple dependent variables.                                               | Compare scores of multiple tests across groups.                      |

---

#### **5. Example: One-Way ANOVA in R**

```r
# Sample Data
group1 <- c(20, 21, 19, 22, 20)
group2 <- c(30, 29, 31, 32, 30)
group3 <- c(25, 27, 26, 24, 25)

# Combine into a data frame
score <- c(group1, group2, group3)
group <- factor(rep(c("A", "B", "C"), each=5))
data <- data.frame(score, group)

# Perform One-Way ANOVA
result <- aov(score ~ group, data = data)

# Summary of the ANOVA
summary(result)
```

**Output Explanation:**

* **Df**: Degrees of freedom.
* **Sum Sq**: Sum of squares (variation).
* **Mean Sq**: Average variation per degree of freedom.
* **F value**: Test statistic.
* **Pr(>F)**: p-value → if < 0.05, reject null hypothesis.

---

#### **6. Post-Hoc Test (Tukey’s HSD)**

If ANOVA is significant, use **Tukey’s HSD** to find which groups differ.

```r
TukeyHSD(result)
```

This shows **pairwise comparison** of group means with confidence intervals and p-values.

---

#### **7. Two-Way ANOVA Example**

```r
# Example Data
data <- data.frame(
  score = c(88, 92, 80, 89, 93, 85, 90, 86, 91, 84, 87, 88),
  gender = factor(rep(c("Male", "Female"), each=6)),
  method = factor(rep(c("A", "B", "A", "B", "A", "B"), 2))
)

# Perform Two-Way ANOVA
result2 <- aov(score ~ gender * method, data=data)

summary(result2)
```

**Interpretation:**

* Tests main effects of **gender** and **method**.
* Tests interaction effect (**gender × method**).

---

#### **8. Assumptions of ANOVA**

1. **Independence** of observations.
2. **Normality**: Data in each group should be approximately normal.
3. **Homogeneity of variance**: All groups have equal variance.

You can check assumptions using:

```r
# Normality test
shapiro.test(residuals(result))

# Equal variance test
bartlett.test(score ~ group, data=data)
```

---

#### **9. Visualization**

```r
boxplot(score ~ group, data=data,
        main="One-Way ANOVA: Group Comparison",
        xlab="Group", ylab="Score", col=c("lightblue","lightgreen","lightpink"))
```

---

#### **10. Summary**

| Concept              | Description                             |
| -------------------- | --------------------------------------- |
| **Purpose**          | Compare means of multiple groups        |
| **Statistical Test** | F-test                                  |
| **p-value < 0.05**   | Reject H₀ → Groups differ significantly |
| **Post-hoc Test**    | Tukey’s HSD                             |
| **Key Assumptions**  | Normality, equal variance, independence |

---

# **Linear Models: Simple Linear Regression in R**

---

#### **1. Introduction**

**Simple Linear Regression (SLR)** is a statistical method used to model the relationship between **two variables**:

* One **independent variable (X)** (also called predictor or feature)
* One **dependent variable (Y)** (also called response or target)

It helps us understand and predict how changes in `X` affect `Y`.

---

#### **2. Equation of Simple Linear Regression**

The model assumes a **linear relationship** between `X` and `Y`:

$$
Y = \beta_0 + \beta_1 X + \epsilon
$$

Where:

* $Y$ = dependent variable (predicted output)
* $X$ = independent variable (input)
* $\beta_0$ = intercept (value of Y when X = 0)
* $\beta_1$ = slope (change in Y for one-unit change in X)
* $\epsilon$ = error term (difference between predicted and actual Y)

---

#### **3. Objective**

To estimate the **best-fitting line** by minimizing the **sum of squared errors (SSE)**:

$$
SSE = \sum (Y_i - \hat{Y_i})^2
$$

where $\hat{Y_i}$ is the predicted value of Y.

---

#### **4. Steps in Simple Linear Regression**

1. Collect data for X and Y.
2. Fit the model using `lm()` function.
3. Examine the model summary.
4. Visualize the regression line.
5. Predict new values.

---

#### **5. Example in R**

```r
# Sample data
x <- c(1, 2, 3, 4, 5, 6)
y <- c(2, 4, 5, 4, 5, 7)

# Create a data frame
data <- data.frame(x, y)

# Fit the linear regression model
model <- lm(y ~ x, data = data)

# Display the model summary
summary(model)
```

**Output Explanation:**

* **Estimate (Intercept)** → Value of β₀
* **Estimate (x)** → Value of β₁
* **R-squared** → Percentage of variance in Y explained by X (ranges 0–1)
* **p-value** → Tests if relationship between X and Y is statistically significant

---

#### **6. Visualization**

```r
# Scatter plot with regression line
plot(data$x, data$y, main="Simple Linear Regression",
     xlab="X", ylab="Y", pch=19, col="blue")
abline(model, col="red", lwd=2)
```

This plots the **best-fitting regression line** in red.

---

#### **7. Predicting New Values**

```r
# Predict new Y values for given X
new_data <- data.frame(x = c(7, 8, 9))
predictions <- predict(model, new_data)
print(predictions)
```

---

#### **8. Diagnostic Plots**

```r
# Check model assumptions
par(mfrow=c(2,2))
plot(model)
```

These plots show:

* **Residuals vs Fitted** → Check for constant variance
* **Normal Q-Q** → Residuals should be approximately normal
* **Scale-Location** → Homoscedasticity
* **Residuals vs Leverage** → Detect influential points

---

#### **9. Interpretation Example**

If the model output is:

```
Coefficients:
(Intercept)   1.5
x             0.9
```

Then the regression equation is:

$$
\hat{Y} = 1.5 + 0.9X
$$

Meaning:

* When X = 0, predicted Y = 1.5
* For every 1 unit increase in X, Y increases by 0.9 units

---

#### **10. Key Metrics**

| Metric             | Meaning                                              |
| ------------------ | ---------------------------------------------------- |
| **R² (R-squared)** | Measures goodness of fit (closer to 1 = better fit)  |
| **Adjusted R²**    | Adjusts R² for number of predictors                  |
| **F-statistic**    | Tests overall significance of model                  |
| **p-value**        | If < 0.05, relationship is statistically significant |

---

#### **11. Assumptions of Linear Regression**

1. **Linearity** – Relationship between X and Y is linear.
2. **Independence** – Observations are independent.
3. **Homoscedasticity** – Constant variance of residuals.
4. **Normality** – Residuals follow a normal distribution.
5. **No Outliers** – No extreme data points influencing the model.

---

#### **12. Summary**

| Step                 | Function/Concept          |
| -------------------- | ------------------------- |
| Fit model            | `lm(y ~ x)`               |
| View summary         | `summary(model)`          |
| Plot regression line | `abline(model)`           |
| Predict new values   | `predict(model, newdata)` |
| Diagnostic check     | `plot(model)`             |

---

# **Multiple Linear Regression in R**

---

#### **1. Introduction**

**Multiple Linear Regression (MLR)** is an extension of **Simple Linear Regression** that models the relationship between **one dependent variable (Y)** and **two or more independent variables (X₁, X₂, X₃, ...)**.

It helps us predict outcomes based on multiple features and understand how each variable contributes to the prediction.

---

#### **2. Equation of Multiple Linear Regression**

The general form of the MLR model is:

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + \epsilon
$$

Where:

* $Y$ = dependent variable
* $X_1, X_2, …, X_n$ = independent variables
* $\beta_0$ = intercept
* $\beta_1, \beta_2, …, \beta_n$ = coefficients (slopes)
* $\epsilon$ = error term

Each coefficient $\beta_i$ represents the **change in Y** when $X_i$ changes by one unit, keeping other variables constant.

---

#### **3. Objective**

The goal of multiple regression is to find the best-fit hyperplane (line in higher dimensions) that minimizes the **sum of squared errors (SSE):**

$$
SSE = \sum (Y_i - \hat{Y_i})^2
$$

---

#### **4. Example Dataset**

Let’s consider a dataset predicting **house prices** based on two factors — `size` (in sqft) and `bedrooms`.

| House | Size (sqft) | Bedrooms | Price (₹ lakhs) |
| ----- | ----------- | -------- | --------------- |
| 1     | 1000        | 2        | 50              |
| 2     | 1500        | 3        | 65              |
| 3     | 1800        | 3        | 80              |
| 4     | 2400        | 4        | 100             |
| 5     | 3000        | 4        | 120             |

---

#### **5. Implementing Multiple Linear Regression in R**

```r
# Sample Data
size <- c(1000, 1500, 1800, 2400, 3000)
bedrooms <- c(2, 3, 3, 4, 4)
price <- c(50, 65, 80, 100, 120)

# Create a DataFrame
data <- data.frame(size, bedrooms, price)

# Fit Multiple Linear Regression Model
model <- lm(price ~ size + bedrooms, data = data)

# Display Model Summary
summary(model)
```

---

#### **6. Example Output Interpretation**

```
Coefficients:
(Intercept)    20.5
size            0.03
bedrooms        5.2
```

**Model Equation:**

$$
\hat{Price} = 20.5 + 0.03 \times Size + 5.2 \times Bedrooms
$$

**Interpretation:**

* Base price (when size = 0 and bedrooms = 0) is ₹20.5 lakhs.
* Every additional square foot adds ₹0.03 lakhs (₹3,000).
* Each additional bedroom increases price by ₹5.2 lakhs, holding size constant.

---

#### **7. Visualization**

You can visualize the relationship between one predictor and the response while holding another constant.

```r
library(ggplot2)

# 2D visualization of one variable
ggplot(data, aes(x = size, y = price, color = factor(bedrooms))) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Multiple Linear Regression",
       x = "House Size (sqft)",
       y = "Price (₹ lakhs)")
```

---

#### **8. Predicting New Values**

```r
# Predicting price for new houses
new_data <- data.frame(size = c(2000, 2800), bedrooms = c(3, 4))
predicted_price <- predict(model, new_data)
print(predicted_price)
```

---

#### **9. Model Evaluation Metrics**

| Metric                 | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| **R-squared (R²)**     | Proportion of variance in Y explained by all X variables.           |
| **Adjusted R-squared** | Adjusted for number of predictors — better for multiple regression. |
| **p-value**            | Tests if each predictor significantly affects Y.                    |
| **F-statistic**        | Tests overall model significance.                                   |
| **Residuals**          | Difference between actual and predicted Y.                          |

---

#### **10. Assumptions of Multiple Linear Regression**

| Assumption               | Explanation                                           |
| ------------------------ | ----------------------------------------------------- |
| **Linearity**            | Relationship between X’s and Y is linear.             |
| **Independence**         | Observations are independent.                         |
| **Homoscedasticity**     | Constant variance of residuals.                       |
| **Normality**            | Residuals are normally distributed.                   |
| **No Multicollinearity** | Predictors are not highly correlated with each other. |

Check **multicollinearity** using Variance Inflation Factor (VIF):

```r
library(car)
vif(model)
```

If **VIF > 5**, it indicates multicollinearity (correlated predictors).

---

#### **11. Diagnostic Plots**

```r
par(mfrow=c(2,2))
plot(model)
```

These include:

* Residuals vs Fitted → checks linearity
* Normal Q-Q → checks normal distribution
* Scale-Location → checks equal variance
* Residuals vs Leverage → identifies influential points

---

#### **12. Summary Table**

| Step              | Function                  | Purpose                               |
| ----------------- | ------------------------- | ------------------------------------- |
| Create Model      | `lm(y ~ x1 + x2, data)`   | Fit regression                        |
| Summary           | `summary(model)`          | Get coefficients, R², p-values        |
| Predict           | `predict(model, newdata)` | Predict Y                             |
| Diagnostics       | `plot(model)`             | Validate assumptions                  |
| Multicollinearity | `vif(model)`              | Detect correlation between predictors |

---

#### **13. Visualization of Relationship**

```
          +---------------------------+
Price (Y) |                          *
          |                     *      
          |               *           
          |        *                  
          | *                        
          +---------------------------+
               Size (X₁) and Bedrooms (X₂)
```

The model finds the **best-fitting plane** that minimizes the error between predicted and actual prices.

---

#### **14. Summary**

✅ Models relationship between **Y and multiple Xs**
✅ Helps in **prediction and feature understanding**
✅ Evaluated using **R², Adjusted R², and p-values**
✅ Must check for **multicollinearity and residual assumptions**

---

# **Logistic Regression in R**

---

#### **1. Introduction**

**Logistic Regression** is a **supervised learning** technique used when the **dependent variable (Y)** is **categorical** (e.g., Yes/No, 0/1, True/False).

Unlike linear regression (which predicts a continuous value), logistic regression predicts the **probability** that an observation belongs to a particular **class**.

---

#### **2. Why Not Linear Regression for Classification?**

Linear regression outputs any real value (−∞ to +∞), but **probabilities** must lie between **0 and 1**.
Logistic regression solves this by using the **logistic (sigmoid) function**.

---

#### **3. Logistic Function (Sigmoid Function)**

The **sigmoid function** maps any real number into a range between 0 and 1:

$$
P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X)}}
$$

Where:

* $P(Y=1|X)$ = probability that event Y = 1 occurs
* $\beta_0$ = intercept
* $\beta_1$ = coefficient of predictor X

The output is interpreted as **probability**, e.g.,
if $P(Y=1|X) = 0.8$, it means there’s an 80% chance of Y being 1.

---

#### **4. Decision Boundary**

To classify:

* If $P(Y=1|X) ≥ 0.5$ → Predict class **1**
* If $P(Y=1|X) < 0.5$ → Predict class **0**

---

#### **5. Logistic Regression Equation**

In log-odds (logit) form:

$$
\log\left(\frac{P}{1 - P}\right) = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n
$$

Where $\frac{P}{1 - P}$ is the **odds** of the event occurring.

---

#### **6. Example: Predicting Student Pass/Fail**

Let’s predict whether a student **passes (1)** or **fails (0)** based on their **study hours**.

| Student | Hours | Pass |
| ------- | ----- | ---- |
| 1       | 2     | 0    |
| 2       | 3     | 0    |
| 3       | 4     | 0    |
| 4       | 5     | 1    |
| 5       | 6     | 1    |
| 6       | 7     | 1    |

---

#### **7. Implementation in R**

```r
# Sample Data
hours <- c(2, 3, 4, 5, 6, 7)
pass <- c(0, 0, 0, 1, 1, 1)

data <- data.frame(hours, pass)

# Fit Logistic Regression Model
model <- glm(pass ~ hours, data = data, family = binomial)

# Display Model Summary
summary(model)
```

---

#### **8. Example Output**

```
Coefficients:
(Intercept)  -6.5
hours         1.3
```

Equation:
$$
\log\left(\frac{P}{1 - P}\right) = -6.5 + 1.3 \times Hours
$$

To get probability:
$$
P = \frac{1}{1 + e^{-(-6.5 + 1.3 \times Hours)}}
$$

---

#### **9. Predicting Outcomes**

```r
# Predict probabilities
predicted_prob <- predict(model, type = "response")

# Display predicted probabilities
print(predicted_prob)

# Classify outcomes based on threshold 0.5
predicted_class <- ifelse(predicted_prob > 0.5, 1, 0)
print(predicted_class)
```

---

#### **10. Visualization**

```r
library(ggplot2)

ggplot(data, aes(x = hours, y = pass)) +
  geom_point(size = 3, color = "blue") +
  stat_smooth(method = "glm", method.args = list(family = "binomial"), col = "red") +
  labs(title = "Logistic Regression: Pass Prediction",
       x = "Study Hours",
       y = "Pass Probability")
```

📊 This will show a **sigmoid curve** that rises steeply around 4–5 hours — indicating higher probability of passing.

---

#### **11. Interpreting the Coefficients**

From model output:

* **Intercept (β₀ = -6.5):** Base log-odds of passing when `hours = 0`
* **Slope (β₁ = 1.3):** Each additional hour increases the log-odds of passing by 1.3

To convert to **odds ratio**:

```r
exp(coef(model))
```

If output = 3.67, it means:
**Each additional study hour multiplies the odds of passing by 3.67×.**

---

#### **12. Model Evaluation**

| Metric               | Function                                     | Meaning                              |
| -------------------- | -------------------------------------------- | ------------------------------------ |
| **Confusion Matrix** | `table(Actual, Predicted)`                   | Compares actual vs predicted         |
| **Accuracy**         | `(TP + TN) / Total`                          | Overall correctness                  |
| **AIC**              | from `summary(model)`                        | Lower = better model                 |
| **ROC Curve**        | `pROC` package                               | Evaluates classification performance |
| **R² (Pseudo)**      | `1 - (model$deviance / model$null.deviance)` | Goodness of fit                      |

Example:

```r
# Confusion Matrix
table(Actual = data$pass, Predicted = predicted_class)

# Pseudo R-squared
1 - (model$deviance / model$null.deviance)
```

---

#### **13. ROC Curve and AUC**

```r
library(pROC)

roc_curve <- roc(data$pass, predicted_prob)
plot(roc_curve, col = "blue", main = "ROC Curve for Logistic Regression")
auc(roc_curve)
```

* **ROC Curve** plots True Positive Rate vs False Positive Rate.
* **AUC (Area Under Curve)** close to 1 indicates strong classification ability.

---

#### **14. Assumptions of Logistic Regression**

| Assumption                     | Description                                             |
| ------------------------------ | ------------------------------------------------------- |
| **Binary/Multiclass Response** | Dependent variable must be categorical.                 |
| **Independence**               | Observations are independent.                           |
| **No Multicollinearity**       | Predictors should not be correlated.                    |
| **Large Sample Size**          | For reliable estimates.                                 |
| **Linearity in Logit**         | Logit of probability is linearly related to predictors. |

---

#### **15. Summary Table**

| Step                | Function                          | Description              |
| ------------------- | --------------------------------- | ------------------------ |
| Fit model           | `glm(y ~ x, family = binomial)`   | Fits logistic regression |
| Predict probability | `predict(model, type="response")` | Gives probabilities      |
| Classify output     | `ifelse(prob>0.5, 1, 0)`          | Converts to 0/1          |
| Evaluate model      | `summary(model)`                  | Get coefficients, AIC    |
| Visualize           | `ggplot2` with `stat_smooth()`    | Sigmoid curve            |

---

#### **16. Visualization Diagram**

```
Pass Probability (Y)
│
│            ●●●●●●●●
│          ●●
│       ●●
│    ●●
│ ●●
│______________________________→ Hours of Study (X)
         2   3   4   5   6   7
```

The red S-shaped **sigmoid curve** shows that as study hours increase, probability of passing rises sharply.

---

#### **17. Key Takeaways**

✅ Logistic regression predicts **probabilities**, not values
✅ Uses **sigmoid function** to map output between 0–1
✅ Evaluated using **accuracy, AIC, ROC-AUC**
✅ Works for **binary classification** problems
✅ Coefficients interpreted in terms of **odds ratio**

---

