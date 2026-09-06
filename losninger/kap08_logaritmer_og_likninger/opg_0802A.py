import numpy as np

lg = np.log10
print(f"{lg(10) = }")
print(f"{lg(100) + lg(10**3) = }")

# lg(0,01) = -2 og lg(1000**4) = lg(10**12) = 12. Til sammen blir det 10.
print(f"{lg(0.01) + lg(1000**4) = }")
