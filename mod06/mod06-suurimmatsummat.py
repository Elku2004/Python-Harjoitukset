numero = input("Anna luku: ")
arvot = []
while numero != "":
    numero = int(numero)
    arvot.append(numero)
    numero = input("Anna luku: ")
arvot.sort(reverse=True)
print(f"Suurimmat 5 arvoa ovat:\n{arvot[0:5]}")
