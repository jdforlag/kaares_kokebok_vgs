import matplotlib.pyplot as plt
import numpy as np

def h(t):
    return -4.9*t**2 + 40*t + 1.2

x_verdier = np.arange(0, 8.21, 0.01)
h_verdier = h(x_verdier)

plt.xlabel("Tid i sekunder")
plt.ylabel("Høyde i meter")
plt.grid()
plt.plot(x_verdier, h_verdier)
plt.show()
