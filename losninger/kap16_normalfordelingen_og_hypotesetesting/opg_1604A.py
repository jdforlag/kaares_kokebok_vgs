import matplotlib.pyplot as plt
import numpy as np

karakterer = np.random.normal(3.2, 0.8, size=200)

plt.hist(karakterer, bins=20, edgecolor="brown", alpha=0.6)
plt.xlabel("Karaktersnitt")
plt.ylabel("Antall elever")
plt.title("Karaktersnitt for 200 elever")
plt.show()
