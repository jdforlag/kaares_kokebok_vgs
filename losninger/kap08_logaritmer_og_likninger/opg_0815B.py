import numpy as np

lg = np.log10

def B(x):
    """Verdien av investeringen i kroner, x måneder etter kjøpet."""
    return 36_000 * lg((x+2)/2)

verdi18 = B(18)
print(f"Etter 18 måneder er investeringen verdt {verdi18:.0f} kr.")

# Hvor lenge tar det før verdien er dobbelt så stor som etter 18 måneder?
maaneder = 18
while B(maaneder) < 2*verdi18:
    maaneder += 1

print(f"Verdien er doblet etter {maaneder} måneder, altså {maaneder - 18}")
print(f"måneder etter at den var {verdi18:.0f} kr.")
