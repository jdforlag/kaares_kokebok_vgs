def f(x):
    return 1/9 * (x+1) * (x-6)**2

x_min = 0
x_maks = 6
n = 6000

bredde = (x_maks - x_min) / n  # Bredden av hvert rektangel
areal = 0

for i in range(n):
    x = x_min + i*bredde   # Venstre endepunkt i rektangel nr. i
    areal += f(x) * bredde

print(f"Arealet er omtrent {areal:.4f}")

# Prøv å endre n. Jo flere rektangler, desto nærmere kommer vi det
# eksakte arealet, som er 20.
