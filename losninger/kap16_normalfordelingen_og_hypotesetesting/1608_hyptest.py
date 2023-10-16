from scipy.stats import binomtest

kast = 40
signifikansnivå = 0.05  # Tilsvarer 5%

maks_grense = 0  # Starter med null seksere som maksimal grense

# Sjekker for hvert antall seksere fra 0 til antall kast
for seksere in range(kast + 1):
    resultat = binomtest(seksere, kast, p=1/6, alternative="greater")
    pverdi = resultat.pvalue

    # Skriver ut resultatet for hvert antall seksere
    print(f"Antall seksere: {seksere}, p-verdi: {pverdi:.5f}")

    if pverdi <= signifikansnivå:
        maks_grense = seksere - 1  # Merk minus 1, forklar hvorfor
        break
        # Så snart p-verdien er mindre enn eller lik signifikansnivået, stopper vi, 
        # siden vi har funnet grensen der det antas juks


print(f"Det maksimale antallet seksere Magnus kan få uten at det antas juks er {maks_grense}.")
