import matplotlib.pyplot as plt

naeringer = ["Jordbruk, skogbruk og fiske",
             "Undervisning",
             "Industri",
             "Bygge- og anleggsvirksomhet"]
dodsfall = [9, 1, 6, 10]

# Gjør figuren bred nok til at navnene på næringene får plass
plt.figure(figsize=(10, 4))

plt.barh(naeringer, dodsfall)
plt.xlabel("Antall dødsfall")
plt.title("Arbeidsulykker med dødelig utfall. Norge, 2021.")
plt.tight_layout()
plt.show()
