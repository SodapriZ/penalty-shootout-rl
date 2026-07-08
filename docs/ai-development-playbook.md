# AI Development Playbook

## Objectives

- Reliable experiments.
- Reproducible runs.
- Clear separation of concerns between environment and learning code.

## Non-negotiable practices

- Keep all run-time controls explicit and versioned.
- Log experiment metadata and full run settings per run.
- Track random seeds for train and eval.
- Keep an immutable checkpoint naming scheme.
- Evaluate against fixed opponent pools in addition to latest policy.

## Config best practices

- Keep defaults minimal and explicit.
- Separate settings by concern: `env`, `algorithm`, `training`, `evaluation`, `logging`.
- Use command-line overrides for exploratory runs.
- Create a named config file per published experiment.

## Reproducibility requirements

- Record commit hash, python version, package versions, and seed.
- Store model checkpoints with config snapshot.
- Avoid hidden mutable global state.

## Experiment review checklist

- Is the environment deterministic under fixed seed?
- Are reward definitions documented and tested?
- Are train and eval metrics separated?
- Is evaluation done against historical opponents?
- Did the run include enough episodes to support claims?
