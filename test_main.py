from main import suma

def test_suma():
    assert suma(1) == 1
    assert suma(3) == 6
    assert suma(0) == 0
    assert suma(10) == 55