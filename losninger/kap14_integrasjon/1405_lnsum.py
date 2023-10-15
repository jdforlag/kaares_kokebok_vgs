import numpy as np

def h(x):
    # Funksjonen for den naturlige logaritmen
    return np.log(x)

# Definerer parametere
antall_rekt = 36
x1 = 2
x2 = np.e**2
dx = (x2 - x1) / antall_rekt  # Beregner bredden til hvert rektangel

# Beregner rektangelsummen ved å bruke høyre endepunkter
R_hoyre = 0
xn = x1
for i in range(antall_rekt):
    xn += dx
    R_hoyre += dx * h(xn)
    

print("Rektangelsum (høyre endepunkter):", R_hoyre)

# Det eksakte arealet under grafen
eksakt_areal = 8  # Gitt verdi

# Beregner differansen mellom rektangelsummen (høyre) og det eksakte arealet
differanse = R_hoyre - eksakt_areal
print("Differanse:", differanse)  # 36 rektangler gir diff mindre enn 0,1
