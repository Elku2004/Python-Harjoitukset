from .hahmo import Hahmo
from random import randint
class Pelaaja(Hahmo):
    def __init__(self, nimi):
        super().__init__(nimi)
        self.score = 0
        self.no_pommi = 0
        self.tavaralista = ["Miekka", "Kilpi"]

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("Tavaralista:")
        for i in self.tavaralista:
            print(f"- {i}")
        print(f"Pisteet: {self.score}")
        
    def taistelu(self, vastustaja, loop):
        print("Tulee suuri taistelu.")
        vastustaja.hp = randint(50, 100) + 2 ** loop
        vastustaja.tulosta_tiedot()
        input()
    
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            return ""
        else:
            print(f"{self.nimi} voitti taistelun!")
            print(f"Sait esineen: {vastustaja.esine}\n")
            self.tavaralista.append(vastustaja.esine)
            self.score += vastustaja.hp
            print(f"+{vastustaja.hp} pistettä")