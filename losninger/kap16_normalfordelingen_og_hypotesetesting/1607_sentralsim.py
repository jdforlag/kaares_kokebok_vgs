import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, hypergeom

# Spillparametere
kort = 52
hjerter = 13
ikke_hjerter = kort - hjerter
trekning = 4

def Y_forsok():
    """Returnerer summen av gevinster over 50 spill"""
    gevinst = 60  # Gevinst for å trekke minst to hjerter
    antall_spill = 50  # Antall spill per forsøk
    
    X_verdier = []
    for _ in range(antall_spill):
        h_trukket = np.random.hypergeometric(hjerter, ikke_hjerter, trekning)
        if h_trukket >= 2:
            X_verdier.append(gevinst)  # Legg til gevinsten for hvert vinnende spill
        else:
            X_verdier.append(0)  # Ingen gevinst
    
    return sum(X_verdier)

# Antall forsøk
forsok = 100

# Samler resultater fra flere forsøk
Y_verdier = []
for j in range(forsok):
    y = Y_forsok()  # Utfører et nytt forsøk for hver iterasjon
    Y_verdier.append(y)  # Lagrer resultatet av hvert forsøk

# Beregner teoretiske verdier
E_X = 15.44  # Forventningsverdien for X
SD_X = 26.23  # Standardavviket for X
E_Y = 50 * E_X  # Forventningsverdien for Y
SD_Y = SD_X * np.sqrt(50)  # Standardavviket for Y

# Tegner histogrammet
plt.hist(Y_verdier, bins=20, density=True, color='skyblue', edgecolor='black')

# Tegner normalfordelingskurven
x_min = E_Y - 3.5 * SD_Y
x_maks = E_Y + 3.5 * SD_Y
x = np.linspace(x_min, x_maks, 120)
f = norm.pdf(x, E_Y, SD_Y)
plt.plot(x, f, color="red")

# Setter etiketter og viser plottet
plt.xlabel("Gevinst (kr)")
plt.ylabel("Sannsynlighetstetthet")
plt.title("Fordeling av gevinster fra kortspill")
plt.show()
