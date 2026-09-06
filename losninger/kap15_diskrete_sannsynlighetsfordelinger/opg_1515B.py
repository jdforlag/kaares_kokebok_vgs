import numpy as np

n = 20        # Antall spørsmål
p = 0.25      # Sannsynlighet for å gjette riktig på ett spørsmål
elever = 800

resultater = np.random.binomial(n, p, size=elever)

bestatt = 0
for riktige in resultater:
    if riktige >= 5:
        bestatt += 1

print(f"{bestatt} av {elever} elever bestod eksamen.")
print(f"Det er en relativ frekvens på {bestatt/elever:.4f}.")
