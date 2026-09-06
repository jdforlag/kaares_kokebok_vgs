import numpy as np

antall_forsok = 4000
innsats = 100
sum_gevinst = 0

for i in range(antall_forsok):
    kast1 = np.random.randint(1, 7)
    kast2 = np.random.randint(1, 7)
    oyne = kast1 + kast2

    if oyne >= 10:
        gevinst = 300
    elif oyne == 3 or oyne == 5:
        gevinst = 200
    else:
        gevinst = 0

    sum_gevinst += gevinst

E_X = sum_gevinst / antall_forsok
print(f"E(X) er omtrent {E_X:.2f} kr.")
print(f"Nettogevinsten per runde er omtrent {E_X - innsats:.2f} kr.")

# Spillet lønner seg altså ikke i lengden.
