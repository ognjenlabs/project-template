# CLAUDE.md

Conventions for agents working in this repository. The org-wide rules are in
https://github.com/ognjenlabs/.github/blob/main/CONTRIBUTING.md.

## Commands

- Install: `uv sync`
- Format: `uv run ruff format .`
- Lint: `uv run ruff check .`
- Test: `uv run pytest`

CI (`.github/workflows/ci.yml`) runs the same checks through the org's shared
workflow. `ci-ok` is the only required check.

## Workflow

- Branch from `main` as `feat/`, `fix/`, `chore/`, `docs/` or `exp/`, and land changes as a pull request, squash-merged.
- Commit subjects are plain imperative sentences. No attribution trailers.
- Never commit secrets, data dumps or model weights. Link to where they live.
- Every reported result names the command, config and seed that produced it.
