import matplotlib.pyplot as plt
from scipy.stats import binom, norm  # Oppdatert importering
import numpy as np

# Antall terningkast og sannsynligheten for å få en sekser
n = 30  # Oppdatert til 30 for denne kjøringen
p = 1/6

# Beregning av forventningsverdi og standardavvik
ex = n * p
sdx = np.sqrt(n * p * (1 - p))  # Korrigert formel

# Genererer x-verdier og tetthetsfunksjonen for normalfordelingen
x_verdier = np.linspace(ex - 3 * sdx, ex + 3 * sdx, 100)
f_verdier = norm.pdf(x_verdier, ex, sdx)  # Bruker pdf-funksjonen for normalfordeling

# Utfall og sannsynligheter for binomisk fordeling
utfall = np.arange(0, n + 1)
sanns = binom.pmf(utfall, n, p)

# Plotting av stolpediagram og normalfordelingskurve
plt.figure(figsize=(10, 6))
plt.bar(utfall, sanns, label="Binomisk fordeling")
plt.plot(x_verdier, f_verdier, color="red", label="Normalfordeling")  # Normalfordelingskurven
plt.xlim(min(x_verdier), max(x_verdier))  # Justerer x-aksens grenser
plt.xlabel("Antall seksere")
plt.ylabel("Sannsynlighet")
plt.title(f"Sannsynlighetsfordeling for {n} terningkast")
plt.legend()  # Viser forklaringene
plt.show()

# For å kjøre med 1200 terninger, endre n til 1200 og kjør koden på nytt.
