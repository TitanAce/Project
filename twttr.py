def main():
    word = shorten(input("Input: "))
    print("Output: ", word)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for twttr in vowels:
        while twttr in word:
            word = word.replace(twttr, "")
    return word

if __name__ == "__main__":
    main()
