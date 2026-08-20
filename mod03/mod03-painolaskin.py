float(luoti = 13,3)
naula = luoti * 32
levi = naula * 20

print("Kerro painomäärä keskiaikaisten mittojen mukaan!")

HenkLev = float(input("Anna Leviskät: "))
HenkNau = float(input("Anna Naulat: "))
HenkLuo = float(input("Anna Luodit: "))


gram = HenkLuo * luoti + HenkNau * luoti * 32 +  HenkLev * luoti * 32 *20
kilo = gram / 1000

print(f"Grammoina {gram} ja Kilogrammoina {kilo}")
