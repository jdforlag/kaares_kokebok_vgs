import numpy as np

# Innstillinger for simuleringen
np.set_printoptions(precision=2)
mu = 74  # Forventningsverdi 74 km/t
sigma = 6  # Standardavvik 6 km/t
fartsgrense = 80  # Fartsgrense i km/t
antall_biler = 840  # Antall biler som passerer under fartskontrollen

# Generere fartsmålinger
maalinger = np.random.normal(loc=mu, scale=sigma, size=antall_biler)

# Beregne bøter basert på fartsoverskridelser
boter = []
for maaling in maalinger:
    fart_over = maaling - fartsgrense
    if fart_over > 5 and fart_over <= 10:
        boter.append(3000)
    elif fart_over > 10 and fart_over <= 15:
        boter.append(4800)
    elif fart_over > 15 and fart_over <= 20:
        boter.append(6700)
    elif fart_over > 20:
        boter.append(9100)
    # Hvis du vil legge til en betingelse for ingen bot ved fart under grensen, kan du inkludere det her

# Beregne politiets totale inntekter
totale_inntekter = sum(boter)

# Beregne gjennomsnittlig inntekt per bil
gjennomsnittlig_inntekt_per_bil = totale_inntekter / antall_biler

# Skrive ut resultatene
print(f"Totale inntekter fra bøter: {totale_inntekter} kr")
print(f"Gjennomsnittlig inntekt per bil: {gjennomsnittlig_inntekt_per_bil:.2f} kr")
