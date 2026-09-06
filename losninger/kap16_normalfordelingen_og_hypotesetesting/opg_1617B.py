from scipy.stats import binomtest

n = 10          # Antall glass
riktige = 8     # Antall riktige svar Marte gav
signifikansnivaa = 0.05

# Nullhypotese H0:      p = 0,50. Marte gjetter.
# Alternativ hypotese:  p > 0,50. Marte kjenner forskjell på colatypene.
resultat = binomtest(riktige, n, p=0.5, alternative="greater")
p_verdi = resultat.pvalue

print(f"p-verdi: {p_verdi:.5f}")

if p_verdi <= signifikansnivaa:
    print("Nullhypotesen forkastes.")
    print("Det er grunnlag for å si at Marte kjenner forskjell på colatypene.")
else:
    print("Nullhypotesen beholdes.")
    print("Det er ikke grunnlag for å si at Marte kjenner forskjell på colatypene.")
