from bank import value

def main():
    test_value()
    test_value2()
    test_values()


def test_value():  # $0
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello") == 0


def test_value2():  # $20
    assert value("how") == 20
    assert value("HOW") == 20
    assert value("Hsiubi") == 20


def test_values():  # $100
    assert value("no") == 100
    assert value("ewdv") == 100
    assert value("odkcn") == 100


if __name__ == "__main__":
    main()
