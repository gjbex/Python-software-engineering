# Word Count

This directory contains dictionary-based examples for counting words in a text
stream.

Type checking can be done using [mypy](http://mypy-lang.org/index.html).


## What is it?

1. `dict_correct.py`: code that counts the words in a text read from standard
   input.
1. `dict_incorrect_01.py`: code that counts the words in a text read from
   standard input and then normalizes the counts to `float`, which introduces a
   type error.
1. `dict_correct_type_statement.py`: same code as `dict_correct.py`, but with a
   type alias statement for the count dictionary.
1. `data/text.txt`: sample input text for the scripts in this directory.

Run the checker from this directory with:

```bash
mypy *.py
```

Run a script with the sample data using:

```bash
python dict_correct.py < data/text.txt
```
