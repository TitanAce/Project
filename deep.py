number =str(input("Whatis the Answer to the Great Question of Life, the Universe, and Everything?").lower())

match number:
    case "42" | "forty-two" | "forty two" | " 42  ":
        print("Yes")
    case _:
        print("No")
