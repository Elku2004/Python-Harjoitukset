print(f"Hei käyttäjä\n")
while True:
        valinta = input("\nValitse laskutyyppi (plus, miinus tai kerto) tai syötä 'lopetus' jos tahdot lopettaa: ")
        
        if valinta == "kerto":
            numeroo = float(input("Anna numero1: "))
            numeroto = float(input("Anna numero 2: "))
            print(f"{numeroo} * {numeroto} = {numeroo * numeroto}")
        elif valinta == "miinus":
            numeroo = float(input("Anna numero1: "))
            numeroto = float(input("Anna numero 2: "))
            print(f"{numeroo} - {numeroto} = {numeroo - numeroto}")
        elif valinta == "plus":
             numeroo = float(input("Anna numero1: "))
             numeroto = float(input("Anna numero 2: "))
             print(f"{numeroo} + {numeroto} = {numeroo + numeroto}")
        elif valinta == "lopetus":
             break
        else:
             print("Kirjoititko oikein?")
print("Kiitos!")

