import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return (1/3)*x**3 - 2*x**2

# Definisjonsmengden er [-2, 3]. Vi tar med 3 ved å gå litt forbi.
x = np.arange(-2, 3.01, 0.01)
y = h(x)

plt.plot(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("h(x)")
plt.show()
