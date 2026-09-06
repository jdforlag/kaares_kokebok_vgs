import numpy as np

ln = np.log
e = np.e

def f(x):
    return ln(x) - e**(0.05*x)

# Først leter vi etter to x-verdier der f har ulikt fortegn
for x in range(1, 11):
    print(f"f({x}) = {f(x):.4f}")

# Utskriften viser at f(3) er negativ og at f(4) er positiv.
x1 = 3
x2 = 4
m = (x1 + x2) / 2

# Halveringsmetoden. Kravet til f(m) må være strengt for at vi skal
# få 4 riktige desimaler i selve løsningen.
while abs(f(m)) >= 0.000001:
    m = (x1 + x2) / 2

    if f(x1) * f(m) < 0:  # Fortegnsskifte mellom x1 og m
        x2 = m
    else:                 # Fortegnsskifte mellom m og x2
        x1 = m

print(f"Løsningen er x = {m:.4f}")
