def jaottelu (luvut):
    s = []
    for i in luvut:
        if i % 2 == 0:
            s.append(i)
    return s

parsimaton = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    parsimaton.append(int(luku))
parilliset = jaottelu(parsimaton)

print(f"Alkuperäinen\n{parsimaton}\nVain parilliset\n{parilliset}")