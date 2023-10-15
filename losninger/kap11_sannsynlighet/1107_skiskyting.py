import numpy as np

p = 0.8  # Sannsynligheten for treff
n = 5  # Antall skudd
treff = np.random.binomial(n, p, size=10)  # Simulerer 10 skuddserier

perfekte_serier = 0  # Teller for antall perfekte serier
totalt_bom = 0  # Teller for totalt antall bom

# Går gjennom resultatene fra hver skuddserie
for i in range(len(treff)):
    nr = i+1
    print(f"Serienr {nr}: Antall treff: {treff[i]}")
    
    # Sjekker om serien var perfekt (ingen bom)
    if treff[i] == 5:
        perfekte_serier += 1
    
    # Teller opp antall bom for hver serie
    totalt_bom += n - treff[i]

# Skriver ut antall perfekte serier og totalt antall bom
print(f"Svein skjøt {perfekte_serier} perfekte serier")
print(f"Totalt antall bom: {totalt_bom}")
