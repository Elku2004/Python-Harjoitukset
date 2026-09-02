def summa (luvut):
    s = 0
    for i in luvut:
        s = s + i
    return s

lukujono = []
while True:
    luku = input("Anna luku tai lopeta painamalla enter: ")
    if luku == "":  
        break  
    else:
        lukujono.append(int(luku))
vastaus = summa(lukujono)
print(f"Summa on {vastaus}")


