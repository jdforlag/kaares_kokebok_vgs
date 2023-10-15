import numpy as np
import matplotlib.pyplot as plt

# Data for antall brød og tilhørende kostnader
brod = [50, 75, 100, 125, 150]
kostnader = [650, 780, 1000, 1150, 1400]

# Utfører lineær regresjon for å finne tilpasningsparametrene
a, b = np.polyfit(brod, kostnader, 1)

# Skriver ut regresjonskoeffisientene
print(f"a = {a:.2f}, b = {b:.2f}")

# Oppretter et sett med x-verdier for å tegne regresjonslinjen
x = np.linspace(0, 200, 100)  # 100 poeng fra 0 til 200

# Beregner de tilsvarende y-verdiene med regresjonsmodellen
f = a * x + b

# Tegner de opprinnelige dataene som punkter
plt.scatter(brod, kostnader, color='red', label='Reelle data')  # reelle data som punkter

# Tegner regresjonslinjen
plt.plot(x, f, color='blue', label=f'Lineær modell')

# Legger til ekstra informasjon til plottet
plt.title('Kostnadsanalyse for brødproduksjon')
plt.xlabel('Antall brød')
plt.ylabel('Kostnader (kroner)')
plt.legend()  # Viser boks med beskrivelser
plt.grid(True)

# Viser plottet
plt.show()
