tuuma = 0
while tuuma >= 0:
    tuuma = float(input("Anna tuumamäärä: "))
    if tuuma >= 0:
        print(f"{tuuma:.0f} tuumaa on {tuuma * 2.54}cm")
    else:
        break
print("Hei hei!")