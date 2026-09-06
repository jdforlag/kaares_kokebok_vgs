import numpy as np

ln = np.log

x = 1

# Vi bytter ut steget 1 med 0,01. Da kommer vi mye nærmere den
# korrekte løsningen x = 12,0519.
while x*ln(x) < 30:
    x = x + 0.01

print(f"{x = }")
