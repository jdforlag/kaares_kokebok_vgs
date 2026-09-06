import numpy as np

n = 200    # Antall straffespark
p = 0.72   # Suksessraten

mal = np.random.binomial(n, p)

print(f"Han scoret {mal} mål av {n} straffespark.")
