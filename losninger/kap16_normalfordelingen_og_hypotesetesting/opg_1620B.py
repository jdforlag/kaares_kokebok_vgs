import pandas as pd
from scipy.stats import binomtest

filnavn = "heste_hindre.csv"
data = pd.read_csv(filnavn)
print(data.head())

passert = data["Hindre passert"]
antall_okter = len(passert)

n = 10 * antall_okter        # Totalt antall hindre hun har hoppet over
suksesser = passert.sum()    # Totalt antall hindre hun klarte

print(f"Maria har hoppet mot {n} hindre og klart {suksesser} av dem.")
print(f"Det gir en andel på {suksesser/n:.3f}")

# Nullhypotese H0:      p = 0,70. Maria er like god som før.
# Alternativ hypotese:  p > 0,70. Maria har blitt dyktigere.
resultat = binomtest(suksesser, n, p=0.70, alternative="greater")
p_verdi = resultat.pvalue
print(f"p-verdi: {p_verdi:.5f}")

signifikansnivaa = 0.05
if p_verdi <= signifikansnivaa:
    print("Nullhypotesen forkastes. Maria har blitt dyktigere.")
else:
    print("Nullhypotesen beholdes. Vi kan ikke si at Maria har blitt dyktigere.")
