# Static analysis

Static analyzers such as pylint or flack8 help to improve the
quality of your code, both by detecting some potential bugs
as well as ensuring PEP 8 compliance.

## What is it?

* `pylint`: illustration of steps to improve some old code and
  make it PEP 8 compliant.
* `ruff`: illustration of steps to improve the same code based on
  feedback from `ruff`.

## Comparing pylint and ruff

For this particular example, the two tools overlap on several issues,
such as missing docstrings, outdated string formatting, useless
`object` inheritance, unnecessary `else` after `return`, and raising
the generic `Exception`.

Some issues are flagged by `ruff`, but not by `pylint` in the example:

* unsorted imports,
* missing type annotations,
* missing docstrings for magic methods such as `__enter__` and
  `__exit__`,
* explicit positional format fields such as `'{0}'`.

Some issues are flagged by `pylint`, but not by `ruff` in the example:

* access to protected members such as `_context_nr`,
* disallowed short names such as `foo` and `bar`,
* the lowercase constant name `status`,
* unreachable code after `raise Exception()`.

The comparison also illustrates that the outcome depends on the
selected rule set.  In this directory, the `ruff` example uses the
configuration in `ruff/ruff.toml`, while `pylint` applies its own
default logic and scoring.
