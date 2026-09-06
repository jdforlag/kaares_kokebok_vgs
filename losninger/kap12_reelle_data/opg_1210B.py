import numpy as np

pasienter = 200
sykehus = 1000
p = 0.43
friske = np.random.binomial(pasienter, p, size=sykehus)

# Teller opp sykehusene der flere enn 100 pasienter ble kurert
antall_sykehus = 0
for kurerte in friske:
    if kurerte > 100:
        antall_sykehus += 1

print(f"Ved {antall_sykehus} av {sykehus} sykehus ble flere enn 100 kurert.")
print(f"Det tilsvarer en relativ frekvens på {antall_sykehus/sykehus:.4f}.")
