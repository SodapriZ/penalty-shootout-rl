# Unit 7 - Introduction (Beginner Notes)

Source:

- [Unit 7 Introduction](https://huggingface.co/learn/deep-rl-course/unit7/introduction)

## Core idea

Multi-Agent Reinforcement Learning (MARL) extends RL from one learner to multiple interacting learners.

## Key beginner concepts

- Agents can cooperate, compete, or both.
- Other agents are part of the environment dynamics.
- Learning becomes less stable because all policies can change together.

## Why it matters for this project

Penalty shootout is naturally two-agent competitive MARL:

- kicker policy
- goalkeeper policy

## Practical implications

- We need separate observation and action spaces per agent.
- We need explicit episode termination rules.
- We need robust evaluation, not only training reward.

## Open questions to answer

1. Which information should each agent observe at each step?
2. Which signals should be hidden to avoid leakage?
3. What is the minimum environment complexity for first stable learning?
