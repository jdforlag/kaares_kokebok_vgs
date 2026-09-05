# Feilene i koden var:
#   1) Def skal skrives med liten forbokstav: def
#   2) Det manglet kolon etter def h(x)
#   3) 3x er ikke gyldig Python. Vi må skrive 3*x
#   4) print manglet en parentes foran anførselstegnet
#   5) Løkka begynte på -1, men tabellen begynner på -2
#   6) Utskriften i løkka hadde byttet om på i og h(i)

def h(x):
    return x**2 - 3*x - 10

print(" x h(x)")
print("-------")
for i in range(-2, 4):
    print(i, h(i))
