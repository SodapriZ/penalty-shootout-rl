# Unit 7 - Hands-On (Beginner Notes)

Source:

- [Unit 7 Hands-On](https://huggingface.co/learn/deep-rl-course/unit7/hands-on)

## Core idea

Hands-on sections translate concepts into implementation workflow.

## Beginner execution sequence

1. Build minimal working environment.
2. Validate API and deterministic tests.
3. Train simple baseline with small runs.
4. Add evaluation protocol and logging.
5. Scale only after stability proof.

## What to log from day one

- Random seed
- Config snapshot
- Commit hash
- Training metrics per run
- Evaluation metrics against fixed opponents

## Common pitfalls in hands-on stage

- Running long training before validating environment transitions.
- No reproducibility metadata.
- No separation between train and eval settings.

## Open questions to answer

1. What is the smallest end-to-end training run we can trust?
2. What minimum metrics are required before scaling experiments?
3. Which failures should block progression to next phase?
