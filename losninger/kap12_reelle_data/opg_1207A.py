import pandas as pd
import numpy as np

filnavn = "brod.csv"
data = pd.read_csv(filnavn)
brod = data["antall brød"]
kostnader = data["kostnader"]

# Tallet 2 betyr at vi ønsker en andregradsmodell
a, b, c = np.polyfit(brod, kostnader, 2)

print("Andregradsmodellen k(x):")
print(f"a = {a:.5f}, b = {b:.5f}, c = {c:.2f}")
