import numpy as np

# Definerer verdier og deres tilhørende sannsynligheter
verdier = [-2, 0, 1, 3, 4]
sanns = [0.1, 0.3, 0.1, 0.05, 0.45]
m = len(verdier)  # Antall mulige verdier

# Beregner forventningsverdien (E(X))
ex = 0
for i in range(m):
    ex += verdier[i] * sanns[i]

print(f"Forventningsverdi: {ex:.2f}")

# Beregner variansen (Var(X))
varx = 0
for i in range(m):
    varx += (verdier[i] - ex) ** 2 * sanns[i]

print(f"Varians: {varx:.3f}")

# Beregner standardavviket (SD(X))
std_x = np.sqrt(varx)
print(f"Standardavvik: {std_x:.3f}")

# Utfører 50 forsøk og beregner statistikkene
n = 50
utfallene = np.random.choice(verdier, p=sanns, size=n)

# Beregner gjennomsnittet av utfallene
gjsnitt = np.mean(utfallene)

# Beregner variansen og standardavviket for utfallene
varians_simulert = np.var(utfallene)
stddev_simulert = np.std(utfallene)

print(f"\nGjennomsnitt av {n} forsøk: {gjsnitt:.1f}")
print(f"Varians av {n} forsøk: {varians_simulert:.3f}")
print(f"Standardavvik av {n} forsøk: {stddev_simulert:.3f}")
