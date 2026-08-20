luoti = 13.3

print("Kerro painomäärä keskiaikaisten mittojen mukaan!")

HenkLev = float(input("Anna Leviskät: "))
HenkNau = float(input("Anna Naulat: "))
HenkLuo = float(input("Anna Luodit: "))

grammat = (HenkLuo * luoti + HenkNau * luoti * 32 +  HenkLev * luoti * 32 *20)
kilo = int(grammat // 1000)
gram = int(grammat % 1000)

print(f"Paino on {kilo} kg ja {gram} g (eli {grammat:.0f} g)")
