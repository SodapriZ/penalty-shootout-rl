# Project Integration Checklist From Unit 7

Use this checklist to convert Unit 7 understanding into implementation tasks.

## Environment

- [ ] Observation spaces are explicitly documented per agent.
- [ ] Action spaces are documented and unit-tested.
- [ ] Terminal and truncation rules are deterministic and tested.

## Rewards

- [ ] Reward logic lives outside learning agent code.
- [ ] Reward terms are documented with expected behavior.
- [ ] Reward-abuse failure cases are listed.

## Training

- [ ] First baseline algorithm selected with rationale.
- [ ] Reproducibility metadata logged for each run.
- [ ] Checkpointing and restore path validated.

## Evaluation

- [ ] Fixed opponent pool evaluation exists.
- [ ] Historical checkpoint evaluation exists.
- [ ] Regression criteria are defined.

## Experiment discipline

- [ ] One-variable-per-experiment rule followed.
- [ ] Experiment registry maintained.
- [ ] Conclusions written with evidence and limitations.

## Exit criteria before Phase 2 coding expansion

- [ ] Phase 0 charter approved.
- [ ] Phase 1 research notes completed.
- [ ] Baseline environment tests are green.
- [ ] Baseline training and evaluation loop runs end-to-end.
