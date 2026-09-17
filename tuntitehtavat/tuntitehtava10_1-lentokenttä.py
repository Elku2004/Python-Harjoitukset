class Lentokentta:
    def __init__ (self, nimi):
        self.nimi = nimi
        self.lentokonelista = []

    def tulosta_koneet(self):
        for a in self.lentokonelista:
            a.tulosta_tiedot()

    def lisaa_koneita (self, lisays):
        self.lentokonelista.append(lisays)

class Lentokone: 
    def __init__ (self, nimi, bensa_max):
        self.nimi = nimi
        self.bensa_max = bensa_max
        self.bensa_nyt = 0

    def tankkaa(self, amount):
        a = self.bensa_nyt
        if self.bensa_nyt + amount > self.bensa_max:
            self.bensa_nyt = self.bensa_max
        else:
            self.bensa_nyt += amount
        print(f"Tankataan kone {self.nimi}\nBensaa mahtui {self.bensa_nyt - a}L\n")

    def tulosta_tiedot(self):
        print(f"Nimi/ID: {self.nimi}\nBensaa tankissa: {self.bensa_nyt}\nBensan maksimimäärä: {self.bensa_max}\n")

kone_1 = Lentokone("MP_LK", 150000)
kentta_1 = Lentokentta("Helsinki-Vantaa")
kentta_1.lisaa_koneita(kone_1)

kone_2 = Lentokone("ISO_KONE", 200000)
kentta_1.lisaa_koneita(kone_2)

kone_1.tankkaa(159000)
kone_2.tankkaa(50000)

kentta_1.tulosta_koneet()

print("Hei hei!")

 
         