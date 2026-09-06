# a) Programmet simulerer N = 100 000 kast med to terninger. For hvert kast
#    trekkes to tilfeldige heltall fra 1 til 6, og telleren gunstige øker med
#    1 dersom summen av de to blir 9. Til slutt skrives den relative
#    frekvensen gunstige/N ut.
#    Eleven ønsker altså å finne sannsynligheten for at summen av øynene på
#    to terninger blir 9.
#
# b) Ved sannsynlighetsregning: det finnes 6*6 = 36 mulige utfall.
#    De gunstige er (3, 6), (4, 5), (5, 4) og (6, 3), altså 4 stykker.
#        P(sum = 9) = 4/36 = 1/9 = 0,1111
#    Programmet gir en relativ frekvens nær denne verdien.

from random import randint
# Importerer funksjonen randint(a, b). Denne gir
# et tilfeldig heltall fra og med a til og med b.

N = 100000
gunstige = 0

for i in range(N):  # Gjentar N ganger
    a = randint(1, 6)
    b = randint(1, 6)
    if a + b == 9:
        gunstige = gunstige + 1

print(gunstige/N)
print(f"Ved regning: 4/36 = {4/36:.4f}")
