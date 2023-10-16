import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Definerer parametere for normalfordelingen
mu = 74  # Forventningsverdi 74 km/t
sigma = 6  # Standardavvik 6 km/t
n = 200  # Antall målinger

# Genererer tilfeldige data basert på normalfordelingen
maalinger = np.random.normal(loc=mu, scale=sigma, size=n)

# Oppretter et histogram for de simulerte dataene
plt.hist(maalinger, bins=30, density=True, color="skyblue", edgecolor="black", alpha=0.7, label="Simulerte data")

# Beregner og tegner normalfordelingskurven
x_start = mu - 3*sigma
x_slutt = mu + 3*sigma
x = np.linspace(x_start, x_slutt, 100)
f = norm.pdf(x, mu, sigma)
plt.plot(x, f, color="darkblue", label="Normalfordeling")

# Legger til en vertikal linje som indikerer gjennomsnittet
plt.axvline(x=mu, color="orange", linestyle="--", label="Forventningsverdien")

# Legger til nødvendige etiketter og tittelen
plt.title("Histogram over fartsmålinger med normalfordelingskurve")
plt.xlabel("Fart (km/t)")
plt.ylabel("Sannsynlighetstetthet")
plt.legend()  # Viser boks med forklaringer på grafikken

# Viser plottet
plt.show()
