import numpy as np
def h(x):
    return np.e**x / x

x1 = 1
x2 = 3
n = 20
bredde = (x2 - x1) / n
rekt_sum = 0

for i in range(n):
    # NB: x-verdiene må starte i x1. Med x_verdi = bredde*i ville den
    # første x-verdien blitt 0, og h(0) gir divisjon med null.
    x_verdi = x1 + bredde*i
    hoyde = h(x_verdi)
    rekt_sum += hoyde * bredde

print(rekt_sum)
