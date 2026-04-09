Quality of software matters, whether you share it with others or not.
Software should be easy to install, easy to use, and well documented.
This training will cover those aspects from the perspective of the
Python ecosystem.  However, it is also important that software is easy
to maintain, so coding style matters, API-level documentation should be
available, as well as a battery of tests to ensure the software's
integrity.  Of course, good design is at least as important.


## Learning outcomes

When you complete this training you will

  * know some best practices for writing quality code;
  * catch errors at development time by using type annotations in your
    code;
  * know how to handle errors;
  * know how to systematically test your code;
  * know how to document your code;
  * be able to use objected-oriented programming to improve
    the reuse of your code;
  * be able to use functional programming concepts to improve
    your coding style;
  * aware that you can use design patterns to avoid reinventing
    the wheel.


## Schedule

Total duration: 4 hours.

  | Subject                                     | Duration |
  |---------------------------------------------|----------|
  | introduction and motivation                 |  5 min.  |
  | coding best practices                       | 15 min.  |
  | exception handling                          | 10 min.  |
  | type hints                                  | 10 min.  |
  | documenting code                            | 10 min.  |
  | unit testing                                | 50 min.  |
  | coffee break                                | 10 min.  |
  | object-oriented programming                 | 80 min.  |
  | functional programming                      | 20 min.  |
  | design patterns discussion                  | 20 min.  |
  | wrap up                                     | 10 min.  |


## Training materials

Slides are available in the
 [GitHub repository](https://github.com/gjbex/Python-software-engineering),
as well as example code and hands-on material.


## Target audience

This training is for you if you want robust software that is easy
to understand and maintain.


## Prerequisites

You will need experience programming in Python.  This is not a training that starts
from scratch.

If you plan to do Python programming in a Linux or HPC environment you should
be familiar with these as well.

More concretely, participants should already be comfortable with the following:

* running Python code in Jupyter or from the command line;
* variables, numbers, strings, booleans, and basic containers such as lists,
  tuples, sets, and dictionaries;
* `if`/`else` statements, `for` loops, and simple comprehensions;
* writing and calling functions with arguments and return values;
* importing modules and using functions, classes, and constants from them;
* reading and writing small text files using `open(...)`;
* basic exception handling with `try`/`except`;
* defining and using simple classes with methods and instance attributes;
* reading short Python scripts without needing every line explained.

You do not need prior experience with type hints, `mypy`, `pytest`,
`unittest`, decorators, context managers, descriptors, coroutines,
metaclasses, `pydantic`, or design patterns. Those are part of the training
itself.

### Quick self-assessment

If you can do most of the tasks below without looking up basic Python syntax,
you are likely ready for this training.

* write a function that reads numbers from a file and returns their sum;
* use `try`/`except` to handle a missing input file or invalid value;
* define a simple class such as `Book` or `Person` with an `__init__` method
  and one extra method;
* import a module such as `pathlib`, `itertools`, or `collections` and use one
  of its basic features;
* read a short script that contains several functions and understand how data
  flows between them;
* explain what a list comprehension does and rewrite it as a regular loop;
* make a small change to an existing script, run it again, and interpret the
  result;
* read a short traceback and identify roughly where an error occurred.

If several of these items still feel difficult, the training will probably move
too fast. In that case, it is better to first take a short introductory Python
course or refresh the basics.

For following along hands-on, you need
* laptop or desktop with internet access.
* a Python environment that can run Jupyter Lab if you want to use your own system;
* access to Google Colaboratory if you prefer not to install software.


## Level of the Material

For participants who already have basic Python programming experience, the material in this training is approximately

* Introductory: 20 %
* Intermediate: 40 %
* Advanced: 40 %

These percentages describe the level of the software engineering and Python
language concepts covered in the training, not the required entry level in
Python itself.


## Trainer(s)

  * Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be))
