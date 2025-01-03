#!/usr/bin/env bash

# create a virtual environment and install the dependencies
python -m venv build_venv
source build_venv/bin/activate
pip install -r requirements.txt

# build the apps
pyinstaller \
   --onefile \
   --hidden-import funcs \
   --collect-submodules funcs \
   src/sum_columns.py
pyinstaller \
   --onefile \
   --add-data data.csv:. \
   --hidden-import funcs \
   --collect-submodules funcs \
   src/prod_columns.py
