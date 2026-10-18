# Project name

One sentence on what this is and who it's for.

Part of [Ognjen Labs](https://github.com/ognjenlabs).

## Why

The problem, and why existing approaches fall short.

## Quickstart

```sh
uv sync
uv run pytest
```

## Results

Headline numbers, each with the command, config and seed that produced it.

## Hardware

Boards, sensors and wiring, if the project runs on a device. Delete this section for software-only projects.

## Repository layout

| Path | What it holds |
|---|---|
| `src/project_template/` | The package |
| `tests/` | Tests, run by CI |
| `docs/` | Notes, figures and the paper |

## Citation

Cite this work with the metadata in [`CITATION.cff`](CITATION.cff). GitHub shows it as a "Cite this repository" button.

## License

Code is licensed under [Apache-2.0](LICENSE). Papers, figures and documentation in `docs/` are licensed under [CC BY 4.0](LICENSE-docs).

## Using this template

After creating a repo from this template:

1. Rename the package: `src/project_template/` and the `name` in `pyproject.toml`.
2. Fill in `CITATION.cff` and the sections above.
3. If the project isn't Python, replace `.github/workflows/ci.yml` with the Rust or Node starter from **Actions > New workflow**. Keep the `ci-ok` job.
4. Delete this section.
