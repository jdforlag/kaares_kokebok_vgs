import numpy as np

def f(x):
    return 2 - np.e**(0.1 * x)

# Initialiser variabler
dx = 0.01  # Bredden på rektanglene
a = 0  # Startverdi for x
b = a  # Vi begynner med b lik a
rekt_sum = 0  # Summen av rektanglene

# Vi vil fortsette å legge til rektangler til summen nærmer seg null
while True:
    Rn = dx * f(b)  # Beregner arealet av det neste rektangelet
    rekt_sum += Rn  # Legger dette arealet til den løpende summen

    # Hvis summen av rektanglene er nær null, avslutter vi løkken
    if rekt_sum <= 0:
        break

    b += dx  # Øker b for neste rektangel

# Skriver ut den beregnede verdien av b
print("Verdien av b er:", b)
fasit = 12.5643
print(f"Diff : {b - fasit:.3f}")  # 0.006
