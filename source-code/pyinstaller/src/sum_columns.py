#!/usr/bin/env python3

import argparse
import sys
from lib.funcs import sum_columns

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input CSV file')
    parser.add_argument('--version', action='store_true',
                        help='Print Python version and exit')
    args = parser.parse_args()
    if args.version:
        print(sys.version)
        sys.exit(0)
    sum_columns(args.input_file)


if __name__ == '__main__':
    main()
