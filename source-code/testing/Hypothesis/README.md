# Hypothesis

Examples of using `hypothesis`, a testing library that
uses fuzzing to find issues in your code.


## What is it?

1. `factorial.py`: implementatino of the factorial
   function.
1. `test_factorial.py`: hypothesis tests of the factorial
   function
1. `points.py`: example of finding a bug with fuzz testing.


## How to use it?

Run with pytest:
```bash
$ pytest --hypothesis-show-statistics
```
