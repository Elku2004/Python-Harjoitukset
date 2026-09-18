class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):

    def __init__ (self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)


    def tulosta_tiedot (self):
        print(f"Nimi: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivut}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot (self):
        print(f"Nimi: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")

Aku_Ankka = Lehti("Aku Ankka", "Aki Hyyppä")
Hytti_No_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
Aku_Ankka.tulosta_tiedot()
Hytti_No_6.tulosta_tiedot()