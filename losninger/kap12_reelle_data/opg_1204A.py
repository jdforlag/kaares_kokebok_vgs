import matplotlib.pyplot as plt
import pandas as pd

filnavn = "treningsokter.txt"
data = pd.read_csv(filnavn)
plt.bar(data.uke, data.okter)
plt.xlabel("Uke")
plt.ylabel("Antall treningsøkter")
plt.show()
