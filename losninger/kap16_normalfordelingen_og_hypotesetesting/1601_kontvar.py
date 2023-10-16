import numpy as np

# Antall dartkast
N = 1000

# Genererer avstander for N dartkast
avstander = np.random.uniform(0, 30, size=N)

# Beregner frekvensene for hver poengkategori
frek_100 = sum(avstander < 5)
frek_40 = sum((avstander >= 5) & (avstander < 15))  # Mellom 5 og 15
frek_10 = sum(avstander >= 15)  # Alt større eller lik 15

# Beregner total poengsum basert på frekvensene
poengsum = frek_100 * 100 + frek_40 * 40 + frek_10 * 10

# Beregner gjennomsnittlig poengsum (tilnærmet forventningsverdi for Y)
E_Y = poengsum / N

print(f"Forventet gjennomsnittlig poengsum (E(Y)): {E_Y}")
