#!/usr/bin/env python

from functools import cache, lru_cache


def memoize(f):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    wrapper.__name__ = f.__name__
    return wrapper


@memoize
def fib_memoized(n):
    return 1 if n < 2 else fib_memoized(n - 1) + fib_memoized(n - 2)


@lru_cache(100)
def fib_lru_cache(n):
    return 1 if n < 2 else fib_lru_cache(n - 1) + fib_lru_cache(n - 2)


@cache
def fib_cache(n):
    return 1 if n < 2 else fib_cache(n - 1) + fib_cache(n - 2)


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


def execute(func, n_max, verbose=False):
    start = datetime.now()
    values = [func(n) for n in range(n_max)]
    delta = datetime.now() - start
    if verbose:
        for n in range(n_max):
            print('{0}({1}) = {2}'.format(func.__name__, n, values[n]))
    return float(delta.seconds) + 1.0e-6*float(delta.microseconds)


if __name__ == '__main__':
    from argparse import ArgumentParser
    from datetime import datetime

    arg_parser = ArgumentParser(description='compare memoized versus '
                                            'non-memooized')
    arg_parser.add_argument('n_max', type=int, help='maximum n value')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='display computed values')
    options = arg_parser.parse_args()
    for fib_impl in (fib, fib_memoized, fib_cache, fib_lru_cache):
        delta_time = execute(fib_impl, options.n_max, options.verbose)
        print(f'{fib_impl.__name__:20s}: {delta_time:.6f} s')