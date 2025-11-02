| Resource                                                                           | What’s good about it / why it’s useful                                                                                               |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **“NASM Tutorial” by Benjamin Ray Seyfarth (LMU)**                                 | Covers standalone programs & integration with C, for x86-64. Good first steps. ([cs.lmu.edu][1])                                     |
| **Asmtutor.com**                                                                   | A series of small lessons (Hello World, loops, system calls, file I/O, etc.) using NASM on Linux. Very hands-on. ([asmtutor.com][2]) |
| **“X86 Assembly From the Ground Up using NASM” (Chris Eagle & Jonathan Bartlett)** | A full book (PDF) that starts from basics up. Very good structured learning. ([United States Naval Academy][3])                      |
| **TutorialsPoint: Assembly Programming Tutorial**                                  | Good general assembly concepts. Not always NASM-specific, but helps with the foundations. ([TutorialsPoint][4])                      |
| **“Introduction to NASM Programming” – ICS312 course material (Hawaii)**           | University-level course material / lecture slides. Good for formal learning. ([courses.ics.hawaii.edu][5])                           |
| **“Resources to help me learn x64 and x86 NASM” GitHub repo**                      | Lots of example code and links. Good place to see real code snippets. ([GitHub][6])                                                  |
| **Learn x86-64 assembly by writing a GUI from scratch (blog)**                     | More advanced / fun project. Helps you see how to build something real in assembly. ([gaultier.github.io][7])                        |
| **YouTube playlists** (e.g. “x86 Assembly with NASM”)                              | Visual learners + seeing code in action is very helpful. ([YouTube][8])                                                              |

[1]: https://cs.lmu.edu/~ray/notes/nasmtutorial/?utm_source=chatgpt.com "NASM Tutorial"
[2]: https://asmtutor.com/?utm_source=chatgpt.com "asmtutor.com: NASM Assembly Language Tutorials"
[3]: https://www.usna.edu/Users/cs/norine/spring25/SI459/resources/X86NasmBook.pdf?utm_source=chatgpt.com "X86 Assembly From the Ground Up using NASM"
[4]: https://www.tutorialspoint.com/assembly_programming/index.htm?utm_source=chatgpt.com "Assembly Programming Tutorial"
[5]: https://courses.ics.hawaii.edu/ReviewICS312/morea/FirstProgram/ics312_nasm_first_program.pdf?utm_source=chatgpt.com "Introduction to NASM Programming"
[6]: https://github.com/Lydxn/NASM-Resources?utm_source=chatgpt.com "Resources to help me learn x64 and x86 NASM (mostly x64)"
[7]: https://gaultier.github.io/blog/x11_x64.html?utm_source=chatgpt.com "Learn x86-64 assembly by writing a GUI from scratch"
[8]: https://www.youtube.com/playlist?list=PL2EF13wm-hWCoj6tUBGUmrkJmH1972dBB&utm_source=chatgpt.com "x86 Assembly with NASM"


# 🖥️ 1. **General-Purpose Registers (GPRs)**

The backbone of the CPU.

### Registers

* **RAX, RBX, RCX, RDX, RSP, RBP, RSI, RDI, R8–R15** (16 total).

### Sizes

* **64-bit full register** → e.g., RAX
* **32-bit low part** → EAX
* **16-bit low part** → AX
* **8-bit low/high** → AL (low 8 bits), AH (high 8 bits, only for RAX–RDX).
* **R8–R15** → also have R8B (8b), R8W (16b), R8D (32b).

### Usage

* **RAX** → accumulator (often return value of functions).
* **RBX** → base register (callee-saved).
* **RCX** → counter register (used in loops, shifts, and `rep` string ops).
* **RDX** → data register (extra multiplier/divisor, I/O).
* **RSI/RDI** → source/destination pointers (used in memory/string instructions).
* **RSP** → stack pointer (points to top of stack).
* **RBP** → base pointer (used in stack frames).
* **R8–R15** → extra general-purpose registers (added in x86-64).

👉 Example:

```asm
mov rax, 5
mov rbx, 10
add rax, rbx   ; RAX = 15
```

---

# 🖥️ 2. **Instruction Pointer + Flags**

* **RIP** (64-bit) → holds the address of the *next instruction*.
* **RFLAGS** (64-bit) → collection of status & control flags.

### Key flags:

* **CF**: Carry flag (unsigned overflow).
* **ZF**: Zero flag (result is zero).
* **SF**: Sign flag (negative result).
* **OF**: Overflow flag (signed overflow).
* **IF**: Interrupt enable flag.
* **DF**: Direction flag (controls string operation direction).

👉 Example:

```asm
cmp rax, rbx   ; compare RAX and RBX
je equal       ; jump if ZF=1
```

---

# 🖥️ 3. **Segment Registers (16-bit)**

Legacy but still exist.

* **CS** (Code Segment)
* **DS** (Data Segment)
* **SS** (Stack Segment)
* **ES** (Extra Segment)
* **FS, GS** (Extra segments — in 64-bit mode used for TLS = Thread-Local Storage).

👉 On Linux x86-64, FS/GS base addresses are heavily used by system libraries and threads.

---

# 🖥️ 4. **Floating-Point Unit (x87 FPU)**

Old-school floating-point coprocessor (still there for compatibility).

* **ST0–ST7** → 8 registers, each **80-bit extended precision**.
* Organized as a **stack** (push/pop style).

👉 Example:

```asm
fld qword [num1]   ; push float
fld qword [num2]
fadd               ; ST0 = num1 + num2
fstp qword [result]
```

---

# 🖥️ 5. **MMX Registers (64-bit SIMD)**

Introduced in the 90s. Obsolete but still present.

* **MM0–MM7** (64-bit each).
* Used for **packed integer SIMD**:

  * 8 × 8-bit integers
  * 4 × 16-bit integers
  * 2 × 32-bit integers

👉 Example: Add 8 bytes at once.

---

# 🖥️ 6. **SIMD / Vector Registers**

Your CPU supports **up to AVX-512**, so you have the *full hierarchy*:

### **XMM0–XMM31 (128-bit)**

* First appeared with SSE.
* Can hold:

  * 4 × 32-bit floats
  * 2 × 64-bit doubles
  * 16 × 8-bit integers

### **YMM0–YMM31 (256-bit)**

* Extension of XMM.
* Can hold:

  * 8 × 32-bit floats
  * 4 × 64-bit doubles
  * 32 × 8-bit integers

### **ZMM0–ZMM31 (512-bit)**

* Full AVX-512 registers.
* Can hold:

  * 16 × 32-bit floats
  * 8 × 64-bit doubles
  * 64 × 8-bit integers

👉 Example (conceptual):

```asm
vmovaps zmm0, [a]   ; load 16 floats
vmovaps zmm1, [b]
vaddps zmm2, zmm0, zmm1  ; add them all at once
```

---

# 🖥️ 7. **Mask Registers (AVX-512)**

* **K0–K7** (64-bit each).
* Used to *selectively enable lanes* in AVX-512 instructions.

👉 Example: Only add the first 8 elements of a vector.

---

# 🖥️ 8. **System Registers**

### **Control Registers**

* **CR0** → CPU mode control (enables paging, protection).
* **CR2** → holds page fault linear address.
* **CR3** → page table base address.
* **CR4** → extended features (SSE, SMAP, etc.).
* **CR8** → task priority register (interrupt priority).

### **Debug Registers**

* **DR0–DR3** → hardware breakpoints.
* **DR6, DR7** → debug status/control.

👉 Used in debugging, not normal programming.

### **MSRs (Model-Specific Registers)**

* Vendor-defined registers for performance, power, CPU ID, etc.
* Accessed with `rdmsr`/`wrmsr`.

---

# 📊 **Cheat Sheet for Your CPU (i5-11300H)**

| Class           | Names                      | Size | Count | Purpose                  |
| --------------- | -------------------------- | ---- | ----- | ------------------------ |
| GPRs            | RAX…R15                    | 64b  | 16    | General integer work     |
| Instruction Ptr | RIP                        | 64b  | 1     | Next instruction         |
| Flags           | RFLAGS                     | 64b  | 1     | Status/control flags     |
| Segments        | CS, DS, SS, ES, FS, GS     | 16b  | 6     | Memory segmentation, TLS |
| FPU             | ST0–ST7                    | 80b  | 8     | Floating-point stack     |
| MMX             | MM0–MM7                    | 64b  | 8     | Packed integer SIMD      |
| SIMD (SSE)      | XMM0–XMM31                 | 128b | 32    | Packed int/float SIMD    |
| SIMD (AVX)      | YMM0–YMM31                 | 256b | 32    | Wider SIMD               |
| SIMD (AVX-512)  | ZMM0–ZMM31                 | 512b | 32    | Huge SIMD vectors        |
| Mask (AVX-512)  | K0–K7                      | 64b  | 8     | Lane masking             |
| Control         | CR0–CR4, CR8               | 64b  | 5     | Paging, protection       |
| Debug           | DR0–DR7                    | 64b  | 8     | Hardware breakpoints     |
| MSRs            | Many (e.g., perf counters) | 64b  | 100s  | CPU-specific features    |

---

✅ That’s every register you have.
Your chip basically has **everything from 8086 → SSE → AVX-512**, except that **some OEMs disable AVX-512** in firmware.

---
