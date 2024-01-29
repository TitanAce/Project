from twttr import shorten

def main():
    test_lower_upper()
    test_num()

def test_lower_upper():
    assert shorten("test") == "tst"
    assert shorten("TEST") == "TST"
    assert shorten("TEst") == "Tst"
    assert shorten("Hello, WORLD") == "Hll, WRLD"
    assert shorten("1") == "1"
    assert shorten("!?.,") == "!?.,"


if __name__ == "__main__":
    main()
