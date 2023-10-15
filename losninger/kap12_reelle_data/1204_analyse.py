import pandas as pd

# Leser data fra filen
filnavn = "overskudd.csv"
data = pd.read_csv(filnavn)

# Beregner differansen mellom overskuddene til bedriftene A og B
differanser = data.overskuddB - data.overskuddA
enheter = data.enheter  # En snarvei til data.enheter

# Skriver ut differansen
print(differanser)

# Skriver ut den første differansen
print(differanser[0])

# Finn det punktet der bedrift A begynner å ha større overskudd enn bedrift B
indeks = 0
while differanser[indeks] > 0:
    indeks = indeks + 1
ant_enheter = enheter[indeks]
print(f"Ved {ant_enheter} enheter har A større overskudd.")

# Finn størst differanse
maks_diff = 0
maks_enhet = 0
for enhet, diff in zip(enheter, differanser):
    if diff > maks_diff:
        maks_diff = diff
        maks_enhet = enhet
print("Største differanse:", maks_diff)
print("Antall enheter:", maks_enhet)
# Kontrollerer resultatet med innebygd funksjon
print("Kontroll:", max(differanser))

