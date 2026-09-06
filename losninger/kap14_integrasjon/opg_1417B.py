def g(x):
    return x**2 - 6*x

def integral(a, b, n=300):
    """Beregner integralet av g fra a til b med n rektangler."""
    dx = (b - a) / n
    summ = 0
    for i in range(n):
        x = a + i*dx
        summ += g(x) * dx
    return summ

b = 1
print(f"Med b = 1 er integralet {integral(b, 2*b):.4f}")

# Integralet er negativt til å begynne med, og vokser når b øker
while integral(b, 2*b) < 0:
    b += 0.001

print(f"b = {b:.3f}")
print(f"Kontroll: integralet fra {b:.3f} til {2*b:.3f} er {integral(b, 2*b):.4f}")
