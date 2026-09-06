import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filnavn = "brod.csv"
data = pd.read_csv(filnavn)
brod = data["antall brød"]
kostnader = data["kostnader"]

a, b, c = np.polyfit(brod, kostnader, 2)
print("Andregradsmodellen k(x):")
print(f"a = {a:.5f}, b = {b:.5f}, c = {c:.2f}")

def k(x):
    return a*x**2 + b*x + c

# 100 x-verdier jevnt fordelt fra det minste til det største antallet brød
x_verdier = np.linspace(min(brod), max(brod), 100)

plt.scatter(brod, kostnader, color="red", label="Reelle data")
plt.plot(x_verdier, k(x_verdier), color="blue", label="Andregradsmodell k(x)")
plt.xlabel("Antall brød")
plt.ylabel("Kostnader i kr")
plt.grid()
plt.legend()
plt.show()
