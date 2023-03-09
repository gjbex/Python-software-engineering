import pytest


@pytest.fixture
def non_empty_list():
    return list(range(5))


def test_pop(non_empty_list):
    orig_len = len(non_empty_list)
    assert non_empty_list[-1] == orig_len - 1
    non_empty_list.pop()
    assert len(non_empty_list) == orig_len - 1
    assert non_empty_list[-1] == orig_len - 2


def test_append(non_empty_list):
    orig_len = len(non_empty_list)
    assert non_empty_list[-1] == orig_len - 1
    non_empty_list.append(orig_len)
    assert len(non_empty_list) == orig_len + 1
    assert non_empty_list[-1] == orig_len
