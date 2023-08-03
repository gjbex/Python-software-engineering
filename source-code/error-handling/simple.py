#!/usr/bin/env python

import sys

ARG_ERROR = 1
FILE_ERROR = 2
DATA_ERROR = 3

def sum_numbers(file):
    return sum(float(line) for line in file)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('### error: no argument given', file=sys.stderr)
        sys.exit(ARG_ERROR)
    file_name = sys.argv[1]
    try:
        file = open(file_name, 'r')
        print(sum_numbers(file))
    except IOError as e:
        print(f'### IO Error on {e.filename}: {e.strerror}')
        sys.exit(FILE_ERROR)
    except ValueError:
        print(f'### Data Error on {file_name}: should contain only numbers')
        sys.exit(DATA_ERROR)
