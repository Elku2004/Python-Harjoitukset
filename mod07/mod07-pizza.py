import math
def yksikkohinta (halk=1, hinta=1):
    vast = hinta/(halk/200*math.pi)
    return vast

pizzat = []
for i in range (2):
    print(f"Pizza {i+1}.")
    halkaisija = input("Anna pizzan halkaisija (cm): ")
    pizhinta = input("Anna pizzan hinta (€): ")
    pizzat.append(yksikkohinta(float(halkaisija), float(pizhinta)))

print(f"\nPizza 1. {pizzat[0]:.3f}€/m^2\nPizza 2. {pizzat[1]:.3f}€/m^2\n")
if pizzat[0] == pizzat[1]:
    print("Pizzat antavat yhtä hyvän vastineen rahallenne.")
elif pizzat[0] > pizzat[1]:
    print("Pizza 1 antaa paremman vastineen.")
else:
    print("Pizza 2 antaa paremman vastineen.")

