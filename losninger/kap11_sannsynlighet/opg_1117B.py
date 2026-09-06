from numpy.random import randint

antall_forsok = 100_000
frekvens = 0

for i in range(antall_forsok):
    kast = randint(1, 7, size=3)
    produkt = kast[0] * kast[1] * kast[2]
    if produkt > 100:
        frekvens += 1

print(f"P(produkt > 100) er omtrent {frekvens/antall_forsok:.4f}")

# Kontroll: her er det bare 216 utfall, så vi kan også telle dem nøyaktig
gunstige = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i*j*k > 100:
                gunstige += 1

print(f"Nøyaktig: {gunstige}/216 = {gunstige/216:.4f}")
