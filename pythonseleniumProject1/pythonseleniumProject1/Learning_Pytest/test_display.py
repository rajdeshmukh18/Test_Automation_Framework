import pytest

@pytest.mark.sanity
def test_c():
    assert 2 + 2 == 4

@pytest.mark.sanity
def testcal():
    assert 2+2 == 4

def testdisp():
    print("heelo")