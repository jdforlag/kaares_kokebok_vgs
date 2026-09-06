import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def v(x, a, b):
    return a*b**x

filnavn = "vareeksport.csv"
data = pd.read_csv(filnavn)
print(data.head())

# x er antall år etter 1980
x_verdier = data["år"] - 1980
y_verdier = data["verdi (i milliarder kroner)"]

param, _ = curve_fit(v, x_verdier, y_verdier)
a, b = param
print(f"v(x) = {a:.2f} * {b:.4f}**x")

x_modell = np.linspace(0, max(x_verdier), 200)

plt.scatter(x_verdier, y_verdier, color="red", label="Reelle data")
plt.plot(x_modell, v(x_modell, a, b), color="blue", label="Eksponentiell modell")
plt.xlabel("År etter 1980")
plt.ylabel("Verdi i milliarder kroner")
plt.grid()
plt.legend()
plt.show()
