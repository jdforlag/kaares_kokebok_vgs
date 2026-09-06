import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return -4*x**2 + 16*x - 12

x = np.arange(0.5, 2.51, 0.01)
y = h(x)

plt.plot(x, y, label=r"$h(x)=-4x^2+16x-12$")

# Toppunktet ligger midt mellom nullpunktene 1 og 3, altså i x = 2
plt.plot(2, h(2), "o", label="Toppunkt (2, 4)")

plt.grid()
plt.legend()
plt.show()
