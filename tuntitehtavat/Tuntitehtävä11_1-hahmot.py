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

class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = randint(50, 100)

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

class Pelaaja(Hahmo):
    def __init__(self, nimi):
        super().__init__(nimi)
        self.score = 0
        self.no_pommi = 0
        self.tavaralista = ["Miekka", "Kilpi"]

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Tavaralista:")
        for i in self.tavaralista:
            print(f"- {i}")
        print(f"Pisteet: {self.score}")
        
    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        vastustaja.hp = randint(50, 100) + loop * 5
        vastustaja.tulosta_tiedot()
        input()
    
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            return ""
        else:
            print(f"{self.nimi} voitti taistelun!")
            print(f"Sait esineen: {vastustaja.esine}\n")
            pelaajahahmo.tavaralista.append(vastustaja.esine)
            self.score += vastustaja.hp
            print(f"+{vastustaja.hp} pistettä")

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki, esine):
        super().__init__(nimi)
        self.repliikki = repliikki
        self.esine = esine

    def tulosta_tiedot(self):
        print(self.repliikki)
        super().tulosta_tiedot()

def valittu_esine(esine):
    if esine == "pommi":
        if pelaajahahmo.no_pommi != 0:
            print("Selviät tällä kertaa!")
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
        pelaajahahmo.tavaralista.append("Vitutus")
    elif esine == "ranskalaiset korkokengät":
        print("Mahtavat korkokengät!")
        pelaajahahmo.tavaralista.append("Ranskalaiset Korkokengät")
        
    elif esine == "rasia":
        print("Ja rasiasta saat...")
        a = randint(1,3)
        if a == 1:
            print("Pommi!")
            if pelaajahahmo.no_pommi != 0:
                print("Selviät tällä kertaa!")
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
    loppu = pelaajahahmo.taistelu(hirviot[randint(0,2)])
    input()
    loop += 1
    if pelaajahahmo.hp == 0:
        break

pelaajahahmo.tavaralista.sort()
pelaajahahmo.tulosta_tiedot()

print(f"Peli ohi.")