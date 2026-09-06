import numpy as np

lg = np.log10

# Likningen lg(x+3) = x - 3 skrives om til lg(x+3) - x + 3 = 0.
# Venstresiden definerer vi som funksjonen f.
def f(x):
    return lg(x+3) - x + 3

x1 = 1    # Vi får vite at f(x1) er positiv
x2 = 6.5  # Vi får vite at f(x2) er negativ
m = (x1 + x2) / 2

# Halveringsmetoden
while abs(f(m)) >= 0.0001:
    m = (x1 + x2) / 2

    if f(x1) * f(m) < 0:  # Fortegnsskifte mellom x1 og m
        x2 = m
    else:                 # Fortegnsskifte mellom m og x2
        x1 = m

print(f"Løsningen er x = {m:.2f}")
