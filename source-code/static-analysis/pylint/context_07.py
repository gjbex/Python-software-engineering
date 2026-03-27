#!/usr/bin/env python
'''Illustrate two ways to implement a context manager.

The example shows:

* a class-based context manager,
* a generator-based context manager.
'''

from contextlib import contextmanager
import sys
from typing import Iterator


class ContextError(Exception):
    '''Exception raised deliberately inside the context manager example.'''


class ContextTest:
    '''Simple context manager that reports its lifecycle events.'''

    _context_nr: int

    @property
    def context_nr(self) -> int:
        '''Return the context number.'''
        return self._context_nr

    @context_nr.setter
    def context_nr(self, value: int) -> None:
        '''Update the context number.'''
        self._context_nr = value

    def __init__(self, context_nr: int) -> None:
        '''Initialize the context manager state.'''
        self._context_nr = context_nr
        print(f'created with {self._context_nr}')

    def __enter__(self) -> 'ContextTest':
        '''Enter the context manager.'''
        print(f'entering {self._context_nr}')
        return self

    def __exit__(self, exception_type, exception_value, backtrace) -> None:
        '''Report whether the context exited normally or via an exception.'''
        print(f'exiting {self._context_nr}')
        if exception_type:
            print(f'exception in context {self._context_nr}:')
            print('\t', exception_type, exception_value, backtrace)
            return
        print(f'no exception in context {self._context_nr}')


@contextmanager
def label(name: str) -> Iterator[str]:
    '''Yield a label while reporting entry and exit.'''
    print(f'entering label({name})')
    yield name
    print(f'exiting label({name})')


def main() -> int:
    '''Run the context manager demonstration.'''
    with ContextTest(1) as context_1, ContextTest(2) as context_2:
        print(f'in context {context_1.context_nr}')
        print(f'in context {context_2.context_nr}')
    with label('foo') as foo_label, label('bar') as bar_label:
        print(foo_label, bar_label)
    with ContextTest(1) as context_1, ContextTest(2) as context_2:
        print(f'in context {context_1.context_nr}')
        raise ContextError('illustration of context manager exceptions')
        # print(f'in context {context_2.context_nr}')
    return 0


if __name__ == '__main__':
    STATUS = main()
    sys.exit(STATUS)
