a = 3  # Startverdien for sekvensen
antall_tall = 52  # Antall tall i sekvensen, basert på ønsket utskrift

# Vi bruker en for-løkke for å gjenta prosessen et bestemt antall ganger
for i in range(antall_tall):
    # Skriver ut det nåværende tallet i sekvensen, etterfulgt av et komma og et mellomrom
    print(a, end=", ")
    a = a + 4  # Legger til 4 for å få det neste tallet i sekvensen

# Etter løkken kan vi skrive ut det siste tallet uten et etterfølgende komma
print(a)
