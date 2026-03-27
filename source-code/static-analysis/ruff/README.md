# ruff

`ruff` is a fast Python linter.  In this example, it is configured to
check for:

* missing type annotations,
* missing docstrings,
* import order issues,
* outdated Python idioms,
* unnecessary `else` after `return`,
* raising the overly generic `Exception`.

## What is it?

* `context_00.py`/`report_00.txt`: original code and corresponding
  `ruff` report.
* `context_01.py`/`report_01.txt`: result of `ruff check --fix`, i.e.,
  the visible safe fixes.
* `context_02.py`/`report_02.txt`: result of `ruff check --fix
  --unsafe-fixes`, i.e., the hidden fixes as well.
* `context_03.py`/`report_03.txt`: the remaining type hints have been
  added manually.
* `context_04.py`/`report_04.txt`: docstrings have been added.
* `context_05.py`/`report_05.txt`: a dedicated exception class is used,
  so the code passes all configured `ruff` checks.
* `ruff.toml`: `ruff` configuration used for this example sequence.

## Configuration

The `ruff.toml` file in this directory is the configuration used for
the example sequence.  It is also a practical baseline for scientific
Python projects.  It combines bug finding, style checks, modern Python
idioms, and documentation requirements without becoming needlessly
strict for tests or package initializers.

### Included rule families

* `ANN`: require type annotations for public functions and methods.
* `B`: catch likely bugs and risky constructs from `flake8-bugbear`.
* `C4`: suggest clearer comprehensions and collection literals.
* `D`: enforce the presence and structure of docstrings.
* `E`: report pycodestyle errors.
* `F`: report likely errors such as unused imports or undefined names.
* `I`: enforce import sorting and grouping.
* `N`: enforce PEP 8 naming conventions.
* `PIE`: check a collection of small code-quality issues.
* `PTH`: prefer `pathlib` over `os.path` style path handling.
* `RET`: simplify return statements and related control flow.
* `SIM`: suggest simpler equivalent code constructs.
* `UP`: encourage modern Python syntax and idioms.
* `W`: report pycodestyle warnings.

### Ignored rules

* `D203`: disabled because it conflicts with `D211`; Ruff cannot
  sensibly enforce both blank-line conventions at once.
* `D213`: disabled because it conflicts with `D212`; only one
  multi-line docstring summary style can be active.
* `D300`: disabled because it prefers triple double quotes for
  docstrings, while this repository prefers single-quoted docstrings.

### Additional settings

* `target-version = 'py312'`: assume Python 3.12 syntax and standard
  library features.
* `line-length = 79`: match the preferred maximum line width.
* `src = ['.']`: treat the repository root as source for import
  resolution.
* `convention = 'numpy'`: apply NumPy-style docstring conventions.
* `quote-style = 'single'`: prefer single quotes when formatting.

### Per-file exceptions

* `tests/**/*.py`: ignore `ANN` and `D` so tests can stay concise
  without requiring complete type annotations and docstrings.
* `**/__init__.py`: ignore `F401` so package re-exports are allowed
  without being flagged as unused imports.

## Note

The exception is raised on purpose to illustrate exception handling by
a context manager.
