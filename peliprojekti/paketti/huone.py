class Huone:
    def __init__(self, nimi, esine, kuvaus):
        self.nimi = nimi
        self.esine = esine
        self.kuvaus = kuvaus
        
    def tapahtuma(self):
        print(self.kuvaus)