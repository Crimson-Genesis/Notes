# Unit - 4 -> Reinforcement Learning
Introduction, Learning How to Optimize Rewards, Policy Search, Neural Network Policies, Action Evaluation: Credit Assignment problem, Using Policy Gradients, Markow Decision Processes, Q Learning
- Function, Using Deep QLearning to learn how to play Pacman.

## Content ->

### **Unit 4: Reinforcement Learning – Introduction**

#### 1. **Definition of Reinforcement Learning (RL)**

* Reinforcement Learning is a type of Machine Learning where an **agent** learns to make decisions by interacting with an **environment** to maximize **cumulative rewards** over time.
* It is inspired by **behavioral psychology** and **trial-and-error learning**.

#### 2. **Key Components of Reinforcement Learning**

* **Agent**: The learner or decision maker.
* **Environment**: The external system the agent interacts with.
* **State (S)**: A snapshot of the environment at a specific time.
* **Action (A)**: A choice the agent can make in a given state.
* **Reward (R)**: A scalar feedback signal received after taking an action.
* **Policy (π)**: A strategy used by the agent to determine the next action based on the current state.
* **Value Function (V)**: A prediction of future rewards from a given state.
* **Q-Value Function (Q)**: Predicts total reward of taking an action in a given state and following a policy thereafter.

#### 3. **Basic Workflow**

```
Agent --(action)--> Environment --(new state, reward)--> Agent
```

* The agent receives a **state**, performs an **action**, receives a **reward**, and transitions to a **new state**.

#### 4. **Types of RL Learning Settings**

* **Model-Free RL**: Learns directly from interaction without modeling the environment (e.g., Q-Learning, SARSA).
* **Model-Based RL**: Builds a model of the environment and uses planning algorithms (e.g., Dyna-Q).

#### 5. **Goals in RL**

* Learn an **optimal policy** that maximizes the **expected cumulative reward**, often formulated as:

  $$
  G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
  $$

  * Where $\gamma \in [0,1]$ is the **discount factor**.

#### 6. **Exploration vs Exploitation**

* **Exploration**: Trying new actions to discover their rewards.
* **Exploitation**: Choosing actions that give maximum reward based on past knowledge.
* Balance between the two is critical in RL.

#### 7. **Applications of Reinforcement Learning**

* **Games**: Playing Atari, Chess, Go (e.g., AlphaGo)
* **Robotics**: Robot control and navigation
* **Finance**: Portfolio management
* **Healthcare**: Dynamic treatment plans
* **Self-driving Cars**: Route planning and decision-making

#### 8. **Example: Simple Python RL Environment with OpenAI Gym**

```python
import gym

# Create the environment
env = gym.make("CartPole-v1")
state = env.reset()

done = False
while not done:
    env.render()              # Show simulation
    action = env.action_space.sample()  # Random action
    state, reward, done, info = env.step(action)

env.close()
```

* **env**: represents the environment
* **action\_space.sample()**: selects a random action
* **env.step(action)**: applies the action, returns new state, reward, and termination flag

This represents a basic RL loop with random actions, a starting point for learning optimal policies.

### **Learning How to Optimize Rewards – Reinforcement Learning**

---

In Reinforcement Learning (RL), the **core objective** is to **maximize cumulative rewards over time**. The agent interacts with the environment, learns from the feedback (reward), and improves its decision-making policy accordingly.

---

### **1. Cumulative Reward Optimization Goal**

* The agent’s goal is to learn a policy $\pi$ that **maximizes the expected cumulative reward**:

  $$
  G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
  $$

  Where:

  * $G_t$: total return at time $t$
  * $R_{t+k+1}$: reward at time $t+k+1$
  * $\gamma$: discount factor $(0 \leq \gamma \leq 1)$

---

### **2. Reward Signal (R)**

* The **reward** is a scalar signal from the environment indicating the **desirability** of the last action taken.
* **Positive reward** encourages the behavior.
* **Negative reward (penalty)** discourages the behavior.
* Learning is driven by this reward signal.

---

### **3. Objective Function to Maximize**

* RL optimizes the **expected return** over time:

  $$
  J(\pi) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R_t \right]
  $$

  * The policy $\pi$ defines how actions are selected.
  * The agent aims to find $\pi^*$, the **optimal policy**.

---

### **4. Value Functions (Prediction-Based Optimization)**

* Value functions estimate how **good** a state or state-action pair is.

  #### a. State-Value Function $V^{\pi}(s)$:

  $$
  V^{\pi}(s) = \mathbb{E}_{\pi} \left[ G_t | S_t = s \right]
  $$

  #### b. Action-Value Function $Q^{\pi}(s, a)$:

  $$
  Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ G_t | S_t = s, A_t = a \right]
  $$

---

### **5. Optimization Techniques in RL**

#### a. **Dynamic Programming (DP)**

* Requires a model of the environment (transition probabilities).
* Solves Bellman equations to find optimal policy.

#### b. **Monte Carlo Methods**

* Estimate value functions using sample episodes.
* Learn from actual rewards after complete episodes.

#### c. **Temporal Difference (TD) Learning**

* Combines ideas from DP and Monte Carlo.
* Learns directly from raw experience using:

  $$
  V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]
  $$

#### d. **Q-Learning (Off-policy TD Control)**

* Learns optimal action-value function:

  $$
  Q(s,a) \leftarrow Q(s,a) + \alpha [R + \gamma \max_{a'} Q(s',a') - Q(s,a)]
  $$

#### e. **Policy Gradient Methods**

* Directly optimize the policy by computing the gradient of expected return with respect to policy parameters $\theta$:

  $$
  \nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) Q^{\pi_\theta}(s, a) \right]
  $$

---

### **6. Exploration vs Exploitation**

* **Exploration**: Try new actions to discover their rewards.
* **Exploitation**: Choose actions that are currently estimated to be best.
* Balance via methods like:

  * **ε-greedy**: With probability $\epsilon$, choose random action.
  * **Softmax**: Select action probabilistically based on Q-values.

---

### **7. Learning Algorithms Examples**

| Algorithm  | Type            | Characteristics                              |
| ---------- | --------------- | -------------------------------------------- |
| Q-Learning | Model-Free      | Off-policy, learns optimal Q-values          |
| SARSA      | Model-Free      | On-policy, updates based on agent’s behavior |
| DDPG       | Actor-Critic    | For continuous action spaces                 |
| PPO / A3C  | Policy Gradient | Stable training in deep RL                   |

---

### **8. Summary**

* The core idea in RL is to optimize a **policy** that maximizes the **expected cumulative reward**.
* This is achieved through **value estimation**, **reward-based feedback**, and **improvement strategies** like TD learning or policy gradients.
* **Function approximation** (e.g., neural networks) is used in **deep RL** when the state/action space is large or continuous.

### **Policy Search – Reinforcement Learning**

---

In reinforcement learning (RL), **Policy Search** refers to a class of methods where the agent directly searches for the optimal policy **π** without relying on value functions like $V(s)$ or $Q(s, a)$. Instead of evaluating actions via expected cumulative rewards (value-based methods), policy search methods **optimize the policy itself** to maximize expected return.

---

### **1. What is a Policy?**

* A **policy** $\pi$ defines the agent’s behavior:

  * **Deterministic Policy**: $a = \pi(s)$
  * **Stochastic Policy**: $\pi(a|s) = P(A_t = a | S_t = s)$

The goal is to find the **optimal policy** $\pi^*$ that maximizes the expected reward.

---

### **2. Policy Parameterization**

* Policies are often **parameterized** by $\theta$ (e.g., weights of a neural network):

  $$
  \pi_\theta(a|s)
  $$
* The optimization problem becomes:

  $$
  \theta^* = \arg\max_\theta J(\theta)
  $$

  where $J(\theta) = \mathbb{E}_{\pi_\theta}[G_t]$

---

### **3. Categories of Policy Search Methods**

#### a. **Gradient-Free Methods (Black-box Optimization)**

* Use random search or evolutionary strategies to explore the policy space.
* Examples:

  * **Cross-Entropy Method (CEM)**
  * **Genetic Algorithms**
  * **CMA-ES (Covariance Matrix Adaptation Evolution Strategy)**

#### b. **Gradient-Based Methods (Policy Gradient)**

* Use the gradient of the objective function $J(\theta)$ to improve the policy.
* Update rule:

  $$
  \theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
  $$
* Gradient is estimated using sampled episodes:

  $$
  \nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) \cdot Q^{\pi}(s, a) \right]
  $$

---

### **4. Policy Gradient Theorem**

* Provides a way to compute the gradient of the performance measure:

  $$
  \nabla_\theta J(\theta) = \sum_s d^{\pi_\theta}(s) \sum_a \nabla_\theta \pi_\theta(a|s) Q^{\pi_\theta}(s, a)
  $$
* Where $d^{\pi_\theta}(s)$ is the state distribution under policy $\pi_\theta$.

---

### **5. REINFORCE Algorithm (Monte Carlo Policy Gradient)**

* A simple episodic policy gradient algorithm:

  * Run episode with current policy.
  * After complete episode, update parameters:

    $$
    \theta \leftarrow \theta + \alpha \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t) G_t
    $$

---

### **6. Advanced Policy Search Algorithms**

| Algorithm        | Description                                       |
| ---------------- | ------------------------------------------------- |
| **REINFORCE**    | Monte Carlo policy gradient method                |
| **Actor-Critic** | Combines policy gradient with value function      |
| **TRPO**         | Trust Region Policy Optimization – stable updates |
| **PPO**          | Proximal Policy Optimization – clipped objective  |
| **A3C**          | Asynchronous Advantage Actor-Critic               |

---

### **7. Advantages of Policy Search**

* Effective in **high-dimensional**, **continuous** action spaces.
* Can model **stochastic policies**.
* Suitable for **non-differentiable reward functions** (in black-box variants).

---

### **8. Disadvantages**

* Gradient estimates may have **high variance**.
* **Sample inefficient** – needs many episodes.
* May converge to **local optima**.

---

### **9. Summary**

* **Policy search** directly learns the policy that maps states to actions by optimizing the expected reward.
* **Gradient-based methods** (like REINFORCE and PPO) are widely used in **Deep RL**.
* Policy search is crucial for solving complex tasks with **continuous action spaces**, **partial observability**, and **non-linear policies**.

### **Neural Network Policies in Reinforcement Learning**

---

In reinforcement learning (RL), **Neural Network Policies** refer to using **neural networks (NNs)** to represent and approximate the policy $\pi(a|s)$. These networks are trained to map input states to output actions (or action probabilities), allowing agents to act optimally in high-dimensional and complex environments.

---

### **1. What is a Policy?**

* A **policy** defines the agent’s behavior by mapping from state $s$ to action $a$.

  * **Deterministic**: $a = \pi(s)$
  * **Stochastic**: $\pi(a|s) = P(A = a | S = s)$

---

### **2. Why Use Neural Networks for Policies?**

* Handle **complex, non-linear** relationships between states and actions.
* Work with **continuous state and/or action spaces**.
* Scale well with large inputs (e.g., images, sensor data).
* Can **generalize** across unseen states.

---

### **3. Structure of Neural Network Policy**

* **Input Layer**: Represents the state vector $s$.
* **Hidden Layers**: Capture complex patterns and abstractions.
* **Output Layer**:

  * **Discrete actions**: Output probabilities (softmax).
  * **Continuous actions**: Output mean and variance of a distribution (e.g., Gaussian).

---

### **4. Training the Neural Network Policy**

* The policy network is parameterized by $\theta$, so we write $\pi_\theta(a|s)$.
* Objective: Maximize expected cumulative reward:

  $$
  J(\theta) = \mathbb{E}_{\pi_\theta}[R]
  $$
* Update rule (Policy Gradient):

  $$
  \theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
  $$

---

### **5. Example: Policy Network with REINFORCE Algorithm**

```python
import gym
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

# Define Policy Network
class PolicyNN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PolicyNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.fc(x)

# Setup environment
env = gym.make("CartPole-v1")
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

policy = PolicyNN(state_dim, action_dim)
optimizer = optim.Adam(policy.parameters(), lr=0.01)

# REINFORCE Training Loop
for episode in range(1000):
    state = env.reset()
    log_probs = []
    rewards = []
    done = False

    while not done:
        state_tensor = torch.FloatTensor(state)
        probs = policy(state_tensor)
        dist = Categorical(probs)
        action = dist.sample()
        log_probs.append(dist.log_prob(action))

        state, reward, done, _ = env.step(action.item())
        rewards.append(reward)

    # Compute return and update policy
    G = sum(rewards)
    loss = -sum(log_probs) * G
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

### **6. Types of Neural Network Policies**

| Type                    | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| **Feedforward NN**      | Basic network for simple policies.                    |
| **CNN (Convolutional)** | Used for image input environments (e.g., Atari).      |
| **RNN/LSTM**            | Used for partially observable environments.           |
| **Actor Network**       | In Actor-Critic models – decides actions.             |
| **Policy Network**      | Generic term for NN representing the policy function. |

---

### **7. Applications**

* **Games**: e.g., Deep Q-Network with CNN policies in Atari.
* **Robotics**: e.g., controlling robotic arms using learned NN policies.
* **Autonomous Vehicles**: Mapping sensor input to driving actions.
* **Finance**: Optimizing trading strategies.

---

### **8. Challenges**

* **Instability**: Gradient updates can be unstable in deep networks.
* **Exploration vs. Exploitation**: Hard to balance.
* **Sample Inefficiency**: Needs many interactions with the environment.
* **Catastrophic forgetting**: NN may forget previous strategies.

---

### **9. Summary**

* **Neural network policies** enable agents to handle **complex environments** and **continuous action spaces**.
* Training is done using **policy gradient methods** or **actor-critic frameworks**.
* They form the backbone of **Deep Reinforcement Learning** (DRL) systems like DDPG, PPO, A3C, etc.

### **Action Evaluation: Credit Assignment Problem**

---

### **1. Introduction**

In **reinforcement learning (RL)**, agents take actions in an environment to maximize cumulative rewards. However, evaluating **which specific actions contributed to the rewards** is not always straightforward. This is known as the **credit assignment problem**.

---

### **2. What is the Credit Assignment Problem?**

* It refers to the difficulty of determining **which actions (or states)** were responsible for obtaining a particular reward.
* Occurs when rewards are **delayed** (not immediately after the action) or when **multiple actions** contribute jointly to the outcome.

---

### **3. Types of Credit Assignment**

| Type                             | Description                                                                                          |
| -------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Temporal Credit Assignment**   | When the effect of an action is only visible after a **time delay**.                                 |
| **Structural Credit Assignment** | When **multiple agents/nodes/neurons** contribute to a decision, it's hard to know **who did what**. |

---

### **4. Importance of Action Evaluation**

* Correctly assigning credit helps:

  * Improve the **learning efficiency** of the agent.
  * Make accurate **policy updates**.
  * Increase **reward** by reinforcing the **right behavior**.

---

### **5. Techniques for Credit Assignment**

#### **A. Monte Carlo Methods**

* Evaluate the action by averaging rewards from **complete episodes**.
* Pros: Simple and unbiased.
* Cons: High variance and inefficient for long episodes.

#### **B. Temporal-Difference (TD) Learning**

* Learn from **partial returns** by bootstrapping.
* TD Target:

  $$
  R_t + \gamma V(s_{t+1})
  $$
* More efficient for delayed rewards.

#### **C. Policy Gradient Methods**

* Estimate **gradient of expected reward** with respect to policy parameters.
* Use **log-likelihood trick** and return as weight:

  $$
  \nabla_\theta J(\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a|s) \cdot G_t]
  $$

#### **D. Advantage Function**

* Measures how much better an action is compared to the average:

  $$
  A(s, a) = Q(s, a) - V(s)
  $$
* Helps in **reducing variance** during training.

---

### **6. Example: REINFORCE with Baseline (to solve credit assignment)**

```python
loss = -log_prob * (G - baseline)
```

* Here, `G` is the return, and `baseline` is an estimate of state value $V(s)$.
* Helps **assign better credit** by comparing actual outcome to expected outcome.

---

### **7. Real-World Example**

In a game:

* You press multiple buttons to defeat a boss.
* You only get the reward at the end.
* Which button press contributed most?
* The agent must **assign credit** to the most **effective actions** during the game.

---

### **8. Challenges in Credit Assignment**

| Challenge             | Explanation                                            |
| --------------------- | ------------------------------------------------------ |
| **Delayed rewards**   | Actions may lead to reward only after many steps.      |
| **Sparse rewards**    | Environment gives reward very rarely.                  |
| **Noisy environment** | Makes evaluation of action outcomes harder.            |
| **Long sequences**    | Hard to trace influence of an action after many steps. |

---

### **9. Neural Network and Credit Assignment**

* In deep RL, neural networks approximate value and policy functions.
* The **gradient flow** through layers indirectly assigns credit.
* Techniques like **backpropagation through time (BPTT)** help in sequential tasks (e.g., LSTM policies).

---

### **10. Summary**

* **Action evaluation** is essential for learning which actions help or harm performance.
* **Credit assignment problem** is central to reinforcement learning.
* Solved using **TD methods, advantage functions, baselines**, and **gradient-based learning**.
* Poor credit assignment leads to slow or unstable learning.

### **Credit Assignment Problem in Reinforcement Learning**

---

### **1. Definition**

The **Credit Assignment Problem** is a core challenge in **Reinforcement Learning (RL)** that involves determining **which actions** (out of a sequence of many) are responsible for receiving a **particular reward**. The agent performs many actions before receiving a reward, so it's difficult to decide which of those actions caused the outcome.

---

### **2. Types of Credit Assignment Problems**

| Type                             | Description                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Temporal Credit Assignment**   | Refers to identifying **when** the right action was taken. Important when rewards are **delayed**.           |
| **Structural Credit Assignment** | Refers to identifying **which part** of a system (e.g., neuron, agent, rule) contributed most to the result. |

---

### **3. Examples**

#### **Temporal Example**

An RL agent plays a game and gets a reward only at the end. Which previous move helped it win?

#### **Structural Example**

In a neural network, many neurons activate before a decision. Which neuron had the most useful contribution?

---

### **4. Why It’s a Problem**

* Rewards are often **delayed**.
* Many actions/states might have contributed jointly.
* The same action might lead to **different outcomes** in different situations (non-determinism).
* Difficult to train policies without knowing which actions were good or bad.

---

### **5. Formal View**

Let:

* $R_t$: reward at time $t$
* $a_t$: action taken at time $t$
* $\pi_\theta(a|s)$: policy parameterized by $\theta$

Then:

* To assign credit, we compute gradient:

  $$
  \nabla_\theta J(\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a_t|s_t) \cdot G_t]
  $$
* This is the **policy gradient theorem**, which helps in attributing returns to actions.

---

### **6. Solutions/Techniques**

| Method                                | Description                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Monte Carlo Methods**               | Assign total reward at end of episode to all past actions.                                                 |
| **Temporal Difference (TD) Learning** | Learn from partial future rewards using bootstrapping.                                                     |
| **TD(λ)**                             | Combines TD and Monte Carlo by assigning credit to a **decay-weighted** history of actions.                |
| **Eligibility Traces**                | Maintains a trace of visited states/actions to spread credit across time.                                  |
| **Advantage Functions**               | $A(s,a) = Q(s,a) - V(s)$: tells how much better an action is compared to average.                          |
| **Baselines**                         | Helps reduce variance by subtracting expected value from reward to better isolate the impact of an action. |

---

### **7. Credit Assignment in Deep RL**

* In deep neural networks:

  * **Backpropagation** through the network layers is a form of **structural credit assignment**.
  * **Backpropagation Through Time (BPTT)** is used in recurrent networks for temporal credit assignment.

---

### **8. Importance**

* Correct credit assignment:

  * Speeds up learning.
  * Prevents reinforcement of bad actions.
  * Improves policy and value estimation accuracy.

---

### **9. Challenges**

| Challenge                 | Explanation                                                  |
| ------------------------- | ------------------------------------------------------------ |
| **Delayed Rewards**       | Makes it hard to trace which past actions caused the reward. |
| **Sparse Rewards**        | Fewer signals to guide learning.                             |
| **Long Action Sequences** | More noise and uncertainty in attribution.                   |
| **Stochasticity**         | Actions may not always lead to same outcomes.                |

---

### **10. Summary**

* The **Credit Assignment Problem** is about figuring out which actions deserve praise or blame.
* Two main forms: **temporal** and **structural**.
* Addressed via methods like **TD learning, eligibility traces, policy gradients**, and **advantage estimation**.
* Essential for **efficient and effective** RL policy learning.

### **Markov Decision Processes (MDPs)**

---

### **1. Definition**

A **Markov Decision Process (MDP)** is a mathematical framework used to model **decision-making problems** in **reinforcement learning**, where outcomes are partly random and partly under the control of a decision-maker.

It provides a formalism for modeling **environments** where agents must make sequences of decisions to maximize **cumulative rewards**.

---

### **2. Components of MDP**

An MDP is defined by a **5-tuple**:

$$
\text{MDP} = (S, A, P, R, \gamma)
$$

| Element            | Description                                                                       |                                                                                                |
| ------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| $S$                | Set of **states** (the environment situations)                                    |                                                                                                |
| $A$                | Set of **actions** (available to the agent in each state)                         |                                                                                                |
| ( P(s'             | s,a) )                                                                            | **Transition probability**: probability of reaching state $s'$ from state $s$ after action $a$ |
| $R(s,a)$           | **Reward function**: expected immediate reward for taking action $a$ in state $s$ |                                                                                                |
| $\gamma \in [0,1]$ | **Discount factor**: determines the importance of future rewards                  |                                                                                                |

---

### **3. Markov Property**

The process satisfies the **Markov property**:

$$
P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, \ldots, s_0, a_0) = P(s_{t+1} | s_t, a_t)
$$

This means the future state **only depends** on the **current state** and **action**, not on the past.

---

### **4. Policy**

A **policy** $\pi(a|s)$ is a function that defines the **probability** of taking action $a$ in state $s$. The goal in MDP is to find an **optimal policy** $\pi^*$ that **maximizes expected cumulative rewards**.

---

### **5. Value Functions**

#### a. **State Value Function $V^\pi(s)$**

The expected return starting from state $s$ and following policy $\pi$:

$$
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s \right]
$$

#### b. **Action Value Function $Q^\pi(s, a)$**

The expected return starting from state $s$, taking action $a$, and then following policy $\pi$:

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s, a_0 = a \right]
$$

---

### **6. Bellman Equations**

#### a. **Bellman Expectation Equation for $V^\pi(s)$:**

$$
V^\pi(s) = \sum_{a} \pi(a|s) \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s') \right]
$$

#### b. **Bellman Optimality Equation:**

$$
V^*(s) = \max_{a} \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s') \right]
$$

---

### **7. Solving an MDP**

#### a. **Policy Iteration**

1. Start with a random policy $\pi$
2. **Policy Evaluation**: compute $V^\pi(s)$
3. **Policy Improvement**: update policy by choosing better actions
4. Repeat until policy converges

#### b. **Value Iteration**

1. Initialize $V(s)$ arbitrarily
2. Iteratively apply Bellman optimality equation:

   $$
   V(s) \leftarrow \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s') \right]
   $$
3. Extract optimal policy from $V^*(s)$

---

### **8. Applications**

* Robot navigation
* Game playing (e.g., chess, Go)
* Inventory management
* Decision support systems

---

### **9. Visualization**

A simple MDP:

```
States: S1 ---a---> S2 ---a---> S3
Rewards:     0        1        10
```

Agent must choose the correct actions to reach S3 and collect the highest total reward.

---

### **10. Summary**

* **MDPs** model the environment in RL where actions lead to rewards and next states.
* The **Markov property** ensures only the current state is needed for decision-making.
* RL algorithms use **MDPs** to find optimal policies through **value functions** and **Bellman equations**.
* Solving MDPs yields the best strategy to **maximize expected rewards over time**.

### **Q-Learning**

---

Q-Learning is a **model-free**, **off-policy** reinforcement learning algorithm used to learn the optimal **action-selection policy** that maximizes the total reward over time.

---

### **1. Objective of Q-Learning**

The main goal is to learn the **optimal action-value function** $Q^*(s, a)$, which gives the **maximum expected cumulative reward** achievable by taking action $a$ in state $s$, and thereafter following the **optimal policy**.

---

### **2. Q-Function (Action-Value Function)**

$$
Q(s, a) = \text{Expected total reward if agent starts from state } s, \text{ takes action } a, \text{ then follows optimal policy}
$$

---

### **3. Q-Learning Update Rule (Function)**

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

#### **Where:**

| Symbol                | Meaning                                                                          |
| --------------------- | -------------------------------------------------------------------------------- |
| $s$                   | Current state                                                                    |
| $a$                   | Action taken                                                                     |
| $r$                   | Immediate reward received                                                        |
| $s'$                  | Next state                                                                       |
| $\alpha$              | Learning rate (step size, 0 < $\alpha$ ≤ 1)                                      |
| $\gamma$              | Discount factor (0 ≤ $\gamma$ < 1)                                               |
| $\max_{a'} Q(s', a')$ | Maximum predicted Q-value for the next state $s'$ over all possible actions $a'$ |

---

### **4. Working Mechanism**

1. **Initialize** the Q-table (a 2D array of states × actions) arbitrarily, usually with zeros.
2. **For each episode:**

   * Initialize the starting state $s$
   * Repeat until terminal state:

     * Choose action $a$ using a policy (e.g., ε-greedy)
     * Take action $a$, observe reward $r$ and next state $s'$
     * Update Q-table using the update rule
     * Move to new state $s'$
3. Repeat over many episodes until Q-values converge.

---

### **5. ε-Greedy Action Selection Policy**

To balance **exploration** and **exploitation**:

* With probability $\epsilon$, choose a **random** action (exploration)
* With probability $1 - \epsilon$, choose the **best-known** action (exploitation)

---

### **6. Q-Learning Characteristics**

| Aspect          | Description                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**        | Model-free, off-policy                                                                                      |
| **Goal**        | Learn $Q^*(s, a)$ to derive optimal policy $\pi^*(s) = \arg\max_a Q^*(s, a)$                                |
| **Policy Used** | Behavior policy (e.g., ε-greedy), different from the target policy                                          |
| **Convergence** | Guaranteed under certain conditions (finite state-action space, proper exploration, decaying learning rate) |

---

### **7. Pseudocode**

```
Initialize Q(s, a) arbitrarily for all s ∈ S, a ∈ A(s)
Repeat (for each episode):
    Initialize s
    Repeat (for each step of episode):
        Choose a from s using policy derived from Q (e.g., ε-greedy)
        Take action a, observe r and s'
        Q(s, a) ← Q(s, a) + α [r + γ max_a' Q(s', a') − Q(s, a)]
        s ← s'
    until s is terminal
```

---

### **8. Simple Example**

Suppose the agent has 3 states (A, B, C) and 2 actions (left, right). The agent updates the Q-table during learning episodes and learns the best actions to reach a goal state with the highest reward.

---

### **9. Use Cases**

* Game AI (e.g., Pacman, CartPole)
* Robotics (navigation)
* Network routing
* Finance (stock trading)

---

### **10. Summary**

* Q-learning learns the optimal action-value function using trial and error.
* It updates Q-values using Bellman equation.
* Uses ε-greedy strategy to balance learning and exploitation.
* Does **not** require knowledge of the environment model.
* Can be extended with **Deep Q-Networks (DQN)** for high-dimensional state spaces.

### **Using Deep Q-Learning to Learn How to Play Pacman**

---

Deep Q-Learning is a combination of **Q-learning** and **deep neural networks**, used to approximate the Q-function in environments with large or continuous state spaces like **Pacman**.

---

## **1. Problem with Traditional Q-Learning**

* In Pacman, the state space is very large (e.g., board configuration, positions of ghosts, pellets, etc.).
* Maintaining a Q-table for every (state, action) pair is **infeasible**.
* Solution: Use a **deep neural network** (DNN) as a **function approximator** for $Q(s, a)$.

---

## **2. Deep Q-Network (DQN)**

### **Objective:**

Learn a neural network $Q(s, a; \theta)$ where:

* $s$ = input state
* $a$ = action
* $\theta$ = network parameters
* Output: predicted Q-value for each action

---

## **3. Key Components of DQN**

| Component          | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| **Q-Network**      | Predicts Q-values for all actions given a state                                        |
| **Target Network** | A separate copy of Q-network, updated less frequently, for stable learning             |
| **Replay Buffer**  | Stores past experiences (s, a, r, s') to break correlation between consecutive samples |
| **Loss Function**  | Measures difference between predicted Q and target Q                                   |
| **Optimizer**      | Updates weights $\theta$ using gradient descent                                        |

---

## **4. DQN Loss Function**

$$
\mathcal{L}(\theta) = \left[ r + \gamma \max_{a'} Q(s', a'; \theta^-) - Q(s, a; \theta) \right]^2
$$

Where:

* $\theta$: current Q-network parameters
* $\theta^-$: target network parameters (copied periodically from $\theta$)

---

## **5. Algorithm Overview**

### **Initialize:**

* Q-network with weights $\theta$
* Target network with weights $\theta^- = \theta$
* Experience replay buffer $D$

---

### **Training Loop:**

1. **Observe state** $s$
2. **Choose action** $a$ using ε-greedy on Q-network
3. **Take action**, observe **reward $r$** and **next state $s'$**
4. **Store** transition $(s, a, r, s')$ in replay buffer
5. **Sample minibatch** from buffer
6. **Compute target Q-values** using target network
7. **Update Q-network** weights via backpropagation
8. Every fixed steps, **update target network**: $\theta^- \leftarrow \theta$

---

## **6. Input Representation for Pacman**

| Feature          | Description                |
| ---------------- | -------------------------- |
| Board layout     | Encoded as matrix or image |
| Pacman position  | x, y coordinates           |
| Ghost positions  | x, y of each ghost         |
| Pellet locations | Binary grid or image       |
| Direction/motion | Previous action taken      |

---

## **7. Output Layer (Actions)**

Q-network outputs **Q-values for each possible action**:

* `["up", "down", "left", "right"]`

Choose the action with **maximum Q-value**:

$$
a = \arg\max_a Q(s, a; \theta)
$$

---

## **8. Python Pseudocode**

```python
import gym
import numpy as np
import torch.nn as nn
import torch.optim as optim
import random

# Assume `PacmanEnv` is a gym-like Pacman environment

class QNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(QNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )
    
    def forward(self, x):
        return self.fc(x)

# Initialize environment
env = PacmanEnv()
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

q_net = QNetwork(state_dim, action_dim)
target_net = QNetwork(state_dim, action_dim)
target_net.load_state_dict(q_net.state_dict())

optimizer = optim.Adam(q_net.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

replay_buffer = []

for episode in range(1000):
    state = env.reset()
    done = False

    while not done:
        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            with torch.no_grad():
                action = torch.argmax(q_net(torch.tensor(state, dtype=torch.float32))).item()

        next_state, reward, done, _ = env.step(action)
        replay_buffer.append((state, action, reward, next_state, done))
        
        # Train
        if len(replay_buffer) >= batch_size:
            batch = random.sample(replay_buffer, batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)

            states = torch.tensor(states, dtype=torch.float32)
            actions = torch.tensor(actions).unsqueeze(1)
            rewards = torch.tensor(rewards, dtype=torch.float32).unsqueeze(1)
            next_states = torch.tensor(next_states, dtype=torch.float32)
            dones = torch.tensor(dones, dtype=torch.float32).unsqueeze(1)

            q_values = q_net(states).gather(1, actions)
            max_next_q = target_net(next_states).max(1)[0].unsqueeze(1)
            target_q = rewards + gamma * max_next_q * (1 - dones)

            loss = loss_fn(q_values, target_q)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        state = next_state

    if episode % target_update_freq == 0:
        target_net.load_state_dict(q_net.state_dict())
```

---

## **9. Summary**

| Concept        | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| Purpose        | Train an agent to play Pacman using Q-learning + Neural Network        |
| Benefit        | Works on high-dimensional input (e.g., grid image or pixel values)     |
| Key Techniques | DQN, replay buffer, target network, ε-greedy policy                    |
| Result         | Agent learns a policy to collect pellets, avoid ghosts, maximize score |

---

