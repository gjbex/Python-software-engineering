Decorators
==========

Python supports decorators, i.e., function wrapping to add functionality
before and/or after the function's invocation.  Python comes with a number
of standard decorators, but it is easy to define one's own.

What is it?
-----------
1. `decorators.py`: two decorators are defined to check a wrapped
    function's arguments.  The first, `check_min` throws an exception
    when the argument is negative, the second, `check_max`, throws another
    exception when the function is called with an argument that is too
    large.  The decorated function in this example is the factorial.
    Also it illustrates `functools` wrap decorator to retain the wrapped
    function's name, docstring, etc.
1. `decorator_arguments.py`: an example of a decorator that takes arguments.
   The `check_range` decorator takes a minimum and maximum value as arguments
   and checks if the wrapped function's argument falls within that range,
   throwing an exception if it does not.
1. `memoize.py`: an example of adding a cache to a function using a simple
    custom decorator, as well as `functools`'s `lru_cache` decorator.
