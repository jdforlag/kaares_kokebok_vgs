def f(x):
    return (x-2)*(x+1)*(x+3)

a = -3
b = 2
n = 150
dx = (b - a) / n
summ = 0

for i in range(n):
    x1 = a + i*dx        # Venstre endepunkt
    x2 = a + (i+1)*dx    # Høyre endepunkt

    # Vi velger den største av de to funksjonsverdiene som høyde
    if f(x1) >= f(x2):
        hoyde = f(x1)
    else:
        hoyde = f(x2)

    summ += hoyde * dx

print(f"Integralet er omtrent {summ:.4f}")
