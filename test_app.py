from app import add, subtract, mul

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(3, 2) == 1

def test_mul():
    assert mul(3, 2) == 6

