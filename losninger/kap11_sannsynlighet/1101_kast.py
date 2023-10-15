from numpy.random import randint

antall_like = 0  # Initialiserer telleren for antall like terningkast

for i in range(1000):  # Gjentar forsøket 1000 ganger
    kast1 = randint(1, 7)  # Første terningkast, gir et tall mellom 1 og 6
    kast2 = randint(1, 7)  # Andre terningkast, gir et tall mellom 1 og 6
    
    if kast1 == kast2:
        antall_like += 1  # Øker telleren hvis begge terningkast er like

# Skriver ut totalt antall like terningkast
print("Antall like:", antall_like)

# Beregner og skriver ut frekvensen av like terningkast
relativ_frekvens = antall_like / 1000
print("Relativ frekvens:", relativ_frekvens)
print("Teoretisk sannsynlighet", 1/6)
