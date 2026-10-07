from .esineet import Esine
from .tallenna import tallenna_peli
def valitse(x):
    print(f"{x}")
    while True:
        try:
            valint = int(input())
            return valint
        except ValueError:
            print("Syötä numero")

def valitse_alku(x, num):
    while True:
        valint = valitse(x)    
        if valint in num:
            return valint
        else:
            print("Vastasitko oikein?")

def oveen_paukutus(kiire: int):
    if kiire > 4:
        print("Kalju mies juoksee ovesta läpi kaiken paukuttamisen jälkeen ja vie sinut mukanaan\n" \
              "Sinun päähäsi laitetaan huppu etkä tiedä mihin olet matkalla\n"
              "Perillä, sinun muistisi pyyhitään, etkä muista enää koko päiväsi tapahtumia...")
        print("The End")
        exit()
    kiire += 1
    print("Paukutus jatkuu...")
    return kiire

#Pelissä on 3 tasoa
def taso_1(kayttaja):
    print("Istut järven rannalla, kuten yleensä. Järven kohina rauhoittaa, mutta jokin painaa sinun mieltäsi.\n"
          "Vesistöt eivät ole enää samanlaisia kuin ennen. Pinta on tummentunut ja likaisempi kuin ennen. ")
    input()
    print("Päätit, että aiot ratkaista kenen syytä vesistön pilaantuminen on")
    input()
    valint = valitse_alku("Haluatko: \n1. Tutkia ympäristöä \n2. Lähde suorinta tietä kaupunkiin", (1,2))
    if valint == 1:
        print("Ympärilläsi on paljon puita, joista lehdet putoilevat. Lehtien seasta huomaat jotain")
        input()
        print("Löysit kymmeniä tynnyreitä, jotka valuttavat roskia veteen! Sen vierestä löydät kengän, jonka koko on 60.")
        kayttaja.kerata(Esine("Iso Kenkä", "Esität aineistossa kengän, jonka koko voi olla pikkukylänne sisällä vain viidellä henkilöllä!"))
        input()
    elif valint == 2:
        pass
    print("Jatkat polulla kylään päin. Kuulet puskista rapinaa")
    input()
    valint = valitse_alku("1. Lähesty äänen lähdettä \n2. Nopeasti karkuun",(1,2))

    if valint == 1:
        print("Lähestyt ääntä ja kuulet" \
        "'Uhargghhhhh'")
        print("HIRVIÖ?!")
        valint = ""
        valint = valitse_alku("1. Karkaa\n2. Jää katsomaan", (1,2))
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
            kayttaja.kerata(Esine("Kalamyyjän Numero", "Kutsut kalamyyjän todistamaan. Hän kuvailee tapahtumia parhaansa mukaan."
                                                       "\nSitten hän lähtee nopeasti maksamaan verojaan, jotka EI OLE UNOHTUNUT"))
            input()
    print("Ja pian saavut kylään...")
    input()
    kayttaja.taso += 1
    print("Ensimmäinen taso läpi!\n")

def taso_2(kayttaja):
    print("Kaupungin portilla, koet että sinulla on kaksi vaihtoehtoa, muttei tarpeeksi aikaa jokaiseen,\n" \
    "jos haluat selvittää tämän pulman tänään")
    valint = valitse_alku("1. Tutki katuja \n2. Kotiin lepäämään",(1,2))
    if valint == 1:
        print("Kiertelet katuja muutaman tunnin ja huomaat roskia polulla. Kävelet niiden luokse ja huomaat niiden muodostavan polun")
        input()
        print("Tietysti seuraat polkua!")
        input()
        print("Polun päädyssä huomaat kaavun, joka on pudonnut maahan. Se lemuaa ja on likainen, kuten järven vesi"
              "\nKeräät sen todistusaineistoksi, jolloin huomaat sen sisältävän nimikirjaimet 'JP'")
        input()
        print("Takaasi kuulet huudon: 'LASKE KAAPU ALAS!!', ja juoksuaskelia selkäsi takaa")
        valint = valitse_alku("1. Pysähdy ja odota\n2. Juokse karkuun",(1,2))
        if valint == 1:
            print("Katsot taaksesi ja huomaat kaljun, harteikkaan miehen. Hän saavuttaa sinut ja sanoo: 'Palauta kaapu heti'\n"
                  "Sinulle se on kriittistä todistusaineistoa, etkä voi luopua siitä")
            kayttaja.tapaaminen = 1
            valint = valitse_alku("1. Harhautus\n2. Juokse",(1,2))
            if valint == 1:
                print("Kun hän ei huomaa, heität kiven hänen takana olevaan ikkunaan\n"
                      "Hän katsoo sinua")
                input()
                print("Mutta hetken päästä katsoo taaksepäin kauhuissaan!\n"
                "Suunnitelmasi onnistui ja seuraat parasta mahdollista reittiä pois\n"
                "Hän ei aavistanut mitään")
                kayttaja.kerata(Esine("Musta kaapu", "Näytät mustan kaavun, jossa on nimikirjaimet JP. Kylässänne ei ole montaa samannimistä henkilöä"))
                input()
            if valint == 2:
                print("Juokset karkuun, mutta kaapu ottaa kiinni aidasta ja repeytyy. Et pysty ottamaan sitä mukaasi")
                input()
        elif valint == 2:
            print("Juokset karkuun, mutta kaapu ottaa kiinni aidasta ja repeytyy. Et pysty ottamaan sitä mukaasi")
            input()
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
        input()
    print("Aika on vähissä, joten sinun täytyy näyttää poliisille, mitä olet löytänyt")
    kayttaja.taso += 1
    print("Toinen taso läpi!")
    input()

def taso_3(kayttaja):
    print(f"Saavut poliisiasemalle.\n{kayttaja.nimi}, tämä on tarinan päätepysäkki ja tehtäväsi on päättää ja todistaa,"
          "\nkuka on roskaamisen takana?")
    input()
    print("Saavut ovelle")
    valint = valitse_alku("1. Astu sisään\n2. Käänny ympäri",(1,2))
    if valint == 2:
        print("Käännyt ympäri ja kävelet hitaasti asunnollesi."
              "\nTämä pulma oli liikaa sinulle tänään, etkä pysty viemään sitä vielä loppuun saakka"
              "\nKokeilet ehkä myöhemmin uudelleen")
        input()
    elif valint == 1:
        print("Astut sisään ja...")
        input()
        print("Täällä on hiljaista, kuten yleensä\n" \
              "Kylänne on pieni, joten 'Poliisiasema' on todellisuudessa vain pieni toimisto\n" \
              "Paikalla on kaupungin vanhempi poliisi, Pekka")
        valint = valitse_alku("1. 'Hei Pekka, mulla on sulle jotain'\n2. 'Moro moro mite menee my guy'", (1,2))
        if valint == 1:
            print("'Hei Pekka, mulla on sulle jotain'")
        if valint == 2:
            print("'Moro moro mite menee my guy'")
        input()
        print("'Aa katsos kukas se siinä!' Pekka sanoo ja nousee ylös tuolistaan\nHän kävelee luoksesi")
        input()
        print("Ojennat hänelle sinun todistusaineistosi")
        pisteet = 0
        for i in kayttaja.esineet:
            print(f"{i.lause}")
            pisteet += 1
            input()
        print("Vai niin...")
        input()
        if pisteet > 1:
            print("'Hmmm... Tämäpä mielenkiintoista' Pekka sanoo ja kävelee pöytänsä taakse\nHän kaivaa sieltä kuvan")
            input()
            print("'Kyseessä on kylän pormestari Jaakko Paakko'\n" \
            "'Lakitaistelu tulee olemaan pitkä, mutta näiden todisteiden avulla, saamme hänet kiinni'" \
            "'Aikanaan...'")
            input()
            print("Pekka kävelee takapihalle, mutta sinä päätät jäädä pitkän päivän jälkeen hetkeksi istumaan.")
            input()
            print("Joku koputtaa ovella")
            print("Menet katsomaan ovisilmän läpi ja huomaat että ulkona on kalju mies")
            if kayttaja.tapaaminen == 1:
                print("Tunnistat hänet samana henkilönä, joka yritti saada sinulta mustan kaavun aiemmin")
            input()
            print("'OVI AUKI TAI MURRAN SEN'")
            kiire = 0
            kutsu = False
            Megafoni = False
            while True:
                valint = valitse_alku("1. Kokeile takaovea\n2. Kutsu Pekkaa\n3. Katso pöydän taakse",(1,2,3))
                if valint == 1:
                    if kutsu == False:
                        print("Ovi ei aukea")
                        input()
                        kiire = oveen_paukutus(kiire)
                        input()
                    elif kutsu == True:
                        print("Ovi aukeaa ja pääset ulos")
                        break
                if valint == 2:
                    if Megafoni == False:
                        print("Pekka ei kuule sinua, seinät ovat liian paksut")
                        input()
                        kiire = oveen_paukutus(kiire)
                        input()
                    elif Megafoni == True:
                        print("Kuulostaa siltä että joku avasi oven!")
                        kutsu = True
                        input()
                if valint == 3: 
                    print("Löydät pöydän takaa megafonin! Voisit varmaan käyttää sitä...")
                    input()
                    Megafoni = True
            print("Juokset ovesta ulos ja Pekka juoksee taas sisälle\n" \
                  "Mysteerinen kalju mies jää kiinni ja käy ilmi, että hän työskentelee Jaakko Paakolle\n")
        input()
        if pisteet >= 3:
            print("Todisteittesi ansiosta, Jaakko Paakko pystytään pidättämään ja erottamaan hänen virastaan")
        elif pisteet == 2:
            print("Jaakko Paakko saa tuomion, mutta pysyy virassaan. Täytyy toivoa että hän korjaa tapansa")
        else:
            print("Todistusaineistosi ei riittäneet todistamaan mitään\n" \
            "Unohditko tavoitteesi?"
            "Mitä olisit voinut tehdä toisin?")
        input()
        print("------The End------")
        input()
        kayttaja.taso += 1
        print("Voit nyt aikamatkustaa aiempiin tasoihin valitsemalla 'Aloita/Jatka' vaihtoehdon valikosta")
        input()    

#Mikä "Taso" pitää käydä läpi
def taso(kayttaja, num):
    if num == 1:
        taso_1(kayttaja)
        valint = valitse_alku("Haluatko tallentaa pelin? (1. kyllä, 2. ei)", (1,2))
        if valint == 1:
            tallenna_peli(kayttaja)
            input()
    elif num == 2:
        taso_2(kayttaja)
        valint = valitse_alku("Haluatko tallentaa pelin? (1. kyllä, 2. ei)", (1,2))
        if valint == 1:
            tallenna_peli(kayttaja)
            input()
    elif num == 3:
        taso_3(kayttaja)
        valint = valitse_alku("Haluatko tallentaa pelin? (1. kyllä, 2. ei)", (1,2))
        if valint == 1:
            tallenna_peli(kayttaja)
            input()
    #Uudelleenvalitse aiemmin suoritettu taso
    else:
        print("Pelasit pelin jo läpi!")
        valint = valitse("Anna aiemman tason numero, johon haluat palata (4 tai enemmän pysyäksesi tässä vaiheessa): ")
        if 1 <= valint <= 3:
            kayttaja.taso = valint
            print("'Jatka' peliä pelataksesi valitsemasi taso uudestaan")
        else:
            pass