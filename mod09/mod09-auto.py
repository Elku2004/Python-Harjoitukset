import time
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
auto1 = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.huippunopeus} km/h\n"
      f"Tämänhetkinen nopeus: {auto1.nyt_nopeus} km/h\nKuljettu matka: {auto1.matka}")

print("Auto lähtee käyntiin!")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Tämänhetkinen nopeus: {auto1.nyt_nopeus}")
auto1.kulje(1.5)
auto1.kiihdyta(-200)
print(f"Tämänhetkinen nopeus: {auto1.nyt_nopeus}")
print(f"Auton kuljettu matka {auto1.matka}")
