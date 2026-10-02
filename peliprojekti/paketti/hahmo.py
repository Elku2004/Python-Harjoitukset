class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi

class Pelaaja(Hahmo):
    def __init__(self, nimi, ika):
        super().__init__(nimi)
        self.esineet = []
        self.sijainti = ""
        self.ika = ika

    def siirry(self, huone):
        self.sijainti = huone.nimi
        print(f"Olet saapunut huoneeseen: {huone.nimi}")
        input()
        huone.tapahtuma
        if huone.esine != "":
            self.saat_esineen(huone.esine)

    def saat_esineen(self, esine):
        if esine.nimi != "":
            print(f"Saat esineen: {esine.nimi}")
            self.esineet.append(esine)
            input()

#class NPC(Hahmo):
#    def __init__(self, nimi):
#        super().__init__(nimi)
#        self.relationship = 50


