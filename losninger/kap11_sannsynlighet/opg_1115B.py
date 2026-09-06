from numpy.random import randint

def simuler(n, antall_forsok=20_000):
    """Anslår P(X > 60) når terningen har n sider."""
    frekvens = 0
    for i in range(antall_forsok):
        kast1 = randint(1, n+1)
        kast2 = randint(1, n+1)
        produkt = kast1*kast2
        if produkt > 60:
            frekvens += 1
    return frekvens / antall_forsok

# a)
print(f"n = 10: P(X > 60) er omtrent {simuler(10):.4f}")

# b) Vi prøver større og større terninger til sannsynligheten passerer 0,5.
n = 10
sannsynlighet = simuler(n)

while sannsynlighet <= 0.5:
    n += 1
    sannsynlighet = simuler(n)
    print(f"n = {n}: P(X > 60) er omtrent {sannsynlighet:.4f}")

print(f"Den minste n som gir P(X > 60) > 0,5 er n = {n}")

# Kontroll: for hver terning er det bare n*n utfall, så vi kan også
# telle dem nøyaktig. Da ser vi at svaret er n = 17.
for m in range(14, 19):
    gunstige = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            if i*j > 60:
                gunstige += 1
    print(f"Nøyaktig for n = {m}: {gunstige}/{m*m} = {gunstige/(m*m):.4f}")
