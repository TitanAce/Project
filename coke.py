coin = 50

while True:
    print("Amount Due:", coin)
    insert_coin = input("Insert Coin: ")
    insert_coin = int(insert_coin)
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        coin = coin - insert_coin
        if coin <= 0:
            print("Change Owed:", -coin)
            break
