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

class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

class Pelaaja(Hahmo):
    tavaralista = ["Miekka", "Kilpi"]
    def __init__(self, nimi):
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Tavaralista:")
        for i in self.tavaralista:
            print(f"- {i}")
        
    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        vastustaja.tulosta_tiedot()
        input()
    
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
        else:
            print(f"{self.nimi} voitti taistelun!")
            print(f"Sait esineen: {vastustaja.esine}\n")
            pelaajahahmo.tavaralista.append(vastustaja.esine)
            

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki, esine):
        super().__init__(nimi)
        self.repliikki = repliikki
        self.esine = esine

    def tulosta_tiedot(self):
        print(self.repliikki)
        super().tulosta_tiedot()


merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!", "Kala")
laavahirvio = Hirvio("Laavahirviö", "Blargh!", "Laavakivi")
salamahirvio = Hirvio("Salamahirviö", "Zzzzpt!", "Salama purkissa")

pelaajahahmo = Pelaaja(input("Anna hahmon nimi: "))

print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()

pelaajahahmo.taistelu(merihirvio)
input()

pelaajahahmo.taistelu(laavahirvio)
input()

pelaajahahmo.taistelu(salamahirvio)
input()

pelaajahahmo.tulosta_tiedot()

print(f"Peli ohi.")