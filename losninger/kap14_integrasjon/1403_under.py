def f(x):
    return 2 * x  # Definerer funksjonen

# Initialiserer totalt areal til 0
A = 0

# Setter tykkelsen/bredden på trapesene
h = 1

# Itererer gjennom de fire trapesene
for i in range(1, 5):
    a = f(i)  # Beregner høyden på venstre side av trapeset
    b = f(i + h)  # Beregner høyden på høyre side av trapeset
    A += h * (a + b) / 2  # Legger til arealet av trapeset i totalen

# Skriver ut det totale arealet
print(f"Totalt areal under grafen: {A}")
