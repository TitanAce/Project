def main():
    greeting = input("Greeting: ")
    get_doller = value(greeting)
    if get_doller == None:
        get_doller = 0
    print("$", get_doller)


def value(greeting):
    greeting = greeting.lower()

    if ("hello") in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
