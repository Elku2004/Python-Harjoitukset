Nimi = input("\nAnna päähahmosi nimi: ")
print(f"\n{Nimi} on urhea soturi. Hän saapuu tuntemattomaan kylään ja hänelle on annettu käsky hyökätä")
valinta = input("\nValitse sota tai rauha: ")
if valinta == "sota":
    print(f"{Nimi} hyökkäsi viattomien kimppuun. Kylä vastasi ja päihitti hänet")
elif valinta == "rauha":
    print(f"{Nimi} teki sopimuksen kylän kanssa ja jäi elämään sinne, vapaana sodasta. Hän eli rauhallisesti loppuun")
else:
    print(f"Virheellinen valinta")

