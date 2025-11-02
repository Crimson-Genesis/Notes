# What “scalar” vs “vector” means (short)

* **Scalar** — a single value processed at a time (e.g. one `int` or one `float`).
  Example: `a = b + c;` — one add, one result.
* **Vector** — many values packed together and processed in parallel by one instruction (SIMD).
  Example: add 8 floats at once in a 256-bit register.

# Why the distinction matters

Scalar code does one operation per instruction. Vector (SIMD) code does N operations per instruction (N = lane count). That’s how CPUs get big speedups for data-parallel workloads (multimedia, ML, signal processing, etc.).

---

# Key terms (quick reference)

* **Lane** — one element inside a vector register (e.g. one of 8 lanes in a 256-bit register when lanes are 32-bit floats).
* **Lane width / element size** — size of each lane (8/16/32/64 bits).
* **Vector width** — overall register size (128/256/512 bits for XMM/YMM/ZMM).
* **Packed** — vector holds multiple *packed* elements of same type (e.g. packed floats).
* **Scalar instruction** — operates on a scalar register / single element (e.g. `ADDSS` for single float).
* **Packed instruction** — operates on packed elements (e.g. `ADDPS` for packed floats).
* **Broadcast** — replicate a scalar across all lanes.
* **Mask / predication** — per-lane enable/disable (AVX-512 k masks). Allows conditional updates without branches.
* **Gather / Scatter** — load/store non-contiguous elements using vector of indices (gather reads, scatter writes).
* **Reduction (horizontal op)** — combine lanes into single scalar (sum of vector elements).
* **AoS vs SoA**:

  * AoS (Array of Structs): `struct {x,y,z}; arr[]` — bad for vectorizing over a field.
  * SoA (Struct of Arrays): `float x[], y[], z[]` — better for SIMD.

---

# Data-level vs other parallelism (where vector fits)

* **SISD** — single instruction single data (scalar CPU model).
* **SIMD** — single instruction multiple data (vector lanes).
* **MIMD / multithreading** — multiple threads each doing different work (task-level).
* **ILP (Instruction-level parallelism)** — CPU executes independent instructions in parallel (out-of-order).

SIMD is *data-level parallelism*. Combine SIMD + multithreading for big speedups.

---

# Visual: scalar vs vector loop

Scalar:

```c
for (i=0; i<n; ++i)
    c[i] = a[i] + b[i];   // one add per loop
```

Vector (pseudo SIMD):

```
for (i=0; i<n; i+=8) {
    vA = load8(a + i)
    vB = load8(b + i)
    vC = vA + vB         // adds 8 floats in parallel
    store8(c + i, vC)
}
```

One `vA + vB` does 8 additions if lanes=8 → up to 8× faster (ignoring memory limits).

---

# Examples (C intrinsics)

AVX2 (256-bit, 8 × float):

```c
#include <immintrin.h>

void add_avx2(float *a, float *b, float *c, int n){
  int i;
  for(i=0; i<n; i+=8){
    __m256 va = _mm256_loadu_ps(a + i);
    __m256 vb = _mm256_loadu_ps(b + i);
    __m256 vc = _mm256_add_ps(va, vb);
    _mm256_storeu_ps(c + i, vc);
  }
}
```

AVX-512 (512-bit, 16 × float) — with mask:

```c
#include <immintrin.h>

void add_avx512(float *a, float *b, float *c, int n){
  int i;
  for(i=0;i<n;i+=16){
    __m512 va = _mm512_loadu_ps(a + i);
    __m512 vb = _mm512_loadu_ps(b + i);
    __m512 vc = _mm512_add_ps(va, vb);
    _mm512_storeu_ps(c + i, vc);
  }
}
```

Masked (handles tail):

```c
__mmask16 tail = (1ULL << rem) - 1; // rem < 16
_mm512_mask_storeu_ps(c + i, tail, vc);
```

---

# Special ops & patterns

* **Broadcast**: load scalar and replicate to all lanes (useful for adding scalar to vector).
* **Masking**: only update lanes where mask bit = 1 (no branch).
* **Gather/Scatter**: read/write elements using index vector (slower than contiguous loads).
* **Horizontal ops**: reduce vector to scalar (e.g. sum all lanes).
* **Shuffle / permute**: rearrange lanes inside vector.

---

# Practical constraints / pitfalls

* **Memory-bound**: sometimes memory throughput, not ALU ops, limits performance.
* **Alignment**: aligned loads/stores can be faster. Use `_mm256_load_ps` vs `_mm256_loadu_ps` when aligned.
* **Remainder handling**: tail elements (n not divisible by lanes) must be handled (masks or scalar tail).
* **Branching inside loops**: hurts vectorization. Prefer predication (masks) or reorganize data.
* **Precision & correctness**: floating-point reassociation changes results (vectorization can change order of ops).
* **Compiler auto-vectorization is not perfect**: sometimes need intrinsics or restructure code.

---

# How compilers/vectorizers fit in

* Compilers (GCC/clang/ICC) can auto-vectorize loops when safe. Flags: `-O3 -march=native -ftree-vectorize`.
* You can request reports: `-fopt-info-vec` (GCC) to see what was vectorized.
* Intrinsics give you explicit control — use when you need deterministic SIMD.

---

# How this maps to GDB / registers you saw

* `xmm` = 128-bit (4×float) lanes
* `ymm` = 256-bit (8×float) lanes
* `zmm` = 512-bit (16×float) lanes
* Mask regs `k0..k7` = per-lane enables (AVX-512)
  When you step SIMD instructions in GDB, you’ll see those registers update — `zmm` contains all lanes, `xmm`/`ymm` are low parts.

---

# When to use scalar vs vector

* Use **scalar** when: code is branchy, memory access is random, or data size small.
* Use **vector** when: operations repeat over arrays, same operation on many elements (embarrassingly parallel), or performance-critical math/ML loops.

---

# Quick checklist to make code vector-friendly

1. Use simple loops operating over arrays (SoA layout helps).
2. Avoid loop-carried dependencies.
3. Align data if possible.
4. Let compiler auto-vectorize or use intrinsics if necessary.
5. Handle tail iterations with masks or scalar epilogue.
6. Measure (profile) — memory vs compute bound.

---
