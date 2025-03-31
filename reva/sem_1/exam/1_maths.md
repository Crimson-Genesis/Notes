# Maths

---
## **Unit 3: Random Variables and Probability Distribution**
Alright! Let's start with **Probability and its Properties.**  

---

# **Probability and its Properties**  

## **1️⃣ What is Probability?**  
Probability is the measure of how likely an event is to occur. It is given by:  

\[
P(E) = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Outcomes}}
\]

where **P(E)** is the probability of event **E** occurring.  

- Probability values **always range from 0 to 1**.  
- If **P(E) = 0**, the event is **impossible**.  
- If **P(E) = 1**, the event is **certain**.  

---

## **2️⃣ Types of Probability**
### **1. Classical Probability** (Theoretical Probability)  
- Based on equally likely outcomes.  
- Example: Tossing a fair coin → **P(Heads) = 1/2**.  

### **2. Empirical Probability** (Experimental Probability)  
- Based on experiments or past observations.  
- Example: If a cricket player scores 50 runs in 5 out of 10 matches, then  
  \[
  P(\text{scoring 50 runs}) = \frac{5}{10} = 0.5
  \]

### **3. Subjective Probability**  
- Based on personal judgment or experience.  
- Example: The probability of **rain tomorrow** based on a weather expert’s opinion.  

---

## **3️⃣ Important Probability Properties**  
### **1. Addition Rule**
For **two mutually exclusive events** A and B:  
\[
P(A \cup B) = P(A) + P(B)
\]
✅ Example: The probability of drawing a **King** or **Queen** from a deck of 52 cards:  
\[
P(King) = \frac{4}{52}, \quad P(Queen) = \frac{4}{52}
\]
\[
P(King \cup Queen) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52}
\]

If events **are not mutually exclusive**, we subtract the common part:  
\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

### **2. Multiplication Rule**
For **independent events** A and B:  
\[
P(A \cap B) = P(A) \times P(B)
\]
✅ Example: The probability of getting **two heads** when flipping two fair coins:  
\[
P(H \cap H) = P(H) \times P(H) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}
\]

### **3. Complement Rule**
The probability of an event **not happening** is:  
\[
P(A^c) = 1 - P(A)
\]
✅ Example: The probability of **not rolling a 6** on a fair die:  
\[
P(6) = \frac{1}{6}, \quad P(\text{Not 6}) = 1 - \frac{1}{6} = \frac{5}{6}
\]

---

### **4️⃣ Conditional Probability**  
- The probability of an event occurring **given that another event has already occurred**.  
- Formula:  
\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]
✅ Example: In a class of **10 students**, 4 like **Math**, 5 like **Science**, and **3 like both Math and Science**. If a randomly selected student **likes Science**, what is the probability they also like Math?  

\[
P(\text{Math} | \text{Science}) = \frac{P(\text{Math} \cap \text{Science})}{P(\text{Science})} = \frac{3}{5} = 0.6
\]

---

## **5️⃣ Real-Life Applications of Probability**
- **Weather Forecasting** (Rain prediction using past data)  
- **Stock Market Analysis** (Risk assessment for investments)  
- **Machine Learning** (Spam detection in emails)  
- **Sports Analytics** (Winning probability calculations)  

---
### **Practice Problems on Probability and Its Properties**  

#### **1️⃣ Basic Probability Problems**  
✅ **Q1**: A bag contains **5 red**, **3 blue**, and **2 green** balls. A ball is drawn at random. What is the probability that it is:  
a) Red?  
b) Not blue?  
c) Either red or green?  

🔹 **Answer**:  
- **Total balls** = 5 + 3 + 2 = **10**  
- **P(Red)** = \( \frac{5}{10} = 0.5 \)  
- **P(Not Blue)** = \( 1 - P(Blue) = 1 - \frac{3}{10} = \frac{7}{10} \)  
- **P(Red or Green)** = \( P(Red) + P(Green) = \frac{5}{10} + \frac{2}{10} = \frac{7}{10} \)  

---

✅ **Q2**: A fair die is rolled once. What is the probability of getting:  
a) A number greater than 4?  
b) An even number?  
c) Not a 3?  

🔹 **Answer**:  
- **Total outcomes** = {1, 2, 3, 4, 5, 6}  
- **P(>4)** = P(5 or 6) = \( \frac{2}{6} = \frac{1}{3} \)  
- **P(Even)** = P(2, 4, 6) = \( \frac{3}{6} = \frac{1}{2} \)  
- **P(Not 3)** = \( 1 - P(3) = 1 - \frac{1}{6} = \frac{5}{6} \)  

---

#### **2️⃣ Conditional Probability**  
✅ **Q3**: In a school, 60% of students study **Math**, and 40% study **Physics**. If 25% of students study **both subjects**, what is the probability that a student who studies Math also studies Physics?  

🔹 **Answer**:  
- Given: \( P(Math) = 0.6 \), \( P(Physics) = 0.4 \), \( P(Math \cap Physics) = 0.25 \)  
- **Conditional Probability Formula**:  
  \[
  P(Physics | Math) = \frac{P(Math \cap Physics)}{P(Math)}
  \]
  \[
  = \frac{0.25}{0.6} = \frac{5}{12} \approx 0.4167
  \]
So, the probability is **41.67%**.  

---

#### **3️⃣ Addition and Multiplication Rules**  
✅ **Q4**: A deck of 52 cards is shuffled, and one card is drawn. What is the probability that it is:  
a) A heart or a king?  
b) A red card and a face card?  

🔹 **Answer**:  
- **P(Heart or King)** = P(Heart) + P(King) - P(Heart & King)  
  \[
  = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
  \]  

- **P(Red & Face Card)** = \( \frac{6}{52} = \frac{3}{26} \)  
  (Since there are **6 red face cards**: **3 in hearts + 3 in diamonds**)  

---

#### **4️⃣ Complement Rule**  
✅ **Q5**: In a lottery, a person wins a prize with a probability of **0.2**. What is the probability that the person **does not win**?  

🔹 **Answer**:  
\[
P(\text{Not Winning}) = 1 - P(\text{Winning}) = 1 - 0.2 = 0.8
\]

---
### **Random Variables (Discrete & Continuous)**  

#### **1️⃣ What is a Random Variable?**  
A **random variable** is a function that assigns a numerical value to each outcome in a sample space.  

- **Discrete Random Variable**: Takes a **countable** number of values. Example: Number of heads in 5 coin flips.  
- **Continuous Random Variable**: Takes an **uncountable** number of values over an interval. Example: The weight of a randomly chosen person.  

---

### **2️⃣ Discrete Random Variables**  
A discrete random variable takes specific values with a certain probability.  

✅ **Example 1**: Let X be the number of heads in two coin tosses.  
- Sample Space: \( S = \{HH, HT, TH, TT\} \)  
- Possible values of \( X \) (Number of heads): **0, 1, 2**  
- Probability Distribution:  

| X  | 0   | 1   | 2   |
|----|-----|-----|-----|
| P(X) | \( \frac{1}{4} \) | \( \frac{2}{4} \) | \( \frac{1}{4} \) |

🔹 **Expectation (Mean)**:  
\[
E(X) = \sum X_i P(X_i) = 0 \times \frac{1}{4} + 1 \times \frac{2}{4} + 2 \times \frac{1}{4} = 1
\]
🔹 **Variance**:  
\[
Var(X) = E(X^2) - [E(X)]^2
\]

---

✅ **Example 2**: A die is rolled. Let \( X \) be the number shown on the die. Find the expected value of \( X \).  
- \( X \) takes values **1, 2, 3, 4, 5, 6**  
- \( P(X) = \frac{1}{6} \) for each value  
\[
E(X) = 1 \times \frac{1}{6} + 2 \times \frac{1}{6} + ... + 6 \times \frac{1}{6} = 3.5
\]

---

### **3️⃣ Continuous Random Variables**  
A continuous random variable takes an infinite number of values in a given range.  

✅ **Example 3**: Let \( X \) be the height of a randomly chosen student. It follows a **normal distribution** with mean \( \mu = 170 \) cm and variance \( \sigma^2 = 25 \).  
- The **probability** of \( X \) being exactly 170 cm is **zero**.  
- We calculate probabilities over **intervals**, e.g., \( P(165 < X < 175) \).  

\[
P(a \leq X \leq b) = \int_{a}^{b} f(x) dx
\]

where \( f(x) \) is the probability density function (PDF).  

---
### **Expectation and Variance of Distributions**  

#### **1️⃣ Expectation (Mean) of a Random Variable**  
The **expectation (or mean)** of a random variable \(X\) is the weighted average of all possible values, where the weights are the probabilities of those values occurring.  

✅ **Formula for Discrete Random Variables:**  
\[
E(X) = \sum X_i P(X_i)
\]
where:  
- \(X_i\) are the possible values of \(X\)  
- \(P(X_i)\) is the probability of \(X_i\)  

✅ **Formula for Continuous Random Variables:**  
\[
E(X) = \int_{-\infty}^{\infty} x f(x) dx
\]
where \( f(x) \) is the probability density function (PDF).  

---

### **2️⃣ Example - Expectation of a Discrete Random Variable**  
A fair six-sided die is rolled. Let \(X\) be the number that appears on the die. Find \(E(X)\).  

✅ **Solution:**  
- Possible values: \(X = 1, 2, 3, 4, 5, 6\)  
- Probability of each value: \( P(X = i) = \frac{1}{6} \) for \( i = 1, 2, 3, 4, 5, 6 \)  

Using the formula:  
\[
E(X) = 1 \times \frac{1}{6} + 2 \times \frac{1}{6} + 3 \times \frac{1}{6} + 4 \times \frac{1}{6} + 5 \times \frac{1}{6} + 6 \times \frac{1}{6}
\]
\[
E(X) = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5
\]
📌 **Interpretation:** The average number expected from rolling a die is **3.5**.  

---

### **3️⃣ Variance of a Random Variable**  
The **variance** of a random variable \(X\) measures the spread or dispersion of its values.  

✅ **Formula for Variance (Discrete):**  
\[
Var(X) = E(X^2) - [E(X)]^2
\]
where:  
- \( E(X^2) = \sum X_i^2 P(X_i) \)  

✅ **Formula for Variance (Continuous):**  
\[
Var(X) = \int_{-\infty}^{\infty} x^2 f(x) dx - (E(X))^2
\]

---

### **4️⃣ Example - Variance of a Discrete Random Variable**  
Using the same die roll example, let's find \( Var(X) \).  

✅ **Step 1: Compute \( E(X^2) \)**  
\[
E(X^2) = 1^2 \times \frac{1}{6} + 2^2 \times \frac{1}{6} + 3^2 \times \frac{1}{6} + 4^2 \times \frac{1}{6} + 5^2 \times \frac{1}{6} + 6^2 \times \frac{1}{6}
\]
\[
E(X^2) = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} = 15.17
\]

✅ **Step 2: Compute Variance**  
\[
Var(X) = E(X^2) - [E(X)]^2
\]
\[
Var(X) = 15.17 - (3.5)^2 = 15.17 - 12.25 = 2.92
\]

📌 **Interpretation:** The variance measures how much the dice rolls deviate from the mean **3.5**.  

---

### **5️⃣ Standard Deviation**  
The **standard deviation** is simply the square root of the variance:  
\[
\sigma = \sqrt{Var(X)}
\]

✅ **For the die roll example:**  
\[
\sigma = \sqrt{2.92} \approx 1.71
\]
📌 **Interpretation:** On average, the roll outcome deviates by **1.71** from the mean value **3.5**.  

---
### **Moments and Moment Generating Functions (MGF)**  

Moments are statistical measures that describe the shape of a probability distribution. They help in understanding the distribution’s **center, spread, skewness, and kurtosis**.  

---

## **1️⃣ Moments of a Random Variable**  
The \( r \)-th moment of a random variable \( X \) about the origin is defined as:  
\[
E(X^r) = \sum X_i^r P(X_i) \quad \text{(for discrete variables)}
\]
\[
E(X^r) = \int_{-\infty}^{\infty} x^r f(x) dx \quad \text{(for continuous variables)}
\]

The **first four moments** are particularly important:  

✅ **First Moment (\(E(X)\)): Mean** – Measures the central tendency.  
✅ **Second Moment (\(E(X^2)\)): Variance** – Measures the spread.  
✅ **Third Moment (\(E(X^3)\)): Skewness** – Measures symmetry of the distribution.  
✅ **Fourth Moment (\(E(X^4)\)): Kurtosis** – Measures whether data has heavy/light tails.  

---

## **2️⃣ Moment Generating Function (MGF)**  
The **Moment Generating Function (MGF)**, \( M_X(t) \), is a function that helps compute all moments of a random variable. It is defined as:  

\[
M_X(t) = E(e^{tX}) = \sum e^{tX_i} P(X_i) \quad \text{(for discrete variables)}
\]

\[
M_X(t) = \int_{-\infty}^{\infty} e^{tX} f(x) dx \quad \text{(for continuous variables)}
\]

📌 **Key Property:**  
If \( M_X(t) \) exists, then the \( r \)-th moment can be obtained by differentiating \( M_X(t) \) \( r \) times and evaluating at \( t=0 \):  

\[
E(X^r) = \frac{d^r M_X(t)}{dt^r} \Big|_{t=0}
\]

---

## **3️⃣ Example - Finding MGF for a Discrete Random Variable**  
Let \( X \) be a random variable with values **1, 2, 3** and corresponding probabilities **0.2, 0.5, 0.3**. Find its **moment generating function (MGF)**.  

✅ **Step 1: Apply MGF Formula**  
\[
M_X(t) = E(e^{tX}) = \sum e^{tX_i} P(X_i)
\]
\[
M_X(t) = e^{t(1)} \cdot 0.2 + e^{t(2)} \cdot 0.5 + e^{t(3)} \cdot 0.3
\]
\[
M_X(t) = 0.2 e^t + 0.5 e^{2t} + 0.3 e^{3t}
\]

✅ **Step 2: Compute Moments**  
- **First Moment (Mean):**  
  \[
  E(X) = \frac{dM_X(t)}{dt} \Big|_{t=0}
  \]
  \[
  M'_X(t) = 0.2 e^t + 1.0 e^{2t} + 0.9 e^{3t}
  \]
  \[
  E(X) = (0.2 + 1.0 + 0.9) \Big|_{t=0} = 2.1
  \]
  
- **Second Moment:**  
  \[
  E(X^2) = \frac{d^2M_X(t)}{dt^2} \Big|_{t=0}
  \]

This can be computed by differentiating again.  

---

## **4️⃣ Why is MGF Important?**
- It provides a compact way to find **all moments**.  
- It is useful for **proving limit theorems** (like the Central Limit Theorem).  
- It helps in **finding distributions** by matching MGFs.  

---
### **Joint Probability Function & Marginal Density Function**  

When dealing with multiple random variables, we need ways to describe their relationship. **Joint probability functions** define how two or more variables interact, while **marginal density functions** help us understand individual distributions.

---

## **1️⃣ Joint Probability Mass Function (Joint PMF)**
For two discrete random variables \(X\) and \(Y\), the **joint probability mass function (PMF)** gives the probability that \(X\) takes a specific value \(x\) and \(Y\) takes a specific value \(y\):

\[
P(X = x, Y = y) = P(X, Y)
\]

📌 **Example:**  
Consider a probability distribution where \(X\) represents the number of heads and \(Y\) represents the number of tails in **two coin flips**.

| \(X\) | \(Y\) | Probability \(P(X, Y)\) |
|------|------|----------------|
| 0    | 2    | \(1/4\)        |
| 1    | 1    | \(1/2\)        |
| 2    | 0    | \(1/4\)        |

Each probability represents the likelihood of a specific outcome in the two flips.

---

## **2️⃣ Joint Probability Density Function (Joint PDF)**
For continuous random variables \(X\) and \(Y\), the **joint probability density function (PDF)** is defined as:

\[
f_{X,Y}(x, y) = \frac{\partial^2}{\partial x \partial y} P(X \leq x, Y \leq y)
\]

The probability of \(X\) and \(Y\) occurring in a given range is:

\[
P(a \leq X \leq b, c \leq Y \leq d) = \int_{a}^{b} \int_{c}^{d} f_{X,Y}(x, y) \, dy \, dx
\]

📌 **Example:**  
Let \(X, Y\) have the joint PDF:

\[
f_{X,Y}(x, y) =
\begin{cases}
6(1-x-y), & 0 \leq x \leq 1, 0 \leq y \leq 1, x + y \leq 1 \\
0, & \text{otherwise}
\end{cases}
\]

To find \(P(0 \leq X \leq 0.5, 0 \leq Y \leq 0.5)\), integrate:

\[
P = \int_0^{0.5} \int_0^{0.5} 6(1-x-y) dy dx
\]

---

## **3️⃣ Marginal Probability Function**
The **marginal probability function** describes the probability of one variable **alone** by summing (discrete case) or integrating (continuous case) over the other variable.

### **For Discrete Random Variables:**
\[
P(X = x) = \sum_{y} P(X = x, Y = y)
\]

\[
P(Y = y) = \sum_{x} P(X = x, Y = y)
\]

📌 **Example:**
Using our earlier joint PMF table,

\[
P(X = 1) = P(1,1) + P(1,0) = \frac{1}{2}
\]

### **For Continuous Random Variables:**
\[
f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy
\]

\[
f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dx
\]

📌 **Example:**
For the joint PDF:

\[
f_{X,Y}(x,y) = 6(1-x-y)
\]

\[
f_X(x) = \int_{0}^{1-x} 6(1-x-y) dy
\]

\[
f_Y(y) = \int_{0}^{1-y} 6(1-x-y) dx
\]

These integrals give us the marginal distributions.

---

### **Key Takeaways**
✔ **Joint PMF/PDF** tells us the probability of two variables occurring together.  
✔ **Marginal PMF/PDF** helps find individual distributions.  
✔ Used in **conditional probabilities, correlation, and independence tests**.

---
### **Special Probability Distributions**  

Probability distributions describe how values of a random variable are spread. Here, we cover the most important **discrete** and **continuous** distributions.  

---

## **1️⃣ Binomial Distribution** (Discrete)  
The **binomial distribution** models the number of **successes** in a **fixed number of independent Bernoulli trials** (where each trial has two outcomes: success or failure).  

### **Formula:**  
\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\]  
where:  
- \( n \) = number of trials  
- \( k \) = number of successes  
- \( p \) = probability of success  
- \( \binom{n}{k} \) = \( \frac{n!}{k!(n-k)!} \) (combinations)  

📌 **Example:** A fair coin is flipped **10 times**. Find the probability of getting exactly **6 heads**.  
\[
P(X = 6) = \binom{10}{6} (0.5)^6 (0.5)^4 = \frac{10!}{6!4!} (0.5)^{10} = 0.205
\]  

📌 **Mean & Variance:**  
- Mean: \( E(X) = np \)  
- Variance: \( Var(X) = np(1-p) \)  

---

## **2️⃣ Poisson Distribution** (Discrete)  
The **Poisson distribution** is used for counting the **number of events in a fixed interval of time or space**, given that events happen at a **constant average rate** independently.  

### **Formula:**  
\[
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
\]  
where:  
- \( \lambda \) = expected number of occurrences in a given interval  
- \( k \) = actual number of occurrences  

📌 **Example:** A website receives **5 hits per minute** on average. Find the probability of exactly **3 hits in a minute**.  
\[
P(X = 3) = \frac{e^{-5} 5^3}{3!} = \frac{e^{-5} 125}{6} \approx 0.1404
\]  

📌 **Mean & Variance:**  
- Mean: \( E(X) = \lambda \)  
- Variance: \( Var(X) = \lambda \)  

---

## **3️⃣ Uniform Distribution** (Continuous)  
The **uniform distribution** represents a situation where every outcome in a range is equally likely.  

### **Formula:**  
\[
f(x) =
\begin{cases}
\frac{1}{b-a}, & a \leq x \leq b \\
0, & \text{otherwise}
\end{cases}
\]  
where:  
- \( a, b \) = lower and upper bounds of the range  

📌 **Example:** If a random number is picked between **2 and 10**, the probability density is:  
\[
f(x) = \frac{1}{10-2} = \frac{1}{8}
\]  

📌 **Mean & Variance:**  
- Mean: \( E(X) = \frac{a+b}{2} \)  
- Variance: \( Var(X) = \frac{(b-a)^2}{12} \)  

---

## **4️⃣ Exponential Distribution** (Continuous)  
The **exponential distribution** models the **time between events** in a Poisson process (i.e., waiting times).  

### **Formula:**  
\[
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
\]  
where:  
- \( \lambda \) = rate parameter (events per unit time)  

📌 **Example:** If a lightbulb lasts on average **1000 hours**, find the probability it lasts more than **1500 hours**.  
\[
P(X > 1500) = e^{-1500/1000} = e^{-1.5} \approx 0.223
\]  

📌 **Mean & Variance:**  
- Mean: \( E(X) = \frac{1}{\lambda} \)  
- Variance: \( Var(X) = \frac{1}{\lambda^2} \)  

---

## **5️⃣ Normal Distribution** (Continuous)  
The **normal (Gaussian) distribution** is the most important distribution in statistics. Many natural phenomena (height, test scores, etc.) follow this **bell-shaped** curve.  

### **Formula:**  
\[
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
\]  
where:  
- \( \mu \) = mean  
- \( \sigma^2 \) = variance  

📌 **Example:** Suppose test scores follow **\( \mu = 70 \), \( \sigma = 10 \)**. What is the probability a student scores **between 60 and 80**?  
Use the **Z-score transformation**:  
\[
Z = \frac{X - \mu}{\sigma}
\]  
Find values for \( Z(60) \) and \( Z(80) \) from standard normal tables.  

📌 **Properties:**  
- **68-95-99.7 Rule**:  
  - **68%** of data falls within \( \mu \pm \sigma \)  
  - **95%** falls within \( \mu \pm 2\sigma \)  
  - **99.7%** falls within \( \mu \pm 3\sigma \)  

---

## **Key Takeaways**
✔ **Binomial** = Fixed trials, success/failure (e.g., coin flips)  
✔ **Poisson** = Counting events in time/space (e.g., website hits)  
✔ **Uniform** = Equal probability over an interval (e.g., random number)  
✔ **Exponential** = Time between events (e.g., lightbulb life)  
✔ **Normal** = Bell curve, natural distributions (e.g., test scores)  

---
## **Bayes’ Theorem**  

Bayes’ Theorem is a fundamental rule in probability that allows us to update our beliefs when new evidence is introduced. It is widely used in machine learning, medical diagnosis, spam filtering, and more.

---

### **Formula:**  
\[
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
\]  
where:  
- \( P(A|B) \) = Probability of event A occurring given that event B has occurred (**posterior probability**)  
- \( P(B|A) \) = Probability of event B occurring given that event A has occurred (**likelihood**)  
- \( P(A) \) = Probability of event A occurring (**prior probability**)  
- \( P(B) \) = Total probability of event B occurring (**marginal probability**)  

---

### **Example 1: Medical Diagnosis**
A test for a disease is **99% accurate** (i.e., if a person has the disease, the test detects it with 99% probability). However, **0.1%** of the population actually has the disease. The test also gives a **false positive rate of 5%** (i.e., 5% of healthy people test positive).  

If a person tests positive, what is the probability that they actually have the disease?  

#### **Step 1: Define the Given Data**
- \( P(D) = 0.001 \) (Probability of having the disease)  
- \( P(\neg D) = 0.999 \) (Probability of not having the disease)  
- \( P(T|D) = 0.99 \) (Probability of testing positive if diseased)  
- \( P(T|\neg D) = 0.05 \) (Probability of testing positive if healthy)  

#### **Step 2: Compute \( P(T) \) (Total Probability of Testing Positive)**
\[
P(T) = P(T|D) P(D) + P(T|\neg D) P(\neg D)
\]
\[
P(T) = (0.99 \times 0.001) + (0.05 \times 0.999) = 0.00099 + 0.04995 = 0.05094
\]

#### **Step 3: Apply Bayes’ Theorem**
\[
P(D|T) = \frac{P(T|D) P(D)}{P(T)}
\]
\[
P(D|T) = \frac{(0.99 \times 0.001)}{0.05094} = \frac{0.00099}{0.05094} \approx 0.0194
\]

#### **Result:**
Even though the test is **99% accurate**, the probability that a person actually has the disease **given that they tested positive** is only **1.94%**! This happens because the disease is very rare, so false positives dominate the results.

---

### **Example 2: Spam Filtering**
An email classifier marks certain words as likely to appear in spam. Suppose:  
- 20% of emails are spam: \( P(S) = 0.2 \)  
- The word "FREE" appears in **60% of spam** emails: \( P(W|S) = 0.6 \)  
- The word "FREE" appears in **10% of non-spam** emails: \( P(W|\neg S) = 0.1 \)  

If an email contains the word "FREE," what is the probability that it is spam?

#### **Step 1: Compute \( P(W) \) (Total Probability of "FREE" appearing)**
\[
P(W) = P(W|S) P(S) + P(W|\neg S) P(\neg S)
\]
\[
P(W) = (0.6 \times 0.2) + (0.1 \times 0.8) = 0.12 + 0.08 = 0.20
\]

#### **Step 2: Apply Bayes’ Theorem**
\[
P(S|W) = \frac{P(W|S) P(S)}{P(W)}
\]
\[
P(S|W) = \frac{(0.6 \times 0.2)}{0.20} = \frac{0.12}{0.20} = 0.6
\]

#### **Result:**
If an email contains "FREE," there is a **60% probability** that it is spam.

---

### **Key Takeaways**
✅ Bayes' Theorem allows **updating probabilities** when new evidence appears.  
✅ It is useful for **medical tests, spam filters, machine learning, and AI**.  
✅ **False positives** can be misleading when dealing with rare events.  
✅ Helps in **decision-making** when probability updates are required.  

---

## **Unit 4: Hypothesis Testing & Design of Experiments**
## **Sampling and Sampling Distribution**  

Sampling is the process of selecting a subset of data from a larger population to make inferences about the population. Since collecting data from an entire population is often impractical, sampling helps in making predictions with limited data.

---

## **Types of Sampling Methods**
There are two major types of sampling techniques:

### **1. Probability Sampling (Random Sampling)**
Every element in the population has an equal chance of being selected. This ensures **unbiased** results.

- **Simple Random Sampling**: Each member is chosen randomly (e.g., lottery method).
- **Stratified Sampling**: The population is divided into subgroups (strata) and samples are taken from each.
- **Systematic Sampling**: Selecting every \( k^{th} \) member from a list.
- **Cluster Sampling**: Dividing the population into clusters and randomly selecting entire clusters.

### **2. Non-Probability Sampling (Non-Random Sampling)**
Not all members have an equal chance of being selected. This is **biased** but useful when randomness is difficult.

- **Convenience Sampling**: Selecting samples that are easiest to reach (e.g., first 100 survey responses).
- **Judgment Sampling**: Selection based on an expert’s opinion.
- **Quota Sampling**: Ensuring specific groups are represented in a certain proportion.

---

## **Sampling Distribution**
A **sampling distribution** is the probability distribution of a statistic (like the mean) obtained from multiple random samples.

### **Example: Sampling Distribution of the Mean**
If we take multiple samples from a population and compute their means, the distribution of those sample means is called the **sampling distribution of the mean**.

- The mean of the sampling distribution is **equal** to the population mean (\(\mu\)).
- The standard deviation of the sampling distribution is called the **standard error (SE)**:

\[
SE = \frac{\sigma}{\sqrt{n}}
\]

where:
- \( \sigma \) = Population standard deviation
- \( n \) = Sample size  

As \( n \) **increases**, the **sampling distribution becomes narrower**.

---

## **Central Limit Theorem (CLT)**
The **Central Limit Theorem** states that if we take sufficiently large random samples from any population, the sampling distribution of the mean will be **approximately normal**, regardless of the shape of the population distribution.

### **Key Points of CLT:**
✅ Works for **large samples** (\( n > 30 \) is preferred).  
✅ Even if the original population is **not normal**, the sample mean distribution will be **normal**.  
✅ The larger the sample size, the **closer** the sampling distribution is to normality.  

### **Example**
Suppose we measure the height of 10,000 students. The population distribution might be **skewed** (not symmetric). However, if we take **many samples of size 50** and calculate their means, the distribution of these means will be **approximately normal**.

---

## **Practical Applications of Sampling and CLT**
📊 **Opinion Polls:** Predicting election results using a small group of voters.  
🏥 **Medical Studies:** Testing new drugs on a sample before approving them for public use.  
📈 **Quality Control:** Checking a few products from a factory instead of testing every item.  

---
## **Confidence Intervals (1% & 5% Significance Levels)**  

A **Confidence Interval (CI)** is a range of values that estimates an unknown population parameter (like the mean or proportion) with a certain level of confidence.

For example, if we estimate the average height of students in a university to be **\( 165 \pm 2 \) cm** with a **95% confidence level**, it means we are **95% confident** that the true mean height lies between **163 cm and 167 cm**.

---

## **Formula for Confidence Interval**
For a population mean (\(\mu\)) with **known standard deviation (\(\sigma\))**, the confidence interval is:

\[
CI = \bar{X} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}
\]

where:
- \( \bar{X} \) = Sample mean  
- \( Z_{\alpha/2} \) = **Critical value from the Z-table** for a given confidence level  
- \( \sigma \) = Population standard deviation  
- \( n \) = Sample size  

If the **population standard deviation (\(\sigma\)) is unknown**, we use the **t-distribution** instead:

\[
CI = \bar{X} \pm t_{\alpha/2} \times \frac{s}{\sqrt{n}}
\]

where \( s \) is the **sample standard deviation**.

---

## **Common Confidence Levels & Z-values**
| Confidence Level | \( Z_{\alpha/2} \) (Z-score) | Significance Level \( \alpha \) |
|-----------------|-----------------|------------------|
| 90% | 1.645 | 0.10 |
| 95% | 1.960 | 0.05 |
| 99% | 2.576 | 0.01 |

- **95% Confidence Interval** → \( \alpha = 0.05 \) → **Z = 1.96**  
- **99% Confidence Interval** → \( \alpha = 0.01 \) → **Z = 2.576**  

💡 **Lower significance level (\(\alpha\)) means more confidence but a wider interval!**

---

## **Example 1: 95% Confidence Interval for Mean**
A survey finds that the average weight of students is **65 kg**, with a **standard deviation of 8 kg** from a sample of **100 students**. Find the **95% confidence interval** for the population mean.

🔹 Given:
- \( \bar{X} = 65 \)
- \( \sigma = 8 \)
- \( n = 100 \)
- \( Z_{\alpha/2} = 1.96 \) (for 95% confidence)

\[
CI = 65 \pm 1.96 \times \frac{8}{\sqrt{100}}
\]

\[
CI = 65 \pm 1.96 \times 0.8
\]

\[
CI = 65 \pm 1.568
\]

\[
CI = (63.432, 66.568)
\]

**Interpretation**: We are **95% confident** that the true average weight of all students lies between **63.43 kg and 66.57 kg**.

---

## **Example 2: 99% Confidence Interval for Mean**
Using the same data, calculate the **99% confidence interval**.

🔹 Given:
- \( Z_{\alpha/2} = 2.576 \) (for 99% confidence)

\[
CI = 65 \pm 2.576 \times \frac{8}{\sqrt{100}}
\]

\[
CI = 65 \pm 2.576 \times 0.8
\]

\[
CI = 65 \pm 2.0608
\]

\[
CI = (62.9392, 67.0608)
\]

**Interpretation**: We are **99% confident** that the true average weight is between **62.94 kg and 67.06 kg**.

---

## **Key Observations**
- **Higher confidence level (99%)** → Wider interval (more uncertainty).  
- **Lower confidence level (95%)** → Narrower interval (less uncertainty).  
- **Larger sample size (\(n\))** → Smaller confidence interval (more precise estimate).  

---
## **One-Tailed and Two-Tailed Tests**  

### **1. Introduction to Hypothesis Testing**  
Hypothesis testing is a statistical method used to decide whether there is enough evidence in a sample to infer a conclusion about a population.

- **Null Hypothesis (\(H_0\))**: The statement that there is no effect or no difference.  
- **Alternative Hypothesis (\(H_a\))**: The statement that there is an effect or difference.  

---

### **2. One-Tailed Test**  
A **one-tailed (one-sided) test** is used when we are only interested in **one direction** of change.  

🔹 **Used when we want to test if:**
- The sample mean is **greater than** a certain value (**right-tailed test**).
- The sample mean is **less than** a certain value (**left-tailed test**).

#### **Right-Tailed Test**
\[
H_0: \mu \leq \mu_0
\]
\[
H_a: \mu > \mu_0
\]
We reject \(H_0\) if the sample mean is significantly greater than \(\mu_0\).

#### **Left-Tailed Test**
\[
H_0: \mu \geq \mu_0
\]
\[
H_a: \mu < \mu_0
\]
We reject \(H_0\) if the sample mean is significantly smaller than \(\mu_0\).

#### **Example: Right-Tailed Test**
A manufacturer claims that the average lifetime of its bulbs is **at least 800 hours**. A random sample of 50 bulbs has a mean lifetime of 780 hours with a standard deviation of 30 hours. Test at **5% significance level** if the claim is false.

✅ **Given Data:**
- \(H_0: \mu \geq 800\) (Manufacturer’s claim)  
- \(H_a: \mu < 800\) (We suspect it’s less)  
- \( \bar{X} = 780 \), \( s = 30 \), \( n = 50 \), \( \alpha = 0.05 \)  
- \( Z_{\alpha} = -1.645 \) (from Z-table for left-tailed test)  

\[
Z = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}
\]

\[
Z = \frac{780 - 800}{30/\sqrt{50}}
\]

\[
Z = \frac{-20}{4.24} = -4.72
\]

Since **-4.72 is much smaller than -1.645**, we **reject \(H_0\)** and conclude that the manufacturer’s claim is likely **false**.

---

### **3. Two-Tailed Test**  
A **two-tailed (two-sided) test** is used when we check for **differences in both directions** (greater or smaller).  

#### **Hypotheses for Two-Tailed Test**
\[
H_0: \mu = \mu_0
\]
\[
H_a: \mu \neq \mu_0
\]
We reject \(H_0\) if the sample mean is **significantly different** from \(\mu_0\) (either too high or too low).

#### **Example: Two-Tailed Test**
A company claims the average salary of its employees is **₹50,000**. A sample of 40 employees has an average salary of ₹47,500 with a standard deviation of ₹8,000. Test at **5% significance level**.

✅ **Given Data:**
- \(H_0: \mu = 50,000\)  
- \(H_a: \mu \neq 50,000\)  
- \( \bar{X} = 47,500 \), \( s = 8,000 \), \( n = 40 \), \( \alpha = 0.05 \)  
- **For two-tailed test:** \( Z_{\alpha/2} = \pm 1.96 \)  

\[
Z = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}
\]

\[
Z = \frac{47,500 - 50,000}{8,000/\sqrt{40}}
\]

\[
Z = \frac{-2,500}{1,264} = -1.98
\]

Since **-1.98 is less than -1.96**, we **reject \(H_0\)** and conclude that the average salary is significantly different from ₹50,000.

---

### **4. Summary of One-Tailed vs. Two-Tailed Tests**
| Type | Hypothesis | Critical Region | Z-Value at 5% Significance |
|------|-----------|----------------|---------------------------|
| **Left-Tailed** | \( H_a: \mu < \mu_0 \) | Left side (lower values) | \( Z < -1.645 \) |
| **Right-Tailed** | \( H_a: \mu > \mu_0 \) | Right side (higher values) | \( Z > 1.645 \) |
| **Two-Tailed** | \( H_a: \mu \neq \mu_0 \) | Both sides | \( |Z| > 1.96 \) |

---
## **Test of Significance (Mean, Difference of Means)**  

### **1. Introduction to Significance Testing**  
Significance tests help determine whether the **sample mean** or **difference of two sample means** is statistically different from a given value.  

🔹 **Key Concepts:**  
- **Null Hypothesis (\(H_0\))**: No significant difference exists.  
- **Alternative Hypothesis (\(H_a\))**: A significant difference exists.  
- **Significance Level (\(\alpha\))**: Probability of rejecting \(H_0\) when it is true (typically 5% or 1%).  
- **Test Statistic**: A value used to compare with critical values from statistical tables.  
- **Critical Region**: The region where \(H_0\) is rejected.  

---

## **2. Test of Significance for a Single Mean**  
Used when we want to check whether a sample mean **significantly differs** from a given population mean.

🔹 **Test Statistic (Z-test for Large Samples, n ≥ 30):**  
\[
Z = \frac{\bar{X} - \mu}{s / \sqrt{n}}
\]
Where:
- \( \bar{X} \) = Sample Mean  
- \( \mu \) = Population Mean  
- \( s \) = Sample Standard Deviation  
- \( n \) = Sample Size  

🔹 **Test Statistic (t-test for Small Samples, n < 30):**  
\[
t = \frac{\bar{X} - \mu}{s / \sqrt{n}}
\]
\( t \)-values are taken from the t-table for \( n-1 \) degrees of freedom.

#### **Example (Single Mean Test - Z-test)**
A company claims that its employees work **on average 50 hours per week**. A random sample of 40 employees shows a mean of **48.5 hours** with a standard deviation of **4 hours**. Test the claim at **5% significance level**.

✅ **Given Data:**
- \( H_0: \mu = 50 \)  
- \( H_a: \mu \neq 50 \)  
- \( \bar{X} = 48.5 \), \( s = 4 \), \( n = 40 \)  
- **Two-tailed test**: Critical value at \( 5\% \) significance \( Z_{\alpha/2} = \pm 1.96 \)

\[
Z = \frac{48.5 - 50}{4 / \sqrt{40}}
\]

\[
Z = \frac{-1.5}{0.632} = -2.37
\]

Since **-2.37 < -1.96**, we **reject \( H_0 \)** and conclude that employees **work significantly less than 50 hours** per week.

---

## **3. Test of Significance for the Difference of Means**  
Used when we compare **two different sample means** from two populations.

🔹 **Z-test for Large Samples (\( n_1, n_2 \geq 30 \))**
\[
Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{(s_1^2 / n_1) + (s_2^2 / n_2)}}
\]

🔹 **t-test for Small Samples (\( n_1, n_2 < 30 \))** (Assuming Equal Variance)
\[
t = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{s_p^2 (1/n_1 + 1/n_2)}}
\]
where:
\[
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
\]

#### **Example (Difference of Means Test - Z-test)**
A university wants to check if **men and women spend different amounts of time studying per week**. A sample of **35 male students** shows an average study time of **10 hours/week** (SD = 2). A sample of **40 female students** shows an average study time of **11 hours/week** (SD = 2.5). Test at **5% significance level**.

✅ **Given Data:**
- \( H_0: \mu_1 = \mu_2 \) (No difference in study time)  
- \( H_a: \mu_1 \neq \mu_2 \) (There is a difference)  
- \( \bar{X}_1 = 10 \), \( s_1 = 2 \), \( n_1 = 35 \)  
- \( \bar{X}_2 = 11 \), \( s_2 = 2.5 \), \( n_2 = 40 \)  
- **Two-tailed test**: \( Z_{\alpha/2} = \pm 1.96 \)

\[
Z = \frac{(10 - 11) - 0}{\sqrt{(2^2 / 35) + (2.5^2 / 40)}}
\]

\[
Z = \frac{-1}{\sqrt{0.114 + 0.156}}
\]

\[
Z = \frac{-1}{0.513} = -1.95
\]

Since **-1.95 is very close to -1.96**, we are **on the borderline** of rejecting \( H_0 \). A slightly lower significance level (e.g., 4%) might reject \( H_0 \).

---

## **4. Summary of Tests of Significance**  

| Test Type | Sample Size | Formula | When to Use |
|-----------|------------|---------|-------------|
| **Z-test for Mean** | \( n \geq 30 \) | \( Z = \frac{\bar{X} - \mu}{s/\sqrt{n}} \) | When testing the mean of a large sample |
| **t-test for Mean** | \( n < 30 \) | \( t = \frac{\bar{X} - \mu}{s/\sqrt{n}} \) | When testing the mean of a small sample |
| **Z-test for Difference of Means** | \( n_1, n_2 \geq 30 \) | \( Z = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{(s_1^2 / n_1) + (s_2^2 / n_2)}} \) | When comparing means of two large samples |
| **t-test for Difference of Means** | \( n_1, n_2 < 30 \) | \( t = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{s_p^2 (1/n_1 + 1/n_2)}} \) | When comparing means of two small samples |

---
## **Chi-Square Test and F-Test**  

### **1. Chi-Square (\(\chi^2\)) Test**  
The **Chi-Square test** is used to determine whether there is a **significant association** between two categorical variables. It is also used to test the **goodness of fit** of observed data to an expected distribution.

---

### **Types of Chi-Square Tests**  

1️⃣ **Chi-Square Goodness of Fit Test**  
   - Used to check if a sample distribution fits a given theoretical distribution.  
   - Example: Are the observed sales of a product consistent with expected sales?  

2️⃣ **Chi-Square Test for Independence**  
   - Used to check if two categorical variables are **independent** or **related**.  
   - Example: Is there a relationship between gender and preference for a product?  

---

### **Chi-Square Formula**  

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

Where:  
- \( O \) = Observed frequency  
- \( E \) = Expected frequency  
- \( \chi^2 \) follows the **Chi-Square distribution** with **(rows - 1) × (columns - 1)** degrees of freedom.  

---

### **Example 1: Chi-Square Goodness of Fit Test**  
A company claims that customer preferences for its three products (**A, B, C**) follow a **40:35:25 ratio**. A survey of 200 customers found that **Product A = 90**, **Product B = 70**, **Product C = 40**. Test the claim at **5% significance**.

✅ **Step 1: Hypothesis**  
- \( H_0 \): The preferences follow the expected 40:35:25 ratio.  
- \( H_a \): The preferences do not follow this ratio.  

✅ **Step 2: Calculate Expected Frequencies**  
- Total customers = 200  
- Expected for A = \( 200 \times \frac{40}{100} = 80 \)  
- Expected for B = \( 200 \times \frac{35}{100} = 70 \)  
- Expected for C = \( 200 \times \frac{25}{100} = 50 \)  

✅ **Step 3: Compute \( \chi^2 \)**  

\[
\chi^2 = \frac{(90-80)^2}{80} + \frac{(70-70)^2}{70} + \frac{(40-50)^2}{50}
\]

\[
\chi^2 = \frac{10^2}{80} + \frac{0^2}{70} + \frac{10^2}{50}
\]

\[
\chi^2 = \frac{100}{80} + 0 + \frac{100}{50}
\]

\[
\chi^2 = 1.25 + 0 + 2 = 3.25
\]

✅ **Step 4: Decision**  
- Degrees of Freedom = \( (3 - 1) = 2 \)  
- From the Chi-Square table, **critical value at 5% significance = 5.99**  
- Since \( \chi^2 = 3.25 < 5.99 \), **we do not reject \( H_0 \)**.  
- **Conclusion:** The customer preferences match the expected ratio.

---

### **Example 2: Chi-Square Test for Independence**  
A company surveyed **100 people** to see if gender influences **preference for a new product**. The results are:  

|  | Like | Dislike | Total |
|---|---|---|---|
| Male | 30 | 20 | 50 |
| Female | 25 | 25 | 50 |
| Total | 55 | 45 | 100 |

✅ **Step 1: Hypothesis**  
- \( H_0 \): Gender and preference are independent.  
- \( H_a \): Gender and preference are related.  

✅ **Step 2: Compute Expected Frequencies**  

\[
E = \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}
\]

For **Males who like the product**:  
\[
E = \frac{50 \times 55}{100} = 27.5
\]

For **Males who dislike the product**:  
\[
E = \frac{50 \times 45}{100} = 22.5
\]

For **Females who like the product**:  
\[
E = \frac{50 \times 55}{100} = 27.5
\]

For **Females who dislike the product**:  
\[
E = \frac{50 \times 45}{100} = 22.5
\]

✅ **Step 3: Compute \( \chi^2 \)**  

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

\[
\chi^2 = \frac{(30 - 27.5)^2}{27.5} + \frac{(20 - 22.5)^2}{22.5} + \frac{(25 - 27.5)^2}{27.5} + \frac{(25 - 22.5)^2}{22.5}
\]

\[
\chi^2 = \frac{2.5^2}{27.5} + \frac{2.5^2}{22.5} + \frac{2.5^2}{27.5} + \frac{2.5^2}{22.5}
\]

\[
\chi^2 = 0.227 + 0.278 + 0.227 + 0.278 = 1.01
\]

✅ **Step 4: Decision**  
- Degrees of Freedom = \( (2-1) \times (2-1) = 1 \)  
- Critical value at 5% significance = **3.841**  
- Since \( \chi^2 = 1.01 < 3.841 \), we **do not reject \( H_0 \)**.  
- **Conclusion:** Gender does not significantly influence preference.

---

## **2. F-Test**  
The **F-test** is used to compare the **variances of two populations**.  

### **Formula**  

\[
F = \frac{S_1^2}{S_2^2}, \quad S_1^2 > S_2^2
\]

Where:
- \( S_1^2, S_2^2 \) = Sample variances of two groups  
- \( F \) follows the **F-distribution** with degrees of freedom \( (n_1 - 1, n_2 - 1) \).  

---

### **Example: F-Test for Variance**  
Two teaching methods were tested on **two different classes**. The variances in test scores were:  

- **Class A:** \( s_1^2 = 25 \), \( n_1 = 16 \)  
- **Class B:** \( s_2^2 = 16 \), \( n_2 = 21 \)  

✅ **Step 1: Compute \( F \)-value**  

\[
F = \frac{25}{16} = 1.56
\]

✅ **Step 2: Compare with Critical Value**  
- Degrees of freedom = \( (16-1, 21-1) = (15, 20) \)  
- From the F-table at **5% significance**, critical value **F(15,20) = 2.35**.  
- Since \( F = 1.56 < 2.35 \), we **do not reject \( H_0 \)**.  
- **Conclusion:** The variances of the two classes are not significantly different.

---

## **✅ Summary**  

| Test | Purpose | Formula |
|------|---------|---------|
| **Chi-Square Goodness of Fit** | Tests if sample follows expected distribution | \( \chi^2 = \sum \frac{(O - E)^2}{E} \) |
| **Chi-Square Test for Independence** | Checks if two categorical variables are related | \( \chi^2 = \sum \frac{(O - E)^2}{E} \) |
| **F-Test** | Compares variances of two populations | \( F = \frac{S_1^2}{S_2^2} \) |

---
## **Central Limit Theorem (CLT)**  

### **Definition**  
The **Central Limit Theorem (CLT)** states that, **regardless of the original population distribution, the sampling distribution of the sample mean will be approximately normal if the sample size is sufficiently large**.

### **Key Points:**  
- The original population **can be any distribution** (normal, uniform, skewed, etc.).  
- As the **sample size increases**, the **distribution of sample means** approaches a normal distribution.  
- The **mean** of the sample means is equal to the population mean.  
- The **variance** of the sample means is **reduced by the sample size**.

### **Mathematical Representation**  

If we take random samples of size \( n \) from a population with:  
- Mean \( \mu \)  
- Standard deviation \( \sigma \)  

Then, the sample mean \( \bar{X} \) follows:

\[
\bar{X} \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)
\]

This means:  
- The **mean** of the sample means = **population mean** \( \mu \)  
- The **standard deviation** of the sample means = **population standard deviation divided by \( \sqrt{n} \)**  

\[
\text{Standard Error} = \frac{\sigma}{\sqrt{n}}
\]

---

## **Why is CLT Important?**  
- **Allows us to use normal probability methods even for non-normal populations.**  
- **Justifies many statistical tests** (e.g., hypothesis testing, confidence intervals).  
- **Explains why sample means tend to follow a normal distribution** in large samples.

---

## **Example 1: Understanding CLT with Dice Rolls 🎲**  
Imagine rolling a **fair 6-sided die** (values 1, 2, 3, 4, 5, 6).  

### **Step 1: Population Distribution**
- The population is **uniformly distributed** (each number has equal probability).  
- Mean \( \mu = \frac{1+2+3+4+5+6}{6} = 3.5 \)  
- Standard deviation \( \sigma = 1.71 \)  

### **Step 2: Take Small Sample Sizes**
- If we roll the die **once** (\( n = 1 \)), the distribution is still **uniform**.  
- If we roll **2 dice** and take the mean, the distribution **starts looking more normal**.  
- If we roll **30 dice** and take the mean, the sample means form a **nearly perfect normal curve**.

✅ **Conclusion:** Even though rolling a single die gives a uniform distribution, rolling multiple dice and taking the mean results in a normal distribution (by CLT).

---

## **Example 2: Exam Scores**  
A class has **exam scores** with:  
- **Population Mean** \( \mu = 70 \)  
- **Standard Deviation** \( \sigma = 15 \)  

We take a **random sample** of **n = 36** students.  

✅ **Step 1: Find the Standard Error**  

\[
SE = \frac{\sigma}{\sqrt{n}} = \frac{15}{\sqrt{36}} = \frac{15}{6} = 2.5
\]

✅ **Step 2: Approximate Probabilities Using Normal Distribution**  
- The sample mean distribution follows \( N(70, 2.5) \).  
- If we want to find the probability that the sample mean is greater than 73:

\[
Z = \frac{X - \mu}{SE} = \frac{73 - 70}{2.5} = \frac{3}{2.5} = 1.2
\]

Using the **Z-table**, \( P(Z > 1.2) = 0.1151 \).  
**So, there is an 11.51% chance that the sample mean is greater than 73.**

---

## **Key Takeaways**  
✅ The **larger the sample size, the closer the sample mean distribution is to normal.**  
✅ If \( n \geq 30 \), the CLT holds, and we assume normality for most practical cases.  
✅ This helps in **statistical inference** (e.g., hypothesis testing & confidence intervals).  

---
## **Design of Experiments (DOE)**
Design of Experiments (DOE) is a structured method used to determine the relationship between different factors affecting a process and the output of that process. It helps in optimizing performance and improving quality in various fields like engineering, manufacturing, and scientific research.

---

## **1. One-Way Classification (One-Factor ANOVA)**  
### **Definition**  
One-way classification is used when there is only **one independent variable (factor)** affecting the dependent variable. It helps compare **multiple groups** to check if there is a significant difference between their means.

### **Example Scenario:**  
A teacher wants to test whether three different teaching methods affect student performance differently.  
- Factor: **Teaching method (A, B, C)**
- Dependent variable: **Student scores**

### **Hypothesis Setup**  
- **Null Hypothesis \( H_0 \):** All groups have the same mean.  
- **Alternative Hypothesis \( H_1 \):** At least one group mean is different.

### **ANOVA (Analysis of Variance) Formula**  
The F-statistic for one-way ANOVA is:

\[
F = \frac{\text{Between-group variability}}{\text{Within-group variability}}
\]

where:  
- **Between-group variability** measures how much the group means differ from the overall mean.  
- **Within-group variability** measures how much data points within each group vary.  

### **Decision Rule**  
- If **F-statistic > Critical F-value** (from F-table), **reject \( H_0 \)** → At least one group is significantly different.  
- Otherwise, **fail to reject \( H_0 \)** → No significant difference between groups.

### **Example Calculation**  
Consider three teaching methods (A, B, and C) applied to students, and their average scores are recorded.

| Group | Mean Score | Variance |
|--------|-----------|-----------|
| A | 80 | 4 |
| B | 85 | 5 |
| C | 78 | 6 |

By applying ANOVA formulas, we can compute the F-value and compare it with a critical value from the **F-distribution table** at a given significance level (e.g., 5%).

---

## **2. Two-Way Classification (Two-Factor ANOVA)**
### **Definition**  
Two-way classification is used when **two independent variables (factors)** influence the dependent variable. It helps analyze:  
1. The effect of **each factor separately** (main effects).  
2. The **interaction effect** between the two factors.

### **Example Scenario:**  
A company tests **two fertilizers (Factor A: Fertilizer Type)** and **three irrigation levels (Factor B: Water Amount)** on crop yield.

| Fertilizer | Low Water | Medium Water | High Water |
|------------|------------|---------------|------------|
| A | 10kg | 15kg | 20kg |
| B | 12kg | 18kg | 22kg |

### **Hypothesis Setup**  
- **Null Hypotheses:**  
  - \( H_{0A} \): No significant difference between fertilizers.  
  - \( H_{0B} \): No significant difference between irrigation levels.  
  - \( H_{0AB} \): No interaction effect between fertilizers and irrigation levels.  

### **ANOVA Calculation**
For two-way ANOVA, we compute three F-values:  
1. **F-factor A** (fertilizer effect)  
2. **F-factor B** (water effect)  
3. **F-interaction (AB)**  

If any \( F \)-value is **greater than critical F**, we reject \( H_0 \) and conclude a significant effect.

---

## **Key Differences: One-Way vs. Two-Way ANOVA**
| Feature | One-Way ANOVA | Two-Way ANOVA |
|----------|--------------|--------------|
| Number of Factors | One | Two |
| Measures | Effect of one factor | Effect of two factors & interaction |
| Example | Teaching method on scores | Fertilizer & Water on Crop Yield |

---

## **Practical Applications of DOE**
✅ **Manufacturing:** Optimize machine settings for maximum efficiency.  
✅ **Medicine:** Test different drugs and dosages for effectiveness.  
✅ **Agriculture:** Study the impact of fertilizers and weather conditions.  
✅ **Marketing:** Analyze how pricing and advertising methods affect sales.  

---
## **Hypothesis Testing (One-Tailed & Two-Tailed Tests)**  

### **What is Hypothesis Testing?**  
Hypothesis testing is a statistical method used to make inferences about a population based on sample data. It helps determine whether there is enough evidence to reject a null hypothesis ( \(H_0\) ) in favor of an alternative hypothesis ( \(H_1\) ).

---

## **1. Components of Hypothesis Testing**
1. **Null Hypothesis (\(H_0\))**: The assumption that there is no significant effect or difference.  
2. **Alternative Hypothesis (\(H_1\))**: The statement we want to test, suggesting a significant effect or difference.  
3. **Significance Level (\(\alpha\))**: The probability of rejecting \(H_0\) when it is actually true. Common values: **0.05 (5%)** or **0.01 (1%)**.  
4. **Test Statistic**: A calculated value used to decide whether to reject \(H_0\). Examples: **Z-test, t-test, Chi-square test**.  
5. **P-value**: The probability of obtaining the observed results under \(H_0\). If **p-value < α**, reject \(H_0\).  

---

## **2. One-Tailed vs. Two-Tailed Tests**
### **a) One-Tailed Test**
A **one-tailed test** checks for an effect in **one specific direction** (either greater than or less than).  

✅ **Right-Tailed Test (\(H_1: \mu > \mu_0\))**  
Used when we suspect the sample mean **is greater than** the population mean.  
✅ **Left-Tailed Test (\(H_1: \mu < \mu_0\))**  
Used when we suspect the sample mean **is less than** the population mean.  

#### **Example (Right-Tailed Test):**
A company claims its **new battery lasts more than 10 hours** on average.  
- **\(H_0\):** The battery lasts **10 hours** or less (\(\mu \leq 10\)).  
- **\(H_1\):** The battery lasts **more than 10 hours** (\(\mu > 10\)).  

If test results show **p-value < α**, we reject \(H_0\) and conclude the battery lasts longer.  

📈 **Right-tailed test:** The rejection region is on the **right side** of the normal distribution curve.

#### **Example (Left-Tailed Test):**
A dietitian claims a new diet **reduces cholesterol below 200 mg/dL**.  
- **\(H_0\):** The average cholesterol level **is 200 mg/dL or more** (\(\mu \geq 200\)).  
- **\(H_1\):** The diet reduces cholesterol **below 200 mg/dL** (\(\mu < 200\)).  

📉 **Left-tailed test:** The rejection region is on the **left side** of the normal distribution curve.

---

### **b) Two-Tailed Test**
A **two-tailed test** checks for an effect in **both directions** (whether it is greater OR less than a given value).  

#### **Example:**
A university wants to check if a **new teaching method changes student performance** (either higher or lower).  
- **\(H_0\):** No change in scores (\(\mu = \mu_0\)).  
- **\(H_1\):** Scores are **different** (\(\mu \neq \mu_0\)).  

📊 **Two-tailed test:** The rejection regions are **both in the left and right tails** of the normal distribution curve.

---

## **3. Decision Making Using P-Value**
| P-Value | Decision |
|----------|------------|
| \( p < \alpha \) | Reject \( H_0 \), accept \( H_1 \) (Significant effect) |
| \( p > \alpha \) | Fail to reject \( H_0 \) (No significant effect) |

---

## **4. Example Calculation (Z-Test)**
A soft drink company claims its bottles contain **500 ml of soda**. A sample of 30 bottles shows an **average of 495 ml**, with a **standard deviation of 10 ml**. Is the company’s claim correct at **5% significance**?

### **Step 1: Define Hypotheses**
- **\(H_0\):** The average volume is **500 ml** (\(\mu = 500\)).  
- **\(H_1\):** The average volume is **not 500 ml** (\(\mu \neq 500\)) → **Two-tailed test**.

### **Step 2: Compute Test Statistic (Z-score)**
\[
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
\]

where:  
- \( \bar{X} = 495 \) (sample mean)  
- \( \mu = 500 \) (population mean)  
- \( \sigma = 10 \) (standard deviation)  
- \( n = 30 \) (sample size)  

\[
Z = \frac{495 - 500}{10 / \sqrt{30}} = \frac{-5}{1.83} = -2.73
\]

### **Step 3: Compare with Critical Value**
At **5% significance level**, the critical **Z-value for a two-tailed test** is **±1.96**.  
Since **-2.73 < -1.96**, we **reject \(H_0\)** → The bottles contain significantly **less** than 500 ml.

---

## **5. Key Differences: One-Tailed vs. Two-Tailed Tests**
| Feature | One-Tailed Test | Two-Tailed Test |
|---------|----------------|----------------|
| Checks for | Increase or decrease | Any difference |
| Rejection Region | One side of curve | Both sides of curve |
| Example | Does drug increase BP? | Does drug change BP? |

---

## **Practical Applications**
✅ **Medicine:** Checking if a new drug increases or decreases effectiveness.  
✅ **Manufacturing:** Testing if a machine produces items **below or above tolerance limits**.  
✅ **Finance:** Analyzing if stock returns are **higher or lower than expected**.  

---
## **Test of Significance (Mean, Difference of Means)**  

### **1. What is a Test of Significance?**  
A **test of significance** is a statistical method used to determine whether the observed difference between sample data and a population parameter (or between two samples) is **due to chance or a real effect**.  

---

## **2. Testing for the Mean of a Population**  

### **Case 1: Population Standard Deviation (\(\sigma\)) is Known** – **Z-Test**  
Used when the **sample size is large** (\(n \geq 30\)) and the **population standard deviation (\(\sigma\)) is known**.  

#### **Formula for Z-Test:**
\[
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
\]
where:  
- \( \bar{X} \) = Sample mean  
- \( \mu \) = Population mean  
- \( \sigma \) = Population standard deviation  
- \( n \) = Sample size  

📌 **Example:**  
A soft drink company claims that the average soda bottle contains **500 ml** of liquid. A random sample of **40 bottles** has a **mean of 495 ml** and a **known standard deviation of 10 ml**. Is the company’s claim correct at a **5% significance level**?  

**Solution:**  
- **\( H_0: \mu = 500 \)** (Claim is correct)  
- **\( H_1: \mu \neq 500 \)** (Claim is incorrect)  
- **Significance level, \(\alpha = 0.05\)**  
- **Critical Z-value for two-tailed test = ±1.96**  
- **Compute Z-score:**
  \[
  Z = \frac{495 - 500}{10 / \sqrt{40}} = \frac{-5}{1.58} = -3.16
  \]
- Since **\( Z = -3.16 \) is less than -1.96**, we **reject \(H_0\)**.  

🔎 **Conclusion:** There is significant evidence that the soda bottles contain less than 500 ml.

---

### **Case 2: Population Standard Deviation (\(\sigma\)) is Unknown** – **t-Test**  
Used when the **sample size is small** (\(n < 30\)) and the **population standard deviation is unknown**.  

#### **Formula for t-Test:**
\[
t = \frac{\bar{X} - \mu}{s / \sqrt{n}}
\]
where:  
- \( s \) = Sample standard deviation  
- \( \bar{X} \), \( \mu \), and \( n \) are the same as in the Z-test.  

📌 **Example:**  
A researcher believes that students in a certain university sleep for less than **7 hours per night** on average. A sample of **10 students** had the following sleep times (in hours):  
**6.2, 6.5, 7.1, 5.9, 6.3, 6.8, 5.7, 7.2, 6.0, 6.4**  

Test the hypothesis at a **5% significance level**.  

**Solution:**  
- **\( H_0: \mu = 7 \)** (Students sleep 7 hours on average)  
- **\( H_1: \mu < 7 \)** (Students sleep less than 7 hours)  
- **Use a t-test since \(\sigma\) is unknown and \(n < 30\).**  

Compute sample mean (\(\bar{X}\)) and standard deviation (\(s\)) and then apply the t-test formula.  
The critical t-value for **\( df = n-1 = 9 \)** at **\( \alpha = 0.05 \)** is **-1.833**.  

If **\( t < -1.833 \)**, reject \(H_0\).  
(We can calculate this step-by-step if needed.)  

---

## **3. Testing the Difference of Two Means**
### **Case 1: Independent Samples (Two-Sample Z-Test)**
Used when we compare two different groups and **population standard deviations are known**.

#### **Formula:**
\[
Z = \frac{(\bar{X_1} - \bar{X_2}) - (\mu_1 - \mu_2)}{\sqrt{ \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2} }}
\]

where:  
- \( \bar{X_1}, \bar{X_2} \) = Sample means  
- \( \sigma_1, \sigma_2 \) = Population standard deviations  
- \( n_1, n_2 \) = Sample sizes  

📌 **Example:**  
A company wants to compare the productivity of **two different teams**.  
- **Team A:** \( n_1 = 50 \), mean **80 tasks/day**, \( \sigma_1 = 10 \)  
- **Team B:** \( n_2 = 40 \), mean **75 tasks/day**, \( \sigma_2 = 12 \)  
- **Is there a significant difference at \(\alpha = 0.05\)?**  

We compute \( Z \) and compare it to the critical value **\( \pm1.96 \)**.

---

### **Case 2: Independent Samples (Two-Sample t-Test)**
Used when **population standard deviations are unknown**.

#### **Formula:**
\[
t = \frac{(\bar{X_1} - \bar{X_2})}{\sqrt{ S_p^2 (\frac{1}{n_1} + \frac{1}{n_2})}}
\]

where:  
- \( S_p \) = **Pooled standard deviation**  
  \[
  S_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
  \]

📌 **Example:**  
A scientist compares the reaction times of **two groups of drivers**.  
- **Group 1:** \( n_1 = 12 \), mean **0.75 sec**, \( s_1 = 0.10 \)  
- **Group 2:** \( n_2 = 10 \), mean **0.80 sec**, \( s_2 = 0.12 \)  
- **Use a t-test to compare means at \( \alpha = 0.05 \).**  

Compute the pooled variance and apply the t-test formula.

---

## **4. Summary of Tests**
| Test | When to Use | Sample Size | Population Std Dev |
|------|------------|-------------|--------------------|
| Z-test | Testing one mean | \( n \geq 30 \) | Known |
| t-test | Testing one mean | \( n < 30 \) | Unknown |
| Two-sample Z-test | Comparing two means | Large \( n_1, n_2 \) | Known |
| Two-sample t-test | Comparing two means | Any \( n_1, n_2 \) | Unknown |

---

## **5. Applications of Test of Significance**
✅ **Medicine:** Checking if a new drug improves patient recovery time.  
✅ **Education:** Comparing test scores of students from two different teaching methods.  
✅ **Business:** Evaluating whether a new marketing strategy increases sales.  

---
