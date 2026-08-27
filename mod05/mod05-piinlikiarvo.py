import math
import random
pistmaara = int(input("Anna arvottavien pisteiden määrä: "))
kierros = 0
n = 0
while kierros != pistmaara:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x ** 2 + y ** 2 < 1:
        n = n + 1
    kierros = kierros + 1
print(f"Piin likiarvo on {4*n/kierros}")
