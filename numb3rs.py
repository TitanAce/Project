import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    try:
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
            ip_1, ip_2, ip_3, ip_4 = map(int, ip.split("."))
            if ip_1 in range(0, 256) and ip_2 in range(0, 256) and ip_3 in range(0, 256) and ip_4 in range(0, 256):
                return True
            else:
                return False
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    main()
