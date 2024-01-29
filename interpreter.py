expression = input(">>")

x, y, z = expression.split(" ")

x, z = float(x), float(z)

operator = y

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
else:
    pass
print(result)
