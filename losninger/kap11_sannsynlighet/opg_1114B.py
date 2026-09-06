from numpy.random import hypergeometric

# Ina har 3 av de 50 loddene. Det trekkes ett vinnerlodd.
# Tallene til hypergeometric er: 3 gunstige lodd, 47 andre lodd, 1 trekning.
antall_forsok = 1000
forsokene = hypergeometric(3, 47, 1, size=antall_forsok)

seiere = sum(forsokene == 1)

print(f"Ina vant førstepremien {seiere} ganger av {antall_forsok}.")
print(f"Relativ frekvens: {seiere/antall_forsok:.4f}")
print(f"Den teoretiske sannsynligheten er 3/50 = {3/50:.4f}")
