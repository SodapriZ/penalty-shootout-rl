# Unit 7 - Introduction To MARL (Beginner Notes)

Source:

- [Unit 7 Introduction To MARL](https://huggingface.co/learn/deep-rl-course/unit7/introduction-to-marl)

## Core idea

MARL requires reasoning about interactions between learners, not just one policy vs static environment.

## Key beginner concepts

- Cooperative settings: shared objective.
- Competitive settings: opposing objectives.
- Mixed settings: partial cooperation and competition.

## Important challenge: non-stationarity

When all agents update, the environment seen by one agent changes over time.

Project consequence:

- Instability can come from policy interaction, not code bugs.

## Practical algorithm guidance

- Start with a simpler baseline (IPPO) to debug the pipeline.
- Move to stronger methods (like MAPPO) after baseline stability.

## Open questions to answer

1. What is our baseline algorithm and why?
2. What training signal proves baseline stability?
3. When do we decide to upgrade algorithm complexity?
