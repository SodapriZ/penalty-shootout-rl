# Unit 7 - Multi-Agent Setting (Beginner Notes)

Source:

- [Unit 7 Multi-Agent Setting](https://huggingface.co/learn/deep-rl-course/unit7/multi-agent-setting)

## Core idea

The environment contract in MARL must define per-agent interfaces clearly:

- observation
- action
- reward
- done or truncation

## Key beginner concepts

- Each agent has its own policy perspective.
- Global state may exist for training, but not necessarily for execution.
- Credit assignment is harder than single-agent RL.

## Design implications for penalty shootout

- Kicker actions: direction and shot profile.
- Goalkeeper actions: dive and timing.
- Rewards should reflect tactical quality, not only binary goal or save.

## Validation implications

- Unit tests for action validity and boundary conditions.
- Deterministic transitions under fixed seeds.
- Contract tests for episode completion and reset behavior.

## Open questions to answer

1. Which state variables are mandatory per agent?
2. Do we need discrete or continuous action spaces first?
3. Which reward components are dense enough for learning but safe from hacking?
