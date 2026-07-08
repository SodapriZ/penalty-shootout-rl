# Unit 7 - Self-Play (Beginner Notes)

Source:

- [Unit 7 Self-Play](https://huggingface.co/learn/deep-rl-course/unit7/self-play)

## Core idea

Self-play means agents improve by training against versions of each other.

## Why it matters

In competitive MARL, static opponents can produce brittle policies.
Self-play helps agents adapt to stronger opponents over time.

## Key beginner concepts

- Current policy vs current policy can overfit.
- Historical opponent pools improve robustness.
- Evaluation should include fixed opponent sets.

## Project integration

- Keep opponent checkpoint pool.
- Sample opponents from different training stages.
- Track performance vs historical versions, not only latest model.

## Risk controls

- Detect mode collapse.
- Detect forgetting of earlier strategies.
- Track trend stability, not single-run peaks.

## Open questions to answer

1. How large should the opponent pool be initially?
2. How often should checkpoints enter the pool?
3. Which metrics detect regression early?
