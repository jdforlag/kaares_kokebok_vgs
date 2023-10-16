import numpy as np
import matplotlib.pyplot as plt

# Parametere
n = 10  # Antall forespørsler per forsøk
p_feil = 0.20  # Sannsynlighet for feil per forespørsel
antall_forsok = 8000  # Totalt antall forsøk

# Utfør forsøkene
utfall = np.random.binomial(n, p_feil, size=antall_forsok)

# Beregn kumulativ sum av feil
kumulativ_sum_feil = np.cumsum(utfall)

# Generer en sekvens av forsøksnumre
forsok_nr = np.arange(1, antall_forsok + 1)

# Beregn gjennomsnittsverdier basert på kumulativ sum
gjsnitt_verdier = kumulativ_sum_feil / forsok_nr

# Beregn forventningsverdien (E(Y))
ey = n * p_feil  # Dette er den teoretiske forventningsverdien

# Opprett plott
plt.figure(figsize=(10, 6))

# Plott gjennomsnittsverdiene
plt.plot(forsok_nr, gjsnitt_verdier, label='Gjennomsnittlig antall feil')

# Tegn en horisontal linje som representerer forventningsverdien
plt.axhline(y=ey, color="r", linestyle="--", label='Forventningsverdien (E(Y))')

# Begrens y-aksen for klarhet
plt.ylim(1.80, 2.20)

# Legg til tittel og etiketter
plt.title('Gjennomsnittlig antall feil over tid')
plt.xlabel('Antall forsøk')
plt.ylabel('Gjennomsnittlig antall feil')
plt.legend()  # Viser boks med forklaringer på linjene

# Vis plottet
plt.show()
