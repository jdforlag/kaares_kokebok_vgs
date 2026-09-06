def f(x):
    return x**3 - 4*x**2 + x

x1 = 2  # Vi får vite at f(x1) er negativ
x2 = 5  # Vi får vite at f(x2) er positiv
m = (x1 + x2) / 2

# Halveringsmetoden: vi halverer intervallet til f(m) er nær nok null
while abs(f(m)) >= 0.01:
    m = (x1 + x2) / 2

    if f(x1) * f(m) < 0:  # Fortegnsskifte mellom x1 og m
        x2 = m            # Nullpunktet ligger i [x1, m]
    else:                 # Fortegnsskifte mellom m og x2
        x1 = m            # Nullpunktet ligger i [m, x2]

print(f"Nullpunktet er x = {m:.4f}")
print(f"Kontroll: f({m:.4f}) = {f(m):.4f}")
