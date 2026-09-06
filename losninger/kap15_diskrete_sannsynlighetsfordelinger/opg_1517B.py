import matplotlib.pyplot as plt
import numpy as np

n = 10_000   # Antall skjermkort i ett forsøk
p = 0.05     # Andelen defekte
N = 5000     # Antall forsøk

utfall = np.random.binomial(n, p, size=N)

# Den kumulative summen delt på forsøksnummeret gir gjennomsnittet så langt
kumulativ_sum = np.cumsum(utfall)
forsok_nr = np.arange(1, N+1)
gjsnitt_verdier = kumulativ_sum / forsok_nr

E_X = n * p   # 500

plt.plot(forsok_nr, gjsnitt_verdier, label="Gjennomsnitt så langt")
plt.axhline(y=E_X, color="r", linestyle="--", label="E(X) = 500")
plt.xlabel("Antall forsøk")
plt.ylabel("Gjennomsnittlig antall defekte")
plt.legend()
plt.grid()
plt.show()

print(f"Etter {N} forsøk er gjennomsnittet {gjsnitt_verdier[-1]:.2f}")
