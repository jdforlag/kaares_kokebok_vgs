def V(t, kjopssum):
    """Beregner ny verdi til en bil t år etter at den ble kjøpt, 
    der kjopssum er beløpet bilen ble kjøpt for.""" 
    return kjopssum * 0.86**t

# Demonstrere bruk av funksjonen
print(f"{V(15, 400_000) = }")

# Bestemme den opprinnelige kjøpssummen
G = 100_000  
while V(15, G) < 37_500:
    G += 1000

# Utskrift av det beregnede resultatet
print(f"{G = }")
