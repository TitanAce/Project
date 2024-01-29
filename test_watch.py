from watch import parse

def main():
    test_parse()
    test_parse2()


def test_parse():  # $0
    assert parse(r'<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == (r'<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')


def test_parse2():  # $20
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None

