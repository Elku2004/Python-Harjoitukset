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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
    def kiihdyta(self, muutos):
        super().kiihdyta(muutos)
    def kulje(self, muutos):
        super().kulje(muutos)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)
    def kiihdyta(self, muutos):
        super().kiihdyta(muutos)
    def kulje(self, muutos):
        super().kulje(muutos)


auto_1 = Sahkoauto("ABC-15", 180, 52.5)
auto_2 = Polttomoottoriauto("ACD-123", 165, 32.3)

print("Autot lähtee käyntiin!\n")
auto_1.kiihdyta(30)
auto_2.kiihdyta(70)

auto_1.kulje(3)
auto_2.kulje(3)

print(f"Auton {auto_1.rekisteritunnus} tiedot:\nHuippunopeus: {auto_1.huippunopeus}\nAkkukapasiteetti: {auto_1.akkukapasiteetti}\n"
      f"Kuljettu matka: {auto_1.matka}\n")
print(f"Auton {auto_2.rekisteritunnus} tiedot:\nHuippunopeus: {auto_2.huippunopeus}\nBensatankin koko: {auto_2.bensatankki}"
      f"\nKuljettu matka: {auto_2.matka}")
#print(f"Tämänhetkinen nopeus: {auto1.nyt_nopeus}")
#auto1.kulje(1.5)
#auto1.kiihdyta(-200)
#print(f"Tämänhetkinen nopeus: {auto1.nyt_nopeus}")
#print(f"Auton kuljettu matka {auto1.matka}")
