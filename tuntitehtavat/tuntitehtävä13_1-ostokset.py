with open("tuntitehtavat/ostoslista.txt", "a") as tiedosto:
    tiedosto.write("\nKananmuna")

with open("tuntitehtavat/ostoslista.txt", "r") as tiedosto:
    print(tiedosto.read())
