def E(x):
    """Produksjonskostnaden per lue når fabrikken lager x luer."""
    return 0.2*x + 40 + 20_000/x

def Ed(x):  # Numerisk derivert av E
    h = 0.0001
    return (E(x+h) - E(x)) / h

print(f"E'(100) = {Ed(100):.4f}")

# Svaret er omtrent -1,8.
# Det betyr at produksjonskostnaden per lue synker med rundt 1,80 kr dersom
# fabrikken øker produksjonen fra 100 til 101 luer.
