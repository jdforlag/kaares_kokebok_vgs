import matplotlib.pyplot as plt
import numpy as np

n = 10
p = 0.228
N = 70
dode_liste = [ ]

for _ in range(N):
    dode = np.random.binomial(n, p)
    dode_liste.append(dode)

# Grensene legges midt mellom heltallene, slik at hver stolpe
# tilsvarer nøyaktig ett antall dødsfall
hist_grenser = np.arange(-0.5, n+1)

plt.hist(dode_liste, bins=hist_grenser, edgecolor="black")
plt.xlabel("Antall dødsfall")
plt.ylabel("Antall forsøk")
plt.title(f"Stolpediagram. {N} forsøk.")
plt.show()
