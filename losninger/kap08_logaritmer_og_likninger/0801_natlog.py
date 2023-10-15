import numpy as np

e = np.e  # Eulers tall
ln = np.log  # Naturlig logaritme

print(f"{e = }")
print(f"{ln(e) = }")
print(f"{ln(e**3) = }")  # Resultatet her vil være 3 siden ln(e^3) = 3
print(f"{ln(e**6) = }")  # Resultatet her vil være 6 siden ln(e^6) = 6
print(f"{ln(e**(-2)) = }")  # Resultatet her vil være -2 siden ln(e^-2) = -2
print(f"{ln(e**(-9)) = }")  # Resultatet her vil være -9 siden ln(e^-9) = -9

# Følgende linje regner ut ln(15 + 3^5) - e^2
print(ln(15 + 3**5) - e**2)

# Følgende linje regner ut 2^3 - ln(e^4 + 50)
print(2**3 - ln(e**4 + 50))
