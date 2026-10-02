while True:
    valinta = input("Tiedoston nimi: ")
    if valinta == "":
        break
    try:
        with open(f"tuntitehtavat/{valinta}", "r") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print("Tiedostoa ei löydy")
    