from fuel import convert, geuge
import pytest


def main():
    test_convert()
    test_geuge()

def test_convert():
    assert convert("1/2") == 0.50
    assert convert("1/4") == 0.25
    assert convert("1/100") == 0.01
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_geuge():
    assert geuge(0.01) == "E"
    assert geuge(0.99) == "F"
    assert geuge(0.2) == "20.0%"



