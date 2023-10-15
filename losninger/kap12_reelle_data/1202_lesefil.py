import pandas as pd

# Leser data fra filen
filnavn = "kjoreturer.txt"
data = pd.read_csv(filnavn)

# Skriver ut kolonnen 'timer'
print(data.timer)

# Skriver ut kolonnen 'km'
print(data.km)

# Beregner summen av alle kjørelengdene
sum_turer = 0
for tur in data.km:
    sum_turer += tur

# Skriver ut total kjørelengde
print(f"Total kjørelengde er {sum_turer} km.")

# Bestemmer den korteste turen målt i timer
min_tid = data.timer[0]  
for tid in data.timer:
    if tid < min_tid:
        min_tid = tid

# Skriver ut den korteste turen
print(f"Den korteste turen tok {min_tid} timer.")

# Bestemmer høyeste fart
hoyest_fart = 0
for i in range(len(data.timer)):
    fart = data.km[i] / data.timer[i]
    if fart > hoyest_fart:
        hoyest_fart = fart

# Skriver ut høyeste fart
print(f"Høyeste fart var {hoyest_fart} km/t.")
