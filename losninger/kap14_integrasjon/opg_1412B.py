import numpy as np

def f(x):
    return np.sqrt(1 - x**2)

x_min = 0
x_maks = 1
n = 230
bredde = (x_maks - x_min) / n
rekt_sum = 0

# Venstreorienterte rektangler: høyden leses av i venstre endepunkt
for i in range(n):
    x = x_min + i*bredde
    rekt_sum += f(x) * bredde

print(f"Rektangelsummen er {rekt_sum:.4f}")
print(f"Ganget med fire: {4*rekt_sum:.4f}")

# Grafen til f er den øvre halvdelen av enhetssirkelen. Området vi har
# regnet ut er derfor en kvartsirkel med radius 1. Fire slike kvartsirkler
# utgjør hele sirkelen, og arealet av en sirkel med radius 1 er pi.
print(f"Til sammenligning er pi = {np.pi:.4f}")
