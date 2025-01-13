import pytest

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 33), (4, 44), (5, 55)])
def test_multiplication_by_11(num, output):  
    assert num*11 == output
