import pytest
import math

def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 5

def test_equality_failure():
    assert 4 == 4

def test_square_failure():
    num = 25
    assert 5 * 5 == num
    
