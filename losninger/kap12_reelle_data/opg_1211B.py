import matplotlib.pyplot as plt
import numpy as np

x = [-1, 1, 2]
y = [5, 0, -2]

a, b = np.polyfit(x, y, 1)
print(f"Den lineære modellen er f(x) = {a:.2f}x + {b:.2f}")

x_verdier = np.linspace(min(x), max(x), 100)

plt.scatter(x, y, color="red", label="Punkter")
plt.plot(x_verdier, a*x_verdier + b, color="blue", label="Lineær modell")
plt.grid()
plt.legend()
plt.show()
