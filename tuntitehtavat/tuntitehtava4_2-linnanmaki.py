pituus = int(input("Anna sinun pituus (cm): "))
ika = int(input("Anna sinun ikä: "))

if pituus >= 195 and ika >= 8:
    print(f"Saat mennä kaikkiin laitteisiin paitsi kirnuun.")
elif pituus >= 195 and ika < 8:
    print(f"Vastasitko oikein? Sinun ikäsi on {ika}v. ja pituus on {pituus}cm.")
elif pituus >= 140:
    if ika >= 8:
        print(f"Saat mennä kaikkiin laitteisiin.")
    else:
        print(f"Saat mennä kaikkiin laitteisiin paitsi Tulirekeen.")
elif pituus >= 100:
    print(f"Saat mennä lasten laitteisiin.")
else:
    print(f"Et saa mennä laitteisiin.")