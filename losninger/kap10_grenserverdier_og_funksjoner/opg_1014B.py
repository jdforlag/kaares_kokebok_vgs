import numpy as np

e = np.e

def f(n):
    return (1 + 1/n)**n

n = 1
for i in range(9):
    print(f"n = {n}, differanse = {e - f(n)}")
    n = n * 10

# Differansen nærmer seg 0. Det betyr at
#     lim (n -> uendelig) (1 + 1/n)**n = e
#
# NB: Prøv å øke antall runder i løkka. Fra rundt n = 10**9 begynner
# differansen å hoppe litt opp og ned, og etter hvert blir den stor igjen.
# Det skyldes ikke matematikken, men at datamaskinen ikke klarer å skille
# 1 + 1/n fra 1 når n blir svært stor.
