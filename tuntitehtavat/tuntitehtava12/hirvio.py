from .hahmo import Hahmo
class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki, esine):
        super().__init__(nimi)
        self.repliikki = repliikki
        self.esine = esine

    def tulosta_tiedot(self):
        print(self.repliikki)
        super().tulosta_tiedot()