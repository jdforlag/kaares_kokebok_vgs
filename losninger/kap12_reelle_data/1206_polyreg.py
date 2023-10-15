import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leser data fra fil
filnavn = "xyPunkter.csv"
data = pd.read_csv(filnavn)

# Polynomregresjon for andregradsmodellen
koef_2 = np.polyfit(data.x, data.y, 2)
f = np.poly1d(koef_2)
# Polynomregresjon for tredjegradsmodellen
koef_3 = np.polyfit(data.x, data.y, 3)
g = np.poly1d(koef_3)

# Lager x-verdier for plotting
x = np.linspace(min(data.x), max(data.x), 100)

# Tegner punkter og modeller
plt.scatter(data.x, data.y, color="orange", label="Punkter")
plt.plot(x, f(x), color="blue", label="Andregradsmodell")
plt.plot(x, g(x), color="green", label="Tredjegradsmodell")
plt.legend()
plt.title("Polynomregresjon")
plt.xlabel("x")
plt.ylabel("y")

# Kommenter ut følgende linje hvis du ikke vil vise plottet hver gang
plt.show()

# Beregner summen av kvadrerte avvik for andregradsmodellen
sum_kvadratavvik_2 = 0
for x_val, y_val in zip(data.x, data.y):
    avvik = f(x_val) - y_val
    sum_kvadratavvik_2 += avvik**2

# Beregner summen av kvadrerte avvik for tredjegradsmodellen
sum_kvadratavvik_3 = 0
for x_val, y_val in zip(data.x, data.y):
    avvik = g(x_val) - y_val
    sum_kvadratavvik_3 += avvik**2

# Skriver ut summen av kvadrerte avvik
print(f"Sum av kvadrerte avvik for andregradsmodellen: {sum_kvadratavvik_2:.2f}")
print(f"Sum av kvadrerte avvik for tredjegradsmodellen: {sum_kvadratavvik_3:.2f}")
