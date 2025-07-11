# Unit - 4 -> Reinforcement Learning
Introduction, Learning How to Optimize Rewards, Policy Search, Neural Network Policies, Action Evaluation: Credit Assignment problem, Using Policy Gradients, Markow Decision Processes, Q Learning
- Function, Using Deep QLearning to learn how to play Pacman.

## Content ->
### **Reinforcement Learning – Introduction**

---

#### 1. **Definition**

* **Reinforcement Learning (RL)** is a type of **machine learning** where an agent learns to **make decisions** by **interacting with an environment** to **maximize cumulative reward**.
* Learning happens through **trial and error**: the agent takes actions, observes results (states), and receives rewards or penalties.

---

#### 2. **Basic Elements of Reinforcement Learning**

| Component                | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| **Agent**                | The learner or decision-maker.                                            |
| **Environment**          | The system the agent interacts with.                                      |
| **State (S)**            | A representation of the current situation of the environment.             |
| **Action (A)**           | A decision taken by the agent that affects the environment.               |
| **Reward (R)**           | Feedback signal that evaluates the action taken by the agent.             |
| **Policy (π)**           | A strategy used by the agent to decide what action to take in each state. |
| **Value Function (V)**   | Measures how good a state is under a policy in terms of future rewards.   |
| **Q-Value Function (Q)** | Measures the value of taking a specific action in a given state.          |

---

#### 3. **How RL Works**

1. Agent observes the current **state (S)**.
2. Agent selects an **action (A)** based on its **policy**.
3. The environment responds by:

   * Changing to a **new state (S')**
   * Giving a **reward (R)** for the action
4. The agent uses this experience to update its **policy** to improve performance over time.

---

#### 4. **Objective of RL**

* Learn a **policy π(a|s)** that **maximizes the expected cumulative reward** (also called **return**) over time.

$$
\text{Goal:} \quad \max_\pi \, \mathbb{E} \left[ \sum_{t=0}^\infty \gamma^t R_t \right]
$$

* Where:

  * $R_t$: reward at time step $t$
  * $\gamma$: discount factor (0 ≤ γ ≤ 1)

---

#### 5. **Types of RL Problems**

| Type              | Description                                              |
| ----------------- | -------------------------------------------------------- |
| **Episodic**      | Interaction ends after finite steps (e.g., games)        |
| **Continuous**    | Interaction goes on indefinitely                         |
| **Deterministic** | Next state is fully determined by current state & action |
| **Stochastic**    | Transitions have some randomness                         |

---

#### 6. **Exploration vs Exploitation**

* **Exploration**: Trying new actions to discover their effects.
* **Exploitation**: Using known actions that yield high rewards.
* A good agent must **balance both** to perform well.

---

#### 7. **Differences from Other Learning Types**

| Learning Type     | Key Feature                                                             |
| ----------------- | ----------------------------------------------------------------------- |
| **Supervised**    | Learns from labeled input-output pairs.                                 |
| **Unsupervised**  | Finds patterns in unlabeled data.                                       |
| **Reinforcement** | Learns from **interaction with environment** and **feedback** (reward). |

---

#### 8. **Examples and Applications**

* **Robotics**: Learning to walk, grasp objects, etc.
* **Games**: AlphaGo, Atari, Chess using RL.
* **Self-driving cars**: Navigation and control.
* **Finance**: Portfolio management.
* **Healthcare**: Personalized treatment plans.

---
### **Learning How to Optimize Rewards in Reinforcement Learning**

---

#### 1. **Objective of RL**

* The primary goal in RL is to **maximize the total cumulative reward** the agent receives over time.

$$
\text{Maximize: } \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t R_t \right]
$$

Where:

* $R_t$: Reward at time step $t$
* $\gamma$: Discount factor (0 ≤ γ ≤ 1) that balances **immediate** and **future** rewards

---

#### 2. **Key Terms in Reward Optimization**

| Term                   | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| **Reward**             | Immediate feedback from the environment after an action |
| **Return (Gₜ)**        | Total accumulated reward from time step $t$ onward      |
| **Policy (π)**         | A function that maps state to action (strategy to act)  |
| **Value Function (V)** | Expected return from a state under a policy             |
| **Q-function (Q)**     | Expected return from a state-action pair under a policy |

---

#### 3. **Approaches to Optimize Rewards**

---

### **A. Value-Based Methods**

* Learn the **value of being in a state** or **taking an action**.
* Use these values to guide the agent's decisions.

#### Examples:

* **Q-Learning**: Learn $Q(s, a)$ → derive optimal policy by picking action with max Q.
* **Value Iteration**, **Temporal Difference (TD)** learning

---

### **B. Policy-Based Methods**

* Learn the **policy directly** (i.e., the probability distribution over actions).
* Do not maintain value functions.

#### Examples:

* **Policy Gradient Methods**
* Useful for high-dimensional or continuous action spaces

---

### **C. Actor-Critic Methods (Hybrid)**

* Combine both value-based and policy-based ideas:

  * **Actor**: updates the policy (action selection)
  * **Critic**: evaluates the action taken using value function

---

#### 4. **Reward Engineering**

* Carefully designing reward signals is essential:

  * Too sparse → agent may never learn
  * Too dense → agent may overfit or exploit unintended behavior
* Rewards should **guide behavior** without ambiguity

---

#### 5. **Exploration for Reward Optimization**

* Optimizing rewards requires the agent to **explore** the environment.
* Common strategies:

  * **ε-greedy**: With probability ε, take a random action (explore)
  * **Softmax/Boltzmann**: Choose actions probabilistically based on estimated rewards
  * **Upper Confidence Bound (UCB)**: Choose actions that balance high reward and uncertainty

---

#### 6. **Delayed Rewards**

* In many environments, rewards are **not immediate**.

  * Example: Winning in chess gives a reward only at the end.
* RL methods learn to **assign credit** to earlier actions for final rewards (solved by credit assignment methods).

---

#### 7. **Discount Factor (γ)**

* Balances **immediate** vs. **future** rewards:

  * γ close to 0 → short-sighted (focus on immediate rewards)
  * γ close to 1 → long-term planning

---

#### 8. **Convergence**

* Reward optimization is successful when:

  * The **expected return is maximized** under the learned policy.
  * The **policy becomes stable** (agent doesn't change actions frequently).

---
### **Policy Search in Reinforcement Learning**

---

#### 1. **Definition**

* **Policy Search** refers to methods that aim to **directly learn the optimal policy** (π) that maps states to actions, rather than relying on value functions.
* It is especially useful when:

  * Action spaces are **continuous**.
  * Value function methods (like Q-learning) are difficult to apply.

---

#### 2. **What is a Policy?**

* A **policy π(a|s)** defines the probability of taking action $a$ in state $s$.
* Can be:

  * **Deterministic**: Always choose the same action for a state.

    $$
    \pi(s) = a
    $$
  * **Stochastic**: Choose actions probabilistically.

    $$
    \pi(a|s) = \mathbb{P}[a \mid s]
    $$

---

#### 3. **Goal of Policy Search**

* Find a policy $\pi$ that **maximizes the expected cumulative reward**:

$$
J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_{t=0}^{\infty} \gamma^t R_t \right]
$$

* Where $\theta$ are the **parameters** of the policy (e.g., weights in a neural network)

---

#### 4. **Types of Policy Search Methods**

---

### **A. Gradient-Free (Black-box) Methods**

* Do **not require gradients** of the objective function.
* Rely on evaluating performance and adjusting parameters heuristically.

#### Examples:

* **Random Search**
* **Genetic Algorithms**
* **Evolution Strategies (ES)**

---

### **B. Gradient-Based Methods (Policy Gradient)**

* Use **gradient ascent** to optimize the policy parameters.

* Update:

  $$
  \theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
  $$

* Where $\nabla_\theta J(\theta)$ is the **gradient of expected reward** with respect to policy parameters.

#### Examples:

* REINFORCE Algorithm
* Actor-Critic Methods

---

#### 5. **Advantages of Policy Search**

* Works well for **continuous action spaces**.
* Can represent **stochastic policies** (important in partially observable environments).
* Does **not require value function approximation** (in pure policy methods).
* Handles **high-dimensional** or **nonlinear** policy representations (e.g., neural networks).

---

#### 6. **Disadvantages**

| Problem                 | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| **High variance**       | Estimating policy gradients from sampled trajectories can be noisy. |
| **Sample inefficiency** | Requires many interactions with the environment.                    |
| **Local optima**        | May converge to suboptimal policies.                                |

---

#### 7. **Variance Reduction Techniques**

* **Baseline Subtraction**: Subtract a baseline (e.g., average return) from the reward to reduce gradient variance.
* **Advantage Functions**: Use the difference between Q-value and value function:

  $$
  A(s, a) = Q(s, a) - V(s)
  $$

---

#### 8. **Applications**

* Robotic control (e.g., movement, locomotion)
* Game playing (e.g., continuous action games)
* Resource allocation
* Autonomous navigation

---
### **Neural Network Policies in Reinforcement Learning**

---

#### 1. **Definition**

* **Neural Network Policies** refer to representing the **policy function π(a|s)** using a **neural network**.
* The network takes **state(s)** as input and outputs either:

  * A **probability distribution** over actions (for stochastic policies), or
  * A **specific action** (for deterministic policies).

---

#### 2. **Why Use Neural Networks?**

* Can model **complex, nonlinear relationships** between states and actions.
* Handle **high-dimensional state** and **action spaces**.
* Can **generalize** across similar states.

---

#### 3. **Architecture**

| Layer             | Role                                                    |
| ----------------- | ------------------------------------------------------- |
| **Input Layer**   | Receives the current **state** vector                   |
| **Hidden Layers** | Process state representation (may use ReLU, tanh, etc.) |
| **Output Layer**  | Outputs action or parameters for action distribution    |

---

#### 4. **Policy Types with Neural Networks**

---

### A. **Deterministic Policy Network**

* Outputs a specific action directly:

  $$
  a = \pi_\theta(s)
  $$
* Example: Used in **DDPG (Deep Deterministic Policy Gradient)**

---

### B. **Stochastic Policy Network**

* Outputs parameters of a probability distribution over actions:

  $$
  \pi_\theta(a|s) = \mathcal{N}(\mu(s), \sigma(s))
  $$
* Action is sampled from the output distribution.
* Example: Used in **REINFORCE**, **PPO**, **A3C**

---

#### 5. **Training Neural Network Policies**

* Use **Policy Gradient Algorithms**:

  * Compute gradient of expected return w\.r.t. policy parameters $\theta$
  * Update using stochastic gradient ascent:

    $$
    \theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
    $$

* Use **Backpropagation** to update network weights.

---

#### 6. **Loss Functions**

* For **REINFORCE**:

  $$
  L(\theta) = -\log \pi_\theta(a|s) \cdot R
  $$

* For **Actor-Critic**:

  $$
  L(\theta) = -\log \pi_\theta(a|s) \cdot A(s, a)
  $$

* Where $A(s, a)$ is the **advantage** function: $Q(s, a) - V(s)$

---

#### 7. **Exploration with Neural Policies**

* Introduce **stochasticity** via:

  * Sampling from output distribution
  * Adding noise (e.g., Gaussian noise for continuous actions)
* Encourages exploration and avoids premature convergence.

---

#### 8. **Challenges**

| Challenge               | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| **Instability**         | Policy updates can destabilize training if too large |
| **Sample inefficiency** | Neural networks often need many training episodes    |
| **High variance**       | Stochastic policies may produce noisy gradients      |

---

#### 9. **Common Algorithms Using NN Policies**

| Algorithm     | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| **REINFORCE** | Simple policy gradient with Monte Carlo returns             |
| **A2C / A3C** | Advantage Actor-Critic methods                              |
| **PPO**       | Proximal Policy Optimization (stable, widely used)          |
| **DDPG**      | Deep deterministic policy gradient (for continuous actions) |
| **SAC**       | Soft Actor-Critic (entropy-regularized, continuous actions) |

---

#### 10. **Applications**

* Robotics: controlling joint angles, manipulation
* Games: Atari, Go, Dota, etc.
* Autonomous vehicles: lane following, obstacle avoidance
* Smart grids, finance, operations research

---
### **Action Evaluation: Credit Assignment Problem**

---

#### 1. **Definition**

* The **Credit Assignment Problem** refers to the difficulty of determining **which specific actions** were responsible for **which outcomes**, especially when the **reward is delayed**.
* This is a core challenge in **reinforcement learning**, where the agent receives feedback **after a sequence of actions**, not immediately.

---

#### 2. **Why It Occurs**

* In many RL tasks, rewards are **not immediate**.

  * Example: Winning a game like chess provides a reward **only at the end**, but involves **hundreds of moves**.
* The agent must figure out **which past actions contributed** positively (or negatively) to the final outcome.

---

#### 3. **Types of Credit Assignment**

| Type                             | Description                                                                                               |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Temporal Credit Assignment**   | Determine **which past time step** contributed to the current reward                                      |
| **Structural Credit Assignment** | Determine **which component of a complex model** (e.g., which neuron in a neural network) caused a result |

---

#### 4. **Goal of Action Evaluation**

* Accurately **assign credit (or blame)** to actions so that:

  * Beneficial actions are **reinforced** (higher probability in policy).
  * Harmful actions are **discouraged**.

---

#### 5. **Common Solutions**

---

### A. **Temporal Difference (TD) Learning**

* Updates the value of a state using a **bootstrapped estimate** from the next state:

$$
V(s_t) \leftarrow V(s_t) + \alpha [r_t + \gamma V(s_{t+1}) - V(s_t)]
$$

* Helps in **propagating reward back in time** efficiently.

---

### B. **Eligibility Traces (TD(λ))**

* A technique that maintains **trace memory** of past actions.
* Rewards are **distributed to recent states** proportionally:

$$
\text{Trace}(s) \propto \lambda^t
$$

* $\lambda \in [0,1]$: Controls how far back the reward is credited.

---

### C. **Policy Gradient with Baselines**

* In **REINFORCE**, use the advantage function to reduce variance and improve credit assignment:

$$
\nabla_\theta J(\theta) \propto \nabla_\theta \log \pi_\theta(a|s) \cdot (R - b)
$$

* Where $b$ is a **baseline** (e.g., average return or value function).

---

### D. **Advantage Function**

$$
A(s, a) = Q(s, a) - V(s)
$$

* Helps isolate how **good an action is compared to average** at that state.
* Makes action evaluation more precise.

---

### E. **Monte Carlo Methods**

* Assign full return to all actions taken in the episode.
* Simple but has **high variance** and **poor temporal resolution**.

---

#### 6. **Challenges in Credit Assignment**

| Challenge                   | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| **Delayed Rewards**         | Difficult to trace rewards back to the exact action      |
| **Long episodes**           | More actions → harder to know which affected the outcome |
| **Stochastic environments** | Rewards may vary randomly despite same actions           |

---

#### 7. **Example**

* Pacman agent receives +100 reward after 50 moves.

  * Which of those 50 moves actually helped?
  * Credit assignment mechanisms help determine this and adjust the policy accordingly.

---

#### 8. **Importance**

* Poor credit assignment → **slow or unstable learning**
* Good credit assignment → **faster convergence** and **better performance**

---
### **Markov Decision Processes (MDP)**

---

#### 1. **Definition**

* A **Markov Decision Process (MDP)** is a **mathematical framework** used to model decision-making in environments where outcomes are partly **random** and partly under the **control of an agent**.
* It provides the formal foundation for **Reinforcement Learning (RL)** problems.

---

#### 2. **Components of an MDP**

An MDP is defined by a **5-tuple**:

$$
\text{MDP} = (S, A, P, R, \gamma)
$$

| Symbol | Meaning                                                                                                      |                                                                              |
| ------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **S**  | Set of **states**                                                                                            |                                                                              |
| **A**  | Set of **actions**                                                                                           |                                                                              |
| **P**  | **Transition probability** function: ( P(s'                                                                  | s, a) ) — probability of reaching state $s'$ from state $s$ using action $a$ |
| **R**  | **Reward function**: $R(s, a, s')$ — immediate reward for taking action $a$ in state $s$ and landing in $s'$ |                                                                              |
| **γ**  | **Discount factor**: $0 \le \gamma \le 1$ — how much the agent values future rewards                         |                                                                              |

---

#### 3. **Markov Property**

* The **Markov property** states that the **future is independent of the past**, given the present state.

$$
P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, \ldots) = P(s_{t+1} | s_t, a_t)
$$

* Only the current **state and action** are needed to predict the next state and reward.

---

#### 4. **Policy (π)**

* A **policy** is a strategy the agent uses to choose actions.

$$
\pi(a|s) = \text{Probability of taking action } a \text{ in state } s
$$

---

#### 5. **Value Functions**

These help evaluate the quality of states and actions under a policy $\pi$:

* **State-Value Function**:

$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_t \mid s_0 = s \right]
$$

* **Action-Value Function (Q-function)**:

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_t \mid s_0 = s, a_0 = a \right]
$$

---

#### 6. **Bellman Equations**

Used to compute value functions recursively.

* **Bellman Expectation Equation** (for policy π):

$$
V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s'} P(s'|s, a)[R(s, a, s') + \gamma V^\pi(s')]
$$

* **Bellman Optimality Equation** (for optimal policy π\*):

$$
V^*(s) = \max_a \sum_{s'} P(s'|s, a)[R(s, a, s') + \gamma V^*(s')]
$$

---

#### 7. **Goal in MDP**

* Find an **optimal policy $\pi^*$** that **maximizes the expected return**:

$$
\pi^* = \arg\max_\pi V^\pi(s), \quad \forall s \in S
$$

---

#### 8. **Solving MDPs**

| Method                  | Description                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| **Dynamic Programming** | Uses Bellman equations (requires full model knowledge)                      |
| **Value Iteration**     | Iteratively update value function until convergence                         |
| **Policy Iteration**    | Alternates between policy evaluation and improvement                        |
| **Model-Free RL**       | Approximate the solution from sampled experiences (e.g., Q-learning, SARSA) |

---

#### 9. **Example: Grid World**

* Agent moves in a 2D grid.
* Each action leads to a new state with some reward.
* Goal is to reach the goal state with maximum reward.
* This scenario fits naturally as an MDP.

---

#### 10. **Importance in RL**

* MDPs provide the **theoretical foundation** for most RL algorithms.
* Define the structure needed to compute **policies**, **value functions**, and perform **planning** or **learning**.

---
### **Q-Learning – Reinforcement Learning Algorithm**

---

#### 1. **Definition**

* **Q-Learning** is a **model-free**, **off-policy**, **value-based** reinforcement learning algorithm used to learn the **optimal action-value function** $Q^*(s, a)$.
* It learns how good an action is in a particular state, in terms of **expected future rewards**.

---

#### 2. **Goal**

* Find the optimal **Q-function**:

$$
Q^*(s, a) = \max_\pi \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t R_t \,|\, s_0 = s, a_0 = a, \pi \right]
$$

* Use this to derive the **optimal policy**:

$$
\pi^*(s) = \arg\max_a Q^*(s, a)
$$

---

#### 3. **Q-Function (Action-Value Function)**

* $Q(s, a)$ estimates the expected cumulative reward starting from state $s$, taking action $a$, and following the optimal policy thereafter.

---

#### 4. **Update Rule (Bellman Equation for Q-Learning)**

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_t + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]
$$

Where:

* $s_t$: current state
* $a_t$: action taken
* $r_t$: reward received
* $s_{t+1}$: next state
* $\alpha$: learning rate (0 < α ≤ 1)
* $\gamma$: discount factor (0 ≤ γ < 1)

---

#### 5. **Characteristics**

| Property               | Description                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Model-Free**         | Does not need to know the environment's transition model                                               |
| **Off-Policy**         | Learns the value of the optimal policy, regardless of the agent's actual actions (exploration allowed) |
| **Tabular Q-Learning** | Stores Q-values in a table (works well for small state-action spaces)                                  |

---

#### 6. **Exploration vs Exploitation**

* Common strategy: **ε-greedy**

  * With probability **ε**, choose a random action (explore)
  * With probability **1 - ε**, choose action that maximizes Q (exploit)

---

#### 7. **Algorithm Steps**

1. Initialize $Q(s, a)$ arbitrarily (e.g., zeros)
2. For each episode:

   * Initialize state $s$
   * For each step in episode:

     * Choose action $a$ using ε-greedy policy
     * Take action $a$, observe reward $r$ and next state $s'$
     * Update $Q(s, a)$ using the Q-learning update rule
     * Set $s \leftarrow s'$
3. Repeat until convergence

---

#### 8. **Convergence**

* Q-learning is proven to **converge to the optimal Q-function** $Q^*$, under the following conditions:

  * All state-action pairs are visited **infinitely often**
  * The **learning rate decays** properly over time

---

#### 9. **Limitations**

| Limitation                  | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| **Large/continuous spaces** | Tabular Q-learning becomes infeasible; needs function approximation |
| **High memory usage**       | Due to storing all Q-values explicitly                              |
| **Slow convergence**        | In complex or high-dimensional environments                         |

---

#### 10. **Extensions**

| Extension                         | Description                                                            |
| --------------------------------- | ---------------------------------------------------------------------- |
| **Deep Q-Learning (DQN)**         | Use neural networks to approximate Q-values in large/continuous spaces |
| **Double Q-Learning**             | Mitigates overestimation of Q-values                                   |
| **Prioritized Experience Replay** | Sample important transitions more often                                |
| **Dueling DQN**                   | Separate value and advantage estimation in the network                 |

---

### **Q-Learning: Function Explanation**

---

#### 1. **What is the Q-function?**

* The **Q-function**, also known as the **action-value function**, represents the **expected cumulative reward** of taking an action in a given state and following the **optimal policy** thereafter.

$$
Q(s, a) = \mathbb{E} \left[ \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \,\bigg|\, s_t = s, a_t = a \right]
$$

Where:

* $s$: current state
* $a$: action taken in state $s$
* $R_{t+k+1}$: reward received after $k$ steps
* $\gamma$: discount factor

---

#### 2. **Purpose of Q-function**

* **Evaluates actions**: Quantifies how good it is to take a specific action in a given state.
* **Used to derive optimal policy**:

  $$
  \pi^*(s) = \arg\max_a Q^*(s, a)
  $$

---

#### 3. **Bellman Optimality Equation for Q-function**

$$
Q^*(s, a) = \mathbb{E}_{s'} \left[ R(s, a, s') + \gamma \max_{a'} Q^*(s', a') \right]
$$

This equation defines the **recursive relationship**:

* The value of the current state-action pair equals the **immediate reward** plus the **discounted maximum future reward**.

---

#### 4. **Q-Learning Update Rule (Function Form)**

The core **update function** for Q-learning is:

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_t + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]
$$

Explanation of terms:

* $Q(s_t, a_t)$: current estimate of the Q-value
* $r_t$: reward received after taking action $a_t$ in state $s_t$
* $\max_{a'} Q(s_{t+1}, a')$: best possible Q-value for the next state $s_{t+1}$
* $\alpha$: learning rate (how much new info overrides old)

---

#### 5. **Role of Discount Factor $\gamma$**

* Balances the importance of **future rewards** versus **immediate rewards**.
* $\gamma = 0$: only care about immediate reward
* $\gamma \to 1$: care more about long-term reward

---

#### 6. **Policy from Q-function**

After training, the optimal policy is derived from the Q-function:

$$
\pi^*(s) = \arg\max_a Q(s, a)
$$

That is, in each state, pick the action with the **highest Q-value**.

---

#### 7. **Q-Table (Tabular Q-learning)**

* For small problems:

  * Store Q-values in a table with entries for each $(s, a)$ pair.
* The agent **looks up** and **updates** values during training.

---

#### 8. **Function Approximation**

* In large/continuous state spaces, use **function approximators** (like neural networks) instead of tables:

$$
Q(s, a) \approx Q_\theta(s, a)
$$

Where $\theta$ are the parameters (weights) of the function (e.g., a neural network).

---

#### 9. **Summary of Function Role**

| Purpose                            | Description                                |
| ---------------------------------- | ------------------------------------------ |
| **Evaluate actions**               | Predict long-term reward for each action   |
| **Update knowledge**               | Via Bellman-based Q-update                 |
| **Guide behavior (policy)**        | Choose action with highest Q-value         |
| **Generalize** (when approximated) | Apply learning to unseen or similar states |

---
### **Using Deep Q-Learning to Learn How to Play Pacman**

---

#### 1. **Problem Overview**

* **Pacman** is a classic video game where an agent (Pacman) navigates a maze, eats pellets, avoids ghosts, and maximizes score.
* The goal is to use **Deep Q-Learning (DQN)** to train an **agent** that learns to **play and win Pacman autonomously** by interacting with the game environment.

---

#### 2. **Why Use Deep Q-Learning?**

* **State space** in Pacman is **large and complex** (positions, directions, ghost states, etc.).
* **Tabular Q-learning** fails in such cases.
* DQN uses **deep neural networks** to approximate the **Q-function**, enabling learning in **high-dimensional** environments like video games.

---

#### 3. **Deep Q-Network (DQN) Architecture**

| Layer             | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| **Input Layer**   | Receives the game state (e.g., raw pixels, or processed grid features)        |
| **Hidden Layers** | Fully connected or convolutional layers to extract patterns from input        |
| **Output Layer**  | Outputs Q-values for each possible action (up, down, left, right, stay, etc.) |

---

#### 4. **State Representation**

* Options for input:

  * **Raw pixels** of the game screen (image input to CNN)
  * **Feature vectors** (Pacman position, ghost positions, remaining dots, direction, etc.)
* This representation is passed into the DQN to compute Q-values.

---

#### 5. **Action Space**

* Discrete set of actions:

  $$
  A = \{ \text{Up}, \text{Down}, \text{Left}, \text{Right}, \text{Stay} \}
  $$

---

#### 6. **Reward Function**

Designing a good **reward signal** is essential. Example:

| Game Event            | Reward |
| --------------------- | ------ |
| Eat a dot             | +1     |
| Eat a power pellet    | +5     |
| Eat a ghost           | +10    |
| Move into empty space | -0.1   |
| Get caught by ghost   | -20    |
| Win the game          | +50    |
| Lose the game         | -50    |

---

#### 7. **Training Loop (High-level Algorithm)**

1. **Initialize** DQN with random weights.
2. For each episode:

   * Start new game (initial state $s_0$)
   * While game is not over:

     1. Choose action $a_t$ using **ε-greedy** policy:

        * With ε probability: random action (explore)
        * Else: $a_t = \arg\max_a Q(s_t, a; \theta)$
     2. Take action $a_t$, observe **reward $r_t$** and **next state $s_{t+1}$**
     3. Store $(s_t, a_t, r_t, s_{t+1})$ in **experience replay buffer**
     4. Sample a **mini-batch** of experiences from the buffer
     5. Compute **target Q-value** using Bellman equation:

        $$
        y = r_t + \gamma \max_{a'} Q(s_{t+1}, a'; \theta^{-})
        $$

        (θ⁻ is the target network)
     6. Compute loss:

        $$
        L = \left( y - Q(s_t, a_t; \theta) \right)^2
        $$
     7. Perform **gradient descent** to minimize loss and update θ
     8. Periodically update **target network**: $\theta^{-} \leftarrow \theta$

---

#### 8. **Key Techniques Used in DQN**

| Technique                | Purpose                                                              |
| ------------------------ | -------------------------------------------------------------------- |
| **Experience Replay**    | Break correlation between consecutive experiences, improve stability |
| **Fixed Target Network** | Use a separate target network to reduce moving target problem        |
| **Frame Skipping**       | Only update every n frames for speed                                 |
| **Reward Clipping**      | Normalize rewards to prevent instability                             |

---

#### 9. **Convergence and Evaluation**

* Agent improves over time by:

  * Reducing collisions with ghosts
  * Maximizing points (eating pellets and ghosts)
  * Learning safe paths and strategic timing
* Evaluate agent by playing **several episodes** and measuring:

  * **Average score**
  * **Survival time**
  * **Number of games won**

---

#### 10. **Challenges in Pacman**

| Challenge                 | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| **Sparse rewards**        | Long periods without rewards (e.g., navigating toward dots)      |
| **Delayed consequences**  | Bad action may result in ghost collision several steps later     |
| **Partial observability** | Depending on input, agent may not see full game state            |
| **Exploration**           | Difficult due to many possible paths and ghost movement patterns |

---

#### 11. **Possible Improvements**

* **Double DQN**: Reduces overestimation bias.
* **Dueling DQN**: Separates state value and advantage estimation.
* **Prioritized Replay**: Sample important transitions more frequently.
* **Convolutional layers**: If using image inputs, use CNNs to improve spatial feature learning.

---

#### 12. **Outcome**

* After sufficient training, the **DQN agent can learn to play Pacman effectively**:

  * Avoids ghosts strategically
  * Prioritizes pellet consumption
  * Uses power pellets to hunt ghosts
  * Navigates maze efficiently

---

