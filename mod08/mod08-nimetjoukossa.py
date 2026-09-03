nimet = {""}
while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        "Aiemmin syötetty nimi"
    else:
        "Uusi nimi"
    nimet.add(nimi)
for i in nimet:
    print(i)