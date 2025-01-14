from fibonacci import fib

import pytest


def test_fib_0():
    assert fib(0) == 1

def test_fib_1():
    assert fib(1) == 1

def test_fib_2():
    assert fib(2) == 2

def test_fib_5():
    assert fib(5) == 8

@pytest.mark.slow
def test_fib_40():
    assert fib(40) == 165580141

def test_fib_negative():
    with pytest.raises(ValueError):
        _ = fib(-1)    
