import numpy as np

ln = np.log

x = float(input("x = "))

# ln er bare definert for positive tall, så vi må sjekke x først
if x > 0:
    print(f"{ln(x) = }")
else:
    print("Ugyldig verdi. Må ha x > 0")
