import pytest


@pytest.mark.parametrize("a,b,final", [(1, 2, 3), (2, 2, 4), (4, 3, 7)])
def test_add(a, b, final):
    assert a + b == final


def test_b():
    print("B test case Passed")
