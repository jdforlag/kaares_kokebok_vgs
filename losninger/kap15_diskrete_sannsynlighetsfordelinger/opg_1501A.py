import numpy as np

verdier = [2, 4, 7]
sanns = [0.4, 0.1, 0.5]
verdi = np.random.choice(verdier, p=sanns)
print("Verdien er:", verdi)

if verdi > 2:
    print("Større enn 2.")
