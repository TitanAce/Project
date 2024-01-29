snake_case = input("camelCase: ")

for i in snake_case:
    if i.isupper():
        snake_case = snake_case.replace(i, "_" + i.lower())
print(snake_case)
