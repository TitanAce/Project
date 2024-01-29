grocery = {}
while True:
    try:
        item = input().lower()
    except EOFError:
        for i in sorted(grocery.keys()):
            print(grocery[i], i.upper())
        break
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1
