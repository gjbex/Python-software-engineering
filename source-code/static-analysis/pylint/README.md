# pylint

pylint is a static analyzer that helps you improve your code by
detecting potential bugs and style issues.  It rates the source code
on a scale from 0 to 10.

# What is it?

* `context_00.py`/`report_00.txt`: original code and corresponding
  report.
* `context_01.py`/`report_01.txt`: the string formatting using the
  `format` method has been replaced by f-strings.
* `context_02.py`/`report_02.txt`: Python 2-style `object` base class
  eliminated, and superfluous `else` removed.
* `context_03.py`/`report_03.txt`: Python 2-style `object` base class
  eliminated, and superfluous `else` removed.
* `context_04.py`/`report_04.txt`: fix variable names.
* `context_05.py`/`report_05.txt`: remove unreachalbe statement.
* `context_06.py`/`report_06.txt`: add docstrings.

## Note

The exception is raised on purpose to illustrate exception handling by
a context manager.
