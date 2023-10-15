import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -0.015*x**2 + 13*x - 400

x_verdier = np.arange(0, 901, 1)
y_verdier = f(x_verdier)

plt.plot(x_verdier, y_verdier)
plt.grid()
plt.xlabel("Antall enheter")
plt.ylabel("Overskudd i kr")
plt.show()
