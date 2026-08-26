luku = input("Anna luku: ")
if luku != "":
    iso = pieni = int(luku)


    while luku != "":
        if int(luku) > iso:
            iso = int(luku)
        elif int(luku) < pieni:
            pieni = int(luku)
        luku = input("Anna luku: ")
    else:
        print(f"Isoin luku oli {iso}\nPienin luku oli {pieni}")
print("Kiitos!")
