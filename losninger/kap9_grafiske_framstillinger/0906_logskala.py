import matplotlib.pyplot as plt
import numpy as np

# Definerer x-verdiene fra 0 til 200 (totalt 201 verdier)
x = np.linspace(0, 200, 201)

# Beregner innskuddsveksten for de forskjellige rentesatsene
f = 500 * 1.01**x  # 1 prosent rente
g = 500 * 1.02**x  # 2 prosent rente
h = 500 * 1.05**x  # 5 prosent rente

# Tegner grafene for hvert innskudd over tid
plt.plot(x, f, label="1 prosent rente")
plt.plot(x, g, label="2 prosent rente")
plt.plot(x, h, label="5 prosent rente")

# Setter logaritmisk skala for y-aksen
plt.yscale("log")

# Legger til etiketter og tittel
plt.xlabel("År")
plt.ylabel("Beløp (i kroner)")
plt.title("Vekst av innskudd over 200 år med forskjellige rentesatser")
plt.legend()  # Viser forklaringene

# Viser plottet
plt.show()
