import matplotlib.pyplot as plt
import numpy as np

def S(x):
    """Forespørsler per sekund hos Sannheten, x sekunder etter start."""
    return 5000 * 1.001**x

def F(x):
    """Forespørsler per sekund hos Fornekteren, x sekunder etter start."""
    return 12 * 1.01**x

x = np.arange(0, 1001, 1)

plt.plot(x, S(x), label="Sannheten")
plt.plot(x, F(x), label="Fornekteren")

# Med vanlig y-akse blir Fornekteren liggende helt nede i bunnen i starten.
# Logaritmisk skala gjør at vi ser begge grafene tydelig i hele intervallet.
plt.yscale("log")

plt.grid()
plt.xlabel("Sekunder")
plt.ylabel("Forespørsler per sekund")
plt.legend()
plt.show()

# Av grafen ser vi at Fornekteren passerer Sannheten litt før 700 sekunder.
# Vi kan også finne tidspunktet med en løkke:
sekunder = 0
while F(sekunder) < S(sekunder):
    sekunder += 1

print(f"Fornekteren passerer Sannheten etter {sekunder} sekunder.")
print(f"Da har begge omtrent {S(sekunder):.0f} forespørsler per sekund.")
