import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 4*x + 3

# Generer en liste med x-verdier
x_verdier = np.arange(-2, 5, 0.1)

# Beregn y-verdiene ved å bruke polynomfunksjonen
y_verdier = f(x_verdier)

# Tegn grafen til funksjonen
plt.plot(x_verdier, y_verdier, label=r"$f(x) = x^2 - 4x + 3$")

# Marker bunnpunktet
plt.plot(2, f(2), "o", label="Bunnpunkt")

# Legg til etiketter og rutenett
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafen til en polynomfunksjon")
plt.legend()  # Viser etikettene
plt.grid()

# Vis grafen
plt.show()
