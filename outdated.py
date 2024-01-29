months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month = 0

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            m, d, y = date.split("/")
            if int(m) >= 1 and int(m) <= 12:
                if int(d) >= 1 and int(d) <= 31:
                    break
        else:
            date = date.replace(",", " ")
            m, d, y = date.split(" ")
            month = months.index(str(m))
            month += 1
            if int(month) >= 1 and int(month) <= 12:
                if int(d) >= 1 and int(d) <= 31:
                    break
    except:
        pass


print(f"{y}-{int(month):02}-{int(d):02}", sep= "")

