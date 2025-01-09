# Markers

pytest supports custom markers that can be used to select or deselect tests.


## What is it?

1. `fibonacci.py`: Python script that defines a function to compute the
   Fibonacci sequence in a (very) naive way.
1. `test_fibonacci.py`: test script that uses pytest to test the
   implementation of the Fibonacci sequence computation.  One of the tests has been marked with the `slow` marker.
1. `pytest.ini`: configuration file for pytest that defines the markers that
   can be used in the test scripts.


## How to use it?

To run all tests:
```bash
$ pytest
```

To run all tests except the `slow` test:
```bash
$ pytest -m "not slow"
```
