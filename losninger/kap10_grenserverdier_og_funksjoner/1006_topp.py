def f(x):
    return -0.05*x**2 + 100*x - 10000

def fd(x, h=0.001):
    """Returnerer den deriverte f'(x)"""
    return (f(x+h) - f(x)) / h

print(fd(5))

# Skriver ut overskuddet for forskjellige produksjonsmengder
a = 200
while a <= 1700:
    print(f"Produksjon: {a}, Overskudd: {f(a)}")
    a += 300

# Endrer programmet for å finne produksjonsmengden som gir størst mulig overskudd
a = 200
while fd(a) > 0:
    a += 1  # Endret fra a += 300

# Skriver ut antall varer som gir størst overskudd, og hva dette overskuddet er
print(f"For å oppnå det største overskuddet, bør {a} varer produseres. Største overskudd er {f(a)} kr.")
