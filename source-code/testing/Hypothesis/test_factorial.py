from math import factorial as fac_math
from hypothesis import assume, given, strategies as st
from factorial import fac, fac_bad


@given(st.integers(min_value=0, max_value=100))
def test_fac(n):
    assert fac(n) == fac_math(n)


@given(st.integers(max_value=-1))
def test_fac_neg(n):
    try:
        _ = fac(n)
        assert False, 'no ValueError raised'
    except ValueError:
        assert n < 0


@given(st.integers(min_value=0, max_value=100))
def test_fac_bad(n):
    assert fac_bad(n) == fac_math(n)


@given(st.integers(max_value=-1))
def test_fac_bad_neg(n):
    try:
        _ = fac_bad(n)
        assert False, 'no ValueError raised'
    except ValueError:
        assert n < 0
