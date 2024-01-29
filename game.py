import random

while True:
    try:
        level = input("Level:")
        level = int(level)
        number = random.randint(1, level)
        break
    except:
        pass

while True:
    try:
        guessing = input("Guess: ")
        guessing = int(guessing)
        if guessing >= 0:
            if guessing > number:
                print("Too large!")
            elif guessing < number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass
