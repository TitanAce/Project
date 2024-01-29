names = []
try:
    while True:
        name = input("")
        names.append(name)
except EOFError:
    pass

if len(names) == 2:
    x = ", ".join(names[:-1]) + " and " + names[-1]
elif len(names) >= 3:
    x = ", ".join(names[:-1]) + ", and " + names[-1]

else:
    x = " ".join(names)

x = x.replace("'", "")
x = x.replace("(", "")
x = x.replace(")", "")
x = x.replace("[", "")
x = x.replace("]", "")

print("Adieu, adieu, to", x)
