# Architecture

## Design goals

- Keep environment dynamics independent from learning algorithms.
- Keep reward logic in environment and explicit reward modules, never in agents.
- Ensure deterministic and reproducible experimentation.
- Make it easy to swap algorithms and policy architectures.

## Core modules

- `environment`: PettingZoo AEC environment and physics abstractions.
- `agents`: role-level wrappers and decision interfaces.
- `policies`: neural policy/value models and distributions.
- `training`: self-play loops, checkpoint pools, optimization orchestration.
- `evaluation`: Elo, cross-play, robustness, and analytics.
- `visualization`: 2D replay and plotting utilities.
- `config`: typed config objects and schema validation.
- `utils`: logging, seeding, persistence helpers.

## Dependency direction

- `training` depends on `environment`, `policies`, `evaluation`, `utils`, `config`.
- `environment` depends only on `config` and low-level libs.
- `agents` and `policies` do not import from `training`.
- `evaluation` must not mutate training state.

## Testing strategy

- Unit tests for transition and reward invariants.
- API compliance tests for PettingZoo contract.
- Deterministic random-policy sanity tests.
- Regression tests for key metrics once training loops are added.
