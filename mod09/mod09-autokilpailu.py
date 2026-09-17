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
            print("Huippunopeus!")
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
#for i in autot:
#    print(f"{i}\n{autot[i]}\n{autot[i].rekisteritunnus}\n{autot[i].huippunopeus}")

#print("3")
#time.sleep(0.5)
#print("2")
#time.sleep(0.5)
#print("1")
#time.sleep(0.5)
#print("GO!")
#time.sleep(0.5)
o = 0
for i in autot:
    o += 1
    print(autot[f"Auto {o}"])
    autot[f"Auto {o}"].kiihdyta(random.randint(10,15))
    print(autot[f"Auto {o}"].nyt_nopeus)

