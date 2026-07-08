# penalty-shootout-rl

Research-grade multi-agent reinforcement learning project for a soccer penalty shootout.

## Step-by-step project setup

### Step 1 (current) - Repository and AI engineering foundations

- Repository governance and contribution flow are defined in `CONTRIBUTING.md`.
- Branch strategy and protection recommendations are in `docs/branching-strategy.md`.
- AI development process and reproducibility guardrails are in `docs/ai-development-playbook.md`.
- CI quality gates run linting, formatting, typing, and tests on PRs.

### Step 2 (next) - Environment and training implementation

- Start implementing Phase 1 training code only after Step 1 conventions are enforced.

### Step 1.5 (now) - Local AI-enabled development environment

- VS Code workspace settings and tasks are available in `.vscode/`.
- Recommended extensions are listed in `.vscode/extensions.json`.
- Local development environment best practices are documented in `docs/development-environment.md`.

## What is implemented now

- Production-ready project skeleton (Python 3.12+, src layout, CI, linting, typing).
- PettingZoo AEC environment baseline and unit tests.
- Governance-first workflow: branch strategy, contribution guide, templates, and CI.
- Automated branch policy checks for branch names and PR titles.
- RL configuration files were intentionally removed to proceed strictly step by step.

## Project structure

```text
src/penalty_shootout_rl/
  agents/
  policies/
  environment/
  training/
  evaluation/
  visualization/
  utils/
  config/

tests/
docs/
scripts/
```

## Quick start

1. Create a virtual environment and activate it.
1. Install dependencies:

```bash
pip install -e .[dev]
```

1. Run quality checks:

```bash
ruff check .
ruff format --check .
mypy src
pytest
```

1. Keep Step 2 implementation tasks disabled until you approve each one.

## Engineering standards

- Type hints across public functions and classes.
- Google-style docstrings.
- No global mutable state in training logic.
- Deterministic seeds for repeatable experiments.
- Explicit, modular separation between env, policy, training, and evaluation.

## Governance files

- `CONTRIBUTING.md`
- `.github/pull_request_template.md`
- `.github/CODEOWNERS`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/workflows/branch-policy.yml`

## Development environment files

- `.vscode/settings.json`
- `.vscode/extensions.json`
- `.vscode/tasks.json`
- `docs/development-environment.md`
