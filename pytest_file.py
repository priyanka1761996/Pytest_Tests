import pytest


def test_greater_than_equal():
    num = 100
    assert num>=100

@pytest.mark.xfail
@pytest.mark.greater
def test_greater():
    num = 100
    assert num<80

@pytest.mark.skip
@pytest.mark.less
def test_less_than_equal():
    num = 200
    assert num<=380

@pytest.mark.less
def test_less():
    num = 50
    assert num<70
