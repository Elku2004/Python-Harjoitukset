import random
from paketti import Esine
def varaston_lapikaynti(varasto):
    while True:
                valint2 = input("\nVaraston valikko:\nLisää\nTarkista\nTakaisin\nKirjoita valintasi: ")
                valint2 = valint2.lower()
                if valint2 == "lisaa" or valint2 == "lisää":
                    listaa(varasto)
                elif valint2 == "tarkista":
                    listatut(varasto)
                elif valint2 == "takaisin" or valint2 == "":
                    break
                else:
                    print("Kirjoititko oikein?\n")

def listaa(varasto):
    while True:
        s = input("Anna esineen nimi (tai paina Enter lopettaaksesi): ")
        if s == "":
            break
        v = input("Anna esineen paino: ")
        if v == "":
             break
        varasto.append(Esine(s, v))
    return varasto

def listatut(varasto):
    print("\n")
    print(f"Sinun varastossasi on: ")
    for x in varasto:
        print(f"-{x.nimi}")

def noppapeli():
    n = []
    kerta = int(input("Kuinka monta kertaa noppaa heitetään: "))
    for i in range(kerta):
        s = random.randint(1,6)
        n.append(s)
    for z in n:
        print(z)
    return n
