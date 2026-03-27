#!/usr/bin/env python

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import ConvertibleToInt


class MyClass:

    def __init__(self, data: 'ConvertibleToInt') -> None:
        self._data = int(data)

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: 'ConvertibleToInt') -> None:
        self._data = int(value)

    def __repr__(self) -> str:
        return f'data: {self.data}'


def print_data(data: MyClass) -> None:
    print(data)


if __name__ == '__main__':
    data = MyClass('25')
    print_data(data)
