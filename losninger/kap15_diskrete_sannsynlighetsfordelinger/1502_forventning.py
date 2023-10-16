import numpy as np

# Definerer verdier og deres tilsvarende sannsynligheter
verdier = [0, 5, 10]
sanns = [1/3, 1/2, 1/6]

# Beregner forventningsverdien
ex = 0
for i in range(3):
    ex += verdier[i] * sanns[i]

print(f"E(X) = {ex:.4f}")  # Skriver ut forventningsverdien

# Starter simuleringen med ulike antall forsøk
for n in range(100, 8001, 100):
    gevinster = np.random.choice(verdier, p=sanns, size=n)
    gjsnitt = np.sum(gevinster) / n  # Beregner gjennomsnittlig gevinst

    # Beregner avviket mellom forventet og faktisk gjennomsnittlig gevinst
    avvik = abs(ex - gjsnitt)
    print(f"Gevinst: {gjsnitt:.4f} kr. Forsøk: {n}. Avvik: {avvik:.4f}")
