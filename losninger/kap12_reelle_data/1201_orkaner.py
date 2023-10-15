import numpy as np

# Definerer dataene
aar = np.arange(2005, 2016)
orkaner = [6, 4, 7, 4, 2, 8, 5, 2, 5, 2, 5]

# Initialiserer variabler for å lagre maksimalt antall orkaner og tilsvarende år
maks_orkaner = orkaner[0]
maks_aar = aar[0]

# Går gjennom dataene for å finne året med det høyeste antallet orkaner
for i in range(len(orkaner)):
    if orkaner[i] > maks_orkaner:
        maks_orkaner = orkaner[i]
        maks_aar = aar[i]

# Skriver ut resultatene
print(f"Det var flest orkaner i {maks_aar}.")
print(f"Dette året var det {maks_orkaner} orkaner.")
