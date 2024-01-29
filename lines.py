import sys

code_lines = 0

if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
        if " " in sys.argv[1]:
            sys.exit("non-zero exit code")
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != "":
                        code_lines += 1
                    else:
                        code_lines += 0
            print(code_lines)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

elif len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
