# Warnings

Python supports warnings and errors at runtime.  This can provide
a useful error handling mechanism for your code.  You can use the
`warnings` module to issue warnings and errors.


## What is it?

1. `will_warn.py`: script that issues a DeprecationWarning, intended
   to illustrate how to suppress it at runtime.


## How to use it?

You can suppress the warning from the command line in two ways:
  * using the `-W` option to the Python interpreter, and
  * setting the `PYTHONWARNINGS` environment variable.

```bash
$ python -Wi::DeprecationWarning will_warn.py
```

```bash
$ export PYTHONWARNINGS="ignore::DeprecationWarning"
$ python will_warn.py
```
