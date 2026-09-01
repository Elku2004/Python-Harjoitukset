arvo = int(input("Anna luku: "))
kaikki = 1
for luku in range(1,arvo,1):
    if arvo % luku == 0 and luku != 1:
        print(f"{arvo} ei ole alkuluku")
        break
    kaikki = kaikki + 1
if kaikki == arvo:
    print(f"{arvo} on alkuluku")

