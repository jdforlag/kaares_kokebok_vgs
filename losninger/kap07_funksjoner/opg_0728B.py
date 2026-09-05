def f(x):
    return 1/x + 0.01*x

def fd(x):  # Den deriverte til f(x)
    dx = 0.001
    dy = f(x+dx) - f(x)
    return dy / dx

b = 1  # Vi får vite at f'(1) < 0

# Funksjonen synker fram til bunnpunktet. Når den deriverte ikke lenger
# er negativ, har vi kommet til bunnen.
while fd(b) < 0:
    b += 0.01

print(f"Bunnpunktet er ({b:.2f}, {f(b):.2f})")
