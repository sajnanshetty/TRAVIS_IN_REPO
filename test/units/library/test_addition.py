from library.addition import *

print(abc(1, 2))

def test_abc():
    val = abc(1, 2)
    assert val == 3

def test_abc2():
    val = abc(1, 2)
    assert val == 4
