import time
import random
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for i in range(10):
                self.autot[f"Auto {i+1}"].kiihdyta(random.randint(10,15))
                self.autot[f"Auto {i+1}"].kulje(1)

    def tulosta_tilanne(self):
        for i in kilpailu_1.autot:
            print(f"{i} - Rekisteritunnus: {kilpailu_1.autot[i].rekisteritunnus} Nopeus: {kilpailu_1.autot[i].nyt_nopeus}km/h Huippunopeus: {kilpailu_1.autot[i].huippunopeus}km/h Matka: {kilpailu_1.autot[i].matka}km")

    def kilpailu_ohi(self, end):
        for i in range(10):
            if self.autot[f"Auto {i+1}"].matka >= self.pituus:
                end = True
        return end


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nyt_nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        if self.nyt_nopeus + muutos <= 0:
            self.nyt_nopeus = 0
        elif self.nyt_nopeus + muutos >= self.huippunopeus:
            self.nyt_nopeus = self.huippunopeus
        else:
            self.nyt_nopeus += muutos
    def kulje(self, muutos):
        if muutos > 0:
            self.matka += self.nyt_nopeus * muutos
        else:
            pass   

autot = {}
for i in range(10):
    autot[f"Auto {i+1}"] = Auto(f"ABC-{i+1}", random.randint(100,200))
kilpailu_1 = Kilpailu("Suuri romuralli", 8000,  autot)
print(f"Tämän päivän kilpailu on {kilpailu_1.nimi}!\nSen pituus on noin {kilpailu_1.pituus}km!!")

print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)
print("GO!")
time.sleep(0.5)

p = 0
end = False
while True:
    p += 1
    kilpailu_1.tunti_kuluu()
    end = kilpailu_1.kilpailu_ohi(end)
    if end == True:
        break
    if p % 10 == 0:
        print(f"------------------------------------------------------------------------\nTunteja kulunut {p}\nTämänhetkinen tilanne: ")
        kilpailu_1.tulosta_tilanne()
        time.sleep(1)
print(f"------------------------------------------------------------------------\nKilpailu on ohi. Se kesti {p} tuntia!")
kilpailu_1.tulosta_tilanne()