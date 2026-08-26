vuosi = int(input("Anna vuosi: "))
if vuosi == 2020:
    print(f"Poikkeuksellisesti ei ollut olympialaisvuosi")
elif vuosi == 2021:
    print(f"Poikkeuksellisesti on olympialaisvuosi")
elif vuosi % 4 == 0 and 1896 < vuosi and vuosi != 1944 and vuosi != 1940 and vuosi != 1916:
    print(f"On olympialaisvuosi")
else:
    print(f"Ei ollut olympialaisvuosi")