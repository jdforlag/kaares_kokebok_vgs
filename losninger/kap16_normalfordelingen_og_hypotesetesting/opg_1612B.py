import numpy as np

mu = 300
sigma = 40
N = 10_000

vekter = np.random.normal(mu, sigma, size=N)

under260 = sum(vekter < 260)
over340 = sum(vekter > 340)

print(f"Antall bjørner under 260 kg: {under260}")
print(f"Antall bjørner over 340 kg:  {over340}")
print(f"Differansen er {under260 - over340}")

# Forklaring:
# 260 og 340 ligger like langt fra forventningsverdien 300, nemlig ett
# standardavvik på hver side. Normalfordelingen er symmetrisk om mu, så de
# to sannsynlighetene er like store. I det lange løp går derfor
#     P(X < 260) - P(X > 340)   mot 0.
