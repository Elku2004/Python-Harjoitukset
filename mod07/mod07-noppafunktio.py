import random
def noppa(luku):
    n = random.randint(1,luku)
    return n

arvo = 0
sivut = int(input("Kuinka monta sivua nopassasi on?: "))
while True:
    arvo = noppa(sivut)
    if arvo == sivut:
        print(f"{arvo}!")
        break
    else:
        print(arvo)
    
