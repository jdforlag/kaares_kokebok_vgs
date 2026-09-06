from numpy.random import binomial

antall_forsok = 10_000
p = 1/37   # Sannsynligheten for grønt i én omgang
n = 10     # Antall omganger i hvert spill

forsokene = binomial(n, p, size=antall_forsok)
frekvens = sum(forsokene >= 1)

print(f"P(minst 1 grønn i 10 omganger) er omtrent {frekvens/antall_forsok:.4f}")

# Ved regning: P(minst 1 grønn) = 1 - P(ingen grønne) = 1 - (36/37)**10
print(f"Eksakt: 1 - (36/37)**10 = {1 - (36/37)**10:.4f}")
