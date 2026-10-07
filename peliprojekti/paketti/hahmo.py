class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi

class Pelaaja(Hahmo):
    def __init__(self, nimi, ika, taso):
        super().__init__(nimi)
        self.esineet = []
        self.ika = ika
        self.alaikainen = False
        #Jos alaikäinen, et voi pelata ollenkaan
        if self.ika < 12:
            self.alaikainen = True
        self.taso = taso
        self.tapaaminen = 0

    def kerata(self, esine):
        print(f"Saat esineen: {esine.nimi}")
        self.esineet.append(esine)