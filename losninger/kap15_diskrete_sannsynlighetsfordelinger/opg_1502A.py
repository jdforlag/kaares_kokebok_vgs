import numpy as np

verdier = [2, 4, 7]
sanns = [0.4, 0.1, 0.5]
E_X = 0
for i in range(len(verdier)):
    E_X += verdier[i] * sanns[i]

print(f"E(X) = {E_X}")
