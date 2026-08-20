print("Tämä laskee suorakulmion piirin ja pinta-alan!")
kanta = float(input("Suorakulmion kanta: "))
korkeus = float(input("Suorakulmion korkeus: "))

piiri = (kanta + korkeus) * 2
pintaala = (kanta * korkeus)

print(f"\nSuorakulmiosi piiri on {piiri}\nSuorakulmiosi pinta-ala on {pintaala}\n")
