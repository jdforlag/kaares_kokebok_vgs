def g(x):
    # Definerer funksjonen for parabelen
    return -x**2 + 2*x + 3

# Tilnærming med fem rektangler
x_start = 0
x_slutt = 2.5
antall_rekt = 5
dx = (x_slutt - x_start) / antall_rekt  # Bredden på hvert rektangel
R = 0  # Initialiserer summen av rektanglene

# Looper gjennom hvert rektangel og legger til arealet i summen
for i in range(antall_rekt):
    xn = x_start + i * dx  # x-posisjonen til det nåværende rektangelet
    R += dx * g(xn)  # Legger til arealet av det nåværende rektangelet

print("Areal tilnærmet med fem rektangler:", R)

# Sammenligner med det eksakte arealet
A_eksakt = 205/24  # Det eksakte arealet gitt i teksten
differanse = R - A_eksakt
print(f"Eksakt areal: {A_eksakt}")
print(f"Differanse: {differanse}")
