# Research Approach For MARL Understanding

This document defines the method to study Unit 7 and transform it into project knowledge.

## Why this approach

MARL documentation is rich but easy to read passively. This method forces active extraction and decision-making.

## The 5-step loop

1. Read

- Read one section and rewrite it in your own words.

1. Extract

- Identify concepts, assumptions, and constraints.

1. Map

- Map each concept to project components:
  - environment
  - rewards
  - training loop
  - evaluation protocol

1. Decide

- Make an explicit design decision with rationale.

1. Validate

- Add a test, metric, or experiment that validates the decision.

## Decision quality rules

- Prefer simple baselines first.
- Keep reward logic independent from learning algorithm code.
- Define evaluation protocol before training large runs.
- Do not change multiple variables in one experiment.

## Evidence template for each concept

- Concept:
- Why it matters:
- Project impact:
- Decision:
- Validation signal:

## Common mistakes to avoid

- Starting with complex algorithms before stable baseline.
- Mixing environment bugs with training instability.
- Using only latest-policy evaluation.
- Ignoring reproducibility controls (seed, config snapshot, commit hash).
