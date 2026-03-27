# People Example

This directory contains an example with a typed list of `Person` instances that
contains several mistakes.

Type checking can be done using [mypy](http://mypy-lang.org/index.html).


## What is it?

1. `people_incorrect.py`: code that defines a `Person` class, stores values in
   a typed list, and introduces several type errors.

Run the checker from this directory with:

```bash
mypy *.py
```
