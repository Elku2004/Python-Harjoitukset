'''
1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
Siirrä se sille luokalle, jossa se on sinusta looginen. 
Testaa, että peli toimii järkevästi.
'''
from random import randint
from time import sleep
from tuntitehtava12 import Hirvio, Pelaaja

def valittu_esine(esine):
    if esine == "pommi":
        if pelaajahahmo.no_pommi != 0:
            print(f"Selviät tällä kertaa!"
                  f"\nWhat doesn't kill you, makes you stronger -Joku todella älykäs"
                  f"\n30hp")
            pelaajahahmo.hp += 30
            pelaajahahmo.no_pommi -= 1
        else:
            print("Räjähdit")
            pelaajahahmo.hp = 0
    elif esine == "kilpi":
        pelaajahahmo.hp += 25
        print("hp nousi +25")
        pelaajahahmo.tavaralista.append("Kilpi")
    elif esine == "no_pommi":
        print("Pelastut yhdeltä pommilta")
        pelaajahahmo.no_pommi += 1
    elif esine == "kerroshampurilainen":
        print("Selvä! Olipa herkkua!\n +10hp")
        pelaajahahmo.hp += 10
    elif esine == "turhautus":
        print("No nyt turhauttaa!")
        pelaajahahmo.tavaralista.append("Turhautus")
    elif esine == "ranskalaiset korkokengät":
        print("Mahtavat korkokengät!")
        pelaajahahmo.tavaralista.append("Ranskalaiset Korkokengät")
    elif esine == "rasia":
        print("Ja rasiasta saat...")
        sleep(1)
        a = randint(1,3)
        if a == 1:
            print("Pommi!")
            if pelaajahahmo.no_pommi != 0:
                print(f"Selviät tällä kertaa!"
                      f"\nWhat doesn't kill you, makes you stronger -Joku todella älykäs"
                      f"\n+30hp")
                pelaajahahmo.hp += 30
                pelaajahahmo.no_pommi -= 1
            else: 
                print("Räjähdit!")
                pelaajahahmo.hp = 0
        elif a == 2:
            print("Kilpi")
            pelaajahahmo.hp += 25
            print("hp nousi +25")
        elif a == 3:
            print("Turhautus")
            print("No nyt turhauttaa!")
        else:
            print("Ei mitään!2")
    else:
        print("Ei mitään esinettä!1")
    print("\n")

class Kauppa:
    def __init__(self, nimi):
        self.varasto = ["Pommi", "Kilpi", "No_Pommi", "Kerroshampurilainen", "Turhautus",
                        "Rasia", "Ranskalaiset korkokengät"]
        self.nimi = nimi

    def kauppa_tapahtuma(self):
        print(f"Tervetuloa {self.nimi}- kauppaan! Saatavilla on: ")
        saatavuus = []
        for i in range(randint(1,4)):
            saatavuus.append(self.varasto[randint(0,6)])
            print(f"{i+1}. {saatavuus[i]}")
        valinta = input("Anna halutun tuotteen numero: ")
        if valinta == "":
                print("Ei valintaa!\n")
                return
        valinta = saatavuus[int(valinta)-1]
        print(valinta)
        valittu_esine(valinta.lower())

loop = 0
hirviot = []
hirviot.append(Hirvio("Merihirviö", "Lits läts, aion syödä sinut!", "Kala"))
hirviot.append(Hirvio("Laavahirviö", "Blargh!", "Laavakivi"))
hirviot.append(Hirvio("Salamahirviö", "Zzzzpt!", "Salama purkissa"))
pelaajahahmo = Pelaaja(input("Anna hahmon nimi: "))
kauppa1 = Kauppa("Pirkon Tavallinen K-Market")

print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()
loppu = "."
while loppu != "":
    kauppa1.kauppa_tapahtuma()
    if pelaajahahmo.hp == 0:
            break
    loppu = pelaajahahmo.taistelu(hirviot[randint(0,2)], loop)
    if pelaajahahmo.hp == 0:
            break
    input()    
    loop += 1
sleep(1)
pelaajahahmo.tavaralista.sort()
pelaajahahmo.tulosta_tiedot()

print(f"Peli ohi.")