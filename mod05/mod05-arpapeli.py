import random
luku = random.randint(1,10)
arvaus = int(input("Arvaa määritelty luku: "))
while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus!\n")
    else:
        print("Liian pieni arvaus!\n")
    arvaus = int(input("Arvaa luku: "))
else:
    print(f"Oikein! Vastaus oli {luku}.")