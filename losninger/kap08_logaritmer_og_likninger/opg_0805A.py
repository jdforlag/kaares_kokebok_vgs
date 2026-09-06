import numpy as np

lg = np.log10

# Vi utvider løkka til range(-2, 10) for at lg(10**9) skal bli det siste
for eksp in range(-2, 10):
    # Skriv ut tierlogaritmen til 10**eksp
    print(f"lg(10**{eksp}) = {lg(10**eksp)}")
