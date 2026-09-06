import numpy as np

lambda_verdi = 0.2
mu = 1 / lambda_verdi
n = 300
pris = 250

# Siden minste ventetid er 10 minutter, skriver vi + 10
tider = np.random.exponential(mu, size=n) + 10
# Finner antall pizzaer som skal ha halv pris
antall_rabatt = sum(tider > 15)

antall_full_pris = n - antall_rabatt
inntekt = antall_full_pris * pris + antall_rabatt * pris/2

print(f"{antall_rabatt} av {n} gjester ventet mer enn 15 minutter.")
print(f"Total inntekt: {inntekt:.0f} kr")
