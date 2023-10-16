import numpy as np
from scipy.stats import binom

# Definerer parametere
n = 10  # Antall egg
p = 0.85  # Sannsynlighet for at et egg klekker
k = 8  # Antall suksesser (egg som klekker)

# Regner ut sannsynligheten P(X = k)
sanns_k = binom.pmf(k, n, p)
print(f"P(X = {k}) = {sanns_k:.3f}")

# Regner ut sannsynligheten P(X <= k)
sanns_til_k = binom.cdf(k, n, p)
print(f"P(X <= {k}) = {sanns_til_k:.3f}")

# Regner ut sannsynligheten P(X > k) = 1 - P(X <= k)
sanns_over_k = 1 - sanns_til_k
print(f"P(X > {k}) = {sanns_over_k:.3f}")

# For et større antall egg
n_stor = 150
k1 = 50
k2 = 120

# Regner ut sannsynligheten P(50 < X <= 120) for det større antallet egg
# P(50 < X <= 120) = P(X <= 120) - P(X <= 50)
sanns_mellom = binom.cdf(k2, n_stor, p) - binom.cdf(k1, n_stor, p)
print(f"P({k1} < X <= {k2}) = {sanns_mellom:.3f}")
