from numpy.random import randint

# Antall forsøk og initialisering av frekvens for hendelsen
antall_forsok = 1500
frekvens = 0

# Gjennomføre det angitte antallet forsøk
for i in range(antall_forsok):
    # Simulerer kast med 10 terninger
    kastene = randint(1, 7, size=10)

    # Undersøker om summen av øynene er mindre enn 23
    if sum(kastene) < 23:
        frekvens += 1  # Øker frekvensen hvis betingelsen er oppfylt

# Beregner og skriver ut frekvensen for hendelsen
print(f"Frekvensen for 'Sum øyne mindre enn 23' i {antall_forsok} forsøk: {frekvens}")

# Hvis ønskelig, kan man beregne og skrive ut den relative frekvensen
relativ_frekvens = frekvens / antall_forsok
print(f"Relativ frekvens: {relativ_frekvens}")
