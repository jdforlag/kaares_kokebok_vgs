import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

E_X = 0.5
SD_X = 0.5
n = 100
forsok = 5000

Y_verdier = []
for i in range(forsok):
    X_verdier = np.random.exponential(E_X, n)
    Y_verdier.append(np.mean(X_verdier))

# Sentralgrensesetningen gir forventning og standardavvik til Y
E_Y = E_X
SD_Y = SD_X / np.sqrt(n)

plt.hist(Y_verdier, bins=40, density=True, color="skyblue",
         edgecolor="black", label="Simulerte gjennomsnitt")

x = np.linspace(E_Y - 4*SD_Y, E_Y + 4*SD_Y, 200)
plt.plot(x, norm.pdf(x, E_Y, SD_Y), color="red", label="Normalfordeling")

plt.xlabel("Gjennomsnittlig ventetid (minutter)")
plt.ylabel("Sannsynlighetstetthet")
plt.legend()
plt.show()

print(f"E(Y) = {E_Y}, SD(Y) = {SD_Y}")
print(f"Simulert gjennomsnitt: {np.mean(Y_verdier):.4f}")
