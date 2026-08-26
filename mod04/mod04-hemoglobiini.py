sukup = input("Anna sinun biologinen sukupuolesi (nainen tai mies): ")
hemogl = float(input("Anna sinun hemoglobiiniarvosi: "))
sukup = sukup.lower()
if sukup == "mies":
    if hemogl > 195:
        print("Arvo on korkea.")
    if hemogl >= 134:
        print("Arvo on normaali")
    else:
        print("Arvo on matala")
elif sukup == "nainen":
    if hemogl > 175:
        print("Arvo on korkea.")
    elif hemogl > 117:
        print("Arvo on normaali.")
    else:
        print(f"Arvo on matala.")
else:
    print("Kirjoititko sukupuolesi oikein? (nainen tai mies)")