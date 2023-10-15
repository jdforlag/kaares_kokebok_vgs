import numpy as np

p = 0.15  # Sannsynligheten for at noen stemmer på ABC
n = 1200  # Antall personer i hver meningsmåling
maalinger = np.random.binomial(n, p, size=8000)  # Simulerer 8000 meningsmålinger

frekvens = 0  # Teller for antall ganger en hendelse inntreffer

# Analyserer resultatene fra hver meningsmåling
for maaling in maalinger:
    # Sjekker om antall stemmer til ABC er mindre enn 160
    if maaling < 160:
        frekvens += 1

# Beregner relativ frekvens og estimerer sannsynligheten
relativ_frekvens = frekvens / 8000
print(f"Relativ frekvens av X<160: {relativ_frekvens}")
