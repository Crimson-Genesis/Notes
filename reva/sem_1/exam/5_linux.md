# Linux
# **Unit 3: Linux Basics & Shell Scripting**
# **Linux File System & Directory Structure**  

The **Linux File System (LFS)** organizes files and directories in a structured hierarchy. It follows a **tree-like structure** where everything starts from the **root (/) directory**.  

---

## **📌 1. Structure of the Linux File System**  
Each Linux distribution follows the **Filesystem Hierarchy Standard (FHS)**, which defines common directories and their purposes.

### **🔹 Important Directories in Linux:**  
| **Directory** | **Description** |
|--------------|----------------|
| **`/` (Root)** | The base of the filesystem; everything starts here. |
| **`/bin`** | Essential binary files (e.g., `ls`, `cat`, `cp`). |
| **`/sbin`** | System binaries for admin tasks (e.g., `fdisk`, `shutdown`). |
| **`/etc`** | Configuration files (e.g., `passwd`, `hosts`). |
| **`/home`** | User home directories (`/home/username`). |
| **`/root`** | Home directory of the **root** user. |
| **`/dev`** | Device files (e.g., `/dev/sda` for hard disks). |
| **`/proc`** | Virtual filesystem for process info (e.g., `/proc/cpuinfo`). |
| **`/sys`** | Kernel-related info and hardware details. |
| **`/tmp`** | Temporary files that get deleted after reboot. |
| **`/var`** | Variable files like logs (`/var/log/syslog`). |
| **`/usr`** | User binaries, libraries, and documentation. |
| **`/opt`** | Optional software packages. |
| **`/mnt` & `/media`** | Mount points for external storage. |

---

## **📌 2. Features of Linux File System**  

✅ **Hierarchical Structure** – Files are organized in a tree format under `/`.  
✅ **Everything is a File** – Even devices (e.g., `/dev/sda`) and processes (`/proc/`) are treated as files.  
✅ **Case Sensitivity** – `File.txt` and `file.txt` are different files.  
✅ **Mounting & Unmounting** – External devices must be "mounted" to access them.  
✅ **Access Control** – Uses file permissions (`rwx`) to restrict access.  

---

## **📌 3. File System Types in Linux**  

Linux supports multiple file systems:  

| **File System** | **Description** |
|---------------|----------------|
| **ext4** | Default filesystem for most Linux distros. |
| **XFS** | High-performance journaling filesystem. |
| **Btrfs** | Supports snapshots and advanced storage features. |
| **FAT32/exFAT/NTFS** | Used for USB drives, compatible with Windows. |
| **tmpfs** | Temporary filesystem stored in RAM. |

To check your system's filesystem, use:  
```sh
df -T
```

---

## **📌 4. Common File System Commands**  

| **Command** | **Purpose** |
|------------|------------|
| `ls` | List files in a directory. |
| `cd` | Change directory. |
| `pwd` | Show current directory. |
| `mkdir` | Create a new directory. |
| `rmdir` | Remove an empty directory. |
| `rm -r` | Delete a directory and its contents. |
| `touch` | Create a new empty file. |
| `cp` | Copy files/directories. |
| `mv` | Move/rename files. |
| `find` | Search for files in directories. |
| `df -h` | Show disk space usage. |
| `du -sh` | Show size of a directory. |
| `mount` | Mount a filesystem. |
| `umount` | Unmount a filesystem. |

---

## **📌 Summary**  
✔ The **Linux File System** is structured **hierarchically**, starting from `/`.  
✔ Linux follows the **"everything is a file"** principle.  
✔ **Different directories** have specific purposes, like `/home` for users and `/etc` for configs.  
✔ Common **file systems** include **ext4, XFS, Btrfs, and NTFS**.  
✔ Essential commands like `ls`, `cd`, `rm`, and `mount` help manage files.  

---
# **Essential Linux Commands: File, Directory, Disk Commands**  

In Linux, **commands** are used to perform various tasks like manipulating files, managing directories, and handling disk operations. These commands are executed in the **Terminal** or **Shell**. Here's a detailed explanation of the most commonly used commands related to **files**, **directories**, and **disks**.  

---

## **📌 1. File Commands**  

### **🔹 `touch`**  
**Purpose**: Creates an empty file or updates the timestamp of an existing file.  
**Usage**:  
```sh
touch filename
```

### **🔹 `cat`**  
**Purpose**: Concatenates (displays) file contents. Can also be used to create a file.  
**Usage**:  
```sh
cat filename   # Display content of file
cat > filename # Create/overwrite file with user input
```

### **🔹 `cp`**  
**Purpose**: Copies files or directories.  
**Usage**:  
```sh
cp source_file destination_file   # Copy a file
cp -r source_dir destination_dir   # Copy a directory
```

### **🔹 `mv`**  
**Purpose**: Moves or renames files and directories.  
**Usage**:  
```sh
mv source_file destination_file    # Move or rename a file
mv source_dir destination_dir      # Move or rename a directory
```

### **🔹 `rm`**  
**Purpose**: Removes (deletes) files or directories.  
**Usage**:  
```sh
rm filename             # Delete a file
rm -r directory_name    # Delete a directory and its contents
rm -f filename          # Force delete a file without confirmation
```

---

## **📌 2. Directory Commands**  

### **🔹 `ls`**  
**Purpose**: Lists files and directories.  
**Usage**:  
```sh
ls                 # List files in the current directory
ls -l              # List with detailed information (permissions, owner, etc.)
ls -a              # List all files, including hidden ones (files starting with `.`
ls /path/to/dir    # List contents of a specific directory
```

### **🔹 `cd`**  
**Purpose**: Changes the current directory.  
**Usage**:  
```sh
cd directory_path   # Change to a specific directory
cd ..               # Go up one directory
cd /                # Go to the root directory
cd ~                # Go to the home directory
```

### **🔹 `pwd`**  
**Purpose**: Prints the current working directory.  
**Usage**:  
```sh
pwd   # Show the full path of the current directory
```

### **🔹 `mkdir`**  
**Purpose**: Creates a new directory.  
**Usage**:  
```sh
mkdir new_directory  # Create a new directory
mkdir -p parent_dir/child_dir  # Create a nested directory structure
```

### **🔹 `rmdir`**  
**Purpose**: Removes an empty directory.  
**Usage**:  
```sh
rmdir directory_name  # Remove an empty directory
```

---

## **📌 3. Disk Commands**  

### **🔹 `df`**  
**Purpose**: Displays disk space usage for filesystems.  
**Usage**:  
```sh
df -h      # Display in human-readable format (e.g., MB, GB)
df -T      # Show filesystem types
df /path   # Check disk usage for a specific directory
```

### **🔹 `du`**  
**Purpose**: Displays disk usage of files and directories.  
**Usage**:  
```sh
du -sh directory_name  # Show the size of a directory
du -ah                 # Show size of all files and directories
```

### **🔹 `lsblk`**  
**Purpose**: Lists information about all available block devices.  
**Usage**:  
```sh
lsblk          # List all block devices
lsblk -f       # Display filesystems on devices
```

### **🔹 `fdisk`**  
**Purpose**: Partitions disks (disk partitioning tool).  
**Usage**:  
```sh
fdisk -l        # List partition tables of all disks
fdisk /dev/sda  # Partition a specific disk
```

### **🔹 `mount`**  
**Purpose**: Mounts a filesystem or device.  
**Usage**:  
```sh
mount /dev/sda1 /mnt    # Mount a device to a directory
```

### **🔹 `umount`**  
**Purpose**: Unmounts a filesystem or device.  
**Usage**:  
```sh
umount /mnt     # Unmount a device from a directory
```

---

## **📌 Summary**  
✔ **File Commands** like `touch`, `cat`, `cp`, `mv`, and `rm` are used for basic file manipulation.  
✔ **Directory Commands** such as `ls`, `cd`, `pwd`, `mkdir`, and `rmdir` help manage directories.  
✔ **Disk Commands** such as `df`, `du`, `lsblk`, `fdisk`, `mount`, and `umount` assist in managing disk space and partitions.  

---
# **Process Management (Foreground & Background Processes)**  

A **process** is an executing instance of a program in Linux. Linux provides various ways to manage processes, including running them in **foreground** or **background**, and controlling their execution.

---

## **📌 1. Foreground Processes**  
A foreground process runs **actively in the terminal** and takes user input. The terminal remains **blocked** until the process completes.  

### **🔹 Running a Foreground Process**
When you run a command normally, it runs in the foreground.  
```sh
ping google.com
```
This command will keep running and display output in the terminal until **Ctrl + C** is pressed to stop it.

---

## **📌 2. Background Processes**  
A background process runs **without occupying the terminal**, allowing you to continue using the terminal for other commands.  

### **🔹 Running a Process in the Background**
Use `&` at the end of a command to run it in the background.  
```sh
ping google.com > output.txt &
```
The process runs in the background and gives a **Process ID (PID)**.

### **🔹 Listing Background Jobs**
Check the background jobs running in the shell.  
```sh
jobs
```
It shows active background processes.

### **🔹 Bringing a Background Process to the Foreground**
Use the `fg` command followed by the job number (`%n`).  
```sh
fg %1   # Bring job 1 to the foreground
```

### **🔹 Sending a Foreground Process to the Background**
If a process is already running in the foreground, press **Ctrl + Z** to **pause** it, then use `bg` to resume it in the background.  
```sh
bg %1   # Resume job 1 in the background
```

---

## **📌 3. Process Control Commands**  

### **🔹 Viewing Running Processes**
Use the `ps` command to see active processes.  
```sh
ps aux    # Show all processes with details
```
Or use `top` for a dynamic view.  
```sh
top
```

### **🔹 Killing a Process**
Use `kill` followed by the **Process ID (PID)** to stop a process.  
```sh
kill 1234   # Kill process with PID 1234
kill -9 1234  # Force kill process
```

Use `pkill` to kill by name.  
```sh
pkill firefox  # Kill all Firefox processes
```

---

## **📌 Summary**
✔ **Foreground processes** occupy the terminal until they finish.  
✔ **Background processes** run in the background, allowing continued use of the terminal.  
✔ **Process management commands** like `jobs`, `fg`, `bg`, `kill`, and `ps` help control processes.  

---
# **Linux Permissions: `chmod`, `chown`, `chgrp`, `umask`**  

Linux uses a **permission system** to control access to files and directories. Each file or directory has **three types of permissions** for **three categories of users**.

---

## **📌 1. Understanding File Permissions**  

### **🔹 Categories of Users**
1. **Owner (`u`)** – The user who created the file.  
2. **Group (`g`)** – A group of users who share the same permissions.  
3. **Others (`o`)** – Everyone else.  

### **🔹 Types of Permissions**
| Symbol | Permission | Effect |
|--------|------------|--------|
| `r` (4) | Read | Can view the file contents |
| `w` (2) | Write | Can modify or delete the file |
| `x` (1) | Execute | Can run the file (if it's a script or program) |

### **🔹 Viewing File Permissions**
Use the `ls -l` command to check permissions.  
```sh
ls -l filename
```
Example output:  
```
-rwxr-xr--  1 user group 1234 Mar 31 12:00 myfile.sh
```
- `rwxr-xr--` → **Owner (`rwx`)** can read, write, and execute.  
- **Group (`r-x`)** can read and execute.  
- **Others (`r--`)** can only read.  

---

## **📌 2. Changing Permissions (`chmod`)**  
The `chmod` command modifies file permissions.

### **🔹 Using Symbolic Mode**
Modify permissions using `+` (add), `-` (remove), and `=` (set exact permission).  
```sh
chmod u+x myfile.sh   # Add execute permission for the owner
chmod g-w myfile.sh   # Remove write permission from the group
chmod o=r myfile.sh   # Set read-only for others
```

### **🔹 Using Numeric Mode (Octal)**
Each permission has a numeric value:  
- **r = 4, w = 2, x = 1**  
- Add values to set permissions:  
  - `chmod 755 file` → **rwxr-xr-x** (Owner can do everything, others can read & execute)

Examples:  
```sh
chmod 777 file    # Full permissions for everyone
chmod 644 file    # Owner can read/write, others can only read
chmod 700 file    # Only owner has all permissions
```

---

## **📌 3. Changing Ownership (`chown`, `chgrp`)**  
Linux allows changing file **ownership**.

### **🔹 Changing File Owner (`chown`)**
Change the owner of a file.  
```sh
chown newuser file.txt   # Change owner to 'newuser'
chown -R newuser dir/    # Change owner of all files in 'dir' recursively
```

### **🔹 Changing Group (`chgrp`)**
Change only the group of a file.  
```sh
chgrp newgroup file.txt   # Change group ownership to 'newgroup'
```

### **🔹 Changing Owner and Group Together**
```sh
chown newuser:newgroup file.txt
```

---

## **📌 4. Default Permissions (`umask`)**  
When a new file is created, its default permissions depend on `umask`.

### **🔹 Checking Current `umask`**
```sh
umask
```
Common output: `0022`  
- The last three digits determine **default permission subtraction**.
- **New file default: `666 - umask`**  
- **New directory default: `777 - umask`**  

### **🔹 Setting a `umask`**
```sh
umask 027  # Default removes write permission for group, all permissions for others
```

---

## **📌 Summary**
✔ **`chmod`** → Modify file permissions using symbolic or numeric mode.  
✔ **`chown` & `chgrp`** → Change file ownership and group.  
✔ **`umask`** → Set default file permissions.  

---
# **Shell Basics: Types of Shells, Shell Variables, and Positional Parameters**  

---

## **📌 1. Types of Shells in Linux**  

A **shell** is a command-line interpreter that allows users to interact with the operating system.

### **🔹 Common Shells in Linux**
| Shell | Description | Default in |
|-------|------------|------------|
| **Bash (Bourne Again Shell)** | Most commonly used, supports scripting & history | Linux (default in many distros) |
| **Zsh (Z Shell)** | More features than Bash, better autocomplete | macOS (default), Linux |
| **Ksh (Korn Shell)** | Faster and more scripting features than Bash | UNIX |
| **Tcsh (TENEX C Shell)** | C-like syntax, advanced scripting | BSD systems |
| **Fish (Friendly Interactive Shell)** | User-friendly, auto-suggestions | Linux (optional) |

### **🔹 Checking Available Shells**
```sh
cat /etc/shells
```
This will list installed shells.

### **🔹 Checking Your Current Shell**
```sh
echo $SHELL
```

### **🔹 Switching Shells**
To switch to `zsh`:
```sh
chsh -s /bin/zsh
```
To switch temporarily:
```sh
zsh   # Opens Zsh for this session only
```

---

## **📌 2. Shell Variables**  

Shell variables store data and affect the behavior of the shell.

### **🔹 Types of Shell Variables**
1. **Local Variables** → Only available in the current shell session.  
2. **Environment Variables** → Available to all processes and child shells.  
3. **Special Variables** → Predefined by the shell.

### **🔹 Creating and Using Variables**
```sh
myvar="Hello, Linux!"
echo $myvar   # Output: Hello, Linux!
```

### **🔹 Exporting Environment Variables**
```sh
export PATH=$PATH:/usr/local/bin
```

### **🔹 Viewing All Environment Variables**
```sh
printenv   # Lists all environment variables
```

### **🔹 Unsetting a Variable**
```sh
unset myvar
```

---

## **📌 3. Positional Parameters**  

Positional parameters hold **arguments passed to a script or command**.

### **🔹 Accessing Arguments in a Script**
```sh
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
```
Running:
```sh
bash script.sh apple banana
```
Output:
```
First argument: apple
Second argument: banana
All arguments: apple banana
```

### **🔹 Special Positional Parameters**
| Parameter | Meaning |
|-----------|---------|
| `$0` | Script name |
| `$1, $2, ...` | Arguments passed |
| `$@` | All arguments as separate words |
| `$*` | All arguments as a single string |
| `$$` | Process ID of the script |
| `$?` | Exit status of the last command |

---

## **📌 Summary**
✔ **Types of Shells** → Bash, Zsh, Ksh, Tcsh, Fish  
✔ **Shell Variables** → Local, Environment, Special  
✔ **Positional Parameters** → Used to pass arguments to scripts  

---
# **Test Command & Exit Status in Shell Scripting**  

---

## **📌 1. `test` Command in Shell**  

The `test` command is used to evaluate expressions, mainly for conditional statements in shell scripts.

### **🔹 Basic Syntax**
```sh
test expression
```
or using brackets:
```sh
[ expression ]
```

### **🔹 Common Uses of `test`**
#### ✅ **Checking if a File Exists**
```sh
if [ -e myfile.txt ]; then
    echo "File exists!"
else
    echo "File does not exist!"
fi
```
#### ✅ **Comparing Numbers**
```sh
if [ 5 -gt 3 ]; then
    echo "5 is greater than 3"
fi
```
#### ✅ **String Comparison**
```sh
if [ "hello" = "hello" ]; then
    echo "Strings are equal!"
fi
```

---

## **📌 2. Exit Status in Shell**  

Every command in Linux returns an **exit status** (also called an **exit code**) after execution.

### **🔹 Checking Exit Status**
```sh
echo $?
```
- `0` → Success  
- `1` → General error  
- `2` → Misuse of shell builtins  
- `127` → Command not found  

### **🔹 Example**
```sh
ls /nonexistent_directory
echo $?   # Will return 2 (error)
```

---

## **📌 3. Using Exit Status in Scripts**
```sh
#!/bin/bash
mkdir mydir
if [ $? -eq 0 ]; then
    echo "Directory created successfully!"
else
    echo "Failed to create directory!"
fi
```

---

## **📌 Summary**
✔ **`test` Command** → Used for file checks, number comparison, and string evaluation  
✔ **Exit Status (`$?`)** → Indicates success (`0`) or failure (`non-zero`)  

---

# **Unit 4: Advanced Shell Scripting & System Administration**
# **Control Structures in Shell Scripting**  

Control structures allow decision-making and looping in shell scripts.

---

## **📌 1. `if` Statement**  
Used for conditional execution of commands.  

### **🔹 Syntax**  
```sh
if [ condition ]; then
    commands
elif [ another_condition ]; then
    commands
else
    commands
fi
```

### **🔹 Example**
```sh
#!/bin/bash
echo "Enter a number:"
read num
if [ $num -gt 0 ]; then
    echo "Positive number"
elif [ $num -lt 0 ]; then
    echo "Negative number"
else
    echo "Zero"
fi
```

---

## **📌 2. `case` Statement**  
Used when multiple conditions need to be checked.

### **🔹 Syntax**  
```sh
case $variable in
    pattern1)
        commands;;
    pattern2)
        commands;;
    *)
        default_commands;;
esac
```

### **🔹 Example**  
```sh
#!/bin/bash
echo "Enter a choice (start/stop):"
read choice
case $choice in
    start)
        echo "Starting...";;
    stop)
        echo "Stopping...";;
    *)
        echo "Invalid choice";;
esac
```

---

## **📌 3. `while` Loop**  
Executes commands while a condition is true.

### **🔹 Syntax**  
```sh
while [ condition ]; do
    commands
done
```

### **🔹 Example**  
```sh
#!/bin/bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

## **📌 4. `until` Loop**  
Similar to `while`, but runs until the condition becomes true.

### **🔹 Syntax**  
```sh
until [ condition ]; do
    commands
done
```

### **🔹 Example**
```sh
#!/bin/bash
num=1
until [ $num -gt 5 ]; do
    echo "Number: $num"
    ((num++))
done
```

---

## **📌 5. `for` Loop**  
Iterates over a list of values.

### **🔹 Syntax**  
```sh
for variable in list; do
    commands
done
```

### **🔹 Example**  
```sh
#!/bin/bash
for name in Alice Bob Charlie; do
    echo "Hello, $name!"
done
```

---

## **📌 Summary**  
✔ **`if`** → Decision-making based on conditions  
✔ **`case`** → Multi-condition matching  
✔ **`while`** → Runs while the condition is true  
✔ **`until`** → Runs until the condition becomes true  
✔ **`for`** → Iterates over a list  

---
# **Advanced Shell Scripting (Functions & Arguments)**  

Functions in shell scripts help modularize code, making it reusable and easy to manage. Arguments allow passing values to functions.

---

## **📌 1. Defining and Calling a Function**  
A function is defined using the `function` keyword or simply by writing its name followed by parentheses.

### **🔹 Syntax**
```sh
function function_name {
    commands
}
# OR
function_name() {
    commands
}
```

### **🔹 Example**  
```sh
#!/bin/bash
greet() {
    echo "Hello, Welcome to Shell Scripting!"
}
greet  # Function call
```

---

## **📌 2. Functions with Arguments**  
Functions can take arguments, which are referenced using `$1`, `$2`, etc.

### **🔹 Example**
```sh
#!/bin/bash
sum() {
    result=$(( $1 + $2 ))
    echo "Sum: $result"
}
sum 5 10  # Passing arguments
```

**📌 Explanation:**  
- `$1` → First argument (5)  
- `$2` → Second argument (10)  

---

## **📌 3. Returning Values from Functions**  
A function can return a value using the `return` statement.

### **🔹 Example**
```sh
#!/bin/bash
multiply() {
    result=$(( $1 * $2 ))
    return $result
}
multiply 4 5
echo "Product: $?"  # $? stores the return value
```

📌 **Note:** The return value should be between 0-255 (due to shell limitations). For larger values, use `echo` instead.

---

## **📌 4. Storing Function Output in a Variable**  
Instead of using `return`, we can capture the output using command substitution.

### **🔹 Example**
```sh
#!/bin/bash
divide() {
    echo "$(($1 / $2))"
}
result=$(divide 20 4)
echo "Division: $result"
```

---

## **📌 5. Using Default Values in Functions**  
If arguments are not provided, we can set default values.

### **🔹 Example**
```sh
#!/bin/bash
greet() {
    name=${1:-"User"}  # Default to "User" if no argument is given
    echo "Hello, $name!"
}
greet "Alice"  # Output: Hello, Alice!
greet          # Output: Hello, User!
```

---

## **📌 Summary**  
✔ **Functions** help in modularizing code  
✔ **Arguments** (`$1`, `$2`, etc.) pass values to functions  
✔ **Returning values** using `return` (limited to 0-255) or `echo`  
✔ **Storing function output** using command substitution  
✔ **Setting default values** using `${1:-default_value}`  

---
# **Grep, Sed, and Awk Commands**  

These are powerful text-processing tools in Linux used for searching, replacing, and formatting text in files or streams.

---

## **📌 1. `grep` (Global Regular Expression Print)**
Used for searching patterns in a file.

### **🔹 Syntax**
```sh
grep [options] "pattern" filename
```

### **🔹 Example**
```sh
grep "hello" file.txt
```
**✅ Finds and prints lines containing "hello" in `file.txt`.**  

### **🔹 Common Options**
| Option  | Description |
|---------|------------|
| `-i`    | Case-insensitive search |
| `-v`    | Invert match (show lines NOT matching pattern) |
| `-n`    | Show line numbers |
| `-o`    | Show only matching part of the line |
| `-r`    | Recursively search in directories |

### **🔹 Example with Options**
```sh
grep -i "linux" file.txt  # Case-insensitive search
grep -v "error" logs.txt  # Show lines NOT containing "error"
grep -n "test" file.txt   # Show line numbers
```

---

## **📌 2. `sed` (Stream Editor)**
Used for text manipulation, substitution, deletion, and insertion.

### **🔹 Syntax**
```sh
sed 's/pattern/replacement/' filename
```

### **🔹 Example**
```sh
sed 's/hello/Hi/' file.txt
```
**✅ Replaces the first occurrence of "hello" with "Hi" in each line.**

### **🔹 Common Options**
| Option  | Description |
|---------|------------|
| `-i`    | Edit file in-place |
| `g`     | Replace all occurrences in a line |
| `d`     | Delete lines matching a pattern |
| `p`     | Print modified lines |

### **🔹 Example with Options**
```sh
sed 's/apple/orange/g' fruits.txt  # Replace all occurrences of "apple"
sed '3d' file.txt                  # Delete the 3rd line
sed '/error/d' logs.txt             # Delete lines containing "error"
```

---

## **📌 3. `awk` (Pattern Scanning and Processing)**
Used for processing and analyzing text files, especially column-based data.

### **🔹 Syntax**
```sh
awk 'pattern {action}' filename
```

### **🔹 Example**
```sh
awk '{print $1, $3}' data.txt
```
**✅ Prints the 1st and 3rd columns from `data.txt`.**

### **🔹 Common Features**
| Feature  | Description |
|---------|------------|
| `$1, $2, ...` | Columns in a line |
| `BEGIN {}` | Run before processing file |
| `END {}` | Run after processing file |
| `if` | Conditional statements |

### **🔹 Example with Conditions**
```sh
awk '$3 > 50 {print $1, $3}' marks.txt
```
**✅ Prints the 1st and 3rd columns only if the 3rd column value is greater than 50.**

---

## **📌 Summary**
✔ **`grep`** – Search for patterns in files  
✔ **`sed`** – Edit and modify text in streams/files  
✔ **`awk`** – Extract and process structured data  

---
# **System Administration: User & Group Management**  

User and group management in Linux is essential for maintaining security and access control.  

---

## **📌 1. User Management Commands**  

### **🔹 Add a New User**
```sh
sudo useradd username
```
👉 Creates a new user.  

### **🔹 Set/Change Password**
```sh
sudo passwd username
```
👉 Sets or changes the password for a user.  

### **🔹 Modify User Details**
```sh
sudo usermod -l newname oldname  # Rename user
sudo usermod -d /new/home/dir username  # Change home directory
sudo usermod -aG groupname username  # Add user to a group
```

### **🔹 Delete a User**
```sh
sudo userdel username
sudo userdel -r username  # Remove user and home directory
```

---

## **📌 2. Group Management Commands**  

### **🔹 Add a New Group**
```sh
sudo groupadd groupname
```

### **🔹 Add a User to a Group**
```sh
sudo usermod -aG groupname username
```

### **🔹 Remove a User from a Group**
```sh
sudo gpasswd -d username groupname
```

### **🔹 Change a User’s Primary Group**
```sh
sudo usermod -g groupname username
```

### **🔹 Delete a Group**
```sh
sudo groupdel groupname
```

---

## **📌 3. Viewing User & Group Information**  

### **🔹 View Logged-in Users**
```sh
who
w
```

### **🔹 View All Users**
```sh
cat /etc/passwd
```

### **🔹 View All Groups**
```sh
cat /etc/group
```

### **🔹 Check a User’s Groups**
```sh
groups username
id username
```

---

## **📌 Summary**  

✔ **Users** – Create, modify, delete users  
✔ **Groups** – Organize users for permission management  
✔ **Commands** – `useradd`, `usermod`, `groupadd`, `passwd`, `groups`, `id`  

---
# **Process Control & Job Scheduling (Crontab, At, Batch)**  

Process control and job scheduling in Linux help manage running processes and automate tasks efficiently.  

---

## **📌 1. Process Control**  

### **🔹 View Running Processes**
```sh
ps aux   # List all running processes
top      # Interactive real-time process monitoring
htop     # Advanced interactive process viewer (install if needed)
```

### **🔹 Kill a Process**
```sh
kill PID     # Kill a process by its ID
kill -9 PID  # Forcefully terminate a process
pkill name   # Kill a process by its name
```

### **🔹 Foreground & Background Processes**
```sh
command &     # Run a command in the background
jobs          # List background jobs
fg %1         # Bring job 1 to the foreground
bg %1         # Resume job 1 in the background
```

### **🔹 Process Priority (Nice & Renice)**
```sh
nice -n 10 command  # Start a process with priority 10
renice -n -5 -p PID # Change priority of a running process to -5
```

---

## **📌 2. Job Scheduling**  

### **🔹 Crontab (Recurring Tasks)**  
Crontab schedules periodic tasks at specified times.

#### **📝 Edit Crontab**
```sh
crontab -e
```

#### **⏳ Crontab Format**
```sh
 * * * * * command_to_execute
 ┬ ┬ ┬ ┬ ┬
 │ │ │ │ └─ Day of the Week (0-6, Sunday = 0)
 │ │ │ └── Month (1-12)
 │ │ └─── Day of the Month (1-31)
 │ └──── Hour (0-23)
 └───── Minute (0-59)
```

#### **⏳ Example Jobs**
```sh
0 5 * * * /home/user/backup.sh  # Run backup script daily at 5 AM
*/10 * * * * echo "Hello" >> /tmp/hello.txt  # Run every 10 minutes
```

#### **🔹 List or Remove Cron Jobs**
```sh
crontab -l   # List all cron jobs
crontab -r   # Remove all cron jobs
```

---

### **🔹 At (One-Time Jobs)**
Runs a command once at a scheduled time.

#### **📝 Schedule a Job**
```sh
at 14:30
```
Then type the command and press **Ctrl+D**.

#### **🔹 View & Remove Jobs**
```sh
atq  # List scheduled jobs
atrm job_id  # Remove a job
```

---

### **🔹 Batch (Low-Priority Jobs)**
Runs jobs when system load is low.

#### **📝 Schedule a Batch Job**
```sh
batch
```
Then type the command and press **Ctrl+D**.

---

## **📌 Summary**  

✔ **Process Control** – `ps`, `kill`, `nice`, `jobs`, `fg`, `bg`  
✔ **Recurring Jobs** – `crontab` (Automate daily, weekly, etc.)  
✔ **One-Time Jobs** – `at` (Run once at a specified time)  
✔ **Batch Jobs** – `batch` (Run when system load is low)  

---
# **Inter-Process Communication (IPC)**  

Inter-Process Communication (IPC) allows processes to share data and synchronize their actions. Linux provides several IPC mechanisms:

---

## **📌 1. Pipes (Anonymous & Named Pipes)**
Pipes allow data to flow between processes in a producer-consumer fashion.

### **🔹 Anonymous Pipes (|)**
Used between parent and child processes or between two commands.

```sh
ls -l | grep ".txt"  # Pass output of `ls -l` to `grep`
```

### **🔹 Named Pipes (FIFO)**
Persistent pipes that can be used by unrelated processes.

#### **📝 Create a Named Pipe**
```sh
mkfifo mypipe
```
#### **📌 Use It**
```sh
echo "Hello" > mypipe  # Write to pipe
cat < mypipe           # Read from pipe
```

---

## **📌 2. Message Queues**
Message queues allow processes to send structured messages.

### **🔹 Create & Send a Message**
```c
msgsnd(msgid, &msg, sizeof(msg), 0);
```

### **🔹 Receive a Message**
```c
msgrcv(msgid, &msg, sizeof(msg), 0, 0);
```

### **🔹 Linux Commands**
```sh
ipcs -q   # List message queues
ipcrm -q ID  # Remove a message queue
```

---

## **📌 3. Shared Memory**
Allows multiple processes to share a segment of memory.

### **🔹 Create Shared Memory**
```c
shmid = shmget(IPC_PRIVATE, 1024, IPC_CREAT | 0666);
```

### **🔹 Attach Memory**
```c
char *data = (char*) shmat(shmid, NULL, 0);
```

### **🔹 Detach & Remove**
```c
shmdt(data);  // Detach
shmctl(shmid, IPC_RMID, NULL);  // Remove
```

### **🔹 Linux Commands**
```sh
ipcs -m   # List shared memory segments
ipcrm -m ID  # Remove a shared memory segment
```

---

## **📌 4. Semaphores**
Used for process synchronization.

### **🔹 Create a Semaphore**
```c
semget(IPC_PRIVATE, 1, IPC_CREAT | 0666);
```

### **🔹 Semaphore Wait (P Operation)**
```c
semop(semid, &sem_lock, 1);
```

### **🔹 Semaphore Signal (V Operation)**
```c
semop(semid, &sem_unlock, 1);
```

### **🔹 Linux Commands**
```sh
ipcs -s   # List semaphores
ipcrm -s ID  # Remove a semaphore
```

---

## **📌 Summary**  
✔ **Pipes** – Simple inter-process data flow (`|`, `mkfifo`)  
✔ **Message Queues** – Structured message passing (`msgsnd`, `msgrcv`)  
✔ **Shared Memory** – Fastest IPC (`shmget`, `shmat`)  
✔ **Semaphores** – Synchronization tool (`semget`, `semop`)  

---

