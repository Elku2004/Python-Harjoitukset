def muunnos(luku):
    bensiini = luku * 3.785
    return bensiini

while True:
    bensiini = float(input("Kuinka monta gallonaa bensiiniä: "))
    if bensiini < 0:
        print("Syötit negatiivisen luvun. Hei hei!")
        break
    else:
        bensiini = muunnos(bensiini)
        print(f"Se on {bensiini} litraa!\n")