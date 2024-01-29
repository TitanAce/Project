def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(f"{percentage}", sep="")

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                fraction = input("Fraction: ")
            result = x / y
        except ValueError:
            raise
        except ZeroDivisionError:
            raise
        except:
            raise
        else:
            break
    return result


def geuge(percentage):
    percentage = float(percentage)
    if percentage == 0.00 or percentage == 0.01:
        return "E"
    elif percentage == 1 or percentage == 0.99:
        return "F"
    else:
        percentage *= 100
        percentage = round(percentage, 2)
        return f"{percentage}%"

if __name__ == "__main__":
    main()
