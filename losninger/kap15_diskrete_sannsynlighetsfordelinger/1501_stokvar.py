import numpy as np

# Definerer verdier og deres tilsvarende sannsynligheter
verdier = [2, 3, 7]
sannsynligheter = [0.4, 0.5, 0.1]

# Lager en løkke for å simulere 20 forsøk
for i in range(20):
    utfall = np.random.choice(verdier, p=sannsynligheter)
    print(utfall)
