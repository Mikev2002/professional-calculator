import pytest
from app.operation import operations

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert operations.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (5, 10, -5),
    (0, 0, 0)
])
def test_subtract(a, b, expected):
    assert operations.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 6),
    (0, 10, 0),
    (-1, -1, 1)
])
def test_multiply(a, b, expected):
    assert operations.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (10, 5, 2),
    (1, 4, 0.25)
])
def test_divide(a, b, expected):
    assert operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(5, 0)
