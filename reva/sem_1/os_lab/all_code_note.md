### **Part A**

#### 1. Count the number of characters in a given string
```bash
#!/bin/bash
read -p "Enter a string: " str
echo "Length: ${#str}"
```
**Output:**
```
Enter a string: hello
Length: 5
```

---

#### 2. Find the factorial of a given number
```bash
#!/bin/bash
read -p "Enter a number: " n
fact=1
for (( i=1; i<=n; i++ ))
do
  fact=$((fact * i))
done
echo "Factorial: $fact"
```
**Output:**
```
Enter a number: 5
Factorial: 120
```

---

#### 3. Count vowels and consonants in a string
```bash
#!/bin/bash
read -p "Enter a string: " str
v=0
c=0
for (( i=0; i<${#str}; i++ )); do
  ch="${str:$i:1}"
  case "$ch" in
    [aeiouAEIOU]) ((v++)) ;;
    [a-zA-Z]) ((c++)) ;;
  esac
done
echo "Vowels: $v, Consonants: $c"
```
**Output:**
```
Enter a string: Hello
Vowels: 2, Consonants: 3
```

---

#### 4. Print all prime numbers between m and n
```bash
#!/bin/bash
read -p "Enter m: " m
read -p "Enter n: " n
for (( i=m; i<=n; i++ )); do
  prime=1
  for (( j=2; j*j<=i; j++ )); do
    if (( i % j == 0 )); then prime=0; break; fi
  done
  (( i > 1 && prime )) && echo "$i"
done
```
**Output:**
```
Enter m: 10
Enter n: 20
11
13
17
19
```

---

#### 5. Check if a string is a palindrome
```bash
#!/bin/bash
read -p "Enter a string: " str
rev=$(echo "$str" | rev)
[[ "$str" == "$rev" ]] && echo "Palindrome" || echo "Not a palindrome"
```
**Output:**
```
Enter a string: madam
Palindrome
```

---

#### 6. Generate the Fibonacci series
```bash
#!/bin/bash
read -p "Enter number of terms: " n
a=0
b=1
echo -n "$a $b"
for (( i=2; i<n; i++ )); do
  c=$((a + b))
  echo -n " $c"
  a=$b
  b=$c
done
echo
```
**Output:**
```
Enter number of terms: 7
0 1 1 2 3 5 8
```

---

#### 7. Find the sum of a series of n numbers
```bash
#!/bin/bash
read -p "Enter numbers separated by space: " -a nums
sum=0
for i in "${nums[@]}"; do
  sum=$((sum + i))
done
echo "Sum: $sum"
```
**Output:**
```
Enter numbers separated by space: 5 10 15
Sum: 30
```

---

#### 8. Find max and min from a list of n numbers
```bash
#!/bin/bash
read -p "Enter numbers: " -a arr
max=${arr[0]}
min=${arr[0]}
for n in "${arr[@]}"; do
  (( n > max )) && max=$n
  (( n < min )) && min=$n
done
echo "Max: $max, Min: $min"
```
**Output:**
```
Enter numbers: 4 7 1 9
Max: 9, Min: 1
```

---

#### 9. Perform basic arithmetic operations
```bash
#!/bin/bash
read -p "Enter num1: " a
read -p "Enter num2: " b
echo "Add: $((a + b))"
echo "Sub: $((a - b))"
echo "Mul: $((a * b))"
echo "Div: $((a / b))"
```
**Output:**
```
Enter num1: 8
Enter num2: 2
Add: 10
Sub: 6
Mul: 16
Div: 4
```

---

#### 10. Find reverse of a number
```bash
#!/bin/bash
read -p "Enter number: " n
rev=0
while (( n > 0 )); do
  r=$((n % 10))
  rev=$((rev * 10 + r))
  n=$((n / 10))
done
echo "Reverse: $rev"
```
**Output:**
```
Enter number: 1234
Reverse: 4321
```

---

### **Part B**

#### 1. Print arguments in reverse order
```bash
#!/bin/bash
for (( i=$#; i>0; i-- )); do
  echo "${!i}"
done
```
**Run example:**
```bash
$ ./script.sh one two three
three
two
one
```

---

#### 2. Compare permissions of two files
```bash
#!/bin/bash
perm1=$(stat -c %A "$1" 2>/dev/null)
perm2=$(stat -c %A "$2" 2>/dev/null)

if [[ "$perm1" == "$perm2" ]]; then
  echo "Common permissions: $perm1"
else
  echo "$1: $perm1"
  echo "$2: $perm2"
fi
```
**Output:**
```
$ ./script.sh file1.txt file2.txt
Common permissions: -rw-r--r--
```

---

#### 3. Script to read a file name and show properties
```bash
#!/bin/bash
read -p "Enter file name: " f
[[ -e "$f" ]] && ls -l "$f" || echo "File does not exist"
```
**Output:**
```
Enter file name: test.txt
-rw-r--r-- 1 user user 24 Apr 4 15:20 test.txt
```

---

#### 4. Convert files to uppercase
```bash
#!/bin/bash
for file in "$@"; do
  if [[ -f $file ]]; then
    tr 'a-z' 'A-Z' < "$file"
  else
    echo "$file not found"
  fi
done
```
**Output:**
```
$ ./script.sh notes.txt
THIS IS A SAMPLE FILE.
```

---

#### 5. Display file creation time or error
```bash
#!/bin/bash
file=$1
if [[ -e "$file" ]]; then
  stat "$file" | grep -i "Birth" || echo "Birth time not available"
else
  echo "File not found"
fi
```
**Output:**
```
$ ./script.sh report.txt
Birth: 2025-04-01 14:22:33.123456789
```

---

#### 6. Display current month calendar with current date as `*` or `**`
```bash
#!/bin/bash
day=$(date +%-d)
cal | sed "s/\b$day\b/${#day}==1 && echo '*'$day || echo '**'$day/'/e"
```
**Output (if today is April 4):**
```
     April 2025
Su Mo Tu We Th Fr Sa
       1  2  3 *4  5
 6  7  8  9 10 11 12
...
```

---

#### 7. Find the smallest of 3 numbers
```bash
#!/bin/bash
read -p "Enter 3 numbers: " a b c
min=$a
(( b < min )) && min=$b
(( c < min )) && min=$c
echo "Smallest: $min"
```
**Output:**
```
Enter 3 numbers: 10 5 8
Smallest: 5
```

---

#### 8. Sum numbers passed as arguments
```bash
#!/bin/bash
sum=0
for n in "$@"; do
  sum=$((sum + n))
done
echo "Sum: $sum"
```
**Output:**
```
$ ./script.sh 10 20 30
Sum: 60
```

---

#### 9. Greet user based on login time
```bash
#!/bin/bash
hour=$(date +%H)
if (( hour < 12 )); then
  echo "Good Morning"
elif (( hour < 17 )); then
  echo "Good Afternoon"
else
  echo "Good Evening"
fi
```
**Output (if time is 15:00):**
```
Good Afternoon
```

---

#### 10. Count words from file1 in other files
```bash
#!/bin/bash
main=$1
shift
for word in $(tr ' ' '\n' < "$main" | sort | uniq); do
  count=0
  for file in "$@"; do
    wc=$(grep -o "\b$word\b" "$file" | wc -l)
    count=$((count + wc))
  done
  echo "$word: $count"
done
```
**Output:**
```
$ ./script.sh file1.txt file2.txt file3.txt
hello: 3
world: 5
```

---
