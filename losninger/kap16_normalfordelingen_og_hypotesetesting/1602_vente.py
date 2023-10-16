import numpy as np

def f(x):
    return 0.5 * np.exp(-0.5 * x)

# Definerer et sett med øvre grenser for å teste konvergensen
ovre_grenser = [7, 10, 20, 40, 100]

# Går gjennom hver øvre grense og beregner det tilnærmede integralet
for b in ovre_grenser:
    x_verdier = np.arange(0, b, 0.1)  # Genererer x-verdier opp til øvre grense
    arealer = f(x_verdier) * 0.1  # Beregner tilnærmede små arealer
    totalt_areal = np.sum(arealer)  # Summerer alle små arealer

    print(f"Integralet fra 0 til {b} er tilnærmet likt {totalt_areal:.4f}")
