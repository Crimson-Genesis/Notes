# 📝 **Detailed Explanation of Regular Expression (Regex) Patterns in Python**
Regular expressions (regex) are powerful tools for pattern matching and text processing. Python’s `re` module allows us to define regex patterns for matching strings in a flexible way.

---

## 🔹 **Basic Regex Syntax**
A regex pattern consists of **metacharacters** and **literals** that define what to match.

| **Pattern** | **Description** | **Example Match** |
|------------|----------------|------------------|
| `abc` | Matches exact characters | `"abc"` in `"123abc456"` |
| `.` | Matches **any** character (except newline `\n` unless `re.DOTALL` is used) | `"a.c"` → Matches `"abc", "adc"` |
| `\` | Escape character to treat special characters as literals | `\.` matches a literal `.` |
| `^` | Matches **start** of string | `^Hello` matches `"Hello world"` but not `"Say Hello"` |
| `$` | Matches **end** of string | `world$` matches `"Hello world"` but not `"worldwide"` |

---

## 🔹 **Character Classes (Character Sets)**
Character classes allow you to match **specific sets of characters**.

| **Pattern** | **Description** | **Example Match** |
|------------|----------------|------------------|
| `[abc]` | Matches **any one** of `a`, `b`, or `c` | `"apple"` → Matches `"a"` |
| `[^abc]` | Matches any character **except** `a`, `b`, or `c` | `"xyz"` → Matches `"x", "y", "z"` |
| `[0-9]` | Matches any **digit** (same as `\d`) | `"123abc"` → Matches `"1", "2", "3"` |
| `[a-z]` | Matches any **lowercase letter** | `"hello"` → Matches `"h", "e", "l", "o"` |
| `[A-Z]` | Matches any **uppercase letter** | `"Python"` → Matches `"P"` |
| `[a-zA-Z0-9_]` | Matches **alphanumeric characters** (same as `\w`) | `"Hello123"` → Matches `"H", "e", "l", "l", "o", "1", "2", "3"` |

---

## 🔹 **Predefined Character Classes**
These are **shortcuts** for common character classes.

| **Pattern** | **Equivalent To** | **Description** |
|------------|----------------|----------------|
| `\d` | `[0-9]` | Matches **digits** (0-9) |
| `\D` | `[^0-9]` | Matches **non-digits** |
| `\w` | `[a-zA-Z0-9_]` | Matches **alphanumeric characters & underscore** |
| `\W` | `[^a-zA-Z0-9_]` | Matches **non-word characters** |
| `\s` | `[ \t\n\r\f\v]` | Matches **whitespace (spaces, tabs, newlines)** |
| `\S` | `[^\s]` | Matches **non-whitespace characters** |

#### Example:
```python
import re
text = "Hello 123!"
print(re.findall(r"\d", text))   # ['1', '2', '3']
print(re.findall(r"\D", text))   # ['H', 'e', 'l', 'l', 'o', ' ']
print(re.findall(r"\w", text))   # ['H', 'e', 'l', 'l', 'o', '1', '2', '3']
print(re.findall(r"\s", text))   # [' ']
```

---

## 🔹 **Quantifiers**
Quantifiers **control how many times** a pattern should repeat.

| **Pattern** | **Description** | **Example Match** |
|------------|----------------|------------------|
| `a*` | Matches **0 or more** occurrences of `a` | `"aaa", "", "abc"` |
| `a+` | Matches **1 or more** occurrences of `a` | `"aaa", "a"` (but **not** `""`) |
| `a?` | Matches **0 or 1** occurrences of `a` (optional) | `"a", ""` |
| `a{3}` | Matches **exactly 3** occurrences of `a` | `"aaa"` |
| `a{2,5}` | Matches **between 2 and 5** occurrences of `a` | `"aa", "aaaaa"` |
| `a{,3}` | Matches **up to 3** occurrences | `"", "a", "aa", "aaa"` |

#### Example:
```python
text = "Hellooo"
print(re.findall(r"o+", text))   # ['ooo']
print(re.findall(r"o{2,4}", text))  # ['ooo']
```

---

## 🔹 **Grouping and Capturing (Parentheses `()` )**
Grouping allows you to:
1. **Capture** parts of a match.
2. Apply **quantifiers** to an entire section.

| **Pattern** | **Description** |
|------------|----------------|
| `(abc)` | Captures **"abc"** as a group |
| `(ab)+` | Matches **one or more** `"ab"` |
| `(a|b)` | Matches `"a"` or `"b"` |

#### Example:
```python
text = "PythonPythonPython"
match = re.search(r"(Python){2}", text)
print(match.group())  # PythonPython
```

---

## 🔹 **Non-Capturing Groups `(?:...)`**
Non-capturing groups `(?:...)` allow you to use parentheses **without capturing** the match.

#### Example:
```python
text = "apple apple orange apple"
pattern = r"(?:apple|orange)+"
print(re.findall(pattern, text))  # ['apple', 'apple', 'orange', 'apple']
```

---

## 🔹 **Lookahead and Lookbehind (Advanced Patterns)**
Lookaheads and lookbehinds **assert** conditions without consuming characters.

### **Lookahead (`?=` and `?!`)**
| **Pattern** | **Description** |
|------------|----------------|
| `a(?=b)` | Matches `a` **only if** followed by `b` |
| `a(?!b)` | Matches `a` **only if not** followed by `b` |

#### Example:
```python
text = "apple123 banana456"
print(re.findall(r"\w+(?=\d+)", text))  # ['apple', 'banana']
```

---

### **Lookbehind (`?<=` and `?<!`)**
| **Pattern** | **Description** |
|------------|----------------|
| `(?<=b)a` | Matches `a` **only if** preceded by `b` |
| `(?<!b)a` | Matches `a` **only if not** preceded by `b` |

#### Example:
```python
text = "123apple 456banana"
print(re.findall(r"(?<=\d{3})\w+", text))  # ['apple', 'banana']
```

---

## 🔹 **Example: Extracting Emails**
```python
text = "Emails: test@example.com, user123@mail.net"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(pattern, text)
print(emails)
```
✅ **Output:**
```
['test@example.com', 'user123@mail.net']
```

---

## 🔹 **Summary Table of Regex Components**

| **Feature**  | **Pattern Example** | **Description** |
|-------------|----------------|----------------|
| **Anchors** | `^abc$` | Start (`^`) and end (`$`) match |
| **Character Sets** | `[a-z0-9]` | Matches one of the listed characters |
| **Quantifiers** | `a{2,5}` | Matches 2 to 5 occurrences |
| **Groups** | `(abc|xyz)` | Matches `"abc"` or `"xyz"` |
| **Lookaheads** | `foo(?=bar)` | `"foo"` only if followed by `"bar"` |
| **Lookbehinds** | `(?<=bar)foo` | `"foo"` only if preceded by `"bar"` |

---
## 📝 **Detailed Explanation of Regular Expressions (Regex) in Python**

Regular expressions (regex) allow you to match patterns in text. Python's `re` module provides powerful tools for working with regex.

---

# 🔹 **Regex Pattern Components**
Regex patterns are made up of **literals**, **metacharacters**, and **special sequences** that define what to match.

---

## 🔥 **1. Anchors (`^` and `$`)**
Anchors specify **positions** in a string rather than characters.

| **Pattern** | **Description** | **Example Match** |
|------------|----------------|------------------|
| `^abc` | Matches `"abc"` **at the start** of the string | `"abc123"` ✅, `"123abc"` ❌ |
| `xyz$` | Matches `"xyz"` **at the end** of the string | `"hello xyz"` ✅, `"xyz hello"` ❌ |
| `^$` | Matches an **empty string** | `""` |

#### Example:
```python
import re
text = "Hello World"
print(re.findall(r"^Hello", text))  # ['Hello']
print(re.findall(r"World$", text))  # ['World']
```

---

## 🔥 **2. Dot (`.`) – Any Character**
- `.` matches **any single character** **except newline** (`\n`).
- If `re.DOTALL` is enabled, `.` matches **newlines** too.

| **Pattern** | **Example Match** |
|------------|------------------|
| `a.c` | `"abc"`, `"axc"`, `"a9c"` ✅ |
| `..` | `"ab"`, `"cd"`, `"a!"` ✅ |

#### Example:
```python
print(re.findall(r"a.c", "abc axc a9c"))  # ['abc', 'axc', 'a9c']
print(re.findall(r"a.c", "ac abc"))  # ['abc']
```

---

## 🔥 **3. Character Classes (`[]`)**
Character classes allow matching **specific sets of characters**.

| **Pattern** | **Matches** |
|------------|------------|
| `[aeiou]` | Any **vowel** |
| `[A-Z]` | Any **uppercase letter** |
| `[0-9]` | Any **digit** |
| `[a-zA-Z]` | Any **letter** |
| `[^abc]` | Any **character except** `a`, `b`, or `c` |

#### Example:
```python
print(re.findall(r"[aeiou]", "Python is awesome"))  # ['o', 'i', 'a', 'e', 'o', 'e']
print(re.findall(r"[^aeiou]", "Python is awesome"))  # Consonants and spaces
```

---

## 🔥 **4. Predefined Character Classes**
Python provides **shorthand notations** for common character groups.

| **Pattern** | **Equivalent To** | **Matches** |
|------------|----------------|------------|
| `\d` | `[0-9]` | **Digits** (0-9) |
| `\D` | `[^0-9]` | **Non-digits** |
| `\w` | `[a-zA-Z0-9_]` | **Alphanumeric + underscore** |
| `\W` | `[^a-zA-Z0-9_]` | **Non-alphanumeric** |
| `\s` | `[ \t\n\r\f\v]` | **Whitespace** |
| `\S` | `[^\s]` | **Non-whitespace** |

#### Example:
```python
print(re.findall(r"\d", "Room 202 has 3 beds"))  # ['2', '0', '2', '3']
print(re.findall(r"\w+", "Python_Regex!!"))  # ['Python_Regex']
print(re.findall(r"\s", "Hello World!"))  # [' ']
```

---

## 🔥 **5. Quantifiers**
Quantifiers define **how many times** a pattern should occur.

| **Pattern** | **Description** | **Example Match** |
|------------|----------------|------------------|
| `a*` | **0 or more** `a` | `"aaa"`, `""`, `"b"` |
| `a+` | **1 or more** `a` | `"aaa"`, `"a"` |
| `a?` | **0 or 1** `a` (optional) | `"a"`, `""` |
| `a{3}` | **Exactly 3** `a` | `"aaa"` |
| `a{2,5}` | **Between 2 and 5** `a` | `"aa"`, `"aaaa"` |

#### Example:
```python
print(re.findall(r"a+", "aa abc aaaa"))  # ['aa', 'a', 'aaaa']
print(re.findall(r"ba{2,4}", "ba baaa baaaa baaaaa"))  # ['baaa', 'baaaa']
```

---

## 🔥 **6. Grouping with Parentheses `()`**
Grouping allows:
1. **Capturing** parts of the match.
2. **Applying quantifiers** to entire sections.

| **Pattern** | **Description** |
|------------|----------------|
| `(abc)` | Captures `"abc"` |
| `(ab)+` | Matches `"ab"`, `"abab"`, `"ababab"` |

#### Example:
```python
text = "PythonPythonPython"
match = re.search(r"(Python){2}", text)
print(match.group())  # PythonPython
```

---

## 🔥 **7. Non-Capturing Groups `(?:...)`**
Use `(?:...)` if you **don't need to capture** a match.

#### Example:
```python
text = "apple apple orange apple"
pattern = r"(?:apple|orange)+"
print(re.findall(pattern, text))  # ['apple', 'apple', 'orange', 'apple']
```

---

## 🔥 **8. Lookaheads and Lookbehinds**
Lookaheads and lookbehinds **assert conditions** without consuming characters.

### **Lookahead (`?=` and `?!`)**
| **Pattern** | **Description** |
|------------|----------------|
| `a(?=b)` | Matches `a` **only if followed by** `b` |
| `a(?!b)` | Matches `a` **only if NOT followed by** `b` |

#### Example:
```python
text = "apple123 banana456"
print(re.findall(r"\w+(?=\d+)", text))  # ['apple', 'banana']
```

---

### **Lookbehind (`?<=` and `?<!`)**
| **Pattern** | **Description** |
|------------|----------------|
| `(?<=b)a` | Matches `a` **only if preceded by** `b` |
| `(?<!b)a` | Matches `a` **only if NOT preceded by** `b` |

#### Example:
```python
text = "123apple 456banana"
print(re.findall(r"(?<=\d{3})\w+", text))  # ['apple', 'banana']
```

---

## 🔥 **9. Substitution with `re.sub()`**
Replaces **matched text** with a replacement string.

#### Example:
```python
text = "I love cats. Cats are cute!"
new_text = re.sub(r"cats", "dogs", text, flags=re.IGNORECASE)
print(new_text)  # I love dogs. Dogs are cute!
```

---

## 🔥 **10. Extracting Emails**
```python
text = "Emails: test@example.com, user123@mail.net"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(pattern, text)
print(emails)
```
✅ **Output:**
```
['test@example.com', 'user123@mail.net']
```

---

## 🔥 **11. Extracting URLs**
```python
text = "Visit https://example.com or http://google.com"
pattern = r"https?://[a-zA-Z0-9.-]+"
urls = re.findall(pattern, text)
print(urls)
```
✅ **Output:**
```
['https://example.com', 'http://google.com']
```

---
