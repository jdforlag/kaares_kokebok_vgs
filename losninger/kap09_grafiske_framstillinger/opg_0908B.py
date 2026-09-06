import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x

def g(x):
    return x**2

def h(x):
    return x**3

x = np.arange(-1, 2.01, 0.01)

# Tre plt.plot-kommandoer før plt.show() gir tre grafer i samme diagram
plt.plot(x, f(x), label=r"$f(x)=x$")
plt.plot(x, g(x), label=r"$g(x)=x^2$")
plt.plot(x, h(x), label=r"$h(x)=x^3$")

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
