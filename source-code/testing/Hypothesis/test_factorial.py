from math import factorial as fac_math
from hypothesis import assume, given, strategies as st
from factorial import fac


@given(st.integers(min_value=0, max_value=100))
def test_fac_same(n):
    assert fac(n) == fac_math(n)


@given(st.integers(max_value=-1))
def test_fac_neg(n):
    try:
        assert fac(n) == fac_math(n)
    except ValueError:
        assert n < 0
