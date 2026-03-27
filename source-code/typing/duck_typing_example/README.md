# Duck Typing

This directory contains examples illustrating both plain duck typing and duck
typing with `Protocol`.

Type checking can be done using [mypy](http://mypy-lang.org/index.html).


## What is it?

1. `duck_typing.py`: example code illustrating duck typing.
1. `duck_typing_incorrect.py`: example code illustrating duck typing with an
   interface mismatch that only shows up at runtime.
1. `typed_duck_typing.py`: example code illustrating duck typing using type
   hints and a `Protocol`.
1. `typed_duck_typing_clean.py`: example code illustrating duck typing using
   type hints with a factory function.
1. `typed_duck_typing_incorrect.py`: example code illustrating duck typing
   using type hints with an error that `mypy` can detect.

Run the checker from this directory with:

```bash
mypy *.py
```
