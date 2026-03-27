# Typing

Python 3.5 introduced optional type annotation for functions, and that
functionality was extended in Python 3.6.

The `mypy` static type checker can use this annotation to detect type errors.

Type checking can be done using [mypy](http://mypy-lang.org/index.html).


## What is it?

1. `fibonacci_basics`: basic examples with a Fibonacci function and several
   type errors that `mypy` can detect.
1. `word_count`: dictionary-based word counting examples, including a sample
   input text.
1. `duck_typing_example`: examples illustrating plain duck typing and duck
   typing with `Protocol`.
1. `people_example`: example with a typed list of `Person` instances that
   contains multiple errors.
1. `class_typing`: examples illustrating type checking with a user-defined
   class.
1. `tree_typing`: example illustrating generic classes and recursive types.
1. `new_type_examples`: example illustrating the use of `NewType`.
1. `numpy_typing_example`: example illustrating typing for NumPy arrays and a
   small plotting workflow.

Each subdirectory contains the code for one example family together with a
local `mypy.ini` configuration file and a local `README.md`.  Run `mypy` from
within a subdirectory, for example:

```bash
cd fibonacci_basics
mypy *.py
```
