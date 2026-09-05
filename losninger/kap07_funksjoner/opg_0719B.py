from tabulate import tabulate
import numpy as np

def k(x):
    return 0.3*x**2 + 20*x + 10_000

x_verdier = np.arange(0, 601, 100)  # [0, 100, 200, ..., 600]
k_verdier = k(x_verdier)
punkter = zip(x_verdier, k_verdier)

tabell = tabulate(punkter, headers=["x", "k(x)"])
print(tabell)
