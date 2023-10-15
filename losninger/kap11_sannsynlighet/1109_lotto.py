import numpy as np

spill_kostnad = 5  # kostnaden for hvert spill i kroner
overskudd = 0

# Gevinster
premie_5 = 600  # for 5 rette
premie_6 = 4500  # for 6 rette
premie_7 = 3000000  # for 7 rette

# Simulerer 5 milliarder spill 60*52
for _ in range(31_200):
    trekning = np.random.hypergeometric(7, 27, 7)
    # Reduserer overskuddet med kostnaden for hvert spill
    overskudd -= spill_kostnad  

    # Sjekker antall rette og justerer overskuddet basert på gevinsten
    if trekning == 5:
        overskudd += premie_5
    elif trekning == 6:
        overskudd += premie_6
    elif trekning == 7:
        overskudd += premie_7

print(f"Etter 31 200 spill, er overskuddet: {overskudd} kr")