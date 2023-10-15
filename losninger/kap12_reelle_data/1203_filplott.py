import matplotlib.pyplot as plt
import pandas as pd

# Leser data fra filen
filnavn = "overskudd.csv"
data = pd.read_csv(filnavn)

# Viser de første radene i datasettet for å bekrefte at data er lest riktig
print(data.head())

# Tegner grafene
plt.plot(data.enheter, data.overskuddA, label="Bedrift A")
plt.plot(data.enheter, data.overskuddB, label="Bedrift B")

plt.xlabel("Enheter")
plt.ylabel("Overskudd i kr")
plt.grid()
plt.legend()

# Viser figuren
plt.show()
