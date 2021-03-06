#!/usr/bin/env python

import sys


class TypedProperty():

    def __init__(self, name, type, default=None):
        self._name = '-' + name
        self._type = type
        self._default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self._name, self._default)

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f'value {value} is not of type {self._type}')
        setattr(instance, self._name, value)

    def __delete__(self, instance, cls):
        raise AttributeError('can not delete attribute')


class Book(object):

    title = TypedProperty('title', str)
    author = TypedProperty('author', str)
    year = TypedProperty('year', int)

    def __init__(self, title=None, author=None, year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year

    def __str__(self):
        return f'{self.title}\n  {self.author}, {self.year}'


if __name__ == '__main__':
    book1 = Book()
    print('showing defaults:')
    print(str(book1) + '\n')
    book1.title = 'Animal farm'
    book1.author = 'George Orwell'
    book1.year = 1945
    print(str(book1) + '\n')
    book2 = Book('Alice in Wonderland', 'Lewis Carroll', 1865)
    print(str(book2) + '\n')
    try:
        book3 = Book(1984, 'George Orwell', 1948)
    except TypeError as error:
        print(f'### error: {error}', file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
