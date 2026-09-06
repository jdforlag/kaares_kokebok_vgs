import numpy as np

def f(t):
    return 1500 / (1+4*np.e**(-0.12*t))

a = 10
b = 40
n = 600
h = (b - a) / n
summ = 0

for i in range(n):
    t1 = a + i*h        # Venstre endepunkt
    t2 = a + (i+1)*h    # Høyre endepunkt

    # Ved trapesmetoden er høyden gjennomsnittet av de to endepunktene
    hoyde = (f(t1) + f(t2)) / 2
    summ += hoyde * h

print(f"Integralet er omtrent {summ:.3f}")
