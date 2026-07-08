# Development Environment

## Recommended setup for this project

This project should be developed with a local Python virtual environment and GitHub Copilot in VS Code.

Use the local environment for execution, testing, and reproducibility.
Use Copilot for code generation, review support, refactoring suggestions, and commit preparation.

## Copilot CLI vs local setup

Use local setup as the default.

Why local-first:

- Training loops, simulations, and tests require direct access to local resources and virtual environments.
- Tooling consistency is easier to enforce (Ruff, mypy, pytest, pre-commit).
- Reproducibility is better when everything runs from the same pinned environment.

Use Copilot CLI as an optional helper for quick one-off actions only, such as:

- Drafting shell commands.
- Summarizing git diffs.
- Generating short scripts for manual review.

Do not make Copilot CLI your primary orchestration layer for this repository.

## Daily workflow

1. Activate local virtual environment.
2. Install/update dependencies with the VS Code task `dev: install`.
3. Implement changes on a short-lived branch.
4. Run `quality: all` before pushing.
5. Open a pull request and use Squash and merge.

## VS Code task shortcuts

The workspace ships with these tasks:

- `dev: install`
- `quality: ruff check`
- `quality: ruff format check`
- `quality: mypy`
- `quality: pytest`
- `quality: all`

## Best practices for AI-assisted coding

- Keep prompts task-specific and bounded to one change at a time.
- Ask AI to generate tests together with implementation.
- Require explicit type hints and Google-style docstrings for public APIs.
- Prefer small PRs with clear intent and reproducible verification steps.
- Never accept generated code without running lint, type-check, and tests.

## Project custom agent in VS Code

This repository now includes a dedicated custom agent:

- `.github/agents/marl-penalty-architect.agent.md`

How to use it:

1. Open Copilot Chat in VS Code.
2. Open the agent picker.
3. Select `MARL Penalty Architect`.
4. Prompt with a concrete task and expected validation, for example:
   - "Refactor the environment step logic and add deterministic tests."
   - "Add an evaluation helper with typed interfaces and pytest coverage."

Best-practice usage pattern:

- Use default Copilot for quick edits and ideation.
- Switch to `MARL Penalty Architect` for architecture decisions, RL-heavy changes, and quality-gated refactors.
- Keep this agent project-scoped in `.github/agents/` so all contributors share the same behavior.

## Reproducibility controls

- Always run commands from `.venv`.
- Record random seeds for experiments.
- Keep training and evaluation scripts deterministic where possible.
- Store experiment metadata and configuration snapshots with checkpoints.
