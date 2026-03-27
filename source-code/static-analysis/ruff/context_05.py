#!/usr/bin/env python
'''Illustrate two ways to implement a context manager.

The example shows:

* a class-based context manager,
* a generator-based context manager.
'''

import sys
from collections.abc import Iterator
from contextlib import contextmanager
from types import TracebackType


class ContextError(Exception):
    '''Exception raised deliberately inside the example.'''


class ContextTest:
    '''Simple context manager that reports its lifecycle events.'''

    def __init__(self, context_nr: int) -> None:
        '''Initialize the context manager state.'''
        self._context_nr = context_nr
        print(f'created with {self._context_nr}')

    def __enter__(self) -> 'ContextTest':
        '''Enter the context manager.'''
        print(f'entering {self._context_nr}')
        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_value: BaseException | None,
        backtrace: TracebackType | None,
    ) -> None:
        '''Report whether the context exits with an exception.'''
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
    with ContextTest(1) as c1, ContextTest(2) as c2:
        print(f'in context {c1._context_nr}')
        print(f'in context {c2._context_nr}')
    with label('foo') as foo, label('bar') as bar:
        print(foo, bar)
    with ContextTest(1) as c1, ContextTest(2) as c2:
        print(f'in context {c1._context_nr}')
        raise ContextError
        print(f'in context {c2._context_nr}')
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
