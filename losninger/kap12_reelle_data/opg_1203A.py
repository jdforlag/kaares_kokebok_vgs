import pandas as pd

filnavn = "treningsokter.txt"
data = pd.read_csv(filnavn)
for okt in data.okter:
    print(f"Denne uka gjennomførte du {okt} treningsøkter.")
