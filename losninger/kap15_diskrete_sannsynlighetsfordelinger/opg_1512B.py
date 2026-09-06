import numpy as np

verdier = [-2, 1, 3]
sanns = [0.1, 0.2, 0.7]

utfallene = np.random.choice(verdier, p=sanns, size=1000)
gjennomsnitt = np.mean(utfallene)

print(f"Gjennomsnittet av 1000 forsøk er {gjennomsnitt:.4f}")

# Til sammenligning er forventningsverdien
E_X = -2*0.1 + 1*0.2 + 3*0.7
print(f"E(X) = {E_X}")
