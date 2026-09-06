import numpy as np

gevinst = 200
innsats = 50
saldo = 1000
p = 0.20
runder = 0

while saldo >= innsats:
    saldo -= innsats
    runder += 1

    # np.random.rand() gir et tilfeldig desimaltall mellom 0 og 1.
    # Det er mindre enn p i 20 % av tilfellene.
    if np.random.rand() < p:
        saldo += gevinst

print(f"{runder} runder")
