import random as rnd
print("\nSyötä tietosi\n")
nimi = input("Nimei: ")
ika = int(input("Ikä: "))
while True:
    if ika < 12:
        print("Sinun täytyy olla vähintään 12v. pelataksesi")
        break
    print(f"\nTervetuloa {nimi}!\n\nAloita\nNoppa\nTarkista Ikä (ika)\nLopeta")
    valinta = input("\nKirjoita valintasi: ")
    valinta = valinta.lower()
    if valinta == "aloita":
        print("Peli tulossa pian")
    elif valinta == "noppa":
        kerta = int(input("Kuinka monta kertaa noppaa heitetään: "))
        heitto = 0
        arvot = []
        while heitto < kerta:
            vast = rnd.randint(1,6)
            arvot.append(vast)
            heitto = heitto + 1
        print(f"{arvot}\nOle hyvä!")
    elif valinta == "ika":
        print(f"Unohditko oman ikäsi? Sinun ikäsi on {ika}")
    elif valinta == "lopeta":
        break
    else:
        print("Kirjoititko oikein?\n")
print("\nHei hei!\n")