from numpy.random import randint

kast1 = randint(1, 7)
kast2 = randint(1, 7)
kast_nr = 1

# NB: Terningene må kastes på nytt inni løkka. Uten de to første linjene
# i løkkekroppen ville de samme to kastene blitt liggende, og programmet
# ville aldri stoppet.
while kast1 + kast2 < 12:
    kast1 = randint(1, 7)
    kast2 = randint(1, 7)
    kast_nr += 1

print("Kast nr:", kast_nr)
