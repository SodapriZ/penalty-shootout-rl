# Branching Strategy

## Recommended model

Use a trunk-based approach with short-lived feature branches.

- `main` is always releasable.
- Feature branches live for a few days, not weeks.
- Rebase frequently on `main` to reduce merge conflicts.

## Branch taxonomy (AI/RL focused)

Use these branch families:

- `feat/<scope>-<short-description>` for product or algorithm features.
- `fix/<scope>-<short-description>` for bug fixes.
- `refactor/<scope>-<short-description>` for architectural cleanup.
- `test/<scope>-<short-description>` for test improvements.
- `docs/<scope>-<short-description>` for documentation work.
- `chore/<scope>-<short-description>` for maintenance.
- `exp/<topic>-<short-description>` for short-lived research experiments.
- `release/<major.minor>` for release hardening.
- `hotfix/<major.minor.patch>-<short-description>` for urgent production fixes.

Scope examples:

- `env`, `agent`, `policy`, `training`, `eval`, `viz`, `infra`, `ci`.

Naming examples:

- `feat/training-self-play-loop`
- `exp/policy-entropy-annealing`
- `fix/env-terminal-state-bug`
- `release/0.2`

## Branch protection settings (GitHub)

Configure these protections for `main`:

1. Require pull request before merging.
2. Require at least 1 approval.
3. Dismiss stale approvals on new commits.
4. Require status checks to pass:
    - `CI / test`
    - `Branch Policy / branch-and-pr-policy`
5. Require branches to be up to date before merging.
6. Restrict force pushes and deletion.

Additional protections:

1. Require conversation resolution before merge.
2. Restrict who can push directly to `main`.
3. Enforce linear history.
4. Require signed commits if your org policy mandates it.

## Rules for experiment branches

- `exp/*` branches are for fast hypotheses and should be short-lived.
- Merge `exp/*` only if outcomes are reproducible and documented.
- Keep raw artifacts (models, logs, datasets) out of git; store externally.
- If experiment fails, close with a short note in PR to preserve learnings.

## Merge policy

- `feat/*`, `fix/*`, `refactor/*`, `test/*`, `docs/*`, `chore/*`:
  - Merge to `main` through PR with squash merge.
- `exp/*`:
  - Prefer PR into `main` only for validated and cleaned results.
  - Otherwise close PR and keep findings documented.
- `hotfix/*`:
  - Merge to `main`, then back-port to active `release/*` if needed.

## Merge strategy

- Prefer **Squash and merge** for a clean linear history.
- PR title should follow Conventional Commits.
- Include issue link and experiment impact in PR description.

## Release tagging

- Tag stable milestones as `vX.Y.Z`.
- For research checkpoints, use annotated tags like `exp-phase1-baseline`.

## Pull request minimums for AI development

- Include reproducibility notes: seed, settings, and evaluation protocol.
- Include risk notes for reward changes and environment transition logic.
- Include metric impact summary for goal/save rates and robustness checks.
