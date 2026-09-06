from numpy.random import hypergeometric

kort = 52
hjerter = 13
ikke_hjerter = kort - hjerter
antall_forsok = 1500
trukket = 5    # Vi trekker 5 kort
frekvens = 0

# hypergeometric trenger tre tall: antall gunstige i bunken, antall ikke-gunstige,
# og hvor mange vi trekker.
forsokene = hypergeometric(hjerter, ikke_hjerter, trukket, size=antall_forsok)
for forsok in forsokene:
    if forsok == 2:  # 2 hjerter
        frekvens += 1

rel_frekvens = frekvens / antall_forsok
print(f"P(nøyaktig 2 hjerter) er omtrent {rel_frekvens:.4f}")
