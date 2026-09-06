import matplotlib.pyplot as plt
import numpy as np

n = 10       # Antall klatrere
p = 0.228    # Dødsraten
N = 70       # Antall simuleringer
dode_liste = [ ]

for _ in range(N):
    # Bruk np.random.binomial for å kjøre ett forsøk
    dode = np.random.binomial(n, p)
    # Legg til antall døde i lista dode_liste
    dode_liste.append(dode)

plt.plot(dode_liste, "o")
plt.xlabel("Forsøknummer")
plt.ylabel("Antall dødsfall")
plt.title(f"Spredningsdiagram. {N} forsøk.")
plt.show()
