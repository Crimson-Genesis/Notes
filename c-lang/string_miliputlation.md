In C, there are many functions for **string manipulation** and **conversion**. Below is a categorized list, including `strcspn` and similar functions.

---

## **1️⃣ String Manipulation Functions (from `<string.h>`)**

| Function | Description |
|----------|-------------|
| `strlen(s)` | Returns the length of string `s` (excluding `\0`). |
| `strcpy(dest, src)` | Copies `src` into `dest` (make sure `dest` has enough space). |
| `strncpy(dest, src, n)` | Copies **at most** `n` characters from `src` to `dest`. |
| `strcat(dest, src)` | Appends `src` to the end of `dest`. |
| `strncat(dest, src, n)` | Appends at most `n` characters of `src` to `dest`. |
| `strcmp(s1, s2)` | Compares `s1` and `s2`. Returns `0` if they are equal. |
| `strncmp(s1, s2, n)` | Compares the first `n` characters of `s1` and `s2`. |
| `strchr(s, c)` | Returns a pointer to the **first occurrence** of `c` in `s`, or `NULL` if not found. |
| `strrchr(s, c)` | Returns a pointer to the **last occurrence** of `c` in `s`, or `NULL` if not found. |
| `strstr(haystack, needle)` | Returns a pointer to the first occurrence of `needle` in `haystack`, or `NULL` if not found. |
| `strtok(s, delim)` | Splits `s` into tokens using `delim` as a delimiter (modifies `s`). |
| `memcpy(dest, src, n)` | Copies `n` bytes from `src` to `dest` (may cause overlap issues). |
| `memmove(dest, src, n)` | Copies `n` bytes from `src` to `dest`, safe for overlapping memory. |
| `memset(s, c, n)` | Fills the first `n` bytes of `s` with `c`. |

---

## **2️⃣ Specialized String Search Functions**
These help find character positions in strings.

| Function | Description |
|----------|-------------|
| `strcspn(s, reject)` | Returns the index of the **first character in `s` that matches any character in `reject`**. |
| `strspn(s, accept)` | Returns the index of the **first character in `s` that is NOT in `accept`**. |
| `strpbrk(s, accept)` | Returns a pointer to the **first character in `s` that matches any character in `accept`**, or `NULL`. |

### **Example Using `strcspn`, `strspn`, and `strpbrk`**
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "hello123world";
    char numbers[] = "0123456789";

    // Find the first number in the string
    int pos = strcspn(str, numbers);
    printf("First number found at index: %d\n", pos); // Output: 5 (h, e, l, l, o)

    // Find the length of the initial alphabetical sequence
    int length = strspn(str, "abcdefghijklmnopqrstuvwxyz");
    printf("Initial letters length: %d\n", length); // Output: 5 (h, e, l, l, o)

    // Find the first number using strpbrk
    char *firstNumber = strpbrk(str, numbers);
    if (firstNumber)
        printf("First number in string: %c\n", *firstNumber); // Output: '1'

    return 0;
}
```

---

## **3️⃣ String to Number Conversion (from `<stdlib.h>`)**

| Function | Description |
|----------|-------------|
| `atoi(s)` | Converts `s` to an `int`. |
| `atol(s)` | Converts `s` to a `long`. |
| `atof(s)` | Converts `s` to a `double`. |
| `strtol(s, &endptr, base)` | Converts `s` to a `long`, supporting different bases (e.g., base 10, 16). |
| `strtoll(s, &endptr, base)` | Converts `s` to a `long long`. |
| `strtod(s, &endptr)` | Converts `s` to a `double`. |

### **Example of Using `strtol()`**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char str[] = "123abc";
    char *endptr;

    long num = strtol(str, &endptr, 10);

    printf("Number: %ld\n", num);  // Output: 123
    printf("Remaining string: %s\n", endptr);  // Output: abc

    return 0;
}
```

---

## **4️⃣ Number to String Conversion (from `<stdio.h>`)**

| Function | Description |
|----------|-------------|
| `sprintf(str, fmt, ...)` | Converts values to a string (`snprintf` is safer). |
| `snprintf(str, n, fmt, ...)` | Converts values to a string but limits output to `n` characters. |

### **Example Using `sprintf()`**
```c
#include <stdio.h>

int main() {
    char buffer[50];
    int num = 42;

    sprintf(buffer, "The number is %d", num);
    printf("%s\n", buffer);  // Output: The number is 42

    return 0;
}
```

---

## **5️⃣ Miscellaneous Useful Functions**
| Function | Description |
|----------|-------------|
| `toupper(c)` | Converts `c` to uppercase (from `<ctype.h>`). |
| `tolower(c)` | Converts `c` to lowercase. |

### **Example: Convert String to Uppercase**
```c
#include <stdio.h>
#include <ctype.h>

int main() {
    char str[] = "Hello, World!";
    
    for (int i = 0; str[i]; i++) {
        str[i] = toupper(str[i]);
    }

    printf("%s\n", str);  // Output: HELLO, WORLD!

    return 0;
}
```

---

## **🔹 Summary**
### **String Manipulation (`<string.h>`)**
- `strcpy`, `strcat`, `strcmp`, `strchr`, `strstr`, `strcspn`
- `memcpy`, `memmove`, `memset`

### **String Search (`<string.h>`)**
- `strcspn`, `strspn`, `strpbrk`

### **String to Number (`<stdlib.h>`)**
- `atoi`, `strtol`, `strtod`

### **Number to String (`<stdio.h>`)**
- `sprintf`, `snprintf`

### **Character Handling (`<ctype.h>`)**
- `toupper`, `tolower`

---


