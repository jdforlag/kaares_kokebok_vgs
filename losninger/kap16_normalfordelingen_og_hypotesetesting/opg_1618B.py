import numpy as np
from scipy.stats import norm

n = 1_200_000
p = 0.002
defekte = 2500
signifikansnivaa = 0.05

# Nullhypotese H0:      p = 0,002. Defektraten er slik fabrikken hevder.
# Alternativ hypotese:  p > 0,002. Defektraten er større.

E_X = n * p
SD_X = np.sqrt(n * p * (1-p))
print(f"E(X) = {E_X}")
print(f"SD(X) = {SD_X:.2f}")

# p-verdien er sannsynligheten for å få minst så mange defekte som
# Trysilfjell observerte, dersom nullhypotesen er sann
p_verdi = 1 - norm.cdf(defekte, E_X, SD_X)
print(f"p-verdi: {p_verdi:.5f}")

if p_verdi <= signifikansnivaa:
    print("Nullhypotesen forkastes.")
    print("Trysilfjell Teknologi har grunnlag for anklagen sin.")
else:
    print("Nullhypotesen beholdes.")
    print("Trysilfjell Teknologi har ikke grunnlag for anklagen sin.")
