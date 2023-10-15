def b(n):
    # Beregner det n-te leddet i den geometriske rekken
    return 300 * 0.8 ** (n - 1)

def S(n):
    """Legger sammen b1+b2+b3+...+bn og returnerer summen"""
    summ = 0  # Initialiserer summen
    for i in range(1, n + 1):
        summ += b(i)  # Legger til det i-te leddet i summen
    return summ  # Returnerer den totale summen

# Algoritme for å undersøke summen av den uendelige geometriske rekken
k = 1  # Setter startverdien for k
while b(k) > 0.00001:  
    print(f"S{k} = {S(k)}")
    k += 1  # Går til neste leddnummer

# Når løkken avsluttes, skriver vi ut den tilnærmede summen av den uendelige rekken
print("Summen av den uendelige geometriske rekken")
print("er:", round(S(k), 2))
