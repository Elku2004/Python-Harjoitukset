import random
import time
import json
import os

from oliot import noppapeli, varaston_lapikaynti
from paketti import Pelaaja, Huone, Esine

#Alaikäinen on muuttuja. Jos totta, peli pysähtyy heti.
alaikainen = False

#Ikätarkistus, joka johtaa hahmon luontiin
def aloita_luonti():
    print("\nSyötä tietosi\n")
    while True:
        nimi = input("Nimi: ")
        if nimi != "":
             break
        print("Nimi ei voi ola tyhjä!")
    ika = int(input("Ikä: "))
    while True:
        if ika < 12:
            print("Sinun täytyy olla 12v tai yli pelataksesi")
            kayttaja = luo_kayttaja(nimi, ika)
            break
        else:
            kayttaja = luo_kayttaja(nimi, ika)
            break
    return kayttaja

#Ikä toimii salasanana. Lataa tallenteen ja uudelleenluo käyttäjän tallennuksen tiedoilla
def lataa_tallenne(save):
        salasana = int(input(f"Hei {save["Nimi"]}, anna ikäsi jatkaaksesi: "))
        while True:    
            if salasana == save["Ika"]:
                kayttaja = Pelaaja(save["Nimi"], save["Ika"])
                tavarat = save["Tavaroiden_nimet"]
                for i in tavarat:
                    kayttaja.esineet.append(Esine(i, save["Varasto"][i])) 
                print("Lataus onnistui")
                input()
                return kayttaja
            if salasana == "":
                break
            else:
                print("Kirjoititko oikein?")

#funktio, joka tekee Pelaajan
def luo_kayttaja(nimi, ika):
    kayttaja = Pelaaja(nimi, ika)
    miekka = Esine("Miekka", "4kg")
    reppu = Esine("Reppu", "0,3kg")
    kayttaja.esineet.append(reppu)
    kayttaja.esineet.append(miekka)
    input()
    return kayttaja

#Tallentaa pelin
def tallenna_peli():
    while True:
        num = input("Minkä tallenuksen päälle kirjoitetaan? 1-10 (tai enter peruaksesi tallentamisen): ")
        if num == "":
            break
        num = int(num)
        if 10 >= num > 0:
            varasto_tallenne = {}
            varasto_nimet = []
            for i in kayttaja.esineet:
                varasto_nimet.append(i.nimi)
                varasto_tallenne[i.nimi] = i.paino
            kayttaja_tiedot = {f"Nimi": kayttaja.nimi,
                               f"Varasto": varasto_tallenne,
                               f"Ika": kayttaja.ika,
                               f"Tavaroiden_nimet": varasto_nimet}
            with open(f"peliprojekti/paketti/save{num}.json", "w") as save:
                json.dump(kayttaja_tiedot, save)
            print("Tallennus onnistui!")
            break
        else:
            print("virheellinen numero")


#Muutama esine, huone
kilpi = Esine("Kilpi", "10kg")
huone1 = Huone("Eteinen", kilpi, "Edessäsi on tavallinen eteinen. Löydät edestäsi jotain")

#Onko tallennus jo olemassa
for i in range(1, 11):
        if os.path.exists(f"peliprojekti/paketti/save{i}.json"):
            on_tallenne = True
            break
        else:
            on_tallenne = False

#Jos tallenne on olemassa, kirjaudut sisään tai aloitat uuden
if on_tallenne == True:
    print("-------------")
    while True:
        valinta = input("Kirjaudu (K)\nLuo uusi(L)\nAnna valintasi: ")
        valinta = valinta.lower()
        if valinta == "k":
            valinta = int(input("Tallenteen numero: "))
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

#Luo käyttäjä


#nollaa valinta
valinta = ""
#Peli!
while True:         
    if kayttaja.alaikainen == True:
        break
    print(f"\nTervetuloa {kayttaja.nimi}!\n\nAloita\nVarasto\nNoppa\nOhjeet\nLopeta")
    valinta = input("\nKirjoita valintasi: ")
    valinta = valinta.lower()
    if valinta == "noppa":
        arvot = noppapeli()
        print(f"\nOle hyvä!")
        input()
    elif valinta == "ohjeet":
        with open("peliprojekti/paketti/ohjeet.txt", "r") as ohjeet:
            print(ohjeet.read())
            input()
    elif valinta == "varasto":
        varaston_lapikaynti(kayttaja.esineet)
    elif valinta == "lopeta" or valinta == "":
        valinta = input("Tallennetaanko eteneminen? k/e: ")
        if valinta == "k":
                tallenna_peli()
                input()
                break
        if valinta == "e":
            break
    elif valinta == "aloita":
        with open("peliprojekti/paketti/intro.txt", "r") as intro:
            print(intro.read())
            input()
        kayttaja.siirry(huone1)
        print("The End!")
        print("Tavarasi ovat: ")
        for i in kayttaja.esineet:
            print(f"- {i.nimi}, Paino: {i.paino}")
        input()
    else:
        print("Kirjoititko oikein?\n")
print("\nHei hei!\n")
