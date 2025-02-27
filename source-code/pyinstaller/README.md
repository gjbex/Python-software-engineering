# PyInstaller

PyInstaller bundles a Python application and all its dependencies into a single
package. The user can run the packaged app without installing a Python
interpreter or any modules.  It is very useful to minimize dependencies.


## What is it?

1. `src`: directory with a Python scripts that use the pandas library and that
   requires access to a CSV file.  Note that the Python scripts dynamically
   load a module `funcs` that is not in the same directory as the script.
1. `data.csv`: CSV file that is used by the Python script in `src`.
1. `requirements.txt`: file listing the Python packages that are required by
   the Python script in `src`.
1. `build_apps.sh`: Bash script that creates a virtual environment, installs
   the required packages, and creates a standalone application using
   PyInstaller.
1. `CMakeLists.txt`: CMake file to build and install the applications.


## How to create the applications?

## By  hand

1. Create a virtual environment and install the required packages:
   ```bash
   $ python -m venv build_venv
   $ source build_venv/bin/activate
   (venv)$ pip install -r requirements.txt
   ```
1. Create the application:
   ```bash
   (venv)$ pyinstaller \
             --onefile \
             --hidden-import funcs \
             --collect-submodules funcs \
             src/sum_columns.py
   (venv)$ pyinstaller \
             --onefile \
             --add-data data.csv:. \
             --hidden-import funcs \
             --collect-submodules funcs \
             src/prod_columns.py
   ```


## Using CMake

```bash
$ cmake -B build -S .
$ cmake --build build
```
