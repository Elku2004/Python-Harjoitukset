from .esineet import Esine
from .hahmo import NPC
def valitse(x):
    print(f"{x}")
    while True:
        try:
            valint = int(input())
            return valint
        except ValueError:
            print("Syötä numero")

def taso_1(kayttaja):
    print("Istut järven rannalla, kuten yleensä. Järven kohina rauhoittaa, mutta jokin painaa sinun mieltäsi.\n"
          "Vesistöt eivät ole enää samanlaisia kuin ennen. Pinta on tummentunut ja likaisempi kuin ennen. ")
    input()
    print("Päätit, että aiot ratkaista kenen syytä vesistön pilaantuminen on")
    input()
    valint = valitse(f"Haluatko: \n1. Tutkia ympäristöä \n2. Lähde suorinta tietä kaupunkiin")
    if valint == 1:
        print("Ympärilläsi on paljon puita, joista lehdet putoilevat. Lehtien seasta huomaat jotain")
        input()
        print("Löysit kymmeniä tynnyreitä, jotka valuttavat roskia veteen! Sen vierestä löydät kengän, jonka koko on 60.")
        kayttaja.esineet.append(Esine("Iso Kenkä", "Esität aineistossa kengän, jonka koko voi olla pikkukylänne sisällä vain viidellä henkilöllä!"))
        input()
    elif valint == 2:
        pass
    print("Jatkat polulla kylään päin. Kuulet puskista rapinaa")
    input()
    valint = valitse(f"1. Lähesty äänen lähdettä \n2. Nopeasti karkuun")

    if valint == 1:
        print("Lähestyt ääntä ja kuulet" \
        "'Uhargghhhhh'")
        print("HIRVIÖ?!")
        valint = ""
        valint = valitse(f"1. Karkaa\n2. Jää katsomaan")
        if valint == 1:
            print("Juokset kaupunkiin!")
            input()
        elif valint == 2:
            print("Jäät katsomaan ja tajuat että kyseessä onkin kylän kalamyyjä!\n" \
            "Hän oli tippunut likaiseen veteen, joten saatat hänet puhtaan veden luokse, että hän voi peseytyä")
            input()
            print("'Kiitos paljon!' hän sanoo. Kerrot hänelle tutkivasi veden tapausta. 'Ai että tutkit...'")
            input()
            print("'Olin juuri jonkin jäljillä, mutta joku työnsi minut veteen!'\n" \
            "'Huomasin että hänellä oli erittäin pienet ja pehmeät kädet...'\n" \
            "'Tässä! Saat numeroni, jotta voit kutsua minut jos löydät syyllisen!'")
            kayttaja.esineet.append(Esine("Kalamyyjän Numero", "Kutsut kalamyyjän todistamaan. Hän kuvailee tapahtumia parhaansa mukaan"))
            input()
    print("Ja pian saavut kylään...")
    input()
    kayttaja.taso += 1
    print("Ensimmäinen taso läpi!\n")

def taso_2(kayttaja):
    print("Kaupungin portilla, koet että sinulla on kaksi vaihtoehtoa, muttei tarpeeksi aikaa jokaiseen,\n" \
    "jos haluat selvittää tämän pulman tänään")
    valint = valitse(f"1. Tutki katuja \n2. Kotiin lepäämään")
    if valint == 1:
        print("Kävellessä kotikyläsi kaduilla, huomaat roskia polulla. Kävelet niiden luokse ja huomaat niiden muodostavan polun")
        input()
        print("Tietysti seuraat polkua!")
        input()
        print("Polun päädyssä huomaat kaavun, joka on pudonnut maahan. Se lemuaa ja on likainen, kuten järven vesi"
              "\nKeräät sen todistusaineistoksi, jolloin huomaat sen sisältävän nimikirjaimet 'JP'")
        input()
        print("Takaasi kuulet huudon: 'LASKE KAAPU ALAS!!', ja juoksuaskelia selkäsi takaa")
        valint = valitse(f"1. Pysähdy ja odota\n2. Juokse karkuun")
        if valint == 1:
            print("Katsot taaksesi ja huomaat kaljun, harteikkaan miehen. Hän saavuttaa sinut ja sanoo: 'Palauta kaapu heti'\n"
                  "Sinulle se on kriittistä todistusaineistoa, etkä voi luopua siitä")
            valint = valitse(f"1. Harhautus\n2. Juokse")
            if valint == 1:
                print("Kun hän ei huomaa, heität kiven hänen takana olevaan ikkunaan\n"
                      "Hän katsoo sinua")
                input()
                print("Mutta hetken päästä katsoo taaksepäin kauhuissaan!\n"
                "Suunnitelmasi onnistui ja seuraat parasta mahdollista reittiä pois\n"
                "Hän ei aavistanut mitään")
                kayttaja.esineet.append(Esine("Musta kaapu", "Näytät mustan kaavun, jossa on nimikirjaimet JP. Kylässänne ei ole montaa samannimistä henkilöä"))
            if valint == 2:
                print("Juokset karkuun, mutta kaapu ottaa kiinni aidasta ja repeytyy. Et pysty ottamaan sitä mukaasi")
        elif valint == 2:
            print("Juokset karkuun, mutta kaapu ottaa kiinni aidasta ja repeytyy. Et pysty ottamaan sitä mukaasi")
    else:
        print("Palaat kotiisi lepäämään sen sijaan että ratkaisisit mysteerin\n"
        "Uuden tiedon määrä on ollut sinulle liian raskasta ja tahdot ottaa pienen tauon")
        input()
        print("Heräät muutaman tunnin päästä ja satut näkemään ulkona henkilön pukeutuneena mustaan kaapuun\n" \
        "Hänen kaavussaan on samanlaista roskaa, mitä näit vedessä rannalta")
        input()
        print("Hän kääntyy vain hetkeksi ja huomatessaan sinut kääntää päänsä äkkiä takaisin\n"
              "mutta huomaat, että hänellä on tuuheat viikset!")
        print("Kuka hän voisi olla?")
    print("Aika on vähissä, joten sinun täytyy näyttää poliisille, mitä olet löytänyt")

def taso_3(kayttaja):
    pass

def taso(kayttaja, num):
    if num == 1:
        taso_1(kayttaja)
    elif num == 2:
        taso_2(kayttaja)
    elif num == 3:
        taso_3(kayttaja)
    else:
        print("Pelasit pelin jo läpi!")
        valint = valitse("Anna aiemman tason numero, johon haluat palata (Tai paina ENTER palataksesi): ")
        if 1 <= valint <= 3:
            kayttaja.taso = valint
        else:
            pass