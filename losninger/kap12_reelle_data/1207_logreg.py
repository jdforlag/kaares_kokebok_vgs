import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(x, a, b, c):
    # Definerer modellfunksjonen for logaritmisk regresjon
    return a * np.log10(b * x) + c

# Datasett
aar = [1930, 1940, 1960, 1980, 1990]
levealder = [58.7, 62.1, 70.0, 73.3, 74.9]

# Konverterer år til antall år etter 1900 for x-verdiene
x_verdier = [x - 1900 for x in aar]

# Utfører logaritmisk regresjon for å finne optimale parametere
param, _ = curve_fit(f, x_verdier, levealder)

# Skriver ut de funnete parameterverdiene
print(f"Parametere fra regresjon: a = {param[0]}, b = {param[1]}, c = {param[2]}")

# Definerer x-verdier for modellen (fra 1920 til 2035, omgjort til år etter 1900)
x_verdier_modell = np.linspace(20, 135, 200)

# Beregner y-verdier basert på den logaritmiske modellen
f_verdier = f(x_verdier_modell, *param)

# Plotter de faktiske dataene
plt.scatter(x_verdier, levealder, color="red", label="Faktiske data")

# Plotter regresjonsmodellen
plt.plot(x_verdier_modell, f_verdier, color="blue", label="Logaritmisk regresjonsmodell")

# Legger til ekstra grafikkelementer
plt.title("Logaritmisk regresjon for forventet levealder")
plt.xlabel("År etter 1900")
plt.ylabel("Forventet levealder")
plt.legend()
plt.grid(True)

# Viser plottet
plt.show()
