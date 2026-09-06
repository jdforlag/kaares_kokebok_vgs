import numpy as np
import pandas as pd
from scipy.stats import norm

filnavn = "inntekter.csv"
data = pd.read_csv(filnavn)
print(data.head())

inntekter = data["inntekt"]

mu = 14_800     # Forventningsverdien i 2022
sigma = 1200    # Standardavviket i 2022
n = len(inntekter)

gjsnitt = inntekter.mean()
print(f"Antall dager: {n}")
print(f"Gjennomsnittlig daglig inntekt i 2023: {gjsnitt:.2f} kr")

# Ifølge sentralgrensesetningen er gjennomsnittet av n dager normalfordelt
# med forventning mu og standardavvik sigma/rot(n)
sd_gjsnitt = sigma / np.sqrt(n)

p_verdi = 1 - norm.cdf(gjsnitt, mu, sd_gjsnitt)
print(f"p-verdi: {p_verdi:.5f}")

signifikansnivaa = 0.01
if p_verdi <= signifikansnivaa:
    print("Nullhypotesen forkastes.")
    print("Det er grunnlag for å si at inntektene har økt.")
else:
    print("Nullhypotesen beholdes.")
    print("Det er ikke grunnlag for å si at inntektene har økt.")
