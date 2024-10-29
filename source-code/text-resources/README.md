# Text resources

It can be convenient to bundle text files in a package for convenient
distribution and access.


## What is it?

1. `show_text.py`: script that reads a text file from the package, and
   prints it to standard output.
1. `lib/utils': package with a text file.
1. `lib/utils/text_data.txt`: text file that contains some text.
1. `run_show_text.sh`: Bash script that runs the `show_text.py` script.  It
   sets the `PYTHONPATH` environment variable to include the `lib` directory to
   find the `utils` package.
