#!/usr/bin/env python3

import argparse
import pathlib
import sys
from lib.funcs import prod_columns

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?',
                        help='Input CSV file')
    parser.add_argument('--version', action='store_true',
                        help='Print Python version and exit')
    args = parser.parse_args()
    if args.version:
        print(sys.version)
        sys.exit(0)
    if args.input_file is None:
        data_dir = pathlib.Path(__file__).parent
        prod_columns(data_dir / 'data.csv')
    else:
        prod_columns(args.input_file)


if __name__ == '__main__':
    main()
