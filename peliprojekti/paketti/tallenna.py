import json
from .hahmo import Pelaaja
from .esineet import Esine
#Ikätarkistus, joka johtaa hahmon luontiin
def aloita_luonti():
    print("\nSyötä tietosi\n")
    while True:
        nimi = input("Nimi: ")
        if nimi != "":
             break
        print("Nimi ei voi ola tyhjä!")
    while True:
        try:
            ika = int(input("Ikä (Muista ikä, Se toimii sinun tallenteesi salasanana): "))
            break
        except ValueError:
            print("Syötä numero")
    while True:
        if ika < 12:
            print("Sinun täytyy olla 12v tai yli pelataksesi")
            kayttaja = luo_kayttaja(nimi, ika, 1)
            break
        else:
            kayttaja = luo_kayttaja(nimi, ika, 1)
            break
    return kayttaja

def luo_kayttaja(nimi, ika, taso):
    kayttaja = Pelaaja(nimi, ika, taso)
    return kayttaja

def lataa_tallenne(save):
    kerrat = 0
    while True:
        try:
            salasana = int(input(f"Hei {save["Nimi"]}, anna ikäsi jatkaaksesi: "))
        except ValueError:
            print("Syötä numero")
        if salasana == save["Ika"]:
            kayttaja = Pelaaja(save["Nimi"], save["Ika"], save["Taso"])
            tavarat = save["Tavaroiden_nimet"]
            for i in tavarat:
                kayttaja.esineet.append(Esine(i, save["Varasto"][i])) 
            print("Lataus onnistui")
            input()
            return kayttaja
        else:
            print("Väärä ikä")
            kerrat += 1
            if  kerrat == 3:
                print("Kirjoitit liian monta kertaa väärin\nHei Hei!")
                exit()
                

def tallenna_peli(kayttaja):
    while True:
        num = input("Minkä tallenuksen päälle kirjoitetaan? 1-10 (tai enter peruaksesi tallentamisen): ")
        if num == "":
            break
        num = int(num)
        if 10 >= num > 0:
            varasto_tallenne = {}
            varasto_nimet = []
            for i in kayttaja.esineet:
                varasto_nimet.append(i.nimi)
                varasto_tallenne[i.nimi] = i.lause
            kayttaja_tiedot = {f"Nimi": kayttaja.nimi,
                               f"Varasto": varasto_tallenne,
                               f"Ika": kayttaja.ika,
                               f"Tavaroiden_nimet": varasto_nimet,
                               f"Taso": kayttaja.taso,
                               f"Tapaaminen": kayttaja.tapaaminen}
            with open(f"peliprojekti/paketti/save{num}.json", "w") as save:
                json.dump(kayttaja_tiedot, save)
            print("Tallennus onnistui!")
            break
        else:
            print("virheellinen numero")