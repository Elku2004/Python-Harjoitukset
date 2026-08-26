hytti = input("\nAnna hyttiluokkasi (LUX, A, B, C): ")
if hytti == "LUX" or hytti == "lux":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A" or hytti == "a":
    print(f"A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B" or hytti == "b":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C" or hytti == "c":
    print(f"C on ikkunaton hytti autokannen alapuolella.")
else:
    print(f"Virheellinen hyttiluokka")