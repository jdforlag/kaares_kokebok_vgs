import numpy as np

def h(x):
    return 10 - np.e**x

def H(x):
    return 10*x - np.e**x

a = 2
b = 3
integral = H(b) - H(a)
print(f"Integralet fra 2 til 3 er {integral:.4f}")

# h synker, så integralet blir mer og mer negativt når b øker.
# Vi øker b til integralet har passert -100.
b = 2
while H(b) - H(a) >= -100:
    b += 0.001

print(f"Integralet blir mindre enn -100 når b er større enn {b:.3f}")
print(f"Kontroll: integralet fra 2 til {b:.3f} er {H(b) - H(a):.2f}")
