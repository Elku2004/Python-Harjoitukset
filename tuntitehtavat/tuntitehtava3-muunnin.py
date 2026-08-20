gramma = float(input("Tämä ohjelma muuntaa grammat kilogrammoiksi \nKuinka monta grammaa: "))

kilot = gramma // 1000
gramma2 = gramma % 1000

print(f"Määrä kiloina ja grammoina: {kilot:.0f} kg ja {gramma2:.0f} g")