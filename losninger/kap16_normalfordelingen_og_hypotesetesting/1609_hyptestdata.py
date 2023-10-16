import numpy as np
import pandas as pd
from scipy.stats import norm

# Leser dataene fra filen
fil = "oppholdstider.csv"
data = pd.read_csv(fil)
print(data.head())  # Viser de første radene i datasettet

# Lagrer bare oppholdstidene i en egen variabel
tider = data["Oppholdstider"]
print(tider.describe())  # Gir en statistisk beskrivelse av dataene

# Beregner gjennomsnittet av oppholdstidene
gjsnitt_data = tider.mean()
print(f"Gjennomsnitt av oppholdstider: {gjsnitt_data:.2f}")

# Setter de kjente verdiene for populasjonen
mu = 3.88
sigma = 1.20

# Beregner antall observasjoner og standardavviket for gjennomsnittet av dataene
n = len(tider)
sd_data = sigma / np.sqrt(n)  # Standard error
print(f"Standardavvik i data: {sd_data:.3f}")

# Utfører hypotesetesten
p_mindre = norm.cdf(gjsnitt_data, mu, sd_data)  # Beregner p-verdien
print(f"p-verdi: {p_mindre:.5f}")

# Sjekker om vi skal forkaste nullhypotesen
signifikansnivå = 0.05
if p_mindre <= signifikansnivå:
    print("Nullhypotesen forkastes. Det er signifikant bevis for at medisinen reduserer oppholdstiden.")
else:
    print("Nullhypotesen beholdes. Det er ikke tilstrekkelig bevis for at medisinen reduserer oppholdstiden.")
