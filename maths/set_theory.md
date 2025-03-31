# **Complete Set Operations and Properties Table**

| **Operation / Relation** | **Symbol / Law** | **Definition / Property** | **Equivalent Forms / Expressions** |
|----------------|-----------------|---------------------------|-----------------------------------|
| **Union** | \( A \cup B \) | Elements in \( A \), \( B \), or both | \( A \cup B = (A^C \cap B^C)^C \) (De Morgan) |
| **Intersection** | \( A \cap B \) | Elements in both \( A \) and \( B \) | \( A \cap B = (A^C \cup B^C)^C \) (De Morgan) |
| **Set Difference** | \( A - B \) or \( A \setminus B \) | Elements in \( A \) but not in \( B \) | \( A - B = A \cap B^C \) |
| **Symmetric Difference** | \( A \Delta B \) | Elements in \( A \) or \( B \), but not both | \( A \Delta B = (A \cup B) - (A \cap B) \) |
| **Complement** | \( A^C \) or \( \overline{A} \) | Elements not in \( A \) (relative to universal set \( U \)) | \( A^C = U - A \) |
| **Subset** | \( A \subseteq B \) | Every element in \( A \) is also in \( B \) | \( A \cap B = A \), \( A - B = \emptyset \) |
| **Proper Subset** | \( A \subset B \) | \( A \) is a subset of \( B \) and \( A \neq B \) | \( A \subseteq B \) and \( A \neq B \) |
| **Disjoint Sets** | \( A \cap B = \emptyset \) | No common elements between \( A \) and \( B \) | \( A - B = A \) and \( B - A = B \) |
| **Universal Set** | \( U \) | Contains all elements under consideration | \( A \cup A^C = U \) |
| **Power Set** | \( \mathcal{P}(A) \) | The set of all subsets of \( A \) | Contains \( 2^{|A|} \) elements if \( A \) has \( |A| \) elements |
| **Cartesian Product** | \( A \times B \) | Set of ordered pairs \( (a, b) \) where \( a \in A, b \in B \) | \( A \times B = \{ (a, b) \mid a \in A, b \in B \} \) |
| **Equivalent of Union** | \( A \cup B \) | Elements in either \( A \) or \( B \) | \( A \cup B = U - (A^C \cap B^C) \) |
| **Equivalent of Intersection** | \( A \cap B \) | Elements common to both \( A \) and \( B \) | \( A \cap B = U - ((A^C) \cup (B^C)) \) |
| **Equivalent of Difference** | \( A - B \) | Elements in \( A \) but not in \( B \) | \( A - B = A \cap B^C \), \( (A \cup B) - B \) |
| **Equivalent of Symmetric Difference** | \( A \Delta B \) | Elements in \( A \) or \( B \), but not both | \( A \Delta B = (A - B) \cup (B - A) \), \( (A \cup B) - (A \cap B) \) |
| **Equivalent of Complement** | \( A^C \) | Elements not in \( A \) | \( A^C = U - A \), \( (A \cup B)^C \) if \( A \cup B = U \) |
| **De Morgan’s Law (Union)** | \( (A \cup B)^C \) | Complement of union is the intersection of complements | \( (A \cup B)^C = A^C \cap B^C \) |
| **De Morgan’s Law (Intersection)** | \( (A \cap B)^C \) | Complement of intersection is the union of complements | \( (A \cap B)^C = A^C \cup B^C \) |

---

# **Set Identities and Their Equivalents**

| **Identity Name** | **Mathematical Expression** | **Definition** | **Equivalent Function Representation** |
|-------------------|---------------------------|---------------|-------------------------------------|
| **Idempotent Law** | \( A \cup A = A \)  | Taking union with itself doesn’t change the set. | \( \max(A, A) = A \) |
|  | \( A \cap A = A \) | Taking intersection with itself doesn’t change the set. | \( \min(A, A) = A \) |
| **Domination Law** | \( A \cup U = U \) | Any set combined with the universal set results in the universal set. | \( \max(A, 1) = 1 \) |
|  | \( A \cap \emptyset = \emptyset \) | Any set intersected with the empty set results in the empty set. | \( \min(A, 0) = 0 \) |
| **Identity Law** | \( A \cup \emptyset = A \) | Any set combined with the empty set remains unchanged. | \( \max(A, 0) = A \) |
|  | \( A \cap U = A \) | Any set intersected with the universal set remains unchanged. | \( \min(A, 1) = A \) |
| **Complement Law** | \( A \cup A^C = U \) | A set and its complement together form the universal set. | \( \max(A, 1 - A) = 1 \) |
|  | \( A \cap A^C = \emptyset \) | A set and its complement have no common elements. | \( \min(A, 1 - A) = 0 \) |
| **Double Complement Law** | \( (A^C)^C = A \) | Taking the complement twice returns the original set. | \( 1 - (1 - A) = A \) |
| **Commutative Law** | \( A \cup B = B \cup A \) | The order of union does not matter. | \( \max(A, B) = \max(B, A) \) |
|  | \( A \cap B = B \cap A \) | The order of intersection does not matter. | \( \min(A, B) = \min(B, A) \) |
| **Associative Law** | \( A \cup (B \cup C) = (A \cup B) \cup C \) | The way elements are grouped in union does not matter. | \( \max(A, \max(B, C)) = \max(\max(A, B), C) \) |
|  | \( A \cap (B \cap C) = (A \cap B) \cap C \) | The way elements are grouped in intersection does not matter. | \( \min(A, \min(B, C)) = \min(\min(A, B), C) \) |
| **Distributive Law** | \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \) | Intersection distributes over union. | \( \min(A, \max(B, C)) = \max(\min(A, B), \min(A, C)) \) |
|  | \( A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \) | Union distributes over intersection. | \( \max(A, \min(B, C)) = \min(\max(A, B), \max(A, C)) \) |
| **Absorption Law** | \( A \cup (A \cap B) = A \) | Union of a set with its intersection with another set is the set itself. | \( \max(A, \min(A, B)) = A \) |
|  | \( A \cap (A \cup B) = A \) | Intersection of a set with its union with another set is the set itself. | \( \min(A, \max(A, B)) = A \) |
| **De Morgan’s Laws** | \( (A \cup B)^C = A^C \cap B^C \) | The complement of a union is the intersection of the complements. | \( 1 - \max(A, B) = \min(1 - A, 1 - B) \) |
|  | \( (A \cap B)^C = A^C \cup B^C \) | The complement of an intersection is the union of the complements. | \( 1 - \min(A, B) = \max(1 - A, 1 - B) \) |

---
