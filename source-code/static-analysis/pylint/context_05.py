#!/usr/bin/env python

from contextlib import contextmanager
import sys


class ContextTest:

    _context_nr: int

    @property
    def context_nr(self):
        return self._context_nr

    @context_nr.setter
    def context_nr(self, value):
        self._context_nr = value

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
        print(f'no exception in context {self._context_nr}')


@contextmanager
def label(name):
    print(f'entering label({name})')
    yield name
    print(f'exiting label({name})')


def main():
    with ContextTest(1) as context_1, ContextTest(2) as context_2:
        print(f'in context {context_1.context_nr}')
        print(f'in context {context_2.context_nr}')
    with label('foo') as foo_label, label('bar') as bar_label:
        print(foo_label, bar_label)
    with ContextTest(1) as context_1, ContextTest(2) as context_2:
        print(f'in context {context_1.context_nr}')
        raise Exception()
        # print(f'in context {context_2.context_nr}')
    return 0


if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)
