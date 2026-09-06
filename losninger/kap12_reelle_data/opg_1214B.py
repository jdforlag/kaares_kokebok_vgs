import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filnavn = "overskudd.csv"
data = pd.read_csv(filnavn)
print(data.head())

# Andregradsmodell for overskuddet til bedrift A
a, b, c = np.polyfit(data.enheter, data.overskuddA, 2)
print("Andregradsmodellen O(x) for bedrift A:")
print(f"a = {a:.4f}, b = {b:.2f}, c = {c:.2f}")

def O(x):
    return a*x**2 + b*x + c

# Løser ulikheten O(x) >= 15000 etter algoritmen i oppgaven
x1 = 0
while O(x1) < 15_000:
    x1 += 1

x2 = x1
while O(x2) > 15_000:
    x2 += 1

print(f"O(x) er større enn 15 000 kr i intervallet [{x1}, {x2}]")

# NB: Datafila stopper på 1200 enheter, så den øvre grensa kommer fra at vi
# regner videre på modellen utenfor området vi har data for.

x_verdier = np.linspace(min(data.enheter), max(data.enheter), 200)
plt.scatter(data.enheter, data.overskuddA, color="red", label="Reelle data")
plt.plot(x_verdier, O(x_verdier), color="blue", label="Andregradsmodell O(x)")
plt.axhline(15_000, color="black", linestyle="--", label="15 000 kr")
plt.xlabel("Enheter")
plt.ylabel("Overskudd i kr")
plt.grid()
plt.legend()
plt.show()
