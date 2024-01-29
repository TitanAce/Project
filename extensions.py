extension = input("File name: ").lower()

images = ["gif", "jpg", "jpeg", "png"]
txts =["pdf", "text", "zip"]
l = 0

for i in images:
    l += 1
    if extension.count(i):
        x = ("image/"+ i)
        x = x.replace(" ", "")
        x = x.replace("jpg", "jpeg")
        print(x)
        l = 0
if l >=  4:
    if "plain.txt" in extension:
        print("text/plain")
        l = 0
        pass
    for t in txts:
        l += 1
        if extension.count(t):
            x = ("application/"+ t)
            x = x.replace(" ", "")
            print(x)
            l = 0

if l == 7 :
    print("application/octet-stream")
