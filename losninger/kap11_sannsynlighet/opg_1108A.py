from numpy.random import binomial

frekvens = 0
antall_forsok = 5000
p = 0.70
n = 145
forsokene = binomial(n, p, size=antall_forsok)

# Forutsetning: hver kunde er turist med sannsynlighet 0,70, uavhengig av
# de andre kundene. Da er antall turister binomisk fordelt.
for forsok in forsokene:
    if forsok >= 100:
        frekvens += 1

rel_frekvens = frekvens / antall_forsok
print(f"P(minst 100 turister) er omtrent {rel_frekvens:.4f}")
