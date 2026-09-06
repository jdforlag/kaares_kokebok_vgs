from numpy.random import binomial

frekvens = 0
p = 0.72
n = 60
antall_forsok = 1500
forsokene = binomial(n, p, size=antall_forsok)

for forsok in forsokene:
    if forsok > 45:      # Hvis forsok > 45
        frekvens += 1    # Øk frekvens med 1

rel_frekvens = frekvens / antall_forsok  # Beregn relativ frekvens
print(f"P(M > 45) er omtrent {rel_frekvens:.4f}")
