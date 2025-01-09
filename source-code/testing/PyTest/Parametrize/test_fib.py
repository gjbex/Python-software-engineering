from fibonacci import fib

import pytest

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 8),
])
def test_fib(n, expected):
    assert fib(n) == expected

@pytest.mark.slow
@pytest.mark.parametrize("n, expected", [
    (40, 165580141),
    (41, 267914296),
    (42, 433494437),
])
def test_fib_40(n, expected):
    assert fib(n) == expected

def test_fib_negative():
    with pytest.raises(ValueError):
        _ = fib(-1)    
