#!/usr/bin/env python

import numpy as np
import gymnasium as gym

# Create the FrozenLake environment (4x4 grid, slippery by default)
env = gym.make("FrozenLake-v1", is_slippery=True)

# Initialize Q-table with zeros
state_size = env.observation_space.n   # Number of states
action_size = env.action_space.n       # Number of actions
Q = np.zeros((state_size, action_size))

# Hyperparameters
learning_rate = 0.8
discount_factor = 0.95
epsilon = 1.0        # Exploration rate
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000
max_steps = 100

# Training
rewards = []

for episode in range(episodes):
    state, _ = env.reset()
    total_rewards = 0
    done = False

    for _ in range(max_steps):
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state, :])     # Exploit

        # Take action and observe outcome
        new_state, reward, done, truncated, info = env.step(action)

        # Update Q-value using Q-Learning formula
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + discount_factor * np.max(Q[new_state, :]) - Q[state, action]
        )

        state = new_state
        total_rewards += reward

        if done:
            break

    # Decay epsilon (exploration probability)
    epsilon = max(min_epsilon, epsilon * epsilon_decay)
    rewards.append(total_rewards)

print("Training finished!\n")

# Evaluate performance
print(f"Average reward over {episodes} episodes: {np.mean(rewards):.2f}")

# Test the trained agent
state, _ = env.reset()
env.render()
done = False

print("\nTesting trained agent:")
while not done:
    action = np.argmax(Q[state, :])  # Always exploit
    new_state, reward, done, truncated, info = env.step(action)
    env.render()
    state = new_state

print("Test finished with reward:", reward)

