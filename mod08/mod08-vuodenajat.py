talvi = (12, 1, 2)
kevat = (3, 4, 5)
kesa = (6, 7, 8)
syksy = (9, 10, 11)
while True:
    kuukaus = input("Anna kuukauden numero: ")
    if kuukaus == "":
        break
    elif int(kuukaus) in talvi:
        print("Talvi")
    elif int(kuukaus) in kevat:
        print("Kevät")
    elif int(kuukaus) in kesa:
        print("Kesä")
    elif int(kuukaus) in syksy:
        print("Syksy")
    else:
        print("Kirjoititko oikein?")
print("Hei hei!")