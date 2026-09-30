import random
from oliot import noppapeli, varaston_lapikaynti

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
        arvot = noppapeli()
        print(f"\nOle hyvä!")
    elif valinta == "ika" or valinta == "ikä":
        print(f"Unohditko oman ikäsi? Sinun ikäsi on {ika}")
    elif valinta == "varasto":
        varaston_lapikaynti(varasto)
    elif valinta == "lopeta" or valinta == "":
        break
    else:
        print("Kirjoititko oikein?\n")
print("\nHei hei!\n")
