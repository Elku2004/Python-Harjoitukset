import random
arvot = []
kerta = int(input("Kuinka monta arpakuutiota?: "))
summa = 0
numero = 0

for luku in range(1,kerta+1):
    numero = random.randint(1,6)
    summa = summa + numero
    arvot.append(numero)
print(f"Numerot ovat {arvot}\nja niiden summa on {summa}")