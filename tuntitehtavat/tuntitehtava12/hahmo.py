from random import randint
class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = randint(50, 100)

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")