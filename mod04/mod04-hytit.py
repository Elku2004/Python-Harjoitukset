hytti = input("\nAnna hyttiluokkasi (LUX, A, B, C): ")
hytti = hytti.upper()
if hytti == "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print(f"A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print(f"C on ikkunaton hytti autokannen alapuolella.")
else:
    print(f"Virheellinen hyttiluokka")