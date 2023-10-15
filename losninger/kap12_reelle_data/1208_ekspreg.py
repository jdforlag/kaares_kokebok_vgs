import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Definere modellfunksjonen for eksponentiell regresjon
def g(x, a, b):
    return a * b ** x

# Definere datasettet
uke = [0, 5, 10, 15, 20, 25, 30]
solgte = [57, 91, 139, 279, 485, 853, 1525]

# Utføre eksponentiell regresjon for å finne optimale parametere
param, _ = curve_fit(g, uke, solgte)

# Skrive ut de funnete parameterverdiene
print(f"Parametere fra regresjon: a = {param[0]:.2f}, b = {param[1]:.2f}")

# Definere x-verdier for modellen
x_verdier = np.linspace(0, 30, 100)

# Beregne y-verdier basert på den eksponentielle modellen
g_verdier = g(x_verdier, *param)

# Plotte de faktiske dataene
plt.scatter(uke, solgte, color="red", label="Faktiske data")

# Plotte regresjonsmodellen
plt.plot(x_verdier, g_verdier, color="blue", label="Eksponentiell regresjonsmodell")

# Legge til ekstra grafikkelementer
plt.title("Eksponentiell regresjon for salgsutvikling")
plt.xlabel("Uker etter lansering")
plt.ylabel("Antall solgte per uke")
plt.legend()
plt.grid(True)

# Vise plottet
plt.show()

# Estimere salg i uke 2 og uke 5
print(f"Antall solgte i uke 2: {g(2, *param):.0f}")
print(f"Antall solgte i uke 5: {g(5, *param):.0f}")

# Beregne totalt antall solgte de første 30 ukene
sum_solgte = 0
for ukenr in range(30):  # 0 til 29
    sum_solgte += g(ukenr, *param)
print(f"Totalt antall solgte i de første 30 ukene: {sum_solgte:.0f}")
