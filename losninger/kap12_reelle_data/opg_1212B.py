import numpy as np
x_verdier = np.arange(0, 20)
y_verdier = np.random.binomial(500, 0.3, size=len(x_verdier))
for x, y in zip(x_verdier, y_verdier):
    print(f"x = {x}, y = {y}")

# Vi antar først at det første punktet er det minste
minste_x = x_verdier[0]
minste_y = y_verdier[0]

for x, y in zip(x_verdier, y_verdier):
    if y < minste_y:
        minste_y = y
        minste_x = x

print(f"Punktet med minst y-verdi er ({minste_x}, {minste_y}).")
