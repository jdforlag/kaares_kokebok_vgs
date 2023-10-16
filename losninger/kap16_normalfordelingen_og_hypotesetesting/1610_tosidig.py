import pandas as pd
from scipy.stats import binomtest

# Leser dataene fra CSV-filen
filnavn = "stemmer_rv.csv"
data = pd.read_csv(filnavn)

# Trekker ut dataene relatert til om respondentene stemmer på RV
stemmer = data["StemmerRV"]

# Teller antall svar og antall "Ja"
n = len(stemmer)
antall_ja = stemmer.value_counts()["Ja"]

# Utfører hypotesetesten
resultat = binomtest(antall_ja, n, p=0.08, alternative='two-sided')  # Her er p=0.08 basert på den opprinnelige oppslutningen
p_verdi = resultat.pvalue

# Skriver ut resultatene av hypotesetesten
print(f"Antall svar: {n}")
print(f"Antall 'Ja': {antall_ja}")
print(f"p-verdi: {p_verdi:.5f}")  # Viser p-verdien med 5 desimaler

# Setter signifikansnivået
sig_nivaa = 0.01  # Tilsvarer 1%

# Konkluderer basert på p-verdien og signifikansnivået
if p_verdi <= sig_nivaa:
    print("Med en signifikans på 1%, forkaster vi nullhypotesen.")
    print("Det er signifikante bevis for at mediesaken har påvirket oppslutningen til RV.")
else:
    print("Med en signifikans på 1%, beholder vi nullhypotesen.")
    print("Det er ikke signifikante bevis for at mediesaken har påvirket oppslutningen til RV.")
