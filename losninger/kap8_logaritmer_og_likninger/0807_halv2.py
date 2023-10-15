import numpy as np

def f(x):
    return x**2 - 4*x - 3

x1 = 2
x2 = 6

xm = (x1 + x2) / 2

if f(xm) * f(x2) < 0:
    x1 = xm
elif f(x1) * f(xm) < 0:
    x2 = xm

while abs(f(xm)) >= 0.003:
    xm = (x1 + x2) / 2

    if f(xm) * f(x2) < 0:
        x1 = xm
    elif f(x1) * f(xm) < 0:
        x2 = xm

print(f"Nullpunktet er x = {xm:.4f}.")

eksakt_nullpunkt = np.sqrt(7) + 2

avvik = abs(xm - eksakt_nullpunkt)
print(f"Avviket er {avvik:.3f}.")
