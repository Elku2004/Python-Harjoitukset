kaupungit = []
print("\n")
for n in range (1,6):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)
print("\n")
for n in range(1,len(kaupungit)+1):
    print(f"{kaupungit[n-1]}")