lentokent = {}
while True:
    valint = input("\n1. Uusi \n2. Hae\nSyötä valintasi (tai paina Enter lopettaaksesi): ")
    valint = valint.lower()
    if valint == "":
        break
    print(f"valinta {valint}")
    if valint == "1" or valint == "uusi":
        print("\nLentokentän lisäys")
        while True:
            nimi = input("Lentokentän nimi (Tai paina enter lopettaaksesi): ")
            if nimi == "":
                break
            else:
                icao = input("Lentokentän ICAO koodi (tai enter peruuttaaksesi): ")
                if icao == "":
                    break
                else:
                    lentokent[icao.upper()] = nimi
    elif valint == "2" or valint == "hae":
        print("\nLentokentän haku")
        while True:
            icao = input("Lentokentän ICAO-koodi (Tai paina enter lopettaaksesi): ")
            if icao == "":
                break
            if icao.upper() in lentokent:
                print(f"Lentokentän ICAO koodi: {icao}\nLentokentän nimi: {lentokent[icao]}")
            else:
                print("Kirjoititko oikein?")
    else:
        print("\nKirjoititko oikein?")