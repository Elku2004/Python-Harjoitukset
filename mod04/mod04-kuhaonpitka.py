kuhapit = float(input("\nAnna kuhan pituus: "))

if kuhapit >= 37:
    print(f"Kuha on sopivan mittainen ja voit pitää kuhan!\n")
else:
    print(f"Päästä kuha vapaaksi. Kuha on {37 - kuhapit} alamittainen.\n")