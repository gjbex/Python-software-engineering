#!/usr/bin/env python3

import functools


def check_bounds(min_value, max_value):
    '''Check bounds of a function argument

    Parameters
    ----------
    min_value: float
        Smallest value allowed for the function's parameter
    max_value: float
        Largest value allowed for the function's parameter

    Raises
    ------
    ValueError:
        If the argument is outside the specified bounds
    '''
    def check_bounds_wrapper(_func):
        @functools.wraps(_func)
        def wrapper(x):
            if min_value > x or x > max_value:
                raise ValueError(f'argument {x} not in [{min_value}, {max_value}]')
            return _func(x)
        return wrapper
    return check_bounds_wrapper


@check_bounds(min_value=-1.0, max_value=1.0)
def silly(x):
    '''Compute a rather uninteresting function

    Parameters
    ----------
    x: float
        Argument for the function

    Returns
    -------
    float:
        Value computed by the function
    '''
    return x**2 - 2.0


if __name__ == '__main__':
    print(silly(0.5))
    try:
        print(silly(2.5))
    except ValueError as e:
        print(f'Exception raised as expected: {e}')
