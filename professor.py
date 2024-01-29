import random

def main():
    correct_answers = 0
    counter = 0
    tries = 0
    level = get_level()
    while True:
        x, y = generate_integer(level)
        z = x+y
        counter += 1
        answer = input(f"{x} + {y} = ")
        answer = int(answer)
        if counter >= 10:
            print()
            print(f"Score: {correct_answers +1}")
            break
        if answer != z:
            while True:
                try:
                    tries += 1
                    if answer == z or tries >= 3:
                        print(z)
                        break
                    print()
                    print("EEE")
                    answer = input(f"{x} + {y} = ")
                    answer = int(answer)
                except:
                    pass
        else:
            correct_answers += 1

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
