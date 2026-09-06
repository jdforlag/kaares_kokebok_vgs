import numpy as np

def f(x):
    return 9 - x**2

def rektangelmetode(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b-h, N)
    return h * np.sum(f(x))

def trapesmetode(a, b, N):
    h = (b - a) / N
    total = 0
    for i in range(N):
        x1 = a + i*h
        x2 = a + (i+1)*h
        total += 0.5 * (f(x1) + f(x2))
    return total * h

x_min = 0
x_maks = 3
antall_rekt = 5
integral = 18  # Det eksakte svaret

while True:
    R = rektangelmetode(x_min, x_maks, antall_rekt)
    T = trapesmetode(x_min, x_maks, antall_rekt)

    # Stopper så snart en av metodene er nærmere enn 0,01
    if abs(R - integral) < 0.01 or abs(T - integral) < 0.01:
        print(f"Antall rektangler: {antall_rekt}")
        print(f"Rektangelmetoden gir {R:.4f}")
        print(f"Trapesmetoden gir   {T:.4f}")

        if abs(T - integral) < 0.01:
            print("Trapesmetoden gav best tilnærming med færrest rektangler.")
        else:
            print("Rektangelmetoden gav best tilnærming med færrest rektangler.")
        break

    antall_rekt += 1
