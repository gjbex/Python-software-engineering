# Fibonacci Basics

This directory contains a small family of examples around a typed Fibonacci
function.

Type checking can be done using [mypy](http://mypy-lang.org/index.html).


## What is it?

1. `correct.py`: code that has type annotations and no type errors.
1. `incorrect_01.py`: code that has type annotations and passes a string to a
   function that expects an `int`.
1. `incorrect_02.py`: code that has type annotations and assigns the result of
   an expression of type `int` to a variable of type `str`.
1. `incorrect_03.py`: code that has type annotations and uses an `int` value
   as though it were a `str`.

Run the checker from this directory with:

```bash
mypy *.py
```
