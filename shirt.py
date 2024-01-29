import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    print("Too many or too few command-line arguments")
    sys.exit(1)

extensions = [".jpg", ".jpeg", ".png"]
extension1 = os.path.splitext(sys.argv[1])[1]
extension2 = os.path.splitext(sys.argv[2])[1]

if extension1 != extension2 or extension1 not in extensions:
    print("Input and output have different extensions or invalid extension")
    sys.exit(1)

try:
    user_image = Image.open(sys.argv[1])
except FileNotFoundError:
    print("File doesn't exist")
    sys.exit(1)

shirt = Image.open("shirt.png")
size = shirt.size
user_image = ImageOps.fit(user_image, size)
user_image.paste(shirt, (0, 0))
user_image.save(sys.argv[2])


sys.exit(0)
