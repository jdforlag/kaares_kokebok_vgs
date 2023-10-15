from numpy.random import choice

# Definisjon av kjønnene og deres sannsynligheter
kjonn = ["gutt", "jente"]
sanns = [0.514, 0.486]

# Velger kjønn for 5 barn
barn = choice(kjonn, size=5, p=sanns)
print(barn)

# Teller antall jenter
jenter = sum(barn == "jente")
print("Antall jenter:", jenter)

# Teller antall fembarnsfamilier med minst 4 jenter
antall_forsok = 6000
frekvens = 0

for i in range(antall_forsok):
    barn = choice(kjonn, size=5, p=sanns)
    jenter = sum(barn == "jente")
    if jenter >= 4:
        frekvens += 1

# Beregner og skriver ut relativ frekvens
relativ_frekvens = frekvens / antall_forsok
print(f"Relativ frekvens for 'minst 4 jenter' i {antall_forsok} forsøk: {relativ_frekvens}")
