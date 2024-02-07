import pytest

@pytest.fixture(params=["a","b"])
def test_a(request):
    print(request.param)
    yield
    print("End")

def test_b(test_a):
    print("Hello from B")