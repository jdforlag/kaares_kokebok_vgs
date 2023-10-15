import numpy as np

# Definerer innholdet i eskene
eskeA = ["rød"]*20 + ["blå"]*40
eskeB = ["rød"]*35 + ["blå"]*50 + ["grønn"]*15

frekvens = 0

antall_simuleringer = 800

# Gjennomfører simuleringene
for _ in range(antall_simuleringer):
    # Trekker kuler fra eskene
    kulerA = np.random.choice(eskeA, size=15, replace=False)
    kulerB = np.random.choice(eskeB, size=10, replace=False)
    
    # Teller antall røde og grønne kuler
    rodeA = sum(kulerA == "rød")
    rodeB = sum(kulerB == "rød")
    gronneB = sum(kulerB == "grønn")
    rode = rodeA + rodeB
    
    if rode < 10 and gronneB >= 4:
        frekvens += 1

# Beregner den estimerte sannsynligheten
rel_frek = frekvens / antall_simuleringer
print(rel_frek)
