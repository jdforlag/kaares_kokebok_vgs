def f(x):
    return -0.015*x**2 + 13*x - 400

# Utskrifter for å demonstrere endringer i overskudd ved bestemte punkter
print(f"{f(0) = }")
print(f"{f(50) = }")
print(f"{f(50) - f(0) = }")

# Initialisere variabler før løkken
maks_overskudd = f(0)  # Det første overskuddet som sammenligningsgrunnlag
enheter_maks = 0  # Antall enheter som gir dette overskuddet

# Løkke gjennom alle mulige antall enheter for å finne det maksimale overskuddet
for i in range(1, 901):
    if f(i) > maks_overskudd:  # Hvis vi finner et større overskudd...
        maks_overskudd = f(i)  # ...oppdaterer vi det maksimale overskuddet...
        enheter_maks = i  # ...og antall enheter som førte til dette overskuddet.

print(f"Det største overskuddet er {maks_overskudd:.2f} kr.")
print(f"{enheter_maks} enheter gir størst overskudd.")
