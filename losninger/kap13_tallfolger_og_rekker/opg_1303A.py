# Feilene i koden var:
#   1) Startverdien var skrevet som tekst: "åtti" skal være tallet 80
#   2) for skal skrives med liten forbokstav
#   3) Kommandoen heter range, ikke rangere
#   4) print("b") skriver ut bokstaven b. Vi vil skrive ut verdien: print(b)
#   5) b:2 er ikke gyldig Python. Divisjon skrives b/2

b = 80
for i in range(15):
    print(b)
    b = b/2 + 6

# Utskriften viser at leddene nærmer seg 12. Grenseverdien er altså
#     lim (n -> uendelig) b_n = 12
