import numpy as np

# Lagrer numpy sin log10-funksjon i variabelen lg
lg = np.log10  

# Skriver ut logaritmen av noen tall
print(lg(100))
print(lg(10**4))

# Demonstrerer at 10^(lg(x)) gir tilbake x
print(10**(lg(0.5)))
print(10**(lg(23)))

print(f"{lg(3*4) = }")
print(f"lg(3) + lg(4) = {lg(3) + lg(4)}")  

for i in range(-3, 4):
    print(lg(10**i))
