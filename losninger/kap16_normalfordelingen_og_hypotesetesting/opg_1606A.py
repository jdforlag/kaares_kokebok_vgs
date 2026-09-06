import numpy as np

def f(x):
    return 0.1*np.e**(-0.1*x)

dx = 0.01
x_verdier = np.arange(10, 15, dx)

# Arealet av hvert lille rektangel er bredden dx ganger høyden f(x)
arealer = dx * f(x_verdier)
sum_areal = sum(arealer)
sanns_prosent = sum_areal * 100

print(f"P(10<X<15) = {sanns_prosent:.1f}")
