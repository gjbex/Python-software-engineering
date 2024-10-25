'''Module to compute the factorial of a number'''


def fac(n: int) -> int:
    '''Return the factorial of n

    Parameters
    ----------
    n : int
        The number to compute the factorial of

    Returns
    -------
    int
        The factorial of n

    Raises
    ------
    ValueError
        If n is negative
    '''
    if n < 0:
        raise ValueError("fac_iter() not defined for negative values")
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


def fac_bad(n: int) -> int:
    '''Return the factorial of n

    Parameters
    ----------
    n : int
        The number to compute the factorial of

    Returns
    -------
    int
        The factorial of n
    '''
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result
