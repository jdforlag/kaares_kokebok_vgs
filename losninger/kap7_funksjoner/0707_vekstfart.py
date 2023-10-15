def f(x):
    return x**3 - 4*x

def gvf(x1, x2):  
    """Gir gjennomsnittlig vekstfart til f i [x1, x2]"""
    endring_x = x2 - x1
    endring_y = f(x2) - f(x1)
    return endring_y / endring_x

# For testing: Skriver ut gjennomsnittlig vekstfart for f fra 0 til 1
print(gvf(0, 1))

# Får input fra brukeren for å beregne gjennomsnittlig vekstfart basert på egendefinerte verdier
x1 = float(input("Oppgi startverdien x1: "))
x2 = float(input("Oppgi sluttverdien x2: "))

# Beregner og skriver ut den gjennomsnittlige vekstfarten med de oppgitte verdiene
resultat = gvf(x1, x2)
print(f"Gjennomsnittlig vekstfart fra {x1} til {x2} er {resultat}.")
