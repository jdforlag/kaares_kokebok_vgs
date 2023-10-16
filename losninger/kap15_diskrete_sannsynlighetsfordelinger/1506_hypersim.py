import matplotlib.pyplot as plt
import numpy as np

# Definerer parametrene for den hypergeometriske distribusjonen
n = 100  # Totalt antall bøker
m = 30   # Antall krimbøker
m_c = n - m  # Antall ikke-krimbøker
r = 10   # Antall bøker som trekkes

# Gjør en enkelt trekning og skriver ut resultatet
trekning = np.random.hypergeometric(m, m_c, r)
print(trekning)

# Utvider til 120 forsøk
N = 120
trekninger = np.random.hypergeometric(m, m_c, r, size=N)

# Undersøker hvor mange av forsøkene som ga minst 5 krimbøker
frek_minst5 = 0
for trekning in trekninger:
    if trekning >= 5:
        frek_minst5 += 1
print(f"Det var {frek_minst5} trekninger med minst 5 krimbøker.")

# Finner nummeret på det første forsøket som ga 6 krimbøker
forsoknr = 0
for i in range(len(trekninger)):
    if trekninger[i] == 6:
        forsoknr = i + 1
        break  # Avbryter løkka når vi finner det første tilfellet
if forsoknr == 0:
    print("Ingen forsøk ga 6 krimbøker.")
else:
    print(f"Det {forsoknr}. forsøket ga 6 krimbøker.")

# Regner ut gjennomsnittlig antall krimbøker per trekning
gjennomsnitt = np.mean(trekninger)
print(f"Gjennomsnittlig antall krimbøker per trekning: {gjennomsnitt:.2f}")

# Lager et spredningsplott for å visualisere trekningene
plt.plot(trekninger, "o")  # Plott trekningene som punkter
plt.xlabel("Forsøknummer")
plt.ylabel("Antall krimbøker")
plt.title(f"Spredningsplott. {N} forsøk.")
plt.show()
