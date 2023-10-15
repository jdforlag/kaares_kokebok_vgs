# Startverdien for sekvensen
b = 100  

# Antall iterasjoner basert på ønsket utskrift og oppførselen til rekursjonsformelen
antall_iterasjoner = 15

# Vi bruker en for-løkke for å gjenta prosessen et bestemt antall ganger
for i in range(antall_iterasjoner):
    # Skriver ut det nåværende tallet i sekvensen
    print(b)
    # Beregner det neste tallet i sekvensen basert på rekursjonsformelen
    b = b/2 + 5  

# Etter løkken kan vi observere den siste verdien av b for å forsøke å forstå oppførselen til sekvensen
print("Sluttverdi:", b)
# Går mot 10
