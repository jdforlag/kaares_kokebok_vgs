import matplotlib.pyplot as plt

# Definerer lovbruddstyper og antall anmeldelser
lovbruddstyper = ["Eiendomstyveri", "Annet vinningslovbrudd", "Eiendomsskade", "Vold og mishandling", "Seksuallovbrudd"]
antall_lovbrudd = [79515, 25066, 19881, 35988, 7989]

# Definerer farger for hver søyle i stolpediagrammet
farger = ["red", "blue", "green", "pink", "brown"]

# Justerer størrelsen på figuren for bedre lesbarhet
plt.figure(figsize=(15, 5))  # Endre tallet for å justere bredden etter behov

# Tegner et horisontalt stolpediagram med definerte farger
plt.barh(lovbruddstyper, antall_lovbrudd, color=farger)

# Legger til titler og merkelapper
plt.xlabel("Anmeldte lovbrudd")  # X-aksetittel siden vi nå har et horisontalt stolpediagram
# plt.ylabel("Lovbruddstype")
plt.title("Anmeldte lovbrudd i Norge i 2021")  # Tilpass tittelen etter ønske

# Viser stolpediagrammet
plt.show()
