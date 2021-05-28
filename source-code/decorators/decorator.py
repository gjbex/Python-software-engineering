#!/usr/bin/env python

from functools import wraps


class NegArgError(Exception):
    def __init__(self, name, n):
        super().__init__()
        self.message = 'argument {0} for {1} negative'.format(n, name)


class TooLargeArgError(Exception):
    def __init__(self, name, n):
        super().__init__()
        self.message = 'argument {0} for {1} too large'.format(n, name)


def check_min(f):
    @wraps(f)
    def wrapped(n):
        if n < 0:
            raise NegArgError(f.__name__, n)
        return f(n)
    return wrapped


def check_max(f):
    @wraps(f)
    def wrapped(n):
        if n > 12:
            raise TooLargeArgError(f.__name__, n)
        return f(n)
    return wrapped


@check_max
@check_min
def fact(n):
    '''compute factorial of given number'''
    if n == 0:
        return 1
    else:
        return n*fact(n - 1)

if __name__ == '__main__':
    import sys
    for n in [3, 7, 22, -1]:
        try:
            print(f'{n}! = {fact(n)}')
        except Exception as error:
            print(f'### error: {error.message}', file=sys.stderr)
    print(f'function name: {fact.__name__}')
    print(f'function docs: {fact.__doc__}')
