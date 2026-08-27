nimi = input("Anna nimi: ")
salasana = input("Anna salasana: ")
yritys = 1
while nimi != "python" and salasana != "rules":
    yritys = yritys + 1
    print("Nimi tai salasana on väärin! Yritä uudelleen")
    nimi = input("Anna nimi: ")
    salasana = input("Anna salasana: ")
    if yritys >= 5:
        print("Pääsy evätty!")
        break
else:
    print("Tervetuloa!")
