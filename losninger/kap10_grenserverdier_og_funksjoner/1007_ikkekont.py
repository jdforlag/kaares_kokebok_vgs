import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 100 * np.e ** (-0.012 * t)

# Forbereder data for plotting grafen av virkestoff over tid
timer = np.arange(0, 600 + 1, 24)  # De første 600 timene
summ = 0  # Total mengde virkestoff til enhver tid
g_verdier = []  # Mengden virkestoff over tid
for time in timer:
    summ += f(time)
    g_verdier.append(summ)

# Tegner grafen
plt.plot(timer, g_verdier, label='Virkestoff over tid')
plt.xlabel("Antall timer")
plt.ylabel("Virkestoff (mg)")
plt.title("Mengden virkestoff i kroppen over tid")
plt.grid(True)
plt.legend()
plt.show()

# max_virkestoff = g_verdier[-1]

