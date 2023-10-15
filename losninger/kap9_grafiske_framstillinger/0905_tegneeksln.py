import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 4, 0.01)
x_g = np.arange(0.1, 4, 0.01)

plt.plot(x, np.e**x, label=r"$f(x)=e^x$")
plt.plot(x_g, np.log(x_g), label=r"$g(x)=\ln x$")
plt.ylim(-4, 4)
plt.axhline(color="black")
plt.axvline(color="black")

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
