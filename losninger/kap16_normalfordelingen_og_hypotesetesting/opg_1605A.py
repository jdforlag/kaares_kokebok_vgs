import numpy as np

E_X = 40
SD_X = 2.5

antall_forsok = 0
while True:
    flytid = np.random.normal(E_X, SD_X)
    antall_forsok += 1
    if flytid <= 30:
        break
print(antall_forsok)

# En flytid på høyst 30 minutter er fire standardavvik under forventningen,
# så det skjer svært sjelden. Kjør programmet flere ganger og se hvor mye
# antall forsøk varierer.
