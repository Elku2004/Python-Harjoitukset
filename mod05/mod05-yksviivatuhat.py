print(f"Tässä on kaikki kolmella jaolliset luvut välillä 1-1000")
kierros = 1
while kierros <= 1000:
    if kierros % 3 == 0:
        print(f"{kierros}")
    kierros = kierros + 1