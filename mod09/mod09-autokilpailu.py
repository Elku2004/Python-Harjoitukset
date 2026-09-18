import time
import random
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

print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)
print("GO!")
time.sleep(0.5)

end = False
while True:
    for i in range(10):
        autot[f"Auto {i+1}"].kiihdyta(random.randint(10,15))
        autot[f"Auto {i+1}"].kulje(1)

    for i in range(10):
        if autot[f"Auto {i+1}"].matka >= 10000:
            end = True
    if end == True:
        print("Kisa seis!")
        time.sleep(1)
        break

for i in autot:
    print(f"{i} - Rekisteritunnus: {autot[i].rekisteritunnus} Nopeus: {autot[i].nyt_nopeus} Huippunopeus: {autot[i].huippunopeus} Matka: {autot[i].matka}")
