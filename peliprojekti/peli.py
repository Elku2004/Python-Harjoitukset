import random
from oliot import noppapeli, varaston_lapikaynti
import time
import json
from paketti import Pelaaja, Huone, Esine
varasto = []
miekka = Esine("Miekka", "4kg")
reppu = Esine("Reppu", "0,3kg")
kilpi = Esine("Kilpi", "10kg")
huone1 = Huone("Eteinen", kilpi, "Edessäsi on tavallinen eteinen. Löydät edestäsi jotain")
print("\nSyötä tietosi\n")
nimi = input("Nimi: ")
ika = int(input("Ikä: "))
kayttaja = Pelaaja(nimi, ika)
kayttaja.esineet.append(reppu)
kayttaja.esineet.append(miekka)
while True:
    if ika < 12:
        print("Sinun täytyy olla vähintään 12v. pelataksesi")
        break

    print(f"\nTervetuloa {nimi}!\n\nAloita\nVarasto\nNoppa\nTarkista Ikä\nLopeta")
    valinta = input("\nKirjoita valintasi: ")
    valinta = valinta.lower()
    if valinta == "noppa":
        arvot = noppapeli()
        print(f"\nOle hyvä!")
    elif valinta == "ika" or valinta == "ikä":
        print(f"Unohditko oman ikäsi? Sinun ikäsi on {ika}")
    elif valinta == "varasto":
        varaston_lapikaynti(kayttaja.esineet)
    elif valinta == "lopeta" or valinta == "":
        break
    elif valinta == "aloita":
        print(f"Tervetuloa {kayttaja.nimi} hotelliin")
        kayttaja.siirry(huone1)
        print("The End!")
        print("Tavarasi ovat: ")
        for i in kayttaja.esineet:
            print(f"- {i.nimi}, Paino: {i.paino}")
        input()
    else:
        print("Kirjoititko oikein?\n")
print("\nHei hei!\n")
