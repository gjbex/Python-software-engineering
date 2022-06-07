#!/usr/bin/env python

from contextlib import contextmanager
import sys


class ContextTest(object):

    def __init__(self, context_nr):
        self._context_nr = context_nr
        print(f'created with {self._context_nr}')

    def __enter__(self):
        print(f'entering {self._context_nr}')
        return self

    def __exit__(self, exception_type, exception_value, backtrace):
        print(f'exiting {self._context_nr}')
        if exception_type:
            print(f'exception in context {self._context_nr}:')
            print('\t', exception_type, exception_value, backtrace)
            return
        else:
            print(f'no exception in context {self._context_nr}')


@contextmanager
def label(name):
    print(f'entering label({name})')
    yield name
    print(f'exiting label({name})')


def main():
    with ContextTest(1) as c1, ContextTest(2) as c2:
        print(f'in context {c1._context_nr}')
        print(f'in context {c2._context_nr}')
    with label('foo') as foo, label('bar') as bar:
        print(foo, bar)
    with ContextTest(1) as c1, ContextTest(2) as c2:
        print(f'in context {c1._context_nr}')
        raise Exception()
        print(f'in context {c2._context_nr}')
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
