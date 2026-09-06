import matplotlib.pyplot as plt
import numpy as np

# Endringer fra startkoden:
#   - x går helt til 20, og steget er 0,01 slik at grafen blir jevn
#   - vi har lagt til rutenett, en svart x-akse og en tittel
x = np.arange(0.1, 20.01, 0.01)
f = np.log(x)

plt.plot(x, f)
plt.grid()
plt.axhline(color="black")
plt.title(r"Grafen til $f(x) = \ln x$")
plt.show()
