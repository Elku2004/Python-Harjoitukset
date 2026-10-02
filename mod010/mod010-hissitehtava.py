from time import sleep
class Talo:
    def __init__ (self, ylinkrs, alinkrs, hissi_määrä):
            self.ylinkrs = ylinkrs
            self.alinkrs = alinkrs
            hissit = []
            for i in range (hissi_määrä):
                 hissit.append(Hissi(self.ylinkrs, self.alinkrs))
            self.hissit = hissit
            
    def aja_hissia (self, hissi, kerros):
          self.hissit[hissi-1].siirry_kerrokseen(kerros)

    def palohalytys (self):
          print("Palohälytys!")
          for i in range(len(self.hissit)):
                self.hissit[i].siirry_kerrokseen(self.alinkrs)

class Hissi:
    def __init__ (self, ylinkrs, alinkrs):
        self.ylinkerros = ylinkrs
        self.alinkerros = alinkrs
        self.nyt_kerros = alinkrs

    def siirry_kerrokseen (self, kerros):
        print(f"Olet nyt kerroksessa {self.nyt_kerros}")
        if kerros > self.nyt_kerros:
                self.kerros_ylös(kerros)
        elif kerros < self.nyt_kerros:
                self.kerros_alas(kerros)
        print("Olet kerroksessasi!")

    def kerros_ylös (self, kerros):
            while kerros !=  self.nyt_kerros:
                self.nyt_kerros += 1
                print(f"Kerros {self.nyt_kerros}")
                sleep(0.5)

    def kerros_alas (self, kerros):
            while kerros !=  self.nyt_kerros:
                self.nyt_kerros -= 1
                print(f"Kerros {self.nyt_kerros}")
                sleep(0.5)


talo_1 = Talo(10,1,3)
talo_1.aja_hissia(1,5)
sleep(1)
talo_1.aja_hissia(2,4)
sleep(1)
talo_1.aja_hissia(1,10)
sleep(1)
talo_1.palohalytys()