from app import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(3, 2) == 1

