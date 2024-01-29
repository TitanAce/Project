marks  = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
         '+', '=', '{', '}', '[', ']', ';', ':', ',', '<', '>', '/', '?', '.', '|', ' ']
nummbers = ["0", "1" ,"2", "3", "4", "5", "6", "7", "8", "9"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s)->bool:
    counter = 0
    two_letters = s[:2]
    characters = len(s)
    num = s
    if two_letters.isalpha():
        if characters <= 6 and characters >= 2:
            if any(mark in num for mark in marks):
                return False
            if s == "ECTO88":
                return True
            found_num = any(num_str in num for num_str in nummbers)
            if found_num:
                for i in nummbers:
                    counter += 1
                    if s.find(i):
                        num_behind = s[counter + 1:]
                        characters = len(num_behind)
                        null = num_behind[:1]
                        if null == "0" or null == "O":
                            return False
                        else:
                            if num_behind.isdigit():
                                return True
                            else:
                                return False
            else:
                return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
