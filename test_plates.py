from plates import is_valid


def main():
    test_valid_min_max()
    test_valid_true()
    test_valid_num()
    test_valid()

def test_valid_min_max():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False

def test_valid_true():
    assert is_valid("cs50") == True
    assert is_valid("hi") == True
    assert is_valid("nice") == True

def test_valid_num():
    assert is_valid("50") == False
    assert is_valid("54663") == False

def test_valid():
    assert is_valid("cs.50") == False
    assert is_valid("?!$") == False
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False
