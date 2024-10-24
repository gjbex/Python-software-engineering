# PyInstaller

PyInstaller bundles a Python application and all its dependencies into a single
package. The user can run the packaged app without installing a Python
interpreter or any modules.  It is very useful to minimize dependencies.


## What is it?

1. `src`: directory with a Python scripts that use the pandas library and that
   requires access to a CSV file.
1. `data.csv`: CSV file that is used by the Python script in `src`.
1. `requirements.txt`: file listing the Python packages that are required by
   the Python script in `src`.


## How to create the applications?

1. Create a virtual environment and install the required packages:
   ```bash
   $ python -m venv build_venv
   $ source build_venv/bin/activate
   (venv)$ pip install -r requirements.txt
   ```
1. Create the application:
   ```bash
   $ pyinstaller \
         --onefile \
         --hidden-import funcs \
         --collect-submodules funcs \
         src/sum_columns.py
   $ pyinstaller \
         --onefile \
         --add-data data.csv:data.csv \
         --hidden-import funcs \
         --collect-submodules funcs \
         src/sum_columns.py
   ```
