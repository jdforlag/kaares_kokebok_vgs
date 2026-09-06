from numpy.random import hypergeometric

hvite = 2
forsok = 1500
trukket = 2  # Vi trekker 2 kuler

for svarte in range(1, 10):
    svarte_trukket = hypergeometric(svarte, hvite, trukket, size=forsok)
    gunstige_utfall = sum(svarte_trukket == 2)
    relativ_frekvens = gunstige_utfall / forsok
    print(f"{svarte} svarte kuler: P(2 svarte) er omtrent {relativ_frekvens:.4f}")

# Av utskriften ser vi at sannsynligheten passerer 0,5 ved 6 svarte kuler.
# Ved regning: P(2 svarte) = (s/(s+2)) * ((s-1)/(s+1))
# For s = 5 gir det 20/42 = 0,476, og for s = 6 gir det 30/56 = 0,536.
print("Det må være minst 6 svarte kuler i krukka.")
