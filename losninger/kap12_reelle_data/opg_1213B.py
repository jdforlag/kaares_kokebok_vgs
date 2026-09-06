import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def f(x, a, b):
    return a*b**x

data = pd.read_csv("populasjon.csv")

# curve_fit finner de a- og b-verdiene som gir best tilpasning
param, _ = curve_fit(f, data.maaned, data.populasjon)
a, b = param
print(f"Eksponentialmodellen er f(x) = {a:.2f} * {b:.4f}**x")

modellverdi = f(50, a, b)

# Rad nr. 50 i fila er måned 50, siden månedene starter på 0
virkelig_verdi = data.populasjon[50]

print(f"Modellen gir {modellverdi:.1f} innbyggere etter 50 måneder.")
print(f"Den virkelige verdien er {virkelig_verdi}.")
print(f"Avviket er {abs(modellverdi - virkelig_verdi):.2f} innbyggere.")

# Avviket er svært lite. Tallene i fila følger altså en eksponentialmodell
# nesten helt nøyaktig.
