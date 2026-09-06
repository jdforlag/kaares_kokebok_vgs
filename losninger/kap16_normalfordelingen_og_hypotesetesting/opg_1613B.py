import numpy as np

antall_forsok = 5000
frekvens = 0
skoler = ["A", "B", "C"]

for forsok in range(antall_forsok):
    karakterer = []

    for elev in range(20):
        valgt_skole = np.random.choice(skoler)

        # Hver skole har sin egen forventning og sitt eget standardavvik
        if valgt_skole == "A":
            karakter = np.random.normal(3.8, 1.2)
        elif valgt_skole == "B":
            karakter = np.random.normal(3.4, 1.4)
        else:
            karakter = np.random.normal(4.1, 1.1)

        karakterer.append(karakter)

    snitt = np.mean(karakterer)
    if snitt > 4:
        frekvens += 1

print(f"P(karaktersnitt > 4) er omtrent {frekvens/antall_forsok:.4f}")
