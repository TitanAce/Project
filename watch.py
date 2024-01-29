import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if (match := re.search(r'^[a-z0-9=\'"\s]*?(https?://(?:www\.)?youtube\.[a-z]/(?:[a-z])?+)/(?:[a-z]+/)?([a-z]*?)$', s, re.IGNORECASE)):
        return match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
