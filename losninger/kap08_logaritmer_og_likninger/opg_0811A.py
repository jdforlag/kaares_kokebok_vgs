import numpy as np

def pH(k):
    """pH-verdien til en løsning med H+-konsentrasjon k mol/L."""
    return -np.log10(k)

kons = 0.1
for i in range(14):
    print(pH(kons))
    kons = kons * 0.1
