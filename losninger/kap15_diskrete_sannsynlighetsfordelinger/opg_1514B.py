import matplotlib.pyplot as plt
import numpy as np

p_verdier = np.arange(0, 1.01, 0.01)
n = 100
SD_verdier = [ ]

for p in p_verdier:
    # Regn ut SD_X med np.sqrt(n*p*(1-p))
    SD_X = np.sqrt(n*p*(1-p))
    # Legg til verdien i lista SD_verdier
    SD_verdier.append(SD_X)

# Plott p_verdier langs x-aksen og SD_verdier langs y-aksen
plt.plot(p_verdier, SD_verdier)
plt.xlabel("Sannsynligheten p")
plt.ylabel("SD(X)")
plt.title("Standardavviket når vi planter 100 frø")
plt.grid()
plt.show()

# Standardavviket er 0 når p er 0 eller 1, og størst når p = 0,5.
print(f"Det største standardavviket er {max(SD_verdier):.2f}")
