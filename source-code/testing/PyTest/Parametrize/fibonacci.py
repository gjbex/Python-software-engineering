#!/usr/bin/env python

def fib(n):
    if n < 0:
        raise ValueError('fac argument must be positive')
    elif n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(description='compute fibonacci numbers')
    arg_parser.add_argument('n', type=int, default=5,
                            help='maximum argument')
    options = arg_parser.parse_args()
    for i in range(options.n + 1):
        print(f'fib({i}) = {fib(i)}')
