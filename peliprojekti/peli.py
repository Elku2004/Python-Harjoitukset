import random
def listaa():
    while True:
        s = input("Anna esineen nimi (tai paina Enter lopettaaksesi): ")
        if s == "":
            break
        varasto.append(s)
    return varasto
def listatut():
    print("\n")
    print(f"Sinun varastossasi on: ")
    for x in varasto:
        print(f"-{x}")
def noppapeli(luku):
    n = []
    for i in range(luku):
        s = random.randint(1,6)
        n.append(s)
    for z in n:
        print(z)
    return n

varasto = []
print("\nSyötä tietosi\n")
nimi = input("Nimei: ")
ika = int(input("Ikä: "))
while True:
    if ika < 12:
        print("Sinun täytyy olla vähintään 12v. pelataksesi")
        break
    print(f"\nTervetuloa {nimi}!\n\nAloita\nVarasto\nNoppa\nTarkista Ikä\nLopeta")
    valinta = input("\nKirjoita valintasi: ")
    valinta = valinta.lower()
    if valinta == "aloita":
        print("Peli tulossa pian")
    elif valinta == "noppa":
        kerta = int(input("Kuinka monta kertaa noppaa heitetään: "))
        arvot = noppapeli(kerta)
        print(f"\nOle hyvä!")
    elif valinta == "ika" or valinta == "ikä":
        print(f"Unohditko oman ikäsi? Sinun ikäsi on {ika}")
    elif valinta == "varasto":
        while True:
            valint2 = input("\nVaraston valikko:\nLisää\nTarkista\nTakaisin\nKirjoita valintasi: ")
            valint2 = valint2.lower()
            if valint2 == "lisaa" or valint2 == "lisää":
                listaa()
            elif valint2 == "tarkista":
                listatut()
            elif valint2 == "takaisin" or valint2 == "":
                break
            else:
                print("Kirjoititko oikein?\n")
    elif valinta == "lopeta" or valinta == "":
        break
    else:
        print("Kirjoititko oikein?\n")
print("\nHei hei!\n")