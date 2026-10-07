from paketti import Pelaaja, tallenna_peli, lataa_tallenne, aloita_luonti, luo_kayttaja, Esine, taso

import os
import json

#Onko tallennus jo olemassa
for i in range(1, 11):
        if os.path.exists(f"peliprojekti/paketti/save{i}.json"):
            on_tallenne = True
            break
        else:
            on_tallenne = False

#Jos tallennus on, voit ladata pelin tai tehdä uuden käyttäjän
if on_tallenne == True:
    print("-------------")
    while True:
        valinta = input("Kirjaudu (K)\nLuo uusi(L)\nAnna valintasi: ")
        valinta = valinta.lower()
        if valinta == "k":
            while True:
                try:
                    valinta = int(input("Tallenteen numero: "))
                    break
                except ValueError:
                    print("Syötä numero")
            if os.path.exists(f"peliprojekti/paketti/save{valinta}.json"):
                with open(f"peliprojekti/paketti/save{valinta}.json", "r") as data:
                    save = json.load(data)
                    kayttaja = lataa_tallenne(save)
                    break            
            else:
                print("Virheellinen numero")
        elif valinta == "l":
            kayttaja = aloita_luonti()
            break
        else:
            print("-------------")
else:
    kayttaja = aloita_luonti()

valinta = ""
print(f"Tervetuloa {kayttaja.nimi}")
input()
#Päävalikko
while True:
    valinta = ""
    if kayttaja.alaikainen == True:
         break
    try:
        valinta = int(input("1. Aloita/Jatka, 2. Varasto\n3. Ohjeet, 4. Tallenna\n5. Lopeta\n"))
    except ValueError:
        print("Syöttämäsi arvo ei ole luku")
        input()
    if valinta == 1:
        taso(kayttaja, kayttaja.taso)
#Voi tarkistaa pelin sisällä keräämäsi esineet. Voi kerätä enemmän kuin yhden samanlaisen
    elif valinta == 2:
        print("Varastossasi on: ")
        for i in kayttaja.esineet:
            print(f"- {i.nimi}")
        input()
#Tulostaa ohjeet
    elif valinta == 3:
        with open("peliprojekti/paketti/ohjeet.txt", "r", encoding="utf-8") as ohjeet:
            print(f"\n{ohjeet.read()}")
#Tallentaa pelin
    elif valinta == 4:
        tallenna_peli(kayttaja)
        input()
#Lopettaa pelin ja kysyy haluatko tallentaa
    elif valinta == 5:
        valinta = input("Tallennetaanko eteneminen? k/e: ")
        if valinta == "k":
            tallenna_peli(kayttaja)
            input()
            break
        if valinta == "e":
            break

print("Hei hei!")
    
    
