import numpy as np

n = 5      # Antall skudd i en serie
p = 0.85   # Treffraten
N = 100    # Antall skuddserier

resultater = np.random.binomial(n, p, size=N)
treff = sum(resultater)
print("Antall treff:", treff)

# Til sammen er det N*n skudd, så antall bom finner vi slik:
bom = N*n - treff
print("Antall bom:", bom)
