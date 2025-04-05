# Operating System and Linux  

---

# Unit -I  
- Introduction: Batch Systems, Multiprogramming and Time Sharing, Parallel, Distributed and real time Systems, Operating System Structures, Components & Services, System calls,.   
- Process Management: Process Concept, Process Scheduling, Threads, Inter process communication, CPU Scheduling Criteria, Scheduling algorithm, Multiple Processor Scheduling,. The Critical Section Problem, Synchronization hardware, Semaphores, Classical problems of synchronization   

---

### **1. Batch Systems**

#### **Definition:**
Batch systems are one of the earliest types of operating systems. They do not interact directly with the computer user. Instead, users prepare their job on offline devices like punch cards and submit them to the computer operator.

#### **Working:**
- Jobs are collected in batches.
- Each batch is processed without user interaction.
- After execution, the output is collected and returned to the user.

#### **Features:**
- No direct interaction between user and system during execution.
- Jobs with similar needs are batched together and executed in sequence.
- Efficient in resource utilization, especially for large-scale repetitive tasks.

#### **Advantages:**
- Increased CPU utilization.
- Reduced setup time between jobs.
- Suitable for long and repetitive processing tasks.

#### **Disadvantages:**
- No real-time processing.
- Difficult to debug.
- Turnaround time is high due to offline job submission and processing.

---
### **2. Multiprogramming and Time Sharing Systems**

---

### **Multiprogramming**

#### **Definition:**
Multiprogramming is a technique where multiple programs are loaded into memory and the CPU switches between them to improve utilization.

#### **Goal:**
To keep the CPU busy at all times by executing another process when the current process is waiting for I/O.

#### **How It Works:**
- Multiple jobs are kept in memory.
- The OS picks one job and begins execution.
- When that job needs I/O, the CPU switches to another job.
- This cycle continues, increasing CPU utilization.

#### **Requirements:**
- **Job scheduling:** To select the job to execute next.
- **Memory management:** To allocate memory for multiple jobs.
- **CPU scheduling:** To manage which job gets CPU time.

#### **Advantages:**
- Better resource utilization.
- Reduced CPU idle time.
- Increased system throughput.

#### **Disadvantages:**
- Complex memory management.
- Complicated CPU scheduling.

---

### **Time Sharing**

#### **Definition:**
Time Sharing (or multitasking) is an extension of multiprogramming where multiple users can interact with a system simultaneously through terminals.

#### **How It Works:**
- CPU time is divided into time slices.
- Each user/process gets a small slice of CPU time in rotation.
- Rapid switching gives the illusion of parallel execution.

#### **Key Concepts:**
- **Time slice/quantum:** Small unit of CPU time allocated to each task.
- **Context switching:** Saving and restoring the state of a process during switching.

#### **Advantages:**
- Interactive use of the system.
- Fair allocation of CPU to all users.
- Quick response time.

#### **Disadvantages:**
- High overhead due to context switching.
- More complex OS design.

---
### **3. Parallel, Distributed, and Real-Time Systems**

---

## **Parallel Operating Systems**

### **Definition:**
A parallel operating system is designed to manage systems that use multiple CPUs or cores simultaneously to perform computation more efficiently.

### **Key Concepts:**

- **Tightly Coupled Systems:** Processors share memory and the clock.
- **Shared Memory:** All processors access the same memory space.
- **Symmetric Multiprocessing (SMP):** Each processor runs an identical copy of the OS and communicates via shared memory.
- **Asymmetric Multiprocessing (AMP):** One processor is the master, controlling the system; others are slaves.

### **Advantages:**

- High performance and faster execution.
- Efficient utilization of CPU cores.
- Can process large computations like simulations, rendering, etc.

### **Challenges:**

- Complex synchronization.
- Memory management becomes harder due to concurrency.
- Data consistency issues.

---

## **Distributed Operating Systems**

### **Definition:**
A distributed OS manages a collection of independent computers (nodes) and makes them appear to the users as a single coherent system.

### **Characteristics:**

- **Loosely Coupled:** Each node has its own local memory and processor.
- **Communication via Network:** Nodes communicate using messages.
- **Resource Sharing:** Enables sharing of files, printers, databases, etc.

### **Examples:**
- Amoeba, Mach, and some Linux-based clusters.

### **Advantages:**

- Resource Sharing: Use of remote hardware/software resources.
- Scalability: Easy to add more nodes.
- Reliability: Failure of one node doesn't bring down the entire system.

### **Challenges:**

- Network latency and failures.
- Security across nodes.
- Complex scheduling and synchronization.

---

## **Real-Time Operating Systems (RTOS)**

### **Definition:**
A real-time OS is designed to process data and respond within a guaranteed time frame. It is commonly used in embedded and mission-critical systems.

### **Types of Real-Time Systems:**

1. **Hard Real-Time Systems:**
   - Must meet strict timing constraints.
   - Failure to meet deadlines causes catastrophic failure.
   - Example: Airbag systems in cars, pacemakers.

2. **Soft Real-Time Systems:**
   - Deadlines are important but not absolute.
   - Occasional missed deadlines are tolerable.
   - Example: Online streaming, gaming systems.

### **Features:**

- **Deterministic behavior:** Predictable response times.
- **Prioritized scheduling:** Tasks with higher priority are executed first.
- **Minimal interrupt latency.**
- **Concurrency handling** for managing multiple real-time tasks.

### **Applications:**

- Aerospace (missile control systems)
- Industrial control (robotics, PLCs)
- Automotive (braking systems)
- Medical devices (life-support systems)

---
### **4. Operating System Structures, Components & Services**

---

## **Operating System Structure**

The structure of an operating system defines how its components interact and how it is organized internally. Several structural models exist:

---

### **1. Monolithic Structure**

- **Description**: Entire OS is a single large program running in a single address space.
- **All OS functions** (like file system, memory management, device drivers) are part of the kernel.
- **Examples**: UNIX, MS-DOS

**Advantages**:
- Fast and efficient (low overhead).
- Simpler implementation.

**Disadvantages**:
- Difficult to debug or extend.
- Less modular; changing one component might affect others.

---

### **2. Layered Structure**

- OS is divided into a hierarchy of layers.
- **Each layer** depends on services from the lower layers and offers services to upper layers.

**Example Layers**:
1. Hardware
2. CPU Scheduling
3. Memory Management
4. File System
5. User Interface

**Advantages**:
- Modular and easy to debug.
- Easier maintenance.

**Disadvantages**:
- Overhead due to layer-by-layer communication.

---

### **3. Microkernel Structure**

- Only essential functions (like IPC, scheduling) are in the kernel.
- Other services run in **user space** (as system processes).

**Examples**: QNX, Minix, newer versions of macOS

**Advantages**:
- Increased security and stability.
- Easy to extend or replace components.

**Disadvantages**:
- Slightly slower due to user-kernel communication.

---

### **4. Modular Structure**

- Modern hybrid approach where OS is built using loadable modules.
- **Each module is independent**, providing specific functionality (e.g., device drivers, file systems).

**Example**: Linux Kernel

**Advantages**:
- Flexibility and scalability.
- Easy to update or load/unload modules at runtime.

---

## **Operating System Components**

1. **Process Management** – Handles creation, scheduling, termination of processes.
2. **Memory Management** – Manages RAM, allocation/deallocation, and swapping.
3. **File System** – Manages file creation, deletion, reading/writing, and directory structure.
4. **Device Management** – Manages communication with I/O devices.
5. **Security & Protection** – Ensures user authentication, file access permissions.
6. **Networking** – Provides networking protocols, communication between devices.
7. **Command Interpreter** – Interface to take commands from the user (shell).

---

## **Operating System Services**

### **1. User Services**
- User Interface (CLI/GUI)
- Program execution
- I/O operations
- File system manipulation
- Communication between processes
- Error detection and handling

### **2. System Services**
- Resource allocation
- Accounting (tracking resource usage)
- Protection and security

---

**Summary Table:**

| **Component**           | **Role**                                |
|------------------------|------------------------------------------|
| Process Manager         | Handles creation/scheduling of processes |
| Memory Manager          | Allocates/deallocates memory             |
| File System             | Manages file storage and retrieval       |
| Device Manager          | Interfaces with hardware devices         |
| Security & Protection   | Ensures data and access control          |

---
### **5. System Calls**

---

**Definition**:  
System calls are the **interface between user-level programs and the operating system**. They provide a way for programs to request services from the OS kernel.

When a program wants to perform an operation like reading a file or creating a process, it doesn’t do it directly — instead, it **calls a system call**, which switches control to the kernel.

---

## **Types of System Calls**

1. **Process Control**
   - `fork()` – Create a new process
   - `exit()` – Terminate a process
   - `wait()` – Wait for a process to finish
   - `exec()` – Replace a process image with a new one

2. **File Management**
   - `open()`, `read()`, `write()`, `close()`
   - `create()`, `delete()`
   - `lseek()` – Move read/write pointer
   - `chmod()` – Change permissions

3. **Device Management**
   - `ioctl()` – Device-specific operations
   - `read()`, `write()` – Common device I/O
   - `close()`

4. **Information Maintenance**
   - `getpid()` – Get process ID
   - `alarm()` – Set an alarm clock
   - `sleep()` – Pause the process

5. **Communication**
   - `pipe()` – Create a pipe
   - `shmget()`, `shmat()` – Shared memory
   - `msgget()`, `msgsnd()` – Message queues
   - `send()`, `recv()` – Network messages

---

## **How System Calls Work**

1. **User Program Request**: A program issues a system call (e.g., `read()`).
2. **Trap to Kernel**: The CPU switches from **user mode to kernel mode** using a software interrupt or trap.
3. **Execution in Kernel**: The requested service (e.g., reading from a file) is performed by the OS.
4. **Return to User**: Control is returned to the user program, often with the result or error code.

---

## **Example: Read System Call in C**

```c
#include <unistd.h>
#include <fcntl.h>

int main() {
    char buffer[100];
    int fd = open("sample.txt", O_RDONLY);
    read(fd, buffer, 100);
    close(fd);
    return 0;
}
```

Here, `open()`, `read()`, and `close()` are system calls.

---

## **Modes of Operation**

- **User Mode**: Limited access to system resources.
- **Kernel Mode**: Full access to all hardware and memory — where system calls run.

**System calls switch from user mode to kernel mode.**

---

**Note**: System calls provide **security and abstraction**. User programs don’t directly access hardware; they request it through controlled interfaces.

---
### **6. Process Management**

---

#### **Process Concept**

A **process** is a program in execution. It is the basic unit of work in a system. A process needs resources like CPU time, memory, files, and I/O devices to perform its task.

**Process vs. Program:**
- **Program**: Passive (just code stored on disk).
- **Process**: Active (code + resources + execution state).

---

#### **Process State**

Each process can be in one of the following states:

1. **New** – Process is being created.
2. **Ready** – Waiting to be assigned to the CPU.
3. **Running** – Instructions are being executed.
4. **Waiting (Blocked)** – Waiting for some event (like I/O).
5. **Terminated** – Process has finished execution.

---

#### **Process Control Block (PCB)**

The OS keeps all information about a process in a data structure called the **PCB**.

**Contents of PCB:**
- Process ID
- Process State
- Program Counter
- CPU Registers
- Memory Limits
- Open Files
- Accounting Info

---

#### **Process Operations**

1. **Process Creation**  
   A process can create other processes using `fork()` in Unix/Linux. The parent and child may run independently.

2. **Process Termination**  
   A process may be terminated by:
   - Completion
   - Error
   - Killed by another process (e.g., `kill()`)

3. **Process Hierarchy**  
   Processes may have **parent-child** relationships forming a tree (like `init` spawning others in Linux).

---

#### **Context Switch**

When the CPU switches from one process to another, the OS saves the state of the old process and loads the state of the new one. This is called a **context switch**.

**Steps in Context Switch:**
1. Save PCB of current process.
2. Load PCB of the next process.
3. Update CPU registers and program counter.

---

**Context switching is essential but costly** as it requires time and can reduce CPU efficiency.

---
### **7. Process Scheduling**

---

#### **What is Process Scheduling?**

**Process scheduling** is the activity of selecting a process from the ready queue and allocating the CPU to it. It's a crucial part of the **CPU Scheduler** in an operating system.

The **goal** of scheduling is to optimize CPU utilization, response time, throughput, waiting time, and fairness among processes.

---

#### **Scheduling Queues in the System**

- **Job Queue** – All processes in the system.
- **Ready Queue** – Processes that are loaded in memory and waiting for the CPU.
- **Device Queues** – Processes waiting for I/O devices.

Processes move between queues depending on their state (e.g., I/O waiting, CPU execution, etc.).

---

#### **Schedulers**

1. **Long-term scheduler (Job scheduler)**  
   - Decides which jobs are to be admitted to the system for processing.  
   - Controls degree of multiprogramming (number of processes in memory).  
   - Less frequent than short-term scheduler.

2. **Short-term scheduler (CPU scheduler)**  
   - Selects one process from the ready queue and allocates CPU.  
   - Invoked frequently (e.g., every few milliseconds).

3. **Medium-term scheduler (Swapper)**  
   - Removes processes from memory to reduce degree of multiprogramming.  
   - Swaps them back later.

---

#### **Preemptive vs Non-Preemptive Scheduling**

- **Non-Preemptive**: Once a process gets the CPU, it runs until it finishes or blocks.
- **Preemptive**: The CPU can be taken away (preempted) from a process for another.

**Preemptive is more complex** but allows better response times for interactive systems.

---

#### **Context Switch in Scheduling**

Every time a process is scheduled out and another is scheduled in, a **context switch** occurs, involving saving the current process state and loading the new one.

---
### **8. Threads**

---

#### **What is a Thread?**

A **thread** is the smallest unit of CPU execution within a process. A single process can have **multiple threads** that share the same memory space but run independently.

- **Process**: Heavyweight, has its own memory and resources.
- **Thread**: Lightweight, shares memory and resources of the process it belongs to.

Each thread has its **own:**
- Program counter
- Stack
- Registers
- State (Running, Ready, Blocked)

But **shares:**
- Code segment
- Data segment
- Heap
- Open files

---

#### **Why Use Threads?**

- Increased **responsiveness** (UI threads stay active).
- Improved **performance** on multi-core systems.
- **Resource sharing** is easier within the same process.
- **Economy**: Creating a new thread is cheaper than creating a new process.
- Better **utilization of multiprocessor architectures**.

---

#### **Types of Threads**

1. **User-level Threads (ULTs):**
   - Managed by user-level libraries.
   - Faster to create/manage.
   - Entire process blocks if one thread blocks (no kernel awareness).

2. **Kernel-level Threads (KLTs):**
   - Managed directly by the OS kernel.
   - Can utilize multiprocessors better.
   - Slower due to kernel overhead.

3. **Hybrid Model:**
   - Combines advantages of ULT and KLT.
   - User threads mapped to kernel threads (many-to-many model).

---

#### **Multithreading Models**

1. **Many-to-One:**
   - Many user threads mapped to a single kernel thread.
   - Efficient, but can’t run threads in parallel on multiprocessors.

2. **One-to-One:**
   - Each user thread maps to a separate kernel thread.
   - Allows parallelism but is resource-intensive.

3. **Many-to-Many:**
   - Multiple user threads mapped to a smaller or equal number of kernel threads.
   - Best balance of concurrency and resource usage.

---

#### **Thread Libraries**

- **POSIX Pthreads** (Unix, Linux)
- **Windows Threads**
- **Java Threads** (JVM level)

---

#### **Multithreaded Process Example:**

**Web Browser**:
- One thread for rendering
- One for network calls
- One for user input
- One for JavaScript engine

All sharing the same memory but working concurrently.

---
### **9. Interprocess Communication (IPC)**

---

#### **What is IPC?**

**Interprocess Communication (IPC)** allows **processes to communicate** and synchronize their actions without sharing the same memory space.

Processes often need to:
- Exchange data
- Coordinate actions
- Share resources without conflict

---

#### **Why IPC is Needed**

- To **share information** among processes (e.g., client-server communication)
- To **avoid race conditions** and maintain **data consistency**
- For **synchronization** (especially in multitasking/multiprocessing systems)

---

#### **IPC Mechanisms**

##### 1. **Shared Memory**
- Two or more processes map a portion of memory into their address spaces.
- Fastest form of IPC.
- Requires **synchronization mechanisms** like semaphores/mutexes.

**Steps:**
- OS allocates a shared segment.
- Processes attach to the segment.
- They read/write from the shared space.

**Example (Linux):** `shmget()`, `shmat()`, `shmdt()`, `shmctl()`

---

##### 2. **Message Passing**
- Processes communicate by **sending and receiving messages** via the kernel.
- Easier to implement but slower than shared memory.
- No direct memory access; kernel acts as a medium.

**Two types:**
- **Direct Communication**: Processes name each other explicitly.
- **Indirect Communication**: Messages sent through **mailboxes** or **ports**.

**Example (Linux):** `msgget()`, `msgsnd()`, `msgrcv()`, `msgctl()`

---

##### 3. **Pipes**

###### a. **Unnamed Pipes**  
- Simple, used for communication between **related processes** (parent-child).
- Data flows in one direction.

```bash
$ ls | sort
```

###### b. **Named Pipes (FIFOs)**  
- Exists as a **file** in the filesystem.
- Can be used by **unrelated processes**.

```c
mkfifo("mypipe", 0666);
```

---

##### 4. **Sockets**
- Allows communication between processes on **different systems** (network communication).
- Used in client-server models (e.g., HTTP, FTP).

**Types:**
- **Stream Sockets (TCP)**
- **Datagram Sockets (UDP)**

---

##### 5. **Signals**
- Used to notify a process that an event occurred.
- Basic, one-way communication.

```c
kill(pid, SIGINT);  // send SIGINT to a process
```

---

##### 6. **Semaphores (for Synchronization)**
- Protects shared resources by controlling access.
- Commonly used with shared memory.

---

#### **Comparison Table**

| Method         | Speed   | Complexity | Used for             |
|----------------|---------|------------|----------------------|
| Shared Memory  | High    | High       | Fast data exchange   |
| Message Passing| Medium  | Medium     | Simple communication |
| Pipes/FIFOs    | Medium  | Low        | Sequential comm.     |
| Sockets        | Medium  | High       | Network communication|
| Signals        | Low     | Very Low   | Event notification   |

---
### **10. CPU Scheduling Criteria**

---

CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it. To determine the **efficiency and fairness** of a scheduling algorithm, we use a set of **criteria**:

---

#### **1. CPU Utilization**
- **Definition**: Percentage of time the CPU is actively working.
- **Goal**: Maximize CPU usage. In real systems, it should range between **40% (light load)** to **90% (heavy load)**.
  
---

#### **2. Throughput**
- **Definition**: Number of processes completed per unit of time.
- **Goal**: Maximize it.
  
Example:
- If 10 processes complete in 5 seconds → Throughput = 2 processes/second

---

#### **3. Turnaround Time**
- **Definition**: Total time taken from **process submission to completion**.

Formula:
```text
Turnaround Time = Completion Time - Arrival Time
```

- Includes waiting, execution, I/O time, etc.
- **Goal**: Minimize it.

---

#### **4. Waiting Time**
- **Definition**: Time a process spends in the **ready queue**, waiting to be assigned to the CPU.

Formula:
```text
Waiting Time = Turnaround Time - CPU Burst Time
```

- **Goal**: Minimize average waiting time across all processes.

---

#### **5. Response Time**
- **Definition**: Time from **submission of a request** until the **first response** is produced (not completion).

- Important in **interactive systems** where immediate feedback is expected.
- **Goal**: Minimize it.

---

#### **6. Fairness**
- **Definition**: Every process should get a **fair share of the CPU**.
- A good scheduler ensures **no starvation** (where a process never gets CPU).

---

### **Summary Table**

| Criterion         | Description                             | Goal        |
|------------------|-----------------------------------------|-------------|
| CPU Utilization   | % of time CPU is busy                    | Maximize    |
| Throughput        | # of completed processes/time            | Maximize    |
| Turnaround Time   | Completion - Arrival time                | Minimize    |
| Waiting Time      | Time in ready queue                      | Minimize    |
| Response Time     | Time to first CPU response               | Minimize    |
| Fairness          | Equal treatment for all processes        | Ensure No Starvation |

---
### **11. CPU Scheduling Algorithms**

---

CPU Scheduling Algorithms are techniques used by the OS to decide **which process gets the CPU**. Each algorithm uses different policies to improve criteria like waiting time, response time, or throughput.

---

### **1. First-Come, First-Served (FCFS)**

- **Non-preemptive** algorithm.
- Processes are scheduled in the order they arrive.
  
**Advantages**:
- Simple to implement.

**Disadvantages**:
- Long waiting times for short processes (convoy effect).
  
**Example**:  
If processes P1, P2, P3 have burst times 24, 3, and 3:

```
Gantt Chart: | P1 | P2 | P3 |
Waiting Times: P1 = 0, P2 = 24, P3 = 27
Avg WT = (0+24+27)/3 = 17
```

---

### **2. Shortest Job Next (SJN) / Shortest Job First (SJF)**

- Picks the process with the **shortest burst time**.
- **Non-preemptive**.
  
**Advantages**:
- Optimal in terms of **minimum average waiting time**.

**Disadvantages**:
- Difficult to predict burst time.
- May cause **starvation**.

---

### **3. Shortest Remaining Time First (SRTF)**

- **Preemptive** version of SJF.
- If a new process arrives with a **shorter remaining time**, the current process is preempted.

**More responsive**, but still risks starvation for long processes.

---

### **4. Round Robin (RR)**

- **Preemptive**.
- Each process gets a **time slice/quantum** (e.g., 5ms).
- After the quantum expires, process is moved to the end of the queue.

**Advantages**:
- Good for **time-sharing** systems.
- Improves **response time**.

**Disadvantages**:
- Too short quantum → many context switches.
- Too long quantum → behaves like FCFS.

---

### **5. Priority Scheduling**

- Each process is assigned a **priority**.
- CPU is allocated to the highest-priority process.

**Types**:
- **Preemptive**: preempts lower priority.
- **Non-preemptive**: waits until CPU is free.

**Disadvantages**:
- Risk of **starvation** for low-priority processes.

**Solution**: Aging – increase the priority of waiting processes.

---

### **6. Multilevel Queue Scheduling**

- Multiple queues (foreground, background) with different **priority levels**.
- Each queue can use a different algorithm (e.g., RR for foreground, FCFS for background).

**Processes don’t move between queues.**

---

### **7. Multilevel Feedback Queue**

- Similar to multilevel queue, but **processes can move between queues** based on their behavior and aging.
- More flexible and fair.

---

### **Summary Table**

| Algorithm          | Preemptive | Fairness | Starvation Risk | Notes                           |
|-------------------|------------|----------|------------------|---------------------------------|
| FCFS              | No         | Low      | Yes              | Simple, poor avg waiting time   |
| SJF               | No         | Low      | Yes              | Optimal WT, hard to implement   |
| SRTF              | Yes        | Low      | Yes              | Best avg WT, needs burst time   |
| Round Robin       | Yes        | High     | No               | Good for interactive systems    |
| Priority          | Optional   | Low      | Yes              | Use aging to fix starvation     |
| Multilevel Queue  | Optional   | Depends  | Yes              | Fixed queues                    |
| Multilevel Feedback| Yes       | High     | No               | Dynamic & flexible              |

---
### **12. Multiple Processor Scheduling**

---

In systems with **more than one processor**, the OS must schedule processes efficiently across all processors to maximize **CPU utilization** and **throughput** while minimizing **response time**, **waiting time**, and **load imbalance**.

---

### **Types of Multiprocessor Systems**

1. **Symmetric Multiprocessing (SMP)**  
   - Each processor runs a **copy of the OS**.
   - All processors share **memory** and **I/O** devices.
   - Most common design in modern systems.
   - Example: All CPUs are equal and pick from the ready queue.

2. **Asymmetric Multiprocessing (AMP)**  
   - One processor is the **master**, the rest are **slaves**.
   - Master assigns tasks; slaves only run user code.
   - Simpler to implement but less efficient.

---

### **Processor Affinity**

- When a process prefers or is **bound to a specific CPU**.
- Reduces **cache misses** and improves performance.

**Types**:
- **Soft Affinity**: Process prefers a CPU but can move.
- **Hard Affinity**: OS guarantees a process will run only on a specific CPU.

---

### **Load Balancing**

- Distributes workload evenly across all CPUs to avoid some being idle while others are overloaded.

**Types**:
1. **Push Migration**: Periodically checks and pushes processes to less loaded CPUs.
2. **Pull Migration**: Idle CPUs try to pull processes from busier CPUs.

---

### **Multicore Scheduling**

- Each **core** in a processor may be scheduled independently.
- Issues include:
  - **Cache sharing**
  - **Resource contention**
  - Coordinated scheduling to reduce overhead

---

### **Real-time Multiprocessor Scheduling**

- Ensures **time-bound processes** meet their deadlines.
- More complex than normal scheduling because of:
  - Priority inversion
  - Shared resource contention
  - Deadline enforcement across cores

---

### **Key Challenges in Multiprocessor Scheduling**

- Avoiding **race conditions** in shared structures.
- Ensuring **fairness** across CPUs.
- Reducing **context switching** overhead.
- Optimizing for **energy consumption**.

---
### **13. The Critical Section Problem**

---

In multiprogramming systems, **concurrent processes** often share resources such as variables, files, and databases. If these processes access shared resources **without coordination**, it can lead to **data inconsistency** or corruption. This gives rise to the **Critical Section Problem**.

---

### **What is a Critical Section?**

A **critical section** is a part of a process where the process **accesses shared resources**, such as shared variables, files, or data structures.

**Problem**: If two or more processes are in their critical sections **at the same time**, it can cause data inconsistency.

---

### **Requirements for a Solution**

Any solution to the critical section problem must satisfy **three conditions**:

1. **Mutual Exclusion**:  
   - Only one process can be in the critical section at any time.

2. **Progress**:  
   - If no process is in the critical section, and some processes wish to enter it, one of them should be allowed to proceed without unnecessary delay.

3. **Bounded Waiting**:  
   - A process must not wait indefinitely to enter its critical section; there should be a bound on the number of times other processes are allowed to enter before the waiting process does.

---

### **Structure of a Typical Process with a Critical Section**

```c
do {
   // Entry Section
   // Critical Section
   // Exit Section
   // Remainder Section
} while (true);
```

- **Entry Section**: Code that checks and allows entry into the critical section.
- **Critical Section**: Code that accesses shared resources.
- **Exit Section**: Code that signals exit from the critical section.
- **Remainder Section**: Code that does not deal with shared resources.

---

### **Approaches to Handle Critical Section Problem**

1. **Software-based solutions**  
   - Algorithms like **Peterson’s Algorithm**, **Dekker’s Algorithm**, etc.

2. **Hardware-based solutions**  
   - Use of special **CPU instructions** like `TestAndSet`, `Swap`, or `CompareAndSwap`.

3. **Operating System-based solutions**  
   - Use of **semaphores**, **monitors**, and **mutex locks**.

---

### **Example: Peterson’s Algorithm** (for 2 processes)

```c
// Shared variables
boolean flag[2];
int turn;

// Process 0
flag[0] = true;
turn = 1;
while (flag[1] && turn == 1);
   // Critical Section
flag[0] = false;
```

Peterson’s Algorithm ensures:
- Mutual Exclusion
- Progress
- Bounded Waiting

---
### **14. Synchronization Hardware**

---

To ensure mutual exclusion in critical sections, operating systems can use **hardware-supported solutions** that provide **atomic** (indivisible) instructions. These are low-level synchronization mechanisms provided by the CPU to avoid race conditions.

---

### **Why Hardware Support is Needed**

Software-only solutions (like Peterson's) are:
- Difficult to generalize for more than 2 processes
- Inefficient on modern multiprocessor systems

**Hardware instructions**, on the other hand:
- Are **atomic** by nature
- Execute without interruption
- Are suitable for **multiprocessor** and **multi-core** environments

---

### **Common Hardware Synchronization Instructions**

#### 1. **Test-And-Set (TAS)**

A hardware instruction that **tests and sets** a value atomically.

```c
boolean TestAndSet(boolean *target) {
    boolean rv = *target;
    *target = true;
    return rv;
}
```

- If `*target` is false, it sets it to true and returns false.
- If `*target` is already true, it returns true.
- Used to implement a **spinlock** (busy-wait lock).

**Example Usage**:
```c
while (TestAndSet(&lock)); // busy-wait
// critical section
lock = false;
```

---

#### 2. **Compare-And-Swap (CAS)**

Compares the contents of a memory location to a given value and, only if they match, modifies the memory location.

```c
int CompareAndSwap(int *reg, int expected, int new_val) {
    int old_val = *reg;
    if (*reg == expected)
        *reg = new_val;
    return old_val;
}
```

Used for:
- Lock implementation
- Lock-free data structures

---

#### 3. **Swap Instruction**

Atomically swaps the values of two variables.

```c
void Swap(boolean *a, boolean *b) {
    boolean temp = *a;
    *a = *b;
    *b = temp;
}
```

---

### **Spinlocks**

Locks implemented using hardware instructions (like TAS or CAS) where a process **spins (busy-waits)** while waiting for the lock to become available.

**Problem**: Wastes CPU cycles during wait  
**Use-case**: Suitable only when wait time is very short

---

### **Advantages of Hardware Synchronization**

- Fast and low-level
- Atomic: Cannot be interrupted
- Effective for simple lock implementation

---

### **Disadvantages**

- Busy-waiting wastes CPU cycles
- Not suitable for all environments
- Can lead to **priority inversion** in real-time systems

---
### **15. Semaphores**

---

A **semaphore** is a powerful synchronization tool used to control access to shared resources in a concurrent system such as a multitasking operating system.

It was introduced by **Edsger Dijkstra** in 1965 and is widely used for solving critical section problems and process synchronization.

---

### **Types of Semaphores**

1. **Binary Semaphore (Mutex)**:
   - Can take only two values: 0 or 1
   - Works like a lock: if it’s 1, it's available; if 0, it's locked

2. **Counting Semaphore**:
   - Can take non-negative integer values
   - Useful for managing a finite number of resources (e.g., 5 printers)

---

### **Basic Operations on Semaphore**

Semaphores use two atomic operations:

#### **1. wait() / P (Proberen/Test)**
Decreases the value of the semaphore by 1  
If the value becomes negative, the process is blocked.

```c
wait(S) {
    while(S <= 0); // busy wait
    S = S - 1;
}
```

#### **2. signal() / V (Verhogen/Increment)**
Increases the value of the semaphore by 1  
If there are blocked processes, one of them is unblocked.

```c
signal(S) {
    S = S + 1;
}
```

---

### **Semaphore Example: Critical Section**

```c
Semaphore S = 1;

Process A:
    wait(S);
    // critical section
    signal(S);

Process B:
    wait(S);
    // critical section
    signal(S);
```

Here, only one process can enter the critical section at a time, preventing race conditions.

---

### **Real-World Use Cases**

- Resource management (e.g., printer, memory)
- Controlling access to critical sections
- Implementing producer-consumer, readers-writers problems

---

### **Drawbacks of Semaphores**

- **Deadlocks**: Improper use can cause all processes to wait indefinitely
- **Starvation**: Some processes may never get a chance if not prioritized
- **Complexity**: Hard to debug and maintain in large systems

---
### **16. Classical Problems of Synchronization**

These are standard synchronization problems used to understand and test inter-process communication mechanisms like semaphores and monitors.

---

### **1. The Bounded-Buffer (Producer-Consumer) Problem**

#### **Problem Statement:**
- A **producer** creates items and places them into a buffer.
- A **consumer** removes items from the buffer.
- The buffer has a limited size.

#### **Constraints:**
- Producer must wait if the buffer is full.
- Consumer must wait if the buffer is empty.

#### **Solution Using Semaphores:**
```c
Semaphore empty = n; // number of empty slots
Semaphore full = 0;  // number of filled slots
Semaphore mutex = 1; // binary semaphore for mutual exclusion

Producer:
  wait(empty);
  wait(mutex);
  // Add item to buffer
  signal(mutex);
  signal(full);

Consumer:
  wait(full);
  wait(mutex);
  // Remove item from buffer
  signal(mutex);
  signal(empty);
```

---

### **2. The Readers-Writers Problem**

#### **Problem Statement:**
- A shared database is accessed by multiple **readers** and **writers**.
- Multiple readers can read simultaneously.
- Only one writer can write at a time.
- No reader should read while a writer is writing.

#### **Solution Idea:**
- Use a reader count to keep track.
- Use semaphores to manage access and synchronization.

---

### **3. The Dining Philosophers Problem**

#### **Problem Statement:**
- Five philosophers sit around a table.
- Each has a plate of food and a fork on either side.
- They need **two forks** to eat.

#### **Challenge:**
- Avoid **deadlock** and **starvation**.

#### **Simple Semaphore Solution:**
```c
Semaphore fork[5] = {1, 1, 1, 1, 1};

Philosopher i:
  wait(fork[i]);
  wait(fork[(i+1)%5]);
  // Eat
  signal(fork[i]);
  signal(fork[(i+1)%5]);
```

To prevent deadlock, a common technique is to make one philosopher pick up the right fork first, breaking the circular wait.

---

### **4. The Sleeping Barber Problem**

#### **Problem Statement:**
- A barber shop with one barber, one barber chair, and n waiting chairs.
- If no customer, barber sleeps.
- If a customer arrives and all chairs are full, they leave.

#### **Challenge:**
- Manage customer arrivals, barber sleep/wake, and queue management.

---

These classical problems are essential for understanding **synchronization**, **deadlocks**, and **concurrency control**.

---

# Unit -II  
- Dead locks: system model, Characterization, Dead lock prevention, avoidance and detection, Recovery from dead lock.   
- Memory Management: Logical and Physical address space, Swapping, Contiguous allocation, Paging, Segmentation, Segmentation with paging, Virtual memory -Demand paging and its performance, Page replacement algorithms, Allocation of frames, Thrashing.  

---

### **1. Deadlocks**  
#### **1.1 System Model**  

A *deadlock* is a situation where a group of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

To understand deadlocks, we must first grasp the **system model** under which such scenarios can occur:

##### **Key Components of the System Model:**
- **Resources:** These can be CPU cycles, memory space, I/O devices (printers, disk drives, etc.).
- **Resource Types:** Each type may have several instances (e.g., a printer may have two identical units).
- **Processes:** Each process may request or release resources.

##### **Resource Allocation Behavior:**
1. **Request:** A process requests a resource. If it is available, it is allocated. If not, the process must wait.
2. **Use:** The process uses the resource.
3. **Release:** After using the resource, the process releases it.

##### **Model Assumptions:**
- Resources are allocated in a fixed manner (one at a time).
- Resources cannot be forcibly taken away (non-preemptive).
- A resource can be requested multiple times, but must be released explicitly.

##### **Resource Allocation Graph (RAG):**
A **graphical model** that represents how resources and processes are related:
- **Processes:** Represented as circles.
- **Resources:** Represented as squares.
- **Edges:**
  - *Request Edge (P → R)*: Process P is requesting resource R.
  - *Assignment Edge (R → P)*: Resource R is allocated to Process P.

**Deadlock Detection via RAG:**
- **No Cycle:** No deadlock.
- **Cycle Exists:**
  - If there’s one instance per resource type → **Deadlock exists.**
  - If multiple instances per type → **Cycle may or may not indicate a deadlock.**

---
### **1.2 Deadlock Characterization**

To understand when and why deadlocks happen, we must examine the **necessary conditions** for a deadlock to occur, collectively known as **Coffman’s Conditions**. All **four conditions must hold simultaneously** for a deadlock to occur.

---

#### **1. Mutual Exclusion**
- At least one resource must be held in a non-shareable mode.
- That is, only one process can use the resource at any one time.
- If another process requests that resource, it must wait until the resource is released.

> Example: A printer cannot be shared between two processes at the same time.

---

#### **2. Hold and Wait**
- A process is holding at least one resource and is waiting to acquire additional resources held by other processes.
- It does **not release** the resources it already holds.

> Example: Process P1 holds a scanner and waits for a printer, while process P2 holds the printer and waits for the scanner.

---

#### **3. No Preemption**
- Resources **cannot be forcibly removed** from a process holding them.
- They must be released voluntarily by the process.

> Example: You cannot forcefully take memory from a process without it freeing it on its own.

---

#### **4. Circular Wait**
- A set of processes are waiting for each other in a **circular chain**:
  - P1 waits for a resource held by P2,
  - P2 waits for a resource held by P3,
  - ..., and
  - Pn waits for a resource held by P1.

> Example: A closed loop where each process is waiting for a resource that the next process in the chain holds.

---

### **Deadlock Summary with Diagram:**

**Deadlock occurs when:**

- All 4 conditions hold,
- The system is in a circular wait state,
- No process can proceed or release its resource.

> Visuals like Resource Allocation Graphs are used to represent and detect such states.

---
### **1.3 Deadlock Prevention**

Deadlock prevention involves **designing the system in such a way** that **at least one of the four necessary conditions for deadlock never holds**, thus **ensuring that deadlocks are impossible**.

Let’s look at how each of the **Coffman Conditions** can be violated (i.e., avoided):

---

#### **1. Prevent Mutual Exclusion**
- Allow resources to be shared among multiple processes.
- However, **not feasible for all resources**, like printers or tape drives.
  
> **Drawback**: Not practical for non-shareable resources.

---

#### **2. Prevent Hold and Wait**
- Require processes to **request all required resources at once**, before execution begins.
- If all resources are available, the process is allocated and allowed to proceed. If not, it waits without holding any.

> **Pros**: Eliminates the wait-for graph, thus no circular wait.
>  
> **Cons**: Leads to **low resource utilization** and **starvation**, as processes may block access unnecessarily.

---

#### **3. Prevent No Preemption**
- If a process holding some resources requests another that is not immediately available, **all resources it holds are preempted** (forcibly taken away).
- Later, the process may try again.

> **Used in**: Systems where **resources can be saved and restored** easily, like CPU registers or memory pages.
>  
> **Cons**: Difficult to implement for resources like files or printers.

---

#### **4. Prevent Circular Wait**
- Impose a **total ordering** of all resource types and require that each process requests resources in an **increasing order** of enumeration.
  
> Example: If you number resources as R1 < R2 < R3, a process can request R1 and R2, but not R2 and then R1.

> **Effect**: Eliminates circular wait by removing the possibility of a closed chain of processes each waiting for a resource.

---

### **Summary Table:**

| Condition            | Prevention Technique                                | Issues                        |
|----------------------|-----------------------------------------------------|-------------------------------|
| Mutual Exclusion     | Make resources sharable                             | Not feasible for all resources |
| Hold and Wait        | Request all resources at once                       | Low utilization, starvation   |
| No Preemption        | Preempt resources if request is denied              | Not always practical          |
| Circular Wait        | Impose total resource ordering                      | Complex to manage             |

---
### **1.4 Deadlock Avoidance**

**Deadlock avoidance** is a **dynamic approach** that requires the operating system to make decisions **during runtime**, ensuring the system never enters an unsafe state that could lead to a deadlock.

It differs from **deadlock prevention**, which eliminates one or more necessary conditions **statically**.

---

### **Key Concepts:**

#### **1. Safe State:**
- A state is **safe** if the system can allocate resources to each process in some order and still **avoid deadlock**.
- There exists at least one **safe sequence** of process execution.
- **Unsafe state ≠ deadlock**, but it might lead to one if no precaution is taken.

---

### **2. Resource Allocation Graph (RAG) for Single Instances:**
- **Extended RAG** includes a new type of edge called a **claim edge**, shown as a **dashed arrow** from process to resource.
- When a process requests a resource, claim edge becomes a request edge.
- Allocation only proceeds if it doesn’t create a cycle in the graph.

> **Limitation**: Works only for systems with **single instance** of each resource.

---

### **3. Banker's Algorithm (for Multiple Instances):**
Proposed by Dijkstra, it's named because it mimics how a banker would decide whether to grant a loan to avoid insolvency.

#### **Important Data Structures:**

| Structure    | Description                                          |
|--------------|------------------------------------------------------|
| **Available** | Vector of available resources                       |
| **Max**       | Matrix: maximum demand of each process              |
| **Allocation**| Matrix: current allocation to each process          |
| **Need**      | Matrix = Max - Allocation                           |

#### **Working:**
1. When a process requests resources:
   - Check if request ≤ Need.
   - Check if request ≤ Available.
2. Temporarily allocate resources.
3. Check if the resulting state is **safe** using the **safety algorithm**.
4. If safe, proceed. Else, **roll back** and deny request.

---

### **Example of Banker’s Algorithm:**

**Initial State:**

```plaintext
Available:   [3, 3, 2]
Max:         P0 [7, 5, 3]  P1 [3, 2, 2]  P2 [9, 0, 2]  ...
Allocation:  P0 [0, 1, 0]  P1 [2, 0, 0]  P2 [3, 0, 2]  ...
```

- Calculate Need = Max - Allocation.
- Simulate allocations and see if all processes can complete one after another (safe sequence exists).
- If yes, it’s safe to allocate.

---

### **Advantages of Avoidance:**
- More flexible than prevention.
- Avoids unnecessary blocking.

### **Disadvantages:**
- Requires **prior knowledge of maximum needs**.
- High **overhead** for checking safe state at every request.
- **Not scalable** for large systems.

---
### **1.5 Deadlock Detection and Recovery**

When a system does **not apply deadlock prevention or avoidance**, it may enter a deadlock state. In such cases, the operating system must:

1. **Detect** that a deadlock has occurred.
2. **Recover** from the deadlock.

---

## **1. Deadlock Detection**

Detection techniques differ based on whether **resources have single instances** or **multiple instances**.

---

### **Case 1: Single Instance of Each Resource**

- Use a **Resource Allocation Graph (RAG)**.
- A **cycle** in the graph indicates a **deadlock**.
- If no cycle exists → no deadlock.
- Detection is straightforward using **Depth First Search (DFS)** or similar algorithms.

---

### **Case 2: Multiple Instances of Resources**

More complex. We use a detection algorithm similar to the **Banker’s Algorithm**.

#### **Key Data Structures:**
Same as Banker’s:
- `Available[]`
- `Allocation[][]`
- `Request[][]`
- `Finish[]`: To keep track of completed processes.

#### **Detection Algorithm Steps:**
1. Initialize `Finish[i] = false` for all processes with non-zero Allocation.
2. Find a process `i` such that:
   - `Finish[i] == false`
   - `Request[i] <= Available`
3. If such a process exists:
   - Allocate its resources to `Available`.
   - Mark `Finish[i] = true`
   - Repeat step 2.
4. If no such process exists and some `Finish[i] == false`, then those processes are **deadlocked**.

#### **Complexity:**
- Time complexity is **O(n² × m)**, where `n` = number of processes, `m` = number of resource types.

---

## **2. Deadlock Recovery**

Once deadlock is detected, the system must recover. There are **two main strategies**:

---

### **A. Process Termination**

1. **Abort all deadlocked processes**:
   - Quick recovery.
   - Risk of losing large computation.
2. **Abort one process at a time** until deadlock is resolved:
   - Carefully select victim to minimize cost.

#### **Victim Selection Criteria:**
- Process priority.
- CPU time used so far.
- Resources held.
- Number of processes to abort.
- Impact on the system.

---

### **B. Resource Preemption**

- Select a process and **preempt its resources**.
- Rollback the process to a **safe state** (using checkpoints).
- Reassign preempted resources to other processes.
- Restart the preempted process later.

#### **Issues with Preemption:**
- Which resources to take?
- Which process to preempt?
- How many times to rollback?
- Starvation possibility.

---

### **Trade-Offs in Detection and Recovery:**

| Strategy         | Pros                         | Cons                          |
|------------------|-------------------------------|-------------------------------|
| Termination       | Simple, fast                  | Loss of computation           |
| Resource Preemption | Keeps processes running     | Complex, risk of starvation   |

---
### **2.1 Memory Management: Logical and Physical Address Space**

Memory management is a key function of the Operating System. It ensures **efficient allocation and use of memory** during program execution.

---

### **1. Logical Address vs. Physical Address**

#### **Logical Address (Virtual Address):**
- Generated by the **CPU** during program execution.
- It is a **reference** to a location in the program’s address space.
- Part of the **logical address space (LAS)**.
- **Used by programs** to access data and instructions.

#### **Physical Address:**
- The actual location in the **main memory (RAM)**.
- Belongs to the **physical address space (PAS)**.
- Determined by **memory management unit (MMU)**.

---

### **Address Binding:**
Binding is the process of mapping logical addresses to physical addresses.

#### Types of Binding:
1. **Compile-time Binding**:
   - Absolute addresses are known at compile time.
   - Used only when the process is loaded at a known location in memory.
2. **Load-time Binding**:
   - If the memory location is not known at compile time.
   - Binding is done when the program is loaded into memory.
3. **Execution-time Binding**:
   - Performed by **MMU** at runtime.
   - Allows processes to move during execution.
   - Most flexible and common.

---

### **Memory-Management Unit (MMU):**

- **Translates logical addresses to physical addresses** at runtime.
- Uses a base register and limit register.

#### **Address Translation Formula:**
```
Physical Address = Base Register + Logical Address
```

---

### **Example:**

- Base = 10000  
- Logical Address = 356  
- Physical Address = 10000 + 356 = **10356**

---

### **Advantages of Logical Addressing:**
- Provides **abstraction** and **protection**.
- Allows **multi-programming**.
- Enables **virtual memory**.

---

### **Diagram:**

```text
+----------------------+             +-----------------------+
|   Logical Address    | --MMU-->   |   Physical Address    |
+----------------------+             +-----------------------+
```

---
### **2.2 Swapping**

Swapping is a memory management technique used by the operating system to **temporarily move processes** between **main memory (RAM)** and **secondary storage (usually a hard disk or SSD)**.

---

### **What is Swapping?**

Swapping involves:
- **Moving a process out** of main memory (to secondary storage) when it is not being used.
- **Bringing it back into memory** when it is needed for execution.

This helps in managing **limited physical memory** and improves **CPU utilization**.

---

### **When is Swapping Used?**

- When **RAM is full** and a new process needs to be loaded.
- During **context switching** in multiprogramming environments.
- For **suspended** or **idle** processes.

---

### **Swapping Steps:**

1. **Process A is executing in RAM.**
2. A new process B needs to be loaded.
3. Process A is swapped out to disk (swap space).
4. Process B is loaded into RAM.
5. When Process A is needed again, it is swapped back in.

---

### **Swap Space:**

- A portion of the disk used to store **swapped-out processes**.
- Also called the **paging file** or **virtual memory area**.

---

### **Advantages of Swapping:**

- Supports **more processes** than the physical memory can handle.
- **Maximizes CPU usage** by keeping it busy with other processes.
- Enables **multiprogramming**.

---

### **Disadvantages:**

- **Slow** compared to RAM due to disk access time.
- **Swapping overhead** may affect performance if done frequently.
- May lead to **thrashing** (discussed later).

---

### **Example:**

- RAM Size = 4 GB  
- Running: Process A (2 GB), Process B (2 GB)  
- New Process C (2 GB) arrives  
- OS swaps out Process A to disk, loads Process C

---

### **Diagram:**

```text
[ RAM ]                          [ Disk (Swap Area) ]
|--------|                      |-------------------|
|  ProcA |   --> Swap out -->   |       ProcA       |
|  ProcB |                      |                   |
|--------|                      |-------------------|
```

---
### **2.3 Contiguous Memory Allocation (In-Depth Explanation)**

Contiguous Memory Allocation is one of the simplest memory management techniques in which **each process is allocated a single contiguous block** of physical memory.

---

### **Key Idea:**

- The entire process must be **loaded into a single continuous section of memory** before it can be executed.
- Memory is divided into **fixed or variable-sized partitions**.

---

### **Types of Contiguous Allocation:**

#### 1. **Single Contiguous Allocation**
- The entire RAM is divided into two parts:
  - **Operating System** (usually in low memory)
  - **User Process**
- Only **one process** can be in memory at a time.
- **Used in early systems** like MS-DOS.

#### 2. **Multiple Contiguous Allocation**
- **Multiple user processes** are kept in memory simultaneously.
- OS divides memory into **fixed or dynamic partitions** for each process.

---

### **Memory Allocation Strategies:**

To manage free space and allocate memory efficiently, operating systems use allocation algorithms:

#### a. **First Fit**
- Allocates the **first hole** that is big enough.
- Fast, but may leave many small unusable holes (**fragmentation**).

#### b. **Best Fit**
- Allocates the **smallest hole** that fits the process.
- Minimizes wasted space but can be **slow** and create more fragmentation.

#### c. **Worst Fit**
- Allocates the **largest available hole**.
- Leaves large remaining holes for future processes.
- Generally not efficient.

---

### **Fragmentation in Contiguous Allocation:**

#### 1. **External Fragmentation**
- **Unused memory** scattered between allocated blocks.
- Cannot be used even though total free memory might be enough.

#### 2. **Internal Fragmentation**
- **Allocated memory is larger** than needed.
- Wasted space inside the allocated partition.

---

### **Compaction:**

- A technique to **reduce external fragmentation**.
- OS **moves processes in memory** to bring all free memory together.
- **Time-consuming and expensive** (requires temporary halting of processes).

**Example Before Compaction:**

```text
+------------+--------+----------+----------+--------+
| Process A  |  Hole  | Process B|   Hole   |Process C|
+------------+--------+----------+----------+--------+
```

**After Compaction:**

```text
+------------+----------+----------+------------------+
| Process A  | Process B| Process C|   Large Hole     |
+------------+----------+----------+------------------+
```

---

### **Advantages:**

- **Simple and easy** to implement.
- Provides **fast access** due to contiguous memory layout.

### **Disadvantages:**

- **Fragmentation** leads to inefficient memory use.
- **Difficult to allocate** memory to large processes after fragmentation.
- **Not scalable** for modern multi-user, multi-tasking systems.

---

### **Use Case Example:**

- Consider 1000 MB RAM:
  - OS takes 200 MB
  - Process A needs 300 MB → Allocated at address 200
  - Process B needs 400 MB → Allocated at address 500
  - Hole of 100 MB remains → Can’t fit a process of 150 MB

---

### **In Real OS:**
Modern operating systems rarely use contiguous allocation due to its **inefficiency and scalability issues**, instead they use **paging** and **segmentation** (up next).

---
### **2.4 Paging (In-Depth Explanation)**

Paging is a **non-contiguous memory allocation** technique that eliminates the problems of contiguous allocation such as external fragmentation. It allows a process’s physical memory to be **scattered across RAM** rather than being placed in one continuous block.

---

### **Basic Concepts:**

- **Paging divides** the logical address space (used by programs) into fixed-size **pages**.
- Physical memory is divided into fixed-size **frames** of the same size as pages.

---

### **Terminology:**

| Term         | Description |
|--------------|-------------|
| **Page**     | A fixed-size block of **logical memory** (typically 4 KB) |
| **Frame**    | A fixed-size block of **physical memory** (same size as page) |
| **Page Table** | A data structure used by OS to **map pages to frames** |

---

### **How Paging Works:**

1. When a program is loaded:
   - It is **divided into pages** by the OS.
   - Free frames in RAM are located.
   - Pages are **loaded into available frames**, not necessarily contiguous.

2. The **Page Table** stores the mapping from each **page number to frame number**.

---

### **Logical Address to Physical Address Translation:**

A logical address is divided into:
- **Page Number (p)** – Index into the page table.
- **Page Offset (d)** – Offset within the page.

**Physical Address = Frame Number (from page table) + Offset**

---

### **Example:**

Suppose:
- Page size = 1 KB (1024 bytes)
- Logical address = 2049
- Then:
  - Page number `p = 2049 / 1024 = 2`
  - Offset `d = 2049 % 1024 = 1`

If page 2 maps to frame 5:
- Physical address = `5 * 1024 + 1 = 5121`

---

### **Advantages of Paging:**

- **No external fragmentation** (free frames can be anywhere).
- **Efficient use** of memory.
- **Allows swapping** individual pages.

---

### **Disadvantages of Paging:**

- **Internal fragmentation** (last page of a process might not be fully used).
- **Overhead of page table** (especially for large programs).
- **Memory access time increases** due to address translation.

---

### **Types of Page Tables:**

1. **Single-level page table**  
   - Simple but consumes memory for large address spaces.

2. **Multi-level page tables**  
   - Page table is divided into levels, saving memory.

3. **Inverted page table**  
   - One entry per frame; reduces memory but slower lookup.

---

### **Hardware Support:**

- **Memory Management Unit (MMU)** performs address translation.
- **Translation Lookaside Buffer (TLB)** caches recent page table entries to speed up translation.

---

### **Real-World Use:**

Paging is used in all modern operating systems like Windows, Linux, and macOS. It forms the **basis for virtual memory systems**.

---
### **2.5 Segmentation (In-Depth Explanation)**

Segmentation is another memory management technique that supports the **user's view of memory**. Unlike paging, which divides memory into fixed-size blocks, segmentation divides memory into **variable-sized segments** based on logical divisions in a program (e.g., code, stack, heap, data).

---

### **Key Concepts:**

- A program is **logically divided** into segments such as:
  - **Code segment** (instructions)
  - **Data segment** (global variables)
  - **Stack segment** (function calls and local variables)
  - **Heap segment** (dynamically allocated memory)

Each segment has:
- A **name**
- A **length**
- A **starting address (base)**

---

### **Logical Address Format:**

A **logical address** in segmentation consists of:
- **Segment number (s)**
- **Offset within segment (d)**

---

### **Translation to Physical Address:**

The OS maintains a **Segment Table** for each process, which contains:

| Segment Number | Base Address | Limit |
|----------------|--------------|-------|
| 0              | 4000         | 1000  |
| 1              | 8000         | 500   |

- **Base**: Starting physical address of the segment.
- **Limit**: Length of the segment.

To translate a logical address `(s, d)`:
- If `d < Limit[s]`, then **Physical Address = Base[s] + d**
- Else, a **segmentation fault** (address out of bounds) occurs.

---

### **Example:**

Suppose we access segment 1 with offset 200.

- From the segment table:
  - Base[1] = 8000
  - Limit[1] = 500

Since 200 < 500, the physical address is:
- **8000 + 200 = 8200**

---

### **Advantages of Segmentation:**

- Supports **user's logical view** of memory (program structure).
- **No internal fragmentation**.
- Allows **protection and sharing** at the segment level.
- **Easy to grow** segments like stack and heap.

---

### **Disadvantages of Segmentation:**

- Leads to **external fragmentation** (due to variable segment sizes).
- Requires **compaction** to handle fragmentation.
- **Overhead of segment table**.

---

### **Comparison with Paging:**

| Feature        | Paging                          | Segmentation                    |
|----------------|----------------------------------|----------------------------------|
| Block Size     | Fixed (pages)                   | Variable (segments)             |
| Address Format | Page number + offset            | Segment number + offset         |
| Fragmentation  | Internal                        | External                        |
| User View      | Doesn't match program structure | Matches program structure       |

---

### **Segmentation in Practice:**

- Some systems use **pure segmentation** (e.g., early Intel processors).
- Most modern systems use **segmentation + paging**, combining benefits of both.

---
### **2.6 Segmentation with Paging (Detailed Explanation)**

**Segmentation with Paging** is a hybrid memory management scheme that combines the benefits of both **segmentation** and **paging** to efficiently manage memory, minimize fragmentation, and maintain logical program structure.

---

### **Why Combine Segmentation and Paging?**

- **Segmentation**: Supports logical division of a program (code, data, stack), but suffers from **external fragmentation**.
- **Paging**: Solves fragmentation by using fixed-size blocks but doesn’t represent the logical structure of programs.

**Solution**: First divide the process into **segments**, and then divide each segment into **pages**.

---

### **Logical Address Structure:**

A logical address in segmentation with paging has **three components**:
- **Segment number (s)**
- **Page number within segment (p)**
- **Offset within page (d)**

---

### **Data Structures Used:**

1. **Segment Table**:  
   - Each entry points to a **Page Table Base Address** for that segment.
   - Also includes segment limit.

2. **Page Tables** (one per segment):  
   - Maps page numbers to **frame numbers** in physical memory.

---

### **Address Translation Process:**

1. The logical address `(s, p, d)` is received.
2. Use **segment number (s)** to index the **Segment Table**.
3. Fetch the base address of the **Page Table** for segment `s`.
4. Use **page number (p)** to index into that page table and get the **frame number (f)**.
5. Combine the frame number and offset `(d)` to get the **physical address**.

---

### **Example:**

Suppose:
- Segment 2 starts at Page Table Base Address: 100
- Page size = 1 KB
- Page table at location 100 maps page 3 → frame 20

Logical address: (s=2, p=3, d=500)

Steps:
1. Look up segment 2 in segment table → Page table base = 100
2. Go to page table at index 100 + 3 → Frame = 20
3. Physical address = 20 * 1024 + 500 = **20980**

---

### **Advantages of Segmentation with Paging:**

- **Logical division of program** (segments) is preserved.
- **No external fragmentation** (thanks to paging).
- Enables **fine-grained protection**: both segment-wise and page-wise.

---

### **Disadvantages:**

- **Overhead** of maintaining multiple page tables (one for each segment).
- Slightly more **complex translation logic**.

---

### **Use in Modern Systems:**

- Intel x86 architecture supports segmentation with paging.
- Linux typically uses **paging only**, but under the hood still maintains some segmentation structure for privilege levels.

---
### **2.7 Virtual Memory – Demand Paging and Its Performance (In-depth Explanation)**

---

### **What is Virtual Memory?**

**Virtual Memory** is a memory management technique that allows the execution of processes that may not be completely in physical memory (RAM). It gives the **illusion of a very large main memory** by using **secondary storage (like HDD/SSD)**.

---

### **Key Concepts:**

- The operating system uses **virtual addresses**, which are translated to **physical addresses**.
- **Only parts** of a program that are needed are loaded into memory.
- This approach allows for **larger programs**, **more programs**, and **better CPU utilization**.

---

### **Demand Paging:**

Demand Paging is a type of virtual memory system where **pages are not loaded into memory until they are actually needed** (on demand).

#### **How it Works:**

1. Initially, no pages of the process are loaded in memory (or only a few essential pages).
2. When the process tries to access a page that is **not in memory**, a **page fault** occurs.
3. The OS:
   - Pauses the process.
   - Loads the required page from secondary storage into memory.
   - Updates the page table.
   - Resumes execution.

---

### **Valid-Invalid Bit Mechanism:**

Each page table entry has a **valid/invalid bit**:
- **Valid**: Page is in memory and can be accessed.
- **Invalid**: Page is not currently in memory → triggers page fault.

---

### **Advantages of Demand Paging:**

- **Efficient memory use** – only needed pages are loaded.
- **Faster startup** – no need to load the entire program at once.
- Enables **larger programs** to run on limited physical memory.

---

### **Disadvantages:**

- **Initial page faults** may slow down execution.
- **Thrashing** can occur if there’s insufficient memory (excessive page faults).
- More **overhead** in page management.

---

### **Page Fault Handling Steps:**

1. Check if the memory access is valid.
2. If valid but the page is not in memory → page fault.
3. Choose a **free frame** (or use replacement algorithm).
4. Load the page from disk to frame.
5. Update page table entry.
6. Restart the instruction that caused the fault.

---

### **Performance of Demand Paging:**

Let:
- **p** = Probability of a page fault (0 ≤ p ≤ 1)
- **ma** = Memory access time
- **pf_time** = Page fault service time

**Effective Access Time (EAT):**

\[
EAT = (1 - p) \times ma + p \times pf\_time
\]

Example:
- ma = 200 ns
- pf_time = 8 ms = 8,000,000 ns
- p = 0.001

\[
EAT = (0.999 \times 200) + (0.001 \times 8,000,000) = 200 + 8000 = 8200 \, \text{ns}
\]

As we see, even **small page fault rates** drastically affect performance.

---

### **Reducing Page Faults:**

- Use **efficient page replacement algorithms**.
- **Increase physical memory** (RAM).
- Use **working set model**.
- Use **locality of reference** to prefetch needed pages.

---
### **2.8 Page Replacement Algorithms (Extremely Detailed)**

---

When a **page fault** occurs and **no free frames** are available in physical memory, the OS must **replace** one of the existing pages with the new required page. This is done using a **Page Replacement Algorithm**.

---

### **Objectives of a Good Algorithm:**

- Minimize the **number of page faults**.
- Select a page to replace that is **least likely to be used again soon**.
- Balance performance and computational cost.

---

## **1. FIFO (First-In First-Out) Algorithm**

**Concept**: Replace the page that **arrived first** in memory.

- Use a **queue** to track page order.
- The **oldest page** is removed first.

### **Example:**
Pages: 1, 2, 3, 4 (reference string), Frame size = 3

Step-by-step insertion:

- [1] → Page Fault  
- [1, 2] → Page Fault  
- [1, 2, 3] → Page Fault  
- [2, 3, 4] → Page Fault → (1 removed)

Total page faults: **4**

### **Disadvantage:**
- May remove **frequently used** pages.
- **Belady’s Anomaly**: Increasing frame size may **increase** page faults.

---

## **2. LRU (Least Recently Used) Algorithm**

**Concept**: Replace the page that was **least recently accessed**.

- Assumes that **recently used pages** are more likely to be used again.

### **Implementation:**
- Use a **stack** or **timestamp system**.
- Track last access time for each page.

### **Example:**
Reference: 7, 0, 1, 2, 0, 3, 0, 4  
Frame size = 3

Insert pages while removing the least recently used.

Total page faults: **8**

### **Advantage:**
- Performs better than FIFO in most cases.

### **Disadvantage:**
- **Overhead** of tracking usage.
- Requires hardware support or costly software tracking.

---

## **3. Optimal Page Replacement**

**Concept**: Replace the page that will **not be used for the longest time** in the future.

- Theoretical model (used for benchmarking).

### **Example:**
Reference: 7, 0, 1, 2, 0, 3, 0, 4  
Frame size = 3

Predict future usage and replace accordingly.

Page faults: **6** (better than LRU and FIFO)

### **Disadvantage:**
- **Impossible to implement** in practice since it needs **future knowledge**.

---

## **4. Clock (Second Chance) Algorithm**

**Concept**: Approximation of LRU using a **circular queue** with a **reference bit**.

- Each page has a **use bit** (0 or 1).
- If a page is referenced, its bit is set to 1.
- When replacement is needed:
  - Check current page:
    - If use bit = 0 → replace it.
    - If use bit = 1 → clear it and move to next.

### **Advantage:**
- **Efficient** and practical.
- **Approximate LRU** with less overhead.

---

### **Comparison Table:**

| Algorithm | Page Faults (typical) | Complexity | Practical Use |
|-----------|------------------------|------------|----------------|
| FIFO      | Medium/High            | Low        | Yes            |
| LRU       | Low                    | Medium/High| Yes (w/ support)|
| Optimal   | Lowest (Theoretical)   | Not usable | No             |
| Clock     | Low                    | Medium     | Yes            |

---
### **2.9 Allocation of Frames (Extremely Detailed)**

---

When multiple processes are running in a system, each process must be allocated a certain number of **frames** (fixed-size blocks of physical memory) for its pages. The strategy of **frame allocation** determines how many frames each process receives and how they are assigned.

---

## **Types of Frame Allocation Algorithms**

---

### **1. Equal Allocation**

- Each process is given **equal number of frames** regardless of its size.
- Total number of frames `F` and number of processes `P`:

  $$ \text{Frames per process} = \frac{F}{P} $$

#### **Example:**
- 100 frames, 5 processes
- Each process gets **20 frames**

#### **Advantage:**
- Simple and fair

#### **Disadvantage:**
- Inefficient for large processes and **wasteful for small ones**

---

### **2. Proportional Allocation**

- Allocate frames based on the **size of each process**.

  $$ \text{Frames for a process} = \frac{\text{Process size}}{\text{Total size of all processes}} \times F $$

#### **Example:**
- Process A: 10 pages, Process B: 30 pages
- Total: 40 pages, 100 frames

- A gets: \( \frac{10}{40} \times 100 = 25 \) frames  
- B gets: \( \frac{30}{40} \times 100 = 75 \) frames

#### **Advantage:**
- More **balanced and efficient** than equal allocation

#### **Disadvantage:**
- Can still cause problems for processes with **dynamic behavior**

---

### **3. Priority Allocation**

- Allocate more frames to **higher-priority processes**.

#### **Approach:**
- Priority weight is assigned to each process
- More weight → More frames

#### **Example:**
- Priority A = 2, B = 1, C = 1  
- Total = 4 units of priority  
- A gets 50%, B gets 25%, C gets 25% of total frames

#### **Advantage:**
- Suitable for **real-time or critical tasks**

#### **Disadvantage:**
- Low-priority processes may starve for memory

---

## **Global vs Local Allocation**

---

### **Global Allocation**

- Frames are assigned from a **global pool**.
- Processes **compete** for frames.

#### **Advantage:**
- More flexible, allows better **overall memory utilization**

#### **Disadvantage:**
- A process’s performance may be **impacted by others**

---

### **Local Allocation**

- Each process is given a **fixed number** of frames.
- It **can only use** its own frames.

#### **Advantage:**
- More **stable and isolated**

#### **Disadvantage:**
- May lead to **underutilization** of memory

---

## **Key Points:**

- Too **few frames** → High page faults (Thrashing)
- Too **many frames** → Wasted memory
- **Smart allocation** → Improved performance and system stability

---
### **2.10 Thrashing (Extremely Detailed)**

---

## **What is Thrashing?**

**Thrashing** is a condition in virtual memory systems where the **CPU spends most of its time swapping pages in and out of memory** rather than executing processes. This leads to **very high page fault rates** and **degraded system performance**.

---

## **Why Does Thrashing Occur?**

Thrashing happens when:

1. **Too many processes** are loaded into memory.
2. Each process is **allocated too few frames**.
3. Processes **continuously compete** for frames.
4. Pages are **frequently replaced**, even though they are needed again shortly after.

---

## **Real Example of Thrashing:**

Assume:

- Three processes A, B, and C are running.
- All three are allocated too few frames (say, 3 each).
- Each needs 6 pages actively.

Because only 3 frames are available:
- Every time a page is referenced, **page fault** occurs.
- The system swaps pages in and out **constantly**.
- CPU is busy in page replacement, not in actual work.

---

## **Consequences of Thrashing:**

- **Excessive paging** activity.
- **Low CPU utilization**.
- **High disk I/O**.
- **Processes slow down** dramatically.
- System becomes **non-responsive**.

---

## **Detection of Thrashing:**

### 1. **Monitor Page-Fault Rate:**
- **High and increasing page-fault rate** is a sign.

### 2. **CPU Utilization Drops:**
- CPU sits idle, waiting for pages to be loaded.

---

## **How to Handle or Avoid Thrashing?**

---

### **1. Using Working Set Model**

- **Working set** is the set of pages a process needs in a given time interval.
- If we ensure a process has at least its working set in memory → **thrashing is avoided**.

#### Formula:
Let Δ = fixed time window

$$
WS(t, Δ) = \{ pages \ used \ by \ process \ in \ time \ window \ Δ \}
$$

- If the sum of working sets of all processes exceeds memory → reduce multiprogramming.

---

### **2. Page Fault Frequency (PFF) Strategy**

- **Set upper and lower bounds** on acceptable page fault rates.

#### If:
- Page fault rate **> upper limit** → Allocate more frames.
- Page fault rate **< lower limit** → Reclaim frames.

---

### **3. Reduce Degree of Multiprogramming**

- **Suspend or swap out** one or more processes temporarily.
- Frees up memory for other processes.

---

### **4. Use Local Page Replacement**

- Limit the impact of one process’s paging on others.

---

### **5. Use Better Page Replacement Algorithms**

- Such as **LRU**, **Optimal**, or **Working Set-based** replacement.

---

## **Key Takeaways:**

- Thrashing = Too much paging, not enough execution.
- Often caused by **low frame allocation** and **high multiprogramming**.
- Can be controlled by:
  - Working Set Model
  - Page Fault Frequency
  - Reducing multiprogramming
  - Using smarter replacement policies

---

# Unit -III  
- Introduction and interacting with shell and Desktop to Linux: History, salient features, Linux system architecture, Linux command format, Linux internal and external commands, Directory commands, File related commands, Disk related commands.   
- The Linux Shell Basic command cls, cat, cal, date, calendar, who, printf, tty, sty, uname, passwd, echo, tput, bc, script,  Introduction to Shell Scripting,  read, Command Line Arguments, Exit Status of a Command.  
- shell types,  shell script features, executing a shell script, system and user-defined variables, expr command, command substitution, escape sequence characters, shell script arguments, positional parameters, test command, file test, string test, numeric test   

---

### **Introduction and Interacting with Shell and Desktop in Linux**

---

#### **1. History of Linux**

- **Origins**:  
  Linux was created in **1991** by **Linus Torvalds**, a Finnish student. He was inspired by **MINIX**, a UNIX-like system used for educational purposes.
  
- **Development**:  
  Initially released as a kernel, Linux evolved into a full-fledged operating system by combining the kernel with GNU tools (hence often called **GNU/Linux**).

- **Open Source Nature**:  
  Linux is open source and free to use, distribute, and modify. It follows the **GNU General Public License (GPL)**.

- **Milestones**:  
  - **1991** – Linux kernel 0.01 released  
  - **1994** – Kernel 1.0 released  
  - **2003** – Kernel 2.6 released (improved performance and driver support)  
  - **2011** – 20th anniversary  
  - **Ongoing** – Used in servers, mobile devices (like Android), desktops, IoT, and more.

---

#### **2. Salient Features of Linux**

- **Multitasking**: Can run multiple processes at the same time.
- **Multiuser**: Several users can work simultaneously without interfering with each other.
- **Portability**: Can run on different hardware architectures.
- **Security**: User-level permissions, encrypted passwords, file protection, firewall tools.
- **Open Source**: The source code is freely available for modification and redistribution.
- **Stability and Reliability**: Rarely crashes, and systems can run for years without needing a reboot.
- **Shell and GUI Support**: Offers powerful command-line interface (CLI) and graphical interfaces (GNOME, KDE, XFCE, etc.)
- **File System Support**: Supports many file systems like ext2, ext3, ext4, FAT, NTFS.
- **Networking**: Built-in networking capabilities for configuration, file sharing, and remote access.

---

#### **3. Linux System Architecture**

Linux follows a **layered architecture** composed of several core components:

```
-------------------------
|    Application Layer   |
-------------------------
|    Shell (CLI/GUI)     |
-------------------------
|    Kernel (Core OS)    |
-------------------------
| Hardware (CPU, RAM etc)|
-------------------------
```

- **Hardware**: Physical components like CPU, memory, disk, etc.
- **Kernel**: Core of the operating system. It:
  - Manages process scheduling
  - Controls hardware
  - Manages file systems and memory
- **Shell**: Interface between the user and kernel. Takes user input and converts it to kernel-understandable instructions.
- **Applications**: End-user programs like browsers, editors, and scripts.

---

### **4. Linux Command Format**

---

#### **Basic Syntax of a Linux Command**

The general format of a Linux command is:

```
command [options] [arguments]
```

- **command**: The actual command to be executed (e.g., `ls`, `cp`, `mkdir`)
- **options (flags)**: Modify the behavior of the command (e.g., `-l`, `-a`)
- **arguments**: The target of the command, such as a filename or directory name

---

#### **Examples:**

1. `ls -l /home/user`

   - `ls`: list directory contents  
   - `-l`: option to display in long format  
   - `/home/user`: argument (the directory to list)

2. `cp -r dir1 dir2`

   - `cp`: copy command  
   - `-r`: recursive copy  
   - `dir1`: source directory  
   - `dir2`: destination directory

3. `grep "text" file.txt`

   - `grep`: searches for "text" inside file.txt  
   - `"text"`: search pattern  
   - `file.txt`: target file

---

#### **Options Explained**

- Options usually start with `-` or `--`:
  - Single-dash for short options: `-l`, `-a`
  - Double-dash for long options: `--help`, `--version`

---

#### **Command Execution Steps**

1. **User enters a command** in shell
2. Shell **parses** the command
3. Shell **locates** the binary (using `PATH` environment variable)
4. Shell **executes** the command
5. **Output is returned** to the user

---

#### **Command Help**

You can get help about any command using:

- `man command_name` – Opens the manual page (e.g., `man ls`)
- `command --help` – Displays brief usage instructions
- `info command_name` – More structured documentation

---

#### **Note on Case Sensitivity**

Linux commands and filenames are **case-sensitive**:
- `ls` is different from `LS`
- `File.txt` is different from `file.txt`


---

### **5. Linux Internal and External Commands**

---

#### **Internal Commands**

Internal commands are **built into the shell itself**. When you type them, the shell executes them **without creating a new process**.

- These commands are part of the **shell binary** (like `bash`).
- They are faster because **no disk access** is required to find an external binary.

**Examples:**

| Command | Purpose |
|---------|---------|
| `cd`    | Change directory |
| `pwd`   | Print current directory |
| `echo`  | Print text to terminal |
| `set`   | Set shell options or variables |
| `export`| Export variables to environment |
| `alias` | Create command aliases |
| `read`  | Read input from user |

---

#### **How to Check if a Command is Internal:**

Use `type` or `which`:

```bash
type cd      # Output: cd is a shell builtin
type ls      # Output: ls is /bin/ls
```

---

#### **External Commands**

External commands are **separate programs** stored as executable files in your file system (usually in `/bin`, `/usr/bin`, etc.).

- When you run an external command, the shell searches through directories listed in the `$PATH` environment variable.
- These commands **create a new process** when executed.

**Examples:**

| Command   | Purpose                         |
|-----------|---------------------------------|
| `ls`      | List directory contents         |
| `cp`      | Copy files or directories       |
| `rm`      | Remove files or directories     |
| `mkdir`   | Create new directories          |
| `grep`    | Pattern searching                |
| `find`    | Search files based on criteria  |
| `tar`     | Archive utility                  |
| `chmod`   | Change file permissions         |

---

#### **How to Check External Commands:**

```bash
which ls       # Shows full path: /bin/ls
whereis grep   # Shows binary and man location
```

---

#### **Why This Difference Matters:**

- **Performance**: Internal commands are faster.
- **Environment**: Some commands (like `cd`) must be internal to affect the current shell process.
- **Customization**: External commands can be replaced with scripts or programs with the same name.

---

### **6. Directory Commands in Linux**

Linux uses a hierarchical directory structure. These **directory-related commands** help in navigating and managing this structure.

---

#### **Common Directory Commands**

| Command | Description |
|---------|-------------|
| `pwd`   | Print the current working directory |
| `ls`    | List the contents of a directory |
| `cd`    | Change to a different directory |
| `mkdir` | Make (create) a new directory |
| `rmdir` | Remove an empty directory |
| `rm -r` | Remove a directory and its contents |
| `tree`  | Show directory structure in tree format (may require installation) |

---

#### **Details and Usage**

---

##### **1. `pwd` – Print Working Directory**
Displays the absolute path of the current directory.

```bash
$ pwd
/home/user/Documents
```

---

##### **2. `ls` – List Directory Contents**
Lists files and subdirectories.

```bash
$ ls
file1.txt  folder1  script.sh
```

**Useful options:**

- `ls -l` – long format with permissions, ownership, size, date
- `ls -a` – show hidden files (starting with `.`)
- `ls -lh` – human-readable sizes
- `ls -R` – recursively list subdirectories

---

##### **3. `cd` – Change Directory**

Changes the current directory.

```bash
$ cd /home/user/Pictures
$ cd ..       # Move up one level
$ cd ~        # Go to home directory
```

---

##### **4. `mkdir` – Make Directory**

Creates a new folder.

```bash
$ mkdir new_folder
$ mkdir -p dir1/dir2/dir3   # Create nested directories
```

---

##### **5. `rmdir` – Remove Empty Directory**

Removes **only empty** directories.

```bash
$ rmdir old_folder
```

---

##### **6. `rm -r` – Remove Directory with Contents**

Recursively deletes directories with their contents.

```bash
$ rm -r project_folder
```

Use with caution – it’s **irreversible**.

---

##### **7. `tree` – Display Tree Structure**

Shows a visual structure of the directory. You may need to install it:

```bash
$ sudo apt install tree
$ tree /home/user
```

---

### **7. File Related Commands in Linux**

Linux treats everything as a file – directories, devices, scripts, configurations. File-related commands are crucial for managing data.

---

#### **Common File Commands**

| Command   | Description |
|-----------|-------------|
| `touch`   | Create an empty file |
| `cat`     | Display content of a file |
| `more`, `less` | View file content page by page |
| `cp`      | Copy files or directories |
| `mv`      | Move or rename files |
| `rm`      | Remove/delete files |
| `file`    | Determine the type of a file |
| `stat`    | Detailed information about a file |
| `wc`      | Word, line, byte count |
| `head`, `tail` | View beginning or end of a file |

---

#### **Details and Examples**

---

##### **1. `touch` – Create File**

Creates an empty file or updates timestamp.

```bash
$ touch hello.txt
```

---

##### **2. `cat` – Display File Content**

Displays contents on the terminal.

```bash
$ cat file.txt
```

To create a file using `cat`:

```bash
$ cat > file.txt
Type here and press Ctrl+D to save
```

---

##### **3. `more`, `less` – Paged Viewing**

- `more file.txt` shows one screen at a time (limited navigation).
- `less file.txt` allows forward/backward movement (`q` to quit).

---

##### **4. `cp` – Copy Files**

```bash
$ cp source.txt destination.txt
$ cp file1.txt /home/user/Backup/
```

Use `-r` for directories.

```bash
$ cp -r folder1/ folder2/
```

---

##### **5. `mv` – Move or Rename**

```bash
$ mv file.txt /home/user/Documents/
$ mv oldname.txt newname.txt
```

---

##### **6. `rm` – Remove Files**

```bash
$ rm file.txt
$ rm -f file.txt     # force remove without prompt
$ rm -r foldername   # remove folder recursively
```

---

##### **7. `file` – File Type**

```bash
$ file file.txt
file.txt: ASCII text
```

---

##### **8. `stat` – File Info**

Displays metadata.

```bash
$ stat file.txt
```

---

##### **9. `wc` – Word Count**

```bash
$ wc file.txt
 10  20  150 file.txt   # lines, words, bytes
```

---

##### **10. `head` & `tail` – View Start/End**

```bash
$ head file.txt     # first 10 lines
$ tail file.txt     # last 10 lines
$ tail -n 20 file.txt   # last 20 lines
```

---

### **8. Disk Related Commands in Linux**

Disk-related commands allow users to monitor and manage disk usage, partitions, and file systems.

---

#### **Important Disk Commands**

| Command     | Description |
|-------------|-------------|
| `df`        | Disk space usage of file systems |
| `du`        | Disk usage of files/directories |
| `mount`     | Mount a file system |
| `umount`    | Unmount a file system |
| `fdisk`     | Partition management |
| `mkfs`      | Create file systems |
| `fsck`      | File system check |
| `lsblk`     | Lists block devices |
| `blkid`     | Shows UUID and type of devices |
| `parted`    | Advanced partitioning tool |

---

#### **Details and Examples**

---

##### **1. `df` – Disk Free**

Displays available and used disk space on file systems.

```bash
$ df -h
```

Options:
- `-h`: Human-readable (e.g., MB/GB)
- `-T`: Shows file system types

---

##### **2. `du` – Disk Usage**

Shows space used by files/directories.

```bash
$ du -sh /home/user/Documents
```

Options:
- `-s`: Summary
- `-h`: Human-readable

---

##### **3. `mount` – Attach File Systems**

Mounts a file system to a directory.

```bash
$ mount /dev/sdb1 /mnt/usb
```

To view mounted file systems:

```bash
$ mount | column -t
```

---

##### **4. `umount` – Unmount File Systems**

```bash
$ umount /mnt/usb
```

Ensure no process is using the mount.

---

##### **5. `fdisk` – Partition Table Tool**

```bash
$ sudo fdisk /dev/sda
```

Used to create, delete, or modify partitions.

---

##### **6. `mkfs` – Make File System**

Formats a partition with a file system.

```bash
$ mkfs.ext4 /dev/sdb1
```

---

##### **7. `fsck` – File System Check**

Used to fix corrupted file systems.

```bash
$ fsck /dev/sda1
```

Run on unmounted or read-only partitions.

---

##### **8. `lsblk` – List Block Devices**

```bash
$ lsblk
```

Shows device names, mount points, and sizes.

---

##### **9. `blkid` – Device Info**

Displays UUID and filesystem type of devices.

```bash
$ blkid
```

---

##### **10. `parted` – Partition Manager**

Advanced alternative to `fdisk`.

```bash
$ parted /dev/sda
```

---

### **9. The Linux Shell Basic Commands**

The shell is a command-line interpreter that allows users to interact with the Linux operating system. Let's explore the most basic and essential Linux commands often used for day-to-day tasks.

---

#### **Commonly Used Basic Commands**

| Command     | Description |
|-------------|-------------|
| `clear` / `cls` | Clears the terminal screen |
| `cat`       | Concatenates and displays file contents |
| `cal`       | Displays a calendar |
| `date`      | Displays or sets the system date/time |
| `who`       | Shows who is logged into the system |
| `printf`    | Prints formatted text to the screen |
| `tty`       | Displays the terminal type |
| `stty`      | Changes and prints terminal line settings |
| `uname`     | Displays system information |
| `passwd`    | Changes the user password |
| `echo`      | Displays a line of text/string |
| `tput`      | Controls terminal capabilities (e.g., color, cursor) |
| `bc`        | Command-line calculator |
| `script`    | Records terminal session |
| `calendar`  | Displays user-defined calendar events |

---

#### **Examples and Usage**

---

##### **1. `clear` or `cls`**

```bash
$ clear
```
Clears the terminal screen. (`cls` is used in some shells.)

---

##### **2. `cat`**

```bash
$ cat file.txt
```
Displays contents of `file.txt`.

To create a file:
```bash
$ cat > file.txt
```

---

##### **3. `cal`**

```bash
$ cal
```
Displays the current month’s calendar.

---

##### **4. `date`**

```bash
$ date
```
Displays current date and time.

Set date (needs superuser):
```bash
$ sudo date -s "5 APR 2025 10:00:00"
```

---

##### **5. `who`**

```bash
$ who
```
Shows users currently logged in.

---

##### **6. `printf`**

```bash
$ printf "Welcome %s\n" "User"
```
Formats output just like in C programming.

---

##### **7. `tty`**

```bash
$ tty
```
Displays the terminal device name.

---

##### **8. `stty`**

```bash
$ stty -a
```
Shows terminal line settings like erase, kill, intr characters.

---

##### **9. `uname`**

```bash
$ uname -a
```
Prints all system information (OS, kernel, architecture, etc.).

---

##### **10. `passwd`**

```bash
$ passwd
```
Changes current user's password.

---

##### **11. `echo`**

```bash
$ echo "Hello World"
```
Prints the string.

You can use variables too:
```bash
$ name="Linux"
$ echo "Welcome $name"
```

---

##### **12. `tput`**

```bash
$ tput setaf 1
$ echo "This is red text"
$ tput sgr0
```
Used to control text formatting and colors.

---

##### **13. `bc`**

```bash
$ echo "5 + 3" | bc
```
Runs basic math in shell.

To use decimal:
```bash
$ echo "scale=2; 5/3" | bc
```

---

##### **14. `script`**

```bash
$ script session.log
```
Records everything in terminal to `session.log`.

Stop recording with `exit`.

---

##### **15. `calendar`**

```bash
$ calendar
```
Displays events from a user-defined `calendar` file (if configured).

---

### **10. Introduction to Shell Scripting**

Shell scripting is the process of writing a series of commands for the shell to execute. Shell scripts are used to automate repetitive tasks, manage system operations, and create custom tools.

---

#### **What is a Shell Script?**

A **shell script** is a text file containing a sequence of commands that are interpreted and executed by a shell (like Bash, Zsh, etc.).

---

#### **Creating and Running a Shell Script**

**Step 1: Create the file**

```bash
$ nano myscript.sh
```

**Example content:**

```bash
#!/bin/bash
echo "Hello, welcome to shell scripting!"
```

**Step 2: Make it executable**

```bash
$ chmod +x myscript.sh
```

**Step 3: Run the script**

```bash
$ ./myscript.sh
```

---

#### **Basic Syntax Rules**

- Every shell script should start with:  
  ```bash
  #!/bin/bash
  ```

- Commands are executed in order, line by line.

- Comments start with `#` and are ignored by the shell.

---

#### **Advantages of Shell Scripting**

- Automates tasks (backups, installations, monitoring, etc.)
- Saves time and reduces manual effort
- Easy to write and understand
- Portable across systems

---

#### **Types of Shells**

- **Bourne Shell (`sh`)**
- **Bash (Bourne Again SHell)** – Most popular shell
- **C Shell (`csh`)**
- **Korn Shell (`ksh`)**
- **Z Shell (`zsh`)**

Most scripting is done in **Bash**, especially on Linux systems.

---

#### **Real-Life Use Case**

**Backup Script Example:**

```bash
#!/bin/bash
tar -czf backup.tar.gz /home/user/documents
echo "Backup completed!"
```

This script compresses the documents folder and creates a backup.

---

### **11. `read` Command in Shell Scripting**

The `read` command in shell scripting is used to accept input from the user during script execution. It pauses the script and waits for the user to enter input.

---

#### **Syntax:**

```bash
read variable_name
```

---

#### **Example 1: Reading a single input**

```bash
#!/bin/bash
echo "Enter your name:"
read name
echo "Hello, $name!"
```

**Output:**

```
Enter your name:
John
Hello, John!
```

---

#### **Example 2: Reading multiple inputs**

```bash
#!/bin/bash
echo "Enter your first and last name:"
read fname lname
echo "First Name: $fname"
echo "Last Name: $lname"
```

**Output:**

```
Enter your first and last name:
Alice Smith
First Name: Alice
Last Name: Smith
```

---

#### **Example 3: With `-p` and `-s` options**

- `-p` lets you prompt the user inline.
- `-s` allows silent input (useful for passwords).

```bash
read -p "Username: " username
read -sp "Password: " password
echo
echo "User: $username, Password: $password"
```

---

#### **Use Cases of `read` Command**

- Get user confirmation before executing critical operations.
- Accept values dynamically (like filenames or numbers).
- Interactive scripts that ask the user questions.


---

### **12. Command Line Arguments in Shell Scripting**

Command line arguments allow users to pass values to a shell script at the time of execution. These are stored in special variables like `$1`, `$2`, ..., `$n`, `$#`, `$@`, `$*`, etc.

---

### **Positional Parameters**

| Symbol | Meaning                                      |
|--------|----------------------------------------------|
| `$0`   | Name of the script                           |
| `$1`   | First argument                               |
| `$2`   | Second argument                              |
| `$#`   | Number of arguments                          |
| `$@`   | All arguments (individually quoted)          |
| `$*`   | All arguments (as a single word)             |

---

### **Example Script:**

```bash
#!/bin/bash
echo "Script Name: $0"
echo "First Arg: $1"
echo "Second Arg: $2"
echo "Total Args: $#"
echo "All Args using \$@: $@"
echo "All Args using \$*: $*"
```

**Execution:**

```bash
bash script.sh apple banana
```

**Output:**

```
Script Name: script.sh
First Arg: apple
Second Arg: banana
Total Args: 2
All Args using $@: apple banana
All Args using $*: apple banana
```

---

### **Shift Command**

The `shift` command is used to move all command-line arguments to the left.

```bash
#!/bin/bash
echo "Before shift: $1 $2 $3"
shift
echo "After shift: $1 $2"
```

**Execution:**

```bash
bash script.sh one two three
```

**Output:**

```
Before shift: one two three
After shift: two three
```

---

### **Practical Use Cases**

- Parsing input files or operation modes
- Customizing behavior of scripts using arguments
- Passing paths, flags, or options


---

### **13. Exit Status of a Command**

In Linux, every command executed returns an **exit status code** to indicate success or failure. This code can be accessed using the special variable `$?`.

---

### **Exit Code Conventions**

| Exit Code | Meaning             |
|-----------|---------------------|
| 0         | Success             |
| Non-zero  | Failure (1–255)     |

---

### **Using `$?`**

The `$?` variable holds the **exit status** of the **last executed command**.

```bash
#!/bin/bash
ls /home
echo "Exit Status: $?"

ls /notexist
echo "Exit Status: $?"
```

**Output:**

```
(home directory listing)
Exit Status: 0
ls: cannot access '/notexist': No such file or directory
Exit Status: 2
```

---

### **Using exit Status in Conditionals**

```bash
#!/bin/bash
cp file1.txt /some/folder/
if [ $? -eq 0 ]; then
    echo "Copy successful"
else
    echo "Copy failed"
fi
```

---

### **The `exit` Command in Scripts**

You can use `exit N` to manually set the exit status of your script:

```bash
#!/bin/bash
echo "This is a script"
exit 1
```

**Run:**

```bash
bash script.sh
echo $?
```

**Output:**

```
This is a script
1
```

---

### **Use Cases**

- Scripting logic flow
- Automation checks
- Error handling

---

### **14. Shell Types**

There are several types of **shells** in Linux. Each shell is a command-line interpreter offering different features and syntax.

---

#### **Common Shells in Linux:**

| Shell        | Command               | Features                                               |
|--------------|-----------------------|--------------------------------------------------------|
| **Bourne Shell (sh)**  | `/bin/sh`             | Original shell, simple syntax                         |
| **Bourne Again Shell (bash)** | `/bin/bash`       | Default shell in most Linux distros, scripting-friendly |
| **C Shell (csh)**     | `/bin/csh`            | C-like syntax, popular in academic settings           |
| **Korn Shell (ksh)**  | `/bin/ksh`            | Combines features of sh and csh                       |
| **Z Shell (zsh)**     | `/bin/zsh`            | Advanced, user-friendly, supports themes, plugins     |
| **Dash Shell (dash)** | `/bin/dash`           | Lightweight sh-compatible shell, used for boot scripts|

---

### **How to Find Current Shell**

```bash
echo $SHELL
```

---

### **Changing Shell Temporarily**

```bash
bash
```

To go back:

```bash
exit
```

---

### **Changing Default Shell Permanently**

```bash
chsh -s /bin/zsh  # or /bin/bash etc.
```

---

### **Shell Script Features**

1. **Interpreted, not compiled**
2. **Portable across UNIX systems**
3. **Supports variables, functions, loops, and conditionals**
4. **Can call external programs**
5. **Ideal for automation and repetitive tasks**

---

### **Shebang (#!)**

First line of every script should define the shell:

```bash
#!/bin/bash
```

This tells the OS which shell to use to interpret the script.

---

### **Running a Shell Script**

```bash
chmod +x script.sh    # Make it executable
./script.sh           # Run the script
```

---

### **15. Executing a Shell Script**

#### **Steps to Execute a Shell Script:**

1. **Create the script:**
   ```bash
   nano myscript.sh
   ```

2. **Add content:**
   ```bash
   #!/bin/bash
   echo "Hello from the script!"
   ```

3. **Make the script executable:**
   ```bash
   chmod +x myscript.sh
   ```

4. **Run the script:**
   ```bash
   ./myscript.sh
   ```

---

### **16. System and User-Defined Variables**

#### **System Variables:**

- Provided by the shell itself.
- Usually in uppercase.
- Examples:
  ```bash
  echo $HOME      # Shows home directory
  echo $USER      # Shows current user
  echo $SHELL     # Shows default shell
  echo $$         # Shows PID of the current shell
  ```

#### **User-Defined Variables:**

- Created by users to store custom data.

```bash
name="Alice"
echo $name
```

- No space around `=`.
- Use `unset` to delete:
  ```bash
  unset name
  ```

---

### **Declaring Constants (readonly):**

```bash
readonly pi=3.14
```

---

### **17. `expr` Command**

`expr` is used to evaluate expressions (arithmetic or string) in shell scripts.

#### **Arithmetic Operations:**

```bash
a=10
b=5

result=`expr $a + $b`
echo "Sum: $result"

result=`expr $a - $b`
echo "Difference: $result"

result=`expr $a \* $b`
echo "Product: $result"

result=`expr $a / $b`
echo "Quotient: $result"
```

> Note: Multiplication `*` must be escaped as `\*`.

#### **String Operations:**

```bash
str1="Hello"
str2="World"

# Concatenation (done with echo usually)
echo "$str1 $str2"

# String length
len=`expr length "$str1"`
echo "Length: $len"

# Substring
substr=`expr substr "$str1" 2 3`
echo "Substring: $substr"
```

---

### **18. Command Substitution**

Used to execute a command and store its output in a variable.

#### **Syntax 1: Using backticks `` ` ``**
```bash
today=`date`
echo "Today's date is: $today"
```

#### **Syntax 2: Using `$()`**
```bash
hostname_val=$(hostname)
echo "Hostname: $hostname_val"
```

---

### **19. Escape Sequence Characters**

Escape sequences are special characters preceded by a backslash `\` used to control formatting in output.

#### **Common Escape Sequences:**

| Escape | Description                     |
|--------|---------------------------------|
| `\n`   | New line                        |
| `\t`   | Horizontal tab                  |
| `\b`   | Backspace                       |
| `\r`   | Carriage return                 |
| `\\`   | Backslash                       |
| `\"`   | Double quote                    |
| `\'`   | Single quote                    |

#### **Example:**

```bash
echo -e "Hello\tWorld\nWelcome to Linux"
```

> Note: `-e` is used with `echo` to enable interpretation of escape characters.

---

### **20. Shell Script Arguments**

Arguments passed to a shell script from the command line can be accessed using **positional parameters**.

#### **Example Script: `args.sh`**

```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
echo "All arguments: $@"
```

#### **Run Script:**
```bash
bash args.sh hello world
```

**Output:**
```
Script name: args.sh
First argument: hello
Second argument: world
Total arguments: 2
All arguments: hello world
```

---

### **21. Positional Parameters**

Positional parameters are special variables `$1`, `$2`, ..., `$9`, `${10}`, etc., that hold the values of the arguments passed to a shell script.

#### **Special Positional Parameters:**

| Parameter | Meaning                                      |
|----------:|----------------------------------------------|
| `$0`      | Name of the script                           |
| `$1-$9`   | First to ninth arguments                     |
| `${10}`   | Tenth argument (note curly braces needed)    |
| `$#`      | Number of arguments passed                   |
| `$@`      | All arguments as separate words              |
| `$*`      | All arguments as a single word               |

---

### **22. `test` Command**

The `test` command is used to evaluate expressions like file type checks, string comparisons, and numerical comparisons.

#### **Syntax:**

```bash
test expression
```
or
```bash
[ expression ]
```

> The spaces are **mandatory** inside the square brackets.

---

#### **23. File Test Operators:**

| Expression    | Description                    |
|---------------|--------------------------------|
| `-e file`     | File exists                    |
| `-f file`     | File is a regular file         |
| `-d file`     | File is a directory            |
| `-r file`     | File has read permission       |
| `-w file`     | File has write permission      |
| `-x file`     | File has execute permission    |

**Example:**

```bash
if [ -f myfile.txt ]; then
    echo "File exists"
else
    echo "File not found"
fi
```

---

### **24. String Tests**

String comparisons are performed using the `test` command or `[ ... ]` in shell scripting.

#### **Operators and Their Meaning:**

| Expression                  | Description                            |
|-----------------------------|----------------------------------------|
| `-z string`                | True if the string is **empty**         |
| `-n string`                | True if the string is **not empty**     |
| `string1 = string2`        | True if both strings are **equal**      |
| `string1 != string2`       | True if both strings are **not equal**  |
| `[ string ]`               | True if string is **not null**          |

#### **Example:**

```bash
#!/bin/bash
echo "Enter a string:"
read str
if [ -z "$str" ]; then
    echo "You entered an empty string."
else
    echo "You entered: $str"
fi
```

---

### **25. Numeric Tests**

Used for comparing integers.

#### **Operators and Meaning:**

| Operator | Description                   |
|----------|-------------------------------|
| `-eq`    | Equal                         |
| `-ne`    | Not equal                     |
| `-gt`    | Greater than                  |
| `-lt`    | Less than                     |
| `-ge`    | Greater than or equal to      |
| `-le`    | Less than or equal to         |

#### **Example:**

```bash
#!/bin/bash
echo "Enter two numbers:"
read a b
if [ $a -gt $b ]; then
    echo "$a is greater than $b"
else
    echo "$b is greater than or equal to $a"
fi
```

---

# Unit -IV  
- Conditional Control Structures-if statement, case statement, Looping Control Structure-while, until, for, statements.  
- Filters, Stream editor SED and AWK, Linux System Communication: Introduction, write, read, wall commands, sending and handling mails. System Administration: Roles of a System Administrator.  

---

## 🔹 **1. Conditional Control Structures – if Statement**

### ✅ What is an `if` statement in shell scripting?

The `if` statement is used to make decisions in shell scripts. It evaluates a **condition**, and based on whether it's true or false, it executes corresponding commands.

---

### 🧱 **Basic Syntax of if**

```bash
if [ condition ]
then
    # commands to execute if condition is true
fi
```

### 🧱 **if-else Syntax**

```bash
if [ condition ]
then
    # true block
else
    # false block
fi
```

### 🧱 **if-elif-else Syntax**

```bash
if [ condition1 ]
then
    # commands if condition1 is true
elif [ condition2 ]
then
    # commands if condition2 is true
else
    # commands if none are true
fi
```

---

### 💡 Note:
- Always **leave spaces** around square brackets: `[ condition ]`
- You can also use `[[ ... ]]` which allows for advanced pattern matching.

---

### 📌 **Example 1: Check if a number is positive**

```bash
#!/bin/bash

echo "Enter a number:"
read num

if [ $num -gt 0 ]
then
    echo "The number is positive."
else
    echo "The number is not positive."
fi
```

---

### 📌 **Example 2: Check login user**

```bash
#!/bin/bash

if [ "$USER" == "root" ]
then
    echo "Welcome, Root user!"
else
    echo "You are not root!"
fi
```

---

### 📌 **Example 3: Grading using if-elif-else**

```bash
#!/bin/bash

echo "Enter your score:"
read score

if [ $score -ge 90 ]; then
    echo "Grade: A"
elif [ $score -ge 75 ]; then
    echo "Grade: B"
elif [ $score -ge 60 ]; then
    echo "Grade: C"
else
    echo "Grade: F"
fi
```

---

## 🔹 **2. Conditional Control Structures – `case` Statement**

### ✅ What is a `case` statement?

The `case` statement is used to execute different blocks of code **based on the value of a variable or expression**. It is similar to the `switch` statement in other programming languages like C/C++ or Java.

---

### 🧱 **Syntax of `case` Statement**

```bash
case variable in
    pattern1)
        # commands
        ;;
    pattern2)
        # commands
        ;;
    ...
    *)
        # default commands (optional)
        ;;
esac
```

### 🔸 `;;` indicates the end of that case block  
### 🔸 `*` is the default pattern (like `else`)

---

### 📌 **Example 1: Basic Menu System**

```bash
#!/bin/bash

echo "Enter your choice: "
echo "1. List files"
echo "2. Show date"
echo "3. Who is logged in"
read choice

case $choice in
    1)
        ls
        ;;
    2)
        date
        ;;
    3)
        who
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

---

### 📌 **Example 2: Vowel or Consonant**

```bash
#!/bin/bash

echo "Enter a letter:"
read letter

case $letter in
    [aeiouAEIOU])
        echo "$letter is a vowel."
        ;;
    [a-zA-Z])
        echo "$letter is a consonant."
        ;;
    *)
        echo "Not a letter."
        ;;
esac
```

---

### 📌 **Example 3: Simple Calculator**

```bash
#!/bin/bash

echo "Enter two numbers:"
read a
read b

echo "Choose operation: add / sub / mul / div"
read op

case $op in
    add)
        echo "Result: $((a + b))"
        ;;
    sub)
        echo "Result: $((a - b))"
        ;;
    mul)
        echo "Result: $((a * b))"
        ;;
    div)
        echo "Result: $((a / b))"
        ;;
    *)
        echo "Invalid operation"
        ;;
esac
```

---

## 🔹 **3. Looping Control Structures**

Looping control structures allow a script to **repeat a set of commands** based on a condition. Linux shell provides:

- `while` loop
- `until` loop
- `for` loop

---

### 🌀 **1. `while` Loop**

#### ✅ Syntax:

```bash
while [ condition ]
do
    # commands
done
```

#### 🔄 Loop executes **as long as the condition is true**.

---

#### 📌 Example: Print 1 to 5

```bash
#!/bin/bash

i=1
while [ $i -le 5 ]
do
    echo $i
    i=$((i + 1))
done
```

---

### 🌀 **2. `until` Loop**

#### ✅ Syntax:

```bash
until [ condition ]
do
    # commands
done
```

#### 🔄 Loop executes **until the condition becomes true** (i.e., while the condition is false).

---

#### 📌 Example: Print 1 to 5 using `until`

```bash
#!/bin/bash

i=1
until [ $i -gt 5 ]
do
    echo $i
    i=$((i + 1))
done
```

---

### 🌀 **3. `for` Loop**

#### ✅ Syntax:

```bash
for variable in list
do
    # commands
done
```

---

#### 📌 Example: Loop over a list of words

```bash
#!/bin/bash

for word in Apple Banana Cherry
do
    echo "Fruit: $word"
done
```

---

#### 📌 Example: Loop over a sequence of numbers

```bash
#!/bin/bash

for i in {1..5}
do
    echo $i
done
```

---

#### 📌 C-style for loop:

```bash
#!/bin/bash

for (( i=1; i<=5; i++ ))
do
    echo $i
done
```

---

## 🔹 **4. Filters, Stream Editor (`sed`), and `awk`**

### 🌊 What are Filters?

A **filter** is a program that **takes input, processes it, and gives output**. They are commonly used in pipelines with `|`.

### 🧰 Common Filter Commands:

| Command | Description |
|--------|-------------|
| `cat`  | Displays content of files |
| `head` | Displays the first few lines of a file |
| `tail` | Displays the last few lines |
| `cut`  | Cuts columns or fields from input |
| `sort` | Sorts lines of text |
| `uniq` | Removes duplicate lines (needs sorted input) |
| `tr`   | Translates characters |
| `wc`   | Word count, line count, etc. |
| `grep` | Searches lines matching a pattern |

---

### 🧵 Example: Using Filters in Pipeline

```bash
cat names.txt | sort | uniq | wc -l
```

🔹 This shows how many **unique sorted names** are in `names.txt`.

---

## 🧽 `sed` – Stream Editor

`sed` is used for **automatic editing** of streams or files.

### ✅ Syntax:

```bash
sed [options] 'command' file
```

### 🧪 Common Examples:

#### 📌 Print only lines containing "hello":
```bash
sed -n '/hello/p' file.txt
```

#### 📌 Delete line 2:
```bash
sed '2d' file.txt
```

#### 📌 Replace "apple" with "orange":
```bash
sed 's/apple/orange/' file.txt
```

- `s` = substitute
- First occurrence only
- Use `g` for all occurrences:

```bash
sed 's/apple/orange/g' file.txt
```

---

## 📊 `awk` – Pattern Scanning and Processing Language

`awk` processes **fields and records** from input (usually lines and words).

### ✅ Syntax:

```bash
awk 'pattern { action }' file
```

### 🧪 Common Examples:

#### 📌 Print 1st column of a file:

```bash
awk '{ print $1 }' file.txt
```

#### 📌 Print lines where 3rd field is greater than 50:

```bash
awk '$3 > 50 { print $0 }' data.txt
```

#### 📌 Print sum of 2nd column:

```bash
awk '{ sum += $2 } END { print "Total:", sum }' file.txt
```

---

## 📡 **Linux System Communication**

Linux supports real-time **user-to-user communication** and **system-wide messaging** via command-line utilities.

---

### 💬 `write` – Send a message to another user

#### ✅ Syntax:

```bash
write username [terminal]
```

#### 📌 Example:

```bash
write alice
```

You can then type messages. Press `Ctrl + D` to end.

#### 🔐 Requirements:
- The recipient must be **logged in**.
- The recipient's terminal must **accept messages** (see `mesg` command below).

---

### 🧾 `read` – Take input from the user

`read` is a shell built-in used to take **user input**.

#### ✅ Syntax:

```bash
read variable_name
```

#### 📌 Example:

```bash
echo "Enter your name:"
read name
echo "Hello, $name!"
```

---

### 🧱 `wall` – Broadcast a message to all users

`wall` stands for “**write all**”. It sends a message to **all logged-in users**.

#### ✅ Syntax:

```bash
wall "System will go down for maintenance at 6 PM."
```

- Used mostly by **administrators** to send alerts.

---

### 📧 Sending and Handling Mails (using `mail`)

#### ✅ Syntax to send a mail:

```bash
mail -s "Subject Here" username
```

After typing the message, press `Ctrl + D` to send.

#### ✅ Reading mail:

```bash
mail
```

You’ll see a list of messages. To read message 1:

```bash
1
```

To delete message 1:

```bash
d 1
```

To exit mail:

```bash
q
```

---

### ✍️ Example Session:

```bash
$ mail -s "Hello from Admin" bob
Hi Bob,
Please logout by 6 PM today.
Thanks!
<Ctrl + D>
```

---

## 👨‍💻 **System Administration in Linux**

System Administration refers to the **management and maintenance** of a Linux system to ensure smooth operation, security, and performance. A **System Administrator (SysAdmin)** is responsible for a wide range of tasks.

---

### ✅ **Roles and Responsibilities of a System Administrator**

---

### 🛠 1. **User Management**
- **Create/Delete/Modify** users and groups using commands like:
  - `adduser`, `useradd`, `deluser`, `passwd`, `usermod`, `groupadd`
- Example:
  ```bash
  sudo useradd john
  sudo passwd john
  ```

---

### 📂 2. **File System Management**
- Creating, formatting, and mounting partitions using:
  - `mkfs`, `mount`, `umount`, `df`, `du`
- Managing disk usage and permissions.
- Example:
  ```bash
  df -h       # Shows disk usage
  mount /dev/sdb1 /mnt/data
  ```

---

### 🖥 3. **Process Management**
- Monitor and control processes using:
  - `ps`, `top`, `htop`, `kill`, `nice`, `renice`
- Example:
  ```bash
  ps aux | grep firefox
  kill -9 1234
  ```

---

### 📬 4. **Service and Daemon Management**
- Start/stop services using:
  - `systemctl`, `service`
- Example:
  ```bash
  sudo systemctl restart apache2
  sudo service ssh status
  ```

---

### 🔐 5. **Security Management**
- Set up firewalls (`ufw`, `iptables`)
- Manage file permissions and ownership (`chmod`, `chown`)
- Configure SSH access, password policies, and user privileges.

---

### 🌐 6. **Network Configuration**
- Configure IP addresses, DNS, gateways
- Use tools like `ip`, `ifconfig`, `ping`, `netstat`, `ss`, `nmap`
- Example:
  ```bash
  ip a      # Show network interfaces
  ping google.com
  ```

---

### 🧪 7. **Backup and Recovery**
- Automate backups using tools like `rsync`, `tar`, `cron`, `scp`
- Example:
  ```bash
  tar -czvf backup.tar.gz /home/user/
  ```

---

### 📅 8. **Job Scheduling**
- Use `cron` for periodic tasks
- `at` for one-time tasks
- Example:
  ```bash
  crontab -e
  0 5 * * * /home/user/backup.sh
  ```

---

### 📊 9. **System Monitoring**
- Monitor system performance with tools like:
  - `top`, `htop`, `iotop`, `vmstat`, `dstat`
- Logging via `/var/log/`

---

### 📦 10. **Package Management**
- Install, upgrade, remove packages using:
  - `apt`, `dnf`, `yum`, `pacman`, etc.
- Example:
  ```bash
  sudo apt update
  sudo apt install nginx
  ```

---

