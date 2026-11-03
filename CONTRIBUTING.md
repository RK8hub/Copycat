# Contributing

Thanks for taking the time to improve Copycat. This project is small, so the process is simple.

## Getting started

1. Fork the repository and clone your fork.
2. Create a virtual environment and install the project with the development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

3. Create a branch for your change:

```bash
git checkout -b fix/short-description
```

## Running the tests

```bash
python -m pytest
```

Add a test for any new behavior or bug fix. Tests live in `tests/` and use pytest with `monkeypatch`, so they never touch the real clipboard.

## Code style

- Follow the structure and naming already in the codebase. Identifiers are in Spanish (for example `copiarContenido`); keep them that way for consistency.
- Keep changes focused. A pull request should solve one problem.
- Do not add dependencies unless they are strictly necessary. If you do, explain why in the pull request.
- User-facing messages are in Spanish and error cases must be handled, not left as tracebacks.

## Submitting a change

1. Commit your change with a clear message.
2. Push the branch to your fork.
3. Open a pull request describing what changed and why.

## Reporting a bug

Open an issue and include:

- What you ran and what you expected to happen.
- What actually happened, including the full error output.
- Your operating system and Python version (`python -V`).

## License

By contributing, you agree that your contributions are licensed under the MIT License.
