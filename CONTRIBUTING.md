# Contributing Guide

## Development flow

1. Create a branch from `main`.
2. Keep PRs focused and small.
3. Open a PR early as draft.
4. Merge only when CI is green and review checklist is satisfied.

## Branch naming

Use one of these prefixes:

- `feat/<scope>-<short-description>`
- `fix/<scope>-<short-description>`
- `refactor/<scope>-<short-description>`
- `test/<scope>-<short-description>`
- `docs/<scope>-<short-description>`
- `chore/<scope>-<short-description>`
- `exp/<topic>-<short-description>`
- `release/<major.minor>`
- `hotfix/<major.minor.patch>-<short-description>`

Examples:

- `feat/training-self-play-loop`
- `fix/env-reward-sign-inversion`
- `exp/policy-entropy-annealing`

Scope values should be one of:

- `env`, `agent`, `policy`, `training`, `eval`, `viz`, `infra`, `ci`, `docs`

## Commit style

Use Conventional Commits:

- `feat: add checkpoint pool sampler`
- `fix: correct save probability for adjacent zones`
- `refactor: split env reward logic from transition logic`
- `test: add deterministic reward invariants`

## Local quality gates

Run before every PR:

```bash
ruff check .
ruff format --check .
mypy src
pytest
```

## RL and experiment hygiene

- Keep deterministic seeds in a versioned run manifest.
- Do not hardcode hyperparameters in Python modules.
- Save the full run settings with each experiment.
- Keep training and evaluation seeds separate.
- Never mix environment and algorithm responsibilities.
- Merge `exp/*` branches only when results are reproducible and documented.
- Never commit large model binaries or run artifacts to git.

## PR checklist

- [ ] Scope is small and focused
- [ ] Tests added or updated
- [ ] No breaking API changes without documentation
- [ ] Config changes documented in PR description
- [ ] Reproducibility impact described (seed/config/checkpoints)
