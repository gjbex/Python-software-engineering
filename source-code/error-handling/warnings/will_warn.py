#!/usr/bin/env python

import warnings


class MyClass:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def get_value(self):
        warnings.warn("get_value is deprecated. Use the value property",
                      DeprecationWarning)
        return self._value


if __name__ == '__main__':
    obj = MyClass(42)
    print(obj.get_value())
    print(obj.value)
