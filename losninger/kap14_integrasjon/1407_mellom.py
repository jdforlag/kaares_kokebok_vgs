import numpy as np

def f(x):
    return x**3 - 3*x**2 + 5

def g(x):
    return -x**2 + 3*x + 2

# Leser antall rektangler fra brukeren
n = int(input("Skriv inn antall rektangler: "))

# Definerer start- og sluttverdier
a = 1
b = 2

# Beregner bredden på hvert rektangel
dx = (b - a) / n

# Lager en liste med x-verdier for hvert rektangel
x_verdier = np.arange(a, b, dx)

# Initialiserer total arealet til 0
total_areal = 0

# Går gjennom hvert rektangel og beregner arealet
for xn in x_verdier:
    # Beregner høyden til rektangelet. 
    # Siden g(x) er over f(x), beregner vi forskjellen som g(x) - f(x)
    h = g(xn) - f(xn)
    
    # Beregner arealet av rektangelet og legger det til totalen
    An = dx * h  # Arealet av rektangelet
    total_areal += An

# Beregner det eksakte arealet
eksakt_areal = 29 / 12  # gitt fra oppgaven

# Beregner avviket i prosent
avvik_prosent = ((total_areal - eksakt_areal) / eksakt_areal) * 100

# Skriver ut totalt areal og avvik
print(f"\nTotalt areal: {total_areal:.3f}")
print(f"Eksakt areal: {eksakt_areal:.3f}")
print(f"Avvik i prosent: {avvik_prosent:.3f} %")
