import py
def test_numbers_3_4():
    assert py.multiply(3,4) == 12
def test_numbers_0_x():
    assert py.multiply(0,4) == 0
    assert py.multiply(4,0) == 0
    assert py.multiply(1,0) == 0
