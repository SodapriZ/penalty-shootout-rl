# Project Initialization ToDo

This checklist is the step-by-step path to start the MARL penalty shootout project with clear intent and validation at each stage.

## Phase 0 - Scope and Success Criteria

- [ ] Define the exact problem statement.
  - Why: keeps implementation focused and prevents feature drift.
- [ ] Define measurable success criteria.
  - Example: average goal prevention, agent win rate, learning stability, and reproducibility under fixed seeds.
- [ ] Define constraints.
  - Example: max training time per run, hardware limits, and framework choices.
- [ ] Write a one-page project charter in docs.
  - Include goals, non-goals, assumptions, and milestones.

## Phase 1 - Subject Research and Design Inputs

- [ ] Collect domain rules for penalty shootout dynamics.
  - Include shot directions, goalkeeper movement constraints, and episode termination.
- [ ] Review MARL references for small competitive games.
  - Focus: IPPO, MAPPO, self-play, and curriculum strategies.
- [ ] Build a short decision log.
  - Why: documents why a method is chosen, not just what is chosen.

## Phase 2 - Modeling Decisions

- [ ] Define observation space for each agent.
  - Example: kicker and goalkeeper state vectors.
- [ ] Define action spaces.
  - Kicker: shot direction and power.
  - Goalkeeper: dive direction and timing.
- [ ] Define reward design as a standalone module.
  - Keep reward logic out of learning agent implementation.
- [ ] Define termination and truncation conditions.
  - Match Gymnasium and PettingZoo contracts.
- [ ] Define evaluation metrics before training.
  - Example: expected return, save rate, policy entropy, and exploitability trend.

## Phase 3 - Environment Baseline

- [ ] Implement deterministic environment transitions.
- [ ] Add seed control and deterministic test cases.
- [ ] Add environment unit tests for edge cases.
  - Invalid actions, boundary conditions, terminal transitions.
- [ ] Add a random-policy smoke test.
  - Why: validates API and rollout stability before training.

## Phase 4 - Training Baseline (Smallest Working Loop)

- [ ] Implement first baseline trainer (start with IPPO).
  - Why: lower complexity, easier debugging.
- [ ] Add experiment configuration schema.
  - Include env, train, eval, and logging sections.
- [ ] Add periodic checkpointing.
- [ ] Add deterministic evaluation pipeline with fixed seeds.
- [ ] Add run metadata logging.
  - Commit hash, package versions, random seeds, and config snapshot.

## Phase 5 - Evaluation and Diagnostics

- [ ] Define fixed opponent pools for robust evaluation.
- [ ] Add historical checkpoint evaluation.
- [ ] Add plots for reward curves and stability indicators.
- [ ] Add failure-case review template.
  - Capture mode collapse, non-stationarity, and reward hacking symptoms.

## Phase 6 - Iteration Plan

- [ ] Introduce MAPPO only after IPPO baseline is stable.
- [ ] Compare algorithms using the same evaluation protocol.
- [ ] Prioritize one variable change per experiment.
  - Why: improves causality in analysis.
- [ ] Maintain an experiment registry.
  - Run id, hypothesis, change, result, decision.

## Phase 7 - Engineering and Delivery Readiness

- [ ] Keep CI green with ruff, mypy, and pytest.
- [ ] Enforce branch and PR naming policies.
- [ ] Require passing quality checks before PR merge.
- [ ] Use squash merge to keep history clean.

## Immediate Next 3 Actions

- [ ] Write the project charter in docs.
- [ ] Finalize observation and action space definitions.
- [ ] Implement or validate deterministic environment tests.
