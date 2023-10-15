import numpy as np

lg = np.log10
x = 10
vs = lg(x) + lg(2*x)

while vs < 4:
    x = x + 1
    vs = lg(x) + lg(2*x)

print(f"Løsning: x = {x}") 

eksakt_losning = 50 * np.sqrt(2)
differanse = abs(x - eksakt_losning)
print("Differansen mellom programløsning og eksakt løsning:", differanse)
