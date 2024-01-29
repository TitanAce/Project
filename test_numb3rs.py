from numb3rs import validate

def main():
    test_layout()
    test_ip()

def test_layout():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.1.1") == False
    assert validate(r"1.1") == False
    assert validate(r"1") == False

def test_ip():
    assert validate(r"255.255.255.255") == True
    assert validate(r"198.832.0.9") == False
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"1.2.3.1000") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()

